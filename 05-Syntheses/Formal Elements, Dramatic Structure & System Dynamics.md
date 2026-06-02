# Formal Elements, Dramatic Structure & System Dynamics

> **What this is:** Everything the canon says about the structural anatomy of games — Fullerton's formal + dramatic + dynamic three-layer framework, system dynamics (objects, properties, behaviors, relationships), and how these three layers work together to produce play. The backbone of analytical game design. Aggregated across s008, s013, s001, s005.

---

## 1. Fullerton's Three-Layer Framework

**Tracy Fullerton** (s008) proposes that every game has three distinct layers that must all work:

```
FORMAL ELEMENTS     → what the game IS (structure)
DRAMATIC ELEMENTS   → what the game FEELS like (experience)
DYNAMIC ELEMENTS    → what the game DOES (behavior in play)
```

These are not in competition — they are three simultaneous, interdependent layers. A game can be formally complete but dramatically empty (chess variants without emotional stakes). It can be dramatically compelling but formally broken (a game with unresolvable ambiguities in the rules). It can be formally and dramatically excellent but dynamically wrong (a game whose run-time behavior contradicts its intended experience).

**The designer must think in all three layers simultaneously.**

---

## 2. Formal Elements — The Structural Layer

**Fullerton's 8 formal elements** (s008, ch.3) — the structural skeleton every game shares:

### Players
Who plays, and how they relate:
- **Number of players:** 1 to N; determines social structure
- **Roles:** all players equal (symmetric) vs. different roles (asymmetric)
- **Interaction patterns:** competitive, cooperative, team competitive, one vs. many, etc.
- **Player entry/exit:** can players join or leave mid-game? With what consequences?

**Design question:** does the player structure create the social relationships the game needs?

### Objectives
What players are trying to achieve:
- **Win/lose condition:** what ends the game with a result
- **Multi-objective:** games can have nested objectives (short-term score + long-term victory condition)
- **Clarity:** players must be able to state the objective at any time

**Failure mode:** players not knowing what they're trying to do in the next 30 seconds = broken objective design.

### Procedures
The legal moves available to players:
- **Starting procedures:** how the game begins
- **Progression procedures:** what players can do during play
- **Resolution procedures:** how conflicts are resolved
- **Ending procedures:** how the game terminates

Procedures are the verbs of the game — they define what actions are possible.

### Rules
Constraints on procedures:
- What is forbidden
- What is required
- What triggers what under what conditions

Rules are the constraints within which procedures exist. The formal relationship:
- Procedures say "the player CAN..."
- Rules say "...BUT only when..."

Rules should be: available (findable), clear (unambiguous), fixed (not arbitrary), and sufficient (covering all possible game states).

### Resources
Things of value that players control, acquire, or spend:
- **Currency:** spendable, countable (gold, points, health)
- **Items:** discrete entities with properties (weapons, tools, cards)
- **Territory/space:** spatial control as a resource (squares, zones, areas)
- **Time:** time as a constrained resource
- **Information:** what players know as a resource (hidden information games)

Resources create the economy of the game. Managing resources IS the gameplay in many game types.

### Conflict
The opposition that makes objectives difficult:
- **Direct conflict:** players acting against each other
- **Indirect conflict:** players competing for the same limited resource
- **Environmental conflict:** the game world itself opposing the player
- **Self-conflict:** games that challenge the player against their own prior performance

Without conflict, there is no challenge. Without challenge, there is no game.

### Boundaries
Where the game world ends:
- **Physical:** the game board, the level geometry, the screen edge
- **Temporal:** when the game ends
- **Conceptual:** the magic circle — what counts as "in the game" vs. "outside it"

Boundaries define the game's possibility space. Everything within the boundaries is game; everything outside is not.

### Outcomes
How the game resolves:
- **Binary (win/lose):** one player wins; all others lose
- **Scalar (ranking):** players ranked by performance
- **Narrative:** the story reaches a resolution (not all games have a mechanical win/lose)
- **Open-ended:** the game can continue indefinitely (sandbox games)

---

## 3. Dramatic Elements — The Experience Layer

**Fullerton** (s008, ch.4) separates dramatic from formal elements because the same formal structure can produce radically different dramatic experiences depending on how the dramatic layer is designed.

