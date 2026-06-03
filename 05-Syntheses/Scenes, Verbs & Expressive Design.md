# Scenes, Verbs & Expressive Design

> **What this is:** Everything the canon says about games as an expressive medium — Anthropy & Clark's vocabulary framework (verbs, objects, scenes, context), how mechanics carry meaning, implicit communication through game design, and games as authorial statements. Aggregated across s002, s010, s005, s016.

---

## 1. Games Speak in Verbs

**Anthropy & Clark** (s002, ch.1–2) open with the claim that has the most direct design implication in their entire book:

> *"The most important design question is not 'what does this game look like?' or even 'what does this game say?' It is 'what does this game make the player do?'"*

**Why verbs are the primary unit of meaning:**
- The player's actions are what they experience most directly and most repeatedly
- A game about war where the only verb is "shoot" has nothing to say about war that isn't said by the shooting
- A game about relationships where the only verb is "collect" has nothing to say about relationships
- The verbs *are* the argument; everything else is decoration

**Adams** (s006, ch.14) states the same principle differently: gameplay = challenges + *actions*. The actions are the verbs. The challenges define when and why to perform them.

**Design implication:** before deciding on any other element — premise, aesthetic, narrative, setting — ask: **what will the player repeatedly do?** That verb set is your game's argument about the world.

---

## 2. The Verb Hierarchy

**Anthropy & Clark** (s002, ch.2) distinguish between different levels of verbs:

### Primary Verbs (Operative Actions)
The fundamental moves the player can make. In *Pac-Man*: move. In *Mario*: run, jump. In *Tetris*: rotate, move, drop.

Primary verbs define the game's fundamental character. A game with only one primary verb is focused but shallow. A game with too many primary verbs is overwhelming.

**Quality criteria for primary verbs:**
- They must be learnable in under 30 seconds
- They must feel satisfying to perform as a pure act (the "toy" quality)
- They must combine with each other and with objects to produce interesting situations

### Secondary Verbs (Contextual Actions)
Verbs that only apply in specific contexts: pick up this specific type of object, talk to NPCs, interact with this environmental element.

Secondary verbs expand the vocabulary without increasing the baseline complexity.

### Emergent Verbs (Resultant Actions)
Actions the player discovers from combining primary and secondary verbs in ways the designer may not have explicitly intended. As Schell calls these (s005, ch.10): resultant actions.

**The depth ratio:** the ratio of emergent verbs to primary verbs measures a game's depth. Chess: two primary verbs per piece (move, capture) produce nearly infinite emergent strategic vocabulary.

---

## 3. Objects Give Verbs Context

**Anthropy & Clark** (s002, ch.2): objects exist to give verbs meaning.

> *"Without objects, verbs mean nothing. Without verbs, objects mean nothing."*

**Examples:**
- "Jump" as a verb = meaningless alone. Jump *over an obstacle* = spatial challenge. Jump *to reach a platform* = exploration. Jump *on an enemy* = combat. The same verb carries different meanings with different objects.
- "Collect" as a verb = meaningless alone. Collect *coins* = economic game. Collect *evidence* = mystery game. Collect *survivors* = rescue mission. Same verb, completely different meaning from object context.

**Design tool:** the matrix of verbs × objects defines your game's interaction space. For every (verb, object) pair, ask: what happens? Is that interaction interesting? Is it intended?

**The object's role:**
- **Target:** what the verb acts on (enemy to shoot, platform to jump on)
- **Tool:** what enables the verb (gun enables shooting, jet pack enables jumping higher)
- **Obstacle:** what constrains the verb (wall blocks movement, shield blocks shooting)
- **Resource:** what is earned by performing the verb (coin dropped when enemy is killed)

---

## 4. Scenes — Composition and Rhythm in Time and Space

**Anthropy & Clark** (s002, ch.3) introduce the concept of **scenes** — one of their most underutilized contributions to game design vocabulary:

> *"A scene is how the designer arranges verbs and objects in time and space to produce a specific experience. Scenes have shape: they can be tense or relaxed, fast or slow, open or confined, punishing or forgiving."*

**Scenes in games are equivalent to scenes in film or theater:** a unit of designed experience with a beginning, middle, and end, a specific tone, and a specific purpose in the larger arc.

### Scene Elements

**Shaping:** the overall arc of challenge within a scene — does it start hard and get easier (relief arc)? Start easy and escalate (tension arc)? Stay constant (steady-state)? Have a spike in the middle?

**Pacing:** the tempo of events — how fast are things happening? How much response time does the player have? How densely are challenges packed? (This is the micro-level application of the interest curve from Level Design synthesis.)

**Layering:** multiple systems operating simultaneously within a scene. Combat + platforming + narrative delivery simultaneously creates layered complexity. Pure single-system scenes are simpler but less rich.

**Moments of inversion:** a sudden change that reverses the dynamic of the scene. The player who was hunter becomes hunted. The environment that was safe becomes dangerous. Inversion creates surprise and sustains interest beyond the initial setup.

### Scene Design vs. Level Design

These are different disciplines that must cooperate:
- **Level design** (spatial): where objects are placed, how spaces connect
- **Scene design** (temporal): how events unfold over time

