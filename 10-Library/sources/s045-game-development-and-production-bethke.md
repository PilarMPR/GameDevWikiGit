---
id: s045
title: "Game Development and Production"
author: Erik Bethke
year: 2003
type: book
tags: [production, project-management, scheduling, budgets, team, gdd, outsourcing, qa, shipping]
---
# s045 · Game Development and Production

**Full title:** Game Development and Production · **Author:** Erik Bethke (lead developer, *Starfleet Command* series; co-founder Taldren) · **Year:** 2003 (© Wordware Publishing, ISBN 1-55622-951-8) · **Publisher:** Wordware Publishing, Inc.

## Summary

The definitive early-2000s textbook on the production side of game development. Foreworded by Greg Zeschuk and Ray Muzyka (BioWare, *Baldur's Gate*, *NWN*, *KOTOR*). Covers the full lifecycle from requirements capture and design documents through scheduling, task tracking, outsourcing, alpha/beta/ship, and post-release. The book's thesis is that **game development is software development** — applying formal engineering discipline (UML, Gantt/PERT charts, the Unified Process, requirements capture) dramatically improves outcomes. Based on Bethke's personal production experience on *Starfleet Command* and extensive industry interviews. (s045)

## Key claims & concepts

### Core thesis
- **Game development is software development.** "Too often game developers hold themselves apart from formal software development and production methods with the false rationalization that games are an art, not a science." Rigorous, repeatable production methods are needed to ship great games on time and on budget. (s045, Ch.1)
- **The majority of commercial games fail to turn a profit.** ~500,000 units needed to break even on a typical title (in 2003 context); feature creep, poor planning, and scope mismatch are the primary causes. (s045, Ch.3)
- **Successful mega-hits have a narrow, polished feature set** — Doom, Warcraft, Myst, Gran Turismo, Mario 64, The Sims. "Their feature set is small but polished to a superior degree." (s045, Ch.1)

### Project Triangle
- The three constraints are **scope (features), time, and budget** — you can fix two and the third floats. The project triangle shapes all production decisions. (s045, Ch.6)
- Game types mapped to triangle: ultra-low budget (fix scope/budget, float time), fixed budget/deadline (fix both, cut scope), high-profile (fix quality/time, manage budget). Sometimes the right answer is to walk away. (s045, Ch.6)

### Requirements and Design
- **Requirements capture** via UML Use Cases — formalizes "what the game needs to do" before writing design docs. Case studies: Diablo and Gran Turismo use cases. (s045, Ch.7, Ch.15)
- **GDD structure (5 sections):** (1) Defining the Game, (2) Core Gameplay, (3) Contextual Gameplay, (4) Talk Story (narrative/world), (5) Cover Your Assets (asset list). (s045, Ch.8)
- **Technical Design Document (TDD):** object-oriented design, UML class diagrams, requirements analysis, testing plan, build time management. (s045, Ch.9)
- **Vision Document:** written twice; pitch version is 1% of projects that catch the eye; focuses on visuals, tactile feel, mood. (s045, Ch.14)
- **60 Seconds of Gameplay:** articulate the core player activity in 60 seconds — a key design document test. (s045, Ch.16)

### Scheduling and Tracking
- **Gantt and PERT charts** for project planning; task granularity and leveling; resource leveling; task dependencies. (s045, Ch.10, Ch.20)
- **Top Ten Risks Document** — maintained throughout production; updated weekly. (s045, Ch.10)
- **Task visibility as the primary morale/progress tool:** "The Wall" (physical task board), daily journals, milestone orientation meetings, public praise. (s045, Ch.11, Ch.21)
- **Only visible tasks are completed.** Making all tasks visible to the team is critical for progress and motivation. (s045, Ch.21)
- **Time estimation:** task owner estimates their own tasks; two methods (time boxing, task estimating); save plans and compare actuals. (s045, Ch.19)

### Feature Creep and Scope Control
- **Feature creep is the primary cause of late games.** "Primary, Secondary, and Tertiary" feature classification — cut tertiary features first. Feature walking. Regular feature cutting practice. (s045, Ch.22)
- **A slipped game** damages publisher relationships, team morale, and market opportunity. Delays are not free. (s045, Ch.7)

### Shipping
- **Alpha = feature complete.** No new features after alpha; additional content and feature trimming begin. (s045, Ch.13)
- **QA pipeline:** publisher QA, team testing, project-leader testing, automated testing, focus group testing, beta testing (open/closed), manufacturer testing, licensor testing. (s045, Ch.13)
- **Game balance phase** at alpha: tuning and playtesting all systems. (s045, Ch.13)

### Outsourcing (Part IV)
- **Outsource art, audio, cinematics, motion capture, voice, writing, QA.** Do NOT outsource programming (with narrow exceptions). (s045, Ch.12)
- Detailed guidance on outsourcing music (MIDI vs. digitized formats, minutes of music per game type, bid breakdowns), voice (interview with Chris Borders), sound effects (interview with Adam Levenson), writing (Scott Bennie guidelines), cinematics, and motion capture. (s045, Ch.28–33)
- **Fan-generated material:** levels, missions, 3D models — enabling modding extends game life beyond normal product lifetime; plan for user extensibility in the technical architecture. (s045, Ch.34)

### Production Survival Test (Ch.4)
A self-assessment tool with 5 categories: Game Requirements, Planning, Project Control, Risk Management, Personnel. Score predicts project health.

## Chapter overview

| Part / Chapter | Topic |
|----------------|-------|
| Part I, Ch.1–4 | What this book covers; why make games; what makes game dev hard; survival test |
| Part II, Ch.5–13 | Game components, business context, key design elements, GDD, TDD, project plan, task tracking, outsourcing strategies, shipping |
| Part III, Ch.14–25 | Vision doc, requirements gathering, design doc, UML, technical design, time estimates, scheduling, measuring progress, feature creep, alpha/beta/ship, patches/point releases |
| Part IV, Ch.26–34 | Getting a job; starting a company; outsourcing music/voice/SFX/writing/cinematics/motion capture; fan material |

## Connections to wiki

- **Production context:** Pairs with [[s036-agile-game-development-keith|s036 Agile Game Development (Keith, 2021)]] — s045 is the formal/waterfall-leaning 2003 approach while s036 is the Scrum/Kanban adaptation. The two together give the historical arc of game production methodology.
- **Also pairs with s037:** [[s037-the-game-producers-handbook|s037 Game Producer's Handbook (Irish, 2005)]] covers the producer *role* while s045 covers the production *methodology*. s045 is the more engineering-oriented counterpart.
- **GDD format:** The 5-section GDD structure here is a notable data point in the documentation debate across [[../../wiki/concepts/production/documentation|production/documentation]].
- **Feature creep and iteration:** The feature-cutting discipline connects to [[../../wiki/concepts/production/iterative-design|iterative-design]] — scope control is the production side of the design iteration coin.
- **Mega-hits have narrow feature sets:** Directly echoes Schell's simplicity arguments (s005) and the constraint-based coherence of [[s024-shovel-knight-designing-by-accident|s024 Shovel Knight]].

## Notable quotes

- "The mega-hits such as Doom, Warcraft, Myst, Gran Turismo, Mario64, and The Sims are not small games; rather their feature set is small but polished to a superior degree." (Ch.1)
- "Game development is software development. Games are software with art, audio, and gameplay." (Ch.1)
- "Games are deeply rewarding because they appeal on so many different levels… only in a game can a player try different actions, experience different outcomes, and explore a model of a world." (Ch.2)
- "Only visible tasks are completed." (Ch.21)
