---
id: s048
title: "Modeling for Skinning (Guilty Gear Xrd — ArcSys Dev Document)"
author: Junya Christopher Motomura (Arc System Works)
year: 2018
type: dev-document
tags: [game-art, character-modeling, skinning, rigging, topology, 3d, fighting-games, technical-art]
---
# s048 · Modeling for Skinning (Guilty Gear Xrd)

**Full title:** *Modeling for Skinning* (translated title) · **Author:** Junya Christopher Motomura, Lead Modeler / Technical Artist, Arc System Works Co. · **Year:** ~2018 (developer slide deck, translated by @LeoBGKK via DeepL/Yandex) · **Source:** ArcSys developer document / GDC/industry presentation

> **Provenance note:** Developer slide deck, not a published book. Translated from Japanese. Companion to [[s047-guiltygear-bone-placement-tips|s047 Bone Placement Tips for Action]] by the same author.

## Summary

The second in a two-part technical art series from ArcSys's *Guilty Gear Xrd* production. Where s047 addresses bone placement, s048 addresses how **mesh modeling decisions affect skinning quality** — with special focus on the "50% Trap," the fundamental mathematical reason why joint deformations become thin, and the topology strategies that avoid this without adding unnecessary polygons. Written for artists who can model but struggle with skinning, and who want to understand the *theory* behind skinning to predict and control deformation results. (s048)

## Key claims & concepts

### The core argument
- **"Are you trying to solve all your skinning problems… with skinning?"** Skinning problems often originate in the modeling or rigging stage. Fixing them with skinning adjustments is treating symptoms, not causes. (s048)
- **Skinning = specifying which vertices are affected by each bone's movement.** For low-poly real-time models, manual vertex-by-vertex specification is required. (s048)

### Modeling for easy skinning
- **Model in a pose that is easy to work with.** T-pose is the standard for a reason: easy vertex selection. Any pose that makes vertex selection difficult is harder to work with. (s048, Part 1)
- **Split the mesh by logical divisions.** At ArcSys: hair, clothes, and accessories are separate objects (merged into one material for UE4 later). Fewer combined pieces = easier selection and weight painting. Processing load favors merged meshes in the final game, but working files benefit from separation. (s048, Part 1)
- **Arrange vertices in loops.** When setting weights in gradients (10% increments per row), clean vertex loops allow setting the same weight value for an entire loop in one step. Disorderly vertex placement multiplies manual effort. (s048, Part 1)

### The 50% Trap (the key insight of the document)
- **Setup:** Standard skinning around a knee — 100% weight to thigh above, 100% to shin below, ~50/50 at the joint boundary.
- **Expected result:** a smooth bend like a real knee.
- **Actual result:** the knee becomes *thinner* when bent — the back of the knee is tucked inward. "The human body is full of stuff inside it. The joints don't become thin even if bent. Only if you bend an empty thing, such as a rubber hose, will it behave like this." (s048, Part 2)
- **Mathematical cause:** Weighted bone blending is linear interpolation between two positions in world space. The 50%-weighted vertex moves to the midpoint of the straight line connecting its 100%-thigh position and its 100%-shin position. When the joint bends, this midpoint traces inward — producing the "thin" artifact.
- **This is not fixable by adjusting skinning values.** Changing 50/50 to 25/75 or any other ratio just moves the pinch point — it cannot eliminate thinning. Increasing polygon count does not fix the root problem and may make it worse.
- **The calculation method is the same in all 3D software and game engines.** (Double quaternion skinning is an alternative but uncommon.) (s048, Part 2)

### Topology solutions to the 50% Trap
- **"Tuck-in" structure:** Remove vertices from the back of the knee entirely. When the joint bends, the mesh overlaps — but the overlap creates sharp shadows that contribute to the expression. Better to make it thin at the back (where it won't be seen) than to have a bulge where you don't want one. (s048, Part 3)
- **"C" structure:** No vertex at the back of the knee; wide range of motion in a C shape. Doesn't thin, doesn't clip at moderate angles, and produces a softer-looking bend than the tuck-in. (s048, Part 3)
- **Common principle for both:** Add divisions on the *stretching* side (kneecap/front), do not add unnecessary segments on the *shrinking* side (back of knee). Design the vertex arrangement working backwards from the desired deformed shape. (s048, Part 3)

### Model while thinking of joints (Part 4)
- **Identify moving vs. non-moving parts at the start of modeling.** Parts that will be animated must be modeled with the 50% trap in mind. Even at 100% bone weight, a basic silhouette should still look correct. (s048, Part 4)

### Other topics (not fully extracted)
- Part 5: Other skinning tips
- Part 6: Basic introduction to rigging (bonus content)

## Connections to wiki

- **Companion document:** [[s047-guiltygear-bone-placement-tips|s047 Bone Placement Tips for Action]] — covers bone placement strategy. s047 and s048 are a two-part system: get bone placement right first (s047), then design the mesh around the bones (s048).
- **The Guilty Gear Xrd toon-shading pipeline:** Both s047 and s048 are production documents from one of the most technically notable art pipelines in game history — ArcSys's method of rendering 3D meshes with custom toon shaders to achieve hand-drawn anime aesthetics. The extreme poses and silhouette-first approach of fighting games make these problems particularly acute. Understanding this pipeline is highly relevant for games targeting anime/cartoon aesthetics in real-time 3D.
- **Skeletal animation systems:** The document assumes the linear blend skinning model universal in game engines. This connects to the skeletal animation implementation in [[s030-game-programming-in-cpp-madhav|s030 Madhav (2018)]] (Ch. on skeletal animation) and the animation system in [[s040-unity-game-dev-24-hours|s040 Unity]] (Animators/Animation chapters).
- **Technical art as a discipline:** Both ArcSys documents exemplify the technical artist role — bridging modeling/rigging (art) and shader/engine (code). This role is described in [[../../wiki/concepts/production/team-and-culture|team-and-culture]] and hinted at in [[s019-the-door-problem|s019 The Door Problem]].

## Notable quotes

- "Proposition: 'Are you trying to solve all your skinning problems… with skinning?'" (Outline)
- "The human body is full of stuff inside it. The joints don't become thin even if bent. Only if you bend an empty thing, such as a rubber hose, will it behave like this." (Part 2)
- "No amount of tinkering with the skinning values will solve this problem. To solve this problem, we need a different approach." (Part 2 Conclusion)
- "Even in an extreme case, with all weights at 100%, a basic silhouette can still be created." (Part 4)
