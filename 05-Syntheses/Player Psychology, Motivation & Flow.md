# Player Psychology, Motivation & Flow

> **What this is:** Everything the canon says about how players think, feel, and stay engaged — perception, memory, attention, motivation, the flow channel, and player types. Aggregated across s014, s005, s016, s001, s015, s009, s006.

---

## 1. The Brain as a Design Constraint

**Celia Hodent** (s014) opens with the argument that makes this entire topic practical:

> *"The brain is biased, emotional, irrational, and yet extremely complex. Designers must understand how players actually perceive, attend, remember, learn, and feel — and guard against their own biases — to build engaging, usable games."*

The brain is not a neutral receiver. It actively constructs its experience, filters inputs according to goals and expectations, and has hard capacity limits. Every design decision either works *with* these constraints or fights against them — and fighting the brain always loses.

---

## 2. Perception

### How the brain processes visual input (s014, ch.4)

**Bottom-up processing:** sensory input → interpretation. The raw signal.
**Top-down processing:** expectations and prior experience shape what is perceived. Players see what they expect to see — which is why tutorial elements placed inconsistently with the game's visual language get missed.

### Visual acuity and foveal focus (s014)

The eye has highest resolution only at the **fovea** — the center of the visual field. Peripheral vision is blurry and motion-sensitive. Practical rules:
- Critical information (health, ammo, active objective) must be placed where the player's gaze is likely to be
- Peripheral signals (screen edge glow, vignetting, sound) are more reliable for off-center alerts than peripheral UI
- **Don't bury critical info in corners** if the player's gaze is locked to center

### Gestalt principles (s014)

The brain automatically groups visual elements by **proximity, similarity, and continuity**. UI and level design that uses these principles is read faster and more accurately:
- Items that should be read together → place near each other (proximity)
- Dangers that should be distinguished → make them visually distinct (similarity)
- A path the player should follow → visual elements form a continuous line (continuity)

### The Weber–Fechner bias (s014; s006)

Perceived change follows a logarithmic curve. A +10 damage upgrade feels huge at level 1 but negligible at level 50. Progression systems must scale *faster than linearly* to maintain felt impact. This is why XP curves are exponential and why "big number go up" requires increasing numbers just to maintain the same perceived reward.

### Affordances and signifiers (s015)

**Norman's** fundamental distinction:
- **Affordance:** a relationship that enables action (ledge at avatar-height *affords* climbing)
- **Signifier:** a perceptible signal that communicates the affordance (glowing edge, character looking at ledge)

Affordances exist whether or not they're perceivable. Unperceivable affordances don't help players. A wall with a hidden door affords exit — but the player will never find it without a signifier. Good level design makes affordances perceivable; good character design makes capabilities self-evident.

### Mental model alignment (s014; s015)

The most critical perceptual principle for game design:

> *"Aligning developer intentions with players' mental models is crucial."* (s014)

When a player's model of how a mechanic works is wrong, they behave incorrectly until the model is corrected. The correction pathway is: visual feedback → player action → new feedback → model update. If the feedback is absent, unclear, or delayed, the model never corrects. This is the root cause of "the game feels unfair" — the player's model predicts X; the game produces Y; the player concludes the game is broken.

---

## 3. Memory

### The multistore model (s014, ch.5)

| Store | Capacity | Duration | Game design relevance |
|---|---|---|---|
| **Sensory** | Large | <1 second | Pre-attentive detection; change blindness |
| **Short-term (STM)** | ~7 items | <1 minute | Tutorial info on first exposure — strictly limited |
| **Working memory** | ~3–4 items | Active | Simultaneous demands during play; cognitive load |
| **Long-term (LTM)** | Unlimited | Indefinite | Learned mechanics; implicit/procedural skills |

The transition from working memory to long-term memory is what mastery feels like. When controls move from procedural LTM, the player stops thinking about *how to act* and starts thinking about *what to do* — this is the cognitive substrate of the flow state.

### Procedural (implicit) LTM (s014; s016)

How players internalize controls: after enough practice, button presses become automatic. **Koster** calls this *grokking* — complete internalization where the pattern becomes part of you. Procedural memory is encoded through *doing*, not through reading or watching. This is why:
- Tutorials that explain instead of letting the player act fail
- Players forget mechanics they've only been told about (forgetting curve)
- Mastery feels natural, not effortful — the action has been offloaded to LTM

