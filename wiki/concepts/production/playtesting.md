# Playtesting

The practice of systematically observing players interact with a game to gather information that drives design decisions. Playtesting is not a validation exercise ("is this good?") but a **learning exercise** ("what is happening and why?").

---

## What playtesting is and isn't (s008, ch.9; s009)

**Playtesting is:**
- Observing players interacting with the current prototype
- Gathering specific data to answer specific design questions
- Identifying gaps between the designer's intent and the player's experience
- The primary feedback mechanism for iteration

**Playtesting is not:**
- Market research (asking players what they want in a game)
- Quality assurance (testing for bugs — that's QA, different discipline and timing)
- Focus groups (asking players' opinions before anything exists)
- Validation (confirming the designer's choices are good)

> "Playtesting and iterative design are at the heart of the design process. This is how you make games better." (s008, ch.1)

---

## The six types of playtests (s009)

Macklin & Sharp identify six distinct playtesting modes:

### 1. Internal playtests
The design team plays the game themselves. Fast, cheap, and continuous — should happen after every significant change. Limitation: the team knows how the game is supposed to work, producing blindness to problems new players will encounter.

### 2. Game developer playtests
Other designers (from the same or different studios) play the game. Value: designers give precise, actionable feedback; they can articulate what broke, not just that it felt wrong. Limitation: game developers play differently from the target audience.

### 3. Friend and family playtests
Known people who will give honest feedback. Value: accessible, willing, and motivated to help. Limitation: social dynamics may soften criticism; they know the designer and may rationalize problems.

### 4. Target audience playtests
People in the intended audience who don't know the team. Value: closest to the actual players. Limitation: harder to access; may require incentives.

### 5. New player playtests
People playing the game for the first time, specifically to test onboarding, first impressions, and tutorial effectiveness. Critical for any game where new-player experience matters.

### 6. Experienced player playtests
Players who have already played significant time with the game, testing mid-game and late-game content. Reveals problems that only emerge after the player is competent.

**Matching prototype to playtester**: an early paper prototype with rough mechanics needs developer feedback; a near-final digital version needs target audience feedback. The type of test should match the stage of development. (s009)

---

## Data types: what to collect (s008, ch.9)

### Qualitative data
What players say and show:
- **Think-aloud protocol**: ask players to narrate their thoughts while playing. Reveals mental model formation, confusion points, and decision-making
- **Post-session interviews**: structured questions about the experience after play. Players can reflect and articulate more clearly after the session
- **Observation notes**: the facilitator records specific behaviors, reactions, and events without interpretation

### Quantitative data
What the numbers show:
- **Completion rates**: what percentage of players reach each milestone?
- **Attrition points**: where do players stop playing?
- **Time spent**: how long on each section? (Too fast = trivial; too slow = stuck or boring)
- **Retry rates**: how often do players attempt a section multiple times?
- **Feature usage**: which mechanics do players use, and which do they ignore?

### Behavioral data
What players do vs. what they say:
- **"Lab behavior"**: players will sometimes do things that contradict what they say they're doing or enjoying. Trust behavior over stated preference.
- **Body language**: leaning forward (engagement), slumping (disengagement), frustration tells (rapid inputs, sighing)
- **Where they look**: with eye-tracking or observation, which UI elements get attention?

---

## The facilitator's role (s008, ch.9)

The test facilitator's job is to **observe without interfering**:
- Do not explain anything the game doesn't explain itself. If the player is confused, that confusion is data.
- Do not lead: questions like "did you like the jump mechanic?" invite confirmation. Ask "what did you think about the movement?"
- Do not defend: when players criticize design decisions, do not explain why the design was made that way. Their criticism is real; the explanation is irrelevant.
- Do not help: watching a player struggle is valuable. The moment you explain something to a stuck player, you've lost information about how the game can be made clearer.

> "Observe, don't explain." (Sellers, s001, ch.5)

---

## Conducting a playtesting session (s008, ch.9)

### Before
- Define the questions you want to answer: "Do players understand the combination mechanic?" is testable. "Is the game fun?" is not.
- Prepare observation instruments (note-taking templates, specific behaviors to watch for)
- Set up the environment: remove distractions; ensure the prototype is stable
- Brief playtesters: give them their role and context, but reveal nothing the game doesn't

### During
- Take notes continuously; don't rely on memory
- Use timestamps if possible (at minute 12, player tried to use the wrong item)
- Note both confusion moments AND moments of delight
- Watch for consistent patterns across multiple testers

### After
- Debrief players with open-ended questions
- Review notes before any analysis
- Pattern analysis: what happened with multiple testers? Single-tester observations are anecdotes; patterns are design signals
- Separate observations from interpretations: "player tried the wrong door three times" is an observation; "player didn't understand doors were locked" is an interpretation — make it clear which is which

---

## Reviewing and acting on playtest results (s009)

Macklin & Sharp's evaluation framework:
1. Cluster observations by design area (onboarding / mechanics / pacing / etc.)
2. For each cluster: does this contradict a design value? If yes, it's a priority fix.
3. For each fix candidate: what is the minimum change that would address the problem?
4. What can be removed? (Often the answer to a playtesting problem is removing complexity, not adding it.)

**Danger of over-reaction**: a single playtest reveals a playtest's worth of information, not ground truth. If two of five playtesters didn't understand a mechanic, that's a signal — but it may not be the mechanic's fault. Run multiple tests before making large structural changes. (s008, ch.9)

---

## Playtesting across the development lifecycle

| Stage | What to test | Best playtesters |
|-------|-------------|-----------------|
| Concept (paper prototype) | Core mechanic; fundamental fun hypothesis | Designers, colleagues |
| Early prototype | Onboarding, core loop, pacing | Developer circle, gamers |
| Alpha | All mechanics, content pacing, difficulty curve | Target audience |
| Beta | Polish, edge cases, balance | Target audience + experienced players |
| Pre-ship | Regression testing; new player experience | Fresh target audience |

---

## Key concepts & cross-links

- [[iterative-design]] — playtesting is one phase of the iteration cycle
- [[../../player/flow-channel]] — playtesting is how you verify players are in the flow channel
- [[../../player/player-psychology]] — understanding cognitive load, attention, and mental models helps interpret playtest data
- [[documentation]] — recording playtest observations and design decisions
- [[../../theory/meaningful-play]] — the test: is play discernable and integrated?

## Sources

s008 ch.1, ch.9 (Fullerton — playcentric design, 6 types of playtests, conducting sessions, data types) · s009 (Macklin & Sharp — matching playtests to prototypes, evaluation against design values) · s001 ch.5 (Sellers — observe don't explain, designer's loop) · s005 ch.7 (Schell — prototyping and playtesting as the core loop; Lens #13 The Lens of the Designer)
