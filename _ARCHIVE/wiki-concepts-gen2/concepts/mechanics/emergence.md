# Emergence

When a system produces behaviors or properties that were not explicitly programmed into any of its individual parts — where the whole is genuinely greater than the sum of its parts. In games, emergence is both the origin of depth and the source of unintended exploits.

---

## Definition (s001, ch.2; s013)

> "Emergent behavior arises when a system produces behaviors or properties not explicitly designed into any of its parts but arising from the interactions between them." (Sellers, s001, ch.2)

Emergence is a property of **complex adaptive systems**: systems with enough interacting components that their combined behavior becomes unpredictable from any individual component. The classic non-game example: ant colonies produce sophisticated collective behavior (path-finding, waste disposal, task allocation) from ants with simple, individual rules.

In games, emergence means: the designer wrote rules, and the players discovered strategies and behaviors the designer never intended.

---

## The two faces of emergence in games

### Positive emergence: depth without added content
Players discover uses of mechanics that the designer never anticipated, creating meaningful variety and depth from a small set of rules.

Examples:
- **Chess openings**: Fischer Random Chess aside, the rules of chess are unchanged for centuries. Yet billions of games have been played without repetition, because the interaction of six piece types produces combinatorial depth that no explicit authoring could match.
- **Minecraft's player-built structures**: the simple block-placement mechanic produces an unlimited range of creative outputs — cathedrals, working computers, functional games within the game. None of these were programmed; all emerged from simple rules.
- **Emergent strategies in competitive games**: the "camping" and "sniping" behaviors in Quake emerged from weapon-spawn-point interactions. Speedrun routes emerge from precise character physics. Meta-game "tier lists" emerge from character interaction patterns.

> ⭐ **Schell on emergence (s005, ch.10, Lenses #23–24)**: resultant actions are the emergent behaviors that arise when players combine operative (designed) actions in unexpected ways. "Good emergent behaviors are those that make the game deeper and more interesting; bad emergent behaviors are those that make the game trivial or unfair." (s005, ch.10)

### Negative emergence: exploits and dominant strategies
The same systemic property that produces interesting depth also produces exploits — unintended behaviors that break the game's intended balance.

Examples:
- An unintended hitbox interaction allows players to skip content
- A resource duplication glitch breaks the economy
- A dominant strategy makes all other approaches obsolete (overshadowing rather than complementing)
- A feedback loop becomes a runaway winner condition that collapses the game state

Negative emergence isn't a design failure in itself — it's a signal that the system has more interactions than the designer anticipated. The failure is not catching it before release (playtesting scope) or not designing with exploit-resistance in mind.

---

## Why emergence requires systems thinking (s001, s013)

You cannot produce emergence by authoring content explicitly. Emergence only arises from **interacting systems with feedback**:

- An RPG with 50 authored quests produces 50 possible stories. An RPG with 10 interacting faction systems, a weather system, an economy, and an NPC relationship model produces millions of possible emergent stories.
- A game where every enemy has handcrafted behavior produces a fixed challenge set. A game where enemies have simple AI rules that interact with the environment produces emergent tactical situations.

Sellers argues that systemic design is the *only* path to the kind of depth that keeps players engaged long-term: "emergent, engaging game systems can only be created by designing interacting systems, not by hand-authoring every outcome." (s001, intro)

The implication: if you want emergence, design systems. If you want control, author content. Most games require a balance of both. → [[../../theory/systems-thinking]]

---

## Salen & Zimmerman: emergence and complexity (s013)

Salen & Zimmerman analyze emergence through the lens of complexity theory. A game exhibits emergence when:
1. Small numbers of rules produce large numbers of possible game states
2. Player decisions have **meaningful and far-reaching consequences** within the system
3. The system has **interdependencies** — changing one part changes others

They contrast **emergence** with **progression**: progression games advance through designer-authored sequences (a cinematic game with fixed story events); emergent games generate their content through system interaction. Most games have both: authored content sets the stage, and emergent system interactions determine the drama within it. (s013)

---

## The MDA dynamics connection (s011)

MDA's Dynamics layer is where emergence lives: it is the run-time behavior of mechanics acting on each other and on player inputs. The designer creates Mechanics; the Dynamics that emerge are not fully predictable until the game runs. This is precisely why MDA emphasizes that designers must **reason about dynamics explicitly**, not just mechanics — because the emergent layer is where the actual player experience occurs. → [[../../theory/mda-framework]]

---

## Designing for emergence (s001, s005, s013)

### Design principles for positive emergence

**Composable mechanics**: design mechanics that can interact with each other in multiple ways. Each mechanic should be able to combine with several others. This multiplicative composition produces exponentially more possible interactions than additive design. (s005, ch.10 — operative + resultant actions)

**Feedback loops**: systems with feedback (where outputs become inputs) produce far more dynamic behavior than open-loop systems. Reinforcing loops create snowballs; balancing loops create stability. The interaction between them creates interesting emergent dynamics. → [[game-loops]]

**Consistent rules**: emergent behavior requires that rules apply consistently. A mechanic that behaves unpredictably cannot produce stable emergent strategies — it just produces noise.

**Playtest for emergence explicitly**: design the playtest sessions to look for emergent behaviors. Ask: "Did players do anything we didn't expect?" Log these; evaluate whether they are positive (depth) or negative (exploit).

### Designing against negative emergence

**Dominant strategy detection**: if one strategy is strictly better than all others in all situations, design is not deep — it is effectively a solved puzzle. Test explicitly for dominant strategies.

**Feedback loop capping**: many balance problems are runaway reinforcing loops. Build in caps, costs, and balancing feedback loops to prevent any single strategy from spiraling to total dominance.

**Complexity budgeting**: every new mechanic adds potential emergent interactions. More mechanics ≠ more depth if the interactions aren't designed. Fewer, well-chosen mechanics that interact richly produce more positive emergence than many mechanics with limited interaction. (s005, ch.10 — parsimony)

---

## Emergence and replayability (s016, s001)

Koster's observation: games with rich emergence stay fun longer because the player can continue learning new patterns from the same rule set. A chess player who has mastered the opening can still discover new mid-game patterns; a Minecraft player who has mastered simple structures can still discover new engineering patterns.

Sellers connects this to long-term engagement: the game that can generate fresh experiences from its systems — without requiring new content — sustains motivation without the content creation overhead. This is the economic case for systemic design: systems amortize investment across infinite emergent play states. (s001, intro) → [[../../theory/theory-of-fun]]

---

## Key concepts & cross-links

- [[core-mechanics]] — the designed rules from which emergence arises
- [[game-loops]] — feedback loops as the engine of emergent dynamics
- [[game-balance]] — managing emergent dominant strategies and runaway feedback
- [[../../theory/systems-thinking]] — emergence is what systems produce
- [[../../theory/mda-framework]] — Dynamics layer is emergence in action
- [[../../theory/meaningful-play]] — positive emergence produces deeper meaningful play

## Sources

s001 ch.2, intro (Sellers — emergence from interacting systems; systemic design produces emergent content; economic case for systems) · s005 ch.10 (Schell — operative vs. resultant actions; Lenses #23–24; emergence as design goal and hazard) · s013 (Salen & Zimmerman — emergence vs. progression; complexity theory; interdependencies) · s011 (MDA — Dynamics as the emergent layer of game behavior) · s016 (Koster — emergence produces sustained replayability and learning depth)
