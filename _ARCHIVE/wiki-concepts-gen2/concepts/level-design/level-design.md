# Level Design

Level design is the craft of creating the spaces, encounters, and sequences through which players experience a game. It is where game design's abstract systems meet the concrete: the specific room, the specific enemy placement, the specific pickup. **Bad level design can ruin a good game. A bad game cannot be saved by good level design.** (s012, ch.1)

---

## Level design vs. game design (s012, ch.1)

Level design is often treated as a subset of game design, but they are distinct disciplines with equal impact. The relationship (Kremers, s012):

- **Game design** defines the rules, mechanics, goals, and systems — the game's "grammar"
- **Level design** implements those rules in specific spaces and sequences — the game's "sentences"

Neither can exist without the other. A strong set of mechanics poorly implemented in levels produces a bad experience; perfectly crafted levels implementing broken mechanics also produce a bad experience. The interrelationship "operates on a deep and fundamental level." (s012, ch.1)

Level design is an **all-encompassing field** — it integrates spatial layout, encounter design, pacing, AI placement, scripted events, lighting, audio, and narrative delivery. It requires deep knowledge of the game's mechanics (to use them correctly), of player psychology (to teach and challenge appropriately), and of visual and spatial design (to create readable, beautiful spaces). (s003, s012)

---

## The primary function of level design: teaching (s012, ch.2)

Kremers' core thesis: **the primary function of level design is to teach players how to interact with the game world.** A level that fails to teach fails at its primary purpose, regardless of visual quality.

Teaching through level design works through:

### Show before ask
Introduce a mechanic through observation before requiring the player to use it. Mario-style design: show the enemy, show how it moves, then put the player in a position to engage. The player's first encounter with any mechanic should be low-stakes enough that failure teaches rather than punishes.

### Scaffolding
Present mechanics in isolation first, then in combination. A trap encountered in isolation (player can study it safely) becomes comprehensible when combined with enemies later. Scaffolding ensures each new challenge is built from understood components. (s012, ch.2)

### Environmental storytelling as tutorial
Objects placed in the environment can teach through implication: a dead character lying next to an enemy teaches that enemy is dangerous; a glow highlighting a ledge teaches that ledges are grabbable. The environment teaches without interrupting the player.

### Reinforcement spacing
Mechanics introduced and then not encountered for a long stretch are forgotten. Level design must re-introduce and reinforce skills at appropriate intervals, building confidence before increasing complexity. Mirrors Hodent's memory principle: the forgetting curve. (s014) → [[../player/player-psychology]]

---

## Level design goals and hierarchy (s012, ch.3)

Kremers identifies a hierarchy of level design goals:

1. **Macro goal**: what the player must ultimately do (complete the mission, escape the building, defeat the boss)
2. **Intermediate goals**: sub-objectives that structure progress toward the macro goal (find the key, clear the room, reach the checkpoint)
3. **Micro goals**: immediate moment-to-moment targets (kill this enemy, avoid this trap, jump this gap)

Good level design ensures players always have a clear micro goal that contributes to an understood intermediate goal, all in service of the macro goal. Loss of clarity at any level produces the "what am I supposed to do?" experience. (s012, ch.3) → [[../theory/meaningful-play]]

---

## Level design structure and methodology (s012, ch.4)

### The level design process
1. **Define goals**: what must the player do? What should they experience?
2. **Create the floorplan**: rough spatial layout (rooms, corridors, connections) — functional space before visual space
3. **Block out**: rough geometry, no detail — test the core gameplay before art
4. **Place gameplay elements**: enemies, pickups, triggers, scripted events
5. **Iterate**: playtest against goals; adjust placement, timing, difficulty
6. **Visual pass**: apply final art, lighting, detail
7. **Final playtest**: verify teaching, pacing, difficulty arc, and clarity

> "Bad level design isn't actually designed — a lot of level design isn't actually designed." (s012, intro)

The block-out step is critical: most level designers who skip directly to visual detail produce levels that look good but play poorly. The floorplan must be validated in gameplay before visual investment is made.

### Single-player vs. multiplayer considerations (s012, ch.5)

Single-player levels can be **authored experiences** — the designer controls the pacing, the revelation sequence, the narrative. Multiplayer levels are **systemic spaces** — the designer creates a balanced arena and lets the player system generate the experience.

Key differences:
- **Sightlines**: single-player uses sightlines to direct attention; multiplayer uses sightlines to create tactical advantage/disadvantage
- **Pacing**: single-player pacing is designed in advance; multiplayer pacing emerges from player confrontation
- **Balance**: multiplayer levels must be balanced for all starting positions and travel routes (s012, ch.5; s003)

---

## Hourences' fundamentals (s003)

Sjoerd Hourences' *The Hows and Whys of Level Design* approaches from a practitioner's perspective, emphasizing the **balance of elements** that must coexist in any level:

