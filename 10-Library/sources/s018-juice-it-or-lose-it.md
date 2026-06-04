---
id: s018
title: "Juice It or Lose It"
author: Martin "Grapefrukt" Jonasson & Petri Purho
year: 2012
type: talk
link: https://www.youtube.com/watch?v=Fy0aCDmgnxg
gdcvault: https://www.gdcvault.com/play/1016487/Juice-It-or-Lose
demo: http://grapefrukt.com/f/games/juicy-breakout/
topics: [game-feel, feedback-systems, polish, visual-design, audio-design, player-psychology]
---

## Summary

A "juicy" game generates a maximum of output (feedback) for every minimum of input (player action). Jonasson and Purho demonstrate this live by starting with a bare-bones Breakout clone and layering juice — visual, audio, and personality feedback — onto it one element at a time, never changing the rules. The talk is a practical proof that game feel is separable from and addable to core mechanics without altering their logic.

## Key claims

- Juiciness is "showing a maximum output for each minimal input" — generating abundant sensory feedback from the player's smallest actions. (s018)
- A game can feel flat and dead or alive and pleasurable with identical rules — the difference is feedback density. (s018)
- Every sensory feedback layer compounds: the whole is greater than the sum of parts. (s018)
- "Don't start polishing until it's final" — juice applied to an unfinished core loop is waste. (s018)
- Over-juicing is a real risk: Folmer Kelly's counter-talk argues excessive juice breaks immersion when visual language contradicts game tone. (s018)

## Detailed notes

### The demonstration structure

The talk proceeds as a live coded demo using a Breakout clone hosted at grapefrukt.com/f/games/juicy-breakout. Starting state: a white rectangle paddle, a white circle ball, white block grid. Playable but inert. Each layer is added while the gameplay rules remain unchanged.

### Juice taxonomy (effects added in demo order)

**1. Motion feedback**
- Ball rotates as it moves (encodes direction of travel)
- Ball stretches in the direction of travel (squash/stretch — classic Disney principle applied to game objects)
- Ball flashes white on impact (hit confirmation frame)
- Ball size oscillates rhythmically (gives personality, life)
- Paddle stretches/squashes based on mouse speed
- Paddle wobbles on ball contact

**2. Impact confirmation**
- Blocks flash/darken when hit before destruction (staged feedback — communicates the block registered the hit)
- Screen shake on hard impacts (Perlin noise-based, not random jitter — gives directional feel rather than visual noise)

**3. Destruction feedback**
- Blocks shrink and spin as they die rather than popping instantly (animation communicates causality)
- Particle burst on block destruction (unique particle types per surface: wall, block, paddle look different)
- Trailing particles following the ball

**4. Systemic reaction**
- All other blocks on screen react (ripple/shudder) when any block is hit — the entire board becomes alive, communicating systemic connectivity

**5. Audio-visual coupling**
- Distinct sounds for wall, block, and paddle hits
- Pitch shifts harmonically on successive hits (creates a musical reward loop — players begin to hear the rhythm of good play)
- Background music reacts to board state (fewer blocks = different musical texture)

**6. Personality**
- Eyes added to the ball — they look in the direction of travel, blink
- Mouth added, reacts to events
- Eyes added to blocks — they watch the ball approaching
- Background pulses/reacts to music beat

The personality layer invokes the Heider-Simmel effect: humans reflexively read faces and intent onto objects with eyes, generating empathy and emotional investment in a bouncing circle.

### The core lesson

None of the juice changes the rules, the challenge, the win condition, or the skill ceiling. The same game, measured by formal elements, became dramatically more engaging through feedback alone. This is the mechanism behind "game feel" at the sensory layer: the systems are the skeleton; feedback is the skin that makes players want to touch it.

### The counter-argument

Folmer Kelly's response talk ("Indies, Resist the Urge to Juice It or Lose It") argues that juice applied without regard to tone breaks immersion. A dark horror game with screen shake and rainbow particles generates tonal dissonance that undermines the aesthetic. Juice is not unconditionally good — it must serve the game's intended emotional register.

## Notable quotes

- "Showing a maximum output for each minimal input." — Jonasson & Purho (core definition of juiciness)
- Rob Miller's gloss: "little details, little moments of surprise and delight; it's the difference between an experience that feels flat and dull and one that feels exciting and engaging."
- "Don't start polishing until it's final." — Jonasson & Purho

## Related wiki pages

- [[../../10-Library/notes/game-feel-definition]] — Swink's three building blocks; polish is the third building block this talk operationalizes
- [[../../05-Syntheses/Player Psychology, Motivation & Flow]] — feedback density as a flow-maintenance mechanism
- [[../../10-Library/notes/game-feel-juice]] — atomic note on juice as a design concept (created from this source)
- [[../../05-Syntheses/Aesthetics & Game Feel]] — situates juice within the broader aesthetics canon
