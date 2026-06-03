# Movement, Controls & Game Feel

> **What this is:** Everything the canon says about how a player's physical input becomes felt experience — from button press to screen shake. Aggregated across s007, s017, s006, s005, s015, s014, s001.

---

## 1. The Core Definition

**Steve Swink** gives the most precise definition (s007):

> *"Game feel is the tactile, kinesthetic sense of manipulating a virtual object. It's real-time control of virtual objects in a simulated space, with interactions emphasized by polish."*

Three building blocks, in order of priority:

1. **Real-time control** — the input/response loop must be continuous and sub-second. Not turn-based, not click-and-wait: the game responds *as* you act, like steering a car. Above ~240ms, players can no longer perceive real-time causality — the game feels "laggy" regardless of all other qualities.
2. **Simulated space** — a physical environment the avatar moves through. Collision, gravity, level geometry. The space provides resistance and affordance; without it, inputs have nothing to push against.
3. **Polish** — audio/visual effects that *sell* and *emphasize* interactions: screen shake, hit-stop, particle effects, sound effects tightly synced to impact frames. Polish transforms a mechanically correct loop into a *satisfying* one.

The **F2P design handbook** (s017) reframes this at the product level as the **3Cs**:

- **Character** — how the avatar looks, moves, animates; personality communicated through motion
- **Camera** — how the world is framed; what the player sees and when
- **Controls** — input responsiveness, button mapping, input→action feedback

> *"Before anything else, nail the 3Cs. If the character doesn't feel good to move, if the camera is disorienting, or if the controls feel unresponsive, no amount of progression or story will save the game."* (s017)

These two frameworks describe the same layer at different granularities. Swink's three building blocks are the engineering model; the 3Cs are the designer's quality checklist.

---

## 2. Input — Physical Contact with the Game

### The 240ms boundary (s007)

Input must produce a perceptible response within **240ms** for the player to experience real-time causality. In practice:

- **Ideal:** <100ms end-to-end (input → visual response)
- **Acceptable:** <240ms
- **"Laggy":** >240ms — the causal link between input and response breaks; the game feels broken regardless of other qualities

Two related thresholds:
- **Frame rate:** below ~24fps, motion appears choppy. 60fps (16ms/frame) is substantially better than 30fps (33ms/frame) for input feel — this is the mechanic behind the "30fps vs 60fps feels different" experience.
- **Input latency:** the gap between physical press and game response. Both must be minimized independently.

### Mapping — the relationship between input and response (s007)

The designer's core creative act in control design: how does a physical signal translate to game action?

**Directness:**
- *Direct mapping:* input position drives output position. Maximum precision; can feel mechanical.
- *Physics-based mapping:* input applies force; avatar has momentum, friction, inertia. More organic; less predictable.

**Curve shape:**
- *Linear:* equal input = equal response across the full range.
- *Exponential/accelerating:* small inputs produce small responses; large inputs produce disproportionately large ones. Fine control at low positions, fast response at extremes.
- *Dead zones:* a neutral zone that produces no input. Prevents unintended stick drift; allows precise neutral holding.

**"Tight" vs "floaty" decoded:**
| Feel | Acceleration | Deceleration | Latency | Polish |
|---|---|---|---|---|
| Tight/responsive | Fast | Fast | Low | Strong hit feedback |
| Floaty/loose | Slow | Slow (high momentum) | Higher | Weak feedback |
| Heavy/weighty | Slow | Medium | Low | Strong impact |
| Snappy | Fast | Fast | Low | Sharp audio/visual |

Both tight and floaty are valid design choices for different games. Mario feels tight; a spaceship sim feels floaty. The error is an *unintentional* mismatch between the intended feel and the actual curves.

### Button semantics

- **Instantaneous:** press → immediate discrete effect (jump, shoot, confirm)
- **Hold/charge:** holding produces a different or amplified effect (charged shot, sprint)
- **Toggle:** press switches a persistent state (crouch, aim mode)
- **Contextual:** same button, different action depending on game state (interact/pick up/vault)

Contextual mapping reduces button count but introduces *mode confusion* — the player must know which mode they're in (s005, Lens #60 Modes). Good contextual design makes the active context obvious from the world state, not from a UI indicator.

### Norman's mapping principle (s015)

Don Norman's principle of **natural mappings**: the relationship between control and effect should exploit spatial metaphor — joystick left → character moves left; scroll up → view moves up. Mappings that violate spatial intuition (inverted Y-axis) require the player to override instinct and build new reflexes. They can work, but they carry a learning cost.

---

## 3. Movement Physics — How Avatars Move

### The physics of feel (s007)

Movement feel is defined by six measurable parameters:

