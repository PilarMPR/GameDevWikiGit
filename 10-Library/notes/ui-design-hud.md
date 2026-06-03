---
id: ui-design-hud
title: Game UI Design — HUD and Information Hierarchy
type: atomic
disciplines: [interface]
sources: [s014, s015, s006, s012]
hp: true
tags: [concept]
status: grown
created: 2026-06-02
updated: 2026-06-02
---

# Game UI Design — HUD and Information Hierarchy

Game UI closes Norman's gulfs: execution ("what can I do?") and evaluation ("what happened?"). Every UI element should answer one of these questions or it's clutter. The golden standard: the player always knows what is happening, what to do next, and how well they are doing — without being distracted from the game (s015, s014).

## Detail

- **Diegetic vs. non-diegetic UI:** Diegetic = exists within the game world (character sees it; maintains immersion). Non-diegetic = overlaid on screen outside the world (clearest communication, breaks immersion). Most games use non-diegetic for critical info, diegetic for atmosphere.
- **HUD information hierarchy (s014):**
  1. Constant critical info: always readable at a glance (health, ammo, active objective).
  2. Situational critical info: unmissable when appearing (alerts, warnings).
  3. Strategic reference info: consulted deliberately (minimap, cooldowns).
  4. Optional info: accessed when the player chooses (detailed stats, menus).
- **Gestalt principles:** group related info together; use consistent color coding; high-contrast text against variable backgrounds.
- **Cognitive load:** every HUD element competes for working memory. Fewer elements, clearer hierarchy = better play. Rule: if removing it wouldn't cause problems, remove it.
- **Attention placement:** put critical info where the player's gaze already goes (near center, or at screen edges for peripheral attention).

## Connections

- [norman-hcd-vocabulary](norman-hcd-vocabulary.md) — gulfs of execution and evaluation
- [feedback-system-design](feedback-system-design.md) — UI elements are feedback delivery mechanisms
- [[player-psychology-perception]] — perception and attention constraints on UI design

## Appears in

- [s014-the-gamers-brain](../sources/s014-the-gamers-brain.md) · ch.3–6
- [s015-design-of-everyday-things](../sources/s015-design-of-everyday-things.md) · ch.2
- [s006-fundamentals-of-game-design](../sources/s006-fundamentals-of-game-design.md) · ch.12
