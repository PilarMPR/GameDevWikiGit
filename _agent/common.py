"""Reusable agent engine: config, logging, budget-guarded Claude calls, markdown helpers.

This file is GENERIC — copy it into a new agent unchanged. Per-agent behaviour lives in
handlers.py; per-agent settings live in config.json. Imported by watcher.py, handlers.py,
git_helper.py and any review/build scripts.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import frontmatter
from anthropic import Anthropic

AGENT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = AGENT_DIR / "config.json"
LOG_DIR = AGENT_DIR / "logs"

_client: Anthropic | None = None


def load_config() -> dict:
    """Load and validate config.json. Raises if a required key is missing."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
        cfg = json.load(fh)
    required = ["vault_path", "model", "max_tokens", "watch_paths",
                "git_auto_commit", "git_commit_prefix"]
    missing = [k for k in required if k not in cfg]
    if missing:
        raise KeyError(f"config.json missing keys: {', '.join(missing)}")
    return cfg


CONFIG = load_config()


def get_logger(name: str, filename: str) -> logging.Logger:
    """Logger that writes timestamped lines to logs/<filename> and stderr."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fh = logging.FileHandler(LOG_DIR / filename, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    sh = logging.StreamHandler(sys.stderr)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
    return logger


# --------------------------------------------------------------------------- #
# Claude API + soft monthly budget
# --------------------------------------------------------------------------- #

class BudgetExceeded(RuntimeError):
    """Raised when the self-tracked monthly budget is reached. SOFT cap (estimated from
    token usage) — the hard cap is the spend limit set in the Anthropic Console."""


USAGE_PATH = AGENT_DIR / "logs" / "usage.json"


def _get_client() -> Anthropic:
    global _client
    if _client is None:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError("ANTHROPIC_API_KEY is not set in the environment.")
        _client = Anthropic()
    return _client


def _month_key() -> str:
    return datetime.now().strftime("%Y-%m")


def _load_usage() -> dict:
    if USAGE_PATH.exists():
        try:
            return json.loads(USAGE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def month_spend_usd() -> float:
    return float(_load_usage().get(_month_key(), {}).get("cost_usd", 0.0))


def _call_cost(input_tokens: int, output_tokens: int) -> float:
    pricing = CONFIG.get("pricing", {})
    return ((input_tokens / 1_000_000) * pricing.get("input_per_mtok", 3.0)
            + (output_tokens / 1_000_000) * pricing.get("output_per_mtok", 15.0))


def _record_usage(input_tokens: int, output_tokens: int, cost_usd: float) -> None:
    usage = _load_usage()
    month = _month_key()
    entry = usage.get(month, {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "calls": 0})
    entry["input_tokens"] += int(input_tokens)
    entry["output_tokens"] += int(output_tokens)
    entry["cost_usd"] = round(entry["cost_usd"] + cost_usd, 6)
    entry["calls"] += 1
    usage[month] = entry
    USAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    USAGE_PATH.write_text(json.dumps(usage, indent=2), encoding="utf-8")


def call_claude(system: str, user: str) -> str:
    """Single entry point for every Claude API call. Enforces the soft monthly budget
    before calling and records estimated cost from the response afterwards."""
    budget = CONFIG.get("monthly_budget_usd")
    if budget is not None and month_spend_usd() >= budget:
        raise BudgetExceeded(
            f"Monthly API budget reached: ${month_spend_usd():.2f} of ${budget:.2f} "
            f"for {_month_key()}. Call skipped. Raise monthly_budget_usd in config.json."
        )
    client = _get_client()
    resp = client.messages.create(
        model=CONFIG["model"],
        max_tokens=CONFIG["max_tokens"],
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    usage = getattr(resp, "usage", None)
    if usage is not None:
        in_tok = getattr(usage, "input_tokens", 0) or 0
        out_tok = getattr(usage, "output_tokens", 0) or 0
        _record_usage(in_tok, out_tok, _call_cost(in_tok, out_tok))
    parts = [b.text for b in resp.content if getattr(b, "type", None) == "text"]
    return "".join(parts).strip()


def safe_call(logger, label: str, system: str, user: str) -> str | None:
    """call_claude wrapper that logs API/budget failures and returns None instead of
    raising — so one failed AI step never aborts a handler's other bookkeeping."""
    try:
        return call_claude(system, user)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Claude call failed (%s); skipping AI step: %s", label, exc)
        return None


