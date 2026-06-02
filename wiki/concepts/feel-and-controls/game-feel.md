# Game Feel

The tactile, kinesthetic layer of a game — the sensation of control. When done right, the player never notices it; when done wrong, nothing else matters.

---

## Definition (Swink, s007)

> "Game feel is the tactile, kinesthetic sense of manipulating a virtual object. It's the sensation of control in a game." — Swink (s007, ch.1)

Feel is an **invisible art** — like cinematography. Players describe it as "tight," "loose," "floaty," "responsive," "heavy," or "snappy" without being able to say what causes it. It operates in the "space between hand and avatar."

Game feel requires **active perception**: the player controls a virtual object in real time, which is fundamentally different from watching a film or reading. Think of a novice player leaning the joystick, physically pulled into the game's spatial illusion — that physical, proprioceptive pull is game feel (s007).

Swink distinguishes game feel from:
- **Thematic feel** (a "Western feel," a "gothic feel") — atmosphere and art direction
- **Emotional feel** (sadness, fear, excitement) — narrative and context
Game feel is specifically the **kinesthetic control dimension**.

---

## The three building blocks (s007, ch.1)

### 1. Real-time control
A continuous closed loop between player input and game response, happening in the present moment — not like a conversation (turn-taking) but like **driving a car**: the response is perceived in the same moment the input is expressed. Sub-second feedback is essential; above ~150ms, the loop feels broken.

Definition so far: *real-time control of virtual objects.*

### 2. Simulated space
Without a physical environment to move through, there is no spatial reference and therefore no kinesthetic sense. Simulated space provides:
- **Collision detection and response** between the controlled avatar and objects
- **Level design** — the construction and spacing of objects relative to avatar speed

Simulated space must be **actively perceived** (not just watched). A game where the player clicks a unit and it moves independently (RTS) doesn't produce game feel in the same way as a game where the player IS the moving thing.

Complete definition: *real-time control of virtual objects in a simulated space.*

### 3. Polish
Polish is the layer that **emphasizes and sells** the mechanical interactions — making them feel satisfying and juicy. Polish elements include:
- Screen shake (communicates impact weight)
- Particle effects and squash/stretch animation
- Sound effects tightly synced to impact moments
- Hit-stop / freeze frames (brief pause on contact)
- Camera recoil

Without polish, the mechanical loop can be correct but feel flat and weak. Polish is the difference between functional and *satisfying*.

Final definition: *real-time control of virtual objects in a simulated space, with interactions emphasized by polish* (s007).

---

## Six measurable components (s007, ch.4–10)

Swink identifies six components of game feel that can be **measured and tuned**:

| Component | What it is | Key metric |
|-----------|-----------|-----------|
| **Input** | How the player's physical input is read | Polling rate, dead zones, input buffering |
| **Response** | How the game character responds to input | Acceleration, max speed, deceleration curves |
| **Context** | The space and objects the avatar moves through | Collision, level density, obstacle spacing |
| **Polish** | Audio/visual emphasis on interactions | Sound sync offset, screen shake magnitude/duration |
| **Metaphor** | The conceptual model the player uses | "Tank controls," "floaty platformer," "realistic physics" |
| **Rules** | Game rules that constrain movement | Gravity, friction, coyote time, jump forgiveness |

"Floaty" = high max speed with low deceleration + weak polish. "Tight and responsive" = low latency input + fast deceleration + strong hit feedback. These are measurable — a team can converge on them rather than arguing about taste (s007, ch.5).

---

## The 3Cs: Character, Camera, Control (s017)

The F2P design handbook identifies game feel at the product level as the **3Cs** — the three intuitive feel systems that form the player's first impression and must be nailed before any deeper system is built:

- **Character** — how the player's avatar looks, moves, and animates; personality communicated through movement
- **Camera** — how the world is framed and presented; what the player sees and when (see [[camera-design]])
- **Control** — responsiveness, button mapping, input feedback; how input becomes action

"Before anything else, nail the 3Cs. If the character doesn't feel good to move, if the camera is disorienting, or if the controls feel unresponsive, no amount of progression or story will save the game" (s017).

The 3Cs form the **foundation layer** in F2P design: Core Loop → System Design → Engagement/Retention. The 3Cs are the core of the core.

---

## Game feel and perception (s007, ch.2)

Swink grounds game feel in human perception:

- **Proprioception** — the sense of one's own body position and movement. Game feel extends this into the avatar: the player's kinesthetic self-model temporarily *includes* the virtual character. This is why input latency is so disruptive — it breaks the proprioceptive loop.
- **Frame rate threshold** — below ~24 fps, motion appears choppy. Above ~60 fps, further gains provide diminishing returns for most game types, but competitive/fast-response games benefit from 120–240fps for input processing.
- **Response time** — the time between a player action and a perceptible response. Humans can detect delays >60–80ms reliably. "Tight" controls require <100ms end-to-end latency (input to visual response).

---

## Tuning game feel: the process (s007)

1. **Establish baseline metrics** — measure current acceleration, max speed, deceleration, frame rate, input-to-response latency
2. **Tune response curves first** — before adding polish; a responsive base that feels neutral is easier to build on
3. **Add context** — design collision geometry and level density relative to avatar speed
4. **Add polish layer last** — once mechanics feel right, add screen shake, sound sync, particle timing
5. **Validate with players** — ask them to describe feel in their own words; compare against intended vocabulary

Key principle: **never let untuned feel reach the player.** Feel forms a first impression that is very hard to overcome later (s017 supports this: 3Cs first).

---

## Game feel vs. usability

Norman (s015) frames interaction design around **feedback, affordances, and mental models** — the same ingredients as game feel, from a usability lens:
- **Feedback** = game feel's response/polish components
- **Affordances** = visual/audio cues that suggest what the avatar can do and how it responds
- **Mental model** = the player's "metaphor" in Swink's framework

Game feel is the experiential (kinesthetic) face of the same underlying design problem Norman addresses analytically. A game can have perfect Norman-style affordances but still feel "wrong" if the response curves are off (too floaty, too twitchy). Both dimensions matter.

See also: [[../interface/usability-and-hcd]], [[../player/player-psychology]]

---

## Key concepts & cross-links

- [[camera-design]] — the Camera component of the 3Cs
- [[input-and-controls]] — the Control component; input latency, device mapping
- [[feedback-systems]] — visual/audio feedback as polish; affordances
- [[../interface/usability-and-hcd]] — Norman's feedback, affordances, mental models
- [[../player/player-psychology]] — proprioception; how feel builds or breaks immersion
- [[../mechanics/core-mechanics]] — game feel operates on the surface of the mechanics system
- [[../player/flow-channel]] — tight game feel keeps the player in the flow channel; bad feel breaks it

## Sources

s007 (Swink — primary source) · s017 (F2P handbook, 3Cs) · s015 (Norman, affordances/feedback) · s005 ch.13 (Schell, interface) · s006 ch.12 (Adams, camera/interaction models)
