# Alexandria — Operating Manual

**What this is:** An LLM-maintained game-design research library. P sources material; Claude does all writing. This file is the operating manual for the current (Alexandria) structure.

**Vault root:** `D:\GameDevWiki` (or `$GAMEDEVWIKI_ROOT` if set)

---

## Architecture

```
GameDevWiki/
├── 00-Atlas/        → navigational layer (MOCs only — no content)
├── 10-Library/
│   ├── sources/     → 17 source cards (sNNN-slug.md)
│   └── notes/       → ATOMIC NOTES — flat, one idea each
├── 20-Reference/    → curated Dataview views (no prose duplication)
├── 30-Analyses/     → game teardowns and genre analyses
├── 40-HotPotato/    → active project workspace
├── 50-Feed/         → online intake (RSS → promote to notes)
├── _meta/           → operating manual, log, index, dashboard, templates
├── _ARCHIVE/        → everything moved/retired (never deleted)
├── raw/             → source PDFs (git-ignored, never committed)
├── _work/           → scratch text dumps (git-ignored)
├── _agent/          → automation scripts (config uses $GAMEDEVWIKI_ROOT)
└── _tools/          → book.py (PDF extraction)
```

---

## The four layers

- **Layer 0:** `raw/` — immutable source PDFs (never modified, never committed)
- **Layer 1:** `10-Library/sources/` — one card per source (sNNN), with Dataview index
- **Layer 2:** `10-Library/notes/` — all atomic notes, flat, discoverable by MOC + tag
- **Layer 3:** `00-Atlas/` (navigational) + `_meta/log.md` + `_meta/index.md`

---

## Atomic note schema

```yaml
---
id: stable-slug
title: Human Title
type: atomic         # atomic | entity
disciplines: [mechanics, theory]   # 1+ from the 11 disciplines
sources: [s005, s011]
lens: 21             # optional — Schell lens number
hp: true             # true if relevant to Hot Potato
tags: [concept]
status: seed | grown | evergreen
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Title

2–6 sentence statement of the single idea, fully cited (sNNN, ch.X).

## Detail
- key points, cited

## Connections
- [[related-slug]] — one-line relationship

## Appears in
- [[../sources/sNNN-slug]] · ch.X
```

**Atomic = one idea.** If a note can answer two different "what is X?" questions, split it. Split notes, never merge.

---

## Source card schema

```yaml
---
id: sNNN
title: Full Title
author: Author
year: YYYY
type: book | paper | article
status: ingested | partial | wishlist
hp_relevance: high | medium | low
tags: [source]
---
```

Includes: TL;DR (2–3 sentences), provenance caveats, and a Dataview block listing atomic notes from this source.

---

## Operations

### Query
1. Read `_meta/index.md` (Dataview-driven) to locate relevant notes.
2. Navigate via `00-Atlas/` MOCs or direct search by `id` slug.
3. Read the atomic notes; synthesize with citations. Offer to file new knowledge back as a note.
4. Log the query in `_meta/log.md`.

### Add a note
1. Create `10-Library/notes/<slug>.md` using the atomic note schema.
2. Add connections to related notes.
3. Update the relevant source card (if applicable — the Dataview auto-updates).
4. Add to `_meta/log.md`.

### Lint
Look for: orphaned notes (no connections), empty source cards (Dataview returns 0 notes), missing `disciplines` or `sources` fields, missing `## Connections` sections, flat files that should be split.

### Feed → note promotion
When a feed item in `50-Feed/` contains genuine library value:
1. Create a source card if it's a new source (`type: article`).
2. Write an atomic note in `10-Library/notes/` drawing on the feed item.
3. Add a backlink from the feed item: `Promoted to: [[../10-Library/notes/slug]]`.
4. Set `promoted: true` in the feed item's frontmatter.

---

## Hot Potato — Four Functions

1. **Library references:** `40-HotPotato/_index.md` has a live Dataview query (`WHERE hp = true`). Tag library notes `hp: true` when relevant to HP design.
2. **Decisions log:** `40-HotPotato/decisions.md` is append-only. Every entry ends with `**Basis:** (sNNN) [[atomic-note-slug]], [[other-note]]`. When an open question resolves, move it to decisions with its basis.
3. **Scratchpad → GDD:** `40-HotPotato/scratchpad/` holds raw mechanics/inspiration. Promotable: a confirmed idea graduates to `40-HotPotato/gdd/` or to a `10-Library/notes/` atomic note.
4. **Prompt library:** `40-HotPotato/prompts/` stores reusable Claude prompts (frontmatter: `task:`, `rating:`, `status:`).

---

## Disciplines (the 11 valid values for `disciplines:` field)

`mechanics` · `feel-and-controls` · `player` · `narrative` · `level-design` · `production` · `programming` · `art-tech` · `theory` · `interface` · `business`

---

## Conventions

- Citations: inline source IDs on every factual claim: `(s005, ch.10)`, `(s011)`.
- Contradictions: `> ⚠️ Contradiction:` callout; never silently overwrite — preserve both positions with their sources.
- Links: Obsidian `[[wikilinks]]`. A link to a not-yet-created note is a valid TODO.
- Dates: absolute `YYYY-MM-DD`.
- Status: `seed` (brief/stub) → `grown` (substantial) → `evergreen` (comprehensive and stable).

---

## Tooling

### PDF extraction (book.py)
```bash
PYTHONIOENCODING=utf-8 python _tools/book.py full sNNN   # full text
PYTHONIOENCODING=utf-8 python _tools/book.py slice sNNN A B > _work/cur.txt
```
**Windows gotcha:** must prefix `PYTHONIOENCODING=utf-8` to avoid UnicodeEncodeError on smart quotes.
**Encryption:** all PDFs are AES-encrypted with empty password — `book.py` handles decryption automatically via `pypdf` + `cryptography`.

### Agent scripts
Located in `_agent/`. Paths are relative via `$GAMEDEVWIKI_ROOT` (defaults to `.`). Set `GAMEDEVWIKI_ROOT=D:/GameDevWiki` in your environment for consistency.

---

## Deep-ingest status

Chapter-by-chapter extraction is paused. Resume point: s005 ch.11/33. Order when resumed: s005 → s013 → s006 → s001 → s008 → rest. Ledger: `_PROGRESS.md`.

---

## Golden rules

1. **Zero content loss.** Anything that doesn't fit goes to `_ARCHIVE/`, not deleted.
2. **Preserve every citation.** Citations travel with the claims they support, always.
3. **Faithful, not inventive.** Migrate and re-link existing prose. Do not fabricate claims.
4. **Atomic = one idea.** One note, one question answerable by it.
5. **Never commit raw/.** PDFs, `_work/`, and `.smtcmp_*` are git-ignored.
