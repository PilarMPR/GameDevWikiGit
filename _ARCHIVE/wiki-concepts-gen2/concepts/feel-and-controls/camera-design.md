# Camera Design

The hypothetical camera is the player's window into the game world. Camera choice shapes spatial literacy, information availability, game feel, and the emotional character of an entire genre.

---

## What is a camera model? (Adams, s006, ch.2 + ch.12)

The **camera model** defines how the game world is presented to the player — the point of view, the behavior of that view over time, and how it responds to player actions and world events. Together with the **interaction model** (how the player controls the avatar), it forms the core of the game's user interface.

Adams distinguishes:
- **Static camera** — fixed perspective; the camera never moves (early arcade games, many 2D games, puzzle games)
- **Dynamic camera** — moves in response to player actions or world events; "makes the player's experience livelier and more cinematic" but requires more design and engineering effort (s006, ch.12)

Camera design is a **layer above** core mechanics — it determines how those mechanics are *perceived*, which profoundly affects difficulty, feel, and strategic depth.

---

## Common camera models (s006, ch.12)

### First-person (FPS perspective)
The camera is placed at the avatar's eye position. The player never sees their own body (except hands/weapons in shooter games). The avatar IS the camera.

**Design implications:**
- Strongest sense of **presence and immersion** — the player literally inhabits the world
- Excellent for **aiming precision** (mouse control of the view = aiming)
- **Spatial disorientation risk** — especially in complex 3D environments; maps and compasses often required
- Avatar personality is mostly communicated through voice, hands, and environment reactions
- Headbob and weapon sway contribute to game feel (s007)

**Genres:** FPS, survival horror, VR experiences, some RPGs (Elder Scrolls, early Doom)

### Third-person
The camera is positioned behind and above (or sometimes to the side of) the avatar, who is visible on screen.

**Design implications:**
- Player can **see their character** — avatar personality, animation quality, and readability matter enormously (s006, ch.12 emphasizes: "You want the player to like and to identify with the protagonist… it's important that she be fun to watch")
- Better **spatial awareness** than first-person — the player can see the space around their character
- **Camera collision** is a major technical/design problem in 3D environments: walls, geometry, and the avatar can occlude or confuse the view
- **Over-the-shoulder variant** (OTS) compromises: slight right-offset gives aiming precision close to FPS while still showing the character

**Genres:** Action-adventure (Zelda, Tomb Raider), platform (Mario 64), TPS shooters (Gears of War)

### Top-down / overhead
Camera looks straight down or at a steep angle. The avatar is seen from above.

**Design implications:**
- Excellent **spatial overview** — ideal for strategy, puzzle, and RPG navigation
- **Minimal game feel** from camera — movement is primarily a spatial/cognitive concern rather than a kinesthetic one
- Isometric variant (45° angle) gives pseudo-3D depth while maintaining readable sprite clarity
- Works well for **emergent/complex games** where understanding the full state of play matters more than immersion

**Genres:** RTSes, isometric RPGs (Diablo), twin-stick shooters, classic Zelda, tactical games

### Side-scrolling
Camera is fixed to a 2D plane; the world scrolls left/right (and sometimes vertically) as the avatar moves.

**Design implications:**
- **Horizontal momentum and trajectory** are the primary spatial dimensions — ideal for platformers where arc of jump and horizontal speed are the core skills
- **Screen space management**: designers carefully tune how much environment is visible ahead of vs. behind the avatar (usually more ahead, to give time to react)
- **Parallax scrolling** (multiple planes moving at different speeds) adds depth cheaply and is a major aesthetic feature of the genre
- Classic challenge: **screen edge** — the avatar should be ahead of center enough to see threats but not so far ahead that the world feels like it's rushing past

**Genres:** Platformers (Mario, Sonic, Hollow Knight), side-scrolling shooters (Gradius), Metroidvanias

### Isometric / 3/4 view
Camera at ~45°, giving a pseudo-3D view. Sprites or 3D models rendered at an angle.

**Design implications:**
- High **readability** for complex tile-based or grid-based games
- "Cheater's 3D" — gives depth cues without the occlusion problems of true 3D
- Movement in diagonals feels natural; cardinal movement can feel rigid
- **Accessibility**: very clear spatial relationships between objects

**Genres:** Classic Diablo, Age of Empires, Baldur's Gate, Final Fantasy Tactics

