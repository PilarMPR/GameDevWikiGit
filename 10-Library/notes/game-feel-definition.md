---
id: game-feel-definition
title: Game Feel — Real-Time Control in Simulated Space
type: atomic
disciplines: [feel-and-controls]
sources: [s007, s017]
hp: true
tags: [concept]
status: evergreen
created: 2026-06-02
updated: 2026-06-02
---

# Game Feel — Real-Time Control in Simulated Space

**Game feel = real-time control of virtual objects in a simulated space, with interactions emphasized by polish.** It is the tactile, kinesthetic sensation of control — the invisible craft that players describe as "tight," "floaty," "responsive," or "snappy" without being able to explain why (Swink, s007).

## Detail

- **Three building blocks (s007):**
  1. **Real-time control** — continuous closed loop between input and response; sub-second feedback; like driving a car, not a turn-based conversation.
  2. **Simulated space** — the physical environment the avatar moves through; collision, level density, obstacle spacing.
  3. **Polish** — audio/visual effects that sell and emphasize interactions: screen shake, particles, hit-stop, sound sync.
- **Six measurable components (s007):** Input (polling rate, dead zones), Response (acceleration/deceleration curves), Context (collision geometry), Polish (sound sync, shake magnitude), Metaphor (the player's conceptual model), Rules (gravity, friction, coyote time).
- **The 3Cs (s017):** At the product level, feel = Character (avatar personality through movement) + Camera (world framing) + Control (input responsiveness). Must be nailed before any system is built on top.
- **Proprioception:** game feel extends the player's kinesthetic self-model into the avatar. Input latency breaks this extension. Target: <100ms end-to-end.
- **Calibration principle:** tuning a 2ms sound sync offset or a 3-frame animation can be the difference between "floaty" and "satisfying." These are measurable and improvable.

## Connections

- [[feedback-systems]] — polish layer and feedback are the third building block
- [[game-feel-3cs]] — the product-level 3Cs model
- [[player-psychology-perception]] — proprioception and kinesthetic self-extension
- [norman-hcd-vocabulary](norman-hcd-vocabulary.md) — affordances and feedback at the control interface level

## Appears in

- [s007-game-feel](../sources/s007-game-feel.md) · throughout
- [s017-f2p-design-handbook](../sources/s017-f2p-design-handbook.md) · Part 1 (3Cs)
