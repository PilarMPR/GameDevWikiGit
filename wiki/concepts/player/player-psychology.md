# Player Psychology

The cognitive, emotional, and motivational substrate that games operate on. Understanding how players perceive, remember, attend, and feel is the foundation for designing experiences rather than just mechanics.

---

## The brain as a game design constraint (Hodent, s014)

Hodent's central argument in *The Gamer's Brain*: games don't operate in a rational cognitive vacuum. The human brain has **fixed constraints** — limits on perception, attention, and memory — and **systematic biases** that shape how players experience games. Effective game design works *with* these constraints, not against them.

Key myths to dispel (s014, ch.3):
- "We only use 10% of our brains" — false; all brain areas are active
- "Right-brain vs. left-brain" — both hemispheres work together in most activities
- "Digital natives have different brains" — the brain adapts to experience, but not categorically differently for gamers

The designer's job: align the game's **communicative intent** with the player's **mental model** of what the game is doing. When these diverge, the player is confused, frustrated, or lost — not because they're bad players, but because the design failed to account for cognitive realities.

---

## Perception (s014, ch.4)

Perception is **active and subjective** — the brain doesn't passively receive the world; it constructs a representation of it, influenced by:
- **Bottom-up processing**: sensory input → interpretation
- **Top-down processing**: expectations, prior experience → shape what is perceived

**Key principles for game design:**

### Visual acuity and foveal focus
The eye has highest resolution only at the **fovea** (center of the visual field); peripheral vision is blurry and motion-sensitive. Critical game information (health bars, enemy indicators) must be placed where the player's gaze is likely to be, or use strong peripheral signals (screen edge glow, vignetting) for off-center alerts.

### Gestalt principles
The brain automatically groups visual elements by proximity, similarity, and continuity. UI and HUD design that uses these principles is read *faster and more accurately* than designs that fight them.

### Affordances (Norman, s015)
An **affordance** is a design property that communicates its own use. A button that looks pressable *affords* pressing. In games: a glowing item *affords* collection; a ledge at avatar-height *affords* grabbing. Poor affordances make the player guess what the game wants from them (see [[../interface/usability-and-hcd]]).

### Weber–Fechner bias
Perceived changes in intensity are **not linear** — they follow a logarithmic curve. A +10 damage upgrade feels huge at level 1 but negligible at level 50. Progression systems must account for this: linear numeric scaling produces diminishing perceived reward. Exponential curves better match perceived progress (s014, ch.4).

### Mental model alignment
"Aligning developer intentions with players' mental models is crucial." When a player's mental model of how a mechanic works is wrong, they will behave inconsistently until the model is corrected — either through tutorial, clear feedback, or playtesting iteration (s014, ch.3; s015 ch.1).

---

## Memory (s014, ch.5)

The **multistore memory model** (Atkinson & Shiffrin):

| Store | Capacity | Duration | Game relevance |
|-------|----------|----------|----------------|
| **Sensory memory** | Large | <1 second | Pre-attentive perception; change blindness |
| **Short-term memory (STM)** | ~7 items | <1 minute | Tutorial information at first exposure |
| **Working memory (WM)** | ~3–4 items | Active | Simultaneous demands during gameplay; cognitive load |
| **Long-term memory (LTM)** | Unlimited | Indefinite | Learned mechanics (implicit/procedural); game knowledge |

**Procedural (implicit) LTM** is how players internalize controls: after enough practice, button presses become automatic. This is why good games teach through **doing** rather than telling — procedural memory is encoded through action, not reading.

**Design implications:**
- **Cognitive load** during onboarding must be managed — don't dump 7+ new systems in a tutorial simultaneously
- Use **spaced repetition**: re-introduce mechanics after an interval to move them from STM to LTM
- Keep critical interface elements permanently visible to reduce memory retrieval demands
- **Context-dependent memory**: players remember things better in the context where they learned them — tutorials should mirror gameplay contexts

**The forgetting curve**: information not revisited is lost rapidly. Mechanics taught once and not practiced again are forgotten. Design onboarding to reinforce, not just introduce (s014, ch.5).

---

## Attention (s014, ch.6)

Attention is the **selective amplification** of relevant information. Two types:
- **Active/endogenous**: goal-directed, controlled ("I'm looking for the key")
- **Passive/exogenous**: stimulus-driven, automatic ("that flashing thing caught my eye")

**Selective attention** focuses on one input while inhibiting others. **Divided attention** (multitasking) is cognitively expensive and error-prone — the brain can't fully process two demanding tasks in parallel; it rapidly switches between them.

**Inattentional blindness**: players focusing intensely on one task may completely miss important events happening in other parts of the screen. Tutorial popups during intense combat fail because players are in a state of high selective attention.

**Cognitive load** (Sweller): every task requires attentional resources. Complex games overload working memory if too many demands occur simultaneously. Symptoms: players make obvious mistakes, miss clear visual cues, feel frustrated without understanding why.

**Design implications:**
- Direct attention to critical information through **salience** (motion, contrast, sound, size) — these trigger passive attention reliably
- Don't teach new mechanics in the middle of high-attention gameplay sequences
- Use **dual sensory cues** (visual + audio) for critical events — attention may be elsewhere for one channel
- Reduce cognitive load by making common actions automatic (good control mapping, clear action-to-button mapping) so they consume minimal working memory

---

## Motivation (s014, ch.7; s005 ch.9)

