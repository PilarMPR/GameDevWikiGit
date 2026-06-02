# Game Loops

The beating, cycling heart of a game and the player's experience of it — the recurring feedback structures that define what players actually *do* and what keeps them coming back.

---

## What is a game loop?

A loop in a system is a causal chain that cycles back to its own starting point, creating self-reinforcing or self-regulating behavior over time. In games, loops exist at every scale — from the millisecond action/feedback tick to the month-long progression arc.

**Sellers' definition (s001, ch.4):** "The give-and-take between the player and the game is often referred to as the game's core loop" — a reciprocating loop where the player provides input, the game changes state and provides feedback, which triggers a new player intent. This is the essence of interactivity.

**MDA (s011):** Loops manifest in the **Dynamics** layer — the run-time behavior of mechanics responding to player input over time. Mechanics (data + algorithms) create dynamics (loops, behaviors) that produce aesthetics (felt experience). The designer reads M→D→A; the player experiences A→D→M.

**F2P design (s017):** The core loop is "the repeating cycle of player actions that sustain engagement (e.g., shooting and reloading in an FPS)" — the shortest repeating arc the player inhabits.

---

## Sellers' four principal loops (s001, ch.7)

Every game contains four nested conceptual loops that a systems designer must understand and design:

### 1. The game's model loop
The game has its own internal dynamic model — its simulation, state machine, and rules engine running continuously. This loop must be dynamic and self-perpetuating; a static or purely linear system has no gameplay. The richness of the **probability space** (the range of possible game states) determines how many meaningful decisions the player can make. A narrow probability space = a shallow game.

### 2. The player's mental model loop
The player continuously builds and refines a **mental model** of the game — a simplified internal representation of how it works (see [[../player/player-psychology]]). This model is updated with every action+feedback cycle. The player uses it to form new intent, take action, get feedback, update the model — a self-improving cognitive loop. Deeper games support **hierarchical mental models** where the player's model continuously expands in scope and depth.

### 3. The interactive loop (contains the core loops)
The player↔game coupling: player intent → player action → game state change → game feedback → new player intent. This is "the essence of interactivity" (s001, ch.4). All interactivity is this loop at some scale. The game design determines which interaction type dominates:
- Fast-paced games → **action/feedback** loops dominate (where to stand, when to shoot)
- Strategy games → **cognitive** loops dominate (planning, managing, optimizing)
- Social games → **social** loops dominate (coordinating, competing, signaling)

Bungie's famous Halo design principle: "3-second loop inside a 30-second loop inside a 3-minute loop, always different" — stacking loops at multiple timescales so engagement operates at every scale simultaneously (s001, ch.4, citing Griesemer).

### 4. The designer's loop
The designer interacts with the game+player system from *outside* it. They supply design → observe player experience → identify gap between intent and reality → change design → repeat. This is a **balancing loop** (the designer reduces the gap between intended and actual experience). This is the same as the iterative design process (see [[../production/iterative-design]]).

---

## Three kinds of gameplay loops (s001, ch.7)

Within the interactive loop, Sellers identifies three functional kinds:

### Core loops
"What the player does most of the time." The tightest repeating cycle of primary action. In a combat RPG: fight → gain resources/XP → use resources → fight again. In Clash of Clans: **Battle** (attack → get coins + elixir) ↔ **Build & Train** (spend resources → strengthen base).

Core loops cycle at **different timescales** (fast: action/feedback; medium: cognitive; slow: social/strategic). Which timescale dominates defines the game's character.

Abstract core loop anatomy (s001):
```
Player intent → Player action → Game state change → Game feedback → new Player intent
```

### Outer loops
Longer-period loops that nest around core loops, providing large-scale structure and retention. A combat core loop might have an outer loop of character progression, faction reputation, or seasonal ranking. The outer loop creates the sense of long-term purpose that makes a player return.

**Clash of Clans example (s001):** Outer loop = ranking and trophy progression. Core loop = collect-battle-build. Each reinforces the other: winning battles increases rank (outer loop), which requires stronger troops and base (drives more core loops).

**Biology parallel (s001 footnote):** Fast sympathetic ("fight or flight") vs. slow parasympathetic ("rest and digest") mirrors the game design split between fast core loops and slow outer loops.

### Reinforcing vs. balancing loops
Every loop is either:
- **Reinforcing (positive feedback):** output amplifies the condition. XP → level up → can kill harder enemies → more XP. Runaway unless balanced elsewhere.
- **Balancing (negative feedback):** output reduces the condition. Harder challenge → more practice → more skill → challenge feels easier. Stabilizing; creates the flow channel (see [[../player/flow-channel]]).

