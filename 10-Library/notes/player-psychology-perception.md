---
id: player-psychology-perception
title: Perception, Attention & Memory — The Brain as a Design Constraint
type: atomic
disciplines: [player, interface]
sources: [s014, s015, s005]
hp: false
tags: [concept]
status: evergreen
created: 2026-06-03
updated: 2026-06-03
---

# Perception, Attention & Memory — The Brain as a Design Constraint

Games don't run on a rational cognitive vacuum. The human brain has **fixed constraints** — limits on perception, attention, and memory — and **systematic biases** that shape how players experience a game. Hodent's central argument in *The Gamer's Brain*: effective design works *with* these constraints, aligning the game's communicative intent with the player's mental model rather than fighting human cognition (s014). When intent and mental model diverge, the player is confused or frustrated — not because they're bad, but because the design ignored cognitive reality.

## Detail

- **Perception is active, not passive (s014, ch.4).** The brain constructs a representation of the world, blending **bottom-up** sensory input with **top-down** expectation. Players see what they expect to see — change blindness and inattentional blindness follow directly.
- **Foveal focus.** The eye resolves detail only at the fovea; peripheral vision is blurry and motion-sensitive. Critical information (health, threats) must sit where the gaze is, or use strong peripheral signals (edge glow, vignetting) for off-center alerts (s014, ch.4).
- **Gestalt grouping.** The brain auto-groups by proximity, similarity, and continuity. UI that respects Gestalt is read faster and more accurately than UI that fights it.
- **Affordances & signifiers (Norman, s015).** A design property that communicates its own use; a glowing item *affords* collection, an avatar-height ledge *affords* grabbing. Poor affordances make players guess what the game wants. See [norman-hcd-vocabulary](norman-hcd-vocabulary.md).
- **Memory is layered (s014, ch.5).** Sensory (<1s) → short-term (~7 items, <1min) → working memory (~3–4 active items) → long-term (unlimited). Onboarding that dumps 7+ systems at once overflows working memory. **Procedural memory** (controls becoming automatic) is encoded through *doing*, not reading — teach by play.
- **The forgetting curve.** Mechanics taught once and never revisited are lost. Use spaced repetition; keep critical interface elements permanently visible to cut retrieval demands.
- **Attention is selective amplification (s014, ch.6).** Active/endogenous (goal-directed) vs. passive/exogenous (stimulus-driven). **Inattentional blindness:** a player locked onto combat will miss a tutorial popup elsewhere on screen. Direct attention with **salience** (motion, contrast, sound, size) and use **dual sensory cues** (visual + audio) for critical events.
- **Cognitive load (Sweller).** Every demand consumes attentional resources; overload produces obvious mistakes and unexplained frustration. Make common actions automatic (clear control mapping) so they cost minimal working memory.
- **Biases to design around (s014, ch.3).** Anchoring (first values become reference points), confirmation bias (players cling to a wrong mental model until repetition corrects it), Dunning-Kruger (novices skip tutorials, then feel cheated), and **loss aversion** (losses hurt ~2× equivalent gains — calibrate economies accordingly).

## Connections

- [norman-hcd-vocabulary](norman-hcd-vocabulary.md) — affordances, signifiers, and the gulfs of execution/evaluation
- [ui-design-hud](ui-design-hud.md) — applying perception limits to HUD and interface layout
- [player-motivation-maslow](player-motivation-maslow.md) — the motivational layer that sits atop these cognitive constraints
- [self-determination-theory-games](self-determination-theory-games.md) — competence/autonomy/relatedness as motivation drivers
- [flow-channel-definition](flow-channel-definition.md) — sustained attention (focus) is a precondition of flow
- [feedback-system-design](feedback-system-design.md) — feedback must reach attention through the right sensory channel
- [schell-ch09-player-mind](schell-ch09-player-mind.md) — Schell's four mental abilities (modeling, focus, imagination, empathy)

## Appears in

- [s014-the-gamers-brain](../sources/s014-the-gamers-brain.md) · ch.3–6, ch.8 (summary/notes edition)
- [s015-design-of-everyday-things](../sources/s015-design-of-everyday-things.md) · affordances, mental models
- [s005-art-of-game-design](../sources/s005-art-of-game-design.md) · ch.9