A platformer level is a spatial design; the experience of playing through it is a scene. The level designer places the platforms; the scene designer ensures the sequence of challenges produces the intended emotional arc.

---

## 5. Context — How Framing Changes Meaning

**Anthropy & Clark** (s002, ch.4):

> *"Context teaches the player how to read the game's verbs. The same mechanical action carries completely different meaning in different fictional contexts."*

**The example:** a button press that moves a piece on a chessboard. In chess, it's a strategic move. In a boxing game, it's a punch. In a platformer, it's a jump. The button press is identical; the context (fictional frame) is what makes it meaningful.

**Types of context:**

**Visual context:** what the game looks like. Dark, desaturated, angular = danger and threat. Bright, saturated, rounded = safe and friendly. The visual aesthetic is a context-setter that teaches players how to interpret verbs before they perform them.

**Narrative context:** what story frames the mechanics. A shooting mechanic in a military game = combat. The same mechanic in a game about loss = something else entirely (*Papers, Please* is about stamping papers — but the context makes it devastating).

**Social context:** who the player is with and what the game expects of their relationship. A competitive mechanic in a party context with strangers feels different from the same mechanic with close friends.

**Historical/genre context:** what games preceded this one. Players bring expectations from prior games. *Portal*'s context is "FPS game" — which is why using the portal gun feels initially like a violation of FPS grammar.

---

## 6. Games as Expressive Medium — Making Arguments

**Anthropy & Clark** (s002):
> *"Games carry meaning. Not because designers attach meaning to them as metadata, but because every design decision is an implicit argument. What verbs are available is an argument. What objects exist is an argument. What the game rewards and punishes is an argument."*

**Koster** (s016) reaches the same conclusion from a different direction:
> *"Games can be art, can be socially meaningful, and can carry serious themes — the medium of games is the teaching of patterns, and patterns can encode anything."*

**Procedural rhetoric** (Bogost, via s010):
> *"Games make arguments through their procedures, not just through their representations. A game where violence always solves problems makes an argument about violence. A game where ecological balance leads to prosperity makes an argument about ecology."*

### Intentional vs. Unintentional Arguments

**Every game makes arguments whether or not the designer intends them.** The question is whether the argument is intentional.

**Unintentional argument examples:**
- A "medieval" RPG where every female NPC is a merchant or quest-giver but never a warrior (argument: women don't fight)
- A game where all problems are solved through violence (argument: violence is the primary solution modality)
- A management game where workers have no agency (argument: workers are fungible)

**Intentional argument examples:**
- *Cart Life* (a game about poverty and retail work where the grind mechanics *are* the argument about precarious employment)
- *Papers, Please* (stamping papers becomes complicity in oppression — the verb is chosen precisely because its mundanity amplifies the horror)
- *Spec Ops: The Line* (a third-person shooter that deliberately makes the player's violence feel bad)

---

## 7. Constraint as Expressive Tool

**Anthropy & Clark** (s002): constraints are not limitations — they are design tools.

> *"What a game cannot do is as meaningful as what it can. A game that only lets you talk (no fighting) is making an argument. A game that only lets you watch (no agency) is making an argument. Constraints define meaning."*

**Schell** (s005, ch.16): constraints as indirect control — limiting the player's option set to the most interesting choices. The constraint isn't "you can't do X" — it's "what you *can* do is precisely calibrated to produce the intended experience."

**Examples of expressive constraints:**
- *Passage* (Jason Rohrer): you can only move right (time only moves forward) — the constraint IS the argument about aging
- *Braid*: time can be reversed — but only in specific ways — the constraint creates the puzzle vocabulary
- *Papers, Please*: you can only approve or deny — no third option, no escalation — the constraint creates complicity

---

## 8. The Vocabulary in Practice

**Anthropy & Clark's** framework provides a precise vocabulary for game criticism and design:

| Term | Definition | Design question |
|---|---|---|
| **Primary verb** | The fundamental action the player repeatedly performs | What is the core activity? Does it feel good? |
| **Secondary verb** | Context-specific action | What actions expand the vocabulary in specific situations? |
| **Emergent verb** | Action discovered by combining verbs and objects | How much emergent play does the verb-object matrix produce? |
| **Object** | Anything that verbs act on, with, or toward | What do verbs mean in context of available objects? |
| **Scene** | A unit of designed experience with shape and rhythm | Does each scene have an arc? A tone? A purpose? |
| **Context** | The fictional/visual/social frame that teaches meaning | What does the frame teach the player to expect and value? |
| **Constraint** | A limitation that defines the game's vocabulary | What can't the player do, and why? |

---

## 9. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Verbs (player actions) are the primary unit of meaning in games | s002 |
| Objects give verbs context; without context, verbs are meaningless | s002 |
| Scenes are temporal design units with shape, pacing, and purpose | s002 |
| Context (visual, narrative, social, genre) teaches players how to read verbs | s002 |
| Every design decision is an implicit argument; designers can make those arguments deliberate | s002, s010, s016 |
| Constraints define meaning as much as affordances | s002, s005 |
| The verb-object matrix defines a game's interaction space | s002, s005 |

---

