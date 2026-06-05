# s053 — Guidelines for the Design of Movement-Based Games

**ID:** s053
**Title:** Guidelines for the Design of Movement-Based Games and their relevance to HCI
**Author:** Florian "Floyd" Mueller & Katherine Isbister
**Date:** 2015 (published in ACM; first presented at CHI 2014)
**Type:** Academic journal article (33 pages)
**Language:** English
**Link:** http://movementbasedgames.wordpress.com (companion website with full guidelines)

---

## Summary

An academic HCI paper presenting 10 design guidelines for movement-based games (digital games using gross-motor bodily input), validated through interviews with 14 expert practitioners from commercial studios, indie development, and academia. The guidelines are organized into three thematic clusters. The paper argues these guidelines represent "intermediate-level design knowledge" — generative, actionable, and practitioner-validated — filling a gap between high-level theoretical frameworks and individual case studies. Beyond game design, the authors argue the guidelines have relevance to any embodied HCI application.

---

## The 10 Guidelines (3 clusters)

### Cluster 1: Movement Requires Special Feedback

**1.1 Embrace Ambiguity**
- Movement sensor data is inherently imprecise; no two movements are the same. Fighting this ambiguity frustrates players and exposes sensor limitations.
- Design with ambiguity: players enjoy "surfing uncertainty" in messy systems. Use sensor limits as a design resource.
- Example: Kinect Adventures (raft leaning — imprecision suits the physical metaphor). (s053)
- Do NOT use button proxies during early dev — you miss the opportunities from dealing with ambiguity.

**1.2 Celebrate Movement Articulation**
- In button games feedback is binary (pressed/not). In movement games, the *how* of movement matters and can be pleasurable in itself.
- Provide instantaneous moment-to-moment feedback on movement quality — not judgment, just mirroring — so players can self-correct and grow.
- Example: Dance Central 2 (bright streaks for "flawless" moves); Remote Impact (hit force → score). (s053)

**1.3 Consider Movement's Cognitive Load**
- Movement requires cognitive attention (especially when learning new movements), competing with attention needed for feedback parsing.
- Design rule of thumb: "if your player can usually remember 3 rules, as soon as she/he moves, she/he will only remember 1." (s053)
- Layer feedback so players can selectively engage as mastery grows; avoid overloading novices.
- Learning new movements may require re-learning previously automatized ones.

**1.4 Focus on the Body**
- Many games draw attention to the screen; movement games should focus on the body itself — or at least balance both.
- Use audio and haptics (not just visual feedback); think about what the game is like without a screen.
- For self-conscious players, redirecting attention away from the body can reduce barriers.
- Example: i-dentity (no screen at all); Dance Central (screen as mirror of player performance). (s053)

### Cluster 2: Movement Leads to Bodily Challenges

**2.1 Intend Fatigue**
- Movement results in fatigue. Make fatigue intentional when using it as a challenge; actively avoid it when not.
- Minimize unintended fatigue: short game cycles, movement variety, music distraction.
- Example: Hanging off a Bar (managing fatigue = the game); Wii Party (short cycles to avoid fatigue). (s053)

**2.2 Exploit Risk**
- Indoor movement carries inherent risk (injury, breaking things, hitting people). This risk creates thrill — a positive game element if handled intentionally.
- Put player safety first; make players aware of risk; consider the environment.
- Let player movements interfere with each other (body contact) for social games.
- Example: JS Joust (physical jostling as mechanic); Hit Me! (helmets mitigate injury risk while preserving "in-your-face" feeling). (s053)

**2.3 Map Imaginatively**
- Movement mapping does not need to be literal or true-to-life. Imaginative mapping unlocks fantasy opportunities impossible in reality.
- "Avateering": make the player's movement look better than it really is.
- Map non-linearly (weak forehand → strong hit); add virtual movement to mapped movement.
- Example: Puss in Boots Kinect (wild swings → elegant sword fighting); Wii Tennis (simple arm up-down → successful serve). (s053)
- Exception: do NOT use imaginative mapping if designing an accurate real-world sports simulator.

