# Monetization, Retention & F2P

> **What this is:** Everything the canon says about free-to-play design, revenue models, retention mechanics, and the ethics of monetization. Aggregated across s017, s014, s005, s006, s011.

---

## 1. The Core Principle

**The F2P design handbook** (s017) opens with the only principle that matters:

> *"Fun first. Without a compelling core experience, no economy, retention loop, or monetization strategy can survive."*

Every F2P design failure traces back to a failure at this level. A game that is not inherently engaging cannot be made engaging through rewards, FOMO, or payment pressure. The handbook explicitly positions **good game design** — fun mechanics, clear 3Cs, engaging systems, strong onboarding — as the foundation without which nothing else works.

**F2P is not a monetization strategy bolted onto a game. It is a design philosophy that shapes every aspect of the experience**, from moment-to-moment feel through economy to social systems.

---

## 2. Revenue Models (s006; s017)

| Model | How it works | Primary design tension |
|---|---|---|
| **Premium / boxed** | One-time purchase; all content included | Justify price at purchase; no recurring revenue |
| **Subscription** | Monthly/annual fee; access to library or ongoing content | Justify ongoing value; manage churn |
| **Free-to-play (F2P)** | Free base game; revenue from in-app purchases | Monetize without alienating non-payers |
| **Season pass / DLC** | Premium + paid expansions | Balance day-one value vs. DLC value |
| **Battle pass** | Seasonal progression track; cosmetic rewards for play + payment | Make the track feel earnable, not mandatory |
| **Ads** | Revenue from advertising display | Don't break flow; keep ads non-intrusive |

---

## 3. The Four-Stage F2P Arc (s017)

### Stage 1: Core Game Design (the foundation)

Everything else rests on this.

**3Cs:** Character, Camera, Control. The moment-to-moment feel that forms the player's first impression. Must be nailed before any system is built on top.

**Systems:** the game's mechanics, loops, and progression that make it worth playing.

**Onboarding:** the new player experience. In F2P, the retention decision happens in the first session — the player has invested zero money. The free experience must be genuinely good; onboarding failures are catastrophic.

F2P onboarding requirements:
- **Immediate value:** genuinely fun within the first 60 seconds
- **Progressive complexity:** one system at a time; never overload working memory (Hodent, s014)
- **Early win:** an achievable, satisfying win in the first session (competence + autonomy from SDT)
- **Hook investment:** something to come back for before the session ends (visible pending reward, incomplete quest, social prompt)

**Feedback:** clear, immediate response to every player action. The player always knows what they did and what effect it had.

**Accessibility:** the free experience must be genuinely reachable and good without payment.

### Stage 2: Economy Design

How resources flow through the game:
- **Soft currency** (earnable through play) — reinforces the core loop; gives non-payers access to content
- **Hard currency** (purchasable with real money) — the monetization layer; abstract from real money to reduce payment friction

**Two-currency rule:** soft currency keeps non-payers engaged; hard currency creates revenue without making non-payer content feel worthless.

**Price anchoring** (s014, Weber-Fechner): the first price seen becomes the reference point. F2P catalogs are designed with this: a prominent mid-tier bundle makes smaller purchases look cheap and larger ones look reasonable.

**Starting whale psychology** (s014): players who make one small purchase are more likely to make larger ones. The first payment crosses a psychological threshold. Design the first purchase to be low-cost and high-perceived-value.

**Currency sinks:** resources must exit the system (are spent on upgrades, items, cosmetics) to prevent inflation. A game where players accumulate unlimited soft currency eventually produces a situation where nothing feels scarce or valuable.

### Stage 3: Retention Loops

Mechanics designed to bring players back across multiple sessions:

| Loop type | Mechanism | Timescale |
|---|---|---|
| **Daily loop** | Daily missions, login rewards, daily quests | 24 hours |
| **Session hook** | End each session with visible pending reward or unfinished objective | Next session |
| **Social retention** | Friends, guilds, co-op events create mutual accountability | Ongoing |
| **Content cadence** | Regular releases (events, seasons, expansions) | Weeks/months |

**Key principle** (s017): **core loop → system loop → retention loop**. This is the correct build order. Retention mechanics on a bad core loop only deepen the problem.

**F2P loop architecture:**

| Loop | Timescale | Purpose |
|---|---|---|
| **Core** | Seconds–minutes | Immediate, satisfying, repeatable |
| **System** | Sessions, daily | Progression toward goals; character growth |
| **Engagement/retention** | Weeks, seasons | Long-term purpose; reasons to return |

Players who complete a loop and see nothing to do next leave. Visible next milestones are retention mechanics.

### Stage 4: Monetization

How the game generates revenue while maintaining player trust:

**The gold standard** (s017): **gameplay equity + cosmetic monetization** for competitive games.

- **Pay-to-win** — purchasing gameplay advantages. Destroys competitive balance and community trust. Not recoverable without major structural changes once players experience it.
- **Cosmetic monetization** — purchasing visual customization with no gameplay impact. Players self-select: those for whom cosmetics matter pay; those for whom they don't, don't. Neither group is disadvantaged.

For non-competitive games, the pay-to-win vs. cosmetic axis is less critical, but player perception of fairness still matters.

---

## 4. The Ethics of Monetization (s014; s017)

