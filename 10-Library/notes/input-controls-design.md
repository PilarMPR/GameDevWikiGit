---
id: input-controls-design
title: Input and Controls — Mapping and Responsiveness
type: atomic
disciplines: [feel-and-controls]
sources: [s007]
hp: true
tags: [concept]
status: grown
created: 2026-06-02
updated: 2026-06-02
---

# Input and Controls — Mapping and Responsiveness

Input design is the player's tactile contact with the game. Before simulated space or polish, the player must be able to act in the world in a way that feels responsive, precise, and natural. The quality of input mapping determines whether a game feels "tight" or "floaty" (Swink, s007).

## Detail

- **The 240ms boundary (s007):** input must produce a response within 240ms for the player to perceive real-time causality. Beyond 240ms, the feel breaks. Ideal: <100ms end-to-end latency. 60fps (16ms frame time) substantially better than 30fps (33ms) for input feel.
- **Input mapping choices:**
  - **Direct vs. physics-based:** direct = input position drives output position (precision); physics-based = input applies force with momentum (organic but unpredictable).
  - **Linear vs. exponential curves:** linear gives equal response across range; exponential/accelerating gives fine control at low positions, fast response at extremes.
  - **Deadzones:** zone around neutral producing no input; prevents stick drift and allows precise neutral holding.
- **Button semantics:** instantaneous (tap = effect), hold/charge (hold = different effect), toggle (state flip), contextual (same button, different contextual response).
- **"Tight" vs. "floaty":** tight = fast acceleration, fast deceleration, low latency. Floaty = slow acceleration, high momentum, longer deceleration curves. Both are valid design choices for different game types.

## Connections

- [game-feel-definition](game-feel-definition.md) — input/response is the real-time control building block
- [feedback-system-design](feedback-system-design.md) — feedback is the response the player perceives after input
- [camera-design-models](camera-design-models.md) — camera + controls = the 2nd and 3rd C of the 3Cs

## Appears in

- [s007-game-feel](../sources/s007-game-feel.md) · throughout (input as first building block)
