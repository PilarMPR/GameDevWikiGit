---
id: s022
title: "Into the Breach Design Postmortem"
author: Matthew Davis (Subset Games); co-designer Justin Ma
year: 2019
type: talk
link: https://www.youtube.com/watch?v=s_I07Iq_2XM
gdcvault: https://www.gdcvault.com/play/1025772
slides: https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf
venue: GDC 2019 (game released February 2018)
topics: [strategy-design, perfect-information, difficulty, game-balance, tension-without-rng, emergent-design, minimalism]
---

## Summary

Into the Breach achieves strategic depth not through complexity or randomness, but through perfect information and deliberately constrained design. Before the player acts, the game shows exactly what every enemy will do. This mandatory transparency inverts genre conventions: tension comes not from uncertainty about what will happen, but from the puzzle of whether you can prevent the worst outcome from complete information. The design challenge was making total transparency feel like tension, not a solved puzzle.

## Key claims

- Perfect information (showing all enemy actions before the player moves) inverts strategy genre conventions without eliminating tension. (s022)
- The "real health bar" is the Power Grid (cities), not the mechs — this inversion creates situations where sacrificing a mech is the correct tactical choice. (s022)
- Almost no RNG at the tactical layer; enemy behavior is deterministic. RNG exists at the strategic layer (island selection, rewards) but not turn-by-turn. (s022)
- "Flooding the board with enemies" was the naive solution to difficulty; targeting cities instead created tension without board clutter. (s022)
- Multi-priority decisions (buildings + mechs + objectives all matter) are the source of interesting turns. (s022)
- Mechanical-narrative coupling: the buildings are not backdrop — they are the health bar. (s022)

## Detailed notes

### The perfect information principle

Before the player takes any action on their turn, Into the Breach displays:
- Which tile every enemy will move to
- Which tile every enemy will attack
- The exact damage each attack will deal
- The direction of any knockback

This is mandatory, total information — not an optional hint system. It is the foundational design decision the entire game is built around.

**Why this works against convention:** Most strategy games generate tension through uncertainty — fog of war, random dice outcomes, incomplete intelligence. Into the Breach removes all of this. The tension shifts register: the question is not "what will the enemy do?" (you know) but "can I rearrange the board state to prevent the worst outcome?"

The puzzle each turn: "I can see exactly what bad things will happen if I do nothing. What can I do to prevent the most of them?"

### Failure as the player's fault

Justin Ma: *"We're requiring players to unlearn something taught by almost every other strategy game — that losing your mechs or main characters is the worst thing."*

The Power Grid (city health, 7 points) is the real health bar. Mechs are tools; their loss is recoverable. This inversion creates:
- Situations where the clearly correct move is to sacrifice a mech to save a building
- Failure that is attributable: when the Power Grid depletes, it's because the player made specific identifiable choices, not because RNG generated an unwinnable state
- A different emotional relationship with loss — not "the game cheated me" but "I made the wrong call"

When players lose with perfect information, the failure is their own — and this is the key to making the game feel fair despite being genuinely demanding.

### Tension without RNG

The game achieves tension from:
- **Multi-priority competition:** buildings, mechs, and mission objectives all matter simultaneously
- **Constrained action space:** each mech has one move and one action; the question is which sequence to execute
- **Board geometry:** knockback direction creates combinatorial possibilities
- **Time pressure via turn limits:** some islands have explicit turn deadlines

Matthew Davis: *"The only way to make it difficult was to flood the board with enemies, which becomes needlessly complex."* The solution was making enemy targets the *cities* (the health bar) rather than the mechs — the player is always defending something meaningful, even with just a few enemies on a sparse board.

### Mechanical-narrative coupling

*"Any amount of atmosphere you put over something is shallow compared to tying it to an important mechanic like your health."*

The narrative framing (giant insects attacking human cities in a time-loop future) is not separate from the mechanics — the cities *are* the health bar. When a building is destroyed, the game world loses a physical structure and the player loses a health point. There is no abstraction between diegetic event and mechanical consequence.

This is the design ideal Schell describes as the Elemental Tetrad working together (s005): mechanics, aesthetics, story, and technology reinforcing the same experience. The story isn't flavor on top of a strategy game — it's the reason you care about the buildings.

### Multi-priority decisions

*"When you have buildings, mechs, and objectives all important, it empowers interesting decision-making."*

Interesting decisions emerge when no single priority dominates. If saving the mech always matters more than saving the building, the decision is trivial. If saving buildings always matters more than mission objectives, the decision is trivial. The design work is calibrating weights so that the relative importance of each priority *shifts* based on board state — creating genuine decision variance across turns.

### Cut features

Four years of development, much of it discarded. Features were cut by asking: does this make decisions harder to read? The perfect information constraint is self-tightening: any feature that obscures what is happening undermines the core premise.

The guiding question throughout development: **"does this clarify or obscure the decision space?"**

### Connection to other sources

This talk illustrates MDA (s011) in a very clean form: the Mechanics layer (deterministic enemy telegraph, city health bar, knockback geometry) produces the Dynamics layer (multi-priority puzzle each turn) which produces the Aesthetic layer (tension from clarity, satisfaction from attribution). The mechanics were specifically designed backwards from the desired aesthetic — the feeling of tense, attributable decision-making.

Connects to Sellers' (s001) concept of balance as a property of the complete system: the balance in Into the Breach is not "are all mechs equally strong?" but "does the overall system generate a probability space worth exploring?"

## Notable quotes

- "We're requiring players to unlearn something taught by almost every other strategy game — that losing your mechs or main characters is the worst thing." — Justin Ma
- "The only way to make it difficult was to flood the board with enemies, which becomes needlessly complex." — Matthew Davis
- "Any amount of atmosphere you put over something is shallow compared to tying it to an important mechanic like your health." — Matthew Davis
- "When you have buildings, mechs, and objectives all important, it empowers interesting decision-making." — Matthew Davis

## Related wiki pages

- [[../../05-Syntheses/Game Balance]] — perfect information / transparent difficulty (s022 added)
- [[../../10-Library/notes/game-balance-overview]] — s022 as a case study in tension without RNG
- [[../../10-Library/notes/meaningful-choices]] — multi-priority decisions as the source of interesting turns
- [[../../05-Syntheses/Economy & Resource Design]] — Power Grid as the "real" resource; city health as diegetic economy
- [[../../10-Library/sources/s011-mda-framework]] — MDA as the design logic for the mechanic→aesthetic chain
