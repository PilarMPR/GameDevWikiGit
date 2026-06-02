# Feedback Systems

Every way a game communicates to the player what is happening in the game world — what their actions caused, what the current state is, and what is about to happen. Feedback is the second half of the input/response loop and the foundation of [[../theory/meaningful-play|meaningful play]]: without discernible feedback, the player cannot know their actions mattered.

---

## Why feedback is foundational (s015, s014, s011)

Norman's principle (s015): **every action must produce a perceivable response**. Without feedback:
- The player cannot form a mental model of the system (they have no information to build from)
- The gulf of evaluation cannot be crossed (the player acts but doesn't know what happened)
- Meaningful play is impossible — outcomes are not discernible

MDA's dynamics layer is entirely produced by feedback: the player observes the consequences of their mechanics, updates their strategy, and acts again. Cut the feedback and the dynamic loop breaks. (s011)

Hodent (s014): **feedback is how the brain builds the game's conceptual model**. Each feedback event updates the player's beliefs about the system. Consistent, accurate feedback produces an accurate mental model; inconsistent or absent feedback produces confusion and the feeling of unfairness.

---

## The five channels of game feedback (s007; s014; s015)

### 1. Visual feedback
The primary and most dense feedback channel. Encompasses:

**Immediate consequence feedback**: what happened right now?
- Damage numbers floating off enemies
- Hit effects (particle systems, flashes, screen shake)
- Enemy health bars depleting
- Destruction animations when objects break
- Player character hit reactions (stagger, stun animation)

**State feedback**: what is the current state?
- Health bar showing current health
- Resource meters (mana, fuel, ammo)
- Status effect icons (poisoned, buffed, chilled)
- Cooldown timers showing when abilities return

**Anticipatory feedback (tells)**: what is about to happen?
- Enemy windup animations before attacks
- Warning indicators (red circles on ground before AoE)
- Charge-up effects before a special ability fires
- Door indicators before an ambush

**Spatial feedback**: where is relevant information?
- Directional damage indicators (screen edge tint showing attack origin)
- Quest markers and waypoints
- Minimap pings
- Enemy awareness icons (stealth games)

### 2. Audio feedback
Sound is the fastest emotional channel and the most pervasive feedback system:

**Confirmation feedback**: audio that confirms an action landed correctly. A crisp click when a combo connects. The distinctive sound of a critical hit. The cash register sound of a coin collected.

**Warning feedback**: audio that signals incoming danger. Footsteps behind the player. An enemy's alert bark. The click before a mine detonates.

**Ambient state feedback**: sounds that communicate ongoing state without demanding attention. A heartbeat intensifying as health drops. Environmental audio that changes when an area's danger level changes.

The power of audio: the player doesn't need to look at an element for audio feedback to work. During intense combat, visual attention is at maximum; a distinctive audio cue can communicate what visual UI might miss. Dual-channel feedback (visual + audio for the same event) greatly increases reliability. (s014)

### 3. Haptic feedback
Physical sensations from the controller:
- **Rumble motors**: general vibration for impacts, explosions, engine rumble
- **Haptic triggers** (PlayStation 5 DualSense): variable resistance in triggers that can simulate drawing a bowstring, engaging a chainsaw, or landing on different terrain
- **Directional haptics**: conveying direction of impacts or events through the physical sensation

Haptic feedback bypasses visual and audio processing and directly activates the body's proprioceptive system — it contributes to kinesthetic identity extension (Swink, s007). When the controller rumbles with a character's heartbeat, the player's body participates in the fiction. (s007)

### 4. Diegetic feedback (in-world)
Feedback delivered through the game world itself rather than UI overlays:
- **Character vocalization**: the player character grunts, cries out, or comments on their situation
- **World reactions**: NPCs flee when the player character draws a weapon; animals scatter at loud noises
- **Environmental responses**: foliage bends where the player walks; glass cracks progressively as it takes damage
- **NPC dialogue**: companions comment on the player's health, resources, or situation

Diegetic feedback maintains immersion by keeping information inside the magic circle. Its limitation: it competes with narrative audio and can be missed during fast-paced sequences.

### 5. Narrative / social feedback
Feedback that operates at the story level:
- **Character arc responses**: a companion's attitude toward the player shifts based on decisions made
- **World state changes**: NPCs remember the player's actions; a town's mood changes after an event
- **Leaderboard and social feedback**: the player's performance contextualized relative to others

---

## Feedback design principles (s015, s014)

### Immediacy
Feedback must occur within the human perception window for cause-and-effect association (~500ms). Feedback that arrives more than 1–2 seconds after an action loses its causal link. The player may not associate the feedback with the action that produced it.

### Informativeness
Feedback should communicate *what* happened, not just *that* something happened. A generic "damage taken" flash is less informative than a flash accompanied by a damage number. The player should know not just that something changed, but why.

### Proportionality
Feedback intensity should be proportional to event significance. A critical hit should produce a more intense feedback response than a normal hit. Boss deaths should produce the most dramatic feedback in the game. If all events produce similar feedback intensity, signal is lost in noise.

### Consistency
Similar events should produce similar feedback. If damage always triggers a red flash, the player learns that red flash = damage. Inconsistency breaks the conceptual model.

### Accessibility of feedback
Feedback that relies on a single channel excludes players with relevant disabilities:
- Color-blind players may miss red/green distinction
- Deaf or hard-of-hearing players miss audio-only feedback
- Players with motor conditions may miss rapid feedback windows

Design for multi-channel redundancy: critical events should have both visual and audio feedback at minimum.

---

## Tells: predictive feedback (s007; s005)

A **tell** is feedback that signals an upcoming event *before* it occurs — giving the player time to respond. Tells are the mechanism that makes reactive gameplay feel fair rather than arbitrary.

Without tells: the enemy deals damage with no warning → the player feels cheated (the system was unfair).
With tells: the enemy raises their arm and glows red before striking → the player had the chance to dodge. The tell is what makes the same damage feel skillfully avoidable rather than random.

**Tell design**:
- The tell must be perceptible (clear enough to see/hear in the game's visual noise)
- The tell must precede the event by enough time for the player to respond (typically 200–600ms depending on game pace)
- The tell should be consistent — the same enemy always telegraphs in the same way
- Tell reading is a learnable skill: early encounters should have obvious tells; advanced encounters can use subtler ones

Tells are the bridge between challenge and fairness: the game is hard, but fair, because the player always had the information they needed.

---

## Feedback calibration (s007)

Swink discusses feedback as one of the six measurable components of game feel. Calibrating feedback involves:

- **Temporal tuning**: when does the feedback begin and end relative to the action? Immediate vs. delayed, sharp vs. extended.
- **Intensity curves**: does the feedback ramp up, sustain, or decay? A hit effect that ramps up briefly before fading feels different from one that instantly appears at full intensity.
- **Feedback stacking**: when multiple events occur simultaneously (multi-hit combo, explosion + damage + pickup), feedback events must not overlap into indistinguishable noise.

The "juice" of game feel is largely in feedback calibration: tiny adjustments to when a sound plays, how long a particle effect lasts, and how a controller vibration is timed produce massive differences in how satisfying an action feels. (s007)

---

## Key concepts & cross-links

- [[game-feel]] — feedback is the third building block of game feel (alongside real-time control and simulated space)
- [[input-and-controls]] — the input half of the input→feedback loop
- [[../interface/usability-and-hcd]] — Norman's feedback principle; gulfs of evaluation
- [[../interface/ui-design]] — UI elements as feedback delivery mechanisms
- [[../player/player-psychology]] — perception, attention, and emotional response to feedback
- [[../theory/meaningful-play]] — discernability requires feedback; integration requires consequential feedback
- [[../mechanics/game-loops]] — feedback is what makes loops feel like loops (action → consequence → next action)

## Sources

s007 (Swink — feedback as component of game feel; tells; calibration; haptic feedback; identity extension) · s015 (Norman — feedback as design principle; gulf of evaluation) · s014 (Hodent — multi-channel feedback; attention and perception; audio as fastest emotional channel) · s011 (MDA — dynamics require feedback to function) · s005 ch.10 (Schell — actions and their consequences as feedback mechanisms; Lens #23–24)
