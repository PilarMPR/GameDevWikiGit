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

## New Sources Batch — s027–s054 (added 2026-06-05)

PDFs staged at `_work/staging/sNNN-*.pdf`. All need source pages created.
Process with: `PYTHONIOENCODING=utf-8 python -c "import pypdf; ..."` or Read tool directly.

| id | file | title | category | status |
|----|------|-------|----------|--------|
| s027 | s027-level-up-scott-rogers.pdf | Level Up! The Guide to Great Video Game Design | design | ✅ |
| s028 | s028-players-making-decisions-hiwiller.pdf | Players Making Decisions | design | ✅ |
| s029 | s029-game-programming-patterns-nystrom.pdf | Game Programming Patterns | programming | ✅ |
| s030 | s030-game-programming-in-cpp-madhav.pdf | Game Programming in C++ | programming | ✅ |
| s031 | s031-multiplayer-game-programming.pdf | Multiplayer Game Programming | programming/networking | ✅ |
| s032 | s032-writing-interactive-music-sweet.pdf | Writing Interactive Music for Video Games | audio | ✅ |
| s033 | s033-intro-game-design-prototyping-3e.pdf | Introduction to Game Design, Prototyping and Development 3e | design/Unity | ✅ |
| s034 | s034-introduction-to-game-systems-design.pdf | Introduction to Game Systems Design | design/systems | ✅ |
| s035 | s035-penner-easing-tweening.pdf | Penner Easing Functions (ch.7) | programming/animation | ✅ |
| s036 | s036-agile-game-development-keith.pdf | Agile Game Development with Scrum 2e | production | ✅ |
| s037 | s037-the-game-producers-handbook.pdf | The Game Producer's Handbook | production | ✅ |
| s038 | s038-3d-user-interfaces.pdf | 3D User Interfaces 2e | UI/UX | ✅ |
| s039 | s039-unreal-engine-vr-cookbook.pdf | Unreal Engine VR Cookbook | engine/VR | ✅ |
| s040 | s040-unity-game-dev-24-hours.pdf | Unity Game Development in 24 Hours (Sams) | engine/Unity | ✅ |
| s041 | s041-roblox-game-dev-24-hours.pdf | Roblox Game Development in 24 Hours | engine/Roblox | ✅ |
| s042 | s042-practical-augmented-reality.pdf | Practical Augmented Reality | AR/XR | ✅ |
| s043 | s043-augmented-reality-pearson.pdf | Augmented Reality (Pearson, 346 MB — large) | AR/XR | ✅ |
| s044 | s044-pragmatic-programmer-ch4.pdf | The Pragmatic Programmer ch.4 | programming/craft | ✅ |
| s045 | s045-game-development-and-production-bethke.pdf | Game Development and Production (Bethke) | production | ✅ |
| s046 | s046-digital-vfx-and-compositing.pdf | Digital Visual Effects and Compositing | art/VFX | ✅ |
| s047 | s047-guiltygear-bone-placement-tips.pdf | GuiltyGear Xrd — Bone Placement Tips for Action | art/rigging | ✅ |
| s048 | s048-guiltygear-modeling-for-skinning.pdf | GuiltyGear Xrd — Modeling for Skinning | art/rigging | ✅ |
| s049 | s049-juan-ordoniez-nivel-1-proceso.pptx | Level Design: Proceso y relación con departamentos (Ordóñez) | level design | ✅ |
| s050 | s050-juan-ordoniez-4-flows.pdf | Level Design: Los 4 flows (Ordóñez) | level design | ✅ |
| s051 | s051-juan-ordoniez-vertical-slice.pdf | Level Design: Vertical Slice (Ordóñez) | level design | ✅ |
| s052 | s052-mecanicas-de-juegos.pdf | Mecánicas de Juegos (Corregido) | design/Spanish | 🟦 IMAGE-ONLY PDF — zero extractable text; OCR needed |
| s053 | s053-guidelines-hci-2015.pdf | Guidelines for Human-Computer Interaction 2015 | UI/UX | ✅ |
| s054 | s054-casual-gaming-trends-2022.pdf | Casual Gaming Trends Snapshot Report 2022 | industry/data | ✅ |

**Recommended ingest order:** s027 → s029 → s030 → s032 → s036 → s039 → s028 → s031 → s033 → s034 → s037 → s038 → s040 → s041 → s042 → s044 → s045 → s046 → s047 → s048 → s035 → s043 → s050 → s051 → s049 → s052 → s053 → s054

## PDF Copies of Existing Sources (available for deep ingest)

Physical PDFs now in `_work/staging/` for chapter-by-chapter deep ingest of existing sources:
- `s001-advanced-game-design-COPY.pdf` → s001 (Sellers)
- `s002-a-game-design-vocabulary-COPY.pdf` → s002 (Anthropy & Clark)
- `s003-hows-and-whys-COPY.pdf` → s003 (Kremers)
- `s006-fundamentals-of-game-design-COPY.pdf` → s006 (Adams)
- `s007-game-feel-swink-COPY.pdf` → s007 (Swink)
- `s008-game-design-workshop-COPY.pdf` → s008 (Fullerton)
- `s009-games-design-and-play-COPY.pdf` → s009 (Macklin & Sharp)

## Notes
- PDF rendering (poppler) unavailable → use pypdf directly or Read tool on extracted files.
- Chapter→PDF-page maps saved as `_tools/map_sNNN.json` as each book is processed.
- All 17 original PDFs cached as `_work/sNNN.full.txt`.
- s043 (AR Pearson) is 346 MB — use page ranges when reading.
- s033 (Intro Game Design Prototyping) is 108 MB — use page ranges.
- s049 is a PPTX, not PDF — extract text via `python-pptx` or PowerShell XML.
