---
id: camera-design-models
title: Camera Design — Models and Tradeoffs
type: atomic
disciplines: [feel-and-controls]
sources: [s006, s007]
hp: true
tags: [concept, framework]
status: grown
created: 2026-06-02
updated: 2026-06-02
---

# Camera Design — Models and Tradeoffs

The camera is the player's window into the game world. Camera choice shapes spatial literacy, information availability, game feel, and the emotional character of the entire game. It is the "second C" in the 3Cs (Character, Camera, Controls) (Adams, s006, ch.12).

## Detail

**Five major camera models (s006, ch.12):**
1. **First-person (FPS):** camera at avatar's eye. Strongest immersion and aiming precision; spatial disorientation risk; avatar personality through voice/hands.
2. **Third-person:** camera behind/above avatar. Player sees their character (personality/animation matter). Camera collision is a major design problem. Over-the-shoulder variant balances immersion with aiming.
3. **Top-down/overhead:** spatial overview; minimal kinesthetic feel; ideal for strategy and tactical games. Isometric gives pseudo-3D depth.
4. **Side-scrolling:** horizontal momentum is the primary spatial dimension; ideal for platformers. Screen space management: show more ahead than behind.
5. **Fixed/static:** no camera movement; simplicity; clarity; favored in horror (removes spatial safety) and puzzle games.

**Key design tensions:**
- Immersion vs. information: first-person maximizes presence; top-down maximizes state readability.
- Camera control vs. automation: player-controlled camera gives power; automated camera gives cinematic quality but can disorient.
- Camera distance: closer = intimacy + feel; farther = overview + strategy.

**Camera contributes to game feel (s007):** headbob, weapon sway, camera shake on impact all contribute to kinesthetic sensation beyond the avatar's movement alone.

## Connections

- [[game-feel-definition]] — camera is the second C in the 3Cs
- [[spatial-design-principles]] — what the camera reveals shapes spatial navigation
- [[game-feel-3cs]] — Character + Camera + Controls as the feel system

## Appears in

- [[../sources/s006-fundamentals-of-game-design]] · ch.12
- [[../sources/s007-game-feel]] · simulated space component
