# Puzzles

A puzzle is a game with a dominant strategy — a problem with a knowable right answer. Puzzles are everywhere in games, from explicit tile-sliding challenges to implicit strategic decisions. Understanding their structure is essential for designing engaging challenge without frustration.

---

## Definition: puzzle vs. game (s005, ch.12)

> "A puzzle is a game with a dominant strategy." (Scott Kim, cited in s005, ch.12)

The key difference: in a game, no single strategy guarantees victory (the opponent, the random elements, or the evolving state prevents it). In a puzzle, one correct approach exists and, once found, guarantees success every time. This makes puzzles non-replayable in their pure form — "once you figure out the best strategy, you can solve the puzzle every time, and it is no longer fun." (s005, ch.12)

Schell's extension: puzzles are not "less than" games — they are games whose goal is to find the dominant strategy. Tic-tac-toe is interesting to children until they find the dominant strategy; at that point the puzzle has been solved and the game ceases to be fun. (s005, ch.12)

**Puzzles are everywhere**: anytime a player stops and thinks — in any genre — they are solving a puzzle:
- Deciding which enemies to prioritize in a shooter = a tactical puzzle
- Finding the optimal turbo placement in a racing game = a resource puzzle
- Figuring out which strategy works against a fighting game opponent = a pattern-identification puzzle

