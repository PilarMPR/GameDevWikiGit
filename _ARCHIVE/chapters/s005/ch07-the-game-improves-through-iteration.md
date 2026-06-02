# s005 · Ch.7 — The Game Improves Through Iteration

**Book:** [[../../sources/s005-art-of-game-design|The Art of Game Design (Schell)]] · **PDF pp. 75–95**
· **Lenses:** **#13 The Eight Filters, #14 Risk Mitigation, #15 The Toy** · **Prev:** [[ch06-the-game-begins-with-an-idea]]
· **Next:** [[ch08-the-game-is-made-for-a-player]]

## Chapter summary
The heart of the design process: **iterate.** Choose an idea decisively, run it through eight
filters, and loop (prototype → test → improve) as many times as you can afford. Borrows the
**spiral model** (risk assessment + prototyping + looping) from software engineering.

## Subsections

### Choosing an Idea
- **Commit fast, reverse fast.** Deciding "yes, I'll make this" reveals flaws and benefits you
  couldn't see before (Steinbeck: "a plan is a real thing"). But **"ideas are like paper cups,
  not fine china"** — drop one the moment it stops working. Snap decisions + willing reversals =
  the fastest use of your decision-making power.

### The Eight Filters → 🔎 Lens #13 — The Lens of the Eight Filters
A finished design must pass all eight; changing it to pass one may break another, so re-run all:
1. **Artistic Impulse** — "Does this game feel right?"
2. **Demographics** — "Will the intended audience like it enough?" (ch.8)
3. **Experience Design** — "Is this a well-designed game?" (the many lenses)
4. **Innovation** — "Is this game novel enough?"
5. **Business & Marketing** — "Will this game sell?" (ch.29)
6. **Engineering** — "Is it technically possible to build?" (ch.26)
7. **Social/Community** — "Does it meet our social/community goals?" (ch.21–22)
8. **Playtesting** — "Do playtesters enjoy it enough?" (ch.25 — *arguably the most important*).
- You may add filters (e.g. educational: "does it teach what it should?") or change a filter
  (retarget the demographic). The job: get through all of them, by changing the design or the filters.

### The Rule of the Loop
- **"The more times you test and improve your design, the better your game will be."** Not a
  lens — an *absolute truth* with no exceptions. The danger of digital games: each loop is
  expensive, forcing **fewer loops** = more risk. Two questions: **(1) How can I make every loop
  count? (2) How can I loop as fast as possible?**

### A Short History of Software Engineering
- **Waterfall model** (1970s): seven linear steps, *violates the Rule of the Loop* — appealing
  to managers, absurd to programmers. (Even Royce, its supposed origin, stressed iteration and
  never said "waterfall.")
- **Barry Boehm's spiral model** (1986): three big ideas — **risk assessment, prototypes,
  looping**. Loop: basic design → identify greatest risks → build prototypes to mitigate them →
  test → refine design → repeat. Answers Loop Q1 (**assess & mitigate risks**) and Loop Q2
  (**build many rough prototypes**).

### Risk Assessment & Prototyping → 🔎 Lens #14 — The Lens of Risk Mitigation
- Worked example *Prisoners of Bubbleville*: list the risks (is the core mechanic fun? can the
  engine draw it all? too much art? will players like the characters? a forced re-theme?), then
  **mitigate each with a targeted (often throwaway) prototype** — a 2D abstract version of the
  mechanic, a tech stress-test with no gameplay, one house to time the art, concept-art on a
  bulletin board, management pressure for the re-theme decision.
- Lens #14: stop thinking positively — *"What could keep this game from being great? How do we
  stop that?"* Face the scary parts first.

### Eight Tips for Productive Prototyping
1. **Answer a question** (state it clearly; don't overbuild).
2. **Forget quality** (rough is better — polish hides problems and lulls you).
3. **Don't get attached** (Brooks: "plan to throw one away"; "learn to cut up your babies").
4. **Prioritize your prototypes** (biggest/upstream risks first).
5. **Parallelize** (tech, art, gameplay prototypes at once = more loops).
6. **It doesn't have to be digital** — **paper prototypes** (Tetris with cardboard; Doom on graph
   paper with a metronome; Toontown's turn-based combat balanced on a whiteboard).
7. **Pick a "fast loop" engine** (late-binding/scripting languages let you recode while running;
   split fast-static low-level + slow-dynamic high-level code).
8. **Build the toy first** (a fun *toy* before the game — *Lemmings*, and *GTA* = "Pac-Man": dots→people, yellow car→me, ghosts→police).

### 🔎 Lens #15 — The Lens of the Toy
Is it fun to play *with*, even with no goal? Do people want to interact before they know what to
do? Use it to add toy-like appeal to a game, or (braver) to invent toys before knowing the game.

### Closing the Loop — the Formal Loop
1. State the problem · 2. Brainstorm solutions · 3. Choose a solution · 4. List the risks ·
5. Build prototypes to mitigate them · 6. Test (good enough? stop) · 7. State the new problems → go to 2.
- Worked "racing game" example shows **problem statements getting more specific each loop**
  (new racing game → racing subs → flying dinos) and ugly problems surfacing early.

### How Much Is Enough?
- The Rule of the Loop means one more loop always helps — *"work is never finished, only
  abandoned."* You can't accurately estimate completion at loop 1 because you don't yet know
  what you're building. **Mark Cerny's "The Method":** you're in **pre-production** until you
  have **two fully publishable levels** (~30% of budget); only then can you reliably schedule
  the rest (the remaining ~70%). Iteration is the key to *any* design, not just games.

## Key concepts & links
- **THE central cross-book node for process.** This is Schell's version of
  [[../../concepts/iterative-design-and-playtesting]]: identical loop to Macklin & Sharp's
  *conceptualize→prototype→playtest→evaluate* ([[../../sources/s009-games-design-and-play|s009]] ch.5),
  Fullerton's playcentric prototyping ([[../../sources/s008-game-design-workshop|s008]]), and
  Sellers' designer's loop ([[../../concepts/the-four-principal-loops]], s001).
- **"Prototypes answer questions"** = Macklin & Sharp's *"prototypes are playable questions"*
  (s009 ch.10, 8 kinds of prototypes) — near-identical idea, two books.
- **Build the toy first** ↔ toy/game distinction from [[ch03-the-experience-rises-out-of-a-game]].
- **Pre-production/production phases** ↔ Sellers ch.12 dev phases
  ([[../../concepts/systemic-design-process]], s001) and the F2P live-tuning loop ([[../../concepts/free-to-play-design]], s017).
- **Risk-driven looping** ↔ game development as risk management; cf. [[../../concepts/systemic-design-process]].

## Notable quotes
- *"The more times you test and improve your design, the better your game will be."* (The Rule of the Loop)
- *"Ideas are like paper cups… when one has holes in it, go get another one."*
- *"Plan to throw one away — you will anyway."* (Fred Brooks)
- *"Work is never finished, only abandoned."*
