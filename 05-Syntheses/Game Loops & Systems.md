# Game Loops & Systems

> **What this is:** Everything the canon says about how games work as dynamic systems — loops, emergence, systems thinking, and the structural mechanics that produce moment-to-moment and long-term engagement. Aggregated across s001, s011, s013, s005, s006, s008, s017.

---

## 1. Games Are Systems

**Michael Sellers** (s001) makes this the load-bearing premise of his entire approach:

> *"Games are systems, and game design is system design."*

A **system** is formally defined as:
> *"A set of parts that together form loops of interaction between them to create a persistent whole; the whole has its own properties and behaviors belonging to the group but not to any single part."* (s001, ch.2)

Three things follow immediately:
1. You cannot understand a game by freezing it and examining its parts in isolation — you must observe it *running*.
2. The game's quality emerges from interactions between parts, not from any individual mechanic.
3. Changing one part cascades through loops to change the whole — never in isolation.

**MDA** (s011) states the same thing differently:
> *"Games are artifacts, not media. Their content is their behavior — the string of events produced when the system runs with a player. That string is unknown until the product runs."*

Both frameworks converge: the game is not its assets, rules, or features. The game is what *happens* when those things interact with a player.

---

## 2. The Four Layers of a Game System (Sellers, s001)

**Parts** — individual entities with properties, behaviors, and relationships.
- Properties: stats, attributes, values (a sword has damage = 50)
- Behaviors: how the part acts over time (enemy patrols, reloads, heals)
- Relationships: how parts connect (sword effectiveness depends on enemy armor)

**Loops** — dynamic feedback relationships between parts that give the system its behavior over time. Two fundamental types:
- **Reinforcing (positive feedback):** output amplifies the condition. XP → level up → kill harder enemies → more XP. Creates snowball dynamics, momentum, power curves. Runaway if unchecked.
- **Balancing (negative feedback):** output reduces the gap. Challenge increases → player practices → skill grows → challenge feels easier. Creates stability, the flow channel, catch-up mechanics.

**Wholes** — emergent properties the system has but no individual part has. Gameplay, balance, and emergent narrative are all properties of the whole, not any component.

**Goals** — the targets toward which the loops drive the system. When game goals, player goals, and designer goals conflict, disengagement results. Alignment between all three is a design requirement, not a bonus.

---

## 3. The Four Principal Loops (Sellers, s001, ch.7)

Every game contains four nested conceptual loops:

### Loop 1: The game's model
The game's own internal simulation running continuously. Must be dynamic — a static system has no gameplay. The **probability space** (range of possible game states) determines meaningful decision count. Narrow probability space = shallow game.

### Loop 2: The player's mental model
The player continuously builds and refines an internal representation of how the game works. Updated with every action+feedback cycle. Deeper games support hierarchical mental models that keep expanding in scope. When the model is accurate, the player feels competent; when it's wrong, they feel cheated.

> ⭐ **Cross-framework:** Sellers' mental model loop ≡ Norman's conceptual model (s015) ≡ Schell's "modeling" cognitive ability (s005, ch.9). All describe how players build an internal map of the system.

### Loop 3: The interactive loop (contains all core loops)
The player↔game coupling:
```
player intent → player action → game state change → game feedback → new player intent
```
This is the *essence of interactivity*. All interaction is this loop at some scale. The game design determines which type dominates:
- Fast-paced games: **action/feedback** loops (where to stand, when to shoot)
- Strategy games: **cognitive** loops (planning, managing, optimizing)
- Social games: **social** loops (coordinating, competing, signaling)

**Bungie's Halo principle** (cited s001): *"3-second loop inside a 30-second loop inside a 3-minute loop, always different."* Stack loops at multiple timescales so engagement operates at every scale simultaneously.

### Loop 4: The designer's loop
The designer interacts with the game+player system from *outside*: design → observe player experience → identify gap between intent and reality → change design → repeat. This is identical to the iterative design process (s008, s009, s005, ch.7). It is a **balancing loop** — the designer reduces the gap between intended and actual experience.

---

## 4. Core Loop Architecture

### The core loop

The tightest repeating cycle of primary player action — what the player does most of the time. Every successful game has a clearly identifiable core loop.

