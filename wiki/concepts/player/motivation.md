# Motivation

Why players play — the psychological drivers that initiate, sustain, and end engagement with a game. Understanding motivation is the foundation of engagement design: you cannot create a game players want to play without understanding what they want from play.

---

## Maslow's hierarchy of needs in games (s005, ch.9)

Schell applies Maslow's hierarchy (physiological → safety → love/belonging → esteem → self-actualization) to game design:

- **Most games operate at esteem** (level 4): achievement, mastery, recognition, status. The satisfaction of getting better at something, earning a reward, and being seen to have accomplished it.
- **Multiplayer games can reach belonging** (level 3): the social connection of playing with others, the belonging of a guild or team. This is why multiplayer games have stronger psychological pull — they satisfy a deeper need.
- **Creative and community games** can reach levels 3–5: being part of a creative community, expressing one's identity, contributing to something shared.

**The promise-and-deliver principle**: "A game must deliver the need it promises. If your game promises belonging but fails to deliver community — the player has no friends who play it, the multiplayer is dead — the disappointment is particularly bitter." (Schell, Lens #19: The Lens of Needs, s005, ch.9)

Design implication: know which level of the hierarchy your game is promising to fulfill, and verify through playtesting that it actually fulfills it.

---

## Intrinsic vs. extrinsic motivation (s014, ch.7)

### Intrinsic motivation
Engaging in an activity because it is inherently rewarding — the activity itself is the reward. The player plays because playing is satisfying.

- Learning and mastery (Koster's fun-as-learning; s016)
- Exploration and curiosity
- Creative expression
- Social connection
- The flow state (Csikszentmihalyi; s005, ch.9)

Intrinsic motivation is durable: players continue until they've gotten everything they want from the experience. It's also fragile: it can be damaged by certain external pressures.

### Extrinsic motivation
Engaging in an activity for an external reward separate from the activity itself — money, points, social recognition, prizes.

- XP, levels, achievements
- Leaderboard rankings
- Real-money rewards
- Social approval

Extrinsic motivation is powerful for **initiating** behavior but produces different engagement patterns than intrinsic motivation. Players motivated extrinsically may stop the moment the reward is removed ("if I'm not earning XP, why am I playing?").

### The undermining effect (overjustification effect) (s014)

Adding **expected, tangible extrinsic rewards** to an intrinsically motivating activity can **decrease intrinsic motivation**.

> When players who loved a game purely for its own sake begin receiving explicit external rewards for playing, their motivation shifts from intrinsic ("I play because it's enjoyable") to extrinsic ("I play to get rewards"). If the rewards are then removed — or if the player feels their play is being controlled by the reward system — intrinsic motivation may not recover.

This is the central ethical design problem of F2P monetization: reward systems that were supposed to enhance engagement may erode the intrinsic enjoyment that makes games worth playing. (s014, ch.7)

> ⚠️ **Design caution**: do not monetize or extrinsically reward activities the player intrinsically enjoys doing. That enjoyment is the core product; rewarding it too directly turns play into work. → [[../../business/monetization]]

---

## Self-Determination Theory (SDT) (s014, ch.7)

Ryan & Deci's SDT identifies three innate psychological needs whose fulfillment enhances intrinsic motivation:

### Competence
Feeling effective and growing in skill. Players need to feel they are getting better and that their skill level is the reason for their success. Games that serve competence:
- Clear skill curve (flow channel)
- Feedback that attributes success to player skill rather than luck
- Difficulty that stays challenging — not too easy, not too hard
- Visible progression of mastery

### Autonomy
Feeling in control and having meaningful choices. Not freedom (infinite unstructured choice) but **meaningful agency** — the player's choices actually matter. Games that serve autonomy:
- Consequential decisions (choices that affect outcomes)
- Multiple valid approaches to challenges
- Customization (of character, playstyle, strategy)
- No artificial restrictions that make the player feel railroaded

### Relatedness
Feeling connected to others — including other players and game characters. Games that serve relatedness:
- Multiplayer and social features
- Characters the player cares about
- Community features and events
- Cooperative goals

> ⭐ **SDT synthesis**: games that satisfy all three — **growing competence** (through the challenge-skill dynamic), **meaningful autonomy** (consequential choices, not scripted paths), and **relatedness** (connection to others or story characters) — produce the strongest intrinsic engagement and longest retention. SDT predicts engagement better than Maslow alone because it focuses on the quality of experience, not just which need is being satisfied. (s014, ch.7)

---

## Reward schedules (s014, ch.7)

How the timing of rewards affects motivation and behavior (Skinner's operant conditioning applied to games):

| Schedule | Pattern | Effect | Game example |
|----------|---------|--------|-------------|
| **Continuous** | Reward every action | Rapid satiation; behavior stops when rewards stop | XP for every button press |
| **Fixed ratio** | Reward after N actions | Steady engagement; pause after each reward | Achievement at 100 kills |
| **Variable ratio** | Reward after unpredictable N actions | Highest, most persistent engagement; resistant to extinction | Loot drops, gacha |
| **Fixed interval** | Reward after time T | Engagement spikes near reward time; low otherwise | Daily login bonus at 24 hours |
| **Variable interval** | Reward after unpredictable time | Moderate persistent engagement | Random world events |

**Variable ratio** produces the strongest engagement — the "slot machine effect." The unpredictability of the reward keeps the player engaged longer than any other schedule. This is why loot drops, gacha pulls, and critical hit chances are so compelling and, when overused, so exploitative. (s014, ch.7) → [[../../business/monetization]]

---

## Koster's fun as motivation (s016)

Koster's theory provides a mechanistic account of intrinsic motivation: fun is the pleasurable signal the brain produces when successfully acquiring a new pattern. The intrinsic motivation to play is the motivation to continue learning.

This makes boredom a motivational signal, not just an emotional state: boredom is the brain reporting that no new patterns are available. The player is not bored because the game is boring — they are bored because the game has stopped teaching them.

Design implication: the game must continuously present new patterns to learn. When the player stops learning, the intrinsic motivation dissolves. → [[../../theory/theory-of-fun]]

---

## Motivation and the flow state (s005, ch.9; s014)

Flow (Csikszentmihalyi) is the motivational sweet spot: challenge matches skill, goals are clear, feedback is immediate. In this state, intrinsic motivation is at maximum — the player does not want to stop.

The conditions for flow are closely related to SDT:
- **Competence**: the challenge is achievable (competence is being exercised)
- **Autonomy**: the player is making the decisions (agency is present)
- The social context varies (flow can occur solo or in groups)

Maintaining the player in the flow state is the practical operationalization of motivation design: keep the challenge/skill balance, keep the feedback loop tight, keep goals clear. → [[flow-channel]]

---

## Motivation and loss aversion (s014)

Kahneman & Tversky's prospect theory: losses are felt approximately twice as strongly as equivalent gains. Players are more motivated to **avoid losing something** than to **gain an equivalent reward**.

Game design applications:
- Permanent death mechanics produce high motivation through loss aversion
- "Save your progress" design — the player is motivated to reach the checkpoint before stopping
- F2P FOMO mechanics ("this offer expires in 24 hours") exploit loss aversion → [[../../business/monetization]]
- Penalty-based difficulty (losing lives, losing progress) produces high motivation in players who can handle it and demotivation in players who cannot

Ethical design uses loss aversion to create meaningful stakes; exploitative design uses it to coerce spending. (s014, ch.7)

---

## Key concepts & cross-links

- [[player-types]] — player-type taxonomies map to different motivational profiles
- [[player-psychology]] — cognitive and emotional foundations of motivation
- [[flow-channel]] — flow as the practical target of engagement design
- [[../../theory/theory-of-fun]] — Koster's mechanistic theory of intrinsic motivation
- [[../../theory/mda-framework]] — 8 aesthetics as the vocabulary of what players are motivated by
- [[../../mechanics/game-loops]] — loops must maintain motivational engagement
- [[../../business/free-to-play-design]] — F2P design built around motivation management
- [[../../business/monetization]] — reward schedules, loss aversion, and the undermining effect

## Sources

s014 ch.7 (Hodent — intrinsic/extrinsic motivation, SDT, undermining effect, reward schedules, loss aversion) · s005 ch.9 (Schell — Maslow's hierarchy, Lens #19 Needs, flow channel) · s016 (Koster — fun as intrinsic motivation; learning-as-reward) · s001 ch.4 (Sellers — engagement and motivation in the interactive loop) · s017 (F2P Handbook — reward design, retention loops)
