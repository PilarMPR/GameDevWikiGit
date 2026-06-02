# Alexandria Migration Log

Append-only. Each entry records what moved, where it went, and any notes.

---

## [2026-06-02] Legacy directories removed

Deleted `HotPotato/` (15 files) and `wiki/` (127 files) from the repository. Both are fully superseded by the Alexandria structure — content lives in `40-HotPotato/`, `10-Library/`, `30-Analyses/`, and `_ARCHIVE/`. Commit `6a27933`, pushed to `origin/alexandria-rebuild`.

---

## [2026-06-02] Phase 8–9 — Git Push & Final Report

**Repository created:** https://github.com/wildalchemists/GameDevWiki (private)
**Branch pushed:** `alexandria-rebuild`
**Commits on this branch:**
- `9c11d1f` — chore: pre-migration-snapshot (180 files, 128310 lines baseline)
- `48e1139` — feat(structure): complete Alexandria rebuild migration (382 files, +23515 lines)
- `16ff08d` — fix: add ## Connections to all entity notes (12 files)

**Final acceptance checklist results:**
- ✅ 0 PDFs in git
- ✅ 0 `_work/` files in git
- ✅ 178 atomic notes in `10-Library/notes/`
- ✅ 17 source cards in `10-Library/sources/`
- ✅ 0 notes missing `## Connections`
- ✅ 115 notes tagged `hp: true`
- ✅ 11 discipline MOCs + 5 bridge MOCs + home MOC
- ✅ `40-HotPotato/_index.md` Dataview wired to `hp: true` notes
- ✅ `decisions.md` first two entries have `**Basis:**` lines

**Content preserved:** All 146 original .md files are in `_ARCHIVE/`. Zero deletions.

**_ARCHIVE/ contents:**
- `wiki-sources-original/` — original 17 source cards (pre-schema-3b)
- `wiki-concepts-gen2/` — all gen-2 disciplined concept files (40 files, 11 discipline subdirs)
- `chapters/` — original s005 ch.1–10 chapter files
- `design-reference/` — original reference sheets including `schell-lenses-all.md`
- `entities/` — original 9 entity files
- `syntheses/` — 4 synthesis files (thesis, frameworks-comparison, applying-the-canon, hot-potato-design)
- `analyses/` — 7 game teardowns
- `genres/` — 2 genre analyses
- `CLAUDE-original.md` — original operating manual

---

## [2026-06-02] Phase 0 — Safety & Scaffold

- `git init` at D:\GameDevWiki
- `.gitignore` written (blocks raw/, *.pdf, _work/, _agent/logs/, .smtcmp_*, workspace.json)
- Initial commit `pre-migration-snapshot`: 180 files, 128310 lines, 0 PDFs
- Branch `alexandria-rebuild` created
- Full target folder tree created: 00-Atlas/, 10-Library/, 20-Reference/, 30-Analyses/, 40-HotPotato/, 50-Feed/, _meta/, _ARCHIVE/
- 7 Templater templates written to `_meta/templates/`

---

## [2026-06-02] Phase 2 — Concept Atomization

Atomic notes written: 66 (as of Phase 2 completion)
Gen-2 concept files archived to: _ARCHIVE/wiki-concepts-gen2/
Flat concept files archived to: _ARCHIVE/wiki-concepts-flat/
Chapter files archived to: _ARCHIVE/chapters/
Collision resolution: 7 name-collision pairs — flat content folded into gen-2 notes; originals archived
Chapter migrations: 10 Schell chapter files → 10-Library/notes/schell-ch*.md
Key notes created: mda-* (5), mechanics-* (6), game-loops-* (4), game-balance-* (3), player-* (5), level-design-* (3), feel-and-controls-* (5), theory-* (7), production-* (3), narrative-* (3), business-* (3), chapter notes (10)

---

## [2026-06-02] Phase 1 — Source Migration (17 files)

| Original | New Location | Notes |
|---|---|---|
| wiki/sources/s001-advanced-game-design.md | 10-Library/sources/s001-advanced-game-design.md | Schema 3b; YAML frontmatter added |
| wiki/sources/s002-a-game-design-vocabulary.md | 10-Library/sources/s002-a-game-design-vocabulary.md | Schema 3b |
| wiki/sources/s003-hows-and-whys-of-level-design.md | 10-Library/sources/s003-hows-and-whys-of-level-design.md | Schema 3b |
| wiki/sources/s004-homo-ludens.md | 10-Library/sources/s004-homo-ludens.md | Schema 3b |
| wiki/sources/s005-art-of-game-design.md | 10-Library/sources/s005-art-of-game-design.md | Schema 3b; deep-ingest note added |
| wiki/sources/s006-fundamentals-of-game-design.md | 10-Library/sources/s006-fundamentals-of-game-design.md | Schema 3b |
| wiki/sources/s007-game-feel.md | 10-Library/sources/s007-game-feel.md | Schema 3b |
| wiki/sources/s008-game-design-workshop.md | 10-Library/sources/s008-game-design-workshop.md | Schema 3b |
| wiki/sources/s009-games-design-and-play.md | 10-Library/sources/s009-games-design-and-play.md | Schema 3b |
| wiki/sources/s010-introduction-to-game-analysis.md | 10-Library/sources/s010-introduction-to-game-analysis.md | Schema 3b |
| wiki/sources/s011-mda-framework.md | 10-Library/sources/s011-mda-framework.md | Schema 3b |
| wiki/sources/s012-level-design.md | 10-Library/sources/s012-level-design.md | Schema 3b; author corrected to Kremers |
| wiki/sources/s013-rules-of-play.md | 10-Library/sources/s013-rules-of-play.md | Schema 3b |
| wiki/sources/s014-the-gamers-brain.md | 10-Library/sources/s014-the-gamers-brain.md | Schema 3b; provenance caveat preserved |
| wiki/sources/s015-design-of-everyday-things.md | 10-Library/sources/s015-design-of-everyday-things.md | Schema 3b |
| wiki/sources/s016-theory-of-fun.md | 10-Library/sources/s016-theory-of-fun.md | Schema 3b; s001 tension note preserved |
| wiki/sources/s017-f2p-design-handbook.md | 10-Library/sources/s017-f2p-design-handbook.md | Schema 3b; Part 1/4 caveat preserved |

