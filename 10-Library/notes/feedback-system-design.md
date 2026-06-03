---
id: feedback-system-design
title: Feedback Systems — Five Channels of Game Communication
type: atomic
disciplines: [feel-and-controls, mechanics]
sources: [s007, s015, s014, s011]
hp: true
tags: [concept]
status: evergreen
created: 2026-06-02
updated: 2026-06-02
---

# Feedback Systems — Five Channels of Game Communication

Feedback is how a game communicates to the player what their actions caused, what the current state is, and what is about to happen. Without feedback, meaningful play is impossible: outcomes are not discernible, the player cannot form a mental model, and the dynamic loop breaks (Norman, s015; MDA, s011).

## Detail

**Five channels (s007, s014, s015):**
1. **Visual** — damage numbers, hit effects, screen shake, status icons, health bars, tells (anticipatory flashes before enemy attacks).
2. **Audio** — confirmation feedback (critical hit sound), warning feedback (footsteps), ambient state feedback (heartbeat at low health). Fastest emotional channel; works when the player isn't looking.
3. **Haptic** — controller rumble, DualSense trigger resistance, directional haptics. Activates proprioceptive system; avatar's physicality extends into the player's hands.
4. **Diegetic (in-world)** — character vocalizations, world reactions, environmental responses. Maintains immersion by keeping information inside the magic circle.
5. **Narrative/social** — character arc responses, world state changes, leaderboard context.

**Design principles:** Immediacy (within ~500ms causal window), informativeness (what happened, not just that something happened), proportionality (feedback intensity ∝ event significance), consistency (same event → same feedback), multi-channel redundancy (visual + audio for critical events = accessibility).

**Tells** — predictive feedback signaling upcoming events before they occur. The bridge between challenge and fairness: if the player had the information and could have responded, the mechanic is fair.

## Connections

- [game-feel-definition](game-feel-definition.md) — feedback/polish is the third building block of game feel
- [meaningful-play-definition](meaningful-play-definition.md) — discernability requires feedback
- [norman-hcd-vocabulary](norman-hcd-vocabulary.md) — Norman's feedback principle
- [mda-feedback-dynamics](mda-feedback-dynamics.md) — feedback loops at the Dynamics level

## Appears in

- [s007-game-feel](../sources/s007-game-feel.md) · throughout
- [s015-design-of-everyday-things](../sources/s015-design-of-everyday-things.md) · feedback principle
- [s014-the-gamers-brain](../sources/s014-the-gamers-brain.md) · ch.4–6
