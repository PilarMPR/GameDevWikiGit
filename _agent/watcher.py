"""Generic file watcher. GENERIC — copy unchanged into a new agent.

Reads config.watch_paths and dispatches to handlers.HANDLERS. Each watch-path entry is
keyed by a name that must exist in handlers.HANDLERS:

  "watch_paths": {
    "<name>": {"path": "...", "recursive": false, "on_modified": false}
  }

(A bare string value is also accepted and treated as {path, recursive=false, on_modified=false}.)

Modes:
  python watcher.py            start watching (blocks until SIGINT/SIGTERM)
  python watcher.py --dry-run  verify every watch path resolves, then exit
  python watcher.py --budget   print this month's estimated API spend, then exit
"""

from __future__ import annotations

import argparse
import signal
import sys
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import handlers
from common import CONFIG, get_logger, month_spend_usd, _month_key

logger = get_logger("watcher", "watcher.log")

DEBOUNCE_SECONDS = CONFIG.get("debounce_seconds", 3)
_stop_event = threading.Event()


def _spec(name: str, raw) -> dict:
    """Normalise a watch_paths entry to {path, recursive, on_modified}."""
    if isinstance(raw, str):
        raw = {"path": raw}
    return {
        "name": name,
        "path": Path(raw["path"]),
        "recursive": bool(raw.get("recursive", False)),
        "on_modified": bool(raw.get("on_modified", False)),
    }


def _specs() -> list[dict]:
    return [_spec(name, raw) for name, raw in CONFIG["watch_paths"].items()]


class _DebouncedHandler(FileSystemEventHandler):
    def __init__(self, name: str, handler_fn, on_modified_too: bool):
        self.name = name
        self.handler_fn = handler_fn
        self.on_modified_too = on_modified_too
        self._last_seen: dict[str, float] = {}
        self._lock = threading.Lock()

    def _should_handle(self, path: str) -> bool:
        if not path.lower().endswith(".md"):
            return False
        now = time.monotonic()
        with self._lock:
            if now - self._last_seen.get(path, 0.0) < DEBOUNCE_SECONDS:
                return False
            self._last_seen[path] = now
        return True

    def _dispatch(self, path: str) -> None:
        if not self._should_handle(path):
            return
        logger.info("[%s] triggered by %s", self.name, path)
        try:
            self.handler_fn(path)
        except Exception:  # noqa: BLE001 - a handler crash must not kill the watcher
            logger.exception("[%s] handler failed for %s", self.name, path)

    def on_created(self, event):
        if not event.is_directory:
            self._dispatch(event.src_path)

    def on_modified(self, event):
        if self.on_modified_too and not event.is_directory:
            self._dispatch(event.src_path)


def dry_run() -> int:
    ok = True
    print("Agent watcher - dry run")
    for spec in _specs():
        exists = spec["path"].is_dir()
        in_handlers = spec["name"] in handlers.HANDLERS
        ok = ok and exists and in_handlers
        flag = "OK " if (exists and in_handlers) else "FAIL"
        note = "" if in_handlers else "  <- no handler named this in handlers.HANDLERS"
        print(f"  [{flag}] {spec['name']:<12} -> {spec['path']}{note}")
    print("Ready to start." if ok else "Fix the FAIL rows above before starting.")
    return 0 if ok else 1


def _handle_signal(signum, _frame):
    logger.info("Received signal %s - shutting down.", signum)
    _stop_event.set()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generic agent file watcher")
    parser.add_argument("--dry-run", action="store_true", help="verify paths/handlers and exit")
    parser.add_argument("--budget", action="store_true", help="show this month's API spend and exit")
    args = parser.parse_args()

    if args.budget:
        budget = CONFIG.get("monthly_budget_usd")
        cap = f"${budget:.2f}" if budget is not None else "(no cap set)"
        print(f"API spend {_month_key()}: ${month_spend_usd():.4f} of {cap}")
        return 0

    if args.dry_run:
        return dry_run()

    specs = _specs()
    problems = [s["name"] for s in specs if not s["path"].is_dir() or s["name"] not in handlers.HANDLERS]
    if problems:
        logger.error("Cannot start - bad watch specs: %s (run --dry-run)", ", ".join(problems))
        return 1

    observer = Observer()
    for spec in specs:
        observer.schedule(
            _DebouncedHandler(spec["name"], handlers.HANDLERS[spec["name"]], spec["on_modified"]),
            str(spec["path"]),
            recursive=spec["recursive"],
        )

    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    observer.start()
    logger.info("Watcher started (%s). Active paths:", CONFIG.get("agent_name", "agent"))
    print(f"{CONFIG.get('agent_name', 'agent')} watcher running. Watching:")
    for spec in specs:
        logger.info("  - %-12s %s (recursive=%s)", spec["name"], spec["path"], spec["recursive"])
        print(f"  - {spec['name']:<12} {spec['path']}")
    print("Press Ctrl+C to stop.")

    try:
        while not _stop_event.is_set():
            time.sleep(0.5)
    finally:
        observer.stop()
        observer.join()
        logger.info("Watcher stopped cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
