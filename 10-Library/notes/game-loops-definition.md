---
id: game-loops-definition
title: Game Loops — Definition and Structure
type: atomic
disciplines: [mechanics, theory]
sources: [s001, s011, s017, s026]
hp: true
tags: [concept]
status: evergreen
created: 2026-06-02
updated: 2026-06-02
---

# Game Loops — Definition and Structure

A game loop is a **causal chain that cycles back to its own starting point**, creating self-reinforcing or self-regulating behavior over time. In games, loops exist at every scale: from the sub-second action/feedback tick to the month-long progression arc. The loops are the beating heart of engagement (s001, ch.4; s011; s017).

## Detail

- **Sellers' definition (s001, ch.4):** "The give-and-take between the player and the game — a reciprocating loop where the player provides input, the game changes state and provides feedback, which triggers a new player intent." This is the essence of interactivity.
- **MDA framing (s011):** Loops manifest in the **Dynamics** layer — the run-time behavior of mechanics responding to player input over time.
- **F2P framing (s017):** the core loop is "the repeating cycle of player actions that sustain engagement — the shortest repeating arc the player inhabits."
- **Core loop anatomy:** Player intent → Player action → Game state change → Game feedback → new Player intent.
- **Three kinds of loops** (s001, ch.7): **Core loops** (what the player does most of the time), **Outer loops** (longer-period loops providing large-scale structure and retention), and nested loops of different timescales.
- Every loop is either **reinforcing** (positive feedback — output amplifies condition) or **balancing** (negative feedback — output reduces gap). Sustaining engagement requires balancing reinforcing against balancing loops.
- **Implementation layer (s026, ch.1):** the game loop is a literal software loop — `while(running) { processInput(); update(dt); render(); }`. **Delta time (dt)** is elapsed seconds since the last frame; all movement and physics must be scaled by dt or the game runs at different speeds on different hardware. Real-time vs. game-time scaling (dt × scalar) is the technical basis for slow motion, bullet time, and replay systems. Multithreaded loops overlap the render thread and the update thread for throughput; the render thread runs one frame behind. **Game object model** patterns: update-only (logic), draw-only (static geometry), update+draw (typical entity) — a precursor to ECS architecture.

## Connections

- [sellers-four-principal-loops](sellers-four-principal-loops.md) — the full nested model with the designer's loop
- [reinforcing-vs-balancing-loops](reinforcing-vs-balancing-loops.md) — the fundamental loop polarity
- [[game-loop-timescales]] — how loops operate at different cognitive registers
- [mda-feedback-dynamics](mda-feedback-dynamics.md) — the MDA treatment of feedback loop dynamics
- [progression-systems-definition](progression-systems-definition.md) — outer loops as the progression frame

## Appears in

- [s001-advanced-game-design](../sources/s001-advanced-game-design.md) · ch.4, ch.7
- [s011-mda-framework](../sources/s011-mda-framework.md) · full paper (Dynamics layer)
- [s017-f2p-design-handbook](../sources/s017-f2p-design-handbook.md) · Part 1
- [s026-game-programming-algorithms-and-techniques](../sources/s026-game-programming-algorithms-and-techniques.md) · ch.1 (game loop implementation, delta time, real time vs. game time, frame limiting, multithreaded loop architecture, game object model)
