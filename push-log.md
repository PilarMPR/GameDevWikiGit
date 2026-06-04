# Push Log

---

## 2026-06-04 — main → origin/main

### What changed
- Ingested s018–s025: 8 non-PDF sources (game design talks and blog posts) including Juice It or Lose It, The Door Problem, Designing Celeste, 30 Things I Hate About Your Pitch, Into the Breach postmortem, Spelunky DNA, Shovel Knight: Designing by Accident, Thief Dark Project postmortem
- Cross-references added to 4 synthesis pages (Movement/Controls/Game Feel; Production/Documentation; Iteration/Playtesting; Cybernetics/Complexity)
- Ingested s026: *Game Programming Algorithms and Techniques* by Sanjay Madhav (2014) — the wiki's first programming textbook; source page + cross-refs in Cybernetics synthesis and game-loops-definition note
- Hot Potato movement GDD update: acceleration curve revised (linear, no gradient), slope/uphill response clarified, two new camera effects added (camera shake on tag, camera arm height gain)

### Wins
- Wiki curator handled all cross-referencing autonomously; no manual fixes needed
- Diverged branch resolved cleanly via rebase before push (14 local commits replayed on top of 4 remote commits)
- Secrets scrub was fast; only false-positive was the word "token" in a compiler discussion

### Mistakes / friction
- Branches had diverged (14 local vs 4 remote) before push — accumulated across several sessions without syncing; required a pull --rebase step
- Push on the previous attempt was blocked because we hadn't committed the pending changes first

### Lessons
- Sync (pull) at the start of every session, not just before push
- One commit per logical batch (wiki ingest vs GDD update) would give cleaner history — bundle only when both are ready at the same time
