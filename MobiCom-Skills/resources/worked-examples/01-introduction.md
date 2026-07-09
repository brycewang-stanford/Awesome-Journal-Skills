> **Illustrative teaching example.** The paper, system, setting, and every number below are
> **fictional** and exist only to demonstrate MobiCom house style. No real-paper facts,
> testbeds, or results are stated, and no policy is invented. Corresponding skills:
> [`mobicom-writing-style`](../../skills/mobicom-writing-style/SKILL.md),
> [`mobicom-topic-selection`](../../skills/mobicom-topic-selection/SKILL.md), and
> [`mobicom-experiments`](../../skills/mobicom-experiments/SKILL.md).

# Worked Example: A MobiCom-Style Abstract + Introduction (before → after)

This demonstrates the **MobiCom first-page arc** from `mobicom-writing-style`:
**wireless/mobile pain → why existing mechanisms fall short → the mechanism → measured
evidence over the air → why it matters for mobile networking** — with the MobiCom rules
that the contribution is a **networking mechanism**, that **claims are paired with
measurement on real hardware** (not simulation alone, not a single run), and that
**percentiles and confidence intervals replace superlatives**.

The framing also reflects `mobicom-topic-selection`: MobiCom is strongest when the novelty
is a **wireless or mobile-networking mechanism** — here, a backscatter link that survives
real channel conditions — rather than an end-to-end platform (which would route to MobiSys)
or a pure PHY abstraction with no networking payoff.

**Illustrative paper (fictional):** *"Batteryless Uplink at Room Scale: A Backscatter Link
That Holds Under Human Mobility."* Fictional mechanism: a tag-side coding scheme that keeps
a backscatter uplink decodable as people move through the channel.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** The Internet of Things is growing rapidly and battery maintenance is a major
> problem. In this work we study backscatter communication, which is a promising low-power
> technology. We propose a new backscatter system that combines a novel coding scheme with a
> custom receiver and achieves excellent performance in our experiments, outperforming prior
> backscatter systems in most settings.
>
> **Introduction.** Backscatter communication has been studied extensively. Many systems
> exist, using ambient signals, dedicated carriers, or Wi-Fi. In this paper, we build a tag
> and a reader and evaluate them in our lab, showing that our system works well and achieves
> high throughput. Section 2 reviews related work, Section 3 describes our system, Section 4
> presents experiments, and Section 5 concludes.

**What's wrong (against `mobicom-writing-style` / `mobicom-topic-selection` / `mobicom-experiments`):**

- **No mechanism on the first page** — leads with "IoT is growing," not the specific
  wireless failure and the mechanism that fixes it. MobiCom wants the networking
  contribution stated up front.
- **The wireless conditions are hidden** — no channel, mobility, distance, or interference
  regime is named, which is exactly what MobiCom reviewers ask a backscatter paper to pin
  down.
- **Overclaims** ("excellent performance," "outperforming in most settings," "works well")
  with **no measurement discipline** — no percentiles, no repetition, no confidence
  intervals (`mobicom-experiments`).
- **Lab-only, single-setting** framing with no mobility and no real deployment condition —
  the under-evaluation flag at MobiCom.
- **No claim → evidence pairing:** "high throughput" is not tied to a channel condition, a
  distance, or a measured distribution.
- **Over-signposted roadmap** standing in for an argument.

---

## After (MobiCom arc — pain → gap → mechanism → measured evidence → why it matters)

