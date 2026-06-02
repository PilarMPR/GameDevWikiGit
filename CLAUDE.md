# Game Dev Wiki — Research Deep-Dive

This directory is an **LLM-maintained game-development research wiki**. It is a persistent, compounding
knowledge base: instead of re-deriving knowledge from raw documents on every question,
the LLM reads each new source once, integrates it into the wiki, and keeps the wiki
current. The wiki — not the raw sources — is the thing you read and reason from.

**Roles.** The human (P) sources material, explores, and asks questions. The LLM (you)
does ALL the writing: summarizing, cross-referencing, filing, and bookkeeping. P never
writes wiki pages by hand; you maintain every page in `wiki/`.

## Topic / thesis

> **TOPIC:** Game development — engines, design, graphics/audio, tooling, production,
> and the craft of building games. (Narrow this to a sub-focus anytime you like.)
>
> **WORKING THESIS:** Game design is a young but coherent discipline whose canon converges
> on a few load-bearing ideas — games are **rule-based systems** that produce **experience**
> through the **player's interaction**, and good design is the **iterative, player-centered**
> craft of shaping that experience — while genuinely disagreeing about the vocabulary for
> "fun" and how much to formalize the process. (Full version + tensions in
> `wiki/syntheses/thesis.md`.)

## Layers

1. **`raw/`** — immutable source documents (articles, papers, reports, notes, images).
   You READ these but NEVER modify them. This is the source of truth. Each source gets
   a short stable id (e.g. `s001`, `s002`) used in citations.
2. **`wiki/`** — LLM-generated markdown. You own this layer entirely.
   - `wiki/sources/` — one summary page per ingested source (`s001-<slug>.md`).
   - `wiki/entities/` — people, orgs, studios. One page per person/org.
   - `wiki/concepts/` — ideas, methods, debates, themes (organized by category subfolder).
   - `wiki/syntheses/` — cross-cutting analyses; `thesis.md` is the evolving overview.
   - `wiki/design-reference/` — per-category reference sheets: all Schell Lenses + multi-source tips.
   - `wiki/analyses/` — game analyses applying wiki frameworks to specific published games.
   - `wiki/genres/` — genre-specific design guides (party brawler, educational games, etc.).
   - `wiki/resources/` — curated external links (GDC talks, papers, blogs, tools, communities).
   - `HotPotato/` — living design workspace for Hot Potato (outside wiki/, same Obsidian vault for linking). Contains GDD pages, decisions log, open questions, research scratchpad, and canvas boards. Use relative links `[[../wiki/...]]` to reference the theory wiki. GDD pages use `gdd-*.md` prefix. Decisions log is append-only. Playtest files go in `HotPotato/playtests/YYYY-MM-DD-context.md`.
   - `wiki/glossary.md` — alphabetical term definitions with concept page links.
   - `wiki/reading-paths.md` — curated paths through the wiki for different goals.
   - `overview.md` (in `wiki/`) — the top-level reader's entry point.

**Project space conventions:** GDD pages use `gdd-*.md` prefix. Decision entries are appended to `decisions.md` (never deleted). Open questions move to decisions.md when resolved. Playtest files go in `project/hot-potato/playtests/YYYY-MM-DD-context.md`.
3. **`index.md`** (root) — content catalog. Every page, with a one-line summary,
   grouped by category. Read this FIRST when answering a query.
4. **`log.md`** (root) — chronological, append-only record of ingests/queries/lints.

## Conventions

- **Links.** Cross-reference liberally with `[[wiki/concepts/foo]]`-style relative
  markdown links (Obsidian-compatible). A link to a page that doesn't exist yet is fine
  — it's a TODO marking a page worth creating.
- **Citations.** Every factual claim in the wiki cites its source id(s) inline, e.g.
  `(s003)` or `(s001, s004)`. This is what lets us trace and audit knowledge.
