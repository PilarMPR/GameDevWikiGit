# Pacing and Flow

The macro-level architecture of an experience over time — how tension, challenge, and emotional intensity are shaped and sequenced to maintain engagement from beginning to end. Closely related to the [[../player/flow-channel|flow channel]] (moment-to-moment challenge/skill balance) but operating at the larger scale of scenes, levels, and entire games.

---

## Interest curves (s005, ch.14)

Schell's core tool for pacing analysis, originating from his experience as a teenage juggler at an amusement park:

> "The quality of an entertainment experience can be measured by the extent to which its unfolding sequence of events is able to hold a guest's interest." (s005, ch.14)

An **interest curve** plots the level of audience interest (y-axis) against time (x-axis) for any entertainment experience. The same concept applies to a 3-minute song, a 2-hour movie, or a 40-hour game.

### The shape of a successful interest curve

Schell's model of a well-crafted experience:

- **A — initial interest**: the player arrives with baseline expectations set by marketing, word of mouth, first impressions
- **B — the hook**: an early spike that grabs attention and earns the player's investment. "You need to start with more of a bang — to get their attention." In a videogame, often a dramatic opening cinematic, an impactful first action, or a surprising setup. The hook must happen *early* — it earns tolerance for the slower unfolding that follows.
- **C, E — intermediate peaks**: interest rises to local peaks (major reveals, escalating encounters, story beats)
- **D, F — valleys**: interest dips slightly, giving the player a moment to breathe and anticipate the next peak. Valleys are not failures — they are necessary recovery space that makes the peaks feel higher.
- **G — climax**: the maximum peak; the game's defining moment. Everything has been building to this.
- **H — resolution**: satisfying conclusion; interest settles. The ideal: the player leaves with *more* interest than they arrived with — "leave them wanting more." (s005, ch.14)

### The shape of a failed interest curve

The failure mode: the experience opens flat (no hook), has one or two local spikes but no rising arc, crosses the **interest threshold** (the minimum level at which the player stays engaged), and the player quits — often before the experience's best content appears.

> "The interest threshold is the point where the guest has become so disinterested in the experience that he changes the channel, leaves the theater, closes the book, or shuts off the game." (s005, ch.14)

The key insight: many games have good content that never gets experienced because the early pacing fails to sustain interest past the threshold.

---

## Fractal interest curves (s005, ch.14)

The most important structural property of good pacing: **the interest curve pattern repeats at multiple scales**.

- A 60-hour game has an interest curve: hook → rising action → climax → resolution
- Each major chapter has its own interest curve: hook → escalation → chapter climax → interlude
- Each level has its own interest curve: encounter warm-up → intensifying challenge → level boss → reward
- Each individual encounter has its own micro-curve: warning → escalation → crisis → resolution

> "Interest curves will prove to be one of the most useful and versatile tools you can have... interest curves are not linear. Experience is not linear." (s005, ch.14)

This fractal property is what Schell calls "patterns inside patterns." When well-constructed, the structure is self-similar across timescales — zoom in to any part of the experience and you find the same hook-escalation-climax-resolution shape.

**Design implication**: draw interest curves at multiple scales for every major component of the game. If a level's curve is flat, identify which beats are missing. If a session's curve never climbs, add a hook. If a game's climax arrives too early, the long denouement will feel like a failure.

---

## Tense and release: the micro-pacing pattern (s005, ch.9)

Schell's tense-and-release pattern is the frame-by-frame implementation of the interest curve:

1. **Tension rises** — challenge increases, threat approaches, the player is pressed
2. **Peak** — the moment of maximum challenge: the boss attack, the puzzle's final move, the platformer's hardest jump
3. **Release** — the tension resolves: the boss is defeated, the puzzle solved, the reward collected
4. **Brief rest** — a moment of lower intensity before the next tension arc begins

