# Sound, Music & Audio Design

> **What this is:** Everything the canon says about audio as a design discipline — sound as the fastest feedback channel, music as indirect control, diegetic vs. non-diegetic audio, audio timing and calibration, adaptive music, and audio accessibility. Aggregated across s007, s005, s014, s003, s012.

---

## 1. Audio Is the Fastest Channel

**Hodent** (s014, ch.6) identifies audio as the single fastest emotional channel available to designers:

> *"The amygdala responds to threatening sounds before the cortex can reason about them. Audio bypasses visual attention filters. A player who is completely focused on a visual task will still process a critical audio cue."*

This makes audio uniquely powerful and uniquely non-optional:
- A player can look away from a UI element and miss it
- A player can fail to read a tooltip during combat
- A player **cannot** un-hear an audio cue; it registers even in peripheral attention

**Swink** (s007) positions audio as one of the three building blocks of game feel:
> *"Polish — the audio/visual effects that emphasize and sell interactions — is what transforms a mechanically correct game into a satisfying one."*

Sound is not decoration. It is a **primary feedback mechanism** that communicates impact, state, causality, and emotional context.

---

## 2. Audio as Feedback — Five Distinct Functions

### Confirmation Feedback
Sound that confirms an action succeeded: the crisp click when a combo lands, the coin collect chime, the critical hit crunch. These sounds close the **Gulf of Evaluation** (Norman, s015) — they tell the player "that worked."

**Design principles:**
- Arrive within the visual frame of the action (sync to the exact moment of impact, not 100ms after)
- Be distinct and recognizable (the player should learn to interpret these sounds as "success" vs. "near-miss" vs. "failure")
- Scale in intensity with event significance (tap vs. heavy hit vs. kill vs. victory)

### Warning Feedback
Sound that signals incoming danger before it arrives: footsteps from behind, an enemy's alert bark, the windup sound before a special attack, the creak before a structure collapses.

**Tells via audio** (s007): a telegraphed warning sound before a dangerous action is what makes reactive gameplay feel fair rather than arbitrary. The player had the information and could have responded — that's the test of fairness.

### Ambient State Feedback
Sound that continuously communicates ongoing game state without demanding attention:
- A heartbeat that intensifies as health drops (always-on, scales with urgency)
- Environmental audio that changes as the danger level changes (safe zone vs. enemy territory)
- Quiet ambient loop in peaceful areas vs. tense low-frequency drone in danger zones

These sounds work at the **peripheral attention** level — the player doesn't actively listen, but they absorb the information and it shapes their emotional state.

### Spatial / Directional Audio
Sound communicates *location*:
- Footsteps from behind tell the player an enemy is approaching from that direction
- 3D audio positioning lets players triangulate threat position without seeing it
- Directional damage indicators via sound (headphones essential; less reliable on TV speakers)

### Emotional / Narrative Audio
Sound that communicates story, personality, and emotional context:
- A companion's anxious tone tells the player they're in the right place before they see anything
- Musical theme for a boss fight establishes its personality before visual encounter
- Silence (the absence of sound) communicating emptiness, dread, or something wrong

---

## 3. Music as Indirect Control

**Schell** (s005, ch.16) identifies music as one of the six methods of indirect control — and perhaps the most powerful:

> *"Music is possibly the most subtle and powerful of the indirect control methods, because the player is often completely unaware they are being guided by it."*

**How music guides player behavior:**

| Musical quality | Player response |
|---|---|
| Threatening, tense | Heightened alertness; caution; faster decision-making |
| Peaceful, calm | Relaxation; exploration; willingness to stop and look around |
| Urgent, driving beat | Increased pace; feeling of time pressure |
| Resolution chord | Sense of completion; willingness to stop and assess |
| Directionality (music louder from one direction) | Player moves toward source |

**Kremers** (s003) and **Kremers** (s012): level designers use audio to set the emotional tone of a space before the player sees it. Walking into a room with ominous music raises tension before the enemy appears. The player's body is prepared before the challenge begins.

### Adaptive / Dynamic Music

Adaptive music changes in response to game state:

- **Horizontal re-sequencing:** music tracks that can be cut between based on game state (calm → tense → combat → victory, each with its own loop)
- **Vertical re-layering:** additional instrument layers that fade in/out based on intensity (strings play softly in exploration; brass + drums add in combat)
- **Interactive music:** music that responds to player actions (tempo increases with player speed; pitch bends with damage taken)

