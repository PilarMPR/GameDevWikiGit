---
id: s020
title: "Level Design Workshop: Designing Celeste"
author: Maddy Thorson & Noel Berry
year: 2018
type: talk
link: https://www.youtube.com/watch?v=4RlpMhBKNr0
gdcvault: https://www.gdcvault.com/play/1024307/Level-Design-Workshop-Designing-Celeste
venue: GDC 2018, Level Design Workshop
topics: [level-design, difficulty, accessibility, flow, iteration, platformer, emotional-design]
---

## Summary

Good level design serves the game's emotional and narrative thesis, not just its mechanics. In Celeste, every room is a self-contained micro-story, each chapter introduces one idea and escalates it, and accessibility is not opposed to difficulty — the two are designed in deliberate counterbalance. The talk demonstrates how a mechanically demanding game can serve the widest possible player range through structural design rather than difficulty sliders.

## Key claims

- Every screen in Celeste is designed around a single mechanic or concept: introduce, challenge, escalate, test mastery. (s020)
- Instant respawn with near-zero death friction is the foundational flow-maintenance mechanism — death is a teaching event, not a punishment. (s020)
- Assist Mode "breaks the game" deliberately — framed as player empowerment, not design compromise. (s020)
- Tiered difficulty (main path / strawberries / B-sides / C-sides) allows a single challenge level to be tuned precisely without excluding players who want more or less. (s020)
- The core prototype (made in 4 days in PICO-8) served as the design document for the full game — feel-first development. (s020)
- Rooms were intentionally designed with movement shortcuts for emergent expert play by speedrunners. (s020)

## Detailed notes

### Emotional thesis as design filter

Thorson's central frame: "Madeline is trying to climb a mountain." Every design decision was evaluated against this emotional narrative. Level design in Celeste is not primarily about teaching moves — it's about creating the *feeling* of a hard climb that you can succeed at.

This is level design in the tradition of Schell's experience-first design (s005, ch.4): start with the emotion, work backward to the mechanics that produce it.

### Rooms as ideas (the Nintendo school)

Each room in Celeste:
1. Introduces one concept (never two simultaneously during introduction)
2. Gives the player a safe practice context
3. Escalates into challenge
4. In B/C-sides: tests mastery under pressure

Each chapter introduces one new mechanic, integrates it through escalation, and combines it with prior mechanics at the chapter's end. This mirrors the Level Design principle of "teach then test" common to Nintendo platformers.

### Prototype as design document

The original Celeste jam game was made in 4 days in PICO-8. It established the core movement feel: dash, climb, precise momentum. The full game was built outward from that feeling. Thorson and Berry never deviated from the feel of the prototype — the prototype was the spec.

This is the same workflow Derek Yu used for Spelunky (s023): freeware version → design document. The implication: get the core feel right first, then build systems around it.

### Difficulty without cruelty

Structural decisions that make a difficult game accessible:
- **Instant respawn:** death returns to start of room within <1 second. The cost of death is measured in seconds, not minutes.
- **Checkpoints inside long rooms:** never lose more than one room's worth of progress
- **Camera design:** the camera always shows what the player needs to see next — no death-by-obscured-information
- **No lives, no score, no external penalty:** the only consequence of death is trying the room again
- **Room as unit:** failure is bounded to the room. Players learn iteratively without losing global progress.

Crucially, these decisions did not reduce the game's challenge ceiling. They reduced the *cost* of failure, which allowed the game to make more demanding design choices without frustrating players into quitting.

### The tiered difficulty structure

Four tiers of difficulty from the same game:
1. **Main path:** one-new-mechanic-per-chapter, designed for a specific challenge level
2. **Strawberries:** optional collectibles requiring perfect execution or unusual routes — not required, but visible as a stretch goal
3. **B-sides:** alternate, radically harder versions of each chapter; require cassette collection to unlock
4. **C-sides:** further radically harder

This structure means:
- The main path is tuned without compromise
- Players who want more have two additional tiers waiting
- No player is blocked from the full narrative experience

### Assist Mode

Assist Mode allows: invincibility, slowing game speed to 70%/60%/50%, infinite stamina, skip individual rooms.

Thorson: *"Assist Mode breaks the game. I spent many hours fine-tuning the difficulty of Celeste, so it's easy for me to feel precious about my designs. But ultimately, we want to empower the player and give them a good experience, and sometimes that means letting go."*

The framing is critical: Assist Mode is presented without judgment, as tools for everyone to experience the complete game. Not hidden, not labeled as "easy mode," not penalized with a separate achievement track.

This is the Celeste model for accessibility that has influenced the industry — see `05-Syntheses/Accessibility & Inclusive Design.md`.

### Speedrunner design

Thorson and Berry designed knowing they were making surfaces for emergent expert play. Rooms contain movement shortcuts — routes that reward deep mastery of the dash/climb/momentum system. These were not afterthoughts; they were designed in. The game has two layers of intended play: casual progression through rooms, and aggressive optimization of those same rooms.

This is Salen & Zimmerman's emergent gameplay from tight formal systems (s013): the same rules that make the game playable for beginners contain a second, deeper game for experts.

## Notable quotes

- "Assist Mode breaks the game. I spent many hours fine-tuning the difficulty of Celeste, so it's easy for me to feel precious about my designs. But ultimately, we want to empower the player and give them a good experience, and sometimes that means letting go." — Maddy Thorson
- (Implicit thesis): "Madeline is trying to climb a mountain." — the design filter applied to every room decision

## Related wiki pages

- [[../../05-Syntheses/Accessibility & Inclusive Design]] — Assist Mode as the canonical model; difficulty tiers (s020 added)
- [[../../05-Syntheses/Game Balance]] — tiered difficulty / flow maintenance through instant respawn (s020 added)
- [[../../10-Library/notes/game-balance-overview]] — instant respawn as flow-maintenance mechanism (s020 added)
- [[../../10-Library/notes/flow-channel-definition]] — instant respawn + escalating difficulty as textbook flow maintenance
- [[../../10-Library/sources/s023-spelunky-dna-roguelike]] — prototype-as-design-document parallel
- [[../../30-Analyses/games/celeste]] — full game analysis using this and other sources