- **Contradictions.** When a new source contradicts an existing claim, do NOT silently
  overwrite. Flag it: keep both, note which source says what, and add a
  `> ⚠️ Contradiction:` callout. Surface it to P.
- **Provenance over prose.** Prefer precise, cited, skimmable notes over flowing essays.
  Bullet points and short sections beat paragraphs.
- **Dates.** Use absolute dates (YYYY-MM-DD), never "last week".

## Operations

### Ingest (P drops a source into `raw/` and asks to process it)
1. Assign the next source id. Read the source fully.
2. Discuss key takeaways with P before writing (unless told to batch silently).
3. Write `wiki/sources/sNNN-<slug>.md`: metadata (id, title, author, date, type, link),
   a structured summary, key claims (each citable), and links to related wiki pages.
4. Update/create relevant `entities/` and `concepts/` pages — fold the new claims in,
   adding citations and flagging contradictions.
5. Revise `syntheses/thesis.md` if the source shifts the overall picture.
6. Add the page(s) to `index.md`.
7. Append a `log.md` entry: `## [YYYY-MM-DD] ingest | <id> <Title>` + 1-2 lines on impact.

### Query (P asks a question)
1. Read `index.md` to locate relevant pages; drill into them (and their links).
2. Synthesize an answer WITH citations to source ids.
3. If the answer is durable (a comparison, analysis, discovered connection), offer to
   file it back into `wiki/` as a new page so the exploration compounds.
4. Append a `log.md` query entry.

### Lint (P asks for a health check)
Scan for: contradictions between pages, stale claims newer sources supersede, orphan
pages (no inbound links), concepts mentioned but lacking a page, missing cross-refs,
and data gaps a web search could fill. Report findings + suggested next questions/sources.

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
- **Ledger: `_PROGRESS.md`** (root) — the resume point. **Read this FIRST every session.** It
  has a per-book table with status (e.g. "s005 9/33, resume ch.10") and the processing order.
- **Order:** flagships first — **s005 → s013 → s006 → s001 → s008**, then the rest.
- **Chapter pages: `wiki/chapters/sNNN/`** — one `chNN-slug.md` per chapter + a `_index.md`
  (chapter list with ✅/⬜ status + running Lens list). The source hub `wiki/sources/sNNN-*.md`
  links to `../chapters/sNNN/_index`.
- **Tooling: `_tools/book.py`** (reusable extractor) and `_tools/map_sNNN.json` (chapter→PDF-page
  maps, created the first time a book is processed).
- **Scratch: `_work/`** — temp text dumps (e.g. `sNNN.full.txt`, `cur.txt`); safe to delete.
- `_PROGRESS.md`, `_tools/`, `_work/` all start with `_` so Obsidian/readers can ignore them.

## Tooling & gotchas (Windows, Python 3.14, no poppler)
- The Read tool **cannot render these PDFs** (poppler/`pdftoppm` not installed). Extract text
  with Python via `_tools/book.py` (uses `pypdf` + `cryptography`, both pip-installed).
- **Many PDFs are AES-encrypted with an EMPTY password** — `book.py` already calls `r.decrypt('')`.
- **Always prefix `PYTHONIOENCODING=utf-8`** on `book.py` runs, or the Windows cp1252 console
  throws `UnicodeEncodeError` on smart-quotes/glyphs.
- Commands:
  - `PYTHONIOENCODING=utf-8 python _tools/book.py full sNNN` → cache full text to `_work/sNNN.full.txt`.
  - `PYTHONIOENCODING=utf-8 python _tools/book.py slice sNNN A B > _work/cur.txt 2>/dev/null`
    → write PDF pages A–B (1-indexed) to a file; then Read `_work/cur.txt`. (Redirect to a file
    instead of stdout to keep the console clean and read exactly what you need.)
