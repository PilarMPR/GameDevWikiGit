# Level Design, Pacing & Indirect Control

> **What this is:** Everything the canon says about building spaces, shaping experiences over time, and guiding players without removing their sense of agency. Aggregated across s005, s012, s003, s006, s014, s015.

---

## 1. What Level Design Is

**Rudolf Kremers** (s012, ch.1) defines the relationship clearly:

> *"Game design defines the rules, mechanics, goals, and systems — the game's grammar. Level design implements those rules in specific spaces and sequences — the game's sentences. Neither can exist without the other."*

**Schell** (s005, ch.19) adds the architectural analogy:

> *"The primary purpose of architecture is to control a person's experience. Architects and game designers are close cousins. Both create structures that people must enter in order to use. Neither can create experiences directly — instead, both must rely on indirect control to guide people into having the right kind of experience."*

Level design is **not** "placing stuff in a space." It is engineering an experience through spatial and temporal design. Every room, corridor, junction, and encounter placement is a decision about what the player will perceive, feel, and do next.

---

## 2. The Primary Function: Teaching

**Kremers** (s012, ch.2) argues that the primary function of level design is to **teach players how to interact with the game world**. A level that fails to teach fails its primary purpose regardless of visual quality.

### Teaching methods through level design

**Show before ask:** introduce a mechanic through observation before requiring the player to use it. Classic *Mario* design: show the enemy, show how it moves, then place the player in a position to engage. First encounters with any mechanic should be low-stakes enough that failure teaches rather than punishes.

**Scaffolding:** introduce mechanics in isolation first, then in combination. A trap encountered alone (studied safely) becomes comprehensible when combined with enemies later. Each new challenge is built from understood components.

**Environmental storytelling as tutorial:** objects placed in the environment teach through implication. A dead character next to an enemy teaches that enemy is dangerous. A glow on a ledge teaches it's grabbable. The environment teaches without interrupting the player.

