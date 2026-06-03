#!/usr/bin/env python3
"""Convert Obsidian [[wikilinks]] into GitHub-friendly relative Markdown links.

Why: GitHub does not render [[wikilinks]] as clickable links in the repo file
browser. Standard Markdown links `[text](path.md)` work in BOTH Obsidian and
GitHub, so converting in place keeps the vault usable in Obsidian while making
it navigable on GitHub.

The script is idempotent: it only touches `[[...]]` patterns and leaves any
already-converted `[text](path.md)` links alone. Re-run it whenever new
wikilinks are generated. Unresolvable links are left as `[[...]]` (and reported)
so breakage stays visible rather than being silently hidden.
"""

import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories excluded as BOTH link sources and link targets.
SKIP_DIRS = {".git", ".obsidian", ".claude", "_agent", "_meta", "_tools", "_ARCHIVE"}

WIKILINK = re.compile(r"(?<!\!)\[\[([^\]]+?)\]\]")
FENCE = re.compile(r"^\s*(```|~~~)")


def is_skipped(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    return any(part in SKIP_DIRS for part in parts[:-1]) or parts[0] in SKIP_DIRS


def collect_md_files():
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                abs_path = os.path.join(dirpath, name)
                rel = os.path.relpath(abs_path, ROOT)
                if not is_skipped(rel):
                    files.append(abs_path)
    return files


def build_basename_index(files):
    """Map lowercased basename (no extension) -> list of absolute paths."""
    index = {}
    for f in files:
        key = os.path.splitext(os.path.basename(f))[0].lower()
        index.setdefault(key, []).append(f)
    return index


def slugify_anchor(heading):
    h = heading.strip().lower()
    h = h.replace(" ", "-")
    h = re.sub(r"[^a-z0-9\-_]", "", h)
    return h


def encode_relpath(relpath):
    relpath = relpath.replace("\\", "/")
    return urllib.parse.quote(relpath, safe="/-._~")


# Legacy structure recovery: the vault was rebuilt from a flat `wiki/concepts/`
# layout into atomic notes whose slugs gained a descriptive suffix. Old links
# like [[mda-framework]] now point at `mda-framework-overview`. These suffixes
# let path-stale links resolve, but only when the guess is UNIQUE (see below).
LEGACY_SUFFIXES = (
    "-definition", "-overview", "-synthesis", "-design", "-systems",
    "-system", "-principles", "-models", "-and-games", "-methods", "-foundation",
)

# Explicit redirects for old slugs whose note exists under a non-derivable name
# (the suffix heuristic can't reach these). Maps old basename -> current basename.
LEGACY_ALIASES = {
    "core-mechanics": "mechanics-definition",
    "player-psychology": "player-psychology-perception",
    "puzzles": "puzzle-design-principles",
    "feedback-systems": "feedback-system-design",
    "game-feel-3cs": "game-feel-definition",
    "game-loop-timescales": "game-loops-definition",
    "indirect-control-tools": "indirect-control-methods",
    "input-and-controls": "input-controls-design",
    "motivation": "player-motivation-maslow",
    "player-psychology-motivation": "player-motivation-maslow",
    "player-types": "bartle-four-types",
    "play-and-culture": "play-and-culture-huizinga",
    "story-and-games": "story-narrative-approaches",
    "story-narrative-games": "story-narrative-approaches",
    "systems-thinking": "game-as-system",
    "theory-of-fun": "fun-as-learning-koster",
    "theory-of-fun-koster": "fun-as-learning-koster",
    "free-to-play-design": "f2p-design-foundation",
    "fun-as-engagement-sellers": "fun-engagement-debate",
    "multiplayer-systems": "multiplayer-conflict-types",
    "pacing-and-flow": "tense-and-release",
    "game-balance-skill-vs-chance": "game-balance-methods",
    "game-balance-simple-vs-complex": "game-balance-methods",
    "game-balance-types-schell": "game-balance-overview",
}


def _index_lookup(key, basename_index, source_dir, allow_ambiguous):
    matches = basename_index.get(key)
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]
    if not allow_ambiguous:
        return None
    # Ambiguous: prefer the closest file by path distance to the source.
    return sorted(matches, key=lambda m: (
        os.path.relpath(m, source_dir).count(".."),
        len(os.path.relpath(m, source_dir)),
    ))[0]


