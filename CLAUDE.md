# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Game Dev Wiki — Research Deep-Dive

This directory is an **LLM-maintained game-development research wiki**. It is a persistent, compounding
knowledge base: instead of re-deriving knowledge from raw documents on every question,
the LLM reads each new source once, integrates it into the wiki, and keeps the wiki
current. The wiki — not the raw sources — is the thing you read and reason from.

**Roles.** The human (P) sources material, explores, and asks questions. The LLM (you)
does ALL the writing: summarizing, cross-referencing, filing, and bookkeeping. P never
writes wiki pages by hand; you maintain every page in the numbered vault folders below.

**Subagent.** A dedicated `gamedevwiki-curator` subagent is defined in `.claude/agents/`.
Use it (or invoke it automatically) for any wiki content task.

## Topic / thesis

> **TOPIC:** Game development — engines, design, graphics/audio, tooling, production,
> and the craft of building games. (Narrow this to a sub-focus anytime you like.)
>
> **WORKING THESIS:** Game design is a young but coherent discipline whose canon converges
> on a few load-bearing ideas — games are **rule-based systems** that produce **experience**
> through the **player's interaction**, and good design is the **iterative, player-centered**
> craft of shaping that experience — while genuinely disagreeing about the vocabulary for
> "fun" and how much to formalize the process. (Full version + tensions in
> `_agent/thesis.md`.)

## Vault structure

The vault uses a numbered Obsidian layout. You own every folder listed here (write freely):

| Folder | Purpose |
|--------|---------|
| `00-Atlas/` | Cross-book concept bridges (`bridges/`) and discipline entry points (`disciplines/`) |
| `05-Syntheses/` | Multi-source synthesis pages — the "big picture" layer |
| `10-Library/` | Atomic notes (`notes/`) + source summary pages (`sources/`) |
| `20-Reference/` | Quick-reference sheets (Schell Lenses, mechanics, theory, etc.) |
| `30-Analyses/` | Published-game analyses (`games/`) + genre design guides (`genres/`) |
| `40-HotPotato/` | Hot Potato workspace: GDD pages (`gdd/`), decisions log, scratchpad, boards |
| `_agent/` | Automated agent scripts and their output (`out/`); also holds `thesis.md`, `index.md`, `log.md` |
| `_ARCHIVE/` | **Read-only.** Old wiki/ structure before the numbered reorganization |
| `_tools/` | PDF extraction tooling (`book.py`, `map_sNNN.json` files) |
| `_work/` | Temp text dumps (e.g. `sNNN.full.txt`, `cur.txt`) — safe to delete |

**Root files:**
- `index.md` — content catalog. Every page, with a one-line summary. Read this FIRST when answering a query.
- `log.md` — chronological, append-only record of ingests/queries/lints.
- `_PROGRESS.md` — deep-ingest resume ledger. Read this FIRST every deep-ingest session.

**HotPotato conventions:** GDD pages use `gdd-*.md` prefix. Decisions are appended to `40-HotPotato/decisions.md` (never deleted). Open questions move to decisions when resolved. Playtest files go in `40-HotPotato/playtests/YYYY-MM-DD-context.md`. Reference the theory wiki with relative `[[../05-Syntheses/...]]` or `[[../10-Library/...]]` links.

Source IDs (`s001`–`s017`) are stable across all layers. Source PDFs are AES-encrypted; extract with `_tools/book.py` (see Tooling below).

## Conventions

- **Links.** Cross-reference liberally with Obsidian-compatible `[[relative/path]]` links. A link to a page that doesn't exist yet is fine — it's a TODO marking a page worth creating.
- **Citations.** Every factual claim in the wiki cites its source id(s) inline, e.g. `(s003)` or `(s001, s004)`. This is what lets us trace and audit knowledge.
- **Contradictions.** When a new source contradicts an existing claim, do NOT silently overwrite. Flag it: keep both, note which source says what, and add a `> ⚠️ Contradiction:` callout. Surface it to P.
- **Provenance over prose.** Prefer precise, cited, skimmable notes over flowing essays. Bullet points and short sections beat paragraphs.
- **Dates.** Use absolute dates (YYYY-MM-DD), never "last week".

## Operations

