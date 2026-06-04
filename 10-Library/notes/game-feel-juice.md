---
id: game-feel-juice
title: Juice — Maximum Output for Minimum Input
type: atomic
disciplines: [feel-and-controls, feedback-systems]
sources: [s018, s007]
hp: true
tags: [concept, polish, feedback, game-feel]
status: evergreen
created: 2026-06-04
updated: 2026-06-04
---

# Juice — Maximum Output for Minimum Input

**Juice** is the density of sensory feedback a game generates in response to player actions. A juicy game produces a maximum of output (visual, audio, tactile feedback) for each minimum of input — a single button press triggers particles, screen shake, sound, animation, and systemic reactions simultaneously. Juiciness is the difference between a game that feels flat and dead and one that feels alive and pleasurable (Jonasson & Purho, s018).

## Detail

- **Core definition (s018):** "Showing a maximum output for each minimal input." The rules don't change; the feedback density transforms the experience.
- **The Breakout demonstration (s018):** Jonasson & Purho proved the concept by adding juice layers to an unchanged Breakout clone. Same rules, same challenge, dramatically different feel — each layer compounds with the others.
- **Juice taxonomy (s018):**
  1. Motion feedback (squash/stretch, rotation, velocity stretch)
  2. Impact confirmation (flash, screen shake, hit sound)
  3. Destruction feedback (animated death, particle burst)
  4. Systemic reaction (board-wide ripple when any element is hit)
  5. Personality (eyes, expressions on game objects — invokes Heider-Simmel effect)
  6. Audio-visual coupling (pitch harmonics on combos, music reactivity to state)
- **Screen shake quality (s018):** Perlin noise-based shake feels directional and weighted; random jitter feels cheap. The implementation matters.
- **Pitch harmonics (s018):** Shifting pitch up on successive hits creates a musical reward loop — players begin to hear the rhythm of good play.
- **Timing constraint (s018):** "Don't start polishing until it's final." Juice applied to an incomplete core loop is wasted effort.
- **The counter-argument:** Folmer Kelly argues over-juicing breaks immersion when visual language contradicts tone. A horror game with rainbow particles loses its identity. Juice must serve the game's aesthetic register.

## Relationship to game feel (s007)

Swink's "polish" (the third building block of game feel in s007) is the theoretical parent of juice: audio/visual effects that "sell and emphasize" interactions. Juice is the practical, maximalist operationalization of polish — not just adding effects but layering them until the feedback density is high enough to make the game feel alive.

The distinction: polish (s007) is any effect added to emphasize interaction; juice (s018) is the *density* principle — more is better, up to the point of tonal contradiction.

## Connections

- [game-feel-definition](game-feel-definition.md) — Swink's polish layer; juice operationalizes it
- [[feedback-systems]] — juice is multi-channel feedback at high density
- [[player-psychology]] — feedback density as a flow-maintenance mechanism; legible feedback keeps players in the channel
- [s018-juice-it-or-lose-it](../sources/s018-juice-it-or-lose-it.md) — source

## Appears in

- [s018-juice-it-or-lose-it](../sources/s018-juice-it-or-lose-it.md)
- [s007-game-feel](../sources/s007-game-feel.md) — polish building block