Modern games have moved from **explicit, incongruous puzzles** (The 7th Guest: a chessboard puzzle appearing randomly in a haunted house game) to **implicit, integrated puzzles** (Zelda: Wind Waker: figuring out how to use the dungeon's items to manipulate switch-controlled doors — the puzzle elements are natural parts of the world). (s005, ch.12)

---

## Ten principles of puzzle design (s005, ch.12)

### Principle 1: Make the goal easily understood
If players don't know what they're trying to do, they won't engage with the puzzle. The goal must be immediately communicable — either self-evident from the puzzle's design or explicitly stated.

Case study: Hasbro's Nemesis Factor failed commercially despite brilliant design because the goal of each puzzle was not clear from looking at it. Even after purchase, players had to figure out what they were supposed to do. Hardcore puzzle fans loved this; general audiences found it frustrating. (s005, ch.12)

### Principle 2: Make it easy to get started
Even when the goal is clear, the first move should be obvious. If players can't envision their first few steps, they give up. Scott Kim: "To design a good puzzle, first build a good toy." A good toy is something people naturally want to touch and manipulate — the first interaction is obvious even before the puzzle is solved.

Rubik's Cube succeeds here: even someone who has no intention of solving it wants to pick it up and twist it. The first interaction is trivially clear. (s005, ch.12)

### Principle 3: Give a sense of progress
The difference between a riddle and a puzzle is often progress. A riddle demands a binary answer — either you know it or you don't. A puzzle allows the player to visibly approach the solution incrementally.

Rubik's Cube: the player can see an entire side complete — clear evidence of progress, even though they haven't solved it. The "20 Questions" game: each question narrows the solution space, giving a visceral sense of closing in. (s005, ch.12)

### Principle 4: Give a sense of solvability
If players begin to suspect the puzzle is unsolvable, they abandon it in frustration. The designer must convince them it can be solved.

Rubik's Cube's elegant solution: it ships in the solved state. The player scrambles it themselves — obviously they just need to reverse what they did, right? This makes it *obviously* solvable, even if reversing the scramble turns out to be extremely difficult. (s005, ch.12)

### Principle 5: Don't impose unnecessary frustration
Frustration = being stuck without a sense of direction. The player knows the goal, can see they haven't reached it, but has no information about what to try next.

Design for gradual revelation: provide clues that open new avenues of approach. The player should always have *something* to try, even if it doesn't immediately succeed.

### Principle 6: Parallelism — let failures lead elsewhere
Give the player multiple sub-puzzles to work on simultaneously. When stuck on one, they can make progress on another. This prevents the "I'm stuck, I quit" response by ensuring that partial progress is always available.

A locked door puzzle that requires three keys: finding any one key is satisfying progress, even if the player can't find the other two yet. (s005, ch.12)

### Principle 7: Pyramid structure
Start with simple, accessible versions of the puzzle mechanics and build toward complexity. The player develops understanding through simpler versions before encountering harder challenges.

This is the Zelda dungeon design philosophy: introduce the dungeon's item mechanic in a simple context, then progressively demand more sophisticated use of it. (s005, ch.12)

### Principle 8: Hints
When players are genuinely stuck, provide hints rather than leaving them in a wall of frustration. The hint should be the minimum information needed to suggest a new avenue — it should not solve the puzzle for the player.

The design problem: players differ in when they want hints. Some want them immediately; others feel hints ruin the experience. Solution: make hints optional and graduated (hint 1 → hint 2 → solution). (s005, ch.12)

### Principle 9: Give a satisfying solution
The solution must feel *right* — the "aha" moment must be genuine. A solution that feels like a guess rather than a logical conclusion is unsatisfying, even when correct.

This means the solution must be logically derivable from information available in the puzzle. Nothing in the solution should be arbitrary.

### Principle 10: Use progressively complex puzzles
Don't make every puzzle equally hard. Calibrate difficulty to create a learning curve: easy puzzles early (teaching the puzzle mechanics), medium puzzles in the middle (building confidence), hard puzzles late (challenging mastery). This is also the interest curve principle applied to puzzle difficulty. → [[../../level-design/pacing-and-flow]]

---

## Explicit vs. integrated puzzles (s005, ch.12)

A critical design dimension for games that include puzzles alongside other gameplay:

**Explicit puzzles**: the game stops, presents a puzzle, and resumes when it is solved. The puzzle is clearly separated from the main gameplay.
- Advantage: the player always knows they're in a puzzle context
- Disadvantage: can feel incongruous if the puzzle is unrelated to the game world (7th Guest problem)

**Integrated puzzles**: puzzle elements are woven into the game world and must be solved as part of natural play.
- Advantage: maintains immersion; the solution is motivated by the game world
- Disadvantage: harder to design; requires the puzzle to make sense within the game's logic

Modern game design strongly prefers integrated puzzles. The puzzle elements of Zelda: Wind Waker are integrated: luring enemies onto pressure plates by using the dungeon's own items makes sense in-world, serves both puzzle and combat simultaneously, and produces a clear "aha" that emerges from the game's mechanics rather than from an external puzzle bolted on. (s005, ch.12)

---

## The walkthrough problem (s005, ch.12)

A common objection: internet walkthroughs make all puzzles trivial because players can simply look up the answer.

Schell's response: this doesn't matter as much as it seems. Players who use walkthroughs have different motivations — they want the experience of the game world, not the challenge of the puzzle. The game still serves them. Players who want the challenge won't use walkthroughs. Designing puzzles with the assumption that no one will ever look them up produces gratuitously obscure puzzles; designing puzzles that remain enjoyable even when the broad solution is known produces better experiences for both types of players.

---

## Puzzles and Koster's fun-as-learning (s016)

Koster's theory applies directly to puzzles: a puzzle is fun while the player is learning its patterns. The moment the dominant strategy is found and internalized, the puzzle is "used up." The designer's goal is to create puzzles whose patterns are engaging to discover but not so easily found that the discovery is trivial.

Well-designed puzzle depth: the puzzle seems simple but contains layered insights — solving the surface puzzle reveals a deeper puzzle, and so on. Braid and The Witness are examples of puzzle games designed around this principle. → [[../../theory/theory-of-fun]]

---

## Key concepts & cross-links

- [[core-mechanics]] — puzzles are a specific application of formal mechanics
- [[game-balance]] — puzzle difficulty calibration is a form of balance
- [[../../level-design/pacing-and-flow]] — puzzle difficulty should follow the interest curve
- [[../../theory/theory-of-fun]] — puzzles succeed when they have appropriate learning depth
- [[../../theory/meaningful-play]] — puzzles require discernable progress and integrated outcomes
- [[../../player/flow-channel]] — puzzle difficulty must track the player's growing skill

## Sources

s005 ch.12 (Schell — puzzle vs. game definition, 10 design principles, explicit vs. integrated, Rubik's Cube analysis, Zelda Wind Waker case) · s016 (Koster — puzzles as pattern-mastery; "used up" principle) · s012 ch.14 (Kremers — puzzle design in level design context) · s006 ch.13 (Adams — challenges and puzzle-type challenge design)