### Cluster 3: Movement Emphasizes Certain Kinds of Fun

**3.1 Highlight Rhythm**
- Movement has an inherent beat; highlighting it through feedback makes movement easier and more engaging.
- Use music, visual cues of upcoming movements, haptics as rhythm aids, and other players as synchronization references.
- Example: Mary Mack 5000 (synchronized clapping); Dance Central 2 (audio beat). (s053)
- Design competitive opportunities by allowing players to throw each other off-beat.

**3.2 Support Self-Expression**
- Movement is a form of self-expression. Allow multiple movement paths to the same game outcome; celebrate secondary performances (gestural excess).
- Photo/trophy systems for unusual moves extend self-expression beyond the play moment.
- Example: Guitar Hero (guitar lift — no gameplay benefit, pure self-expression); Just Dance 4 (freestyle snapshot moments); JS Joust (open-ended rules for achieving the goal). (s053)

**3.3 Facilitate Social Fun**
- Movement is visible and performative; design for multi-player including audience.
- Start with multi-player mode; make the game easy to learn by observation; turn bystanders into players.
- Example: Yamove! (b-boy dance battle, scored by accelerometer + audience/MC); Musical Embrace (sensor-augmented pillow requires physical embracing — spectacle by design). (s053)

---

## Key claims

- Movement-based games (gross-motor input) are a growing category enabled by Kinect, Wii, PS Move, and mobile sensors (s053).
- There is a persistent gap between HCI academic research and practicing game designers — designers rely on conversations and online resources, not papers (s053).
- The guidelines are not revelatory to experienced designers — they "were following them anyhow" — but are valuable for encapsulating tacit knowledge and transmitting it to less experienced designers (s053).
- "The guidelines are like rules in any creative field: of course you can also break them, but first, you need to know them before you can break them." (s053)
- Guidelines validated by 14 experts: 4 commercial (Dance Central, Just Dance, Singstar, Sports Champions), 4 indie, 6 academic (s053).
- The scope is living-room and exhibit-scale games; location-based movement games are acknowledged as an underserved area (s053).

---

## Methodology note

Multi-step: (1) reflection on authors' own design practice + literature review; (2) website + internal feedback; (3) semi-structured interviews with 14 experts; (4) grounded theory analysis → final guidelines. Format modeled on design patterns (Alexander et al. 1977) but called "guidelines" because no formal inter-guideline relationships are established yet (s053).

---

## Key concepts & cross-links

- "Cognitive load during movement" connects directly to [[../../wiki/concepts/player/player-psychology]] and [[../../10-Library/sources/s014-the-gamers-brain]] (Hodent — cognitive load in game UX).
- "Feedback on movement quality" relates to [[../../wiki/concepts/feel-and-controls/feedback-systems]] and [[../../10-Library/sources/s007-game-feel]] (Swink's 6 components include feedback richness).
- "Ambiguity as resource" links to [[../../wiki/concepts/feel-and-controls/game-feel]] — the feel of imprecise systems can be pleasurable when designed intentionally.
- "Social fun" and audience-aware design connects to [[../../wiki/concepts/player/player-types]] (Bartle's socializers) and LeBlanc's 8 aesthetics fellowship aesthetic (s011).
- "Self-expression" maps to LeBlanc's expression aesthetic (s011) and [[../../wiki/concepts/player/motivation]] (autonomy, SDT).
- "Rhythm" aligns with [[../../10-Library/sources/s032-writing-interactive-music-sweet]] — rhythm as a design element.
- The intermediate-level knowledge concept (Höök & Löwgren 2012) cited here is the same framing used in game design pattern literature; connects to [[../../wiki/concepts/theory/mda-framework]].
- HCI relevance: companion to [[../../10-Library/sources/s015-design-of-everyday-things]] (Norman's HCD) and [[../../10-Library/sources/s038-3d-user-interfaces]] (embodied interaction).
