# Story and Games

The relationship between narrative and interactivity — games' most contested design territory. Stories want predetermined meaning; games want player agency. Understanding the tensions and techniques for resolving them is central to narrative game design.

---

## The story/game duality (s005, ch.15)

Schell opens his narrative chapter with the wave-particle analogy:

> "With the advent of computer games, story and gameplay, two age-old enterprises with very different sets of rules, show a similar duality. Storytellers are now faced with a medium where they cannot be certain what path their story will take." (s005, ch.15)

Historically:
- Stories are **single-threaded, authored experiences** — the author controls what happens, in what order, to what effect
- Games are **multi-outcome experiences** — the player's choices determine what happens

Single-player computer games combined both for the first time, producing something neither pure story nor pure game: experiences with elements of both. The field has been working out the implications ever since.

---

## The myth of passive entertainment (s005, ch.15)

A common misconception: that non-interactive stories are "passive" and interactive games are "active," and therefore the narrative techniques of traditional storytelling don't apply to games.

Schell's rebuttal: **all storytelling engages the audience actively**. A well-told story — whether read, watched, or played — compels its audience to:
- Predict what will happen next
- Question what the characters should do
- Feel emotionally invested in outcomes

> "A poorly told story doesn't compel the listener to think and make decisions during the telling." (s005, ch.15)

The difference between interactive and non-interactive storytelling is not whether the audience makes decisions, but whether they can **take action** on those decisions. A skilled storyteller already creates the desire to act — an interactive designer gives the audience the ability to act on that desire.

**Design implication**: game designers should learn from traditional storytelling. The principles of narrative structure (setup, conflict, escalation, climax, resolution), character motivation, thematic resonance, and emotional pacing all apply to games, even though the delivery mechanism differs.

---

## Three narrative approaches in games (s005, ch.15)

### 1. String of pearls
A linear story is presented, with gameplay as the string connecting story moments (pearls). The player has agency within gameplay sections but the narrative path is predetermined.

Examples: most cinematic action games (Uncharted, God of War, The Last of Us). The story is authored; the gameplay delivers it. Advantages: strong narrative control, reliable pacing, cinematic quality. Disadvantages: player choice has no narrative impact.

### 2. Story machine
The game's mechanics generate narrative as a byproduct of play. No authored story exists; the player's actions produce story-like sequences that the player narrates to themselves (or others).

Examples: emergent narrative games (Dwarf Fortress, RimWorld, Crusader Kings). The mechanics are a story generator. Advantages: infinite narrative variety, deep player investment in "their" story. Disadvantages: no narrative coherence guaranteed; can produce absurd or hollow narratives.

### 3. Branching / choice-based
The player makes explicit choices that affect the story's direction. The designer authors multiple possible story branches.

Examples: RPGs with dialogue trees (Mass Effect, Disco Elysium), visual novels. Advantages: player agency feels directly narratively meaningful. Disadvantages: exponential content cost; choices often converge to minimize branching ("illusion of choice").

> ⭐ **The tension**: all three approaches struggle with the core problem that *what makes a good story* (conflict, consequence, rising stakes, satisfying resolution) often conflicts with *what makes good gameplay* (player agency, reversible decisions, restartability). Resolving this tension is the central problem of narrative game design.

---

## Ludonarrative dissonance

**Ludonarrative dissonance** (a term popularized by Halo lead designer Clint Hocking, 2007) describes the conflict when a game's mechanics and its narrative contradict each other:

- In *Bioshock*: the game's narrative asserts the player character is a slave to his programming; but the game mechanics give the player full autonomy. The story says "you have no choice"; the gameplay says "you have total choice."
- In many violent games: the story frames the protagonist as a reluctant hero; the mechanics reward gratuitous violence. The player creates a narrative divergent from the authored one.

Ludonarrative dissonance breaks the player's engagement with the story by exposing the constructed nature of the experience — the mechanics and the narrative are "lying" to each other. (s005 ch.15 framing; Kremers s012)

**Avoiding it**: the game's mechanics should reinforce rather than contradict its narrative claims. If the story says the protagonist is fragile and cautious, the mechanics should make cautious play rewarding and reckless play costly.

---

## Embedded vs. emergent narrative (s013)

Salen & Zimmerman distinguish two types of game narrative:

**Embedded narrative**: the pre-authored story elements created by the designer — cutscenes, dialogue, environmental storytelling, worldbuilding. This is narrative the designer controls.

**Emergent narrative**: stories that arise from gameplay itself — the player's sequence of meaningful choices and experiences that form a narrative in their mind. This is narrative the designer enables but does not author.

Good narrative game design works at both levels:
- Strong embedded narrative gives context, motivation, and emotional stakes
- Strong emergent narrative makes the player's choices feel meaningful and personal
- The two levels should reinforce each other: the embedded story should make the player want to make the kinds of choices that produce good emergent narratives

---

## Story and formal elements (s013, s008, s002)

