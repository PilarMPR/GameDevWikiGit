"""Git auto-commit helper. GENERIC — copy unchanged into a new agent.

Commits happen inside the vault repo (config.vault_path) with the conventional-commit
prefix from config.json. The repo is initialised on first use. Files outside the vault
work-tree are edited but skip auto-commit (git can't stage them). Pushing never forces.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from common import CONFIG, get_logger

logger = get_logger("git_helper", "git_helper.log")

VAULT = Path(CONFIG["vault_path"])
PREFIX = CONFIG["git_commit_prefix"]


class GitError(RuntimeError):
    pass


def _run(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(["git", *args], cwd=str(VAULT), capture_output=True, text=True)
    if check and result.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def _ensure_repo() -> None:
    if (VAULT / ".git").exists():
        return
    VAULT.mkdir(parents=True, exist_ok=True)
    _run(["init"])
    if not _run(["config", "user.email"], check=False).stdout.strip():
        _run(["config", "user.email", "agent@localhost"])
    if not _run(["config", "user.name"], check=False).stdout.strip():
        _run(["config", "user.name", "Agent"])
    logger.info("Initialised git repo at %s", VAULT)


def _prefixed(message: str) -> str:
    return message if message.startswith(PREFIX) else f"{PREFIX} {message}"


def _in_vault(filepath: str | Path) -> bool:
    try:
        Path(filepath).resolve().relative_to(VAULT.resolve())
        return True
    except ValueError:
        return False


def _rel(filepath: str | Path) -> str:
    return str(Path(filepath).resolve().relative_to(VAULT.resolve()))


def get_diff(filepath: str | Path) -> str:
    _ensure_repo()
    if not _in_vault(filepath):
        return ""
    rel = _rel(filepath)
    return (_run(["diff", "--cached", "--", rel], check=False).stdout
            + _run(["diff", "--", rel], check=False).stdout).strip()


def commit_file(filepath: str | Path, message: str) -> str | None:
    return commit_multiple([filepath], message)


def commit_multiple(filepaths: list[str | Path], message: str) -> str | None:
    if not CONFIG.get("git_auto_commit", True):
        logger.info("git_auto_commit disabled; skipping commit: %s", message)
        return None
    _ensure_repo()
    rels = []
    for fp in filepaths:
        if not Path(fp).exists():
            logger.warning("Skipping missing file for commit: %s", fp)
            continue
        if not _in_vault(fp):
            logger.warning("Skipping auto-commit (outside vault repo): %s", fp)
            continue
        rels.append(_rel(fp))
    if not rels:
        logger.info("Nothing inside the vault to commit for: %s", message)
        return None
    _run(["add", "--", *rels])
    if _run(["diff", "--cached", "--quiet"], check=False).returncode == 0:
        logger.info("No changes staged; skipping commit: %s", message)
        return None
    _run(["commit", "-m", _prefixed(message)])
    sha = _run(["rev-parse", "HEAD"]).stdout.strip()
    logger.info("Committed %s -> %s", _prefixed(message), sha[:8])
    return sha


def push(remote: str = "origin", branch: str | None = None) -> None:
    """Push without ever forcing. Raises GitError if rejected."""
    _ensure_repo()
    if not _run(["remote"], check=False).stdout.strip():
        raise GitError("No git remote configured; nothing to push.")
    if branch is None:
        branch = _run(["rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    result = _run(["push", remote, branch], check=False)
    if result.returncode != 0:
        err = result.stderr.lower()
        if "non-fast-forward" in err or "rejected" in err or "fetch first" in err:
            raise GitError("Push rejected (would require force). Refusing to force push.")
        raise GitError(f"git push failed: {result.stderr.strip()}")
    logger.info("Pushed %s to %s/%s", branch, remote, branch)
