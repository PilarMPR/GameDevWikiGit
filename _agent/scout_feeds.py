"""Shared discovery engine for GameDevWiki scout agents.

Provides: config loading, once-per-day and once-per-ISO-week run guards,
RSS/Atom feed fetching via feedparser, and a URL-dedupe ledger (seen.json).
Imported by scout_daily.py and hp_scout_daily.py.

Claude calls stay in common.py — this module is pure discovery, no AI.
"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

import feedparser
import requests

AGENT_DIR = Path(__file__).resolve().parent

_FEED_TIMEOUT_SECS = 15
_FEED_HEADERS = {"User-Agent": "GameDevWiki-Scout/1.0 (research bot)"}


# ---- config ---------------------------------------------------------------- #

def loadScoutConfig(configPath: str | Path) -> dict:
    path = Path(configPath)
    if not path.exists():
        raise FileNotFoundError(f"Scout config not found: {path}")
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


# ---- daily guard ----------------------------------------------------------- #

def _stampPath(stateDir: Path, agentName: str, kind: str) -> Path:
    return stateDir / f"state_{agentName}_{kind}.json"


def hasRunToday(stateDir: Path, agentName: str) -> bool:
    """True if the agent already completed a run today."""
    path = _stampPath(stateDir, agentName, "daily")
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8")).get("last_run") == date.today().isoformat()
        except (json.JSONDecodeError, KeyError):
            pass
    return False


def markDailyDone(stateDir: Path, agentName: str) -> None:
    """Record that today's run finished. Call after writing the inbox note."""
    stateDir.mkdir(parents=True, exist_ok=True)
    _stampPath(stateDir, agentName, "daily").write_text(
        json.dumps({"last_run": date.today().isoformat()}), encoding="utf-8"
    )


# ---- weekly guard ---------------------------------------------------------- #

def _isoWeekKey() -> str:
    now = datetime.now().isocalendar()
    return f"{now.year}-W{now.week:02d}"


def checkWeekly(stateDir: Path, agentName: str) -> bool:
    """True if the web-search sweep has NOT yet run this ISO week."""
    path = _stampPath(stateDir, agentName, "weekly")
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8")).get("last_week") != _isoWeekKey()
        except (json.JSONDecodeError, KeyError):
            pass
    return True


def markWeeklyDone(stateDir: Path, agentName: str) -> None:
    """Record that this week's web-search sweep succeeded."""
    stateDir.mkdir(parents=True, exist_ok=True)
    _stampPath(stateDir, agentName, "weekly").write_text(
        json.dumps({"last_week": _isoWeekKey()}), encoding="utf-8"
    )


# ---- feed fetching --------------------------------------------------------- #

def fetchFeeds(feedUrls: list[str]) -> list[dict[str, str]]:
    """Fetch RSS/Atom feeds and return a flat list of {title, link, summary}.

    Tries requests first (better timeout control) then falls back to
    feedparser's built-in HTTP client. Silently skips feeds that fail.
    """
    items: list[dict[str, str]] = []
    for url in feedUrls:
        feed = None
        try:
            resp = requests.get(url, timeout=_FEED_TIMEOUT_SECS, headers=_FEED_HEADERS)
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
        except Exception:
            try:
                feed = feedparser.parse(url)
            except Exception:
                continue
        for entry in getattr(feed, "entries", []):
            link = entry.get("link", "")
            if not link:
                continue
            items.append({
                "title": entry.get("title", "(no title)"),
                "link": link,
                "summary": entry.get("summary", ""),
            })
    return items


# ---- URL dedupe ledger ----------------------------------------------------- #

def loadSeen(seenPath: Path) -> set[str]:
    if seenPath.exists():
        try:
            return set(json.loads(seenPath.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, TypeError):
            pass
    return set()


def saveSeen(seenPath: Path, seen: set[str]) -> None:
    seenPath.parent.mkdir(parents=True, exist_ok=True)
    seenPath.write_text(json.dumps(sorted(seen), indent=2), encoding="utf-8")


def dedupeItems(
    items: list[dict[str, str]], seen: set[str]
) -> tuple[list[dict[str, str]], set[str]]:
    """Return (new_items_not_in_seen, updated_seen_including_new_items)."""
    updated = set(seen)
    newItems = []
    for item in items:
        if item["link"] not in updated:
            newItems.append(item)
            updated.add(item["link"])
    return newItems, updated
