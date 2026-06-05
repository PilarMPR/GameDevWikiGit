---
id: s030
title: "Game Programming in C++: Creating 3D Games"
author: Sanjay Madhav
year: 2018
type: book
tags: [game-dev, programming, cpp, 3d-graphics, opengl, audio, animation, collision, ui]
sources: [s030]
---

# s030 · Game Programming in C++ (Madhav)

**Full title:** Game Programming in C++: Creating 3D Games
**Author:** Sanjay Madhav | **Year:** 2018 | **Publisher:** Pearson (Addison-Wesley Game Design and Development Series)
**Type:** Book | **Pages:** ~526

## Summary

A project-based C++ game programming textbook that extends Madhav's earlier 2D/algorithmic-focused s026 into 3D territory. Whereas s026 covers algorithms and techniques in a language-agnostic style, s030 takes a hands-on approach: each chapter builds a working C++ game component using SDL2 and OpenGL, progressing from a 2D Pong/Asteroids prototype through a 3D scene with full skeletal animation, collision detection, AI, audio (FMOD), user interfaces, and level serialization. Written for readers who already know C++ and basic game loops. The USC game programming curriculum foundation. 2018 publication means coverage includes modern C++11/14 patterns and contemporary engine architecture (component model similar to Unity/Unreal).

## Key claims & concepts

- **Game loop anatomy (Anatomy of a Frame)**: ProcessInput → UpdateGame → GenerateOutput; delta time calculation for frame-rate independence. (s030, ch.1)
- **Component-based game object model**: Actor + Component architecture where each Actor holds a collection of Components; mirrors Unreal Engine's Actor-Component paradigm. (s030, ch.2)
- **2D → 3D graphics progression**: color buffer, double buffering (ch.1-2), then full OpenGL pipeline: vertex/fragment shaders, matrices, lighting, 3D transformations (ch.5-6).
- **Physics with vectors**: vector math, Newton's equations, basic collision response — the necessary maths for game physics without a full physics engine. (s030, ch.3)
- **AI fundamentals**: steering behaviors (seek, flee, wander), state machines; path following. (s030, ch.4)
- **Audio via FMOD**: sound loading, playback, 3D positional audio, sound buses, FMOD Studio integration. (s030, ch.7)
- **Input systems**: keyboard/mouse/gamepad handling; event-driven vs. polling; action mapping abstraction. (s030, ch.8)
- **Camera systems**: follow camera, orbit camera, first-person camera implementations in 3D. (s030, ch.9)
- **Skeletal animation pipeline**: skeleton hierarchy, skinning, animation blending, FBX asset loading. (s030, ch.12)
- **Level serialization**: JSON/binary level files, asset loading pipelines. (s030, ch.14)
- **Collision detection**: AABB, sphere, OBB; narrow/broad phase; response integration. (s030, ch.10)

## Chapter overview

| Ch | Title | Key topics |
|----|-------|-----------|
| 1 | Game Programming Overview | Game loop; anatomy of a frame; SDL2 setup; delta time; basic 2D graphics |
| 2 | Game Objects and 2D Graphics | Actor-Component model; sprite rendering; animated sprites; scrolling backgrounds |
| 3 | Vectors and Basic Physics | Vector math; Newton's laws; force/velocity integration; spring physics |
| 4 | Artificial Intelligence | Steering behaviors; pathfinding basics; state machines; decision trees |
| 5 | OpenGL | OpenGL pipeline; vertex/fragment shaders; GLSL; vertex buffers |
| 6 | 3D Graphics | Transformation matrices; projection; lighting (Phong); normal mapping |
| 7 | Audio | FMOD integration; sound loading; 3D audio; sound buses |
| 8 | Input Systems | Keyboard/mouse/gamepad; action mapping; event system |
| 9 | Cameras | Follow camera; orbit camera; first-person camera; spring arm |
| 10 | Collision Detection | AABB; sphere; OBB; broad/narrow phase; physics component |
| 11 | User Interfaces | UI rendering; buttons; canvas system; font rendering |
| 12 | Skeletal Animation | Skeleton hierarchy; skinning; animation blending; FBX loading |
| 13 | Intermediate Graphics | Shadow mapping; deferred rendering; particle systems |
| 14 | Level Files and Binary Data | JSON level files; binary serialization; asset loading pipeline |
| A | Intermediate C++ Review | References; templates; smart pointers; STL containers; iterators |

## Connections to wiki

- **Relationship to s026 (Madhav's earlier book)**: s030 is the direct sequel. s026 covers algorithms (A*, FSMs, networking basics) at a conceptual level; s030 implements a full 3D engine from scratch. Together they form Madhav's complete game programming curriculum. Cross-reference [[../../10-Library/sources/s026-game-programming-algorithms-and-techniques]].
- **Game Loop**: ch.1's ProcessInput/UpdateGame/GenerateOutput loop is the canonical implementation of the pattern described in [[../../wiki/concepts/mechanics/game-loops]] and theorized in Nystrom (s029, ch.9). Three sources now cover game loops from different angles (Madhav s026 introductory, Madhav s030 implementation, Nystrom architectural).
- **Component model**: ch.2's Actor-Component architecture is the practical C++ implementation of Nystrom's Component pattern (s029, ch.14) and foreshadows Unreal Engine's Actor-Component-UObject hierarchy (relevant to Hot Potato UE5 work).
- **AI / steering behaviors**: ch.4 connects to [[../../wiki/concepts/mechanics/game-loops]] (AI as dynamic behavior generator) and to s026's FSM coverage. Steering behaviors (Reynolds) are foundation for crowd/enemy systems.
- **Audio chapter**: ch.7 is the wiki's first technical treatment of audio implementation. Cross-references [[../../10-Library/sources/s032-writing-interactive-music-sweet]] (the compositional/creative side of game audio).
- **Cybernetics and emergence**: the full game-object model (Actor + Component + delta-time update loop) is the practical realization of [[../../05-Syntheses/Cybernetics, Complexity & Emergent Systems]] — emergent behavior arises from interactions among independently updated components.

## Notable quotes

- "The game loop is the heartbeat of any real-time game. It processes input, updates the game state, and generates output, repeatedly, until the game ends." (s030, ch.1)
- "The Actor-Component model gives each actor a collection of components that define its behavior — the actor is a container, not a monolith." (s030, ch.2)
