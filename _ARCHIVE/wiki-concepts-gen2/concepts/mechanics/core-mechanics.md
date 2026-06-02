# Core Mechanics

The structural skeleton of a game — what it *is* when aesthetics, story, and technology are stripped away.

---

## What are game mechanics?

**Schell (s005, ch.10):** Game mechanics are "the interactions and relationships that remain when all of the aesthetics, technology, and story are stripped away." They are the core of what a game truly is. Taxonomy is hard because mechanics involve both objective rule sets and the mental models players form — partly living in the subconscious.

**Adams (s006, ch.2 + ch.14):** Core mechanics are "a symbolic and mathematical model that can be implemented algorithmically." They are more specific than the rules — rules say "caterpillars move faster than snails," core mechanics state exactly how fast in centimeters per minute. They generate gameplay by defining the **challenges the player faces** and the **actions the player can take** to overcome them.

**MDA (s011):** Mechanics are "the particular components of the game at the level of data representation and algorithms." The designer reads M→D→A; the player experiences A→D→M. A small mechanical change cascades into new dynamics and different emotional aesthetics.

**Anthropy & Clark (s002, ch.2):** Mechanics are expressed as **verbs** (rules that give the player liberty to act) and **objects** (things the verbs act upon). "Verbs are the rules that allow [the player] to communicate back. The game is a dialogue between game and player."

---

## Schell's six-mechanic taxonomy (s005, ch.10)

Schell identifies six categories of game mechanics. Each is a different lens on the same system.

### Mechanic 1: Space
Every game takes place in a *functional space* — an abstract construct stripped of aesthetics. Functional spaces are:
- **Discrete or continuous** (chess board vs. pool table)
- **Dimensioned** (1D linear loop in Monopoly; 2D grid in chess; 3D in most video games)
- **Bounded**, with areas that may or may not be connected
- **Nestable** — RPGs have an outdoor world with sub-spaces (towns, dungeons) connected only through gateway points, matching how humans mentally compartmentalize space

> 🔎 **Lens #21 — Functional Space.** Is the space discrete or continuous? How many dimensions? Boundaries? Sub-spaces? Is there more than one useful abstraction?

### Mechanic 2: Objects, Attributes, and States
Objects are the **nouns** of game mechanics. Every object has **attributes** (categories of information, e.g. "current speed") and each attribute has a current **state** (e.g. 75 mph). Attributes can be static or dynamic; designers track dynamic ones via **state diagrams**.

Key design decision: **who knows what state?** Schell's "hierarchy of knowers" (God → Game → Players) maps the public/private information structure:
- **Public** — all players see it (chess pieces on the board)
- **Private to one player** — your hand of cards
- **Known only to the game** — hidden AI state, procedural generation
- **Unknown to all** — randomly generated, not yet revealed

> 🔎 **Lens #22 — Dynamic State.** What are the objects, attributes, possible states? What state is public/private/game-only? Would changing who knows what improve the game?

### Mechanic 3: Actions
Actions are the **verbs** of game mechanics. Two kinds:
- **Operative actions** — the base actions a player can take (in checkers: move forward, jump, move backward as king)
- **Resultant actions** — higher-level strategies that *emerge* from combining operative actions (protect a piece, sacrifice to trick opponent, build a bridge)

**Elegant games have many resultant actions per operative action.** Tips for nurturing emergence:
1. Add more verbs (more operative actions → more interaction opportunities)
2. Verbs that act on many objects (one "shoot" verb + many shootable things = rich possibilities)
3. Goals achievable in more than one way
4. Many subjects (more pieces → more possible interactions)
5. Side effects that change constraints (every move in checkers reshapes the threat landscape)

> 🔎 **Lens #23 — Emergence.** How many verbs? How many objects per verb? How many ways to achieve goals? How many subjects? Side effects?
> 🔎 **Lens #24 — Action.** What can players do and what can't they? Ratio of resultant to operative actions?

