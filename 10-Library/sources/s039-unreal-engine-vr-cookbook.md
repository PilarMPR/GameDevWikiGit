---
id: s039
title: "Unreal Engine VR Cookbook: Developing Virtual Reality with UE4"
author: Mitch McCaffrey
year: 2017
publisher: Pearson (Addison-Wesley Game Design and Development Series)
pages: 277
type: textbook
---

# s039 — Unreal Engine VR Cookbook (McCaffrey)

**Author:** Mitch McCaffrey (YouTube: Mitch's VR Labs; forums contributor at unrealengine.com)
**Publisher:** Pearson, 2017 · **Pages:** 277 · **Engine version:** UE4 (circa 4.14)
**Technical reviewers:** Luis Cataldi (Epic Games), Jeff Wilson, Clinton Crumpler

## Summary

A recipe-style UE4 Blueprint cookbook for VR development. Each chapter covers a discrete VR problem (HMD setup, trace interaction, teleportation, UI in VR, IK, motion controllers, locomotion, optimization) with step-by-step Blueprint implementations and exercises. The book is tightly scoped to UE4 Blueprints — C++ is not covered. It is the most practical companion to s038 (3D User Interfaces) in the wiki, providing engine-specific implementations of the interaction paradigms s038 catalogs theoretically.

> ⚠️ **Version caveat:** Written for UE4 (2017). UE5 introduced significant changes to the VR plugin architecture, XR API, and motion controller setup. Treat specific Blueprint node names as UE4-specific; the patterns and concepts transfer but implementations will need updating. (⚠️ sin verificar for UE5 specifics.)

## Key claims and recipes

### Part I: Getting Started

**Terminology (ch.1):**
- **HMD** (Head-Mounted Display), **Room-scale** vs. **Seated** tracking, **6DOF** vs. **3DOF** controllers.
- **SDK layers:** hardware SDK (Oculus SDK, SteamVR/OpenVR) → Unreal's VR plugin layer → Blueprint API.
- **Best practices:** always use "VR Preview" mode; disable Anti-Aliasing (TAA) in VR; lock framerate target before content authoring.

**HMD Setup (ch.2):**
- **Gear VR:** Android-based; requires Gear VR project settings, Global Menu setup (back button handler), Progress Material for loading screens. Samsung-specific SDK calls via `OculusFunctionLibrary`.
- **Rift and Vive:** PC-based; uses SteamVR plugin (both); Tracking Origin — Floor Level (room-scale) vs. Eye Level (seated). "Tracking Origin" is a critical UE4 setting affecting all pawn/controller transforms.

**Toolkit (ch.3):**
- `GenericFunctionLibrary` — cross-platform VR Blueprint helpers.
- `OculusFunctionLibrary` — Oculus-specific (guardian boundary, recenter HMD).
- `SteamVRFunctionLibrary` — SteamVR-specific queries.

### Part II: Recipes

**Trace Interaction (ch.4):**
- Uses UE4 line/sphere traces (raycasting from motion controller) to detect interactive objects.
- **Interface pattern:** `Interaction Interface` with `OnInteract` and `OnHoverBegin/End` functions; objects implement the interface, controller calls it — decouples interaction from object type. This is the UE4 Blueprint equivalent of the Observer pattern ([[../../10-Library/sources/s029-game-programming-patterns-nystrom|s029 Nystrom]] Event Queue / Observer).
- **Interaction Component:** Actor Component attached to pawn; handles trace logic and interface dispatch.

**Teleportation (ch.5):**
- **Parabolic tracing:** arc trace from motion controller; visualizes landing zone with a decal/mesh.
- **Visualization Material:** procedural ring/marker material on the teleport target.
- **Simple Teleport Volume:** trigger volume that teleports the pawn on overlap — good for doorways and scripted transitions.
- Maps directly to the "selection-based travel / teleportation" technique in s038 ch.8.

**UMG in VR (ch.6):**
- Challenge: 2D screen-space UMG widgets break in stereo VR (parallax mismatch).
- Solution: render UMG to a 3D Widget Component placed in the world (world-space widget). This eliminates parallax issues at the cost of requiring manual placement.
- Custom gaze/pointer interaction for menu selection (two approaches: trace-based and collision-based).

**Character Inverse Kinematics — IK (ch.7):**
- **Head IK:** drive the character's head bone from HMD transform (using animation Blueprint IK node + `Look At` solver). Requires a "mirror" scene component to account for HMD→character neck offset.
- **Hand IK:** Two-bone IK solver driven by left/right motion controller transforms. `Hand IK Animation Blueprint` maps controller position/rotation to arm pose.

**Motion Controller Interaction (ch.8):**
- Affordance-first design: controllers should feel physically natural — grabbable objects should look graspable (size, shape, handle indicators).
- Shared input mapping for Rift + Vive controllers (trigger = grab/select, grip = hold, thumbstick = navigate).
- **World Interaction Project:** grabbable Static Mesh Actor, interactive Button (press-and-release state machine), interactive Lever (constrained rotation arc) — each implemented as a Blueprint Actor implementing the World Interaction Interface.

**VR Locomotion (ch.9):**
- **Simulator sickness** caused by: visual-vestibular mismatch, latency, field-of-view conflicts.
- **Locomotion taxonomy** (maps directly to s038 ch.8 travel techniques):
  - *Natural* — physical room-scale walking; highest presence, limited to tracked space
  - *Teleportation* — arc-select and warp; lowest sickness, lowest presence
  - *Vehicle* — player is "in" a vehicle; sickness reduced by having a stable visual reference frame
  - *Physical* — treadmill or redirected walking hardware
  - *Artificial* — thumbstick locomotion; high sickness risk; requires comfort FOV reduction (vignette)
- **Snap turning** (ch.9 implementation): discrete 45°/90° rotation vs. smooth turning; snap turning dramatically reduces rotational VR sickness.
- **Running-in-place** detection: accelerometer threshold on HMD or foot trackers to trigger locomotion without physical movement.

**VR Optimization (ch.10):**
- **VR rendering requirements:** target 90+ fps per eye; any dropped frames cause judder and sickness. UE4 default Deferred Rendering is expensive for VR.
- **Forward Rendering:** UE4 Forward Rendering mode reduces draw calls and works better with MSAA; recommended for VR. Trade-off: fewer dynamic lights and no screen-space effects (s039, ch.10).
- **Instanced Stereo Rendering:** renders both eyes in a single pass using vertex shader instancing; halves draw call overhead. UE4 project setting (s039, ch.10).
- **Hidden Area Mesh Optimization:** masks pixels outside the visible area of the HMD lens; saves fill rate on GPU (s039, ch.10).
- **Timewarp/ATW (Asynchronous Timewarp):** hardware/driver technique that re-projects the last rendered frame to compensate for head movement during rendering latency. Reduces perceived judder without requiring perfect frame timing.
- **VR Project Settings checklist:** Forward Rendering ON, Instanced Stereo ON, Hidden Area Mesh ON, round-trip latency target <20ms.

## Chapter structure

**Part I: Getting Started**
- Ch.1 Terminology and Best Practices
- Ch.2 Head Mounted Display Setup (Gear VR; Rift and Vive)
- Ch.3 Toolkit (Generic/Oculus/SteamVR Function Libraries)

**Part II: Recipes**
- Ch.4 Trace Interaction
- Ch.5 Teleportation
- Ch.6 UMG and 2D User Interfaces in VR
- Ch.7 Character Inverse Kinematics
- Ch.8 Motion Controller Interaction
- Ch.9 VR Locomotion
- Ch.10 VR Optimization

## Connections and cross-links

- **3D UI theory (s038):** Direct implementation companion. s039's locomotion taxonomy (ch.9) implements s038's travel technique framework (ch.8). s039's trace interaction (ch.4) implements s038's ray-casting selection metaphor (ch.7). Read s038 for design rationale; s039 for Blueprint implementation.
- **Game programming algorithms (s026):** McCaffrey's VR game loop requirements (90fps, <20ms latency, per-frame head tracking) are the extreme end of the real-time game loop covered in [[../../10-Library/sources/s026-game-programming-algorithms-and-techniques|s026 (Madhav ch.1)]]. Frame-rate independence and delta-time (s026) are even more critical in VR.
- **Game Programming in C++ (s030):** The Actor/Component model used throughout s039 ([[../../10-Library/sources/s030-game-programming-in-cpp-madhav|s030 Madhav]]) — Interaction Components, Motion Controller Components, Animation Blueprints — directly correspond to s030's Actor + Component architecture. The IK Animation Blueprint pattern extends s030's skeletal animation chapter.
- **Game Programming Patterns (s029):** The `Interaction Interface` + `Interaction Component` decoupling pattern in ch.4 is a Blueprint implementation of the Observer / Command patterns from [[../../10-Library/sources/s029-game-programming-patterns-nystrom|s029 (Nystrom)]].
- **Forward Rendering vs Deferred:** The VR-specific argument for Forward Rendering (ch.10) connects to the rendering pipeline overview in s030 and s026.
- **Input and controls:** [[../../wiki/concepts/feel-and-controls/input-and-controls|input-and-controls]] — motion controllers add a physical ergonomics dimension absent in traditional gamepad design.
- **Hot Potato:** Hot Potato targets flatscreen UE5, not VR. However, the Blueprint architecture patterns (Interface components, decoupled interaction, locomotion state machines) are directly applicable to the UE5 pawn/movement design.
