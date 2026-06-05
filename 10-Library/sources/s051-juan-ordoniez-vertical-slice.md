# s051 — Level Design: Vertical Slice

**ID:** s051
**Title:** Vertical Slice — Diseño de videojuegos: Niveles
**Author:** Juan P. Ordóñez (juanpablo.ordonez@esne.es / @JuanPOrdonez)
**Date:** n.d. (lecture PDF, ESNE)
**Type:** Lecture PDF (9 pages)
**Language:** Spanish
**Link:** n/a (internal course material)
**Related sources:** [[s049-juan-ordoniez-nivel-1-proceso]] · [[s050-juan-ordoniez-4-flows]]

---

## Summary

A short lecture defining the "Vertical Slice" as Ordóñez uses it in the context of **level design documentation** — notably, a different usage from the production milestone meaning. Here, the Vertical Slice is a narrative/analytical document that describes a level in exhaustive first-person detail, then uses color-coded annotation to extract all production-relevant asset lists. It is a tool for aligning the whole team around a shared vision of the level before building it.

> **Note on terminology:** In standard production usage (see [[s049-juan-ordoniez-nivel-1-proceso]]), "Vertical Slice" refers to a playable build milestone. Ordóñez applies the term to a pre-production documentation method in the level design context — the two usages co-exist in industry practice. (s051)

---

## Key claims

- A Vertical Slice in this context is a **document** that visualizes the level scenario in the greatest possible detail before it is built (s051).
- Requires prior input: game design documentation, the narrative script for the level, etc. (s051).
- Written from the **player's point of view** — the author must assume the player knows nothing about the game unless explicitly shown or told within it (s051).
- The document helps control the user experience, identify audio sources, locate all interactions, deepen the learning process through space, and work from an emotional standpoint (s051).

---

## The 4-Step Vertical Slice Process

### Step 1: Narración (First-person narrative description)
A document narrating in first person everything that happens from player spawn to level completion. Must describe clearly (s051):
- Surroundings (general description)
- What the player sees; what the space looks like
- What the player hears at every moment
- All objects in each zone (named, with state and position)
- Available actions — and which ones lead to progression
- What the player learns
- Lighting and environmental conditions
- How the player feels / what they feel before performing actions

### Step 2: Identificación (Color-coded annotation)
Using a distinct color per concept, every element is marked in the narrative document (s051):
- Assets → red
- Audio → green
- Actions → blue
- Spaces/rooms → yellow
- Atmosphere/lighting details → brown
- Learning points → pink
- Sensations/emotions → cyan

### Step 3: Listado (Production lists)
From the color-coded document, extract separate lists for each element type (s051):
- Assets
- Audios (SFX, voices, music)
- Actions/interactions
- Spaces/rooms/corridors/open areas
- Atmosphere and lighting details
- Learning points
- Sensations/emotions

These lists serve as production checklists for collaboration with all departments.

### Step 4: Puesta en común (Team alignment)
- Share the lists and narrative with the full team.
- Production manages implementation with the respective departments.
- The narrative description helps everyone visualize the intended user experience, improving communication quality and preventing misaligned interpretations of the final level (s051).

---

## Key concepts & cross-links

- This VS methodology is a pre-production version of the 4 Flows framework: [[s050-juan-ordoniez-4-flows]] — the emotional and spatial elements of the VS map to the Emotional and Spatial flows.
- The color-coded annotation method is a practical operationalization of the "indirect control" table in [[../../wiki/concepts/level-design/spatial-design]].
- "Player's point of view, no assumed knowledge" directly echoes the player-centric design stance in [[../../10-Library/sources/s006-fundamentals-of-game-design]] (Adams) and [[../../10-Library/sources/s008-game-design-workshop]] (Fullerton).
- The asset/audio extraction step bridges into production documentation: [[../../wiki/concepts/production/documentation]] and [[../../10-Library/sources/s045-game-development-and-production-bethke]].
- The team alignment function mirrors the "Inception Deck" mentioned in [[s049-juan-ordoniez-nivel-1-proceso]].
- Companion lecture: [[s049-juan-ordoniez-nivel-1-proceso]] (process and departments).
- Companion lecture: [[s050-juan-ordoniez-4-flows]] (the 4 Flows documentation framework).
