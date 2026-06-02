# s005 · Ch.10 — Some Elements are Game Mechanics

**Book:** [[../../sources/s005-art-of-game-design|The Art of Game Design (Schell)]] · **PDF pp. 129–169**
· **Lenses:** **#21 Functional Space, #22 Dynamic State, #23 Emergence, #24 Action, #25 Goals,
#26 Rules, #27 Skill, #28 Expected Value, #29 Chance** · **Prev:** [[ch09-the-experience-is-in-the-players-mind]]
· **Next:** [[ch11-game-mechanics-must-be-in-balance]]

## Chapter summary
The "nuts and bolts." **Mechanics are the interactions and relationships that remain when
aesthetics, technology, and story are stripped away** — the core of what a game *is*. Schell's
taxonomy has **six categories: Space, Objects/Attributes/States, Actions, Rules, Skill, Chance**,
each with its own lens. This is the densest mechanics treatment in the wiki.

> ⭐ **Central cross-book node (per the linking goal).** Schell's six mechanics ≈ MDA's
> **Mechanics** layer ([[../../concepts/mda-framework]], s011) and the **[[../../concepts/formal-elements]]**
> of Fullerton (s008) / Macklin & Sharp (s009: actions, goals, rules, objects, playspace,
> players — almost a 1:1 match) / Adams' core mechanics (s006). See [[../../concepts/game-genres-and-mechanics]].

## Mechanic 1: Space → 🔎 Lens #21 Functional Space
- The abstract, stripped-of-aesthetics space of play (the "magic circle" as geometry). Described
  by: **discrete vs continuous**, **number of dimensions**, **bounded/connected areas**.