**Anatomy** (s001, s017):
```
player intent → action → game state change → feedback → new intent
```

**F2P loop architecture** (s017) makes this explicit as three nested timescales:

| Loop | Timescale | Example (Clash of Clans) | Purpose |
|---|---|---|---|
| **Core** | Seconds–minutes | Attack → earn coins+elixir | Moment-to-moment fun |
| **System** | Sessions, daily | Spend resources → upgrade → attack better | Progression and goals |
| **Retention** | Weeks, seasons | Rankings, trophies, seasonal content | Long-term investment |

Key sequence: **the core loop must be fun first**. Adding retention mechanics to a bad core loop deepens the problem rather than fixing it (s017). All loop architecture rests on core loop quality.

### Outer loops

Longer-period loops that nest around core loops, providing large-scale structure and retention. The outer loop creates the sense of long-term purpose — the reason to return.

**Clash of Clans example** (s001): Core loop = collect-battle-build. Outer loop = ranking and trophy progression. Each reinforces the other.

**The biology parallel** (s001 footnote): Fast sympathetic ("fight or flight") vs. slow parasympathetic ("rest and digest") mirrors the game design split between fast core loops and slow outer loops.

---

## 5. Mechanics — What Lives Inside the Loops

**Schell's six mechanic categories** (s005, ch.10):

