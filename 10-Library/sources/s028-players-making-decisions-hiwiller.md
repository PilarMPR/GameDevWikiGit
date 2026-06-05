---
id: s028
title: "Players Making Decisions: Game Design Essentials and the Art of Understanding Your Players"
author: Zack Hiwiller
year: 2016
type: book
tags: [game-dev, game-design, decision-making, game-theory, psychology, balance, playtesting]
sources: [s028]
---

# s028 · Players Making Decisions (Hiwiller)

**Full title:** Players Making Decisions: Game Design Essentials and the Art of Understanding Your Players
**Author:** Zack Hiwiller | **Year:** 2016 | **Publisher:** New Riders (Pearson/Peachpit)
**Type:** Book | **Pages:** ~481

## Summary

A rigorous, interdisciplinary textbook covering game design through the lens of decision theory, game theory, cognitive psychology, and behaviorism. Hiwiller (chair of the Game Design program at Full Sail University) argues that the designer's core job is to create meaningful decisions for players, and then systematically draws on economics, psychology, and mathematics to build a toolkit for doing so. The book is unusual in the canon for its depth on formal game theory (Nash equilibria, dominant strategies, zero-sum analysis), probability, Monte Carlo simulation, and cognitive biases — making it the most analytically rigorous game design textbook in the wiki. Organized into seven parts: Getting Started; Prototypes and Playtesting; Meaningful Decisions; Describing Game Elements; Game Theory and Rational Decision-Making; Human Behavior in Games; Game Design Tools.

## Key claims & concepts

- **The Fundamental Game Design Directive**: create meaningful decisions for players; flow and interest curves are the pacing tools that keep players in that decision-making sweet spot. (s028, ch.9)
- **Anatomy of a Choice**: less-interesting decisions are dominated (one option is always better), trivial (no stakes), or obvious; more-interesting decisions involve trade-offs, uncertainty, and player agency. (s028, ch.10)
- **MDA in Practice**: Hiwiller extends MDA (Hunicke/LeBlanc/Zubek, s011) with a "More Dynamics" section and applies it to analyze feedback loops and emergent behavior. (s028, ch.13)
- **Milieu** is Hiwiller's term for the aesthetic/presentation layer — polish, player types, and motivation as design inputs distinct from mechanics. (s028, ch.14)
- **Feedback loop taxonomy**: positive loops amplify leads (snowball effect); negative loops compress outcomes (rubber-banding); both can be designed intentionally. (s028, ch.17)
- **Game theory for designers**: Nash equilibria, dominant strategy elimination, zero-sum vs. non-zero-sum games, Prisoner's Dilemma, Stag Hunt — applied directly to game balance. (s028, ch.19-21)
- **Rational actor problem**: real players are not rational; cognitive biases (anchoring, loss aversion, misreading randomness, attribution errors) predictably distort decisions. (s028, ch.26)
- **Behaviorism and reward schedules**: operant conditioning, variable-ratio reinforcement as the most powerful engagement driver; ethical concerns with manipulative design. (s028, ch.23)
- **Cognitive load and learning**: novice/expert distinction, split-attention effect, expertise reversal effect — tutorial design must account for these. (s028, ch.24)
- **Quantitative tools**: probability calculations, spreadsheet simulation, Monte Carlo methods for testing design hypotheses before implementation. (s028, ch.29-31)

## Chapter overview

