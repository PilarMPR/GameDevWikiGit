---
id: sellers-four-principal-loops
title: Sellers' Four Principal Loops
type: atomic
disciplines: [mechanics, theory]
sources: [s001]
hp: false
tags: [concept, framework]
status: evergreen
created: 2026-06-02
updated: 2026-06-02
---

# Sellers' Four Principal Loops

Michael Sellers proposes that every game contains four nested conceptual loops that a systems designer must explicitly understand and design. These loops operate at different scales and serve different functions; designing them deliberately produces more engaging, more coherent games than designing mechanics in isolation (s001, ch.7).

## Detail

1. **The game's model loop:** the game's own internal dynamic model — its simulation, state machine, and rules engine running continuously. A narrow probability space (few possible states) = a shallow game.
2. **The player's mental model loop:** the player continuously builds and refines an internal representation of how the game works. Every action+feedback cycle updates this model. Deeper games support hierarchical mental models that keep expanding.
3. **The interactive loop (contains the core loop):** the player↔game coupling: intent → action → state change → feedback → new intent. All interactivity is this loop at some scale. Fast games emphasize action/feedback; strategy games emphasize cognitive loops; social games emphasize social loops. The famous Halo design principle — "3-second loop inside 30-second inside 3-minute, always different" — is an example of nesting interactive loops at multiple timescales (s001, ch.4, citing Griesemer).
4. **The designer's loop:** the designer interacts with the game+player system from *outside*, supplying design → observing player experience → identifying gaps → changing design. This loop is identical to the iterative design process.

## Connections

- [game-loops-definition](game-loops-definition.md) — the basic loop concept
- [reinforcing-vs-balancing-loops](reinforcing-vs-balancing-loops.md) — the polarity of each loop type
- [iterative-design-process](iterative-design-process.md) — the designer's loop in full
- [flow-channel-definition](flow-channel-definition.md) — the mental model loop feeds the flow channel

## Appears in

- [s001-advanced-game-design](../sources/s001-advanced-game-design.md) · ch.7