### Cognitive load (s014; Sweller)

Every task requires attentional resources. Complex games overload working memory if too many demands occur simultaneously. Symptoms: players make obvious mistakes, miss clear visual cues, feel frustrated without understanding why.

**Design rules for managing cognitive load:**
- Introduce one mechanic at a time during onboarding
- Use **spaced repetition:** re-introduce mechanics after an interval to consolidate to LTM
- Keep critical interface elements permanently visible (reduces retrieval demand)
- Make common actions automatic through repetition before introducing complex combinations
- **Context-dependent memory:** players remember things better in the context they learned them — tutorials should mirror actual gameplay conditions

### The forgetting curve

Information not revisited is lost rapidly. Mechanics taught once and not practiced are forgotten. Tutorial design must not just introduce — it must reinforce at spaced intervals, increasing complexity as mechanics are consolidated.

---

## 4. Attention

### Selective vs. divided attention (s014, ch.6)

- **Selective (endogenous):** goal-directed, controlled attention. "I'm looking for the key."
- **Passive (exogenous):** stimulus-driven, automatic. "That flashing thing caught my eye."

**Divided attention** (multitasking) is costly and error-prone. The brain can't fully process two demanding tasks in parallel; it rapidly switches between them. During intense combat, players in high selective attention states will completely miss UI elements, popups, and even audio cues they'd normally notice — **inattentional blindness**.

**Design consequence:** don't teach new mechanics during high-attention gameplay sequences. Tutorial popups during combat are seen but not processed. Place teaching moments in low-attention contexts (loading screens don't count — those are missed entirely).

### Directing attention (s014; s005)

The brain's passive attention is drawn to:
- **Motion:** anything moving catches the eye
- **Contrast:** bright objects against dark backgrounds; unusual colors in a neutral field
- **Size:** larger objects attract more attention
- **Sound:** audio cues bypass visual attention filters entirely (fastest emotional channel)

If the designer controls what the eye goes to, they control where the player goes. This is the perceptual foundation of all indirect control (s005, ch.16).

---

## 5. Fun — Three Frameworks

The three most influential answers to "what is fun?" in the canon:

### Koster: fun = pattern learning (s016)

> *"Fun from games arises out of mastery. It arises out of comprehension. It is the act of solving puzzles. In other words, with games, learning is the drug."*

The brain evolved as a pattern-recognition machine. When it successfully acquires a new pattern, it releases a pleasurable signal. Games are formal systems stripped of real-world noise — pure, tractable patterns for the brain to recognize and master.

**Boredom as failure signal:** boredom means no new patterns are available. It's the brain's notification that the game has been exhausted.

**The definition of a good game:** one that teaches everything it has to offer before the player stops playing.

### MDA: fun = targeted aesthetic experiences (s011)

LeBlanc, Hunicke & Zubek reject "fun" as too vague and replace it with 8 specific aesthetics:

| # | Aesthetic | The drive |
|---|---|---|
| 1 | Sensation | Sensory pleasure — visual, audio, haptic, kinesthetic |
| 2 | Fantasy | Make-believe, escapism, being someone else |
| 3 | Narrative | Drama, story, unfolding events |
| 4 | Challenge | Mastery, obstacle course, competition |
| 5 | Fellowship | Social framework, cooperation, community |
| 6 | Discovery | Exploration, novelty, uncharted territory |
| 7 | Expression | Self-discovery, customization, creativity |
| 8 | Submission | Pastime, relaxation, low-stakes engagement |

Design for specific aesthetics, not for "fun." A horror game targets Sensation + Fantasy + Challenge. A party game targets Fellowship + Challenge + Sensation. Knowing your target aesthetics makes every design decision sharper.

### Sellers: fun = sustained engagement (s001)

> *"Fun is too shallow a target. What we're really designing for is sustained engagement — the player's ongoing desire to continue interacting with the game system."*

A game can be scary, frustrating, melancholy, or morally disturbing and still be deeply engaging. The game's job is to maintain the interactive loop in the healthy zone — appropriate arousal + continuous mental model updating — not to produce a specific emotional valence.

