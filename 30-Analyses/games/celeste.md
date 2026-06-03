# Game Analysis: Celeste (2018, Maddy Thorson & Noel Berry / Extremely OK Games)

**Genre:** Precision platformer · **Platform:** Multi · **Player count:** 1 · **Session length:** Variable (12–40+ hours depending on completion goal)

**Why this game:** Celeste is the gold standard for difficulty and accessibility design done simultaneously — it is ruthlessly hard AND accessible. The Assist Mode and its design philosophy are directly applicable to party brawler accessibility (Hot Potato), and the narrative-mechanics integration is a masterclass.

---

## Quick stats

| Property | Value | Hot Potato relevance |
|----------|-------|---------------------|
| Control complexity | Low (handful of moves) | Comparable target |
| Death frequency | Very high (average player dies 1000+ times) | Hot Potato: explosion as punchline not punishment |
| Accessibility solution | Assist Mode (player-adjustable) | Configurable chaos/skill modes |
| Narrative integration | Anxiety as both subject and mechanic | — |

---

## Formal Elements

| Element | Detail |
|---------|--------|
| **Players** | 1 |
| **Objectives** | Reach the top of Celeste Mountain; collect strawberries (optional); find B-sides (optional) |
| **Procedures** | Move, jump, dash (single use until touching ground/wall), climb (brief stamina) |
| **Rules** | One dash per jump; wall cling depletes quickly; every obstacle kills on contact; checkpoint (room-level) respawn |
| **Resources** | Dash charge (refills on landing/touching crystal); stamina (for climbing); heart gems (chapter collectibles) |
| **Conflict** | Player vs. environment (no enemies — obstacles and your own execution) |
| **Boundaries** | Individual rooms (each is a discrete puzzle-platformer challenge) |
| **Outcome** | Reach the summit; optional completion milestones (all strawberries, B-sides, C-sides) |

---

## MDA Analysis

### Mechanics
- **Dash mechanic**: a single directional burst, recharging on ground contact. Simple, readable, expressive in 8 directions. The entire game's depth comes from this one mechanic combined with the environment.
- **Room-as-level**: each screen is a discrete challenge. Failure restarts the room instantly — no "load screen death," just immediate retry.
- **Assist Mode**: a suite of player-adjustable settings: game speed (50%–100%), invincibility, infinite dash, skip difficult rooms. These are framed as accessibility tools, not "easy mode" shame.
- **Crystal hearts, strawberries**: optional collectibles that don't affect the main path; create different difficulty tiers for different players without gatekeeping.

### Dynamics
- **The death-as-learning loop**: failure is designed to be instructive, not punishing. Instant respawn + fast checkpoint reads + clear death cause = tight learning loop. Players fail hundreds of times and feel like they're improving, not losing.
- **Flow staircase**: Celeste manages a smooth challenge gradient by making early sections easy (one mechanic in isolation), medium sections harder (mechanic + environment interaction), and late sections masterful (multiple mechanics perfectly combined). The gradient is exceptionally well-calibrated.
- **Assist Mode as personalization**: players using Assist Mode still experience the full narrative and much of the challenge — they are choosing their own difficulty dial, not accepting a dumbed-down version. This produces a massive accessibility benefit without affecting the base game.

### Aesthetics
- **Challenge** (primary): mastery; the satisfaction of clearing a room after 40 attempts
- **Narrative** (co-primary): Madeline's anxiety and self-doubt are mechanically expressed — the harder sections of the game literally visualize anxiety
- **Discovery** (secondary): B-sides, C-sides, crystal hearts — the game has layers of content for those who seek it

---

## Core loop diagram

```
Enter room → Observe obstacles and goal
                ↓
          Attempt crossing
                ↓
    Success → Exit room → Next room
    Failure → Instant respawn (same room start)
                ↓
           Attempt again
           (same room, new knowledge)
```

The macro loop: chapter by chapter, the mountain gets harder; narrative beats are interspersed with mechanical escalation.

---

## Design highlights

### 1. Assist Mode as ethical accessibility design

The traditional difficulty spectrum: Easy / Normal / Hard. The problem: "Easy" is often stigmatized; players who "need" it feel they're not playing the real game.

Celeste's solution: **Assist Mode is a suite of surgical tools, not a difficulty level.** Players enable specific helps: slow the game without changing the mechanics, add extra dashes, or just make Madeline invincible. The game's entire content is still present — the story, the levels, the challenge structure — just with adjustable friction.