| Part | Ch | Title | Key topics |
|------|-----|-------|-----------|
| 1 | 1 | What Is a Game Designer? | Responsibilities; attributes; formalism vs. ontology |
| 1 | 2 | Problem Statements | Defining the design problem; brainstorming; functional fixedness |
| 1 | 3 | Development Structures | Production methodologies; scope management |
| 1 | 4 | Starting Practices | Analog prototyping; theme and mechanics; designing for others |
| 2 | 5 | Paper Prototyping | Software and materials; card design; InDesign data merge |
| 2 | 6 | Playtesting | Goals; benefits; listening to feedback; finding playtesters |
| 2 | 7 | Playtesting Methods | Testing environment; think-aloud; A/B testing; self-playtesting |
| 2 | 8 | Prototypes and IP | NDAs; ideas and value |
| 3 | 9 | Flow and the Fundamental Game Design Directive | Csikszentmihalyi flow; interest curves; learning curves; individual differences |
| 3 | 10 | Decision-Making | Player agency; anatomy of a choice; less- and more-interesting decisions |
| 3 | 11 | Randomness | Skill vs. luck spectrum; fairness; mitigating randomness |
| 3 | 12 | Goals | How players determine goals; criteria for effective goals; solving goal problems |
| 4 | 13 | MDA | MDA framework; dynamics taxonomy; feedback loops in play |
| 4 | 14 | Milieu | Polish; player types; motivation; milieu as design focus |
| 4 | 15 | Rules and Verbs | Rule qualities and types; verbs as design vocabulary |
| 4 | 16 | Balance | Symmetry; self-balancing mechanisms; progression and numeric relationships |
| 4 | 17 | Feedback Loops | Positive loops; negative loops; fixing imbalance |
| 4 | 18 | Puzzle Design | Puzzle definition; possibility space; breadcrumbs; ineffective puzzle features |
| 5 | 19 | Equilibria in Normal Form Games | Prisoner's Dilemma; dominant strategies; zero-sum games; Nash equilibria |
| 5 | 20 | Sequential and Other Games | Extensive form; backward induction; repeated games |
| 5 | 21 | Problems with Game Theory | Rationality assumptions; Dollar Auction; Guess Two-Thirds |
| 5 | 22 | Marginal Decision Analysis | Marginal utility; balancing on margins |
| 6 | 23 | Behaviorism and Schedules of Reinforcement | Operant conditioning; variable-ratio schedules; ethical concerns |
| 6 | 24 | Learning and Constructivism | Novice/expert; cognitive load; expertise reversal; tutorial design |
| 6 | 25 | Motivation | Intrinsic/extrinsic; self-determination theory; competition; personality |
| 6 | 26 | Human Decision-Making | Cognitive biases; attribution errors; loss aversion; anchoring; framing |
| 6 | 27 | Attention and Memory | Attention; working/long-term memory; perception |
| 7 | 28 | Documentation | GDD; flowcharts; documentation for tabletop games |
| 7 | 29 | Probability | Counting; die rolls; practical probability for designers |
| 7 | 30 | Spreadsheets | Simulation tools; Excel Goal Seek/Solver |
| 7 | 31 | Monte Carlo Simulation | Design question testing; Hot Hand; Monty Hall |
| 7 | 32 | Presenting Ideas | Pitching; communication strategies |

## Connections to wiki

- **MDA**: ch.13 directly extends [[../../wiki/concepts/theory/mda-framework]] and [[../../10-Library/sources/s011-mda-framework]]. Hiwiller adds dynamics taxonomy and practical loop analysis.
- **Flow and interest curves**: ch.9 aligns with [[../../wiki/concepts/player/flow-channel]] (Csikszentmihalyi flow, Koster's learnable middle). Hiwiller adds the "learning curves" dimension missing from Schell (s005).
- **Decision-making**: ch.10 is the most rigorous treatment of Sid Meier's "interesting decisions" maxim in the wiki. Connects to [[../../wiki/concepts/mechanics/game-balance]] and [[../../wiki/concepts/mechanics/emergence]].
- **Feedback loops**: ch.17 extends [[../../wiki/concepts/mechanics/game-loops]] with rubber-band mechanics; connects to [[../../wiki/concepts/mechanics/game-balance]].
- **Behaviorism / reward schedules**: ch.23 deepens [[../../wiki/concepts/player/motivation]] (variable-ratio = most powerful reward schedule). Important ethical dimension for F2P analysis [[../../wiki/concepts/business/free-to-play-design]].
- **Cognitive load and learning**: ch.24 bridges to [[../../wiki/concepts/player/player-psychology]] and [[../../wiki/concepts/interface/ui-design]] (tutorial design, cognitive load reduction).
- **Probability + simulation tools**: chs.29-31 are unique in the canon — no other wiki source covers quantitative design simulation. Candidate for a new `wiki/concepts/production/quantitative-design.md` note.
- **Game theory**: chs.19-22 are unique — formal game theory applied to balance design. Connects to [[../../wiki/concepts/mechanics/game-balance]] (transitive/intransitive systems).
- **Human decision biases**: ch.26 connects to [[../../wiki/concepts/player/player-psychology]] and adds loss aversion/anchoring not covered elsewhere. Bridges to Norman (s015) on mental models.

## Notable quotes

- "The fundamental game design directive: create meaningful decisions for players." (s028, ch.9)
- "A dominated strategy is never interesting because a rational player would never choose it." (s028, ch.10)
- "Variable-ratio schedules of reinforcement are the most effective for maintaining behavior — and raise the most ethical concerns in game design." (s028, ch.23)