**Good adaptive music** maintains musical coherence (doesn't feel like jarring cuts) while tracking game state (always emotionally appropriate). Bad adaptive music either changes too abruptly (jarring transitions) or too slowly (still playing combat music in a safe area).

---

## 4. Diegetic vs. Non-Diegetic Audio

| Type | What it is | Examples |
|---|---|---|
| **Diegetic** | Sound that exists in the game world; characters can hear it | Character footsteps, gunfire, dialogue, ambient environment |
| **Non-diegetic** | Sound outside the game world; characters cannot hear it | Soundtrack music, UI click sounds, menu audio |
| **Meta** | Ambiguous; in-universe explanation exists but is loose | Heartbeat as health warning, UI sounds attributed to HUD tech |

**Design tension:**
- Diegetic audio maintains immersion but limits information density
- Non-diegetic audio breaks the fourth wall but communicates clearly and efficiently
- Most games mix both; the balance depends on tone and genre

**Horror games** tend toward heavy diegetic audio — the character hears what the player hears, creating authentic fear. A non-diegetic "you're in danger" jingle would destroy the horror atmosphere.

**Party games** lean non-diegetic — exaggerated cartoon sounds, non-realistic music, UI fanfares all contribute to the playful tone. Perfect diegetic audio would feel tonally wrong.

**The UI sound question:** should menu and HUD clicks be diegetic? Some games (Fortnite, many mobile games) have entirely non-diegetic UI audio that is clearly game-layer sound. Others (Alien: Isolation) give UI sounds diegetic explanations (the tablet your character carries). Both work; the choice should align with the game's overall tone.

---

## 5. Sound Design Principles

### Timing is Everything (s007)

Swink's calibration principle applies directly to sound:

**The sync rule:** sound must arrive at the exact visual frame of the event it confirms. A hit sound arriving 2 frames late feels disconnected; 5 frames late feels laggy. In testing, players consistently describe well-synced audio as making a game "feel better" without knowing why.

**Attack time:** how fast the sound begins from the triggering event. Sharp, fast attack = punchy, impactful. Slow attack = soft, forgiving.

**Pitch variation:** playing the same sound at identical pitch every time creates robotic repetition. Apply slight random pitch shift (95–105% range) to each instance. The player's ear hears variation and the sounds feel organic rather than programmatic.

**Layering:** complex sounds contain multiple frequency layers:
- Sub-bass: the felt physical impact
- Mid: the body of the sound
- High transient: the brightness and immediacy

A hit that only has one layer feels thin. Layering across the frequency spectrum creates sounds that feel physical, present, and real.

### The Silence Design

Silence is a powerful sound design tool — often underused. Silence communicates:
- Empty space (an empty corridor is silent)
- Wrongness (music stops when something terrible is about to happen)
- Transition (a moment of silence before a new musical theme)
- Achievement (the world goes quiet after a major victory — just for a moment)

**Schell** (s005) uses the concept of **interest curves** applied to audio: sustained constant audio habituates the listener; silence followed by sound has far more impact than continuous noise.

### Audio Accessibility

Not all players can hear audio equally. Audio should never be the *only* channel for critical information:
- Directional audio cues should be supplemented with visual indicators (screen edge flash, minimap ping)
- Warning sounds should have visual companions (flashing UI element, screen glow)
- Subtitles for all dialogue
- Audio frequency design that works across different speaker setups (mono compatibility; no critical info exclusively in bass frequencies)

---

## 6. Audio in Level Design (Kremers, s012, ch.11; Hourences, s003)

**Kremers** (s012, ch.11) gives audio a dedicated level-design chapter:

- **Ambient soundscapes** establish the identity of a space before visuals register — the sound of wind, distant machinery, water, crowds all communicate environment type and scale
- **Reactive audio** — environments that respond to player action (footsteps change per surface, doors creak, glass breaks) make the world feel physical and real
- **Spatial audio density** — busy, loud spaces feel populated and alive; quiet, empty spaces feel isolated and potentially dangerous

**Hourences** (s003): audio placement in levels is as important as enemy placement:
- Sounds heard *before seen* create anticipation
- Off-screen sounds create a larger world than what's visible
- Recurring audio themes for specific space types (safe room vs. danger zone vs. secret area) teach the player to read space by ear

**Environmental audio as indirect control:** a sound coming from one direction pulls the player's attention. Players naturally orient toward interesting sounds. A useful item, a NPC who can help, or the path forward can all be signaled via audio without a waypoint marker.

---

## 8. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Audio is the fastest emotional channel — bypasses visual attention | s014 |
| Sound sync to visual frame is critical; late audio feels laggy | s007 |
| Music as indirect control is among the most powerful and most invisible design tools | s005 |
| Diegetic audio maintains immersion; non-diegetic communicates efficiently — balance by genre tone | s012, s003 |
| Silence is a tool; sustained constant audio habituates | s005 |
| Audio must never be the only channel for critical information | s014 |
| Environmental audio establishes space identity before visuals register | s012, s003 |

---

