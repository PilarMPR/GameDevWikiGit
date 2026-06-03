---
type: moc
discipline: mechanics
tags: [moc]
---

# 🧩 Mechanics — Map of Content

**Start here:** [mechanics-definition](../../10-Library/notes/mechanics-definition.md) → [schell-mechanic-taxonomy](../../10-Library/notes/schell-mechanic-taxonomy.md) → [game-loops-definition](../../10-Library/notes/game-loops-definition.md) → [emergence-from-simple-rules](../../10-Library/notes/emergence-from-simple-rules.md) → [game-balance-overview](../../10-Library/notes/game-balance-overview.md)

## Core concepts

- [mechanics-definition](../../10-Library/notes/mechanics-definition.md) — what mechanics are (4 source views)
- [schell-mechanic-taxonomy](../../10-Library/notes/schell-mechanic-taxonomy.md) — Schell's 6 categories (Space, Objects, Actions, Rules, Skill, Chance)
- [adams-mechanic-families](../../10-Library/notes/adams-mechanic-families.md) — Adams' 5 mechanic families
- [mechanics-as-verbs](../../10-Library/notes/mechanics-as-verbs.md) — Anthropy & Clark: verbs + objects
- [formal-elements-synthesis](../../10-Library/notes/formal-elements-synthesis.md) — Fullerton + Macklin & Sharp synthesis

## Game loops

- [game-loops-definition](../../10-Library/notes/game-loops-definition.md) — what a loop is
- [sellers-four-principal-loops](../../10-Library/notes/sellers-four-principal-loops.md) — Sellers' nested 4-loop model
- [reinforcing-vs-balancing-loops](../../10-Library/notes/reinforcing-vs-balancing-loops.md) — positive/negative feedback
- [[game-loop-timescales]] → see game-loops-definition

## Balance and depth

- [game-balance-overview](../../10-Library/notes/game-balance-overview.md) — what balance is and why it matters
- [game-balance-methods](../../10-Library/notes/game-balance-methods.md) — 4 approaches
- [transitive-vs-intransitive-systems](../../10-Library/notes/transitive-vs-intransitive-systems.md) — structural balance
- [meaningful-choices-triangularity](../../10-Library/notes/meaningful-choices-triangularity.md) — the most compelling choice type

## Other mechanics

- [emergence-from-simple-rules](../../10-Library/notes/emergence-from-simple-rules.md) — resultant/operative ratio
- [emergence-definition](../../10-Library/notes/emergence-definition.md) — the systems concept
- [progression-systems-definition](../../10-Library/notes/progression-systems-definition.md) — XP, levels, skill trees
- [multiplayer-conflict-types](../../10-Library/notes/multiplayer-conflict-types.md) — competitive/cooperative/mixed
- [party-game-design-patterns](../../10-Library/notes/party-game-design-patterns.md) — party-game-specific patterns
- [puzzle-design-principles](../../10-Library/notes/puzzle-design-principles.md) — 10 Schell principles

## Schell lens notes (mechanics)

```dataview
TABLE lens FROM "10-Library/notes"
WHERE contains(disciplines, "mechanics") AND lens >= 1 AND lens <= 100
SORT lens ASC
```

## All mechanics notes

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "mechanics") AND type = "atomic"
SORT title ASC
```

## Bridges

- [Mechanics across the canon](../bridges/Mechanics%20across%20the%20canon.md)
- [Iteration & Playtesting](../bridges/Iteration%20%26%20Playtesting.md)