### Maslow's hierarchy (Schell, s005 ch.9)
Maslow's five-level hierarchy (physiological → safety → belonging/love → self-esteem → self-actualization) shapes which needs a game can fulfill:
- Most games operate at **self-esteem** (achievement, mastery, recognition)
- **Multiplayer** games can reach **belonging** (level 3) — explaining their stronger psychological pull
- **Community/creation games** can reach levels 3–5
- A game must deliver the need it promises; unfulfilled promises of belonging or mastery create a particularly bitter disappointment (Schell Lens #19: The Lens of Needs)

### Intrinsic vs. extrinsic motivation (Hodent, s014 ch.7)
- **Intrinsic motivation**: engaging in an activity for its own sake — it is inherently rewarding
- **Extrinsic motivation**: engaging for an external reward (points, money, social recognition)

**The undermining effect (overjustification effect)**: adding expected extrinsic rewards to an intrinsically motivating activity can *decrease* intrinsic motivation. Players who loved a game for its own sake can have that love eroded by aggressive monetization that reframes the activity as "work for reward."

### Self-Determination Theory (SDT) (s014)
Ryan & Deci's SDT identifies three innate psychological needs that, when fulfilled, enhance intrinsic motivation:
- **Competence** — feeling effective and growing in skill
- **Autonomy** — feeling in control, having meaningful choices
- **Relatedness** — feeling connected to others

Games that satisfy all three produce the strongest intrinsic engagement. The best game designs create a sense of **growing competence** (through the challenge-skill dynamic), **meaningful autonomy** (consequential choices, not scripted paths), and **relatedness** (multiplayer, shared culture, story connections).

### Reward schedules (s014)
- **Continuous rewards** (every action rewarded) lead to rapid satiation
- **Intermittent (variable ratio) rewards** produce the highest, most consistent engagement — the "slot machine effect"
- F2P games exploit intermittent rewards aggressively; ethical design ensures the activity itself is rewarding, not just the rewards (s017)

---

## The four mental abilities (Schell, s005, ch.9)

Schell identifies four cognitive abilities that make gameplay possible:

### Modeling
The mind never experiences reality — only **simplified models** of it. Games are "pre-digested models" — they strip reality's complexity and present pure, tractable systems for the mind to reason about. This is why even abstract games (chess) feel meaningful: they match our brain's model-building machinery perfectly.

> ⭐ **Cross-link:** The player's mental model (Schell ch.9) ≡ Norman's conceptual model (s015) ≡ Sellers' player mental model loop (s001, ch.7).

### Focus
The brain selects a narrow band of sensory input to attend to at any moment (cocktail party effect). **Flow** (Csikszentmihalyi) is sustained focus + enjoyment. Games facilitate focus by providing clear goals, direct feedback, and manageable challenge — the conditions that allow the brain's attentional system to lock onto the game world. See [[flow-channel]].

### Imagination
The brain fills gaps — it infers missing information from context. Games **don't need to show everything**; the player's imagination fills what's left out, often more richly than any explicit depiction. The art: knowing what to show and what to leave to imagination. Text adventures relied entirely on this; modern games calibrate between visual completeness and imaginative suggestion.

### Empathy
Humans **project decision-making capacity** into perceived agents. We empathize with cartoon characters, game avatars, and even abstract shapes (Heider & Simmel). In games, the player projects their full identity into their character — this is deeper than empathy with a film character; the player is making the decisions. This projection is the psychological mechanism behind "being" your character (s005, ch.9).

---

## Emotion in games (Hodent, s014 ch.8)

Emotions are **fast, pre-cognitive evaluations** of situations. The amygdala responds to threats and rewards before the cortex can reason about them. This is why:
- **Fear in horror games** is genuine — the threat-response system doesn't know it's fiction
- **Loss aversion** in games (losing what you've earned) hurts more than equivalent gains feel good
- **Frustration** (blocked goal) can quickly override rational engagement; game design must create frustration-resistant flow paths

**Emotional engagement tools:**
- Character design that triggers empathy (large eyes → perceived vulnerability, Schell ch.9)
- Narrative context that frames stakes (s005 ch.15–18)
- Music and sound as the fastest emotional channel
- Victory/defeat rituals that give emotional punctuation to game events

---

## Cognitive biases in game design (Hodent, s014 ch.3)

Systematic deviations from rational cognition that affect how players experience games:
- **Anchoring**: first values seen in a game become reference points (initial health bar, first-seen prices)
- **Confirmation bias**: players focus on information that confirms their mental model, ignore disconfirming information → tutorial must repeat key information until the model is correct
- **Dunning-Kruger effect**: novice players overestimate their understanding; they may skip tutorials, then feel cheated when they fail
- **Loss aversion**: players feel losses ~2x as intensely as equivalent gains → game economy must account for this in reward calibration

---

## Key concepts & cross-links

- [[flow-channel]] — flow as the psychological state when attention, motivation, and challenge align
- [[motivation]] — deeper treatment of Maslow, SDT, intrinsic/extrinsic motivation
- [[player-types]] — how different players have different motivational profiles
- [[../interface/usability-and-hcd]] — Norman's HCD framework; affordances, feedback, mental models
- [[../theory/theory-of-fun]] — Koster's fun = learning; the brain as pattern-matcher
- [[../mechanics/game-loops]] — loops must maintain player in a state of engaged attention
- [[../feel-and-controls/game-feel]] — proprioception and kinesthetic self-extension into avatar

## Sources

s014 (Hodent, notes ed.) · s005 ch.9 (Schell — four abilities, Maslow) · s001 ch.4 (Sellers — mental models, arousal, engagement) · s015 (Norman — affordances, mental models) · s016 (Koster — fun as learning, pattern-matching) · s017 (F2P — reward schedules, dopamine loops)