### Mechanic 4: Rules
Rules are the most fundamental mechanic — they define space, objects, actions, consequences, and goals. Schell adapts **Parlett's 8 rule types**:
1. **Operational** — what players do to play ("move a checker forward")
2. **Foundational** — the underlying mathematical model ("player's power value increases by random 1–6")
3. **Behavioral** — implicit sportsmanship rules ("don't tickle your opponent while they think")
4. **Written** — the rule book
5. **Laws** — formalized sportsmanship for competitive/tournament play
6. **Official** — the merged written+laws, evolving over time
7. **Advisory** — strategy tips, not mechanics
8. **House rules** — player-created modifications (Parlett's "feedback")

**Game modes** split the rules into distinct sets. Sid Meier's rule: players should never spend so much time in a sub-game that they forget the main game.

**Video games = rule enforcer.** Computers make it possible to build games far too complex to enforce manually — but the system must remain transparent enough for players to form rough mental models of how it works.

**Goals (the most important rule):** Good game goals are (1) **concrete**, (2) **achievable**, and (3) **rewarding**. Provide a balance of short-term and long-term goals.

> 🔎 **Lens #25 — Goals.** Concrete, achievable, rewarding? Balance of short/long term? Can players set their own goals?
> 🔎 **Lens #26 — Rules.** Foundational vs. operational? Modes? Who enforces? Any confusions to fix?

### Mechanic 5: Skill
Every game requires players to exercise skills. Three categories:
- **Physical** — dexterity, coordination, endurance (controller manipulation, DDR)
- **Mental** — memory, observation, puzzle solving
- **Social** — reading opponents, bluffing, teamwork (poker is primarily social)

**Real vs. virtual skills.** A character's "sword fighting skill level" is a virtual skill; the player's real skill is button timing. Virtual skills let casual players feel power progression even without real skill growth — but taken too far feel hollow.

> 🔎 **Lens #27 — Skill.** What skills does the game require? Which dominate? Do they match the intended experience?

### Mechanic 6: Chance
Chance interacts with all other mechanics. Uncertainty = surprise = a key source of pleasure. Schell presents 10 probability rules for designers, rooted in the historical invention of probability theory (Pascal–Fermat 1654, prompted by a gambling problem).

Key: designers must sculpt chance deliberately — never assume intuitions about probability are correct.

---

## Adams's five types of core mechanics (s006, ch.14)

Adams (with Joris Dormans) identifies five families of mechanics in video games:

| Type | Description | Examples |
|------|-------------|---------|
| **Physics** | Motion, force, collision | Platformers, racing, shooters |
| **Internal Economy** | Production, consumption, exchange of resources (money, ammo, XP) | RTSes, RPGs, most games |
| **Progression** | Lock-and-key sequences; largely the same path each run | Adventure games, linear action games |
| **Tactical Maneuvering** | Positional advantages in open/semi-open spaces | Chess, Go, Total War |
| **Social Interaction** | Communication, alliances, bluffing, trade between players | MMOs, poker, negotiation games |

The **internal economy** is the most universal: an economy is a system where resources are produced, consumed, and exchanged in quantifiable amounts. Even simple games have one (ammo, health). The economy defines **numeric relationships** (additive, multiplicative, exponential curves) and **symbolic relationships** (state flags: on/off, found/unfound).

Core mechanics "operate behind the scenes to create and manage gameplay… keep track of everything that happens in the game world" (s006, ch.14).

---

## Anthropy & Clark: verbs and objects (s002, ch.2)

A game is a dialogue between game and player; **verbs are the vocabulary of that dialogue**. The key relationships:

- **A verb** = any rule that gives the player liberty to act, to change game state ("jump," "shoot," "flap")
- **An object** = the noun the verb acts upon
- **Verb relationships** create richer choices (moving and shooting in *Space Invaders* interact — aiming requires you to enter enemy fire range)
- Developing verb relationships over the course of a game = how difficulty and narrative co-evolve

Anthropy distinguishes **primary verbs** (Janet's Megablaster = "shoot") from all the secondary interactions that the primary verb creates. The design work is in the *duration, cost, and constraint* around the verb, not just the verb itself.

---

## Fullerton: formal elements (s008, ch.3)

Fullerton lists eight **formal elements** shared by all games:

| Element | Definition |
|---------|-----------|
| **Players** | Who plays, how many, what structure (solo, competitive, cooperative) |
| **Objectives** | What the player is trying to achieve |
| **Procedures** | Steps players take to play (moves, turns, actions) |
| **Rules** | Constraints on procedures |
| **Resources** | Anything of value players control (lives, tokens, territory) |
| **Conflict** | The obstacle that prevents trivial goal achievement |
| **Boundaries** | Where the game ends and the "real world" begins |
| **Outcome** | The quantifiable result (win/lose/score/narrative state) |

Fullerton adds *dramatic elements* (challenge, play, premise, character, story) as a parallel layer — the emotional/narrative wrapper around the formal skeleton (s008).

---

## Macklin & Sharp: six elements (s009)

A lean, action-oriented list:
1. **Actions** — what players do
2. **Goals** — what players are trying to achieve
3. **Rules** — constraints on actions
4. **Objects** — things in the game space
5. **Playspace** — where play happens
6. **Players** — who plays

This maps directly onto Schell's taxonomy: Space = playspace; Objects/Attributes = objects; Actions = actions; Rules ⊇ goals+rules+players.

---

## Salen & Zimmerman: the core mechanic (s013)

Salen & Zimmerman use "core mechanic" to mean the **essential repeated action** at the heart of a game — the activity players perform over and over. It is the atomic unit of gameplay, the interaction that defines the game's identity. Finding the core mechanic = finding what the game *is* (s013, ch.23).

---

## Sellers: core mechanic → core loop → genre (s001)

Sellers defines mechanics as any subsystem players interact with. The **core mechanic** or **core gameplay** = mechanics the player encounters repeatedly throughout a game. These mechanics form the basis of **game genres**:
- Platformer → jumping is the core mechanic (+ double-jump, wall-jump variants)
- RPG → combat + collecting loot + gaining power
- Genre familiarity = shared systemic interactive loops

The core mechanic generates the **core loop** (see [[game-loops]]) — the short repeating cycle that drives session-to-session play (s001).

---

## Synthesis

Across all sources, remarkable agreement on structure:

**Shared skeleton:**
> A game is *players* performing *actions* (verbs) on *objects* (nouns) under *rules* (constraints) toward *goals* (objectives) within a *bounded space*, with *resources* and *chance* modulating the challenge.

**Where sources diverge:**
- **What counts as a "mechanic"?** Schell treats Space, Objects, Rules, Skill, and Chance as mechanics; Adams groups mechanics by domain (physics, economy, etc.); Anthropy focuses on verbs+objects as the atomic unit; Fullerton calls them "formal elements."
- **Realism vs. abstraction.** Adams emphasizes that core mechanics are always *simplified models* of reality — the art is in choosing what to abstract away.
- **Emergence vs. prescription.** Schell foregrounds emergent resultant actions as the hallmark of good design; Adams is more taxonomic and quantitative.

**The key design insight (convergent):** Interesting gameplay comes not from the number of rules, but from **simple rules that interact in complex ways** — a high ratio of resultant/emergent actions to operative actions. This is the same insight as Sellers' systems thinking ([[../../systems-thinking]]) and MDA's dynamics layer ([[../../theory/mda-framework]]).

---

## Key concepts & cross-links

- [[../../theory/mda-framework]] — Mechanics as the bottom layer; M→D→A causal chain
- [[../../theory/formal-elements]] — Fullerton's and Macklin & Sharp's element lists
- [[game-loops]] — core mechanic → core loop → meta loops
- [[game-balance]] — balancing mechanics (transitive/intransitive, curves)
- [[emergence]] — resultant actions, complexity from simple rules
- [[../../theory/meaningful-play]] — how mechanics produce discernable, integrated outcomes
- [[../../theory/systems-thinking]] — games as systems of interacting parts
- [[../../player/flow-channel]] — skill mechanic × difficulty = flow or frustration

## Sources

s005 ch.10 (Schell) · s006 ch.2, ch.14 (Adams) · s002 ch.2 (Anthropy & Clark) · s008 ch.3 (Fullerton) · s009 ch.1 (Macklin & Sharp) · s013 ch.23 (Salen & Zimmerman) · s001 ch.5 (Sellers) · s011 (MDA)