### The checklist approach
Before finalizing a level, Hourences recommends checking against a comprehensive list of elements:
- **Spatial flow**: can the player navigate without confusion? Are dead-ends meaningful?
- **Encounter rhythm**: are enemies/challenges spaced with appropriate recovery time?
- **Visual clarity**: can the player read the space — where to go, what is dangerous, what is interactable?
- **Landmark density**: are there enough distinctive reference points that the player can orient?
- **Item placement**: are rewards placed in positions that encourage desired behavior?

### The floorplan
The floorplan is the level's skeleton — the 2D layout of spaces and connections. A good floorplan:
- Enables efficient movement without trivializing challenge
- Creates natural choke points, flanking routes, and strategic variety
- Scales to the game's vision (tight corridors = tension; open spaces = freedom)

### Singleplayer fundamentals
Key concerns for singleplayer level design (s003):
- **AI placement**: enemies positioned to create dramatic tension, not random distribution
- **Scripted events and gameplay variation**: structured surprises that break routine and reinforce narrative
- **Landmarks**: distinctive visual anchors that aid navigation and make the space memorable
- **Difficulty pacing**: challenge should rise and fall in a designed arc — not uniformly increasing (see [[pacing-and-flow]])

---

## The level designer as architect (s005, ch.19)

Schell draws the analogy directly:

> "The primary purpose of architecture is to control a person's experience. For this reason, architects and game designers are close cousins. Both create structures that people must enter in order to use. Neither can create experiences directly — instead, both must rely on the use of indirect control to guide people into having the right kind of experience." (s005, ch.19)

This reframes level design: it is not "placing stuff in a space" but **engineering an experience through spatial design**. Every room, corridor, and junction is a decision about what the player will perceive, feel, and do.

> ⭐ **"One of the keys to good level design is that the player's eyes pull them through the level."** (s005, ch.14)

Visual design is inseparable from functional design — sightlines, lighting, and composition guide movement as effectively as walls and locked doors. → [[spatial-design]]

---

## Indirect control in levels (s005, ch.16)

Schell identifies six methods of indirect control that level designers use constantly:

1. **Constraints** — limit choices so the player goes where intended. An empty room with two doors guides movement. Constraining freedom to curated options feels like freedom while maintaining designer control.
2. **Goals** — give the player clear objectives. The player moves toward goals; the level designer places goals strategically.
3. **Interface** — the UI reveals only what the designer wants revealed; interface design is indirect control over attention.
4. **Visual design** — color, lighting, and composition guide the eye to targets, paths, and hazards. Bright objects attract attention; dark spaces suggest danger or reward.
5. **Characters** — NPCs can explicitly direct ("the treasure is through the door on your left") or implicitly direct (following a friendly NPC leads the player along the right path).
6. **Music** — audio cues signal safety, danger, direction, and emotional context without interrupting play.

Together, these techniques create the **feeling of freedom while maintaining designed experience** — the player believes they are exploring freely while moving through a carefully authored sequence. (s005, ch.16)

---

## Level design and narrative (s012, ch.12; s005)

Level design is a primary delivery mechanism for narrative in games. The environment tells the story through:
- **Environmental storytelling**: objects, damage, and props tell what happened before the player arrived
- **Spatial narrative**: the layout and progression of spaces tells a story (descending deeper into a dungeon; ascending toward a goal)
- **Scripted events**: triggered cutscenes, NPC dialogues, and environmental events advance the plot
- **Discovery**: secrets, collectibles, and optional spaces reward curiosity with lore

The key principle: **don't interrupt play to deliver story**. Narrative delivered during cutscenes where the player is passive competes with the player's desire to act. Environmental narrative and in-play story delivery keep the player in the magic circle while advancing the story. → [[../narrative/story-and-games]]

---

## Key concepts & cross-links

- [[spatial-design]] — the architecture of game spaces; organizing principles
- [[pacing-and-flow]] — interest curves and difficulty arcs across a level
- [[../mechanics/core-mechanics]] — the mechanics that level design teaches and deploys
- [[../player/flow-channel]] — level design is the primary tool for keeping players in the flow channel
- [[../player/player-psychology]] — teaching through level design draws on memory and attention principles
- [[../interface/usability-and-hcd]] — visual clarity and affordance in level design
- [[../theory/meaningful-play]] — levels must produce discernable, integrated outcomes
- [[../narrative/story-and-games]] — levels as narrative delivery

## Sources

s012 (Kremers — Level Design: Concept, Theory, and Practice; game design vs level design, teaching, goals hierarchy, methodology, single vs multiplayer) · s003 (Hourences — The Hows and Whys of Level Design; fundamentals, floorplans, AI placement, singleplayer) · s005 ch.16, ch.19 (Schell — indirect control, architecture analogy, spaces) · s006 ch.12–13 (Adams — spatial design, challenge design) · s008 (Fullerton — playcentric design, iterative development)