| Parameter | What it controls | Tuning for "tight" | Tuning for "floaty" |
|---|---|---|---|
| **Max speed** | Peak velocity | Lower (more control) | Higher (more momentum) |
| **Acceleration** | Time to reach max speed | Fast | Slow |
| **Deceleration** | Time to stop after input released | Fast | Slow (drift) |
| **Turning radius** | How fast direction changes | Tight | Wide |
| **Air control** | Input influence while airborne | Full (Mario) | Minimal (realistic) |
| **Gravity** | Fall speed and arc feel | Fast fall = responsive | Slow fall = floaty |

These are all *measurable* — a team can converge on a feel target by defining it numerically, not just verbally. "Floaty" stops being a subjective complaint and becomes "reduce deceleration from 800 to 400, increase gravity from 9.8 to 14."

### Jump design

Jump feel deserves special attention because it's the most playtested mechanic in games:

- **Jump height/arc:** determined by initial velocity + gravity. Both can be independently tuned. Higher initial velocity + stronger gravity = snappier jump with good height. Lower initial velocity + weak gravity = floaty.
- **Coyote time:** the player can jump for a brief window (4–8 frames) after walking off a ledge. Removes pixel-perfect timing requirements; makes the player feel skilled without being cheated.
- **Jump buffering:** if the player presses jump just before landing, the jump fires the moment they touch ground. Removes the "I pressed it but it didn't register" frustration.
- **Variable jump height:** holding jump = higher arc; tapping = lower arc. Provides expressive control and tactical range. Used in almost all precision platformers.
- **Air control:** full air control (Mario) vs. committed trajectory (early Sonic) completely changes the character of a platformer. Full control is more forgiving; committed trajectory creates more skillful risk/reward.

### Collision and spatial resistance (s007)

The simulated space must provide meaningful collision — the avatar must push against the world, not pass through it. Key considerations:

- **Hitbox shape:** actual collision shape vs. visual representation. Smaller hitboxes than the visual (generous) = player feels skilled; larger (punishing) = frustrating. Most games go generous, especially for jumps.
- **Step height:** how tall an obstacle the avatar automatically climbs vs. must jump over. Invisible step heights remove micro-frustrations from terrain.
- **Ledge grabbing:** auto-grab vs. manual grab. Auto-grab is forgiving; manual grab is skill-expressive.

---

## 4. Camera Design — the Player's Window

**Ernest Adams** (s006, ch.12) provides the canonical camera taxonomy:

### First-person (FPS)

Camera at the avatar's eye. The avatar IS the camera.

**Strengths:**
- Strongest **presence and immersion** — the player inhabits the world
- Excellent for **aiming precision** (look direction = aim direction)
- Fastest read of immediate spatial environment

**Weaknesses:**
- **Spatial disorientation** risk in complex 3D spaces
- Avatar personality limited to voice, hands, weapon animations
- Headbob and weapon sway must be designed carefully — they add feel but cause motion sickness if excessive