This pattern appears across all scales:
- Within a single combat encounter (building to the enemy's special attack)
- Across a level (encounters of rising intensity leading to the boss)
- Across a game session (building to the session's climax before a natural stopping point)
- Across the whole game (the final boss is the climax of the macro arc)

The valleys (rest moments) are as important as the peaks. Without rest, the player habituates to peak tension and stops perceiving it as intense. Without peaks, there is nothing to rest from. → [[../player/flow-channel]]

---

## Difficulty curves and the flow channel (s006, s005, s016)

Pacing and difficulty are inseparable. A good pacing structure means the difficulty curve tracks the player's growing skill:

### The principle (Adams, s006, ch.13)
- Early content: low difficulty, teaching focus — getting the player to minimum competence
- Mid-game: rising difficulty, skill development — staying in the flow channel as the player grows
- Late-game: high difficulty, skill expression — challenging the player's mastered toolkit
- Endgame/optional content: expert-level challenge — for those who have fully mastered the system

The difficulty curve must be **intentional, not accidental**. Many games have difficulty spikes (sudden impossible sections) or difficulty flatlines (sections with no real challenge). Both are pacing failures.

### Common pacing failure patterns

| Failure | Description | Fix |
|---------|-------------|-----|
| **Spike** | Sudden difficulty jump with no preparation | Scaffold the skills needed; add warning encounter |
| **Flatline** | Long stretch of trivial challenge | Add escalating sub-objectives; introduce complications |
| **Early peak** | Hardest encounter too early | Move challenge to later; reduce early intensity |
| **Late sagging** | Difficulty stops rising before the ending | Maintain the arc; add late-game challenges |
| **Bad finale** | Climax doesn't exceed all previous peaks | The final boss/challenge must feel definitively bigger |

### Koster's boredom analysis (s016)
Koster adds pattern-learning perspective: pacing fails when the player has mastered the game's patterns before the content ends (boredom) or when patterns feel like noise before they're learnable (frustration). The difficulty curve must track the player's pattern-acquisition rate. → [[../theory/theory-of-fun]]

---

## Pacing tools: the level designer's toolkit

### Variable encounter density
Cluster high-intensity encounters (dense combat, rapid puzzles, tight platforming) and separate them with lower-density spaces (exploration, resource collection, narrative). The density variation creates the valleys and peaks of the interest curve.

### Boss encounters as structural anchors
Bosses serve a critical structural function: they are the interest peak at the end of a pacing arc, and they also function as **teaching checkpoints** — a player who cannot defeat the boss has not learned what the preceding levels taught. Boss failure should be diagnosable: which skill is the player missing?

### Checkpoint and save point placement
Checkpoints function as **tension regulators**: placing a checkpoint before a spike gives the player permission to attempt it without fear of losing large amounts of progress. Removing checkpoints (deliberately difficult games like Dark Souls) is a pacing design choice — the player carries the tension across many attempts.

### Rest and reward spaces
After a major challenge, a dedicated reward space (a room with pickups, a story beat, a panoramic view) provides:
- Physiological rest (cognitive load decreases)
- Emotional punctuation (the challenge is over; you succeeded)
- Reinforcement (you are rewarded for completing the arc)
- Interest valley (setting up the next tension arc)

These spaces are not "empty content" — they are essential pacing architecture. (s012, ch.7; s003)

### Opening sequences and tutorials
The first minutes are the most critical pacing zone. The interest curve requires a hook, but early game also requires teaching. The tension between "grab attention immediately" and "teach the player patiently" must be resolved:
- **Delayed competence**: start with a powerful, dramatic moment (player is competent without knowing why), then pull back to teach the mechanics that produced that moment
- **Action tutorial**: teach through doing from the first moment, ensuring the teaching context is exciting
- **In medias res**: begin mid-action; exposition comes through experience

---

## Pacing across multiple sessions

For games played over multiple sessions, pacing must also work at the session level:

- Each session should have its own hook-escalation-climax-resolution arc
- **Session hooks**: something compelling happens within the first 5 minutes to establish engagement
- **Natural stopping points**: the game should offer clear, rewarding stopping points (chapter ends, save points after boss victories) so players can stop without frustration
- **Session cliffhangers**: some sessions should end with unresolved tension that makes the player want to start the next session quickly

F2P games design these arcs explicitly: daily missions, timed events, and login rewards are all pacing mechanisms for session-level engagement. (s017) → [[../business/free-to-play-design]]

---

## The interest curve as design tool (s005, ch.14)

**Draw the curve.** Schell's practical recommendation: before finalizing any section of content, draw its interest curve on paper. Key questions:

- Where is the hook? Does it happen early enough?
- Where are the peaks and valleys? Is there a recognizable rising arc?
- Is there a clear climax that exceeds all previous peaks?
- Is there a satisfying resolution?
- Does the curve cross the interest threshold anywhere?

> "If you don't take a step back and draw an interest curve of your experience, you risk not being able to see the forest for the trees. If you get in the habit of creating interest curves, though, you'll be surprised to find that they help you unlock the secrets of every kind of experience." (s005, ch.14) — Lens #61: The Lens of the Interest Curve

**Questions from Lens #61:**
- If I draw an interest curve of my experience, how is it generally shaped?
- Does it have a hook?
- Is there a clear, exciting climax?
- What changes would give me a better interest curve?
- Is there a fractal structure? Should there be?
- Do my intuitions about the curve match what playtesters actually experience?

---

## Pacing and player types (s005, ch.8)

Different player types have different pacing preferences:

- **Achievers** (Bartle) prefer dense challenge pacing with frequent mastery milestones
- **Explorers** prefer broader valleys with freedom to explore before the next challenge
- **Socializers** prefer pacing that allows for interaction and pause
- **Killers** prefer intense, rapid escalation

A game targeting multiple player types must find a pacing structure that serves all of them, or must allow different pacing tracks (difficulty modes, optional content, multiplayer vs. singleplayer modes). → [[../player/player-types]]

---

## Key concepts & cross-links

- [[../player/flow-channel]] — flow channel = the moment-to-moment constraint that interest curves must stay within
- [[level-design]] — pacing is implemented through level design
- [[spatial-design]] — spatial rhythm of tension and release
- [[../theory/theory-of-fun]] — Koster's learning curve and the boredom threshold
- [[../mechanics/game-balance]] — difficulty curve balance
- [[../player/player-psychology]] — cognitive load, emotional response to tension and release
- [[../narrative/indirect-control]] — music, environment, and character as pacing tools

## Sources

s005 ch.14 (Schell — interest curves: hook, peaks, valleys, climax, resolution; fractal curves; Lens #61) · s005 ch.9 (Schell — tense and release, flow channel, macro structure) · s006 ch.13 (Adams — difficulty curve design, challenge types) · s016 (Koster — boredom as pacing failure; learning rate and difficulty) · s012 ch.3, ch.16 (Kremers — challenge design, pacing, difficulty) · s003 (Hourences — encounter rhythm, singleplayer pacing, difficulty) · s017 (F2P — session-level pacing, daily arcs, retention hooks)