def resolve_target(target, source_abs, basename_index):
    """Return absolute path of the target file, or None if unresolvable."""
    source_dir = os.path.dirname(source_abs)

    if target.endswith(".canvas"):
        candidate = os.path.normpath(os.path.join(source_dir, target))
        return candidate if os.path.isfile(candidate) else None
    if target.endswith(".md"):
        target = target[:-3]

    is_path = "/" in target or target.startswith("..")

    # 1. Exact relative path (well-formed path-style links).
    if is_path:
        candidate = os.path.normpath(os.path.join(source_dir, target + ".md"))
        if os.path.isfile(candidate):
            return candidate
        # Path no longer exists (vault was restructured) -> fall through to
        # basename-based recovery, but require a UNIQUE match to stay safe.

    base = os.path.basename(target.rstrip("/")).lower()

    # 2. Basename lookup. Bare links may use distance to disambiguate; recovered
    #    path links must be unambiguous.
    hit = _index_lookup(base, basename_index, source_dir, allow_ambiguous=not is_path)
    if hit:
        return hit

    # 3. Explicit legacy alias (authoritative, unique match only).
    if base in LEGACY_ALIASES:
        hit = _index_lookup(LEGACY_ALIASES[base], basename_index, source_dir, allow_ambiguous=False)
        if hit:
            return hit

    # 4. Legacy suffix recovery (unique matches only).
    for suffix in LEGACY_SUFFIXES:
        hit = _index_lookup(base + suffix, basename_index, source_dir, allow_ambiguous=False)
        if hit:
            return hit

    # 4. Plural -> singular fallback (unique matches only).
    if base.endswith("s"):
        hit = _index_lookup(base[:-1], basename_index, source_dir, allow_ambiguous=False)
        if hit:
            return hit

    return None


def convert_file(abs_path, basename_index, stats):
    with open(abs_path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    in_fence = False
    changed = False
    out = []

    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence or "[[" not in line:
            out.append(line)
            continue

        def repl(match):
            nonlocal changed
            raw = match.group(1)

            alias = None
            if "|" in raw:
                target_part, alias = raw.split("|", 1)
            else:
                target_part = raw

            heading = None
            if "#" in target_part:
                target, heading = target_part.split("#", 1)
            else:
                target = target_part

            target = target.strip()
            resolved = resolve_target(target, abs_path, basename_index)
            if resolved is None:
                stats["unresolved"].append((os.path.relpath(abs_path, ROOT), raw))
                return match.group(0)

            display = alias.strip() if alias else os.path.splitext(os.path.basename(target))[0]
            rel = os.path.relpath(resolved, os.path.dirname(abs_path))
            href = encode_relpath(rel)
            if heading:
                href += "#" + slugify_anchor(heading)

            changed = True
            stats["converted"] += 1
            return f"[{display}]({href})"

        out.append(WIKILINK.sub(repl, line))

    if changed:
        with open(abs_path, "w", encoding="utf-8", newline="") as fh:
            fh.writelines(out)
        stats["files_changed"] += 1


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    files = collect_md_files()
    basename_index = build_basename_index(files)
    stats = {"converted": 0, "files_changed": 0, "unresolved": []}

    for f in files:
        convert_file(f, basename_index, stats)

    print(f"Processed {len(files)} Markdown files.")
    print(f"Converted {stats['converted']} wikilinks across {stats['files_changed']} files.")

    if stats["unresolved"]:
        print(f"\n{len(stats['unresolved'])} wikilinks could not be resolved (left as [[...]]):")
        shown = {}
        for src, raw in stats["unresolved"]:
            shown.setdefault(src, []).append(raw)
        for src in sorted(shown)[:40]:
            for raw in shown[src][:5]:
                print(f"  {src}: [[{raw}]]")
    else:
        print("All wikilinks resolved.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
