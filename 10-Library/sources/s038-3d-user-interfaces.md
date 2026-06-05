---
id: s038
title: "3D User Interfaces: Theory and Practice (2nd Edition)"
author: "Joseph J. LaViola Jr., Ernst Kruijff, Ryan P. McMahan, Doug A. Bowman, Ivan Poupyrev"
year: 2017
publisher: Pearson
pages: 624
type: textbook
---

# s038 — 3D User Interfaces: Theory and Practice (2e)

**Authors:** LaViola, Kruijff, McMahan, Bowman, Poupyrev
**Publisher:** Pearson (Addison-Wesley Usability and HCI Series), 2017 · **Pages:** 624
**Endorsed by:** Richard Marks (Sony PlayStation Magic Lab), Andy Wilson (Microsoft Research), Mark Billinghurst (U. South Australia)

## Summary

The comprehensive academic reference for VR/AR interaction design. Covers the full stack from display hardware and spatial input devices to interaction technique taxonomies (manipulation, travel, system control) to design strategies and evaluation methodology. The book synthesizes decades of HCI and VR research into actionable design guidance. It is the theoretical counterpart to McCaffrey's UE4 cookbook (s039) — s038 gives the *why* and *taxonomy*, s039 gives the *how* in Blueprints.

## Key claims

### Foundations
- **3D UI definition:** interfaces in which users perform tasks in a 3D spatial environment using 3D interaction techniques (s038, ch.1). Distinguished from 2D GUIs by: continuous spatial input, six-degrees-of-freedom (6DOF) interaction, immersive display.
- **Why 3D UIs matter:** spatial tasks (manipulation, assembly, wayfinding, training simulations) are better supported by interaction modalities that match the task's spatial nature (s038, ch.1).
- Terminology: HMD, CAVE, Fish Tank VR, AR/MR; degrees of freedom (DOF); presence; immersion; proprioception (s038, ch.1).

### Human factors (Part II)
- **Information processing model:** sensory input → perception → cognition → motor output. Each stage introduces latency and error; good 3D UIs minimize cognitive load at each stage (s038, ch.3).
- **Perception:** visual (depth cues: stereopsis, motion parallax, perspective, occlusion), proprioceptive, vestibular. VR sickness occurs when visual and vestibular signals conflict.
- **Cognition:** spatial cognition, mental models, attention, memory limitations. 3D UIs can exceed working memory faster than 2D because spatial navigation adds cognitive overhead (s038, ch.3).
- **Physical ergonomics:** "Gorilla arm" problem — extended arm use at shoulder height is fatiguing; input devices must account for natural arm postures (s038, ch.3).

### Hardware (Part III)
- **Output hardware (ch.5):** HMDs (optical and video see-through), CAVEs, projection displays, haptic devices, audio spatialization.
- **Input hardware (ch.6):** tracking systems (optical, magnetic, inertial), gloves, motion controllers, eye tracking, physiological input. Key specs: latency (<20ms for presence), accuracy, drift.

### Interaction techniques (Part IV)
**Selection and Manipulation (ch.7):**
- *Grasping metaphors:* direct touch, virtual hand (co-located), ray casting (pointing), HOMER (hand offset)
- *Manipulation DOF:* position only; position + orientation; full 6DOF
- *Bimanual interaction:* dominant hand for precision, non-dominant for reference frame; Guiard's kinematic chain model
- *Indirect manipulation:* widgets, handles, constraints

**Travel (ch.8):**
- **Walking/natural locomotion:** highest presence, limited scale
- **Steering metaphors:** joystick/thumbstick flying; gaze-directed; head-directed
- **Selection-based travel:** teleportation (arc-based, point-and-click); reduces VR sickness; reduces presence
- **Route planning:** map + navigate vs. continuous navigation
- **Redirected walking:** imperceptibly rotate the virtual world to extend physical space

**System Control (ch.9):**
- **Voice commands:** high cognitive overhead; poor in noisy environments
- **Menus in 3D space:** pop-up, pie/radial, world-anchored, hand-held
- **Embodied/tangible controls:** physical props mapped to virtual objects

### Design strategies (Part V)
- **Design process for 3D UIs (ch.10):** identify task requirements → generate interaction technique candidates → prototype → evaluate. Iterative; never skip user testing.
- **Three design dimensions:** input modality, display type, interaction technique.
- **Transfer-appropriate processing:** match interaction technique to the real-world task analogue where possible.
- **Comfort-presence tradeoff:** techniques that maximize presence (natural walking, 6DOF manipulation) often maximize VR sickness risk. Teleportation sacrifices presence for comfort.

### Evaluation (ch.11)
- Controlled experiments (task completion time, error rate, NASA-TLX workload), presence questionnaires (IPQ, SUS), qualitative think-aloud.

## Chapter structure

**Part I:** Ch.1 Introduction · Ch.2 History and Roadmap
**Part II:** Ch.3 Human Factors · Ch.4 General HCI Principles
**Part III:** Ch.5 Output Hardware · Ch.6 Input Hardware
**Part IV:** Ch.7 Selection and Manipulation · Ch.8 Travel · Ch.9 System Control
**Part V:** Ch.10 Design Strategies · Ch.11 Evaluation
**Part VI:** Ch.12 The Future of 3D UIs

## Connections and cross-links

- **UE4 VR implementation:** Direct theoretical partner to [[../../10-Library/sources/s039-unreal-engine-vr-cookbook|s039 (McCaffrey)]]. s038 supplies the taxonomy and design rationale; s039 provides Blueprint implementations.
- **HCI/usability foundations:** Extends [[../../wiki/concepts/interface/usability-and-hcd|usability-and-hcd (s015 Norman)]] into 3D space. Norman's 6 principles (affordances, mappings, feedback, conceptual model) apply with extra spatial dimensions.
- **Game feel and input:** Travel techniques and selection metaphors directly inform [[../../wiki/concepts/feel-and-controls/input-and-controls|input-and-controls]] and [[../../wiki/concepts/feel-and-controls/game-feel|game-feel]]. Gorilla arm fatigue is a physical game feel issue.
- **Player psychology:** Presence, immersion, and VR sickness connect to [[../../wiki/concepts/player/player-psychology|player-psychology]] — the physical dimension of player experience.
- **Hot Potato:** Not a VR game; however, the manipulation/affordance and travel comfort tradeoffs are useful mental models for any controller-input design.