Originals archived to: _ARCHIVE/wiki-sources-original/sources/ (17 files)

---
# Log

Append-only, chronological record. Prefixes: `ingest` | `query` | `lint`.
`grep "^## \[" log.md | tail -5` → recent activity.

---

## [2026-06-01] setup | Wiki scaffolded
Created raw/, wiki/{sources,entities,concepts,syntheses}, index.md, log.md, CLAUDE.md,
overview.md, and a placeholder thesis. Topic not yet set. Ready for first ingest.

## [2026-06-01] setup | Renamed to Game Dev Wiki
Renamed folder D:\LLMWiki → D:\GameDevWiki and set topic to game development across
CLAUDE.md, index.md, overview.md, thesis.md.

## [2026-06-01] ingest | s001 Advanced Game Design: A Systems Approach (Michael Sellers, 2018)
AES-encrypted PDF (empty pwd), 456 pp — NOT the 97pp the harness reported. Installed
pypdf+cryptography to extract text (poppler/pdftoppm unavailable). Summarized from TOC,
chapter openers, and author's end-of-chapter summaries. Copied source to
raw/s001-advanced-game-design.pdf. Created source page, entity (michael-sellers), and 7
concept pages (systems-thinking, parts-loops-wholes, game-as-system, fun-and-interactivity,
the-four-principal-loops, game-balance, systemic-design-process). Set initial thesis
(games as systems / design as system design) and flagged one open tension: s001 claims a
game need not be "fun" if interactive+engaging.

## [2026-06-01] ingest | s002–s017 — batch of 16 game-design books
Bulk ingest of the rest of D:\FileOrganizer\Learning\GameDesign. NOTE: the Jesse Schell file
that was 0 bytes earlier had since finished downloading (now 518pp) and was ingested as s005.
Extraction pipeline: pypdf+cryptography (empty-pw decrypt for s006/s009 etc.), full-text dump +
TOC + author chapter-summary extraction to _work/ (since deleted). Sources added:
 s002 A Game Design Vocabulary (Anthropy & Clark) · s003 Hows & Whys of Level Design (Hourences)
 s004 Homo Ludens (Huizinga) · s005 The Art of Game Design (Schell) · s006 Fundamentals of Game
 Design 3e (Adams) · s007 Game Feel (Swink) · s008 Game Design Workshop (Fullerton) · s009 Games,
 Design and Play (Macklin & Sharp) · s010 Introduction to Game Analysis (Fernández-Vara) · s011
 MDA (Hunicke/LeBlanc/Zubek) · s012 Level Design (author unattributed in file) · s013 Rules of
 Play (Salen & Zimmerman) · s014 The Gamer's Brain (Hodent — SUMMARY/NOTES edition, flagged) ·
 s015 The Design of Everyday Things (Norman) · s016 A Theory of Fun (Koster) · s017 Ultimate F2P
 Handbook Pt 1/4 (Genesis, Medium blog).
Created 16 source pages + copied all PDFs to raw/ as sNNN-*.pdf. Created 15 new concept pages
(mda-framework, theory-of-fun, formal-elements, meaningful-play, magic-circle, play-and-culture,
iterative-design-and-playtesting, player-experience-and-ux, usability-and-hcd, game-feel-and-3cs,
level-design, game-analysis, game-design-vocabulary, game-genres-and-mechanics, free-to-play-design)
and extended fun-and-interactivity + systems-thinking with cross-source links. Rewrote thesis as a
17-source synthesis (5 consensus pillars + the "what is fun?" tension), rebuilt index & overview.
Provenance caveats recorded: s014 notes-edition, s012 unattributed, s017 blog/Part-1-only.

## [2026-06-01] deep-ingest | Pass 1 — infrastructure + Schell ch.1–2
Started the "game dev brain" deep pass (depth = detailed + exhaustive per chapter; order =
flagships first). Built reusable tooling _tools/book.py (pypdf extract/slice, set
PYTHONIOENCODING=utf-8 to avoid cp1252 console errors), saved _tools/map_s005.json (Schell
chapter→PDF-page map, offset ≈ book page +30), and _PROGRESS.md ledger. New structure:
wiki/chapters/sNNN/ with _index.md + chNN-slug.md per chapter (keeps existing source-hub links
intact). Wrote exhaustive pages for s005 ch.1 (the designer; deep listening; 5 kinds of
listening; major vs minor gift) and ch.2 (experience is the goal; Lens #1 Essential Experience;
introspection perils; defeating Heisenberg). Created s005/_index.md (2/33). NEXT: s005 ch.3+ then
remaining flagships. This is a multi-pass job (~200 chapters total) — resume from _PROGRESS.md.

