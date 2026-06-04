---
id: s019
title: "The Door Problem"
author: Liz England
year: 2014
type: blog
link: https://lizengland.com/blog/2014/04/the-door-problem/
republished: https://www.gamedeveloper.com/design/-quot-the-door-problem-quot-of-game-design
topics: [game-design-role, production, team-structure, design-process, interdisciplinary]
---

## Summary

"Game designer" is hard to explain because design is cross-cutting — it touches every discipline. England illustrates this by taking a single unremarkable game object (a door) and deriving the cascade of questions and responsibilities it generates for every role on a production team. The punchline: the player never notices the door. Successful design is invisible.

## Key claims

- The game designer's job is not to do all of these things, but to own the answers to the questions they raise across every discipline. (s019)
- Every game object generates decisions that span: creative direction, design, art (concept, environment, lighting), animation, sound, music, writing, programming (gameplay, AI, network), level design, UI, combat design, QA, and localization. (s019)
- The designer's primary output is the *document* — not the art, not the code, but the spec that everyone else implements against. (s019)
- Successful design is invisible: the player who walks through a well-designed door never registers the door. (s019)
- "SOMEONE has to solve The Door Problem, and that someone is a designer." (s019)

## Detailed notes

### The framing pivot

England opens by refusing the question "what does a game designer do?" She replaces it with: "Are there doors in your game?" From this single object she derives why the question is hard to answer.

### The cascade of design questions from one door

- Can the player open every door, or are some decorative? How does the player tell the difference?
- Can doors be locked and unlocked? How does the player know which state a door is in?
- Does the player know *how* to unlock a locked door?
- What if a co-op partner opens a door — does it open for both players?
- How large do doors need to be? (Depends on what can walk through them — including enemies.)
- Can enemies open doors? Should they? Will they chase the player through a door?

Each question has a downstream owner: the AI programmer needs to know if enemies pathfind through doors; the network programmer needs to know if door state is replicated; the lighting designer needs to know which color signals locked vs. unlocked.

### The Door Problem by role

England runs the question through every studio role verbatim:

- **Creative Director:** "Yes, we definitely need doors in this game."
- **Designer:** "I wrote a doc explaining what we need doors to do."
- **Concept Artist:** "I made some gorgeous paintings of doors."
- **Environment Artist:** "I took this painting of a door and made it into an object in the game."
- **Animator:** "I made the door open and close."
- **Sound Designer:** "I made the sounds the door creates when it opens and closes."
- **Composer:** "I created a theme song for the door."
- **Writer:** "When the door opens, the player will say, 'Hey look! The door opened!'"
- **Lighter:** "There is a bright red light over the door when it's locked, and a green one when it's opened."
- **Gameplay Programmer:** "This door asset now opens and closes based on proximity to the player."
- **AI Programmer:** "Enemies and allies now know if a door is there and whether they can go through it."
- **Network Programmer:** "Do all the players need to see the door open at the same time?"
- **Level Designer:** "I put the door in my level and locked it. After an event, I unlocked it."
- **UI Designer:** "There's now an objective marker on the door, and it has its own icon on the map."
- **Combat Designer:** "Enemies will spawn behind doors, and lay cover fire as their allies enter the room."
- **QA Tester:** "I walked to the door. I ran to the door. I jumped at the door. [I tested] all scenarios."
- **Localization:** "Door. Puerta. Porta. Porte. Tür. Dør. Deur. Drzwi. Drws. 문"
- **Player:** "I totally didn't even notice a door there."

### The invisible design principle

The Player entry is the punchline and the thesis. Every role did their work. Fifteen specialists solved their part of The Door Problem. The player walked through without noticing. That is good design — not noticed, because it worked exactly as expected.

This connects directly to Norman's affordances (s015): well-designed doors communicate their operation without conscious thought. A door that requires instructions has failed as a door.

### Why this matters for understanding the designer's role

England clarifies that the designer does not make the art, write the code, or animate the door. The designer writes the document that specifies what all those people need to know. The designer owns the answers, not the implementations.

This means design is inherently cross-cutting and coordinative. The designer's influence is measured not in their own artifacts but in how well the whole team's artifacts cohere.

## Notable quotes

- "SOMEONE has to solve The Door Problem, and that someone is a designer." — Liz England
- "I totally didn't even notice a door there." — [Player entry; the thesis in one line]

## Related wiki pages

- [[../../10-Library/notes/usability-and-hcd]] — Norman's affordances; doors as the canonical affordance example
- [[../../05-Syntheses/Production & Team Structure]] — designer's cross-cutting coordinative role
- [[../../10-Library/sources/s015-design-of-everyday-things]] — Norman on doors as the paradigm case of affordance failure/success
