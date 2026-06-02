# Team and Culture

How game design work is organized and practiced within teams — roles, collaboration dynamics, communication structures, and the culture that makes or breaks development. Games are almost always team efforts, and understanding how teams work is inseparable from understanding how good games get made.

---

## Core team roles (s009, ch.8; s006; s003)

Modern game development distributes responsibilities across specialized roles. The core creative disciplines:

### Game designer
Responsible for mechanics, systems, balance, and the interactive experience. Designs the rules, the core loop, and the formal structure. May also design levels, quests, or missions (or those may be separate roles).

### Level designer
Responsible for the spatial implementation of game design — creating the environments, encounters, and sequences through which players experience the mechanics. (s003, s012) → [[../../level-design/level-design]]

### Programmer / engineer
Implements the design in code. Technical decisions have direct design consequences — the performance budget, the tooling, and the physics simulation all constrain and enable what the design can do.

### Artist / art director
Responsible for visual identity, character design, environment art, and the aesthetic experience. Art decisions shape player psychology and indirect control. (s003) → [[../../narrative/indirect-control]]

### Producer
Responsible for project management — scope, schedule, budget, and team coordination. The producer mediates between creative vision and production reality.

### Sound designer / composer
Responsible for the audio experience. Sound is the fastest emotional channel and a primary indirect control tool. → [[../../narrative/indirect-control]]

**The critical point (Kremers, s012)**: roles are increasingly specialized and distributed. A single person can rarely cover all disciplines on a professional game. Understanding which role owns which decisions — and respecting those boundaries — is a production competency.

---

## Game design within the team (s009, ch.8; s005)

The game designer's relationship to the rest of the team is unique: every discipline's decisions affect the design, and the designer's decisions affect every discipline.

Key tensions:
- **Engineering vs. design**: the designer wants things; the engineer implements them. "This is technically difficult" is a design constraint that must be respected; "this can't be done" is often negotiable with creative problem-solving.
- **Art vs. design**: visual direction and game feel are deeply connected but sometimes pull in different directions. Art that makes enemies less readable (for aesthetic reasons) may damage gameplay clarity.
- **Producer vs. designer**: every feature a designer wants takes time the producer must find. The designer who cannot scope and prioritize creates production risk. "Cutting with craft" — finding the smallest version of a good idea — is a professional design skill.

> "A bad game cannot be saved by good level design. Bad level design can ruin a good game." (s012) — the same applies across all disciplines.

---

## Communication and alignment (s009, ch.8; s005)

### The shared vision problem
Every person on a team has a mental model of what the game is. These models diverge over time unless actively aligned. Documentation, regular syncs, and shared artifacts (prototype builds, reference boards) keep the models converging.

### Decision-making clarity
Who has final say on which decisions? Design by committee produces compromised work. Effective teams have clear decision authority:
- One person owns the creative vision (often the creative director or lead designer)
- That person's decisions are final on design questions
- Other roles own their domains (art director on visuals, lead engineer on architecture)

### Critique culture
The ability to give and receive design critique is a professional skill. Good critique:
- Targets the work, not the person
- Is specific: "the jump feels floaty" is actionable; "this isn't fun" is not
- Offers alternatives when possible: "what if the jump had more snappiness on landing?"
- Separates observation from solution: describe the problem before proposing the fix

Macklin & Sharp (s009) specifically address team agreements for managing disagreement:
- Establish ground rules for critique at the start of the project
- Distinguish between "I don't like this" (preference) and "this doesn't serve our design values" (design argument)
- Design values as arbitration: when the team disagrees, the design values are the tiebreaker

---

## The designer's role in production (s005, ch.23; s009)

### Pre-production
The designer's most intensive phase: defining what the game is, validating the core experience, and creating enough documentation for the team to build. The goal of pre-production is to reduce risk before the expensive production phase begins.

Schell's principle: **don't go into full production until the core is proven**. A successful pre-production deliverable: a polished slice of the game that demonstrates the core experience works. If the core isn't fun in pre-production, it won't be fun in the full game. (Cerny's Method, s005, ch.7)

### Production
The designer's role shifts to maintaining design coherence as the team builds. Key activities:
- **Triaging new ideas**: production always generates new ideas; the designer must decide which serve the vision and which are scope creep
- **Monitoring for design drift**: as other disciplines build, small decisions can accumulate into unintended design changes
- **Regular playtesting**: production should include regular internal playtests to catch problems before they become embedded in final content
- **Communicating changes**: when the design changes (and it will), communicating clearly and quickly prevents teams from building around outdated specs

### Post-production / polish
The designer focuses on quality pass — ensuring everything that shipped is as good as it can be. In practice, this phase reveals scope problems from earlier phases. The designer who scoped correctly has time to polish; the designer who didn't is cutting features.

---

## Team size and structure (s009; s005)

### Small teams (1–10 people)
Advantages: fast iteration, direct communication, full-stack ownership. Every member sees the whole game. Design decisions can be made quickly.

Disadvantages: no specialization depth; each person covers multiple disciplines, reducing mastery in any one area. Scope must be minimal to match team capacity.

**Indie game design**: most of the books in this wiki were written with small-team or individual design in mind. The iterative, player-centered process is even more critical for small teams, where there is no room for large structural mistakes.

### Large teams (50–500+ people)
Advantages: specialization depth; parallel development across disciplines; ability to build large-scope games.

Disadvantages: communication overhead grows with team size; design coherence is harder to maintain; decisions take longer; culture becomes a critical variable.

**Conway's Law**: organizations tend to produce systems that mirror their communication structures. A team organized in silos produces a game that feels siloed. Cross-discipline communication is a production investment, not a distraction.

---

## Culture and sustainability (s005, s009)

Game development has a documented history of **crunch** — unsustainable work hours that damage developer health and, paradoxically, game quality (fatigued workers make poor creative decisions and produce more bugs).

The design perspective on culture:
- **Sustainable pace produces better games**: games made under chronic crunch have more bugs, more design inconsistencies, and higher post-ship debt than games made sustainably
- **Psychological safety**: teams where it's safe to raise problems early catch design issues before they become expensive. Cultures that punish bad news create games full of known-bad-news nobody raised.
- **Creative diversity**: games made by homogeneous teams tend to solve design problems with solutions that worked for that team before. Diverse teams (by background, playing style, and experience) catch more design issues and generate more creative solutions.

---

## Key concepts & cross-links

- [[iterative-design]] — the team's production cycle
- [[playtesting]] — team-run playtesting
- [[documentation]] — the team's communication artifacts
- [[../../level-design/level-design]] — Kremers' coverage of level designer role within teams
- [[../../player/player-types]] — understanding the team's audience requires knowing who plays

## Sources

s009 ch.8 (Macklin & Sharp — collaboration, team agreements, communication, critique culture) · s005 ch.23 (Schell — teams and leadership) · s006 (Adams — production roles, game design in professional context) · s012 (Kremers — level designer role, level design specialization trends, common production problems) · s003 (Hourences — level design as profession, team dynamics)
