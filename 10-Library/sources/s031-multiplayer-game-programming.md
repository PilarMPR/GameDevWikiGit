---
id: s031
title: "Multiplayer Game Programming: Architecting Networked Games"
author: "Joshua Glazer, Sanjay Madhav"
year: 2016
type: book
tags: [game-dev, programming, networking, multiplayer, cpp, client-server, latency, unreal, unity]
sources: [s031]
---

# s031 · Multiplayer Game Programming (Glazer & Madhav)

**Full title:** Multiplayer Game Programming: Architecting Networked Games
**Author:** Joshua Glazer & Sanjay Madhav | **Year:** 2016 | **Publisher:** Pearson (Addison-Wesley Game Design and Development Series)
**Type:** Book | **Pages:** ~384

## Summary

A comprehensive, implementation-focused textbook on networked multiplayer game programming, developed from USC game programming coursework. The book progresses systematically from networking fundamentals (the TCP/IP stack, Berkeley sockets) through game-specific networking concerns (object serialization, replication, topologies), then to the hard problems of real-time networking (latency, jitter, packet loss), followed by scalability, security, and finally integration with commercial gamer services (Steamworks SDK) and cloud-hosted dedicated servers. Full source code for two sample games (an action game and an RTS) accompanies the book. Co-authored by Glazer (industry veteran) and Madhav (USC, also author of s026 and s030), the book explicitly builds on s026's networking introduction and assumes C++ proficiency.

## Key claims & concepts

- **The networking stack for games**: games need to understand the full TCP/IP layer cake (Physical → Link → Network → Transport → Application) to make informed protocol choices. (s031, ch.2)
- **UDP over TCP for real-time games**: TCP's reliability guarantees come at latency cost unacceptable for action games; most real-time games implement reliable delivery on top of UDP. (s031, ch.7)
- **Object serialization**: game objects must be converted to binary streams for network transmission; stream design, compression, and maintainability are the central engineering challenges. (s031, ch.4)
- **Object replication**: the server maintains authoritative world state; clients receive state updates; naive full-state broadcast is replaced by delta/dirty-bit approaches at scale. (s031, ch.5)
- **Network topologies**: client-server (authoritative server, common in modern games) vs. peer-to-peer (lockstep, used in RTS); each has distinct consistency, cheat-resistance, and latency tradeoffs. (s031, ch.6)
- **Latency mitigation trilogy**: client-side interpolation (smooth movement between received positions), client-side prediction (apply inputs locally before server confirmation), server-side rewind (lag compensation for hit detection). (s031, ch.8)
- **Jitter buffers**: absorb packet timing variance by buffering incoming data; trade added latency for smoother delivery. (s031, ch.7)
- **Scalability techniques**: object scope/relevancy (only send what's nearby), server partitioning (zones), instancing, and update prioritization/frequency tuning. (s031, ch.9)
- **Security fundamentals**: packet sniffing (encryption), input validation (server authority), cheat detection software; the server must never trust client-side claims. (s031, ch.10)
- **Gamer services (Steamworks)**: lobby/matchmaking, networking abstraction, leaderboards, achievements, player statistics — Valve's SDK as the canonical integration example. (s031, ch.12)
- **Cloud hosting dedicated servers**: cloud infrastructure overview; server process management; virtual machine managers for scaling game server fleets. (s031, ch.13)
- **Historical case studies**: Starsiege Tribes (zone-of-relevance, server-side physics) and Age of Empires (lockstep determinism) as canonical solutions to network architecture problems. (s031, ch.1)

## Chapter overview

| Ch | Title | Key topics |
|----|-------|-----------|
| 1 | Overview of Networked Games | History; Tribes (zone of relevance); Age of Empires (lockstep) |
| 2 | The Internet | TCP/IP layers; IP addressing; TCP vs UDP; NAT traversal |
| 3 | Berkeley Sockets | Socket API; UDP/TCP sockets; blocking/non-blocking I/O |
| 4 | Object Serialization | Binary streams; compression; maintainability |
| 5 | Object Replication | World state; delta replication; RPCs as serialized objects |
| 6 | Network Topologies and Sample Games | Client-server; peer-to-peer; implementation walkthrough |
| 7 | Latency, Jitter, and Reliability | RTT; jitter; packet loss; TCP vs UDP reliability; packet delivery notification |
| 8 | Improved Latency Handling | Client interpolation; client prediction; server rewind |
| 9 | Scalability | Relevancy; server partitioning; instancing; priority/frequency |
| 10 | Security | Sniffing; input validation; cheat detection; server authority |
| 11 | Real-World Engines | Unreal Engine 4 networking; Unity networking (UNET) |
| 12 | Gamer Services | Steamworks SDK; matchmaking; lobbies; statistics; achievements; leaderboards |
| 13 | Cloud Hosting Dedicated Servers | Cloud infrastructure; server process management; VM scaling |
| App A | Modern C++ Primer | C++11; references; templates; smart pointers; STL; iterators |

## Connections to wiki

- **Relationship to s026 (Madhav's first book)**: s031 expands the ch.10 networking overview in s026 into a full textbook. The preface explicitly cites s026 as prerequisite reading. Together with s030 they form the complete Madhav game programming trilogy.
- **Multiplayer game design**: s031 provides the technical architecture underpinning [[../../wiki/concepts/mechanics/multiplayer-systems]] (which covers design considerations). The two pages are complementary: design constraints (lag, cheating, authority) shape the design space.
- **Hot Potato (UE5 multiplayer)**: ch.11 covers Unreal Engine 4 networking (replication system, NetMode, RPCs) — the direct predecessor of UE5's replication model used by Hot Potato. Critical reference for networking implementation. Links to `40-HotPotato/` GDD pages.
- **Client prediction / server authority**: ch.8's latency mitigation trilogy is the technical basis for why certain gameplay mechanics are harder to implement in multiplayer (real-time physics, precise hit detection). Relevant to Hot Potato's physics-driven potato passing mechanic.
- **Lockstep vs. client-server**: ch.6's topology comparison is foundational for any multiplayer game architecture decision. Lockstep suits turn-based/RTS (determinism required); client-server suits action games (tolerance for rollback).
- **Game loops in distributed context**: ch.5-8 make clear that the game loop (s026, s029, s030) must be redesigned for networked play: the authoritative loop lives on the server while clients run predictive local loops.
- **Cybernetics and emergence**: multiplayer games are coupled systems of systems (server state + N client states); the consistency/availability/partition theorem applies. Links to [[../../05-Syntheses/Cybernetics, Complexity & Emergent Systems]].

## Notable quotes

- "Networked multiplayer games are a huge part of the games industry today. As of 2014, League of Legends boasts 67 million active players each month." (s031, preface)
- "The server must never trust the client — input validation on the server side is the most important cheat prevention." (s031, ch.10)
- "Client-side prediction allows the client to apply the local player's inputs immediately, before receiving server confirmation, to eliminate perceived input lag." (s031, ch.8)