---

## Static vs. dynamic camera: design decisions

### Static camera
- Every frame is carefully **composed** by the designer (like a theatrical set)
- Used powerfully in horror games (Resident Evil 1) to create tension through **limited visibility** — the player doesn't know what's around the corner
- Can emphasize **specific spatial relationships** important to a puzzle or moment
- Downside: creates jarring transitions; can confuse navigation

### Dynamic camera systems
Once a camera moves dynamically in 3D, a suite of sub-problems must be solved:

**Follow camera:** Stays behind/above the avatar. Key variables:
- **Lag/lerp speed** — how fast the camera follows; slow lag = cinematic, fast = tight and responsive
- **Vertical damping** — how much the camera bobs up/down with the avatar; too much = motion sickness
- **Distance** — how far back; close = more personal + harder to see; far = more strategic + avatar looks small

**Camera collision:** Prevents the camera from clipping through walls.
- Simple sphere-cast approaches pull the camera toward the avatar when colliding
- Poor collision handling is among the most common complaints about 3D action games

**Camera automation / scripted cameras:** Designer-triggered camera movements for dramatic moments
- Rule (Adams, s006): don't seize control away from the player unexpectedly; "players want to feel in charge of the game — at least in regard to control of their avatars"
- Brief scripted moments (cutscenes, environmental reactions) are acceptable; long unsolicited camera movements are frustrating

**Lock-on / target lock:** Many 3D action games add an explicit lock-on system (Z-targeting in Zelda, Dark Souls lock-on). This trades camera freedom for **predictable, reliable enemy-relative orientation** — critical for melee combat where knowing the direction relative to the enemy matters.

---

## Camera and game feel (Swink, s007)

Camera is the **Context** component of game feel: it defines the spatial environment the avatar moves through, and how that movement is *perceived*. The same movement mechanics feel completely different through:

- A wide, high-mounted follow camera (Epic third-person — spacious, power fantasy)
- A tight, low, shake-prone follow camera (survival game — claustrophobic, vulnerable)
- A locked-on tracking camera (action game — focused, controlled, tense)

**Camera shake and recoil** are key polish tools: brief displacement of the camera on impact communicates kinesthetic weight. Over-applied → disorientation and motion sickness. Correctly applied → visceral hit confirmation (s007, ch.9).

**Coyote time** analogy: just as coyote time (forgiving jump window) is a rule mechanic that *feels* like real-time physics, camera smoothing and lag are **perceptual tricks** that make movement feel more cinematic without changing the underlying simulation. These are both examples of feel being constructed at the output layer, not the core mechanic layer.

---

## Camera in 2D: the platformer scrolling problem

In side-scrollers, camera placement affects **difficulty and feel** directly:
- Camera too tight behind avatar → player can't see what's ahead → reaction time is inadequate
- Camera too far forward → back-tracking feels like walking off-screen
- Classic solution: **deadzone** (player can move within a box before the camera follows) combined with **lookahead** bias (camera slightly ahead of travel direction)

Super Mario Bros. uses a fixed left-wall (you can't scroll left) + rightward lookahead — a design that enforces forward momentum and prevents backtracking, shaping the entire game's feel.

---

## Design principle: use genre conventions (Adams, s006)

Camera control conventions are deeply embedded in player **muscle memory and expectations**. Adams: "Over the years, most genres have evolved a practical set of feedback elements and control mechanisms suited to their gameplay… Do not innovate unnecessarily."

If you deviate from genre conventions (e.g., inverted vertical in a genre where uninverted is standard), offer **camera inversion settings** and clear tutorials. Unconventional camera choices require playtesting with both novice and experienced players (s006, ch.12).

---

## Key concepts & cross-links

- [[game-feel]] — camera as the Context component; camera shake as polish
- [[input-and-controls]] — control and camera are coupled; stick controls for camera rotation
- [[../level-design/spatial-design]] — camera choice shapes how spatial design is experienced
- [[../interface/ui-design]] — camera model is part of the UI layer
- [[../player/player-psychology]] — presence, immersion, spatial cognition; motion sickness thresholds

## Sources

s006 ch.2, ch.12 (Adams) · s007 (Swink, game feel) · s017 (F2P, 3Cs) · s003 (Hows & Whys of Level Design) · s005 ch.19 (Schell, game worlds and spaces)
