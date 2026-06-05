# s050 — Level Design: Los 4 Flows

**ID:** s050
**Title:** Level Design: Los 4 flows — Diseño de experiencia de usuario en un espacio interactivo en videojuegos
**Author:** Juan P. Ordóñez (juanpablo.ordonez@esne.es / @JuanPOrdonez)
**Date:** n.d. (lecture PDF, ESNE)
**Type:** Lecture PDF (22 pages)
**Language:** Spanish
**Link:** n/a (internal course material)
**Related sources:** [[s049-juan-ordoniez-nivel-1-proceso]] · [[s051-juan-ordoniez-vertical-slice]]

---

## Summary

A focused lecture on Ordóñez's "4 Flows" framework for structuring level design documentation. Rather than thinking only about space and interactions, the designer must model four parallel flows — **Interactive, Narrative, Emotional, and Spatial** — and then cross-reference and align them before building the level. The primary goal is to control the user experience at a deeper level than traditional floor plans or interaction lists allow.

---

## The 4 Flows Framework

### 1. Flujo de Interacciones (Interaction Flow)
- Ordered list of player actions from spawn to scene transition (s050).
- Includes expected AND unexpected player behaviors — the level must respond to both with solidity and coherence.
- Captures: objects the player can interact with, items obtained/consumed, what the player learns in each zone, relevant NPCs (quest givers, bosses), and all UX/learning considerations.
- Information source: game design documentation (mechanics, rules, dynamics, learning progressions).
- Also captures spatial requirements: minimum/maximum sizes for mechanics and situations, placement of required elements.

### 2. Flujo Narrativo (Narrative Flow)
- Schematic, ordered summary of narrative events tied to specific zones of the level.
- Some narrative events are global (not tied to a specific zone — they provide context).
- Information source: the narrative department's script/storyline (s050).
- Example: "Sky is summoned by Clorthark to become a knight → must face his fears → Clorthark gives Sky the sword → friends cry → a grey wolf lurks at the forest edge."

### 3. Flujo Emocional (Emotional Flow)
- Ordered list of the emotions the player should feel at each relevant situation and space.
- Must be **cross-referenced with the Interaction and Narrative flows** before building the Spatial Flow, because the desired emotion affects space design: lighting, spatial perception, zone distribution, distances, interactions (s050).
- Example: spawn = tranquility (safe zone) → sword acquisition = expectation + joy → leaving the village = uncertainty → catacombs = claustrophobic anxiety → boss arrival area = impactful sensation → mission end = joy + recognition.

### 4. Flujo Espacial (Spatial Flow)
- Lists and describes each location/zone of the level according to what happens in it.
- Correspondence with the other three flows is flexible: 1-to-1, 1-to-many, or many-to-1.
- Zones can exist purely for tension release, as transition spaces, or as loading areas.
- Built last, informed by the other three flows.

### Why not a 5th Sound Flow?
- Audio documentation is typically handled by game design (greater flexibility and reuse of audio elements; avoids per-level designers requesting 20 tracks each).
- Game design maintains audio coherence (global ambiences: forest, horror, exploration, catacombs...).
- Exception: cinematics, game intros, credits — these justify dedicated per-level audio treatment.
- Ideal: game design and level design co-build the audio direction (s050).

---

## Key claims

- The 4 Flows framework provides more information for designing a level than thinking only about space and interactions (s050).
- Designing the emotional flow and crossing it with the other flows gives the designer much greater control over the player experience (s050).
- Cross-referencing immersion and believability of the level and game are enhanced by aligning all four flows (s050).
- The level designer begins work slightly after game design and is a natural integrator of all game elements — using placeholders until other departments deliver final work (s050).
- All flows must start with the player spawn and end with the transition to the next scene (s050, slide 11).
- Flow diagrams alone are insufficient; they need accompanying explanatory text with enough detail to understand each step (s050, slide 21).
- Cross-departmental communication is essential — each department knows best what should happen in the level from its own perspective (s050, slide 21).

---

## Information the level designer receives upfront
- **Game design:** mechanics, rules, dynamics, gameflow, systems, interaction tables, character definitions, AI, mission objectives.
- **Narrative:** storyline, character descriptions, setting, narrative objectives per zone.
- **Art:** concepts, some final art.
- **Programming:** core tech, level editor.
- **Production:** timeline pressure.
- **Audio:** "probably nothing" — this is noted as an error (s050, slide 4).

---

## Extended flows (mentioned but out of scope for the lecture exercise)
Beyond the four primary flows, Ordóñez notes that flow design can also be applied to: user experience, cultural, social, and psychological levels — but these are considered advanced/optional for the teaching context (s050).

---

## Key concepts & cross-links

- The Emotional Flow concept maps directly onto interest curves: [[../../10-Library/notes/interest-curves-schell]] (Schell s005 ch.9) — both use a temporal arc of designed emotional states.
- The Spatial Flow corresponds to the "spatial design" layer in [[../../wiki/concepts/level-design/spatial-design]].
- The Interaction Flow aligns with the "gameflow" concept in [[../../10-Library/sources/s049-juan-ordoniez-nivel-1-proceso]] (same author).
- The Narrative Flow bridges to [[../../wiki/concepts/narrative/story-and-games]] — particularly "embedded vs. emergent narrative" and environmental storytelling.
- The concept of crossing emotional and spatial design before building resonates with [[../../wiki/concepts/level-design/pacing-and-flow]].
- Companion lecture: [[s049-juan-ordoniez-nivel-1-proceso]] (level design process and departments).
- Companion lecture: [[s051-juan-ordoniez-vertical-slice]] (vertical slice methodology).
- Level design as integrator role: mirrors [[../../10-Library/sources/s019-the-door-problem]] (Liz England) — the level designer as the one object every discipline touches.