- Examples: tic-tac-toe = 9 zero-D cells in a 2-D grid (adjacency matters); Monopoly = a 1-D
  loop of 40 points; pool table = continuous 2-D (or 3-D). **Nested spaces** ("spaces within
  spaces" — RPG overworld → town/cave icons) match our mental models. Even "Twenty Questions"
  (zero-D) has a useful space (answerer's mind / questioner's mind / conversation channel).
- Lens #21: discrete or continuous? how many dimensions? boundaries? sub-spaces & connections?
  more than one useful abstraction? Pairs with **Lens #8 Holographic Design**.

## Mechanic 2: Objects, Attributes, and States → 🔎 Lens #22 Dynamic State
- **Objects = nouns; attributes & states = adjectives.** Attributes are categories of info
  (max speed); each has a current **state** (75 mph). Static vs **dynamic** attributes (we care
  about dynamic). Use **state diagrams / state machines** (Pac-Man ghost example) to design
  complex behaviors and forbid illegal transitions. Rule of thumb: *behave the same → look the
  same; behave differently → look different.*
- **Secrets / who knows what.** Changing public vs private state radically changes a game (draw
  vs stud poker). The **"hierarchy of knowers"** Venn diagram: God (random/fate) ⊃ the Game ⊃
  players, with info shared at different levels. (The grandmother who insists the computer
  "cheats" because it knows all the cards.)
- Lens #22: objects? attributes? states & their triggers? what's known by the game only / all /
  some players? would changing who-knows-what improve the game? (Making private info suddenly
  public = drama.)

## Mechanic 3: Actions → 🔎 Lens #23 Emergence, #24 Action
- **Actions = verbs.** Two kinds: **operative actions** (the base moves) and **resultant
  actions** (strategic moves that *emerge* — protect, sacrifice, force a bad jump). **The ratio
  of resultant : operative actions measures emergence.** Elegant games: few operatives, many
  resultants.
- **Five ways to plant emergence** (Lens #23): ① add more verbs; ② verbs that act on many
  objects (one "shoot" that works on locks, windows, tires…); ③ goals achievable >1 way;
  ④ many subjects (resultants ≈ subjects × verbs × objects); ⑤ side effects that change constraints.
- "Innovative" games give new actions (*Donkey Kong* = run/jump, *Katamari* = rolling). The
  text-adventure decline reframed: too many *unclear* verbs → frustration. Lens #24: operative
  vs resultant actions; which resultants do I want; happy with the ratio; what do players wish
  they could do?
  > ⭐ Verbs ≈ Anthropy & Clark's "games speak in verbs" ([[../../concepts/game-design-vocabulary]], s002);
  > emergence ≈ Sellers' emergent **wholes** from loops ([[../../concepts/parts-loops-wholes]], s001).

## Mechanic 4: Rules → 🔎 Lens #25 Goals, #26 Rules
- **Rules are the most fundamental mechanic — "a game *is* its rules."** They define space,
  objects, actions, consequences, constraints, and goals.
- **Parlett's rule analysis:** Operational, **Foundational** (the abstract math of state),
  Behavioral (unwritten sportsmanship), Written, Laws (tournament rules — e.g. "Mokujin is
  banned"), Official, Advisory (strategy "rules"), and **House rules** (player feedback).
- **Modes** (Pitstop racing↔tire-change): signal the mode clearly; Sid Meier's rule — players
  shouldn't get so lost in a sub-game they forget the main game. **The Enforcer:** computers can
  enforce rules, enabling far more complex games (a rule becomes a physical constraint) — but
  don't overwhelm the player; rules must be *discoverable*, not memorized.
- **The Most Important Rule = the Object of the Game.** Goals should be **concrete, achievable,
  rewarding**, with a balance of short- and long-term goals (chess's real goal: "capture the
  king"). Lens #25 (goals) + Lens #26 (rules: foundational vs operational, laws/house rules,
  modes, enforcement, clarity). *Rules are arrived at gradually/experimentally; written rules
  come last.*
  > ⭐ "A game is its rules / artificial conflict toward goals" ≈ Salen & Zimmerman's game
  > definition ([[../../concepts/meaningful-play]], s013); goals/challenges ≈ Adams' hierarchy of
  > challenges ([[../../concepts/game-genres-and-mechanics]], s006).

## Mechanic 5: Skill → 🔎 Lens #27 Skill
- Skill shifts focus to the player; matching skill to difficulty keeps players in the **flow
  channel** ([[ch09-the-experience-is-in-the-players-mind]]). Three categories: **physical,
  mental, social.** Most games blend several.
- **Real vs virtual skills:** "sword-fighting skill" in an RPG is *virtual* (the real skill is
  button-pressing). Virtual skills give a feeling of power but can feel hollow; find the right
  mix. **Enumerate** your game's skills (the *RC Pro Am* grip example — you may be testing a
  different skill than you think, e.g. memorization vs reaction). Lens #27: which skills? missing
  categories? dominant skills? right level? can players improve with practice?

## Mechanic 6: Chance → 🔎 Lens #28 Expected Value, #29 Chance
- **Chance = uncertainty = surprise** (the secret ingredient of fun), and it interacts with all
  the other five mechanics. Probability was *invented for game design* (Chevalier de Méré →
  Pascal & Fermat, 1654).
- **Ten rules of probability:** ① fractions=decimals=percents; ② range 0–1; ③ P = looked-for ÷
  possible outcomes; ④ **enumerate**; ⑤ OR → add (if mutually exclusive); ⑥ AND → multiply (if
  not mutually exclusive); ⑦ **1 − "does" = "doesn't"** (the key shortcut; the Chevalier's true
  odds: game 1 ≈ 51.8% win, game 2 ≈ 49.1%); ⑧ summed random selections aren't linear (dice-sum
  bell curve; D&D 3d6 vs 1d20); ⑨ **Monte Carlo** (roll/simulate to get *practical* probability);
  ⑩ "Geeks love showing off" (Gombauld's Law — ask a math whiz).
- **Expected value** = average of all possible outcomes; the prime **balancing** tool. Watch
  *real* value (a 40-dmg lightning bolt vs a 15-HP enemy is wasted) and the **human element**:
  **regret** (Kahneman & Tversky — people prefer a sure $2400 over a higher-EV gamble) and
  **perceived vs actual probability** (people overestimate dramatic risks). Lens #28: actual vs
  perceived chance; outcome value (incl. intangibles); happy with the choices it creates?
- **Skill & chance entangle:** estimating chance is a skill; skills have a probability of
  success; estimating an opponent's skill is a skill; predicting/controlling pure chance are
  *imagined* skills (lucky-streak & gambler's fallacies — and that illusion is part of the fun).
  Lens #29: what's truly random vs feels random? does randomness excite or frustrate? tune the
  distribution curves; interesting risks? relationship between chance and skill?
  > ⭐ Probability/EV/curves → [[../../concepts/game-balance]] (transitive/intransitive, progression
  > & power curves, s001 ch.9–10); chance↔surprise↔fun → [[ch03-the-experience-rises-out-of-a-game|Lens #2]], [[../../concepts/theory-of-fun]].

## Key concepts & links
- **The mechanics hub:** [[../../concepts/formal-elements]], [[../../concepts/mda-framework]],
  [[../../concepts/game-genres-and-mechanics]].
- **Emergence/systems:** [[../../concepts/parts-loops-wholes]], [[../../concepts/systems-thinking]] (s001, s013).
- **Skill ↔ flow:** [[ch09-the-experience-is-in-the-players-mind]], [[../../concepts/game-balance]].
- **Chance/EV ↔ balance math:** [[../../concepts/game-balance]] (the next chapter, ch.11, applies it).

## Notable quotes
- *"Game mechanics are the interactions and relationships that remain when all of the aesthetics, technology, and story are stripped away."*
- *"A game is not just defined by its rules, a game IS its rules."*
- *"Risk and randomness are like spices… get them just right, and they bring out the flavor of everything else."*
