---
id: s047
title: "Bone Placement Tips for Action (Guilty Gear Xrd — ArcSys Dev Document)"
author: Junya Christopher Motomura (Arc System Works)
year: 2018
type: dev-document
tags: [game-art, rigging, character-animation, 3d, fighting-games, technical-art, character-modeling]
---
# s047 · Bone Placement Tips for Action (Guilty Gear Xrd)

**Full title:** *Bone Placement Tips for Action* (translated title) · **Author:** Junya Christopher Motomura, Lead Modeler / Technical Artist, Arc System Works Co. · **Year:** ~2018 (PPTX-converted-to-PDF developer presentation, translated by @LeoBGKK via DeepL/Yandex) · **Source:** ArcSys developer document / GDC/industry presentation

> **Provenance note:** This is a developer slide deck (pptx→pdf), not a published book. Content is faithful but translated from Japanese. The companion document is [[s048-guiltygear-modeling-for-skinning|s048 Modeling for Skinning]], by the same author.

## Summary

An ArcSys technical art presentation on bone placement strategy for character rigs in action/fighting games. The central argument: poor bone placement is the **root cause** of poor animation quality — it can't be compensated for with better skinning, and is extremely costly to fix once animation work has begun. The presentation documents guidelines for placing hip, knee, ankle, toe, torso, clavicle, arm, and other joints to handle the extreme, exaggerated poses that fighting games require. Junya Motomura's credit: Lead Modeler/TA on *Guilty Gear Xrd Series*; Director/Modeling Supervisor/TA on *Dragon Ball FighterZ* (Bandai Namco). (s047)

## Key claims & concepts

### Why bone placement is the root of everything
- **Bone placement is directly related to final quality** but inconspicuous — unlike mesh shape or skinning, bad bone placement is hard to judge at a glance.
- **Cannot be corrected by adjusting skinning.** A bad bone position is a fundamental constraint that no amount of weight painting can fix.
- **Extremely difficult to modify post-animation.** If a rig has 100 animations and a bone position error is found, all 100 must be modified, checked, and re-exported. On large projects, this becomes practically impossible.
- **Errors are invisible in normal poses; only revealed by extreme poses.** Without checking in extreme poses before animation begins, problems will be missed. (s047)

### Core principle
- **"As long as what you see on the screen is cool, it's OK."** The layout presented is not anatomically exact — it uses exaggerations and omissions suited to real-time animation convenience, designed to handle fighting game extremes. (s047)
- **Fighting games require more than realism.** If a rig can handle fighting game extremes (flashy attacks, impossible splits, exaggerated poses), it can handle any everyday animation. (s047)

### Lower body bone placement guidelines
- **Hip joint (front view):** Work backwards from range of motion. Human hip can rotate ~90° from bottom to side (splits). Draw a 45° diagonal from the base of the groin; place the hip joint where it intersects the center of the foot axis. This is much less likely to fail and approximately matches anatomy. (s047)
- **Hip joint (side view):** Legs bend forward more than 90°. Place slightly forward of center, based on overall hip width excluding buttock overhang. "Humans were once quadrupeds — the legs are conveniently designed to bend forward." (s047)
- **Common mistake: hip too low.** Placing the rotation axis too low creates distorted leg silhouette, short-leg appearance, and bad wide-stance/kick deformations. (s047)
- **Knee joint:** Approximately center of front-to-back knee width. Too far forward → kneecap becomes pivot, calf clips. Too far back → knee looks stretched and thin. Auxiliary bones (half-rotation / kneecap) recommended for deep-bend expression. (s047)
- **Shin-thigh ratio:** Thigh (femur) is longer than shin in the human body — the femur is the longest bone. Shins longer than thighs make kneeling/wide-stride poses difficult. If a stylized character requires long shins, use a per-pose rig that can freely adjust length. (s047)
- **Ankle:** Place the axis at the bottom of the ankles. Too high → force direction exits outside the base of the foot during stomping ("about to sprain"). Especially critical for characters with heeled shoes. (s047)
- **Toe bone:** ~1/3 of total foot length for the toe pivot (slightly shorter if barefoot). Height at middle of base of toes. (s047)

### Torso (partial, pages 29–30 in extract)
- The torso is the "core" / "trunk" — enables bending, twisting, tilting, and supports all actions. (s047)

### Auxiliary bones
- **Half-turn auxiliary bones:** follow each joint at 50% rotation (e.g., knee bends 90°, aux bone points 45°). Help represent kneecap, define joint edge, create crisper and more expressive bends. (s047)

## Connections to wiki

- **Companion document:** [[s048-guiltygear-modeling-for-skinning|s048 Modeling for Skinning]] (same author, same series) — covers mesh topology and the "50% trap" in skinning. s047 and s048 form a two-part technical art system.
- **Toon shading / hand-drawn 3D pipeline:** Both s047 and s048 come from the *Guilty Gear Xrd* development context — the ArcSys approach of using 3D meshes rendered with toon shaders to achieve hand-drawn anime aesthetics in real-time is a landmark technique in game art. The underlying rigging requirements (extreme poses, silhouette-first thinking) are a direct consequence of the visual approach.
- **Character art pipeline:** Connects to the animation pipeline in [[s045-game-development-and-production-bethke|s045 Bethke (2003)]] (motion capture, animation systems, outsourcing animation) and the asset pipeline in [[s030-game-programming-in-cpp-madhav|s030 Madhav (2018)]] (skeletal animation system architecture).
- **Silhouette thinking:** The emphasis on "what you see on the screen is cool" and silhouette-driven decisions aligns with the visual communication principles in game art — readable characters require good silhouettes in any pose, especially in action games.
- See also: [[../../wiki/concepts/feel-and-controls/game-feel|game-feel]] — the quality of extreme poses directly feeds into the game feel/impact of attacks in fighting/action games.

## Notable quotes

- "Proposition: If you're having trouble striking a cool pose, it's probably because you're not placing the bones properly!" (Outline)
- "In the end, my stance is, 'As long as what you see on the screen is cool, it's OK'." (Part 1)
- "A lacking bone position cannot be corrected by adjusting the skinning." (Part 1)
- "It is only when you actually strike an extreme pose that the problems are shown. And in many cases, by the time you realize it, it's already too late." (Part 1 Summary)