### Ingest (P provides a new source and asks to process it)
1. Assign the next source id. Read the source fully.
2. Discuss key takeaways with P before writing (unless told to batch silently).
3. Write `10-Library/sources/sNNN-<slug>.md`: metadata (id, title, author, date, type, link), a structured summary, key claims (each citable), and links to related wiki pages.
4. Update/create relevant `10-Library/notes/` and `05-Syntheses/` pages — fold the new claims in, adding citations and flagging contradictions.
5. Revise `_agent/thesis.md` if the source shifts the overall picture.
6. Add the page(s) to `index.md`.
7. Append a `log.md` entry: `## [YYYY-MM-DD] ingest | <id> <Title>` + 1-2 lines on impact.

### Query (P asks a question)
1. Read `index.md` to locate relevant pages; drill into them (and their links).
2. Synthesize an answer WITH citations to source ids.
3. If the answer is durable (a comparison, analysis, discovered connection), offer to file it back as a new page in `05-Syntheses/` or `10-Library/notes/` so the exploration compounds.
4. Append a `log.md` query entry.

### Lint (P asks for a health check)
Scan for: contradictions between pages, stale claims newer sources supersede, orphan pages (no inbound links), concepts mentioned but lacking a page, missing cross-refs, and data gaps a web search could fill. Report findings + suggested next questions/sources.

## Log entry prefixes (keep parseable)
- `## [YYYY-MM-DD] ingest | ...`
- `## [YYYY-MM-DD] query  | ...`
- `## [YYYY-MM-DD] lint   | ...`
- `## [YYYY-MM-DD] deep-ingest | ...`

`grep "^## \[" log.md | tail -5` → recent activity.

---

# DEEP-INGEST OPERATING MANUAL (active project)

**Goal:** turn this wiki into a "game dev brain" — an **exhaustive, detailed page for every
chapter of every source PDF**, heavily cross-linked between books. 17 sources, ~200 chapters,
~5,700 pages. This is a long, multi-pass job. Work in batches; the wiki is the durable artifact.

**Depth bar (per P):** detailed **and** exhaustive. Every subsection of a chapter is captured,
plus key concepts/definitions/frameworks, notable examples/case studies, and (for Schell) every
numbered **Lens**. Faithful and cited, but skimmable (bullets, short sections — see Conventions).

## Where things live
- **Ledger: `_PROGRESS.md`** (root) — the resume point. **Read this FIRST every session.** It has a per-book table with status (e.g. "s005 9/33, resume ch.10") and the processing order.
- **Order:** flagships first — **s005 → s013 → s006 → s001 → s008**, then the rest.
- **Chapter pages: `_ARCHIVE/chapters/sNNN/`** — one `chNN-slug.md` per chapter + a `_index.md` (chapter list with ✅/⬜ status + running Lens list). The source hub `10-Library/sources/sNNN-*.md` links to `../../_ARCHIVE/chapters/sNNN/_index`.
- **Tooling: `_tools/book.py`** (reusable extractor) and `_tools/map_sNNN.json` (chapter→PDF-page maps, created the first time a book is processed).
- **Scratch: `_work/`** — temp text dumps (e.g. `sNNN.full.txt`, `cur.txt`); safe to delete.
- `_PROGRESS.md`, `_tools/`, `_work/` all start with `_` so Obsidian/readers can ignore them.

## Tooling & gotchas (Windows, Python 3.14, no poppler)
- The Read tool **cannot render these PDFs** (poppler/`pdftoppm` not installed). Extract text with Python via `_tools/book.py` (uses `pypdf` + `cryptography`, both pip-installed).
- **Many PDFs are AES-encrypted with an EMPTY password** — `book.py` already calls `r.decrypt('')`.
- **Always prefix `PYTHONIOENCODING=utf-8`** on `book.py` runs, or the Windows cp1252 console throws `UnicodeEncodeError` on smart-quotes/glyphs.
- Commands:
  - `PYTHONIOENCODING=utf-8 python _tools/book.py full sNNN` → cache full text to `_work/sNNN.full.txt`.
  - `PYTHONIOENCODING=utf-8 python _tools/book.py slice sNNN A B > _work/cur.txt 2>/dev/null` → write PDF pages A–B (1-indexed) to a file; then Read `_work/cur.txt`. (Redirect to a file instead of stdout to keep the console clean and read exactly what you need.)
