---
name: ieee-transactions-on-communications
description: Use when targeting IEEE Transactions on Communications (TCOM) or deciding whether a communication-systems manuscript fits this venue. Encodes the journal's fit, the analysis-plus-simulation bar, the system-performance expectation, the TCOM-vs-TWC-vs-JSAC routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Communications (ieee-transactions-on-communications)

## Journal positioning

IEEE Transactions on Communications (TCOM) is a broad archival venue for the design
and analysis of communication systems: modulation and detection, applied channel
coding, equalization, multiple access, networking, and wireless and optical
communication systems, with an emphasis on end-to-end system performance. The
defining expectation is a **communication contribution with quantitative
performance analysis** — a new scheme or architecture whose error/throughput/latency
behavior is derived analytically and corroborated by simulation, sometimes by
hardware. Pure fundamental-limit theorems belong in information theory; purely
empirical ML pipelines with no communications model are a poor fit. This skill is a
**fit / venue-selection / re-framing** tool. It does not replace the journal's
current official author guidelines. Before submitting, re-check the live IEEE
Transactions on Communications author information and submission system.

## When to trigger

- The author names TCOM for a communication-system design or performance-analysis
  manuscript and wants a fit/framing check.
- A scheme must be re-framed from "it works in simulation" into a performance result
  with analysis, the right system model, and credible baselines.
- The author is choosing among TCOM, `ieee-transactions-on-wireless-communications`
  (wireless-specific), and `ieee-journal-on-selected-areas-in-communications` (topical
  special issues).
- The author needs the analysis-plus-simulation bar and desk-reject heuristics for
  communication systems.

## Scope & topic fit

- Modulation, detection, and equalization; coded-modulation and applied channel-coding
  system design with performance analysis.
- Multiple-access and multiuser communication; interference management; cooperative
  and relay communication systems.
- Optical and free-space optical communication; underwater and molecular
  communication; satellite and non-terrestrial links.
- Communication networking and cross-layer design where the physical/link layer and
  measurable system performance are central.
- Energy efficiency, latency, and reliability analysis of communication systems,
  including emerging waveforms and architectures.

## Method & evidence bar

- The contribution is a **scheme/architecture with quantitative performance** — BER/BLER,
  throughput, outage, latency, or energy efficiency — derived analytically where
  feasible and validated by Monte Carlo simulation.
- Analytical results (closed-form or asymptotic expressions, bounds, scaling laws)
  strengthen the paper; simulation alone, without insight into why a scheme performs,
  is weaker.
- Baselines must be current, correctly tuned competitors under the same channel and
  system model; gains must be attributable to the proposed idea.
- Channel models, system assumptions, and operating regimes must be explicit and
  realistic; robustness to imperfect CSI or model mismatch should be addressed.
- Where applicable, complexity and implementability are discussed; testbed or hardware
  validation adds credibility but is not always required.

## Structure & house style

- IEEE format; TCOM publishes full **Papers** — match scope to the format and re-check
  current article types and limits on the live guide.
- The system model and assumptions are stated precisely early; the proposed scheme,
  its analysis, and the performance evaluation form the core.
- The introduction motivates the communications gap and positions against prior
  schemes, not against fundamental limits unless that is the contribution.
- Figures are quantitative and comparative: performance-vs-SNR curves, throughput/latency
  plots, and analysis-vs-simulation agreement plots.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Transactions on Communications page you checked.
- Search the live site for "IEEE Transactions on Communications information for
  authors" and follow the current submission-system version.
- Re-check article types and length/overlength policy, the IEEE template, and any
  overlap/dual-submission policy with sibling journals.
- Confirm reproducibility/simulation-code expectations for performance claims.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a communication scheme/architecture with quantitative performance, not a fundamental-limit theorem or a bare ML pipeline.
- [ ] Performance is derived analytically where feasible and corroborated by simulation, with analysis–simulation agreement shown.
- [ ] Baselines are current, correctly tuned competitors under a matched system/channel model.
- [ ] Channel and system assumptions are explicit and realistic; sensitivity to imperfect CSI/model mismatch is addressed.
- [ ] The wireless-specific vs. general-comms scope choice (TCOM vs. TWC vs. JSAC) is deliberate.
- [ ] Article type and length fit current limits.

## Common desk-reject triggers

- Simulation-only scheme with no analysis and no insight into why it performs.
- Gains shown only over outdated or mistuned baselines, or under unrealistic channel assumptions.
- A fundamental-limit/capacity paper with no system-design contribution (belongs in information theory).
- Application of an off-the-shelf ML model to a communications dataset with no communications-system contribution.
- Incremental tweak of a known scheme with negligible, unexplained performance change.

## Re-routing decision

- Fundamental capacity/limit theorem is the core → `ieee-transactions-on-information-theory`.
- Wireless-specific PHY/MAC, MIMO, channel modeling → `ieee-transactions-on-wireless-communications`.
- Topical systems-frontier work matching an active call → `ieee-journal-on-selected-areas-in-communications`.
- Signal-processing method with analysis as the core → `ieee-transactions-on-signal-processing`.
- Broad tutorial/survey of a communications area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Communications
[Topic tags] <2–3 closest communications subtopics>
[Scheme + performance] <the design and the metric(s) it improves>
[Analysis vs simulation] <derived + corroborated? baselines matched?>
[Top risk] <the single most likely reason for rejection>
[Sibling check] TCOM vs. TWC vs. JSAC (one-line reason)
[Official items to re-check] <article type / length / sim-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