1. **Space** — the abstract topology of play. Discrete vs. continuous, dimensions, boundaries. Tic-tac-toe = 9 zero-D cells in a 2D grid; pool table = continuous 2D. The functional space (s005, Lens #21) is distinct from the visual representation.

2. **Objects, Attributes, States** — the nouns of the game. Every object has attributes (categories) with states (current values). State diagrams design complex behaviors. Critical question: who knows what? Public vs. private vs. secret information completely changes a game (open hand vs. poker hand).

3. **Actions** — the verbs. **Operative actions** (what the designer explicitly provides) vs. **resultant actions** (strategies that emerge from combining operative actions). The ratio of resultant-to-operative actions measures a game's depth. Chess: few operative actions, enormous resultant depth.

4. **Rules** — the constraints that define the possibility space. Complete, understandable, and interesting. Rules create the space within which emergence happens.

5. **Skill** — the player-side challenges: physical (speed, accuracy), cognitive (memory, planning), social (bluffing, cooperation).

6. **Chance** — randomness. Creates uncertainty and variety. Interacts with skill to define the luck-skill balance.

**Adams' five mechanic families** (s006, ch.14) — a complementary type-based taxonomy:

| Family | Domain | Challenge type | Examples |
|---|---|---|---|
| **Physics** | Spatial forces | Timing, precision, trajectory | Platformers, shooters, pinball |
| **Internal economy** | Resources | Optimization, trade-offs | Strategy, RPG, city-builders |
| **Progression** | Unlocking | Exploration, accumulation | Metroidvania, RPG, adventure |
| **Tactical maneuvering** | Positioning in conflict | Spatial + prediction | RTS, tactics, competitive |
| **Social interaction** | People | Reading others, negotiation | Party games, social deduction |

---

## 6. Emergence

### The core principle (s001, s005, s013)

Emergence = when a system produces behaviors not explicitly programmed into any of its parts, arising from interactions between them.

**The operative/resultant ratio** (s005, ch.10, Lenses #23–24): *good operative actions produce many resultant actions*. Simple rules that interact in complex ways are better than complex rules. One rule in *Space Invaders* — aliens speed up as they're thinned — produces two emergent properties: natural game acceleration and increased difficulty at the moment the player is most skilled.

**Five ways to plant emergence** (s005, ch.10):
1. Add more verbs
2. Design verbs that act on many objects (one "shoot" that works on locks, windows, tires, enemies)
3. Design goals achievable multiple ways
4. Increase the number of subjects (players, units, NPCs)
5. Add side effects that change constraints

**Positive vs. negative emergence:**
- *Positive:* players discover strategies the designer never anticipated → deepens the game without new content
- *Negative:* unintended dominant strategies, exploits, balance-breaking interactions → a signal the system has more interactions than the designer anticipated

**Systemic design produces emergence; authoring does not** (s001, intro): an RPG with 50 authored quests produces 50 possible stories. An RPG with 10 interacting faction systems produces millions of emergent stories. Systems scale; authored content doesn't.

---

## 7. Feedback Loops — The Engine of Dynamics

### MDA's Dynamics layer (s011)

MDA places all loops in the **Dynamics** layer — the run-time behavior that emerges when Mechanics act on player inputs over time. The designer can't directly observe Dynamics from reading the Mechanics; they must run the game.

Most dynamics are feedback loops:
- A combat mechanic + player health resource = **survival loop**
- XP mechanic + level threshold = **progression loop**
- Resource-generation + spend mechanic = **economy loop**

### Reinforcing loops in game design

Examples:
- XP → level up → kill harder enemies → more XP (power progression)
- Rich players earn more → buy more property → earn more (Monopoly's fatal flaw)
- Snowball mechanics in MOBA/RTS: early lead → easier kills → bigger lead

Without a countervailing balancing loop, reinforcing loops produce runaway leaders and game collapse. **The Monopoly case study** (s011): the Mechanics create a reinforcing positive-feedback loop that produces wrong Aesthetics — boredom and resentment as losing players wait for the inevitable outcome.

### Balancing loops in game design

Examples:
- Catch-up mechanics (items that target the leader)
- Dynamic difficulty adjustment (game gets harder when winning, easier when losing)
- King-of-the-hill social targeting (players naturally gang up on the leader — an emergent balancing loop)
- Regenerating health (removes punishing accumulation of damage)
- Fog of war (limits information to prevent perfect optimization)

**Designing feedback:** identify what loop types your Mechanics create in the Dynamics layer *before* the intended Aesthetic is ruined. The fix is at the Dynamics level (add a balancing mechanism), not the Mechanics level (patch individual numbers).

---

## 8. Information Design — Who Knows What

A massively underused system lever (s005, ch.10; s013):

| Information state | Effect | Examples |
|---|---|---|
| **Perfect information** | Pure skill; optimal play exists | Chess, Go |
| **Imperfect (shared hidden)** | Uncertainty for all players | Fog of war, RNG |
| **Asymmetric** | Different players know different things | Poker, Among Us, Battleships |
| **Private** | One player knows something others don't | Detective games, hidden traitor |
| **Simultaneous revelation** | All reveal at once | Rock-paper-scissors, Diplomacy |

Changing from public to private information (or vice versa) can transform a game's entire dynamic without changing any other mechanic. *Draw poker vs. stud poker*: same cards, same hands, completely different strategies because information is hidden vs. partially visible.

---

## 9. The MDA Causal Chain

The full MDA model (s011) as a design tool:

```
DESIGNER VIEW:   Mechanics ──────→ Dynamics ──────→ Aesthetics
                 (data + rules)    (behaviors)       (felt emotion)

PLAYER VIEW:     Aesthetics ←───── Dynamics ←───── Mechanics
                 (feels first)     (sees patterns)  (learns rules)
```

**Design experience-first, not feature-first:**
1. Define target Aesthetics: what emotional responses do you want?
2. Derive necessary Dynamics: what behaviors must emerge to produce those emotions?
3. Design Mechanics: what rules produce those dynamics?

This reverses the "feature list" approach. Adding features to Mechanics doesn't guarantee Aesthetic improvement — it must be traced through the Dynamics layer.

**The asymmetry insight:** the designer reads M→D→A; the player experiences A→D→M. These are opposite traversals of the same causal chain. This is why designer assumptions about player experience are so often wrong — the designer is thinking forward from rules while the player is working backward from feeling.

---

## 10. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Games are dynamic systems; design is system design | s001, s013, s011 |
| Balance is a property of the game+player system, not the game alone | s001 |
| Reinforcing loops need countervailing balancing loops | s001, s011 |
| High resultant/operative ratio = depth | s005 |
| The core loop must be fun before anything else is layered | s017 |
| Positive emergence requires designed system interactions | s001, s013 |
| Information asymmetry is a powerful design lever | s005, s013 |
| The designer reads M→D→A; the player experiences A→D→M | s011 |

---

