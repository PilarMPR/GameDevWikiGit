# Deep-Ingest Progress Ledger

Tracks both the chapter-by-chapter deep extraction AND the concept compendium approach.

Legend: ⬜ not started · 🟦 in progress · ✅ done

---

## Concept Compendium (primary approach as of 2026-06-01)

Concept-first pages in `wiki/concepts/<category>/`, each synthesizing all relevant sources.
All 17 PDFs cached as `_work/sNNN.full.txt`.

| Category | Page | Status |
|----------|------|--------|
| mechanics/ | core-mechanics.md | ✅ |
| mechanics/ | game-loops.md | ✅ |
| mechanics/ | game-balance.md | 🟦 (existing stub) |
| mechanics/ | progression-systems.md | ✅ |
| mechanics/ | puzzles.md | ✅ |
| mechanics/ | emergence.md | ✅ |
| feel-and-controls/ | game-feel.md | ✅ |
| feel-and-controls/ | camera-design.md | ✅ |
| feel-and-controls/ | input-and-controls.md | ✅ |
| feel-and-controls/ | feedback-systems.md | ✅ |
| interface/ | ui-design.md | ✅ |
| interface/ | usability-and-hcd.md | ✅ |
| interface/ | interest-curves.md | → see pacing-and-flow.md |
| player/ | player-psychology.md | ✅ |
| player/ | flow-channel.md | ✅ |
| player/ | player-types.md | ✅ |
| player/ | motivation.md | ✅ |
| narrative/ | story-and-games.md | ✅ |
| narrative/ | world-building.md | ✅ |
| narrative/ | characters.md | ✅ |
| narrative/ | indirect-control.md | ✅ |
| level-design/ | level-design.md | ✅ |
| level-design/ | spatial-design.md | ✅ |
| level-design/ | pacing-and-flow.md | ✅ |
| production/ | iterative-design.md | ✅ |
| production/ | playtesting.md | ✅ |
| production/ | documentation.md | ✅ |
| production/ | team-and-culture.md | ✅ |
| theory/ | mda-framework.md | ✅ |
| theory/ | systems-thinking.md | ✅ |
| theory/ | magic-circle.md | ✅ |
| theory/ | meaningful-play.md | ✅ |
| theory/ | theory-of-fun.md | ✅ |
| theory/ | formal-elements.md | ✅ |
| business/ | free-to-play-design.md | ✅ |
| business/ | monetization.md | ✅ |

Concept Compendium + Design Reference + Batch 6 all complete as of 2026-06-01.

---

## Expansion Phase (analyses, genres, resources, syntheses)

| Category | Page | Status |
|----------|------|--------|
| analyses/ | smash-bros.md | ✅ |
| analyses/ | jackbox.md | ✅ |
| analyses/ | celeste.md | ✅ |
| analyses/ | portal-2.md | ✅ |
| analyses/ | hades.md | ✅ |
| analyses/ | among-us.md | ✅ |
| genres/ | party-brawler.md | ✅ |
| genres/ | educational-games.md | ✅ |
| genres/ | roguelite.md | ⬜ (low priority) |
| resources/ | external.md | ✅ |
| entities/ | jesse-schell.md | ✅ |
| entities/ | raph-koster.md | ✅ |
| entities/ | katie-salen-eric-zimmerman.md | ✅ |
| entities/ | tracy-fullerton.md | ✅ |
| entities/ | steve-swink.md | ✅ |
| entities/ | mark-cerny.md | ✅ |
| entities/ | nicole-lazzaro.md | ✅ |
| entities/ | sid-meier.md | ✅ |
| syntheses/ | frameworks-comparison.md | ✅ |
| syntheses/ | applying-the-canon.md | ✅ |
| design-reference/ | schell-lenses-all.md | ✅ |
| wiki/ | glossary.md | ✅ |
| wiki/ | reading-paths.md | ✅ |
| concepts/mechanics/ | multiplayer-systems.md | ✅ |

**Expansion phase complete.** Only remaining: genres/roguelite.md (low priority, write when relevant).

---

## Chapter-by-Chapter Deep-Ingest (secondary, on hold)

Order: **flagships first** (s005, s013, s006, s001, s008), then the rest.

| id | book | pages | chapters | status |
|----|------|-------|----------|--------|
| s005 | The Art of Game Design (Schell) | 518 | 33 | 🟦 10/33 (ch.1–10 done; resume ch.11) |
| s013 | Rules of Play (Salen & Zimmerman) | 695 | ~30+ | ⬜ |
| s006 | Fundamentals of Game Design (Adams) | 578 | ~30 | ⬜ |
| s001 | Advanced Game Design (Sellers) | 456 | 12 | ⬜ (overview-level pages exist) |
| s008 | Game Design Workshop (Fullerton) | 492 | ~16 | ⬜ |
| s002 | A Game Design Vocabulary | 236 | ~8 | ⬜ |
| s003 | Hows & Whys of Level Design | 178 | — | ⬜ |
| s004 | Homo Ludens | 226 | ~12 | ⬜ |
| s007 | Game Feel (Swink) | 380 | ~17 | ⬜ |
| s009 | Games, Design and Play | 289 | ~15 | ⬜ |
| s010 | Introduction to Game Analysis | 362 | ~8 | ⬜ |
| s011 | MDA | 5 | 1 | ✅ (source page is full) |
| s012 | Level Design | 400 | 17 | ⬜ |
| s014 | The Gamer's Brain (notes ed.) | 250 | ~17 | ⬜ |
| s015 | The Design of Everyday Things | 369 | ~7 | ⬜ |
| s016 | A Theory of Fun (Koster) | 299 | ~14 | ⬜ |
| s017 | F2P Handbook (Pt 1/4) | 1 | — | ⬜ |

## Notes
- PDF rendering (poppler) unavailable → extract via pypdf+cryptography (`_tools/book.py`).
- Chapter→PDF-page maps saved as `_tools/map_sNNN.json` as each book is processed.
- All 17 PDFs now cached as `_work/sNNN.full.txt`.