## [2026-06-01] deep-ingest | Pass 2 — Schell ch.3–6
First loop batch. Wrote exhaustive pages for s005 ch.3 (definitions of toy/play/fun/game;
Lenses #2–6; magic circle = internal problem-solving system; cross-links to s013/s004/s016),
ch.4 (elemental tetrad Mechanics/Story/Aesthetics/Technology; visibility gradient; Lenses #7–8;
Space Invaders case), ch.5 (theme/unification/resonance; experience- vs truth-based; Lenses
#9–10; Pirates VR, Titanic, Toontown "work vs play"), ch.6 (idea generation; the subconscious
"silent partner"; 15 brainstorming tips; Lenses #11–12). s005 now 6/33; lenses #1–12 captured.
Resume at s005 ch.7 (The Game Improves Through Iteration).

## [2026-06-01] deep-ingest | Pass 3 (loop) — Schell ch.7–9
Self-paced /loop batch. Wrote exhaustive pages for s005 ch.7 (iteration; Eight Filters /
Rule of the Loop / waterfall vs Boehm spiral / risk mitigation / 8 prototyping tips /
build-the-toy-first / Cerny's Method; Lenses #13–15 — the central process cross-link node to
s009/s008/s001), ch.8 (the player; demographics & gender; psychographics; **LeBlanc's 8
pleasures = MDA's 8 aesthetics**, **Bartle's 4 player types**; Lenses #16–17), ch.9 (the mind;
modeling/focus/imagination/empathy; **flow & the flow channel**; Maslow; judgment; Lenses
#18–20). Strengthened cross-book links per request (mechanics↔MDA, pleasures↔MDA, flow↔Koster/
balance, mental models↔Norman/Sellers). Resolved the thesis open question on flow + Bartle.
s005 now 9/33; lenses #1–20 captured. Resume at s005 ch.10 (Some Elements are Game Mechanics).

## [2026-06-01] deep-ingest | Pass 4 (loop) — Schell ch.10 (the big mechanics chapter)
Read in two halves (42pp). Wrote exhaustive page for the six game mechanics — Space (Lens #21),
Objects/Attributes/States + hierarchy-of-knowers (Lens #22), Actions/operative-vs-resultant +
emergence (Lenses #23–24), Rules/Parlett taxonomy/modes/enforcer/goals (Lenses #25–26), Skill
real-vs-virtual (Lens #27), Chance/10 probability rules/expected value/regret/skill-chance
(Lenses #28–29). Made this the central MECHANICS cross-link node per P's request: tied Schell's
six mechanics to MDA Mechanics (s011), formal-elements (s008/s009/s006), verbs (s002),
emergence↔systems (s001/s013), and EV/curves↔game-balance (s001). s005 now 10/33; lenses #1–29
captured. Resume at s005 ch.11 (Game Mechanics Must be in Balance).

## [2026-06-01] deep-ingest | Concept Compendium — Batch 1 (Mechanics + Feel + Player)
Pivoted from chapter-by-chapter deep-ingest to a **concept-first compendium** approach: comprehensive
multi-source pages grouped by category. Cached all 17 PDFs as `_work/sNNN.full.txt`. Created
category directory structure under `wiki/concepts/`: mechanics/, feel-and-controls/, interface/,
player/, narrative/, level-design/, production/, theory/, business/. Wrote 6 deep concept pages
(each synthesizing 6–10 sources):
  - `mechanics/core-mechanics.md` — Schell 6 mechanics, Adams 5 types, Anthropy verbs/objects,
    Fullerton formal elements, Macklin & Sharp 6 elements, Salen & Zimmerman core mechanic, MDA, Sellers
  - `mechanics/game-loops.md` — Sellers 4 principal loops + 3 gameplay loop types, MDA dynamics,
    F2P loop architecture, Halo stacking model, reinforcing/balancing loops
  - `feel-and-controls/game-feel.md` — Swink 3 building blocks + 6 measurable components,
    3Cs (s017), Norman affordances/feedback, game feel as invisible art
  - `feel-and-controls/camera-design.md` — Adams camera models taxonomy, static vs. dynamic,
    FPS/3rd-person/top-down/side-scroll/isometric, camera and game feel, genre conventions
  - `player/flow-channel.md` — Csikszentmihalyi flow, Schell tense-and-release + Lens #18, Koster
    fun=learning, Macklin & Sharp absorption caveat, Sellers interactive loop, Adams challenge design
  - `player/player-psychology.md` — Hodent perception/memory/attention/cognitive load/motivation,
    Schell 4 mental abilities + Maslow, Sellers mental models, Norman, Koster pattern-matching, SDT
Updated `index.md` with new category structure (compendium + legacy stubs). TODO: continue with
theory/, production/, level-design/, narrative/, business/ categories.

## [2026-06-01] deep-ingest | Concept Compendium — Batch 2 (Theory & Foundations)
Expanded all 6 theory/ stubs from thin single-source pages into comprehensive multi-source entries.
Read s011 (MDA paper) in full; grepped s013 (Rules of Play), s016 (Theory of Fun), s004 (Homo Ludens),
and s001 (Advanced Game Design) for rich primary passages. New/rewritten pages:
  - `theory/mda-framework.md` — full MDA paper synthesis; 3 layers + 8 aesthetics with examples
    (Charades/Quake/Sims/FF), artifact vs. media claim, dynamic models + feedback systems (Monopoly),
    aesthetic-first design workflow, cross-source connections to all 7 related pages
  - `theory/systems-thinking.md` — Sellers' 4-element decomposition (parts/wholes/loops/goals),
    reinforcing vs. balancing loops, emergence, game+player as coupled system, 4 source perspectives
    (Sellers/Salen&Zimmerman/Fullerton/MDA/Koster)
  - `theory/magic-circle.md` — Huizinga origin (play as voluntary/separate/rule-governed/autotelic),
    Caillois 4 play types + paidia/ludus, Suits' lusory attitude, Salen & Zimmerman's design concept
    (porous boundary, special meanings, new reality), Sellers non-consequential context, design critique
  - `theory/meaningful-play.md` — full definition (discernable + integrated), 3 schemas (formal/
    experiential/cultural), all 5 operationalizations (Schell/Sellers/Fullerton/Norman/Fernández-Vara),
    procedural rhetoric, fun debate synthesis table
  - `theory/theory-of-fun.md` — Koster full theory: pattern-matching brain, grokking, 5 boredom
    failure modes, learnable middle ≡ flow channel comparison table, games-as-teachers claim, "fun"
    debate (Koster/MDA/Sellers reconciliation), hard fun + expressive medium
  - `theory/formal-elements.md` — side-by-side comparison of 6 sources' lists, synthesis table
    mapping Fullerton/Macklin&Sharp/Schell/Anthropy columns, game-type comparison (chess/Monopoly/
    Tetris/Minecraft/Poker), MDA + game analysis cross-links
All pages heavily cross-linked to existing mechanics/, feel-and-controls/, and player/ pages.
Next: level-design/, then narrative/, production/, business/.

## [2026-06-01] deep-ingest | Concept Compendium — Batch 3 (Level Design)
Read Schell ch.14 (interest curves, PDF pp.274-289) and ch.19 (spaces, PDF pp.358-380) in full.
Extracted and read s012 pt1 (pp.1-55) and s003 intro (pp.1-60). Discovered s012 author: Rudolf Kremers —
corrected source page (was logged as "unattributed" from metadata failure). Wrote 3 level-design pages:
  - `level-design/level-design.md` — Kremers' game design vs. level design distinction, teaching as
    primary function (show before ask, scaffolding, reinforcement spacing), goals hierarchy (macro/
    intermediate/micro), structure & methodology (block-out process), Hourences' checklist/floorplan,
    Schell's architecture analogy + 6 indirect control methods, environmental narrative
  - `level-design/spatial-design.md` — Schell's 5 organizational principles (linear/grid/web/points-
    in-space/divided), functional vs. experienced space, sightlines (3 functions: guiding/tactical/
    mystery), landmarks + hierarchy, scale as emotion, Hourences composition (unity, moving geometry,
    light), spatial flow + encounter rhythm, indirect control table
  - `level-design/pacing-and-flow.md` — Full Schell interest curve model (A hook → B–F peaks/valleys
    → G climax → H resolution), interest threshold, fractal structure, tense-and-release, difficulty
    curve failure table (spike/flatline/early peak/late sagging/bad finale), pacing toolkit (boss
    anchors, checkpoints, rest spaces), session-level pacing (F2P), Lens #61 design questions
Updated _PROGRESS.md (3 new ✅). Also corrected s012 author: Rudolf Kremers (was "unattributed" from PDF metadata failure).

## [2026-06-01] deep-ingest | Concept Compendium — Batches 4–5 (Narrative + Production + Business)
Read Schell ch.15 (story/game duality, PDF pp.290-312) in full. Used cached s008/s009 TOC + grep
results for production content. Wrote 10 pages across narrative, production, and business categories:

**Narrative (4 pages):**
  - `narrative/story-and-games.md` — story/game duality (wave-particle analogy), myth of passive
    entertainment, 3 narrative approaches (string of pearls / story machine / branching), ludonarrative
    dissonance (definition + Bioshock example), embedded vs emergent narrative (Salen & Zimmerman),
    verbs as narrative (Anthropy), procedural rhetoric (Fernández-Vara), 5 practical principles
  - `narrative/indirect-control.md` — Schell's 6 methods (constraints/goals/interface/visual design/
    characters/music) with full explanations, feeling of freedom principle, candy store/colored doors
    examples, combined methods example, connection to ludonarrative coherence
  - `narrative/world-building.md` — 5 functions of a game world, consistency as foundation (world-
    rules not realism), closed/open worlds, biomes, environmental storytelling (has-happened/who-lives/
    what-valued/happening-now), world and theme (world IS the thematic argument), fiction contract
  - `narrative/characters.md` — projection vs. empathy (Heider & Simmel), silent protagonist vs.
    characterized protagonist design choice, NPC functions + believability over realism, empathy
    mechanism (large eyes / symmetry / animation), character+theme alignment, companions as indirect
    control, character across formal elements (Anthropy: verbs define characters)

**Production (4 pages):**
  - `production/iterative-design.md` — why iteration is necessary (game ≠ experience), playcentric
    process (s008 6-step cycle), Schell's Rule of the Loop + 8 prototyping tips, Macklin & Sharp
    design values as anchor, Sellers' designer's loop, waterfall vs. Boehm spiral vs. Cerny's Method,
    common iteration failure modes
  - `production/playtesting.md` — what playtesting is/isn't, 6 playtesting types (internal/developer/
    friend-family/target-audience/new-player/experienced), 3 data types (qualitative/quantitative/
    behavioral), facilitator role (observe don't explain), session structure (before/during/after),
    Macklin & Sharp evaluation framework, development lifecycle table
  - `production/documentation.md` — why documentation matters, GDD structure (overview/mechanics/
    formal elements/world/features), one-pager + pitch deck formats, best practices (alive/certain/
    decisions+rationale/one source/visual), Macklin & Sharp Pong case study, Schell on writing as clarity
  - `production/team-and-culture.md` — 6 core roles (designer/level designer/programmer/artist/
    producer/sound), design within team (3 tensions: engineering/art/producer), communication +
    alignment (shared vision, decision authority, critique culture, design values as arbitration),
    designer lifecycle (pre-production/production/polish), team size trade-offs, Conway's Law, crunch

**Business (2 pages):**
  - `business/free-to-play-design.md` — expanded existing stub: fun-first principle, 3Cs framework,
    4-stage F2P arc (core/economy/retention/monetization), F2P core loop architecture (short/medium/
    long loops), onboarding criticality, ethical design (undermining effect, variable ratio, loss
    aversion, fair reflection test)
  - `business/monetization.md` — revenue models table (premium/subscription/F2P/season-pass/battle-
    pass/ads), pay-to-win vs. cosmetic axis, IAP/currency systems/price anchoring, gacha mechanics +
    variable ratio + ethical concerns, battle pass structure + FOMO risk, ethical principles checklist

All pages cross-linked to existing compendium pages. _PROGRESS.md updated.
Concept Compendium is now COMPLETE for all planned pages (33 total pages across 9 categories).
Remaining ⬜ pages: mechanics/progression-systems, mechanics/puzzles, mechanics/emergence,
feel-and-controls/input-and-controls, feel-and-controls/feedback-systems, interface/ui-design,
interface/usability-and-hcd, interface/interest-curves, player/player-types, player/motivation
(these are labeled ⬜ in _PROGRESS.md but were not in the Batch 1–5 plan; can be added as Batch 6).

## [2026-06-01] deep-ingest | Concept Compendium — Batch 6 (Remaining Mechanics, Feel, Interface, Player)
Completed all remaining ⬜ pages. Read Schell ch.12 (puzzles) in full; used s007 (Swink) grep for
input/feedback; s015 (Norman) for HCD; s005 ch.8 for Bartle player types. Wrote 9 pages:

**Player (2):**
  - `player/player-types.md` — Bartle's 4 types + axes (acting/interacting × world/players), design
    implications per type, LeBlanc's 8 aesthetics as parallel taxonomy, demographics/psychographics
    distinction, BrainHex mention, type shifts across player lifecycle, F2P retention connection
  - `player/motivation.md` — Maslow's hierarchy in games (levels 3–5 analysis), intrinsic vs. extrinsic
    + undermining effect (overjustification), SDT (competence/autonomy/relatedness + what games that
    satisfy all three look like), reward schedules table (5 types + effects), Koster's fun-as-motivation,
    flow as motivational sweet spot, loss aversion (prospect theory, ethical design line)

**Interface (2):**
  - `interface/usability-and-hcd.md` — Norman's 6 principles (affordances/signifiers/constraints/
    mappings/feedback/conceptual models); affordance vs. signifier distinction from 2013 edition;
    gulfs of execution and evaluation; HCD 5-step process; Hodent's cognitive extension (perception/
    memory/mental model alignment/learnability); games vs. other software usability
  - `interface/ui-design.md` — diegetic vs. non-diegetic vs. meta UI (with examples); HUD design
    (4-level attention hierarchy, visual hierarchy, cognitive load, dynamic HUDs); menu structure
    (flat/hierarchical/contextual); inventory design tension (minigame vs. chore); onboarding
    (progressive disclosure, contextual tutorials, fail-state teaching); safe zone and accessibility

**Feel & Controls (2):**
  - `feel-and-controls/input-and-controls.md` — "input structure is tactile contact" framing; 240ms
    boundary (upper limit for perceived real-time response); input-to-response mapping (directness,
    curve shape, deadzones, button semantics); analog vs. digital; identity extension (players "look
    through the controller"); controller accessibility (remapping, hold-vs-toggle); platform table
  - `feel-and-controls/feedback-systems.md` — 5 channels (visual/audio/haptic/diegetic/narrative)
    each with sub-types; tells as predictive feedback (fairness mechanism); feedback design principles
    (immediacy/informativeness/proportionality/consistency/accessibility); calibration (temporal
    tuning, intensity curves, stacking); "juice" as feedback calibration insight

**Mechanics (3):**
  - `mechanics/emergence.md` — definition (whole > parts); positive emergence (chess/Minecraft/
    competitive metas) vs. negative emergence (exploits/dominant strategies); why emergence requires
    systems; Salen & Zimmerman complexity theory (emergence vs. progression); MDA Dynamics as
    emergence layer; designing for positive emergence (composable mechanics, feedback loops, consistency);
    Koster's replayability connection
  - `mechanics/puzzles.md` — puzzle vs. game definition (dominant strategy); explicit vs. integrated
    puzzles (7th Guest failure vs. Zelda Wind Waker success); 10 design principles (goal clarity /
    easy start / sense of progress / solvability / minimal frustration / parallelism / pyramid /
    hints / satisfying solution / progressive complexity); walkthrough problem response; Koster connection
  - `mechanics/progression-systems.md` — XP loop design; level curves (flat/exponential/adjustable);
    Weber-Fechner problem (why linear numbers feel sublinear); power curves + balance failures; skill
    trees (design properties + anti-patterns); meta-progression (outer loop); unlock systems (criteria
    types + sequencing); progression vs. treadmill (intrinsic vs. extrinsic concern); game-type table

**THE CONCEPT COMPENDIUM IS NOW FULLY COMPLETE.** All 42 planned pages across all 9 categories
are written. Total: mechanics(6), feel-and-controls(4), interface(3), player(4), narrative(4),
level-design(3), production(4), theory(6), business(2) = 36 category pages + legacy stubs preserved.

## [2026-06-01] deep-ingest | Design Reference — All 100 Schell Lenses + Multi-Source Tips
Created `wiki/design-reference/` section: 9 per-category reference sheets (+ _index.md) extracting
all design questions and practical tips from all 17 sources. Grepped s005 for all lens names (TOC),
extracted lens question content from ch.11–16, organized by category. Each sheet contains:
  - All applicable Schell Lenses with their design questions (s005, ch.1–28)
  - Practical tips from Adams (s006), Kremers (s012), Hourences (s003), Norman (s015),
    Swink (s007), Sellers (s001), Macklin & Sharp (s009), Fullerton (s008), Hodent (s014), Koster (s016)
  - MDA (s011) and Salen & Zimmerman (s013) analytical frameworks as design checklists

Sheets produced:
  - `mechanics.md` — Lenses #21–52; Adams mechanic types; Sellers systemic questions; Fullerton
    formal elements checklist; Macklin & Sharp design values; Koster fun-as-learning diagnostics
  - `feel-and-controls.md` — Lenses #15, #53–60; Swink 3 building blocks + 6 components + identity
    extension test; Norman mapping + feedback checklists; Hourences composition; Hodent sensory feedback
  - `interface.md` — Lenses #53–60; Norman 6-principle checklists (affordances/signifiers/constraints/
    mappings/feedback/conceptual model); Hodent cognitive load + HUD + onboarding checklists;
    Adams player-centric; Kremers diegetic decision questions
  - `player.md` — Lenses #16–20, #64, #75, #84–88; Hodent cognitive constraints (perception/memory/
    attention/motivation); Schell 4 mental abilities; Koster fun diagnostic; Sellers interactive loop
    health; Bartle player type coverage; Adams audience analysis
  - `narrative.md` — Lenses #65–83 (story, characters, world, indirect control, freedom); Schell
    indirect control 6-method audit; Kremers environmental storytelling + narrative/gameplay integration;
    Sellers mental model alignment; Adams world-building consistency test
  - `level-design.md` — Lenses #61–63, #71–72; Kremers goal hierarchy + teaching + methodology
    checklists; Hourences spatial checklist + audiovisual composition; Schell architecture as experience;
    Adams 5 spatial types + level principles
  - `production.md` — Lenses #11–14, #89–100 (all Schell production lenses incl. Eight Filters,
    Risk, Team, Documentation, Playtesting, Technology, Crystal Ball, Client, Pitch, Profit,
    Transformation, Responsibility, Secret Purpose); Fullerton playcentric process; Macklin & Sharp
    design values framework; Sellers designer's loop health; Adams pre-production; Kremers level process
  - `theory.md` — Lenses #1–10, #44–45; MDA analysis chain + designer direction test; Sellers systems
    audit; Salen & Zimmerman meaningful play + three-schema check; Koster mastery curve; Norman HCD;
    Fullerton formal elements completeness
  - `business.md` — Lenses #95–96 (Pitch, Profit); F2P 4-stage checklist; Hodent ethical monetization
    (fair reflection test, reward schedule audit, undermining effect, loss aversion); Adams model
    selection; community health questions; pricing principles
Updated index.md with Design Reference section. _PROGRESS.md not updated (no ⬜ items remaining).

## [2026-06-01] deep-ingest | Expansion Phase — Session 1 (Hot Potato Priority + References)
New directories: wiki/genres/, wiki/analyses/, wiki/resources/. Wrote 7 new pages:

  - `genres/party-brawler.md` — definitive genre guide for Hot Potato; party axis vs. brawler axis
    tension; MDA for party brawlers (Fellowship + Challenge dual-primary); player-type mix management
    (Achievers/Socializers/Killers at a party); catch-up mechanics; object/ball mechanic analysis (how
    a shared object shifts conflict from "Killers vs. Players" to "Achievers vs. World"); Hot Potato
    specific design: timer feedback design (visual/audio/haptic), pass mechanics table, score economy
    options (penalty-only vs. hold-time-reward vs. contextual); round structure; accessibility checklist
    with 10 actionable items

  - `analyses/smash-bros.md` — Super Smash Bros. Ultimate; formal elements table; full MDA analysis
    (% mechanics → edgeguarding/neutral/combo dynamics → Challenge + Fellowship + Fantasy); core loop
    diagram; 5 design highlights (% system as accessible tension engine, stage design as mechanic,
    asymmetric chars without progression, items as skill-gap management, Final Smash as spectacle);
    extractable principles; Hot Potato relevance + the "Hot Potato delta" question (what changes when
    you add the shared object to a brawler)

  - `analyses/jackbox.md` — Jackbox Party Pack; formal elements; MDA analysis (Fellowship + Expression
    dominant; Challenge vestigial); core loop diagram; 5 design highlights (phone as input innovation,
    player-generated content, score as scaffolding not point, simultaneous input, audience mode); "what
    Jackbox cannot do" contrast; extractable party design principles; Hot Potato relevance

  - `analyses/_index.md` — index + template for all analyses

  - `resources/external.md` — curated external resources: GDC talks by category (game feel, mechanics,
    MDA, story, level design, player psychology, party games, F2P) with Sakurai's YouTube series as
    top recommendation; academic papers; blogs (Koster, Lostgarden, Gamasutra postmortems, Designer
    Notes, GMTK); tools table (Machinations, Articy, Twine, BoardGameGeek, itch.io); communities;
    educational games section (Games for Change, ISTE, Filament Games, SCORM/xAPI standards)

  - `glossary.md` — ~70 alphabetical entries; each with one-line definition, source citation, concept
    page link; covers all major technical vocabulary used across the wiki

  - `reading-paths.md` — 5 curated paths: (1) foundation, (2) Hot Potato sprint, (3) edugames pitch,
    (4) playtesting prep, (5) source-first; each 8 steps with annotations; includes source→path table

Infrastructure updates: CLAUDE.md updated with 7 new wiki directory types; index.md updated with
Analyses/Genres/Resources/Standalone sections; _PROGRESS.md updated with expansion phase tracking table.
Next: frameworks-comparison + applying-the-canon syntheses (Session 2).

## [2026-06-01] deep-ingest | Expansion Phase — Sessions 2–5 (Full Library Expansion)
Completed all planned expansion pages in a single extended session. Total: 22 new pages written.

**Syntheses (2):**
  - `syntheses/frameworks-comparison.md` — 5 comparison tables: what-is-a-game (6 frameworks), what-is-fun
    (6 frameworks with resolution of the Koster/MDA/Sellers/flow/Lazzaro/Bartle debate), design process
    (6 frameworks), player frameworks (6 frameworks with practical synthesis), formal vs. craft debate;
    quick-reference decision table (15 situations mapped to tools)
  - `syntheses/applying-the-canon.md` — Part 1: 15-row decision-framework map; Part 2: Hot Potato full
    worked example (MDA, formal elements table, 4 Sellers loops, flow calibration, round interest curve,
    12 applicable Lenses); Part 3: educational games studio application (Koster→learning bridge, SDT in
    educational contexts, MDA for edugames, B2B pitch structure)

**Design Reference (1):**
  - `design-reference/schell-lenses-all.md` — all 100 Lenses in a single scannable page; number, name,
    2-3 key questions, category tag; grouped by chapter

**Entities (8):**
  - `entities/jesse-schell.md` — Lenses, Tetrad, experience-first, 5 kinds of listening; tensions with
    Sellers (craft vs. formal) and MDA (Aesthetics naming collision)
  - `entities/raph-koster.md` — fun=learning, grokking, learnable middle; raphkoster.com; tensions with
    LeBlanc (8 aesthetics as competing vocabulary), Sellers (engagement ≠ fun), Macklin & Sharp (absorption)
  - `entities/katie-salen-eric-zimmerman.md` — meaningful play, magic circle, 3 schemas, game definition,
    embedded/emergent narrative; Salen: Quest to Learn school; Zimmerman: NYU Game Center
  - `entities/tracy-fullerton.md` — playcentric design, formal+dramatic+dynamic elements, 4-step iteration;
    Walden game; USC Games; tensions with Schell (systematic vs. intuitive) and MDA
  - `entities/steve-swink.md` — 3 building blocks, 6 components, 240ms, identity extension; tensions
    with Norman (kinesthetic vs. information-level) and Hodent (motor vs. cognitive)
  - `entities/mark-cerny.md` — Cerny Method (2 polished levels before full production), pillar-based
    design, hardware as game design (PS4/PS5 DualSense); tensions with Schell (milestone vs. loop speed)
  - `entities/nicole-lazzaro.md` — 4 Keys to Fun (Hard/Easy/Serious/People Fun); maps to MDA+Bartle;
    fills the "Serious Fun" gap MDA doesn't name; direct relevance to educational games
  - `entities/sid-meier.md` — "series of interesting decisions"; Civilization as emergence from simple
    rules; strategic depth + accessibility; tensions with Anthropy (instrumental vs. expressive decisions)

**Game Analyses (4):**
  - `analyses/celeste.md` — Assist Mode as ethical accessibility design; death as punchline not punishment;
    narrative-mechanic integration (anxiety as mechanic); strawberries as optional depth without gating;
    direct application to Hot Potato respawn + accessibility design
  - `analyses/portal-2.md` — 4-stage teaching scaffold (observe→attempt→combine→synthesize) across all
    9 chapters; narrative during play via ambient voice + environmental storytelling; co-op as separate
    design problem; aha moment as the reward (Koster grokking at 90s timescale)
  - `analyses/hades.md` — death as diegetically motivated (Underworld pulls you back); narrative through
    all runs including failures; meta-progression unlocks options not power; relationship system as intrinsic
    retention; Heat system as self-selected difficulty; build expression via boon system
  - `analyses/among-us.md` — emergence from asymmetric information + 3 simple mechanics; trust-and-
    betrayal as designed social space; meeting as structured disagreement mechanism; spectator design as
    growth mechanic; cosmetics-only monetization at scale; educational applications (persuasion, deduction)

**Genre Guides (1):**
  - `genres/educational-games.md` — central premise (Koster's fun=learning as bridge); Bloom's taxonomy
    mapped to game mechanics; SDT in educational contexts; 5 design patterns (simulation/challenge/
    narrative/hidden mechanic/failure-safe); B2B market realities (buyer priority chain, procurement);
    standards alignment (UK National Curriculum, Common Core); technical requirements (SCORM/xAPI, COPPA,
    device compatibility, bandwidth); pricing models (5 types); pilot model; 10-item design checklist

**Concept Pages (1):**
  - `concepts/mechanics/multiplayer-systems.md` — fills thesis.md gap; conflict types (direct/indirect/
    coop/asymmetric/mixed); social dynamics problem (king-of-hill, trust/betrayal, blame attribution);
    party game patterns (observable play, short sessions, asymmetric skill range); UE5 netcode for
    Hot Potato (physics replication, server authority for potato position)

Infrastructure: _PROGRESS.md updated; index.md updated with all entities, analyses, genres, syntheses,
concept pages, and new design-reference entry. All expansion phase ⬜ items now ✅ except roguelite.md
(low priority).

**LIBRARY STATUS:** The wiki now contains ~100 pages across all categories. From 17 source PDFs +
17 source summaries + 36 concept pages + 9 design-reference sheets + 6 analyses + 2 genre guides +
9 entities + 4 syntheses + 4 standalone reference pages + 9 Schell chapters = comprehensive game dev
knowledge base. Alexandria-complete for the scope defined.

## [2026-06-01] project | Hot Potato design space created
Added `wiki/project/hot-potato/` — 10 files forming a full project design workspace:
  - `_index.md` — master index + one-line status; how the space works
  - `gdd-overview.md` — logline, 4 design pillars (pillar 5 TBD), target MDA (Fellowship+Challenge),
    scope table (2–6 players, 4–6 chars, 4–6 stages, Steam 2027), audience definition, key references
  - `gdd-mechanics.md` — the potato mechanic (core loop diagram, timer options, score economy options,
    pass mechanic options); brawler layer (movement, combat, recovery); full formal elements table;
    locked vs. open tracking table
  - `gdd-systems.md` — 4-loop hierarchy (interactive/gameplay/round/session) with diagrams; round
    structure table (~90s target, provisional); score economy with banking mechanic; game modes table;
    meta-progression notes (deferred); Steam platform systems
  - `gdd-feel.md` — 3Cs targets (character weight/speed, camera candidates, control layout); 3-state
    potato feedback model (Safe/Warning/Critical with visual+audio+haptic per state); explosion design
    (visible attribution, fast transition, funny not punishing); juice target table; input latency targets
  - `gdd-characters.md` — horizontal variety philosophy; 4 archetype launch roster (Balanced/Holder/
    Passer/Brawler) with potato relationship axis; ability design principles; balance methodology
  - `gdd-stages.md` — potato-first design constraint; stage requirements; 4 stage archetypes
    (Platform Classic/Open Floor/Tight Arena/Dynamic); per-stage balancing checklist
  - `decisions.md` — 3 initial locked/provisional decisions: core mechanic (hybrid brawler+object),
    score-based outcome (not elimination), round structure (~90s provisional)
  - `open-questions.md` — 14 unresolved design questions in 3 tiers (prototype-blocking / alpha /
    deferred); Tier 1: timer duration, score economy, pass mechanic, camera
  - `research.md` — competitor analysis (Smash, Brawlhalla, Gang Beasts, Fall Guys, Jackbox,
    SpeedRunners, Pummel Party, Towerfall, Nidhogg); GDC talks to watch; patterns-to-steal table;
    UE5 technical reference

Updated CLAUDE.md with project space conventions; index.md with full Hot Potato project section.

## [2026-06-01] deep-ingest | Depth Pass — All Wiki Concept Pages Maximally Expanded
Systematic depth expansion across all categories. New page created + 6 legacy stubs fully rewritten + 3 narrative pages substantially expanded.

**New page:**
  - `concepts/mechanics/game-balance.md` — the biggest gap: was a 34-line stub, now full treatment.
    Sellers' 4 balance methods + transitive/intransitive systems (dominant strategy, exploits,
    value assignment methodology); Schell's 12 balance types (Fairness / Challenge vs. Success /
    Meaningful Choices + Triangularity / Skill vs. Chance / Head vs. Hands / Competition vs.
    Cooperation / Short vs. Long / Rewards 8 types / Punishment 6 types / Freedom vs. Control /
    Simple vs. Complex + Elegance / Detail vs. Imagination); methodology (doubling+halving, problem
    statement, playtest with mixed skill); Sellers cost/benefit curves; MDA feedback loop diagnosis