**Reinforcement spacing:** mechanics introduced and then absent for a long stretch are forgotten (Hodent's forgetting curve, s014). Level design must re-introduce and reinforce skills at appropriate intervals, building confidence before increasing complexity.

### The three-goal hierarchy (s012, ch.3)

Good level design ensures the player always has clarity at all three levels:

- **Macro goal** — complete the mission, escape the building, defeat the boss
- **Intermediate goals** — find the key, clear the room, reach the checkpoint
- **Micro goals** — kill this enemy, avoid this trap, jump this gap

Loss of clarity at any level produces the "what am I supposed to do?" experience. Micro goals that don't obviously contribute to intermediate goals feel like busywork; intermediate goals that don't connect to the macro feel arbitrary.

---

## 3. The Level Design Process (s012, ch.4)

The canonical sequence:

1. **Define goals** — what must the player do? What should they experience?
2. **Create the floorplan** — rough spatial layout; functional space (topology) before visual space
3. **Block out** — rough geometry, no visual detail — test gameplay before art investment
4. **Place gameplay elements** — enemies, pickups, triggers, scripted events
5. **Iterate** — playtest against goals; adjust placement, timing, difficulty
6. **Visual pass** — apply final art, lighting, detail
7. **Final playtest** — verify teaching, pacing, difficulty arc, and clarity

> *"Bad level design isn't actually designed. A lot of level design isn't actually designed."* (s012, intro)

**The block-out step is critical.** Designers who skip to visual detail produce levels that look good but play poorly. The floorplan must be validated in gameplay before any art investment.

### Single-player vs. multiplayer

| | Single-player | Multiplayer |
|---|---|---|
| Experience type | Authored — designer controls sequence | Systemic — designer creates arena |
| Sightlines | Directs attention and movement | Tactical advantage/disadvantage |
| Pacing | Designed in advance | Emerges from player confrontation |
| Balance | Challenge curve | Balanced starting positions and routes |

---

## 4. Five Ways to Organize Space (Schell, s005, ch.19)

From most to least designer control:

### 1. Linear
Single path; maximum narrative control; minimum navigational freedom. The player can only go forward (and sometimes back). Used in: most story-driven games, *Crash Bandicoot*, *Guitar Hero*, linear dungeon crawls.

**When to use:** when narrative sequence is critical and the designer must guarantee a specific experience order.

### 2. Grid
Organized on a spatial grid (square, hex, isometric). Players can form an accurate mental map. Easy to reason about tactically. Used in: strategy games, tactical RPGs, classic *Zelda* dungeons, most board games.

**When to use:** when player planning and spatial reasoning are core gameplay.

### 3. Web
Spaces connected by a graph of possible routes. Real navigational choice — some paths are shortcuts; some are more dangerous; some require keys or abilities. Used in: action-adventure hubs, metroidvanias, interconnecting dungeon maps.

**When to use:** when exploration and player agency in navigation are design goals.

### 4. Points-in-space
Discrete locations in a larger field; no required path between them. Open-world default. Used in: open-world games, exploration games, many sandbox environments.

**Requirement:** good landmark design. Players must be able to identify and navigate toward points without a prescribed path. Without landmarks, free-field navigation collapses into confusion.

### 5. Divided spaces
Sub-spaces (rooms, zones, biomes) with controlled connections. The default for indoor environments and most large games.

**Value:** allows the designer to control density (lots happening in small area) and contrast (tense combat space followed by quiet exploration space) at the boundary level.

---

## 5. Sightlines — The Primary Spatial Tool

> *"One of the keys to good level design is that the player's eyes pull them through the level."* (s005, ch.14)

**A sightline is a line of sight from the player's viewpoint to something in the world.** Controlling sightlines controls player movement without explicit instruction.

### The eye moves toward (s003; s014)

- **Contrast** — light objects against dark backgrounds; bright areas at the end of dark corridors
- **Motion** — anything moving draws the eye automatically (biological fact; irreducible)
- **Unique forms** — distinct shapes in a repetitive environment (a red barrel, an unusual structure)
- **Openings** — doorways, gaps, and passages suggest traversable space
- **Light** — bright areas signal safety, reward, goals; dark areas signal danger, mystery, secrets

Place targets, goals, and waypoints at the end of sightlines. The player follows the line naturally and feels like they're exploring freely while moving through a designed sequence.

### Tactical sightlines (multiplayer)

In competitive spaces, sightlines determine tactical advantage. Balance requires:
- No position with too many sightlines (unchallengeably dominant)
- Flanking routes that allow approaches from multiple angles
- Cover positions distributed equitably relative to starting positions

---

## 6. Scale and Spatial Emotion (s005, ch.19; s003)

Spatial scale communicates emotional state directly — before story, before audio, before mechanics:

| Space type | Emotional effect | Design trigger |
|---|---|---|
| Small, low-ceiling | Claustrophobia, intimacy, tension, vulnerability | Horror, safe rooms, storage |
| Large, high-ceiling | Awe, freedom, exposure, vulnerability-at-scale | Boss arenas, outdoor climaxes, exploration |
| Sudden scale change | Strong emotional response — revelation, shift | Emerging from tunnel into open world |
| Symmetric, organized | Control, order, civilization | Friendly territory, shops, hubs |
| Asymmetric, chaotic | Danger, discovery, authenticity | Enemy territory, abandoned spaces |

**Rule:** use scale changes intentionally. A boss arena should feel larger and more imposing than the corridors leading to it. A safe rest area should feel enclosed and calm after an open, dangerous space.

---

## 7. Landmarks and Navigation (s003; s012)

A landmark is a distinctive visual element used as a navigational anchor:
- Helps players orient ("I need to go toward the tower")
- Makes spaces memorable and distinct (reduces "all rooms look the same" disorientation)
- Provides exploration targets ("I want to reach that glowing structure")

**Hierarchical landmark design** (s003):
- **Primary landmarks** (quest targets, level exits) — most visually striking
- **Secondary landmarks** (neighborhood anchors) — moderately distinctive
- **Background elements** — visually coherent, not individually notable

Landmark density is a design dial. Dense landmarks → high readability, risk of visual clutter. Sparse landmarks → exploration required, risk of confusion.

---

## 8. Lighting as Design Tool (s003)

Light is the most powerful compositional tool in 3D level design:

| Light type | Effect | Player response |
|---|---|---|
| Bright, warm | Safety, reward | Move toward |
| Dark | Tension, danger, hidden | Approach cautiously or avoid |
| Rim light (behind silhouette) | Dramatic readability | Notice the subject |
| Cold blue | Threat, alienation | Unease |
| Colored light in neutral space | Marks important interaction point | Investigate |

The player unconsciously follows light. A level designer who controls lighting controls player movement — without walls, signs, or UI.

---

## 9. Interest Curves — Pacing Over Time

**Schell's** most versatile tool (s005, ch.14):

An **interest curve** plots audience interest (y-axis) against time (x-axis) for any entertainment experience. The pattern works at all scales — a 3-minute encounter, a 2-hour session, a 40-hour game.

### Shape of a successful interest curve

```
Interest
  ↑                               G (climax)
  |                         E
  |                   C           H (resolution)
  |   B (hook)     D       F
  |
  A (arrival)
  |
  └────────────────────────────────→ Time

Interest threshold ─────────────────── (player quits below here)
```

- **A** — player arrives with baseline expectations
- **B** — the hook: early spike that earns investment (must happen quickly)
- **C, E** — intermediate peaks (major encounters, reveals, story beats)
- **D, F** — valleys (recovery space; necessary for contrast; not failures)
- **G** — climax: the maximum peak; the game's defining moment
- **H** — resolution: satisfying conclusion

**The interest threshold:** the point where the player changes the channel. Many games have excellent content that no one ever sees because early pacing crosses the threshold first.

### Fractal structure

The most important structural property of well-paced games: **the interest curve pattern repeats at multiple scales**.

- A 60-hour game has an interest curve: hook → rising arc → climax → resolution
- Each chapter has its own: hook → escalation → chapter climax → interlude
- Each level has its own: encounter warm-up → intensifying challenge → boss → reward
- Each combat encounter has its own: warning → escalation → crisis → resolution

This self-similarity across scales is what Schell calls "patterns inside patterns." Zoom into any part of a well-paced game and find the same structure.

### Common pacing failure patterns

| Failure | Description | Fix |
|---|---|---|
| **Spike** | Sudden difficulty jump with no preparation | Scaffold; add warning encounter |
| **Flatline** | Long stretch of uniform challenge | Add escalating sub-objectives; vary encounter types |
| **Early peak** | Hardest encounter too early | Move challenge to later; reduce early intensity |
| **Late sagging** | Difficulty plateaus before the ending | Add late challenges; maintain arc to the end |
| **Bad finale** | Climax doesn't exceed all previous peaks | The final encounter must feel definitively bigger |

---

## 10. Tense and Release — The Micro Pattern

The fundamental unit of pacing (s005, ch.9):

1. **Tension rises** — challenge increases, threat approaches
2. **Peak** — the maximum challenge moment
3. **Release** — tension resolves (boss defeated, puzzle solved, reward collected)
4. **Brief rest** — lower intensity before the next arc

This pattern appears at all timescales. It is the temporal implementation of staying in the flow channel: challenge oscillates within the channel rather than exiting it in either direction.

**Practical tools:**
- Boss encounters as structural anchors (peak at the end of a pacing arc; skill checkpoint)
- Checkpoint placement as tension regulators (permission to attempt a spike without losing large progress)
- Rest and reward spaces after major challenges (physiological rest + emotional punctuation + next-arc setup)
- Opening sequences that hook attention *before* teaching (delayed competence: start dramatic, then pull back to teach)

---

## 11. Indirect Control — Guiding Without Dictating

**Schell** (s005, ch.16):

> *"We don't have to give the player true freedom — we only have to give the player the feeling of freedom. If a clever designer can make a player feel free when really they have very few choices, we have the best of both worlds."*

This is not deception — it is design. The player has already consented to an artificial, rule-bound experience (the lusory attitude). Indirect control shapes that experience so the player moves through a designed path while feeling like they're exploring freely.

### The six methods

**1. Constraints** — limit choices to the ones worth making. Walls, locked doors, impassable terrain. Constraints work best when invisible — when they feel like natural features of the world.

**2. Goals** — pull players toward objectives. A player will move toward a goal; the designer places goals at the end of the intended path.

**3. Interface** — reveal only what you want revealed. The UI determines what information the player has, and therefore what they think about and prioritize.

**4. Visual design** — guide the eye, then the body. Bright areas, contrast, motion, unusual forms, openings all attract the eye. If the designer controls the eye, they control movement — no walls or signs required.

**5. Characters** — players naturally follow human-like agents. Explicit guidance ("go north"), implicit guidance (NPC walks that way), environmental storytelling (dead NPC near a door), character gaze direction.

**6. Music** — the fastest emotional channel. Threatening music = caution; peaceful ambient = relax; directional audio = orientation. The most powerful and most invisible method.

**When all six agree:** guidance is irresistible and feels entirely self-directed. The player arrives at the intended location believing they discovered it themselves.

### Indirect control and narrative

Indirect control is how designers ensure narrative and gameplay point in the same direction. A story that says "go north" but mechanics/level design that make north feel unrewarding → players go elsewhere.

Conversely, indirect control *carries* narrative: moving through a darkening corridor as music becomes ominous delivers narrative purely through environment and audio, without text or dialogue. The player *feels* the story through designed conditions.

---

## 12. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Level design's primary function is teaching | s012 |
| The block-out step must precede art; function before visual | s003, s012 |
| Player eyes pull them through levels — sightlines control movement | s005 |
| Landmarks are required for free-field navigation | s003 |
| Interest curves repeat fractally at multiple scales | s005 |
| Good games oscillate tension — constant challenge doesn't sustain | s005 |
| Indirect control creates the feeling of freedom without sacrificing designed experience | s005 |
| When all six indirect control methods agree, guidance is irresistible | s005 |

---

## 13. Hot Potato — Level Design Implications

| Decision | Rationale |
|---|---|
| Arena-based stages (bounded spaces) | Party game observable play; all players visible; contained conflict |
| Multiple route options per arena | Web-type space; prevents dominant safe zones; supports parkour |
| Distinct visual landmarks per map | Player identification in chaos; "I'm at the red tower, Potato is coming from the left" |
| Vertical layout (parkour affordances) | Sightlines at multiple heights; creates interesting risk/reward for elevation |
| Strong environmental contrast (danger zones obvious) | Player must parse danger quickly; clear visual language |
| Items in visible, accessible-but-contested positions | Triangularity: safe play = no item; risky play = item at center of arena |
| Boss-like finale design in Infected mode | Interest curve structure within a match; escalation to final moment |

**Sources:** s005 (Schell) · s012 (Kremers) · s003 (Hourences) · s006 (Adams) · s014 (Hodent) · s015 (Norman)

**See also:** [level-design-principles](../10-Library/notes/level-design-principles.md) · [spatial-design-principles](../10-Library/notes/spatial-design-principles.md) · [interest-curves-schell](../10-Library/notes/interest-curves-schell.md) · [tense-and-release](../10-Library/notes/tense-and-release.md) · [indirect-control-methods](../10-Library/notes/indirect-control-methods.md) · [Level Design](../00-Atlas/disciplines/Level%20Design.md)