- **Finding chapter boundaries** for a new book: cache full text, locate the TOC, then detect
  each chapter's first PDF page by normalizing whitespace and matching the full chapter title in
  the body (skip TOC pages). There's usually a fixed offset (book page + N). Save the result as
  `_tools/map_sNNN.json`. (Schell's offset was ≈ +30; see `map_s005.json` for the pattern.)

## Per-chapter workflow (one chapter at a time)
1. `slice` the chapter's PDF page range to `_work/cur.txt`; **Read it fully** (be faithful — no
   inventing).
2. Write `wiki/chapters/sNNN/chNN-slug.md` using the template below.
3. Update `wiki/chapters/sNNN/_index.md` (mark ✅, add any Lenses).
4. When a chapter raises a cross-cutting theme, **also touch the relevant `wiki/concepts/` page**
   (add the citation/link) — this is where the cross-book value compounds.
5. After each batch: update `_PROGRESS.md`, append a `## [date] deep-ingest | ...` line to
   `log.md`, and revise `wiki/syntheses/thesis.md` if something shifts the picture.

### Chapter page template
```
# sNNN · Ch.N — <Title>

**Book:** [[../../sources/sNNN-slug|<Short Title (Author)>]] · **PDF pp. A–B**
· **Lenses:** <#n names, or —> · **Prev:** [[chNN-…]] · **Next:** [[chNN-…]]

## Chapter summary
<2–4 sentences: the chapter's core argument.>

## Subsections
### <Subsection heading (verbatim from book)>
- <key points, definitions, frameworks, examples — cited (sNNN, ch.N) where useful>
（…one block per subsection; capture ALL of them…）

## 🔎 Lens #n — <Name>   (Schell only, one block per lens, with its questions)

## Key concepts & links
- <cross-links to wiki/concepts/* and to other books' chapters; call out agreements/tensions>

## Notable quotes
- <1–4 short verbatim quotes>
```

## Cross-book linking (P explicitly wants this)
Actively connect ideas ACROSS books, not just within one. Use `[[../../concepts/<page>]]` and
`[[../sNNN/chNN-…]]` links and a one-line note on the relationship. Known high-value bridges:
- **Mechanics:** Schell elemental tetrad / "mechanics make a game a game" (s005 ch.4, ch.10) ·
  MDA **Mechanics** (s011, `concepts/mda-framework`) · core mechanics (s006 ch.14, s013 ch.23) ·
  verbs (s002) · `concepts/formal-elements`, `concepts/game-genres-and-mechanics`.
- **Pleasures/aesthetics:** LeBlanc's 8 pleasures (s005 ch.8) **≡** MDA's 8 aesthetics (s011);
  Bartle player types (s005 ch.8, cited s001). → `concepts/theory-of-fun`, `concepts/mda-framework`.
- **Iteration/playtesting:** s005 ch.7 ≈ s009 ch.5 ≈ s008 ≈ s001 designer's loop →
  `concepts/iterative-design-and-playtesting`.
- **Flow / mental models:** s005 ch.9 (flow channel) ↔ Koster learnable middle (s016) ↔ balance
  (s001); mental model ↔ Norman (s015), Sellers game+player system (s001).
- **Magic circle / play:** s005 ch.3 ↔ Huizinga (s004) ↔ Salen & Zimmerman (s013) →
  `concepts/magic-circle`, `concepts/play-and-culture`, `concepts/meaningful-play`.
Keep `concepts/*` pages as the synthesis hubs; deepen them as recurring themes accumulate.

## Provenance caveats (carry forward)
- **s014** (The Gamer's Brain) is a **summary/notes edition**, not the full original.
- **s012** (Level Design) author is **unattributed** in the file.
- **s017** (F2P) is a **blog, Part 1 of 4** only.

## Resume procedure (start of every session)
1. `grep "^## \[" log.md | tail -5` and read `_PROGRESS.md` → find the resume point.
2. Open that book's `_index.md` and `_tools/map_sNNN.json` (build the map if the book is new).
3. Continue per the per-chapter workflow above. Batch size: as many chapters as context allows;
   stop at a clean boundary and update the ledger/index/log before ending.