**Narrative pages expanded:**
  - `narrative/story-and-games.md` — added: 5 problems of fully interactive storytelling (unity
    problem, combinatorial explosion with exact numbers 88,573/5.2B outcomes, multiple endings,
    game actions undermine story, dramatic control is the storyteller's tool); the dream vs. reality
    framing; why traditional storytelling applies to games; Lens #65 Story Machine questions
  - `narrative/world-building.md` — added: transmedia worlds (Henry Jenkins concept); Star Wars
    action figures case study (world > story + characters); Pokémon 3-gateway synergy case study;
    binocular effect in game design; Sherlock Holmes pipe-and-cap as transmedia evolution example;
    Santa Claus as oldest transmedia world; Schell's 10 world design tips; Hero's Journey world
    archetypes (mundane vs. special world)
  - Game balance: story-and-games now notes the dual-narrative structure more deeply

**Legacy stubs fully rewritten:**
  - `play-and-culture.md` — 24 lines → comprehensive page. Huizinga's 5 characteristics + function
    of play in culture; Caillois 4 categories (Agon/Alea/Mimicry/Ilinx) + paidia/ludus poles;
    Suits' lusory attitude and 3 components; Schell's toy/play/game/puzzle hierarchy; Koster's
    evolutionary pattern-learning account; Salen & Zimmerman 3 schemas + transforming/non-transforming
    play; Macklin & Sharp 6 play types; design implications; tensions (universal vs. cultural; can
    play be instrumentalized for education?)
  - `fun-and-interactivity.md` — brief stub → comprehensive synthesis. Sellers engagement over
    fun (mental models + arousal + engagement components); Koster pattern learning diagnostic;
    MDA 8 aesthetics as fun-vocabulary; reconciliation table; Hodent ethical engagement dimension
  - `game-analysis.md` — 31 lines → comprehensive page. Fernández-Vara's 3-area framework
    (Context/Overview/Formal Elements) in full depth; procedural rhetoric with 3 examples
    (SimCity, Papers Please, September 12th); diegetic vs. extradiegetic table for all element
    types; methodology (source, play, write critically); game analysis as design skill; all
    connections to MDA, formal elements, meaningful play

Bookkeeping: all new content integrated. Log updated.

## [2026-06-01] project | Hot Potato — GDD real procesado + proyecto reubicado fuera de wiki/
Procesado el GDD completo de Hot Potato (`HotpotatoDesign_2026-06.pdf` + `00Gdd_2026-06.pdf`).
**Corrección fundamental**: HP no es un brawler con objeto físico — es un juego de tag/pillar donde
UN player ES la Patata (chaser). El que es Patata al final del match PIERDE. Los runners ganan FAP
(Fuck Around Points) por trollear. Este cambio invalida todos los GDD files anteriores en wiki/project/.

**Reubicación**: el proyecto se movió a `HotPotato/` en la raíz del vault (fuera de wiki/, dentro del
mismo vault de Obsidian para mantener los links con la teoría).

**GDD files creados en HotPotato/ con info real del documento:**
  - `_index.md` — concepto real: tag game 2–8 players, Patata = chaser, runners ganan FAP
  - `gdd-overview.md` — logline, UPS (5), target audience, plataformas, genre (party tag + parkour),
    art/audio (TBD), pillars (inferidos: caos=mechanic, morir es chiste, movimiento expresivo,
    Patata siempre tiene recursos, todo puede ser un punto)
  - `gdd-mechanics.md` — FAP system completo (tabla de 15 acciones + multiplicadores + deducciones +
    todas las variables), tagging (conditions, terror radius, Patata Dive, all variables), escala
    dinámica Patata (Tier1 @25s ×1.2, Tier2 @40s ×1.5), sistema de objetos (2 slots, replace logic),
    tabla completa de 13 ítems (5 universales, 5 runner-only, 3 patata-only) con descripciones
  - `gdd-movement.md` — run (GASP compatible, aceleración, redirección, slopes, input buffer, VFX/SFX,
    todas las variables), jump (variable height, speed scaling, auto-parkour, wall jump, fast fall+roll,
    wave dash combo), slide (speed inherited, downhill boost, chain moves), parkour (auto-vault, ledge
    grab, wall kick), wave dash (fall→slide→jump, intensity scales with fall height, todas las vars),
    push/interact (push=RT, pull=RMB, range 200u, force 10%, VFX, variables)
  - `gdd-systems.md` — core loop completo (lobby→assignment→120s match→endgame), match timer phases
    (30s+5s con variables detalladas), lobby flow (invite code, playground, slot machine, cage VFX),
    potato assignment variables (bounce intervals, IntervalDecelerationCurve, cage animations),
    leaderboard (LiveLeaderboardUI, TopTrollVFX, podium layout), anti-camp system
  - `gdd-gamemodes.md` — FFA (modo principal), Infected (completo: propagación del rol, 1.5min timer,
    no friendly fire, no XRay, speed+superjump abilities, stun=muerte), TDM/Ranked/Custom (vacíos)
  - `decisions.md` — 7 decisiones iniciales documentadas: tag game (no objeto), FAP, Patata pierde,
    escala dinámica, 2 slots, run always on, wave dash opt-in
  - `open-questions.md` — 18 preguntas en 3 tiers: Tier1 (match duration, anti-camp Patata, giftbox
    density, boomerang vs Patata, wave dash timing), Tier2 (spawn, fall OOB, lootboxes XRay, dummy
    vs XRay, Dive range, Infected respawn cooldown), Tier3 (art style, nombre, 5th pillar, mapas)
  - `research.md` — referentes reales: DBD (terror radius, anti-camp), Mario Kart (items), Gang Beasts
    (tone), análisis de por qué HP NO es un brawler (tabla comparativa), talks relevantes
  - `board-overview.canvas` y `board-sprint.canvas` — canvas actualizados con paths nuevos

CLAUDE.md y index.md actualizados con nueva ubicación HotPotato/.
