# Indirect Control

The designer's primary tool for guiding player behavior and narrative experience without removing the player's sense of agency. The central insight: **the designer cannot control what a player does; they can only control the conditions under which the player makes choices.** If those conditions are designed well, the player will freely choose to do what the designer intended — and feel like they chose it themselves.

---

## The core principle (s005, ch.16)

> "We don't always have to give the player true freedom — we only have to give the player the *feeling* of freedom. If a clever designer can make a player feel free, when really the player has very few choices, or even no choice at all, then suddenly we have the best of both worlds — the player has the wonderful feeling of freedom, and the designer has managed to economically create an experience with an ideal interest curve and an ideal set of events." (s005, ch.16)

This is not deception — it is design. The lusory attitude (Suits) means the player already consents to an artificial, rule-bound experience. Indirect control is the craft of shaping that experience so the player moves through it as if freely exploring, while actually following a designed path.

**The feeling of freedom** is what players want, not freedom itself. Too much freedom (an infinite empty world with no guidance) is disorienting and frustrating. Appropriate indirect control creates a structured experience that feels open.

---

## Six methods of indirect control (s005, ch.16)

### Method 1: Constraints
Limit the player's choices to the ones the designer wants them to consider.

> "Consider the difference between 'Pick a color: ___' and 'Pick a color: red / blue / green.' Both give the answerer freedom of choice. But for the first, the answerer could choose from millions; for the second, only three. They still feel free — they still get to choose — but we have cut the choices from millions to three." (s005, ch.16)

In games: walls, locked doors, inaccessible areas, and limited action sets constrain choice space without feeling oppressive. A room with two doors gives the player freedom; a room with two doors where one is obviously interesting and one is obviously dangerous gives the player a choice with stakes.

Constraints work best when invisible — when the player doesn't notice they could have gone elsewhere. Good spatial design makes constraints feel like natural features of the world, not arbitrary blocks.

### Method 2: Goals
Give the player clear objectives that pull them in the intended direction.

A player will move toward a goal. If the goal is placed at the end of a specific path, the player follows that path — not because they're forced to, but because they want to reach the goal. The placement of objectives is one of the most powerful tools for guiding player movement through a designed space.

Goal clarity is essential: fuzzy goals produce wandering. Crisp goals ("reach the exit," "kill the target," "solve the puzzle") produce directed action. → [[../../theory/meaningful-play]] (clear goals = discernability)

### Method 3: Interface
Design the UI to reveal only what the designer wants revealed.

The interface is an indirect control tool because it determines what information the player has access to. A minimap that shows quest objectives but not all possible locations guides movement. A health bar that changes color at low health triggers cautious behavior. An inventory system that shows item descriptions guides player choices.

Interface design is attention management: what the UI makes salient becomes what the player thinks about. → [[../../interface/ui-design]]

### Method 4: Visual design
Use color, lighting, and composition to guide the eye — and through the eye, guide the body.

This is the spatial designer's primary tool (see [[../../level-design/spatial-design]]). The eye moves toward:
- **Light**: bright areas attract attention and suggest safety, reward, and goals
- **Contrast**: a brightly colored object in a neutral environment demands attention
- **Motion**: anything moving draws the eye
- **Unusual forms**: distinctive shapes in a repetitive environment create focal points

The player goes where their eye goes. If the designer controls what the eye goes to, they control where the player goes — without any explicit instruction.

Examples:
- Red barrel in a grey corridor → the player notices and investigates the barrel
- Lit door at the end of a dark corridor → the player moves toward the light
- NPC looking in a specific direction → the player looks in that direction
- Crumbling wall with a distinctive crack pattern → the player tries to destroy it

### Method 5: Characters
Use NPCs and story characters to direct player attention and movement.

Characters are highly effective guides because players naturally follow human-like agents:
- **Explicit guidance**: an NPC says "The treasure is through the north door" → the player goes through the north door
- **Implicit guidance**: an NPC walks down a corridor → the player follows
- **Environmental characters**: a dead NPC slumped against a door → the player tries the door
- **Character gaze direction**: NPCs looking in a specific direction → the player looks there

Characters also carry narrative intent — a companion character running ahead feels like invitation rather than instruction. The player follows the companion because they want to (narrative + spatial momentum), not because they're told to.

### Method 6: Music
Use audio to set emotional context, signal danger, and guide behavior.

Music is the fastest emotional channel (Hodent, s014): the amygdala responds to music before the cortex processes it consciously. This makes it an extremely powerful — and almost unavoidable — indirect control tool:
- **Threatening music** near an enemy → the player becomes alert and cautious
- **Peaceful ambient sound** in a safe area → the player relaxes
- **Directional audio** (a sound heard from one direction) → the player moves toward or away from the source
- **Musical intensity tracking** → music that grows more intense as the player approaches the correct area guides progression without a minimap

> "Music is possibly the most subtle and powerful of the indirect control methods, because the player is often completely unaware they are being guided by it." (s005, ch.16 paraphrased)

---

## Combining indirect control methods

The most effective indirect control uses multiple methods simultaneously, all pointing in the same direction:

**Example: guiding the player to a hidden area**
- **Constraints**: the other paths lead to visible dead ends or low-reward areas
- **Goals**: the mission objective is in this direction
- **Visual design**: a crack of light visible through a wall; unusual architecture marks the spot
- **Characters**: a sound of movement suggests something is here
- **Music**: a subtle shift in ambient tone signals this is important

When all six methods agree, the player moves to the intended location quickly and willingly, feeling like they discovered it themselves.

---

## Indirect control and ludonarrative coherence (s005, s012)

Indirect control is how designers ensure that narrative and gameplay point in the same direction. If the story says "go north" but the mechanics and level design make north feel unrewarding, the player goes elsewhere. The story and the indirect control system must agree.

Conversely, indirect control can carry narrative weight: moving through a darkening corridor as music becomes ominous tells a narrative story purely through environment and audio, without any explicit text or dialogue. The player feels the story through the designed conditions, not just through cutscenes.

> ⭐ **Connection to level design**: indirect control is the mechanism by which spatial design becomes narrative design. The level designer's primary creative act is selecting which indirect control methods to use, where, and in what combination to guide the player through a designed experience. → [[../../level-design/level-design]], [[../../level-design/spatial-design]]

---

## Key concepts & cross-links

- [[story-and-games]] — the narrative context that indirect control serves
- [[../../level-design/spatial-design]] — visual design and constraints in space
- [[../../level-design/pacing-and-flow]] — interest curves as the macro target indirect control helps maintain
- [[../../interface/ui-design]] — interface as indirect control system
- [[../../player/player-psychology]] — attention, visual perception, emotional response to music
- [[../../feel-and-controls/feedback-systems]] — feedback as a form of indirect control
- [[../../theory/magic-circle]] — indirect control operates within the magic circle's consent framework

## Sources

s005 ch.16 (Schell — "Story and Game Structures can be Artfully Merged with Indirect Control"; 6 methods; feeling of freedom; Lens #71 Freedom) · s012 ch.12 (Kremers — environmental storytelling as indirect control) · s003 (Hourences — composition, lighting, landmarks as guidance) · s014 (Hodent — music as fastest emotional channel) · s013 (Salen & Zimmerman — lusory attitude as the psychological foundation)
