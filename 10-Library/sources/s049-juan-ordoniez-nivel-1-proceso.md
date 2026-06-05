# s049 — Level Design: Proceso y relación entre departamentos

**ID:** s049
**Title:** Proceso de level design y relación entre departamentos
**Author:** Juan P. Ordóñez (juanpablo.ordonez@esne.es / @JuanPOrdonez)
**Date:** n.d. (lecture slides, ESNE)
**Type:** Lecture PPTX (52 slides)
**Language:** Spanish
**Link:** n/a (internal course material)
**Related sources:** [[s050-juan-ordoniez-4-flows]] · [[s051-juan-ordoniez-vertical-slice]]

---

## Summary

A university lecture (ESNE) covering the role of the level designer as a cross-departmental integrator, the step-by-step process for creating a level (floor plan → whitebox → tileset → events → playtesting), and an introduction to Agile/Scrum methodology as applied to game development. The core argument is that **the level designer is an integrator** who cannot work in isolation — they depend on, and must continuously communicate with, game design, art, programming, audio, narrative, and production.

---

## Key claims

- **The level designer is an integrator** — they translate the work of every other department into a playable spatial experience (s049).
- **Unique property of videogames:** real-time user interaction where the system reacts to player input; without mechanics there is no game — narrative, art, and audio wrap the interactive core but cannot substitute it (s049, slide 21).
- **Classic error:** treating story as "lo principal" while ignoring interactivity — attributed to writers/aspiring scriptwriters with excessive ego; solution is understanding games as a purely interactive medium, team communication, and a clear product vision (s049, slides 7–19).
- **Level documentation starts late** — the level designer begins work slightly after game design, once core mechanics, rules, dynamics, narrative objectives, and technology constraints are defined (s049, slide 38).
- **Incremental/whitebox-first development:** use greybox (boxing) before creating final assets; enables parallel work, correct spatial measurements for mechanics, and early UX testing of navigation and interaction timings (s049, slide 30).
- **Level production order:** zones distribution map → floor plan (planta) → whitebox → tileset → events/POIs → playtesting (s049, slides 24–36).
- **Playtesting of a level can require changes to the game design layer itself** (s049, slide 36).
- **Typical project milestones:** first playable prototype → MVP → Dev Alpha → Dev Beta → Public Alpha/Beta → Product Release (s049, slide 49).
- **Dev vs. User versions differ:** dev versions are internal, green, tested by QA/focus groups; user versions have most content and are tested by real users who "throw out" automated test results (s049, slide 50).
- **Agile/Scrum:** recommended methodology; values people over processes, working product over documentation, customer collaboration over contract, responding to change over following a plan — the "bible de diseño" does not work (s049, slides 40–47).
- **SCRUM definition attributed to** Nonaka & Takeuchi (early 1980s), analyzing companies like Canon, Honda, Epson; key benefits include flexibility, reduced TTM, higher ROI, better quality per iteration (s049, slide 42).

---

## Structured outline

### The level designer's role
- Described as "integrador" — maps other departments' work into the level environment.
- Does not wait for final versions; uses placeholders.
- Depends on game design for mechanics/rules/dynamics, narrative for story context, art for concept/style, programming for the engine/editor, audio for atmosphere, and production for scheduling.

### The interactive medium
- Games are unique because users interact in real time and the system responds.
- Gameplay must function without narrative/art/audio (could work as a card game).
- Without interaction there is no game.

### Level production workflow
1. Distribution of zones in the world
2. Floor plan (fast, modifiable, carries lots of information before 3D)
3. Whitebox / Greybox (spatial dimensions, mechanics validation, parallel work enabler)
4. Tileset integration
5. Events and Points of Interest
6. Playtesting (may trigger game design revisions)

### Information the level designer needs before starting
- Game design: mechanics, rules, dynamics, gameflow, systems, tables, character/AI definitions, spatial requirements.
- Technology: engine, level editor, libraries.
- Art: style study, lighting type.
- Audio: how audio will be used per situation.
- Production: timeline and constraints.
- Business: important milestones (events, investors, publishers).

### Agile / Scrum methodology
- Agile: people over processes, flexibility, short iterations, constant validation.
- Scrum: sprints (~2 weeks), product backlog, user stories, sprint backlog → shippable product.
- Agile values: code over documentation; customer collaboration; responding to change.
- "Inception Deck" mentioned as a pre-coding alignment tool.

---

## Notable quotes

- "Sin mecánicas, no hay interacción; sin interacción, no es un juego." (s049, slide 21)
- "El juego, si es bueno como juego, debe poder funcionar perfectamente sin narrativa, ni gráficos, ni audio, y hasta podría funcionar en formato cartas." (s049, slide 21)
- "Hay que comprobar que el escenario tiene las medidas necesarias para que las mecánicas se puedan desarrollar correctamente." (s049, slide 30)
- "La 'biblia de diseño' no funciona." (s049, slide 44, paraphrasing Agile Manifesto)

---

## Key concepts & cross-links

- Level designer as integrator: reinforces [[../../wiki/concepts/level-design/level-design]] and [[s050-juan-ordoniez-4-flows]] (same author's companion lectures).
- Whitebox/greybox methodology: connects to [[../../wiki/concepts/level-design/spatial-design]] and [[../../wiki/concepts/production/iterative-design]].
- Agile/Scrum applied to game dev: matches [[../../10-Library/sources/s036-agile-game-development-keith]] (Keith 2021) — both advocate Scrum + Agile thinking; Keith is the full-book treatment.
- "Without mechanics there is no game": aligns with Schell's elemental tetrad primacy of mechanics (s005) and MDA's mechanics-first perspective (s011).
- Milestone taxonomy (Dev Alpha/Beta vs. Public Alpha/Beta): cross-links to [[../../10-Library/sources/s045-game-development-and-production-bethke]] milestone framework.
- Playtesting triggering game design revisions: aligns with [[../../10-Library/notes/iterative-design-process]].
