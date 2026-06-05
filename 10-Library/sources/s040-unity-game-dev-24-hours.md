---
id: s040
title: "Sams Teach Yourself Unity Game Development in 24 Hours"
author: Mike Geig
year: 2022
type: book
tags: [game-dev, unity, engine, beginner, tutorial, c-sharp, 3d]
---
# s040 · Unity Game Development in 24 Hours

**Full title:** Sams Teach Yourself Unity Game Development in 24 Hours · **Author:** Mike Geig (Unity Technologies production team) · **Year:** 2022 (© Pearson Education, ISBN 978-0-13-744508-0) · **Publisher:** Sams Publishing / Pearson

## Summary

A hands-on beginner Unity textbook structured as 24 one-hour lessons, culminating in four complete playable games. Covers the full Unity editor workflow — from installation and navigation to scripting, physics, animation, audio, UI, particle systems, mobile deployment, and final build/deploy. The author's philosophy is that readers should have a portfolio of games, not just theory, by the end of the book. (s040)

## Key claims & concepts

- **Unity Hub** is the centralized launcher for managing editor versions and projects; the LTS (Long Term Support) build is the recommended target for production. (s040, Hr.1)
- **Unity Editor views:** Project (asset browser), Hierarchy (scene graph), Scene (3D/2D viewport), Inspector (property editor), Game (preview). Any view can be moved, docked, duplicated, or resized; layouts are saveable. (s040, Hr.1)
- **Asset vs. Game Object distinction:** An *asset* is a file in the Assets folder (texture, mesh, script); a *game object* is a scene instance. Assets can generate game objects and vice versa. All asset management should be done inside Unity to preserve links. (s040, Hr.2)
- **Transforms** are the foundational component of every game object (position, rotation, scale in 3D coordinate space). (s040, Hr.2)
- **Prefabs** are reusable game-object blueprints; modifications to the prefab propagate to all instances. (s040, Hr.11)
- **Scripting in C#** — variables, conditionals, iteration, methods, input handling, component access, inter-object communication are progressive topics across Hr.7–8. Scripts attach to game objects as components.
- **Physics via Rigidbodies and Colliders** — collision detection, triggers, raycasting. (s040, Hr.9)
- **2D tools** — Orthographic cameras, Sprites, Tilemaps, 2D physics. (s040, Hr.12–13)
- **UI system** — Canvas, UI elements (Text, Button, Image), Canvas Render Modes (Screen Space Overlay/Camera, World Space). (s040, Hr.14)
- **Particle Systems** — modules-based with a Curves Editor; smoke, fire, effects. (s040, Hr.16)
- **Animator / Animation system** — Animation clips, Animator Controller state machines, scripted parameter control. (s040, Hr.17–18)
- **Timeline** — cinematic sequencing of multiple tracks (animation, audio, activation). (s040, Hr.19)
- **Audio** — AudioSource, AudioClip, Audio Mixer, scripted triggering. (s040, Hr.21)
- **Mobile deployment** — build targets, accelerometer input, touch input. (s040, Hr.22)
- **Scene management, data persistence, Player Settings, build pipeline.** (s040, Hr.23)
- Four built-in project games: *Amazing Racer* (Hr.6), *Chaos Ball* (Hr.10), *Captain Blaster* (Hr.15), *Gauntlet Runner* (Hr.20).
- **Project organization rule of thumb:** one folder per asset type, every asset in a folder, folder hierarchy becomes more specific. (s040, Hr.1)

## Chapter overview (24 Hours)

| Hour | Topic |
|------|-------|
| 1 | Installation, Unity Hub, editor interface, scene navigation |
| 2 | Game Objects, Transforms, 3D coordinate systems |
| 3 | Models, Materials, Textures, Shaders |
| 4 | Terrain generation, terrain textures, trees/grass, Character Controllers |
| 5 | Lights (directional/point/spot), Cameras, Layers |
| 6 | **Game 1: Amazing Racer** — design, world, gamification, playtesting |
| 7 | Scripting Pt.1: variables, operators, conditionals, iteration |
| 8 | Scripting Pt.2: methods, input, component access, inter-object |
| 9 | Collision: Rigidbodies, Colliders, Triggers, Raycasting |
| 10 | **Game 2: Chaos Ball** |
| 11 | Prefabs |
| 12 | 2D tools: sprites, orthographic cameras, draw order, 2D physics |
| 13 | 2D Tilemaps, Palettes, Tiles, physics integration |
| 14 | UI: Canvas, elements, render modes |
| 15 | **Game 3: Captain Blaster** |
| 16 | Particle Systems and Curves Editor |
| 17 | Animations: types, tools |
| 18 | Animators: state machines, asset configuration, scripting |
| 19 | Timeline |
| 20 | **Game 4: Gauntlet Runner** |
| 21 | Audio: sources, scripting, mixers |
| 22 | Mobile: build targets, accelerometers |
| 23 | Scene management, data persistence, build pipeline |
| 24 | Wrap-up and resources |

## Connections to wiki

- **Engine companion:** pairs well with [[s026-game-programming-algorithms-and-techniques|s026 Madhav (2014)]] (programming fundamentals) and [[s030-game-programming-in-cpp-madhav|s030 Game Programming in C++]] for architecture depth behind the Unity abstractions.
- **Component/ECS model:** Unity's component system is the runtime manifestation of the Component pattern discussed in [[s029-game-programming-patterns-nystrom|s029 Game Programming Patterns (Nystrom)]].
- **Agile/iteration:** The hands-on project-first structure aligns with iterative design doctrine in [[s036-agile-game-development-keith|s036 Agile Game Development]]; each "game" is a Minimum Viable Game (MVG).
- **Game feel:** Unity's Animator, particle systems, and Audio Mixer are the primary tools for implementing juice/polish as described in [[../../10-Library/sources/s018-juice-it-or-lose-it|s018 Juice It or Lose It]].
- **UI design:** The Canvas system is the practical implementation layer for the HUD/UI concepts in [[../../wiki/concepts/interface/ui-design|UI Design]].
- Relevant concept: [[../../wiki/concepts/production/iterative-design|iterative-design]] (playtesting step in each game hour).

## Notable quotes

- "By the time you are done reading this book, you won't have just theoretical knowledge of the Unity game engine. You will have a portfolio of games to go with it." (Preface)
- "Unity maintains links between the various assets associated with projects. As a result, moving or deleting items outside Unity could potentially cause problems." (Hr.1)
