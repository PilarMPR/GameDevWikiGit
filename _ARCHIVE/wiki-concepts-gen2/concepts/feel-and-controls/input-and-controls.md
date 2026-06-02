# Input and Controls

The mechanical and temporal relationship between the player's physical actions and the game's response. Input design is the first building block of [[game-feel]]: before simulated space or polish, the player must be able to act in the world in a way that feels responsive, precise, and natural.

---

## Input as tactile contact (s007)

Swink quotes a pivotal framing:

> "The input structure is the player's tactile contact with the game." (s007, citing game developer sources)

The controller or keyboard is not just a neutral transmission device — it is the physical interface through which the player's agency enters the game world. The quality of that contact determines whether the game feels responsive or sluggish, precise or sloppy, empowering or frustrating.

Everything in input design is a relationship between:
- **Input signal** (the player's physical action: button press, analog stick position)
- **Response** (what the game does in response to that input)
- **Timing** (when the response occurs relative to the input)

"When a button gets pressed, is the response gradual or abrupt? Is the response locked to the input position, or does it have its own momentum? These relationships define the expressive potential of the control system." (s007)

---

## The 240ms boundary (s007)

Swink identifies a critical timing threshold for game feel: **240 milliseconds (ms)**.

- **Input must be accepted and output produced within 240ms** for the player to perceive the game as responding to their input in real time
- Beyond 240ms, the causal link between input and response begins to break — the player cannot reliably predict that their action caused the observed effect
- At 240ms+ latency, the game feels "laggy" regardless of other qualities

The 240ms figure is an amalgam of human reaction time (~200ms for visual stimulus → response) and the time required to perceive cause-and-effect. It is the upper boundary for real-time interaction.

Two thresholds:
- **Frame rate**: the game must update visually fast enough that motion appears continuous (≥ 24fps, ideally 60fps for action games)
- **Input latency**: the gap between the physical input and the game's response must be under ~100ms for great feel, under 240ms for acceptable feel

**Why this matters**: many performance-targeting debates in console development (30fps vs. 60fps) trace back to this principle. 60fps (16ms per frame) has substantially better input feel than 30fps (33ms per frame), independent of visual quality.

---

## Input mapping: relationships between input and response (s007)

The designer's core creative act in control design: **mapping input signals to motion/response**. The choices are:

### Directness
- **Direct mapping**: input position directly drives character/camera position. Maximum precision; can feel mechanical.
- **Physics-based mapping**: input applies force; response has momentum, friction, and inertia. More organic; more unpredictable.

### Curve shape
- **Linear**: equal input produces equal response across the full range (15° stick = 15° turn; 45° stick = 45° turn)
- **Exponential/accelerating**: small inputs produce small responses; large inputs produce disproportionately large responses (fine control at low stick positions, fast response at extremes)
- **Deadzones**: a zone around the neutral position that produces no input (prevents unintended stick drift and allows precise neutral holding)

The combination of these curves produces a game's "input feel" — the character that players describe as "tight" (responsive, precise, little momentum) vs. "floaty" (sluggish, high momentum, drifting).

### Button semantics
- **Instantaneous**: button press produces immediate discrete effect (jump, fire, menu confirm)
- **Hold/charge**: holding produces different effect than tapping (charged shot, contextual hold action)
- **Toggle**: button toggles a state on/off (crouch, sprint)

Modal complexity must be managed: when the same button does different things in different contexts, players must track their current mode. Context-dependent button behavior reduces the total input vocabulary required but increases the cognitive cost of remapping expectations across contexts. (s015, Norman — mappings)

---

## Analog vs. digital input (s007; s006)

**Digital input** (buttons, D-pad): on/off. The player either pressed it or didn't. Fast and precise for discrete actions; cannot express gradation.

**Analog input** (thumbsticks, triggers): continuous. The player's input has a value along a range (0–1 for triggers; x,y coordinates for sticks). Enables nuanced control (feathering a brake, leaning around a corner, crouching partially) but requires more careful mapping to translate the continuous range into useful game response.

Analog input's expressive potential comes from the relationship between input range and response range. A character that can walk at 50% speed when the stick is at 50% but sprint at 100% speed at 100% has a meaningful analog spectrum. A character that does the same sprint regardless of analog position wastes the input's potential.

---

## Responsiveness and identity extension (s007)

Swink observes that a key marker of great game feel is **identity extension** — the player stops feeling like they are controlling a character and starts feeling like they *are* the character. The controller becomes transparent; the virtual space becomes real.

> "Players look through the controller in their hands — they see Azeroth, the beach at Normandy or Donut Plains." (s007)

This requires the input response to be responsive enough that the player's intention and the character's action feel synchronous. Any latency, imprecision, or unexpected behavior in the input chain breaks this extension.

Identity extension is the upper target of input design — not just "responsive" but "I am the character."

---

## Control accessibility (s006; s014)

Input design must account for the full range of player physical capabilities:

- **Remappable controls**: players with limited mobility may not be able to use default button layouts. Industry standard is now fully remappable controls.
- **Single-stick/one-handed modes**: some players cannot use both thumbsticks simultaneously. Accessibility-focused games provide alternative input schemes.
- **Toggle vs. hold**: holding a button for an extended action (sprint, crouch, aim) is fatiguing and inaccessible for players with certain motor conditions. Toggle alternatives should be available.
- **Input timing tolerance**: tight timing windows (parry windows, rhythm games) are inaccessible at standard difficulty for many players. Widening windows or providing timing assist modes improves accessibility.

---

## Platform-specific considerations (s006; s007)

| Platform | Primary input | Key considerations |
|----------|-------------|-------------------|
| Console (controller) | Analog sticks + buttons | Thumbstick precision, aim assist, vibration feedback |
| PC (mouse + keyboard) | Mouse (high precision) + keyboard | Mouse sensitivity curves, button layout, no controller auto-rotation |
| Mobile (touch) | Touch screen | Fat finger problem, swipe precision, no physical feedback |
| VR | Motion controllers | 1:1 physical mapping, latency intolerance (motion sickness at >20ms), grip mechanics |

Mouse vs. analog stick for aiming: mouse is dramatically more precise for fast targeting. Most console shooters use **aim assist** (automatic tracking of nearby targets) to compensate. This is not a design failure — it is a deliberate accessibility/feel adjustment for the hardware limitation.

---

## Key concepts & cross-links

- [[game-feel]] — input is the first of three building blocks of game feel
- [[feedback-systems]] — the response half of the input→response relationship
- [[../interface/usability-and-hcd]] — Norman's mappings and constraints apply to input design
- [[../player/player-psychology]] — proprioception, body schema, and kinesthetic identity extension
- [[../interface/ui-design]] — control prompts and button indicators as UI elements

## Sources

s007 (Swink — Game Feel: input as tactile contact, 240ms boundary, identity extension, input-to-response mapping; ch.6 on input metrics) · s015 (Norman — natural mappings, constraints, button semantics) · s006 ch.12 (Adams — platform input types, control design for different audiences) · s014 (Hodent — sensory feedback and motor learning; procedural LTM for controls)
