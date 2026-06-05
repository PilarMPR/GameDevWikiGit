---
id: s029
title: "Game Programming Patterns"
author: Robert Nystrom
year: 2014
type: book
tags: [game-dev, programming, software-architecture, design-patterns, cpp, performance]
sources: [s029]
---

# s029 · Game Programming Patterns (Nystrom)

**Full title:** Game Programming Patterns
**Author:** Robert Nystrom | **Year:** 2014 | **Publisher:** Self-published (also free at gameprogrammingpatterns.com)
**Type:** Book | **Pages:** ~353

## Summary

A practical software architecture book for game programmers, adapted from Nystrom's years as an engineer at Electronic Arts. The book fills the gap between domain-specific graphics/physics books and generic software engineering texts by cataloguing patterns that are specifically useful — or specifically troublesome — in game codebases. It is structured in three sections: a revisit of classic Gang of Four (GoF) patterns with a game lens, and two sections of original game-specific patterns organized by concern (sequencing, behavioral, decoupling, optimization). Each pattern follows a rigorous template: Intent, Motivation, Pattern, When to Use, Keep in Mind, Sample Code (C++), Design Decisions, See Also. The book is notable for its candid critique of Singleton and for its central architecture thesis: good game architecture maximizes the ability to change code quickly without breaking things. Also available free online.

## Key claims & concepts

- **Architecture as change-enablement**: "good software architecture is code that lets you change quickly and confidently." The real cost is not writing code but changing it. (s029, ch.1)
- **Performance vs. architecture tension**: game-specific constraint — cache locality, tight loops, and real-time constraints push against clean abstraction; patterns must earn their indirection cost. (s029, ch.1)
- **Game Loop pattern**: decouple game time from user input and processor speed; fixed-update with variable render interpolation as the standard approach. (s029, ch.9)
- **Update Method pattern**: give each entity its own behavior tick; the collection of entities with update() is the basis of the game object model. (s029, ch.10)
- **Component pattern**: decompose entities into independent components (ECS precursor); reduces coupling and enables mix-and-match behavior composition. (s029, ch.14)
- **Event Queue pattern**: decouple senders from receivers asynchronously; prefer to Observer for high-frequency events where immediate dispatch causes cascades. (s029, ch.15)
- **State pattern (FSM)**: clean way to model character/AI behavior; hierarchical state machines as the scalable extension. (s029, ch.7)
- **Singleton critique**: Singleton is overused in games; it creates hidden global state and coupling; prefer passing dependencies explicitly or using Service Locator. (s029, ch.6)
- **Data Locality / cache performance**: organizing data for cache-friendly access (Structure of Arrays vs. Array of Structures) can be the dominant performance factor in hot loops. (s029, ch.17)
- **Object Pool pattern**: avoid dynamic allocation in real-time code; pre-allocate fixed pools for particles, bullets, enemies. (s029, ch.19)
- **Bytecode pattern**: implement a lightweight VM / scripting language to let designers tune behavior without recompilation. (s029, ch.11)
- **Double Buffer pattern**: prevent rendering artifacts by writing to one buffer while displaying another; canonical solution for frame-coherent rendering. (s029, ch.8)

## Chapter overview

| Section | Ch | Title | Key topics |
|---------|-----|-------|-----------|
| I | Intro | Architecture, Performance, and Games | What is good architecture; change cost; the performance–abstraction trade-off |
| II | 2 | Command | Undo/redo; input replay; decoupling input from action |
| II | 3 | Flyweight | Shared intrinsic state; tile/terrain data; instancing |
| II | 4 | Observer | Achievement systems; event-driven decoupling; GoF Observer pitfalls |
| II | 5 | Prototype | Cloning for spawning; data-driven prototypes; type objects |
| II | 6 | Singleton | Why to avoid it; alternatives (Service Locator, explicit passing) |
| II | 7 | State | FSM implementation; enum vs. class states; hierarchical + pushdown automata |
| III | 8 | Double Buffer | Frame rendering coherence; physics state snapshots |
| III | 9 | Game Loop | Fixed update; variable render; clock independence; power consumption |
| III | 10 | Update Method | Per-entity tick; sleeping entities; update ordering issues |
| IV | 11 | Bytecode | VM design; scripting for designers; security tradeoffs |
| IV | 12 | Subclass Sandbox | Safe base class operations; avoiding base-class coupling |
| IV | 13 | Type Object | Data-driven type hierarchy; spell/monster types |
| V | 14 | Component | Entity decomposition; physics + render + AI as components; ECS foundations |
| V | 15 | Event Queue | Async messaging; request vs. notification; ring buffer implementation |
| V | 16 | Service Locator | Global service access with swappable implementations; null service pattern |
| VI | 17 | Data Locality | Cache line size; hot/cold split; SoA vs. AoS |
| VI | 18 | Dirty Flag | Lazy recalculation; scene graph transforms |
| VI | 19 | Object Pool | Pre-allocation; particle systems; defragmentation |
| VI | 20 | Spatial Partition | Grid, quad tree, BSP for collision/query acceleration |

## Connections to wiki

- **Game Loop**: ch.9 is the canonical reference for the game loop pattern, directly extending [[../../wiki/concepts/mechanics/game-loops]] and the loop implementation notes in [[../../10-Library/sources/s026-game-programming-algorithms-and-techniques]]. Nystrom's treatment is more architectural; Madhav's (s026) is more introductory.
- **Component/ECS**: ch.14 provides the software-architecture foundation for the Entity-Component-System model referenced in [[../../10-Library/sources/s025-thief-dark-project-postmortem]] (Dark Object System as ECS precursor). Links to [[../../05-Syntheses/Cybernetics, Complexity & Emergent Systems]] — components are an implementation of composable behavior emergence.
- **FSM/State**: ch.7 is the technical counterpart to AI behavior discussed in s026 (ch.11 FSM). Together they cover FSM from both algorithmic and pattern perspectives.
- **Observer/Event Queue**: chs.4+15 implement the feedback mechanisms underlying [[../../wiki/concepts/mechanics/game-loops]] (reinforcing/balancing loops expressed as event flows).
- **Singleton critique**: directly relevant to game engine architecture discussions; warns against the global-state anti-pattern that creates coupling in complex systems.
- **Performance patterns** (ch.17-20): unique coverage in the wiki — the only source covering cache locality, dirty flags, and spatial partitions. Bridges to Hot Potato UE5 performance work.

## Notable quotes

- "The measure of a design is how easily you can change it." (s029, ch.1)
- "If there's a 'most misused pattern' award, Singleton wins it." (s029, ch.6)
- "A game loop runs continuously. Each turn of the loop, it processes user input without blocking, updates the game state, and renders the game." (s029, ch.9)