Every game tells some kind of story through its formal elements:
- **Premise** (Fullerton's dramatic element): the fictional frame that makes mechanics meaningful. Chess has a thin premise (medieval warfare) that is enough to make the abstract mechanics feel like something. (s008, s005)
- **Verbs as narrative** (Anthropy & Clark, s002): the actions available to the player are the game's narrative vocabulary. A game where the only verb is "shoot" tells a story about shooting. Expanding the verb set expands the narrative palette.
- **Rules as argument** / procedural rhetoric (Fernández-Vara, s010): the game's rules make implicit claims about how the world works. A game where economic growth always brings happiness argues something about economics. → [[../../theory/meaningful-play]]

---

## Practical principles for story-game integration (s005, s012)

1. **Theme before story**: establish the emotional/thematic core first; let story and mechanics both serve it (s005, ch.5 on theme and resonance)
2. **Show story through play**: deliver narrative through gameplay moments, not just cutscenes. The player should feel the story, not just watch it.
3. **Match mechanical stakes to narrative stakes**: if the story says something important is at risk, the mechanics should make the player feel that risk
4. **Don't interrupt play for story**: tutorial popups during action fail because they interrupt the magic circle. Story beats delivered during natural pauses (level completion, safe rooms) work better.
5. **Give the player narrative ownership**: let the player feel their choices shaped the story, even when the major story beats are authored

---

## The dream of full interactivity — and why it hasn't arrived (s005, ch.15)

A recurring fantasy in game design: a fully interactive story tree where every choice matters, dozens of satisfying endings exist, and the player has complete narrative freedom while experiencing a great story. Schell identifies **5 structural problems** that prevent this dream from being realized — not due to laziness or conservatism, but due to genuine design constraints.

### Problem 1: Good stories have unity
The deepest issue. A great story is crafted as a whole — its beginning and ending are of a piece. The wretchedness of Cinderella's situation is carefully designed so that her dramatic escape can be as satisfying as it is. If Cinderella could leave in chapter 2 and get a job as an administrative assistant, there is no Cinderella story — there's just a sequence of events.

> "To craft a story with twenty endings and one beginning that is the perfect beginning for each of the twenty is challenging, to say the least. As a result, most interactive stories with many branching paths end up feeling kind of watery, weak, and disconnected." (s005, ch.15)

Unity is why the string-of-pearls method (predetermined story + free gameplay) dominates commercial game design: it guarantees unity while still providing interactivity.

### Problem 2: The combinatorial explosion
A story with 3 choices at each decision point that is 10 choices deep requires **88,573 unique outcomes**. A 20-choice-deep story with 3 branches each requires **5,230,176,601 outcomes**. This is geometrically impossible to author within human lifespans.

The standard solution — funneling branches back together — produces the "illusion of choice" problem: the player has "choices" but most paths lead to the same outcome. Players feel the seams and the illusion fails.

### Problem 3: Multiple endings, one beginning
A story with a perfect beginning has a specific perfect ending. The reverse is not true: a story with twenty possible endings does not necessarily have a beginning that makes each one feel earned. Most branching narratives sacrifice narrative satisfaction at the cost of apparent freedom.

### Problem 4: Game actions undermine story
In a game, players can do things a good story would never allow. They can die and retry. They can play the same scene differently twice. They can exploit mechanics in ways the narrative didn't anticipate. Every game action that the story must account for adds exponentially to the design cost — and every game action the story ignores produces ludonarrative dissonance.

### Problem 5: Dramatic control is the storyteller's primary tool
A skilled storyteller controls what happens, when, and with what emotional weight. Games give that control to the player. The more freedom the player has, the less dramatic control the author has. This is not a solvable problem — it is the fundamental nature of the medium.

**What actually works (the 99%):** Schell observes that the string of pearls and the story machine together account for essentially all successful interactive narratives. The string of pearls gives narrative control; the story machine gives genuine emergence. Everything in between is a difficult, partially-solved problem.

---

## Traditional storytelling techniques applied to games (s005, ch.15)

Despite the tension, traditional storytelling principles are **directly applicable** to game narrative — because the human psychological response to story doesn't change based on medium.

A skilled storyteller knows:
- When to create the desire to act (and when not to fulfill it yet)
- How to use the interest curve (hook → escalation → climax → resolution)
- How to create emotional investment through character
- How to use setting to establish tone and meaning
- How to pace revelation — what information to reveal and when

All of these apply to games. The difference is that in games, the player can act on the desires the story creates. This makes the storyteller's job **harder** (more variables to manage), not fundamentally different.

> "While interactive storytelling is more challenging than traditional storytelling, by no means is it fundamentally different. Game designers are well-served to learn all they can about traditional storytelling techniques." (s005, ch.15)

**The key implication:** game designers who dismiss traditional storytelling as "not applicable" to games are making a strategic error. The field of traditional narrative — from Aristotle to screenwriting — is a usable toolkit for game narrative design, requiring adaptation but not replacement.

---

## The Lens #65: Story Machine (s005, ch.15)

To make a game a better story generator:
- When players have different choices about how to achieve goals, new and different stories arise. How can more of these choices be added?
- Different conflicts lead to different stories. How can the game allow more types of conflict to arise?
- When players can personalize characters and setting, they care more about story outcomes. How can the story be personalized?
- Good stories have good interest curves. Do the game's rules lead to stories with good interest curves?
- A story is only good if you can tell it. Who can players tell their story to that will actually care?

---



- [[indirect-control]] — Schell's 6 methods for guiding players through narrative spaces
- [[world-building]] — constructing a consistent fictional world
- [[characters]] — player characters, NPCs, and narrative identification
- [[../../level-design/level-design]] — levels as the primary story delivery mechanism
- [[../../theory/meaningful-play]] — player actions must have discernable, integrated narrative consequences
- [[../../mechanics/core-mechanics]] — Anthropy's verbs as narrative
- [[../../player/player-psychology]] — empathy, imagination, and emotional response to narrative
- [[../../level-design/pacing-and-flow]] — interest curves apply to narrative arcs

## Sources

s005 ch.15 (Schell — story/game duality, myth of passive entertainment, string of pearls, lenses) · s012 ch.12 (Kremers — story and narrative in level design) · s013 (Salen & Zimmerman — embedded vs emergent narrative, three schemas) · s008 (Fullerton — dramatic elements including premise, character, story) · s002 (Anthropy & Clark — verbs as narrative vocabulary, games as expressive medium) · s010 (Fernández-Vara — procedural rhetoric, diegetic/non-diegetic, narrative analysis)
