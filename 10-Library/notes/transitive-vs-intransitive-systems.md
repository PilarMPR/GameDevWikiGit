---
id: transitive-vs-intransitive-systems
title: Transitive vs. Intransitive Systems
type: atomic
disciplines: [mechanics]
sources: [s001, s005]
hp: true
tags: [concept]
status: evergreen
created: 2026-06-02
updated: 2026-06-02
---

# Transitive vs. Intransitive Systems

A **transitive** system has an ordered power hierarchy: A > B > C > D. A **intransitive** system has a cyclic relationship: A beats B, B beats C, C beats A — like rock-paper-scissors. Intransitive design is the structural solution to dominant strategies: when no option is universally superior, the meta cannot be solved, and depth persists (s001, ch.9; s005, ch.11).

## Detail

- **Transitive systems** are natural but dangerous: as players discover the power ordering, lower-tier options become irrelevant. The dominant strategy problem emerges when one option is strictly better than all others in all situations.
- **Dominant strategy:** "Once a dominant strategy is discovered, the game is no longer fun, because the puzzle of the game has been solved — there are no more choices to make." (s005, ch.11). Exploits are dominant strategies hidden in the system.
- **Intransitive systems:** cyclic relationships mean every option has a counter. Rock-paper-scissors: no single choice wins universally. Applied to game units: infantry beats cavalry, cavalry beats archers, archers beat infantry (classic RTS triad).
- **Design application:** use intransitive triads for characters, weapons, strategies, or game modes. The players must always evaluate *context* rather than simply picking the "best" option.
- **Balancing transitives:** assign numerical value to each attribute, sum per option, adjust until totals are equivalent — then validate with playtesting. The model informs the prototype; the prototype informs the model (s001, ch.9; s005, ch.11 — *Biplane Battle* example).

## Connections

- [[game-balance-overview]] — this is one of the core balance structures
- [[game-balance-methods]] — mathematical modeling for transitive balance
- [[emergence-from-simple-rules]] — intransitive triads produce emergent strategic depth
- [[meaningful-choices-triangularity]] — triangularity requires a form of intransitive risk/reward

## Appears in

- [[../sources/s001-advanced-game-design]] · ch.9
- [[../sources/s005-art-of-game-design]] · ch.11