WEB_SEARCH_MAX_USES = 5


def call_claude_with_search(system: str, user: str) -> str:
    """Claude call with Anthropic's built-in web_search_20250305 tool enabled.
    Same budget guard and usage recording as call_claude. Use for weekly
    discovery sweeps; prefer call_claude for deterministic RSS processing."""
    budget = CONFIG.get("monthly_budget_usd")
    if budget is not None and month_spend_usd() >= budget:
        raise BudgetExceeded(
            f"Monthly API budget reached: ${month_spend_usd():.2f} of ${budget:.2f} "
            f"for {_month_key()}. Raise monthly_budget_usd in config.json."
        )
    client = _get_client()
    resp = client.messages.create(
        model=CONFIG["model"],
        max_tokens=CONFIG["max_tokens"],
        tools=[{"type": "web_search_20250305", "name": "web_search",
                "max_uses": WEB_SEARCH_MAX_USES}],
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    usage = getattr(resp, "usage", None)
    if usage is not None:
        in_tok = getattr(usage, "input_tokens", 0) or 0
        out_tok = getattr(usage, "output_tokens", 0) or 0
        _record_usage(in_tok, out_tok, _call_cost(in_tok, out_tok))
    parts = [b.text for b in resp.content if getattr(b, "type", None) == "text"]
    return "".join(parts).strip()


def safe_call_with_search(logger, label: str, system: str, user: str) -> str | None:
    """call_claude_with_search wrapped with the same error-logging as safe_call."""
    try:
        return call_claude_with_search(system, user)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Claude web-search call failed (%s): %s", label, exc)
        return None


# --------------------------------------------------------------------------- #
# Markdown helpers
# --------------------------------------------------------------------------- #

def read_post(filepath: str | Path) -> frontmatter.Post:
    with open(filepath, "r", encoding="utf-8") as fh:
        return frontmatter.load(fh)


def extract_section(content: str, header: str) -> str:
    """Body of a markdown section (header matched at line start) until the next header of
    the same or higher level, or EOF. Empty string if absent."""
    level = len(header.split(" ", 1)[0])
    match = re.compile(rf"^{re.escape(header)}\s*$", re.MULTILINE).search(content)
    if not match:
        return ""
    start = match.end()
    stop = re.compile(rf"^#{{1,{level}}}\s+\S", re.MULTILINE).search(content, start)
    return content[start:(stop.start() if stop else len(content))].strip()


def append_to_file(filepath: str | Path, text: str) -> None:
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = text.strip()
    if not body:
        return
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    sep = "" if existing == "" or existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"{sep}{body}\n")


def append_to_section(filepath: str | Path, header: str, text: str) -> None:
    """Insert text at the end of the named section, creating the section if absent."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = text.strip()
    if not body:
        return
    content = path.read_text(encoding="utf-8") if path.exists() else ""
    level = len(header.split(" ", 1)[0])
    match = re.compile(rf"^{re.escape(header)}\s*$", re.MULTILINE).search(content)
    if not match:
        prefix = "" if content == "" or content.endswith("\n\n") else ("\n" if content.endswith("\n") else "\n\n")
        path.write_text(f"{content}{prefix}{header}\n\n{body}\n", encoding="utf-8")
        return
    start = match.end()
    stop = re.compile(rf"^#{{1,{level}}}\s+\S", re.MULTILINE).search(content, start)
    insert_at = stop.start() if stop else len(content)
    before = content[:insert_at].rstrip("\n")
    after = content[insert_at:]
    path.write_text(f"{before}\n\n{body}\n\n{after.lstrip(chr(10))}" if after else f"{before}\n\n{body}\n",
                    encoding="utf-8")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
