---
id: s033
title: "Introduction to Game Design, Prototyping, and Development (3rd Edition)"
author: Jeremy Gibson Bond
year: 2023
publisher: Pearson
pages: 1443
type: textbook
---

# s033 — Introduction to Game Design, Prototyping, and Development (3e)

**Author:** Jeremy Gibson Bond · **Publisher:** Pearson, 2023 · **Pages:** 1,443
**Subtitle:** From Concept to Playable Game with Unity and C#

## Summary

The most comprehensive single-volume game design and development textbook in the wiki. Bond integrates design theory, C# programming fundamentals, and five hands-on prototype tutorials (Unity) into one continuous arc. The central theoretical contribution is the **Layered Tetrad** — Bond's synthesis of Schell's Elemental Tetrad (s005) and the MDA framework (s011) augmented with a Cultural layer. The book argues that design, prototyping, development, and balancing are inseparable and iterative; students learn each concept by building something immediately.

## Key claims

- **Layered Tetrad** extends Schell's four elements (Mechanics, Aesthetics, Story, Technology) by wrapping them in three layers (s033, ch.3):
  - *Inscribed Layer* — the designed artifact: rules, content, goals (the game as authored)
  - *Dynamic Layer* — the game in play: emergent behaviors, player experiences, actual dynamics
  - *Cultural Layer* — meaning produced in social context: community, interpretation, cultural impact
- Paper prototyping is a first-class design skill, not a preliminary step to "real" development (s033, ch.9).
- Game testing (playtesting + unit testing) belongs inside the iterative design loop, not after it (s033, ch.10).
- Math and game balance are design problems, not post-production polish (s033, ch.11).
- The Agile/iterative mentality is explicitly taught as a design discipline (s033, ch.14).
- Data-Oriented Design (ch.28) bridges OOP practice toward modern performance patterns — connects to Nystrom (s029) Data Locality.
- Five prototype tutorials (Apple Picker, Mission Demolition, Space SHMUP, Prospector Solitaire, Dungeon Delver) each illustrate distinct mechanic families.

## Chapter structure

**Part I — Game Design and Paper Prototyping (chs. 1–15)**
- Ch.1 Thinking Like a Designer · Ch.2 Game Analysis Frameworks · Ch.3 The Layered Tetrad
- Ch.4 The Inscribed Layer · Ch.5 The Dynamic Layer · Ch.6 The Cultural Layer
- Ch.7 Acting Like a Designer · Ch.8 Design Goals · Ch.9 Paper Prototyping
- Ch.10 Game Testing · Ch.11 Math and Game Balance · Ch.12 Guiding the Player
- Ch.13 Puzzle Design · Ch.14 The Agile Mentality · Ch.15 The Digital Game Industry

**Part II — Programming C# in Unity (chs. 16–28)**
- Unity Editor basics, C# fundamentals, OOP, Data-Oriented Design

**Part III — Game Prototype Tutorials (chs. 29–36)**
- Apple Picker, Mission Demolition, Space SHMUP (×2), Prospector Solitaire (×2), Dungeon Delver (×2)

**Part IV — Next Steps (chs. 37–38)**

**Part V — Online Appendices** (http://book.prototools.net)

## Connections and cross-links

- **Layered Tetrad vs. Elemental Tetrad:** Bond's framework explicitly extends [[../../10-Library/sources/s005-art-of-game-design|Schell (s005)]] ch.4/5 — the four elements remain but gain the Inscribed/Dynamic/Cultural wrapper. Compare MDA's three-layer structure [[../../10-Library/sources/s011-mda-framework|MDA (s011)]]; the Dynamic Layer corresponds to MDA Dynamics, the Inscribed Layer to Mechanics/Rules, the Cultural Layer is Bond's unique addition.
- **Iterative/agile design:** Ch.14 ("The Agile Mentality") and ch.10 ("Game Testing") connect to [[../../10-Library/notes/iterative-design-process|iterative-design-process]], [[../../10-Library/sources/s036-agile-game-development-keith|s036 (Keith)]], and [[../../10-Library/sources/s008-game-design-workshop|s008 (Fullerton)]].
- **Game balance and math:** Ch.11 directly extends [[../../10-Library/sources/s028-players-making-decisions-hiwiller|s028 (Hiwiller)]] and [[../../10-Library/sources/s034-introduction-to-game-systems-design|s034 (Gazaway)]] on spreadsheet-driven balance.
- **Puzzle design:** Ch.13 connects to [[../../wiki/concepts/mechanics/puzzles]].
- **Data-Oriented Design:** Ch.28 is a practical bridge to [[../../10-Library/sources/s029-game-programming-patterns-nystrom|s029 (Nystrom)]] Data Locality and [[../../10-Library/sources/s030-game-programming-in-cpp-madhav|s030 (Madhav)]].
- Dedicated author website: http://book.prototools.net

## Provenance note

3rd edition (2023). Earlier editions (2014, 2018) have the same Layered Tetrad core; this edition adds Unity Hub/Unity 2022 workflow and extended prototype tutorials.