- **Finding chapter boundaries** for a new book: cache full text, locate the TOC, then detect each chapter's first PDF page by normalizing whitespace and matching the full chapter title in the body (skip TOC pages). There's usually a fixed offset (book page + N). Save the result as `_tools/map_sNNN.json`. (Schell's offset was ≈ +30; see `map_s005.json` for the pattern.)

## Per-chapter workflow (one chapter at a time)
1. `slice` the chapter's PDF page range to `_work/cur.txt`; **Read it fully** (be faithful — no inventing).
2. Write `_ARCHIVE/chapters/sNNN/chNN-slug.md` using the template below.
3. Update `_ARCHIVE/chapters/sNNN/_index.md` (mark ✅, add any Lenses).
4. When a chapter raises a cross-cutting theme, **also touch the relevant `10-Library/notes/` or `05-Syntheses/` page** (add the citation/link) — this is where the cross-book value compounds.
5. After each batch: update `_PROGRESS.md`, append a `## [date] deep-ingest | ...` line to `log.md`, and revise `_agent/thesis.md` if something shifts the picture.

### Chapter page template
```
# sNNN · Ch.N — <Title>

**Book:** [[../../10-Library/sources/sNNN-slug|<Short Title (Author)>]] · **PDF pp. A–B**
· **Lenses:** <#n names, or —> · **Prev:** [[chNN-…]] · **Next:** [[chNN-…]]

## Chapter summary
<2–4 sentences: the chapter's core argument.>

## Subsections
### <Subsection heading (verbatim from book)>
- <key points, definitions, frameworks, examples — cited (sNNN, ch.N) where useful>
（…one block per subsection; capture ALL of them…）

## 🔎 Lens #n — <Name>   (Schell only, one block per lens, with its questions)

## Key concepts & links
- <cross-links to 10-Library/notes/* and 05-Syntheses/* and to other books' chapters; call out agreements/tensions>

## Notable quotes
- <1–4 short verbatim quotes>
```

## Cross-book linking (P explicitly wants this)
Actively connect ideas ACROSS books, not just within one. Use `[[../../10-Library/notes/<page>]]`, `[[../../05-Syntheses/<page>]]`, and `[[../sNNN/chNN-…]]` links with a one-line note on the relationship. Known high-value bridges:
- **Mechanics:** Schell elemental tetrad / "mechanics make a game a game" (s005 ch.4, ch.10) · MDA **Mechanics** (s011) · core mechanics (s006 ch.14, s013 ch.23) · verbs (s002) → `10-Library/notes/formal-elements-synthesis`, `10-Library/notes/game-loops-definition`.
- **Pleasures/aesthetics:** LeBlanc's 8 pleasures (s005 ch.8) **≡** MDA's 8 aesthetics (s011); Bartle player types (s005 ch.8, cited s001). → `10-Library/notes/bartle-four-types`, `05-Syntheses/Play, Pleasure & Autotelic Experience`.
- **Iteration/playtesting:** s005 ch.7 ≈ s009 ch.5 ≈ s008 ≈ s001 designer's loop → `10-Library/notes/iterative-design-process`, `05-Syntheses/Iteration, Playtesting & Production`.
- **Flow / mental models:** s005 ch.9 (flow channel) ↔ Koster learnable middle (s016) ↔ balance (s001); mental model ↔ Norman (s015) → `10-Library/notes/flow-channel-definition`, `05-Syntheses/Player Psychology, Motivation & Flow`.
- **Magic circle / play:** s005 ch.3 ↔ Huizinga (s004) ↔ Salen & Zimmerman (s013) → `10-Library/notes/huizinga-caillois`, `05-Syntheses/The Philosophy & Theory of Play`.

Keep `05-Syntheses/` and `10-Library/notes/` pages as the synthesis hubs; deepen them as recurring themes accumulate.

## Provenance caveats (carry forward)
- **s014** (The Gamer's Brain) is a **summary/notes edition**, not the full original.
- **s012** (Level Design) author is **unattributed** in the file.
- **s017** (F2P) is a **blog, Part 1 of 4** only.

## Resume procedure (start of every session)
1. `grep "^## \[" log.md | tail -5` and read `_PROGRESS.md` → find the resume point.
2. Open that book's `_ARCHIVE/chapters/sNNN/_index.md` and `_tools/map_sNNN.json` (build the map if the book is new).
3. Continue per the per-chapter workflow above. Batch size: as many chapters as context allows; stop at a clean boundary and update the ledger/index/log before ending.
