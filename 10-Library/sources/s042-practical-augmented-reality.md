---
id: s042
title: "Practical Augmented Reality: A Guide to the Technologies, Applications, and Human Factors for AR and VR"
author: Steve Aukstakalnis
year: 2017
type: book
tags: [ar, vr, xr, hardware, human-factors, hmd, sensors, applications, game-dev]
---
# s042 · Practical Augmented Reality

**Full title:** Practical Augmented Reality: A Guide to the Technologies, Applications, and Human Factors for AR and VR · **Author:** Steve Aukstakalnis (former Director, Virtual Environment and Interactive Systems Program, NSF) · **Year:** 2017 (first printing September 2016; © Pearson Education, ISBN 978-0-13-409423-6) · **Publisher:** Addison-Wesley Professional / Pearson

## Summary

A practitioner-facing survey of AR and VR technologies, organized from the inside out: it begins with the human perceptual system (sight, hearing, touch), then covers the hardware that exploits those perceptual systems (HMDs, spatial audio, haptic devices, tracking sensors), then surveys real-world applications, and closes with human factors, legal/ethical issues, and future outlook. Written for undergraduate/graduate courses in CS, engineering, and architecture, and for practitioners in business and science. The author stands on the shoulders of AR/VR pioneers from the 1980s–90s (Furness, Lanier, Fisher, Brooks, etc.). (s042)

## Key claims & concepts

- **AR definition:** overlays alphanumeric, symbolic, or graphical information on a user's real-world view in a spatially contextual and stabilized manner; coined by Boeing's Tom Caudell in 1992. (s042, Ch.1)
- **Historical lineage of AR:** the first AR device is arguably Howard Grubb's 1901 collimating reflector sight (gun sight overlaying a virtual reticle on a real-world target); led directly to 1918 Oigee Reflector Sight and modern HUDs. (s042, Ch.1)
- **Head-Up Displays (HUDs):** three components — projector, combiner (glass), video generation computer; information collimated at optical infinity so pilot's eyes don't need to refocus. First combat HUD was Blackburn Buccaneer (1958). (s042, Ch.1)
- **Two types of wearable AR displays:**
  - *Optical see-through:* user looks through optical elements (holographic waveguides, etc.); graphics overlaid directly.
  - *Video see-through:* outward cameras capture real world, blend with CGI, display on HMD screen. (s042, Ch.1)
- **Handheld/mobile AR** is a video see-through device using smartphone/tablet cameras. (s042, Ch.1)
- **The human eye can only focus on one depth plane at a time** — a fundamental challenge AR systems must address through collimation. (s042, Ch.1)
- **Spatial vision and depth cues** (Ch.3), **audio 3D localization** (Ch.7), **tactile/haptic feedback** (Ch.9–10): each sense covered before its hardware chapter.
- **Tracking technologies** (Ch.11): optical, beacon, electromagnetic, inertial, acoustic — each with different accuracy/latency/workspace tradeoffs.
- **Vergence–accommodation conflict:** a key human factors problem — eyes verge for 3D depth cue while display focal plane remains fixed (Ch.21).
- **Visually-induced motion sickness:** caused by sensory mismatch between visual (showing motion) and vestibular (detecting stillness) systems. (s042, Ch.21)
- **Legal considerations** (Ch.22): product safety, courtroom evidence, increasing violence/realism of first-person games.
- **Applications survey:** gaming/entertainment, architecture/construction, science/engineering, health/medicine, aerospace/defense, education, telerobotics, big data visualization.

## Chapter overview

| Ch. | Topic |
|-----|-------|
| 1 | Computer-Generated Worlds — AR/VR definitions, history (Grubb→HUD→helmet sights→smart glasses), optical/video see-through taxonomy |
| 2 | Understanding Virtual Space — coordinate systems, navigation |
| 3 | The Mechanics of Sight — visual pathway, spatial vision, monocular/stereo depth cues |
| 4 | Component Technologies of HMDs — display types, ocularity, optical architectures |
| 5 | Augmenting Displays — binocular and monocular AR headsets on market |
| 6 | Fully Immersive Displays — PC/console HMDs, smartphone-based, CAVEs |
| 7 | The Mechanics of Hearing — sound physics, auditory pathway, 3D localization, vestibular system |
| 8 | Audio Displays — spatial audio solutions |
| 9 | The Mechanics of Feeling — skin anatomy, mechanoceptors, proprioception |
| 10 | Tactile and Force Feedback Devices — haptic illusions, tactile and force feedback hardware |
| 11 | Sensors for Tracking — optical, beacon, EM, inertial, acoustic |
| 12 | Devices for Navigation and Interaction — hand/gesture tracking, whole body, BCI |
| 13 | Gaming and Entertainment |
| 14 | Architecture and Construction |
| 15 | Science and Engineering |
| 16 | Health and Medicine |
| 17 | Aerospace and Defense |
| 18 | Education |
| 19 | Information Control and Big Data Visualization |
| 20 | Telerobotics and Telepresence |
| 21 | Human Factors Considerations — motion sickness, vergence-accommodation conflict |
| 22 | Legal and Social Considerations |
| 23 | The Future |

## Connections to wiki

- **Companion to s038 and s039:** This source (s042) is the hardware/human-factors companion to [[s038-3d-user-interfaces|s038 3D User Interfaces (LaViola et al., 2017)]] which covers interaction techniques, and [[s039-unreal-engine-vr-cookbook|s039 UE4 VR Cookbook (McCaffrey, 2017)]] which covers engine implementation. s042 fills the hardware/perception layer those sources assume.
- **Companion to s043:** [[s043-augmented-reality-pearson|s043 Augmented Reality (Schmalstieg & Höllerer, 2016)]] is the technical/academic counterpart — covering computer vision, tracking algorithms, software architecture in depth. s042 is the practitioner/hardware survey; s043 is the theoretical/algorithmic treatment.
- **Human factors:** The vergence–accommodation conflict and motion sickness material connects to the player psychology concepts in [[../../wiki/concepts/player/player-psychology|player-psychology]] and the cognitive load discussion in [[../../wiki/concepts/interface/ui-design|ui-design]].
- **Historical AR applications:** The HUD and helmet-sight history puts game AR in lineage — AR gaming is just the latest application of 100+ year-old optical overlay technology.

## Notable quotes

- "Despite the public fascination with augmented reality (AR) and virtual reality (VR), few within the broader audience understand how these systems actually function." (Preface)
- "The true pioneers of augmented and virtual reality can be found in the scientific literature, tech briefs, conference proceedings, and patents filings of the 1980s and 1990s." (Preface)
- "As a developer, use this book as an index of equipment in your tool belt and make sure to pick the right tool for the right job, even if that means not using VR or AR at all." — Victor Luo, NASA JPL (Foreword)
