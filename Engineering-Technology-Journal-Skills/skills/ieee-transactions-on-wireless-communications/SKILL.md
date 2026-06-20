---
name: ieee-transactions-on-wireless-communications
description: Use when targeting IEEE Transactions on Wireless Communications (TWC) or deciding whether a wireless-communications manuscript fits this venue. Encodes the journal's fit, the analysis-plus-simulation bar, the wireless-specific scope, the TWC-vs-TCOM-vs-JSAC routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Wireless Communications (ieee-transactions-on-wireless-communications)

## Journal positioning

IEEE Transactions on Wireless Communications (TWC) is the archival venue dedicated to
wireless systems: physical- and medium-access-layer techniques, MIMO and massive
MIMO, channel modeling and estimation, resource allocation, and wireless networking,
with an emphasis on quantitative wireless-link and system performance. The defining
expectation is a **wireless-specific contribution with analysis and simulation** — a
new technique or architecture whose rate/outage/energy/latency behavior is derived
and validated under realistic wireless channel models. Work with no genuinely
wireless dimension (generic comms, pure information theory, or an ML model on a
dataset) is a poor fit. This skill is a **fit / venue-selection / re-framing** tool.
It does not replace the journal's current official author guidelines. Before
submitting, re-check the live IEEE Transactions on Wireless Communications author
information and submission system.

## When to trigger

- The author names TWC for a PHY/MAC, MIMO, channel, or resource-allocation manuscript
  and wants a fit/framing check.
- A wireless technique must be re-framed from "good simulation results" into a result
  with a wireless channel model, analysis, and the right baselines.
- The author is choosing among TWC (wireless-specific),
  `ieee-transactions-on-communications` (general comms), and
  `ieee-journal-on-selected-areas-in-communications` (topical calls).
- The author needs the wireless analysis-plus-simulation bar and desk-reject
  heuristics.

## Scope & topic fit

- MIMO and massive MIMO: precoding, beamforming, hybrid/analog architectures,
  reconfigurable intelligent surfaces, and their performance analysis.
- Channel modeling, estimation, and feedback; effects of imperfect CSI, mobility, and
  hardware impairments on wireless performance.
- Radio resource management: power control, scheduling, spectrum sharing, interference
  coordination, and energy-efficient wireless design.
- Multiple access and waveform design for wireless links (e.g., NOMA, OFDM variants),
  with link- and system-level evaluation.
- Wireless networking and cross-layer design — including mmWave/THz, cell-free, and
  integrated sensing-and-communication — where the wireless layer is central.

## Method & evidence bar

- The contribution is a **wireless technique/architecture with quantitative
  performance** — spectral/energy efficiency, outage, rate region, or latency — derived
  analytically where feasible and validated by simulation under realistic channels.
- Channel and impairment models must be appropriate to the regime (e.g., correlated
  fading, mmWave sparsity, hardware non-idealities); idealized assumptions that erase
  the wireless difficulty weaken the paper.
- Imperfect-CSI, pilot-overhead, and mobility effects should be addressed where they
  matter; an analysis assuming perfect CSI without discussion is often insufficient.
- Baselines must be current, correctly tuned wireless competitors under the same model;
  gains must be attributable to the proposed idea, not to favorable assumptions.
- Complexity, pilot/feedback overhead, and implementability should be discussed;
  closed-form or asymptotic analysis that explains the gain strengthens the result.

## Structure & house style

- IEEE format; TWC publishes full **Papers** — match scope to the format and re-check
  current article types and limits on the live guide.
- The wireless system and channel model are stated precisely early; the technique, its
  analysis, and the simulation evaluation form the core.
- The introduction positions against prior wireless techniques and articulates the
  wireless-specific gap, not a general communications or limit-theory framing.
- Figures are quantitative: spectral/energy-efficiency curves, outage/rate plots,
  analysis-vs-simulation agreement, and overhead/complexity comparisons.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Transactions on Wireless Communications page you checked.
- Search the live site for "IEEE Transactions on Wireless Communications information
  for authors" and follow the current submission-system version.
- Re-check article types and length/overlength policy, the IEEE template, and any
  overlap/dual-submission policy with TCOM and JSAC.
- Confirm reproducibility/simulation-code expectations for wireless performance claims.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is genuinely wireless-specific (PHY/MAC/MIMO/channel/resource), not general comms or pure limit theory.
- [ ] Performance is derived analytically where feasible and validated by simulation under realistic channel models.
- [ ] Imperfect-CSI, overhead, and mobility effects are addressed where they matter.
- [ ] Baselines are current, correctly tuned wireless competitors under a matched model.
- [ ] The TWC vs. TCOM vs. JSAC scope choice is deliberate and justified.
- [ ] Article type and length fit current limits.

## Common desk-reject triggers

- Idealized assumptions (e.g., perfect CSI, no overhead) that remove the wireless difficulty and inflate gains.
- Simulation-only technique with no analysis and no insight into the wireless mechanism of improvement.
- Gains over outdated or mistuned wireless baselines, or under unrealistic channel models.
- A general-communications or capacity-theorem paper with no wireless-specific contribution.
- Off-the-shelf ML applied to a wireless dataset with no wireless-systems advance.

## Re-routing decision

- General (non-wireless-specific) communications result → `ieee-transactions-on-communications`.
- Topical wireless frontier matching an active call → `ieee-journal-on-selected-areas-in-communications`.
- Fundamental capacity/limit theorem → `ieee-transactions-on-information-theory`.
- Signal-processing estimation/detection method with analysis → `ieee-transactions-on-signal-processing`.
- Broad tutorial/survey of a wireless area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Wireless Communications
[Topic tags] <2–3 closest wireless subtopics>
[Technique + performance] <the wireless idea and the metric(s) it improves>
[Channel realism] <models appropriate? imperfect-CSI/overhead handled?>
[Top risk] <the single most likely reason for rejection>
[Sibling check] TWC vs. TCOM vs. JSAC (one-line reason)
[Official items to re-check] <article type / length / sim-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
