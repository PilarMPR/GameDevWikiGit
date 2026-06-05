---
id: s035
title: "Motion, Tweening, and Easing (Ch.7 of Programming Macromedia Flash MX)"
author: Robert Penner
year: 2002
publisher: Osborne/McGraw-Hill
pages: 42
type: book-chapter
---

# s035 — Penner: Motion, Tweening, and Easing

**Author:** Robert Penner · **Source:** Ch.7 of *Programming Macromedia Flash MX*
**Publisher:** Osborne/McGraw-Hill, 2002 · **Pages:** 42 (ch.7 only, PDF pp. 1–42)

## Summary

The canonical reference for programmatic easing functions in games and interactive media. Penner formalizes tweening as a mathematical problem — "a change in position over time" — and derives the complete easing equation taxonomy (linear, quadratic, cubic, quartic, quintic, sinusoidal, exponential, circular), each available as easeIn / easeOut / easeInOut variants. The `(t, b, c, d)` parameter convention he defines here is the standard still used in game engines, CSS, and animation libraries today.

## Key claims and concepts

### Motion defined
- A **motion** = a numerical change in position over time. Three essential components: position, time, beginning position (s035, p.192).
- Position is any numerical scalar — not just physical coordinates. Visual properties (_x, _alpha), sound volume, any continuous value qualifies.
- Position is a function of time: `p = f(t)` — one position per point in time.

### Tweening defined
- A **tween** = interpolation from one position to another with a finite duration. Adds two properties to a generic motion: *duration* and *final position* (s035, p.199).
- Critiques the "standard exponential slide" (`_x += distance / 2` per frame) as insufficient: only ease-out, unbounded duration, no way to query position at an arbitrary time.

### The canonical function signature
```
Math.tweenFunc = function (t, b, c, d) { ... }
```
- `t` = current time (elapsed frames or ms)
- `b` = beginning value
- `c` = change in value (= finish - begin)
- `d` = duration

This `(t, b, c, d)` convention became universal — used in jQuery, GSAP, Unity's AnimationCurve, Godot's Tween, UE4's interpolation nodes.

### Easing taxonomy (complete)
Each type has **easeIn**, **easeOut**, **easeInOut** variants:

| Type | Characteristic | Base equation shape |
|---|---|---|
| Linear | Constant velocity | `c * t/d + b` |
| Quadratic | Gentle acceleration | `c * (t/d)^2 + b` (easeIn) |
| Cubic | Moderate acceleration | `c * (t/d)^3 + b` (easeIn) |
| Quartic | Strong acceleration | `c * (t/d)^4 + b` (easeIn) |
| Quintic | Very strong acceleration | `c * (t/d)^5 + b` (easeIn) |
| Sinusoidal | Smooth S-curve (based on cosine) | `−c/2 * (cos(πt/d)−1) + b` (easeInOut) |
| Exponential | Dramatic start/stop (2^x basis) | sharp power-of-two curves |
| Circular | Geometric arc (√(1−t²) basis) | rounded motion extremes |
| Back | Overshoots then settles | extra `s` overshoot constant |
| Elastic | Spring oscillation on arrival | sinusoidal × decaying exponential |
| Bounce | Bounces on arrival | piecewise quadratic simulation |

### Motion OOP design
Penner builds a `Motion` class (position, time, begin) and a `Tween` class extending it (duration, finish/change, the active easing function). Functions are interchangeable via the shared `(t, b, c, d)` interface.

### Design insight: aesthetics of motion
- Linear tweens "look stiff, artificial, mechanical" — appropriate for robots and machinery, wrong for organic subjects.
- Easing is **perceptually necessary**: humans are extraordinarily sensitive to whether motion follows natural acceleration curves.
- The best easing for UI/game feedback is typically easeOut (fast start, gradual brake) — it communicates responsiveness and agency.

## Connections and cross-links

- **Game feel:** Penner's easing functions are the mathematical foundation of the "polished" feel described in [[../../10-Library/notes/game-feel-juice|game-feel-juice (s018)]] and [[../../wiki/concepts/feel-and-controls/game-feel|game-feel (s007)]]. Juice without good easing is jarring.
- **Animation systems:** Connects to [[../../10-Library/sources/s026-game-programming-algorithms-and-techniques|s026 (Madhav)]] animation chapter and [[../../10-Library/sources/s030-game-programming-in-cpp-madhav|s030 (Madhav)]] skeletal animation — both use interpolation internally.
- **UI feedback:** Directly relevant to [[../../wiki/concepts/feel-and-controls/feedback-systems|feedback-systems]] — the response curve shapes how players perceive responsiveness.
- **Hot Potato:** Any UI transitions, camera snaps, or VFX timing in Hot Potato should use easeOut or easeInOut rather than linear interpolation.

## Notable quote

> "I have often come across animations where the author obviously threw down some keyframes and tweened between them without applying any easing. It drives me nuts." — Penner, p.205

## Provenance note

This is Chapter 7 of a Flash ActionScript book (2002). The language is ActionScript/JavaScript but the mathematics and conventions are language-agnostic. The `(t, b, c, d)` equations are directly translatable to C++, C#, Python, or Blueprint.
