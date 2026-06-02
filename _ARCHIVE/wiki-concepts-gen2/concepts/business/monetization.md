# Monetization

The systems and patterns by which games generate revenue. Modern monetization is inseparable from game design — the model chosen shapes the player experience, the design incentives, and the ethical posture of the product.

---

## Revenue models overview (s006; s017)

| Model | How it works | Primary design tension |
|-------|-------------|----------------------|
| **Premium / boxed** | One-time purchase; all content included | Justify price at purchase; no recurring revenue |
| **Subscription** | Monthly/annual fee; access to library or ongoing content | Justify ongoing value; churn management |
| **Free-to-play (F2P)** | Free base game; revenue from in-app purchases | Monetize without alienating non-payers |
| **Season pass / DLC** | Premium game with paid content expansions | Balance new content vs. day-one value |
| **Battle pass** | Seasonal progression track; cosmetic rewards for play + payment | Make the track feel earnable, not mandatory |
| **Ads** | Revenue from displaying advertisements | Don't break flow; keep ads non-intrusive |

---

## Pay-to-win vs. cosmetic monetization

The single most important axis in IAP design:

**Pay-to-win**: purchasing gameplay advantages (stronger weapons, faster progression, exclusive mechanics). Creates an immediate tension:
- Players who pay have an advantage over players who don't
- Non-paying players feel the game is unfair; competitive balance is destroyed
- Paying players who paid for advantage may feel cheated if the advantage is later reduced
- Community trust is difficult to rebuild once pay-to-win is perceived

**Cosmetic monetization**: purchasing visual customization (skins, emotes, cosmetic items) with no gameplay impact. The gold standard for F2P competitive games:
- Non-paying players are not disadvantaged
- Paying players express identity and support the developer
- Community perceives the monetization as fair
- Players self-select: those for whom cosmetics matter pay; those for whom they don't, don't

> The competitive game lesson: **gameplay equity + cosmetic monetization** is the most sustainable model for games with competitive components. (s017)

---

## In-app purchases (IAP) (s017, s014)

### Currency systems
Most F2P games use a two-currency system:
- **Soft currency** (earnable through play): used for common purchases; reinforces the core loop
- **Hard currency** (purchasable with real money): used for premium purchases; the monetization layer

The two-currency system serves two purposes:
1. **Psychological**: hard currency abstracts the purchase one step from real money, reducing payment friction
2. **Design**: soft currency gives non-paying players access to most content, maintaining engagement

### Price anchoring
The first price the player sees becomes a reference point (Weber-Fechner effect; s014). F2P pricing catalogs are designed with this in mind: a prominent mid-tier bundle makes smaller purchases look cheap and larger ones look reasonable.

**Starting whale psychology**: players who make one small purchase are more likely to make larger purchases later. The first payment crosses a psychological threshold. (s014)

### Gacha / loot boxes
Randomized reward systems where the player pays for a chance at a desirable item.

Design analysis:
- **Variable ratio reinforcement** (Skinner): the most powerful engagement pattern — intermittent, unpredictable reward. More compelling than guaranteed rewards. (s014)
- **Near-miss effect**: getting "almost" the desired item increases the desire to try again
- **Pity systems**: guaranteeing the desired item after N pulls makes the system feel fair while maintaining the variable-ratio core

Ethical concerns:
- Players cannot predict spending; this creates compulsive spending risk
- Near-miss mechanics are deliberately exploitative
- Many jurisdictions now classify loot boxes as gambling

> ⚠️ **Design caution**: gacha and loot box mechanics produce short-term revenue and long-term player resentment. Games that rely heavily on them often see engagement collapse when players feel they've been treated unfairly. (s017, s014)

---

## Battle passes (s017)

The battle pass emerged as a widely accepted alternative to loot boxes:

**Structure**: 
- 100+ tiers of cosmetic rewards
- Tiers unlocked by playing the game (earning XP)
- A free track (limited rewards) and a premium track (paid; more rewards)
- Seasonal: expires after ~3 months, replaced with new content

**Why it works**:
- **Predictable value**: players know exactly what they're buying
- **Reinforces core loop**: the tier-progression mechanic gives players a reason to keep playing
- **Non-exploitative timing**: the player pays once and earns by playing; no randomness
- **Community fairness perception**: all premium-track players earn the same rewards through the same play time

**Design risk**: battle pass FOMO. Players who can't play enough to complete the pass feel punished. This creates a "job" dynamic — healthy play becomes obligatory play. Games that set the XP requirement too high or the time window too short produce this pathology.

---

## Season/DLC content (s006; s005)

Premium games often release paid expansions after launch. The design considerations:

**Day-one value question**: if the base game content is thin and the DLC "completes" it, players feel the base game was incomplete — especially if the DLC was in development before launch.

**Post-launch game health**: DLC and updates keep the game in public attention and generate ongoing revenue from an existing audience. The economics favor investing in good post-launch content.

**Bundling and GOTY editions**: games that initially sell poorly sometimes find large audiences through complete editions — the full game + DLC bundled at a discount. This is a lifecycle monetization strategy, not just a pricing decision.

---

## Subscription models (s006)

**Game library subscriptions** (Xbox Game Pass, PlayStation Plus, Apple Arcade): player pays a monthly fee to access a large catalog. 
- Design implication: the player has zero financial barrier to trying your game — but also zero commitment. Churn from low-quality first impressions is the main risk.

**Live-service subscriptions** (recurring payment for ongoing content access):
- Only viable if the game provides continuous new content worth paying for
- Player expectations are high: they are paying every month and expect monthly-level value

---

## Ethical design principles for monetization (s014, s017)

The core test (Hodent, s014): **the fair reflection test**. If players, upon reflection, feel they were treated fairly and received value proportional to what they paid, the monetization is ethical. If they feel manipulated, deceived, or coerced, it isn't — and they will eventually leave and warn others.

Practical principles:
1. **The free experience must be genuinely good** — if non-paying players have a poor experience, the monetization is exploitative
2. **Never sell gameplay advantage in competitive contexts** — this destroys community trust
3. **Predictable value over randomized reward** where possible
4. **No dark patterns** — fake timers, misleading "sale" prices, hidden mandatory purchases
5. **Make spending optional and satisfying** — players who spend should feel good about it, not guilty

---

## Key concepts & cross-links

- [[free-to-play-design]] — the full F2P design system
- [[../../mechanics/game-loops]] — monetization is integrated into loop architecture
- [[../../player/player-psychology]] — reward schedules, loss aversion, undermining effect
- [[../../player/motivation]] — extrinsic rewards and the risk of undermining intrinsic motivation
- [[../../player/flow-channel]] — monetization must not break the flow state

## Sources

s017 (F2P Handbook — revenue models, IAP, ethical design) · s014 (Hodent — reward schedules, psychological mechanisms, fair reflection test) · s006 ch.6 (Adams — payment models, subscription design) · s005 ch.8, ch.9 (Schell — player needs, motivation, reward) · s001 (Sellers — engagement vs. manipulation)