**HP relevance:** Not the right camera for Hot Potato — kills social readability (can't see other players) and the parkour/tag reads as second-person chaos.

### Third-person (behind/above)

Camera behind and above the avatar, who is visible on screen.

**Strengths:**
- Player sees their character — avatar animations, personality, readability
- Better **spatial awareness** than first-person
- Avatar visibility creates stronger character identity

**Weaknesses:**
- **Camera collision** is a major engineering/design problem — walls and geometry can occlude or confuse the view
- **Over-the-shoulder (OTS)** variant: slight right-offset gives near-FPS aiming precision while showing the character

**HP relevance:** This is Hot Potato's camera. Character readability, third-person parkour, visible player differentiation (colors/silhouettes) all require it.

### Top-down / overhead

Camera looks straight down or at a steep angle.

**Strengths:**
- Excellent **spatial overview** — see the whole arena
- Ideal for strategy, puzzle, and tactical games
- Works for **emergent/complex games** where state readability matters

**Weaknesses:**
- Minimal kinesthetic feel from camera movement
- Loss of vertical dimension reduces parkour expressiveness

### Side-scrolling (2D platformer)

Camera fixed to a 2D plane.

**Strengths:**
- Jump arc and horizontal momentum are fully readable — ideal for precision platformers
- Clean separation of foreground/background

### Static / fixed

Camera doesn't move or moves only along a rail.

**Strengths:**
- Maximum compositional control per shot
- Used in horror (removes player sense of spatial safety) and some puzzle games
- No camera collision problems

---

### Camera behavior (all perspectives)

Beyond position, camera *behavior* is the second dimension of camera design:

**Follow camera:** tracks the player with lag. The amount of lag is a feel dial — too much lag = disorienting; too little = jerky. Lerp interpolation smooths it. Dead zones (the camera doesn't move until the player reaches the edge of the dead zone) give the player more visual "breathing room."

**Camera shake:** communicates impact weight. Too much = nauseating; too little = flat. Usually implemented as noise on camera position/rotation decaying over time. Swink (s007) includes camera shake as a core *polish* element.

**Look-ahead:** camera peeks in the direction the player is moving, showing them more of what's ahead. Critical for fast movement games where the player needs reaction time.

**Camera rotation:** whether the player can freely rotate the camera (full 3rd-person) or whether it auto-rotates (locks to movement direction, or orbits enemies). Full control = more expressive; auto-rotate = more accessible.

**Camera distance:** closer = more intimate + stronger game feel; farther = more overview + better spatial planning. Zoom can be dynamically adjusted — pull out in open areas, push in during tight spaces.

**For Hot Potato specifically:**
- Camera must accommodate 2–8 players in a shared space. Dynamic zoom-out when players spread, zoom-in when clustered. Reference: *Towerfall*, *Brawlhalla*, all couch brawlers.
- Split-screen vs. single shared view. Hot Potato couch play = shared view with zoom. Steam online = per-player camera.

---

## 5. Polish Layer — Juice

**"Juice"** (Schell's Lens #58, s005) is the layer of audio/visual feedback that makes interactions feel *satisfying*. It's the difference between "functionally correct" and "great."

### Screen shake

Communicates **impact weight**. Parameters:
- **Magnitude:** how far the camera displaces. Scaled to event significance.
- **Duration:** how long the shake lasts. Too long = nauseating.
- **Decay:** how the shake diminishes (linear, exponential, or spring-return).
- **Directional:** trauma-style shake (random) vs. directional (hit from left = shake left).

Screen shake should be trauma-accumulative — multiple hits stack, not reset.

### Hit-stop (freeze frame)

A 2–8 frame pause on impact — the game "holds" for a fraction of a second at the moment of contact. Used in fighting games, action games, and any game where impacts need to feel weighty. The brain reads the brief pause as "something significant happened." Duration: 2–4 frames for light hits, 6–12 for heavy.

### Squash and stretch

Avatars and objects compress on impact, stretch on acceleration. Communicates physics and personality. More cartoon = more squash/stretch (Mario, Cuphead). More realistic = subtler (Uncharted, Celeste).

### Sound feedback timing

**The most critical polish element.** Sound synchronized to the exact visual frame of an impact makes the whole interaction feel real. Sound arriving even 1–2 frames late feels disconnected. Parameters:
- Attack time (how fast the sound starts)
- Pitch variation (slight random pitch shift prevents repetitive audio — same sound at 95–105% pitch sounds different each time)
- Layering (impact has sub-bass + mid + high transient for full-spectrum weight)

### Particle effects

Visual confirmation of physical events. Hit particles, movement dust, footstep effects. Key principle: particles should be **additive** (add brightness to the scene) and **brief** (gone in < 0.3s for most actions) to avoid visual clutter.

### Haptic feedback (controller vibration)

Activates the player's proprioceptive system — the body participates in the fiction. Swink (s007) notes that haptics extend kinesthetic self-model into the avatar. Parameters: rumble motor intensity, duration, decay. PlayStation DualSense adds **trigger resistance** (draw a bowstring, engage a chainsaw). For Hot Potato: light rumble on potato receipt, heavy on tag.

---

## 6. Proprioception — The Psychology of Control

**Swink** (s007) grounds game feel in **proprioception** — the sense of one's own body position and movement. When game feel works, the player's kinesthetic self-model temporarily extends *into the avatar*. The player doesn't just control the character; they *become* it.

This explains:
- Why input latency breaks feel so severely — it disrupts the proprioceptive loop
- Why camera shake works — it simulates the physical sensation of impact in the player's body
- Why controller rumble adds feel even when players "know" it's fake
- Why deaths feel personal — the player's extended body was "killed"

**Hodent** (s014) connects this to the brain's **body schema** — the neural map of the body's position in space. Games hijack this map; good feel design maintains the illusion that the avatar *is* the player's body.

**Norman** (s015) describes the same phenomenon from a HCD angle: **affordances** and **conceptual models**. The player forms a mental model of how the avatar moves. When the avatar behaves consistently with that model, control feels natural; when it doesn't, control feels "wrong." This is why changing physics parameters mid-game feels jarring even when the new values are technically better — the player's model has to re-form.

---

## 7. Usability at the Control Layer

Norman's six principles applied to control design (s015):

| Principle | Control design application |
|---|---|
| **Affordances** | Button prompt appearing near interactive objects |
| **Signifiers** | Visual indicator of available jump platform, grabbable ledge, interactable NPC |
| **Constraints** | Movement speed cap; collision prevents passing through walls |
| **Mappings** | Natural stick-to-movement direction; consistent button assignments across all menus |
| **Feedback** | Immediate visual + audio response to every input |
| **Conceptual model** | Physics behave predictably; camera rotation is reversible; landing always feels like landing |

**The Gulf of Execution** (s015): the gap between wanting to do something and knowing how to do it. In movement design this manifests as: "I wanted to vault but the game made me jump" — the player couldn't express their intent because the control vocabulary was unclear.

**Hodent's cognitive load principle** (s014): complex control schemes overload working memory. When the player is simultaneously learning movement AND fighting enemies AND reading the UI, the brain reaches capacity. Good control design makes movement *automatic* (procedural long-term memory) as fast as possible — so the player stops thinking about controls and starts thinking about play.

---

## 8. Designing & Tuning Feel

### Swink's tuning process (s007)

1. **Establish baseline metrics** — measure current acceleration, max speed, deceleration, latency
2. **Tune response curves first** — before adding polish; a responsive base is easier to build on
3. **Add context** — design collision geometry and level density relative to avatar speed
4. **Add polish last** — once mechanics feel right, add screen shake, sound sync, particle timing
5. **Validate with players** — ask them to describe feel in their own words; compare against intended vocabulary

**Never let untuned feel reach players.** Feel forms a first impression that is very hard to overcome (s017 supports: 3Cs must be nailed before anything else is built).

### The vocabulary method

Define the target feel in concrete adjectives *before* tuning:
- *"Weighty, grounded, deliberate"* → slow acceleration, strong gravity, strong hit-stop
- *"Slippery, frantic, chaotic"* → low friction, fast acceleration, minimal deceleration
- *"Nimble, precise, clean"* → fast acceleration/deceleration, no drift, low latency

Then tune until the numbers produce those adjectives from blind playtesters.

### Doubling and halving (s005, ch.11)

When tuning feel parameters, don't adjust in small increments. **Double or halve** to find the useful range quickly, then refine. Changing gravity from 9.8 to 9.6 reveals nothing; changing it to 19.6 reveals how far you can push the parameter space.

---

## 9. Cross-Source Synthesis — What Everyone Agrees On

| Claim | Sources |
|---|---|
| Input latency below ~240ms is required for real-time feel | s007 |
| Feedback must be immediate, proportional, and multi-channel | s007, s015, s014 |
| Players extend their self-model into the avatar | s007, s014 |
| 3Cs must be solved before layering other systems | s017 |
| Tune base physics before adding polish | s007 |
| Natural mappings (spatial metaphors) reduce learning cost | s015 |
| Game feel is measurable, not just a "vibe" | s007 |
| Camera must serve readability before aesthetics | s006 |

**The convergence:** Swink's engineering model (s007), Norman's usability model (s015), Hodent's cognitive model (s014), and the F2P product model (s017) all arrive at the same design truth: **the player must be able to express their intent precisely and receive immediate, clear feedback that their action worked**. Every model describes a different layer of the same requirement.

---

## 10. Hot Potato — Design Implications

| Decision | Rationale from canon |
|---|---|
| Third-person camera | Avatar visibility required for social play; identity through animation (s006) |
| Dynamic zoom out | Party game observable play requirement — all players visible (s005, multiplayer-conflict-types) |
| Target <16ms local latency | 60fps tick rate; 240ms boundary requires sub-100ms ideally (s007) |
| Rollback netcode for online | Physics replication is expensive; server-authoritative potato position (s007) |
| Exaggerated squash/stretch | Party game aesthetic = cartoon physics = strong visual feedback (s007) |
| Heavy screen shake on tag | Tag is the core impact event — deserves the strongest feedback signal (s007, Lens #58) |
| Controller haptic on potato receipt | Proprioceptive signal that you're now the chaser (s007) |
| Big, readable player silhouettes | Observable play from 2m away on a TV (party-game-design-patterns) |
| Coyote time + jump buffering | Parkour should feel skilled, not pixel-perfect; generous collision (s007) |

**Sources:** s007 (Swink) · s017 (F2P handbook) · s006 (Adams) · s005 (Schell) · s015 (Norman) · s014 (Hodent) · s001 (Sellers)

**See also:** [game-feel-definition](../10-Library/notes/game-feel-definition.md) · [input-controls-design](../10-Library/notes/input-controls-design.md) · [camera-design-models](../10-Library/notes/camera-design-models.md) · [feedback-system-design](../10-Library/notes/feedback-system-design.md) · [norman-hcd-vocabulary](../10-Library/notes/norman-hcd-vocabulary.md) · [Feel & Controls](../00-Atlas/disciplines/Feel%20%26%20Controls.md)
