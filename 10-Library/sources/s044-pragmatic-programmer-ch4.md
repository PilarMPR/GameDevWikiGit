---
id: s044
title: "The Pragmatic Programmer (Ch.4: Pragmatic Paranoia) — 20th Anniversary Edition"
author: Dave Thomas, Andy Hunt
year: 2020
type: chapter-excerpt
tags: [programming, software-engineering, defensive-programming, dbc, assertions, best-practices]
---
# s044 · The Pragmatic Programmer — Ch.4: Pragmatic Paranoia

**Full title:** *The Pragmatic Programmer: Your Journey to Mastery, 20th Anniversary Edition* — **Chapter 4: Pragmatic Paranoia** · **Authors:** Dave Thomas & Andy Hunt · **Year:** 2020 (© Pearson Education, ISBN 978-0-13-595705-9) · **Publisher:** Addison-Wesley Professional

> **Provenance note:** This is a single-chapter excerpt (Chapter 4 only, Topics 23–27), not the full book. The full book spans 9 chapters and 53 numbered Topics. Cite as `(s044, Pragmatic Programmer ch.4)`.

## Summary

Chapter 4 argues that pragmatic programmers must defend against their *own* mistakes, not just external bad inputs. It presents four defensive programming techniques: Design by Contract (preconditions/postconditions/invariants), crashing early rather than propagating corrupt state, assertive programming (assertions as live documentation), and resource balancing (the allocator must deallocate). The chapter's framing is: "You Can't Write Perfect Software" — accept this, then build systematic defenses. (s044, Pragmatic Programmer ch.4)

## Key claims & concepts

### Tip 36: You Can't Write Perfect Software
- Perfect software does not exist. Accepting this allows pragmatic programmers to build in *defenses against their own mistakes*, not just external ones. (s044, ch.4 intro)

### Topic 23: Design by Contract (DBC)
- Concept originated by Bertrand Meyer for the Eiffel language; formalized from Dijkstra/Floyd/Hoare/Wirth prior work.
- Three components of a function's contract:
  - **Preconditions:** what must be true before the routine is called (caller's responsibility).
  - **Postconditions:** what the routine guarantees upon completion (implies termination — no infinite loops).
  - **Class invariants:** conditions the class guarantees are always true from the caller's perspective.
- DBC vs. testing: DBC defines success/failure for *all cases*; TDD tests one specific case at a time. DBC is active during design, development, deployment, and maintenance — not just at test time.
- "Be strict in what you will accept before you begin, and promise as little as possible in return." — Tip 37: Design with Contracts. (s044, ch.4 T23)
- **Semantic invariants:** fixed, inviolate requirements that become core to the system's meaning (e.g., "err in favor of the consumer" in a debit transaction system). (s044, ch.4 T23)
- DBC can be partial in languages without native support — put the contract in comments or unit tests. In Clojure: `:pre`/`:post` maps. In Elixir: guard clauses.

### Topic 24: Dead Programs Tell No Lies
- All errors give information; never convince yourself an error "can't happen."
- **Tip 38: Crash Early** — crashing as soon as a problem is detected is better than continuing with corrupted state. "A dead program normally does a lot less damage than a crippled one."
- Erlang/Elixir embrace "let it crash" philosophy with supervisor trees for fault-tolerant systems.
- "Catch and release is for fish" — re-raising exceptions without fixing the root cause adds complexity and coupling. (s044, ch.4 T24)

### Topic 25: Assertive Programming
- **Tip 39: Use Assertions to Prevent the Impossible** — whenever you think "this can never happen," add code to check it.
- Do NOT use assertions as a substitute for real error handling (e.g., validating user input).
- Beware Heisenbugs from assertions with side effects.
- **Leave assertions turned on in production.** The argument "testing found all the bugs, so we can disable assertions" rests on two false assumptions: that testing covers all permutations, and that production is like the test environment. "Turning off assertions when you deliver a program to production is like crossing a high wire without a net." (s044, ch.4 T25)

### Topic 26: How to Balance Resources
- **Tip 40: Finish What You Start** — the function/object that allocates a resource should deallocate it.
- **Tip 41: Act Locally** — use scoped resource lifetimes (Rust's ownership model; Ruby's block-scoped `File.open do...end`; C++ RAII).
- Nested allocation rules: deallocate in reverse order; always allocate same resources in the same order across call sites (prevents deadlock).
- Exception antipattern: allocating before a `begin...finally` block — if allocation fails, `finally` tries to deallocate something that was never allocated. Correct: allocate before `begin`, deallocate in `finally`. (s044, ch.4 T26)

### Topic 27: Don't Outrun Your Headlights
- (Referenced in chapter intro but not in the extracted pages — content not available in this excerpt.)

## Connections to wiki

- **Game programming relevance:** DBC and assertions are directly applicable to game engine code — preconditions on component initialization, invariants on game state (e.g., "health is always in [0, maxHealth]"), postconditions on physics/collision resolution. See [[s026-game-programming-algorithms-and-techniques|s026 Madhav]] and [[s030-game-programming-in-cpp-madhav|s030 Game Programming in C++]] for game-specific patterns.
- **Crashes vs. silent corruption in games:** The "crash early" principle directly applies to game server code and multiplayer state synchronization discussed in [[s031-multiplayer-game-programming|s031 Glazer & Madhav]] — corrupted game state propagates across the network and is extremely difficult to debug.
- **Testing integration:** The DBC vs. TDD comparison adds nuance to the testing approach described in [[s036-agile-game-development-keith|s036 Agile Game Development (Keith)]]'s QA sections.
- **Resource balancing in game engines:** The allocator-must-deallocate pattern is the C++ RAII principle underlying smart pointer usage in game engine code ([[s030-game-programming-in-cpp-madhav|s030]]) and the Object Pool pattern in [[s029-game-programming-patterns-nystrom|s029 Game Programming Patterns]].

## Notable quotes

- "Perfect software doesn't exist. No one in the brief history of computing has ever written a piece of perfect software." (Tip 36)
- "All errors give you information. You could convince yourself that the error can't happen, and choose to ignore it. Instead, Pragmatic Programmers tell themselves that if there is an error, something very, very bad has happened." (T24)
- "Turning off assertions when you deliver a program to production is like crossing a high wire without a net because you once made it across in practice." (T25)
- "A dead program normally does a lot less damage than a crippled one." (T24)