**The reconciliation:** these three aren't contradictions — they're different vocabularies for the same phenomenon. Koster's "fun" = MDA's Challenge + Discovery aesthetics primarily. Sellers' "engagement" includes all 8 aesthetics plus art game experiences. All agree: the real target is *sustained engagement where the player's actions feel meaningful*.

---

## 6. The Flow Channel

**Csikszentmihalyi's flow state** (via Schell, s005, ch.9) is the optimal zone of human experience: fully absorbed, not bored, not overwhelmed. Required conditions:

- Clear goals (player knows what to do right now)
- Direct, immediate feedback (player knows whether they're succeeding)
- No distractions
- Continuous achievable challenge (difficulty stays in the narrow band where success is possible but not guaranteed)

The **flow channel** diagram:
```
↑ Challenge
│         ╱─────── FLOW CHANNEL (challenge ≈ skill)
│       ╱     
│     ╱       ← ANXIETY (too hard)
│   ╱         
│ ╱           
│             ← BOREDOM (too easy)
└──────────────────────→ Skill
```

As skill grows, challenge must grow proportionally to maintain the channel. A good game "climbs the channel" — increasing challenge in sync with growing player skill.

**Koster's convergent framing:** the "learnable middle" is structurally identical to the flow channel. Both describe the zone where challenge meets skill. Koster adds the mechanistic why: the flow channel is fun because that's where pattern acquisition is actively occurring.

**Sellers' systems framing:** the interactive loop must maintain the player in a state of **engaged attention** — neither understimulated (loop too slow, no new information) nor overwhelmed (loop too fast to process). Flow requires the right loop tempo.

**The macro structure — tense and release** (Schell, s005, ch.9): good games don't maintain constant challenge; they oscillate. Tension rises (challenge increases) → peak (boss, difficult puzzle) → release (reward, easier content) → brief rest → tension rises again. This pattern appears at every timescale from single encounters to the full game arc.

**Flow is hard to test:** requires long observation. Watch for the moment a player exits the channel — **boredom exit** (disengagement, phone-checking) requires a difficulty increase; **anxiety exit** (repeated failure, frustration) requires difficulty reduction or skill teaching.

---

## 7. Motivation

### Maslow's hierarchy applied to games (s005, ch.9)

| Level | Human need | Game design examples |
|---|---|---|
| 5 — Self-actualization | Personal growth, achievement of full potential | Creative games, master-level competition |
| 4 — Esteem | Achievement, mastery, recognition, status | Most single-player and competitive games |
| 3 — Belonging | Social connection, acceptance, community | Multiplayer games, guilds, co-op |
| 2 — Safety | Security, stability | — |
| 1 — Physiological | Survival | — |

Most games operate at esteem (level 4). **Multiplayer games operate at belonging (level 3)** — this explains their stronger psychological pull and higher retention. Creative/community games can reach levels 3–5.

**Critical rule** (Lens #19, s005): if a game promises to fulfill a need and fails to deliver, the disappointment is proportionally bitter. A game that promises community (multiplayer, social features) must actually deliver community. A dead multiplayer is particularly disabling because it violates a level-3 promise.

### Self-Determination Theory (Ryan & Deci, via s014)

Three innate psychological needs that, when satisfied, enhance intrinsic motivation:

**Competence** — feeling effective and growing in skill.
- Delivered by: the flow channel, level-up moments, feedback that attributes success to player skill
- Games that satisfy competence: any game with a legible skill curve and appropriate difficulty

**Autonomy** — feeling in control, having meaningful choices.
- Delivered by: consequential decisions, multiple valid approaches, customization, no artificial railroading
- Games that satisfy autonomy: open worlds, branching RPGs, sandbox games

**Relatedness** — feeling connected to others or to characters.
- Delivered by: multiplayer, social features, character attachment, community
- Games that satisfy relatedness: co-op, guilds, games with compelling companion characters

Games satisfying all three produce the **strongest intrinsic engagement** and longest retention.

### The undermining effect (overjustification) (s014)

Adding expected, tangible extrinsic rewards to an intrinsically motivating activity can **decrease** intrinsic motivation. Players who loved a game for its own sake begin to feel they're "working for rewards" rather than playing. If the rewards are removed, intrinsic motivation may not recover.

This is the central ethical problem of F2P monetization: reward systems that were meant to enhance engagement can erode the intrinsic enjoyment that makes the game worth playing.

**Design rule:** don't monetize or extrinsically reward activities the player already intrinsically enjoys. That enjoyment is the core product.

### Reward schedules (s014)

| Schedule | Pattern | Engagement effect | Example |
|---|---|---|---|
| **Continuous** | Reward every action | Rapid satiation | XP per button press |
| **Fixed ratio** | Reward after N actions | Steady, pauses after each reward | Achievement at 100 kills |
| **Variable ratio** | Reward after unpredictable N | Highest, most persistent — "slot machine" | Loot drops, gacha |
| **Fixed interval** | Reward after time T | Spikes near reward, drops otherwise | 24-hour login bonus |
| **Variable interval** | Reward after unpredictable T | Moderate persistent | Random world events |

**Variable ratio** produces the strongest engagement. The unpredictability of the reward — knowing it's *coming* but not *when* — keeps the player engaged longer than any other schedule. This is the mechanic behind loot boxes, critical hit chances, and rare item drops.

---

## 8. Player Types — Who Is Playing

### Bartle's four types (s005, ch.8; s001)

| Type | Core drive | Card suit |
|---|---|---|
| **Achievers** | Accumulate points, items, status; complete goals | ♦ Diamonds |
| **Explorers** | Discover the breadth; understand how it works | ♠ Spades |
| **Socializers** | Relationships with other players; the social dimension | ♥ Hearts |
| **Killers** | Compete with and defeat other players; dominate | ♣ Clubs |

Use as a design checklist, not a classification tool. Most players are mixtures. Most games should serve all four to retain diverse audiences.

**Player lifecycle shift** (s001): new players trend Achievers (need clear goals to feel competent) → experienced players shift to Explorers (probe the system) → long-term players become Killers or Socializers (having mastered the game, they compete or build community).

**F2P design maps directly to Bartle** (s017):
- Achievers → daily missions, battle pass tiers, collection systems
- Explorers → seasonal content, story updates, hidden secrets
- Socializers → guilds, co-op events, friend features
- Killers → ranked modes, leaderboards, PvP content

### MDA's 8 aesthetics as a player taxonomy

More granular than Bartle and maps directly to feature design. A player coming for Fellowship needs different features than one coming for Challenge, even if both are "Socializers" in Bartle's terms.

---

## 9. Emotion and Bias

### Loss aversion (Kahneman & Tversky, via s014)

Losses are felt approximately **twice as strongly** as equivalent gains. Players are more motivated to *avoid losing something* than to *gain an equivalent reward*.

Game applications:
- Permanent death → high motivation through loss aversion
- Save before risky action → player is motivated to reach the checkpoint
- F2P FOMO mechanics ("this offer expires in 24 hours") → exploit loss aversion to drive purchases

Ethical design uses loss aversion for meaningful stakes. Exploitative design uses it to coerce spending.

### Dunning-Kruger effect (s014)

Novice players overestimate their understanding; they may skip tutorials, then feel cheated when they fail. Design for overconfident beginners: make failure instructive rather than just punishing, and make tutorial content available passively (the world teaches) not only actively (popup demands attention).

### Confirmation bias (s014)

Players focus on information that confirms their mental model and ignore disconfirming information. Tutorial must repeat key information until the model is correct — one mention is almost never enough.

---

## 10. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| The brain constructs experience; perception is not passive | s014, s015 |
| Working memory has ~3–4 item capacity; respect cognitive load | s014 |
| Procedural LTM (mastery) is encoded through doing, not reading | s014, s016 |
| Flow requires clear goals + feedback + appropriate challenge | s005, s016, s001 |
| Fun = pattern learning = sustained engagement (same phenomenon, different vocabulary) | s016, s011, s001 |
| Intrinsic motivation is more durable than extrinsic | s014 |
| Extrinsic rewards can undermine intrinsic motivation | s014 |
| Variable ratio rewards produce maximum engagement | s014 |
| Loss aversion is ~2× stronger than equivalent gain | s014 |

---