### Challenge
Not the mechanical difficulty (that's a formal element) but the *felt* difficulty — the sense that the player is engaged in something genuinely difficult and meaningful.

Challenge requires:
- Uncertainty of outcome (if victory is guaranteed, there's no challenge)
- Player agency (if success doesn't depend on the player, there's no challenge)
- Stakes that the player cares about (if losing doesn't matter, there's no challenge)

**Design question:** does the player feel genuinely challenged, or merely occupied?

### Play
The quality of the activity itself — is it inherently enjoyable to engage with, independent of winning or losing? Schell's "toy" concept (s005, Lens #15) is the same idea: is the core interaction fun to do?

**Design question:** if you removed all the scoring, progression, and winning, would players still want to manipulate the game's elements for their own sake?

### Premise
The fictional frame that makes the formal elements meaningful. Chess's premise (medieval warfare) is thin but sufficient — the pieces are "knights" and "pawns," not "piece A" and "piece B." *The Sims* premise (suburban life) motivates all its formal elements.

**Design question:** does the premise make the formal elements feel like they belong in the same world?

### Character
The agents in the game world — player characters, NPCs, enemies. As covered in the Character Design synthesis, characters must serve multiple functions simultaneously.

**Design question:** do the characters create emotional investment? Do players care about them?

### Story
The sequence of events that constitute the narrative arc — as detailed in the Narrative synthesis. The relationship between formal elements (the game events that happen) and story (the meaning those events carry).

**Design question:** is there a narrative arc that gives the player's actions meaning beyond the mechanical outcome?

### World
The fictional space in which the game takes place — as detailed in the Narrative synthesis. The world must be internally consistent and motivate exploration.

**Design question:** is this world interesting enough to make players want to understand and inhabit it?

---

## 4. Dynamic Elements — The Behavioral Layer

**Fullerton** (s008, ch.5–8) introduces system dynamics as the third layer: what actually *happens* when the formal and dramatic elements run together with real players.

### Objects, Properties, Behaviors, and Relationships

**This is Fullerton's formalism for game objects** — complementary to Sellers' parts/loops/wholes (s001) and Schell's objects/attributes/states (s005, ch.10):

**Objects:** every distinct entity in the game world.
- Players, enemies, items, terrain, projectiles, currency, timers

**Properties:** attributes of objects, each with a current value.
- Player HP (property: health; value: 75); enemy speed (property: velocity; value: 3.0)

**Behaviors:** rules governing how objects act over time.
- "If player HP reaches 0, player dies"
- "Enemy patrols left/right between two points every 3 seconds"
- "Item respawns 30 seconds after pickup"

**Relationships:** connections between objects.
- "This item can only be used by this character type"
- "Killing this enemy increases this currency"
- "This door only opens when this button is pressed"

**Why this formalism matters:** documenting objects, properties, behaviors, and relationships in a structured way (a spreadsheet or design document) allows the designer to:
1. Check for internal consistency (no undefined behavior states)
2. Balance the economy (all exchange rates explicit)
3. Hand off clearly to engineers (every game object is fully specified)

**Sellers' equivalent** (s001, ch.8): parts (objects + properties), behaviors, and relationships are identical to Fullerton's formalism, approached from a systems-thinking angle. Fullerton provides the design-document structure; Sellers provides the systems-thinking rationale.

### System Dynamics

**What emerges when you run the formal elements + dramatic elements together with real players:**
- Unexpected player strategies
- Emergent narratives
- Balance failures
- Feedback loops (positive and negative)
- Player behavior patterns the designer didn't anticipate

System dynamics cannot be predicted entirely from reading the rules. They can only be discovered through playtesting.

**Fullerton's** playcentric conclusion: the only way to know if the dynamics are right is to run the system — build a prototype and watch it. Design on paper is hypothesis; playtesting is experiment.

---

## 5. The Three Layers in Diagnosis

When a game has problems, the three-layer framework helps locate the root cause:

| Symptom | Possible layer | Diagnostic question |
|---|---|---|
| "Players don't know what to do" | Formal (objectives/procedures) | Are objectives clear? Are procedures signified? |
| "The game feels hollow" | Dramatic (premise/story/character) | Is there emotional investment? Does the premise motivate the mechanics? |
| "The game is broken in play" | Dynamic (system behavior) | What unintended behaviors is the system producing? |
| "It's fun but feels random" | Dynamic (feedback loops) | Are reinforcing loops running unchecked? Is there meaningful player agency? |
| "The story and gameplay contradict each other" | Formal-Dramatic mismatch | Do the formal elements produce behavior consistent with the dramatic premise? |

---

## 6. Salen & Zimmerman's Parallel Frameworks

**Salen & Zimmerman** (s013) offer a parallel three-schema framework that maps to Fullerton's three layers:

| Fullerton | Salen & Zimmerman | What it analyzes |
|---|---|---|
| Formal elements | Rules schema | The game as a formal system |
| Dramatic elements | Culture schema | The game as a cultural/meaningful object |
| Dynamic elements | Play schema | The game as an experiential system in action |

The convergence: both frameworks insist that **complete game design and analysis requires all three layers**. Focusing on only one produces incomplete understanding and incomplete design.

---

## 7. Practical Application — The Design Document Structure

**Adams** (s006, ch.2) and **Fullerton** (s008, ch.9) converge on what a game design document should contain:

For each game object: document its **properties** (attributes + values), **behaviors** (rules governing it), and **relationships** (connections to other objects). This is the formal specification that allows engineers to implement and designers to balance.

**Template for a designed entity:**
```
Entity: [name]
Properties:
  - [attribute]: [current value] (min: [X], max: [Y], default: [Z])
  - [attribute]: [current value]
Behaviors:
  - When [condition], [action]
  - [behavior description]
Relationships:
  - Interacts with [entity] via [rule]
  - Cost/reward: [exchange relationship]
```

This level of specification is what separates a design that can be handed to an engineer from a design that exists only in the designer's head.

---

## 8. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Three layers (formal/dramatic/dynamic) are interdependent and all required | s008 |
| Dynamic layer (system behavior in play) can only be discovered through playtesting | s008 |
| Objects, properties, behaviors, relationships = the fundamental specification unit | s008, s001 |
| Formal-dramatic mismatch produces ludonarrative dissonance | s005, s008 |
| The three schemas (Salen & Zimmerman) map directly to Fullerton's three layers | s013, s008 |
| Complete design diagnosis requires locating problems in the correct layer | s008 |

---

## 9. Hot Potato — Three-Layer Analysis

**Formal elements:**
- Players: 2–8; competitive with mixed indirect/direct conflict
- Objectives: survive (don't hold Potato at timer=0); accumulate FAP (highest FAP wins)
- Procedures: move, jump, parkour, tag, use item, interact with environment
- Rules: Potato transfers on contact; FAP earned through troll actions; timer ends the match
- Resources: FAP (accumulating score), items (2-slot system), the Potato role (liability resource)
- Conflict: direct (Potato chases runners); indirect (FAP competition among runners)
- Boundaries: arena bounds; match timer
- Outcomes: ranked by FAP + Potato penalty

**Dramatic elements:**
- Challenge: the chase (Potato vs. runners) + the accumulation game (FAP competition)
- Play: parkour movement should be intrinsically enjoyable as a toy
- Premise: "hot potato" — children's game elevated to competitive parkour brawl
- Character: 8 distinct player avatars with personality through movement
- Story: emergent ("I was chased, passed the Potato right before the timer, and won!")
- World: colorful, chaotic arena that rewards vertical play

**Dynamic elements (to validate through playtesting):**
- Does the Potato scaling actually create catch-up? Or does it enable stalling?
- Does FAP system create trolling diversity, or does one optimal troll strategy dominate?
- Does the item system create triangularity or power imbalance?
- Do social dynamics (king-of-hill targeting) emerge naturally?

**Sources:** s008 (Fullerton) · s013 (Salen & Zimmerman) · s001 (Sellers) · s005 (Schell)

**See also:** [[../10-Library/notes/formal-elements-synthesis]] · [[../10-Library/notes/game-as-system]] · [[../10-Library/notes/meaningful-play-definition]] · [[../00-Atlas/disciplines/Theory]]
