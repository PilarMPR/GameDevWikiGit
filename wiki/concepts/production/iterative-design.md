# Iterative Design

The process of repeatedly designing, building, testing, and refining — the professional standard for game development. The core insight: **you cannot design a great game by thinking about it; you can only design one by making it and watching people play it.** Iteration is what separates game design from game theory.

---

## Why iteration is necessary (s005, ch.7; s008; s009)

Games are interactive, dynamic systems whose quality can only be assessed in play. Unlike a book or painting, which can be evaluated by its creator, a game's quality depends on the player's *experience of it* — which is inaccessible until someone plays it. This creates a fundamental epistemic problem:

> "The game is not the experience. The game is the artifact that creates the experience. You can't know if you've got the experience right until someone plays the artifact." (Schell paraphrased, s005, ch.7)

Iteration is the process of repeatedly closing the gap between the designed artifact and the desired experience. It cannot be skipped or compressed — it can only be made more efficient.

---

## The playcentric design process (s008)

Fullerton's foundational framework: design revolves around the player's experience, assessed through continuous playtesting.

The cycle:
1. **Conceptualize** — define the experience goal, the core mechanic, and a rough sense of what makes this game worth playing
2. **Prototype** — build the minimum viable version as quickly as possible. Physical prototypes (paper, cards, dice) are fastest. Speed matters more than fidelity at this stage.
3. **Playtest** — put the prototype in players' hands and observe. What do they understand? What do they struggle with? What are they feeling?
4. **Evaluate** — analyze playtest observations against the experience goals. What needs to change?
5. **Revise** — make targeted changes, then prototype the revised version
6. **Repeat** — continue the cycle until the experience goals are met

The key rule: **move to the next cycle as soon as possible**. A day of playtesting teaches more than a week of thinking. (s008, ch.1)

---

## Schell's "Rule of the Loop" (s005, ch.7)

> "The more times you go around the loop, the better your game will be." (s005, ch.7)

Schell's principle is simple: iteration count directly correlates with quality. A game playtested 50 times is better than a game playtested 5 times, assuming the designer is learning from each test. This means:
- Make prototypes faster and cheaper so you can test more often
- Make smaller, faster cycles rather than longer, deeper ones
- Build the simplest possible thing that lets you answer the current design question

### Schell's 8 prototyping tips (s005, ch.7)
1. **Answer a question**: every prototype should answer a specific design question, not just "is this fun?"
2. **Forget quality**: a prototype is not a product; don't waste time on polish
3. **Don't get attached**: be willing to throw prototypes away when they've answered their question
4. **Prototype the hardest thing first**: test the risky elements early, when change is cheap
5. **Expect the unexpected**: the most useful prototypes reveal surprises, not confirmations
6. **Use physical prototypes when possible**: physical is faster to modify than digital
7. **Build the toy first**: make the core interaction feel satisfying before adding game structure
8. **Get it in front of people fast**: designer intuition is unreliable; player behavior is real

---

## Macklin & Sharp's design process (s009)

Macklin & Sharp's framework emphasizes **design values** — explicit statements of what the designer believes is important — as the anchor for iteration:

1. Define **design values**: what experiences and ideas is this game trying to create? These become the evaluation criteria for every playtest.
2. **Prototype rapidly**: generate multiple possible approaches; don't commit to one direction too early
3. **Playtest with intention**: each playtest should test specific design questions derived from design values
4. **Reflect and revise**: after each test, evaluate against design values — did the prototype produce the intended experience?

The emphasis on design values prevents "feature creep" and ensures that iteration stays purposeful rather than reactive. Without design values, every playtest suggestion gets incorporated; with them, suggestions are filtered through "does this serve the experience we're building?" (s009, ch.1–2)

---

## Sellers' systemic design process (s001, ch.5)

Sellers frames iteration as the designer's loop — one of the four principal loops in game design:

> "The designer's loop: define experience → design system → observe player → revise system → repeat." (s001, ch.7)

Sellers' contribution: **the designer must think in systems, not features**. When a playtest reveals a problem, the fix is not always adding a feature — often the system needs to be restructured. The designer's loop requires willingness to discard not just a mechanic but the architecture that produced it.

Key principle: **observe, don't explain**. When watching a playtest, resist the urge to explain why the design made a choice. Let the player encounter the design as it is and observe their actual behavior. The game must explain itself through play, not through the designer's words. (s001, ch.5) → [[playtesting]]

---

## Waterfall vs. iteration (s005, ch.7)

Traditional software development used **waterfall**: complete design → complete production → test at the end. For games, this is catastrophically bad:
- Design can't be verified until it's playable
- Problems discovered at the end are expensive to fix (most code and content is already built around the bad design)
- The game that ships is the first full version anyone has played

**Boehm's spiral model** (cited by Schell as superior): iterative development with risk mitigation at each cycle. Test the riskiest elements first; each spiral adds more completeness while continuously validating the core.

**Cerny's Method** (described by Mark Cerny, cited s005): specifically for games:
1. Make a small, polished version of the core experience first (2 "publishable levels")
2. Get the experience right before building the rest of the game around it
3. Pre-production ends when those core levels are fun; production then expands the proven design

---

## Practical iteration discipline

Common failure modes in iteration:
- **Design by committee**: every playtest comment is treated as valid feedback; the game responds to individuals rather than patterns. Fix: look for behavior patterns across multiple playtesters, not individual reactions.
- **Feature creep**: each iteration adds features; the game grows but doesn't improve. Fix: for every addition, ask what can be removed.
- **Playtest too late**: the first player to try the game is the final playtester. Fix: get players involved from week one with paper prototypes.
- **Sunk cost attachment**: the designer can't kill features they've spent time on. Fix: the question is never "how much work was this?" but "does it serve the experience goal?"

---

## Key concepts & cross-links

- [[playtesting]] — the test phase of the iteration cycle; methods and practices
- [[documentation]] — how design decisions are captured between iterations
- [[team-and-culture]] — how iteration works in a team context
- [[../../mechanics/game-loops]] — the designer's loop is itself a loop that produces the game
- [[../../theory/meaningful-play]] — iteration is how you verify that play is meaningful
- [[../../player/flow-channel]] — playtesting is how you verify the player is in the flow channel

## Sources

s008 ch.1, ch.9 (Fullerton — playcentric design process, iteration as method, physical prototypes) · s005 ch.7 (Schell — Rule of the Loop, 8 prototyping tips, Boehm spiral, Cerny's Method; Lenses #13–15) · s009 ch.1–2 (Macklin & Sharp — design values, design process) · s001 ch.5, ch.7 (Sellers — systemic design process, designer's loop)