> **Abstract.** Backscatter uplinks are attractive because tags need no battery, but they
> **break under human mobility**: as a person moves through the channel, the reflected
> signal fades and the reader's bit-error rate spikes, so existing tags either sit still or
> add a carrier that defeats the power argument. We present **DriftCode**, a tag-side coding
> scheme that keeps the uplink decodable across mobility-induced fades by spreading each
> symbol over channel coherence intervals the reader tracks blindly. We implement DriftCode
> on a **passive tag and a software-radio reader** and evaluate it over the air in a
> furnished room with **people walking through the link**. Across 20 runs at 1-4 m,
> DriftCode holds packet-reception rate above the batteryless-tag usability threshold where
> a fixed-rate baseline collapses under the same walking traces; we report reception rate
> and energy-per-bit with 95% confidence intervals and the measured channel conditions.
> *(pain → gap → mechanism → measured evidence with uncertainty — all on the first page.)*
>
> **Introduction.** *(¶1 — pain + contribution, first breath.)* A batteryless tag is only
> useful if its uplink survives the room it lives in, and rooms contain **moving people**.
> When a person crosses a backscatter link, the reflected path fades on a timescale of tens
> of milliseconds, and a fixed-rate tag loses the packet. We present **DriftCode**, a
> tag-side coding scheme that keeps a passive backscatter uplink decodable **through
> mobility-induced fades**, without a dedicated carrier and within the tag's harvested
> energy budget.
>
> *(¶2 — gap: why existing mechanisms are insufficient.)* Existing designs fall short for
> distinct, nameable reasons. Ambient-signal tags assume a **quasi-static channel** and
> degrade sharply once the multipath moves. Carrier-assisted tags restore the link but
> **reintroduce an active transmitter**, spending the power budget the tag was supposed to
> save. Reader-side equalization helps a stationary tag but **cannot recover a symbol the
> tag already sent below the noise floor** during a deep fade. *(each prior line gets a
> specific failure tied to the wireless condition, not a vague "prior work is limited.")*
>
> *(¶3 — mechanism + the operating regime named.)* DriftCode spreads each tag symbol across
> several channel-coherence intervals and interleaves so that a fade erases parity, not
> whole symbols; the reader tracks coherence blindly from the pilot reflections it already
> receives. The design targets **room-scale distances (1-4 m), pedestrian mobility, and the
> energy a passive tag harvests indoors** — the regime stated plainly because a backscatter
> claim outside its channel and power envelope is a review risk.
>
> *(¶4 — mechanism justified by measurement, each claim paired.)* We built DriftCode on a
> passive tag and a software-radio reader and measured it **over the air**, with volunteers
> walking scripted paths through the link (protocol in App. A). Under those walking traces,
> DriftCode keeps packet-reception rate above the usability threshold at 1-4 m while the
> fixed-rate baseline collapses in the same fades (Fig. 3), at an energy-per-bit within the
> harvested budget (Fig. 4). **All results are 20 runs with 95% confidence intervals**, and
> the channel conditions — RSSI traces, coherence-time distribution, and walker positions —
> are reported alongside each figure. *(every claim → a figure, a measured condition, or a
> reproducibility location.)*
>
> *(¶5 — why it matters for mobile networking + roadmap.)* The contribution is to make a
> **batteryless uplink robust to the everyday mobility of the space it operates in** — a
> networking-layer coding mechanism, not a new radio or a new platform. Section 2 states the
> channel model and the coding scheme; Section 3 describes the tag and reader; Section 4
> reports the over-the-air evaluation under mobility. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the MobiCom bar

Mapped to the skill checklists:

- **Mechanism on the first page** — the abstract and ¶1 name the pain (mobility fades),
  the gap, and the coding mechanism before any implementation detail
  (`mobicom-writing-style`: "put the wireless/mobile mechanism in the first page").
- **Operating regime explicit** — distance, mobility, and energy envelope are named as the
  regime, and the paper does not claim outside it (`mobicom-writing-style`: reviewers flag a
  wireless claim with an unstated channel/power envelope).
- **Every claim paired with measurement** — robustness → Fig. 3 under walking traces;
  energy → Fig. 4 within the harvested budget; conditions → RSSI/coherence traces; protocol
  → App. A (`mobicom-experiments` claim→evidence map).
- **No overclaiming** — "holds above the usability threshold where the baseline collapses,"
  with **20 runs and 95% confidence intervals** and the channel conditions shown, not
  "outperforms in most settings" (`mobicom-experiments`: report distributions and
  uncertainty, not single best runs).
- **Over-the-air, under mobility** — measured with people moving through the link, not a
  static lab bench or simulation only (`mobicom-experiments`: real-hardware, realistic
  conditions).
- **Right venue** — the contribution is a **networking-layer coding mechanism** for a
  wireless link, a strong MobiCom fit rather than a MobiSys platform paper or a pure-PHY
  result (`mobicom-topic-selection` fit test).
- **12-page double-column discipline** — the channel model derivation and the full
  measurement protocol are pushed to appendices while the body stays a readable argument
  (`mobicom-writing-style`: use the 12-page body for the core mechanism and its evidence).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, venue-verified
> MobiCom papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for MobiCom-specific submission
> policy.