Good game design balances reinforcing loops (that create a sense of power and progress) against balancing loops (that maintain challenge and prevent dominance). The **game economy** (see [[core-mechanics]] → internal economy) is largely a system of reinforcing and balancing loops on resources.

---

## The interaction timescales (s001, ch.4)

Sellers maps interactive loops to different cognitive registers:

| Timescale | Loop type | Example |
|-----------|-----------|---------|
| Sub-second | Action/feedback | Aiming, jumping, shooting |
| Seconds | Action/feedback + short cognition | Evaluating whether to shoot or dodge |
| Minutes | Tactical/short-term cognitive | Clearing a room, using a skill combo |
| Tens of minutes | Strategic/long-term cognitive | Managing resources, planning build order |
| Hours/sessions | Social + goal-seeking | Leveling, guild progression |

"Moment-to-moment gameplay" refers to the fast action/feedback tier — what the player is doing in *every* moment. This is the **carrier wave** on which all other loops ride. "Games that do not provide regular, timely feedback and opportunities for player action risk allowing the player to become bored and disengaged" (s001, ch.4).

---

## MDA: mechanics generate dynamics (loops) (s011)

In MDA's framework, **Dynamics** are the run-time behavior that emerges from Mechanics — and most dynamics are loops:
- A combat mechanic (damage formula) + player health resource creates a **survival loop**
- An XP mechanic + level threshold creates a **progression loop**
- A resource-generation mechanic + spend mechanic creates an **economy loop**

From the designer's view (M→D→A), designing loops = designing mechanics carefully enough that the right dynamics emerge. From the player's view (A→D→M), the aesthetics (fun, tension, satisfaction) arise from experiencing those loops.

---

## F2P loop architecture (s017)

F2P games make loop architecture explicit as a design discipline:

1. **Core loop** (moment-to-moment) — the fundamental "action → reward" cycle, e.g. fight → loot
2. **System loop** (mid-term) — progression systems, crafting, skill trees that connect core loops to long-term goals
3. **Engagement/retention loop** (long-term) — daily rewards, seasons, live events, social ranking

The key sequence: **Core loop must be fun first** → then add system layer → then add retention layer. Adding retention mechanics to a bad core loop only deepens the problem (s017).

The "compulsion loop" (goal → action → reward) is the psychological mechanism underneath F2P retention — dopamine-driven reinforcement. Ethical design requires ensuring this serves genuine player enjoyment rather than exploiting habit formation (s017).

---

## Loop design principles (cross-source)

**Emergent actions from simple mechanics (s005, ch.10):** Good operative actions produce many resultant actions — the ratio of resultant-to-operative actions measures loop richness. Simple rules that interact in complex ways are better than complex rules (see [[core-mechanics]]).

**Goals and loops are inseparable (s001, ch.7):** A loop without a goal is meaningless activity. Every core loop needs a **clear goal** the player is working toward, preferably with short-term and long-term versions (Schell's Lens #25: Goals). The loop is the *how*, the goal is the *why*.

**Loops need tension and release (s005, ch.9):** Flow requires cycles of challenge (tension) and reward/downtime (release). The loop structure creates natural "tense and release" rhythms — Schell uses the term to describe how games maintain the flow channel.

**Loops across books:** The core loop ≡ the essential repeated action in Salen & Zimmerman's "core mechanic" (s013) ≡ Fullerton's cycle of procedures/actions (s008) ≡ the interaction at the center of gameplay in Adams' core mechanics (s006, ch.14).

---

## Key concepts & cross-links

- [[core-mechanics]] — what lives inside loops; operative and resultant actions
- [[game-balance]] — tuning the reinforcing/balancing structure of loops
- [[progression-systems]] — outer loops; how power curves and XP interact
- [[../player/flow-channel]] — the flow channel as a macro-level balancing loop
- [[../player/player-psychology]] — how mental models build through loop iteration
- [[../theory/mda-framework]] — Dynamics layer = runtime loop behavior
- [[../theory/systems-thinking]] — reinforcing/balancing loops in complex systems
- [[../theory/the-four-principal-loops]] — the existing wiki concept (Sellers' four loops)
- [[../production/iterative-design]] — the designer's loop = iterative design process

## Sources

s001 ch.4, ch.7 (Sellers) · s011 (MDA) · s017 (F2P handbook) · s005 ch.10 (Schell) · s013 ch.23 (Salen & Zimmerman) · s006 ch.14 (Adams) · s008 ch.3 (Fullerton)