> "Not everyone who wants to experience a game can play it the same way. Accessibility isn't about making games 'easier' — it's about making them playable for more people." (Maddy Thorson, various interviews)

**Application to Hot Potato:** rather than a single "casual mode," consider tunable parameters — timer length, explosion severity, character speed — that each player can adjust. Skilled players use default settings; novices tune a couple of dials. No one gets a "baby mode" label.

→ [[../../concepts/player/flow-channel]] (accessibility as widening the flow channel)

### 2. Death as punchline, not punishment

Celeste players die hundreds of times in a normal playthrough. This should feel awful; instead it feels like part of the process. Why?

- **Instant respawn**: no load screen; no animation death spiral; just blink and you're back
- **Checkpoint granularity**: each room is a checkpoint. Failure costs you the room attempt, not the whole chapter.
- **Clear death cause**: you always know why you died. The obstacle is visible; your mistake is obvious. The game teaches through failure.
- **Optional death count display**: the game shows your death count but never makes it shameful. It's a badge of effort.

**Application to Hot Potato:** the explosion should be the punchline, not the punishment. Fast respawn, clear visual cause ("you were holding it!"), and a brief invincibility window turn explosion from "I lost" to "oh that was funny." → [[../../concepts/feel-and-controls/feedback-systems]] (tells and clear feedback)

### 3. Narrative-mechanic integration (anxiety as both subject and mechanic)

Celeste's story is about Madeline climbing a mountain while dealing with anxiety and depression; her "Part of Her" enemy is a literal manifestation of her self-doubt. The B-side chapters — which appear after she reconciles with the Part of Her — are mechanically more chaotic and disorienting.

This is narrative-mechanic integration at its finest: the mechanical challenge *is* the thematic content. The anxiety you feel trying to clear the hardest rooms IS the game's subject matter, delivered through play rather than cutscene.

→ [[../../concepts/narrative/story-and-games]] (ludonarrative coherence; narrative delivered through mechanics)

### 4. Strawberries as optional depth without gatekeeping

Strawberries are collectibles scattered across Celeste's rooms — often in visibly harder-to-reach spots. They do not unlock anything; they are a pure optional challenge.

This structure serves multiple player types simultaneously:
- **Story-first players** can ignore strawberries entirely and get the full narrative
- **Challenge-seekers** can pursue 100% completion and find significantly harder challenges hidden in plain sight
- **Perfectionist achievers** have a clearly defined completionist goal

No player type is blocked from the core experience; additional depth is always available but never mandatory.

→ [[../../concepts/player/player-types]] (simultaneous service of multiple motivations)

---

## What Celeste does well (extractable principles)

1. **Fail fast, fail clearly, fail cheaply**: instant respawn + obvious death cause + granular checkpoints
2. **Accessibility without shame**: surgical tunable assists rather than binary difficulty levels
3. **The gradient matters more than the peak**: the difficulty ramp is as important as the maximum difficulty
4. **Narrative and mechanics are the same thing**: the hardest parts of the game express the narrative's themes
5. **Optional depth never gates required content**: strawberries, B-sides, and C-sides serve different audiences without blocking anyone

---

## Relevance to Hot Potato

- **Explosion as punchline**: Celeste's death mechanic shows how frequent failure can feel energizing rather than punishing. Apply to Hot Potato's explosion: fast respawn, clear blame assignment, brief invincibility window.
- **Tunable difficulty**: Assist Mode's philosophy maps to Hot Potato's party accessibility challenge. Consider tunable timer length and explosion severity rather than a single "casual mode."
- **Clear cause for every outcome**: "I died because I missed that platform" is as readable as "I exploded because I was holding it." Both should be immediately clear without UI explanation.

---

## Related analyses

- [smash-bros](smash-bros.md) — party brawler accessibility through character asymmetry
- [portal-2](portal-2.md) — puzzle teaching through level design
- [hades](hades.md) — roguelite difficulty and progression design

## Sources

s005 ch.9 (Schell — flow channel; tense-and-release) · s005 ch.14 (Schell — interest curves) · s014 (Hodent — cognitive load; accessibility) · s011 (MDA — Challenge + Narrative aesthetics) · s007 (Swink — death feel and respawn feedback)
