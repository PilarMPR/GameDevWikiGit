---
id: s043
title: "Augmented Reality: Principles and Practice"
author: Dieter Schmalstieg, Tobias Höllerer
year: 2016
type: book
tags: [ar, vr, xr, computer-vision, tracking, hci, software-architecture, academic]
---
# s043 · Augmented Reality: Principles and Practice

**Full title:** Augmented Reality: Principles and Practice · **Author:** Dieter Schmalstieg (TU Graz) & Tobias Höllerer (UC Santa Barbara) · **Year:** 2016 (first printing June 2016; © Pearson Education, ISBN 978-0-321-88357-5) · **Publisher:** Addison-Wesley / Pearson · **Pages:** 527

> **Note:** 346 MB PDF. Source page based on full TOC (pp.1–20) and Preface; no deep chapter extraction performed. This is an academic/technical textbook — extremely dense on algorithms, computer vision, and software architecture.

## Summary

The definitive academic textbook on augmented reality, covering the complete technical stack from display hardware and tracking algorithms through computer vision, visual coherence, interaction, authoring, navigation, collaboration, and software architecture. Framed around the idea that AR is emerging as the dominant user interface metaphor for *situated computing* — the physical world becomes the user interface. The book is positioned at the transition from mobile/desktop computing to ubiquitous, anywhere-anytime computing where AR is the natural interface layer. (s043)

## Key claims & concepts

- **AR as situated computing UI metaphor:** As users move away from the desktop, including the physical world in computing experience becomes logical. AR provides a direct link between physical reality and virtual information — "the world becomes the user interface." (s043, Preface)
- **Mixed Reality Continuum:** AR exists on a continuum between fully real and fully virtual (Milgram & Kishino, cited). (s043, Ch.1)
- **Display taxonomy** (Ch.2): Near-eye displays, handheld displays, stationary displays, projected displays. Key display characteristics: method of augmentation, ocularity/stereoscopy, focus, occlusion, resolution/refresh, FoV, viewpoint offset, brightness/contrast, latency, ergonomics, social acceptance.
- **Tracking** (Ch.3): Coordinate systems, tracking characteristics (physical phenomena, measurement principle, degrees of freedom, workspace coverage, measurement error, temporal characteristics). Technology types: mechanical, electromagnetic, ultrasonic, GPS, wireless networks, magnetometer, gyroscope, accelerometer, odometer, optical.
- **Computer vision for AR** (Ch.4): Marker tracking (camera representation, marker detection, pose estimation from homography), natural feature tracking (interest point detection, descriptor creation/matching, SLAM). Key algorithms: Kanade-Lucas-Tomasi tracking, ZNCC, parallel tracking and mapping, relocalization.
- **Calibration and Registration** (Ch.5): Camera calibration (internal parameters, lens distortion correction), display calibration, hand-eye calibration. Registration errors: geometric distortions, error propagation, latency.
- **Visual coherence** (Ch.6): Registration, occlusion (probabilistic, model-free), photometric registration (image-based lighting, light probes), common illumination (differential rendering, global illumination, shadows), diminished reality.
- **Situated Visualization** (Ch.7): Data overload, annotations/labeling, X-ray visualization, spatial manipulation, information filtering.
- **Interaction** (Ch.8): Output modalities (augmentation placement, agile displays, magic lenses), input modalities (rigid object tracking, body tracking, gestures, touch, tangible interfaces), haptic interaction, multimodal interaction.
- **Authoring** (Ch.10): Elements (actors, story, stages, interactions, setup), desktop authoring, authoring by performance, web technology.
- **Software Architectures** (Ch.13): AR application requirements (environment control, display space, real-virtual consistency, semantic knowledge); distributed computing, dataflow graphs, scene graphs, declarative/procedural scripting.
- **SLAM (Simultaneous Localization and Mapping):** core enabling technology for tracking in unknown environments; five-point algorithm, bundle adjustment, parallel tracking and mapping (PTAM). (s043, Ch.4)
- **Future AR drivers** (Ch.14): Better displays, outdoors use, uncooperative users, AR as dramatic medium, AR as social computing platform, confluence with VR, augmented humans.

## Chapter overview

| Ch. | Topic |
|-----|-------|
| 1 | Introduction to Augmented Reality (definition, history, examples, related fields, mixed reality continuum) |
| 2 | Displays (multimodal; visual perception requirements; near-eye, handheld, stationary, projected) |
| 3 | Tracking (coordinate systems, technology types, sensor fusion) |
| 4 | Computer Vision for AR (marker tracking, natural features, SLAM, outdoor tracking) |
| 5 | Calibration and Registration |
| 6 | Visual Coherence (occlusion, photometric registration, global illumination, diminished reality) |
| 7 | Situated Visualization (data overload, labeling, X-ray, spatial manipulation) |
| 8 | Interaction (output/input modalities, tangibles, haptic, multimodal) |
| 9 | Modeling and Annotation |
| 10 | Authoring |
| 11 | Navigation |
| 12 | Collaboration (co-located and remote) |
| 13 | Software Architectures (distributed computing, dataflow, scene graphs, scripting) |
| 14 | The Future |

## Connections to wiki

- **Primary AR/VR academic reference:** This is the most technically rigorous AR source in the wiki. Complements the practitioner survey in [[s042-practical-augmented-reality|s042 Aukstakalnis (2017)]] (hardware/human factors) and the UE4 implementation guide in [[s039-unreal-engine-vr-cookbook|s039 McCaffrey (2017)]].
- **Also complements s038:** [[s038-3d-user-interfaces|s038 LaViola et al. (2017)]] covers 3D UI interaction technique taxonomy; s043 provides the deeper computer vision and software architecture underpinning.
- **SLAM as game-dev relevance:** SLAM algorithms from Ch.4 are the backbone of modern mobile AR (ARKit, ARCore) and are relevant to any games using markerless tracking; see [[../../wiki/concepts/feel-and-controls/game-feel|game-feel]] for immersion implications.
- **Software architecture chapter (Ch.13)** bridges to [[s029-game-programming-patterns-nystrom|s029 Game Programming Patterns]] — dataflow graphs, scene graphs, and scripting architectures in AR mirror game engine patterns.

## Notable quotes

- "Augmented reality (AR) has the potential to become the leading user interface metaphor for situated computing. The world becomes the user interface." (Preface)
- "Virtual reality, which by definition monopolizes our attention, is not necessarily a good fit for everyday and spontaneous use of computing." (Preface)