The most important and most contested area. Three mechanisms and their ethical status:

### The undermining effect (s014)

Adding **expected, tangible extrinsic rewards** to an intrinsically motivating activity can **decrease** intrinsic motivation. Players who loved a game for its own sake begin to feel they're working for rewards. If the rewards are then removed — or if the player feels their play is being controlled by the reward system — intrinsic motivation may not recover.

**The design test** (s017): if players would feel fairly treated upon reflection, the design is ethical. If they would feel manipulated, it isn't.

**Ethical application:** design reward systems that *reflect* genuine enjoyment — XP for doing things players would do anyway. Avoid reward systems that make players feel obligated to grind activities they don't enjoy.

### Variable ratio rewards (s014)

Variable ratio reinforcement produces the strongest and most persistent engagement — the "slot machine effect." This is a fact of psychology, not an ethical judgment.

The ethical question: does the activity itself have intrinsic value, or is the variable ratio the *only* reason the player continues?

- **Ethical use:** loot drops from combat that was already fun; critical hits in a satisfying combat system
- **Exploitative use:** loot boxes purchased with real money; gacha pulls as the primary game loop

**Regulatory note:** many jurisdictions are moving toward regulating gacha/loot boxes as gambling. This is not a fringe concern.

### Loss aversion exploitation (s014)

Losses are felt ~2× as strongly as equivalent gains. F2P tactics that exploit this:

- **FOMO timers** ("this offer expires in 24 hours")
- **Temporary content** that players must engage with immediately or lose permanently
- **Permanent de-buff** rather than temporary buff (players pay to remove a disadvantage rather than gain an advantage)

**Ethical line:** using loss aversion to create meaningful stakes in gameplay (permadeath, checkpoint spacing) is legitimate. Using it to coerce spending by creating artificial scarcity is manipulative.

---

## 5. F2P and Player Types

**F2P designs consciously for all four Bartle types** because long-term retention depends on serving the full range of motivations:

| Type | What they need | F2P features that serve them |
|---|---|---|
| **Achievers** | Clear goals; quantifiable progress | Daily missions, battle pass tiers, collection systems, achievement tracking |
| **Explorers** | Content to discover | Seasonal content, story updates, hidden secrets, new champions/maps |
| **Socializers** | Community features | Guild systems, co-op events, friend systems, social sharing |
| **Killers** | Competitive systems with stakes | Ranked modes, leaderboards, competitive seasons, PvP content |

---

## 6. MDA Applied to F2P (s011; s017)

The F2P handbook explicitly cites MDA. The connection:

**Mechanics** (the 3Cs + systems) → **Dynamics** (player behaviors, session patterns, social interactions) → **Aesthetics** (the emotion and experience that make players want to return)

F2P retention is fundamentally an **Aesthetics problem** — players return because of how the game makes them feel (Fellowship, Challenge, Discovery, Expression, Submission). Retention mechanics are Mechanics designed to maintain the Dynamics that produce those Aesthetics.

**Retention loop = MDA in action:**
- Core loop Mechanics → engaging Dynamics → the Challenge/Sensation Aesthetics → intrinsic motivation to return
- Daily mission Mechanics → check-in Dynamics → competence reward Aesthetics → habit loop

The failure mode: retention Mechanics that produce the *wrong* Dynamics. Daily missions that feel like chores → obligation Aesthetics → resentment → churn.

---

## 7. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Core loop fun is prerequisite; retention mechanics can't save a bad game | s017 |
| Cosmetic monetization is sustainable; pay-to-win destroys competitive communities | s017 |
| Variable ratio rewards produce maximum engagement but can exploit habit formation | s014 |
| Undermining effect: extrinsic rewards can erode intrinsic motivation | s014 |
| Loss aversion is legitimate for gameplay stakes; illegitimate for purchase coercion | s014 |
| F2P must serve all player types to sustain long-term retention | s017, s005 |
| Price anchoring is real and must be designed into catalog structure | s014 |
| MDA explains why retention mechanics succeed or fail | s011, s017 |

---

## 8. Hot Potato — F2P/Monetization Notes

Hot Potato targets **Steam premium** (one-time purchase), not F2P. However, F2P lessons still apply:

| F2P principle | Steam premium application |
|---|---|
| Core loop fun first | Same; no UA budget means organic word-of-mouth depends entirely on the game being genuinely fun |
| Onboarding is critical | No refunds after 2 hours on Steam; the first session must justify the purchase |
| Session design | Sessions should end with desire to play again — not frustration or satiation |
| Cosmetic monetization | DLC skins/cosmetics for characters are viable; pay-to-win items would destroy party game balance |
| Retention loops | Seasonal content, cross-platform events, ranked mode could apply post-launch |

**Sources:** s017 (F2P Handbook) · s014 (Hodent) · s005 (Schell) · s006 (Adams) · s011 (MDA)

**See also:** [f2p-design-foundation](../10-Library/notes/f2p-design-foundation.md) · [monetization-models](../10-Library/notes/monetization-models.md) · [player-motivation-maslow](../10-Library/notes/player-motivation-maslow.md) · [self-determination-theory-games](../10-Library/notes/self-determination-theory-games.md) · [Business](../00-Atlas/disciplines/Business.md)
