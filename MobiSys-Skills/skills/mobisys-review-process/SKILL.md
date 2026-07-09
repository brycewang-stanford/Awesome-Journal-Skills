---
name: mobisys-review-process
description: Use when explaining or planning around MobiSys peer review — the two-round process with an early-reject cut after round 1, the round-2 rebuttal window, double-blind HotCRP mechanics, the systems-and-services reviewer pool, and decision criteria for on-device claims, so response strategy fits how MobiSys decides.
---

# MobiSys Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, the HotCRP site, and
the organizing-committee page before making process claims — the mechanics are cycle-specific.

## Process model

- MobiSys uses HotCRP for submission and review, with a paper-registration step preceding the
  paper upload and **double-blind** review (author identities hidden since 2017).
- Review runs in **two rounds**. Papers that do not advance past round 1 receive an **early
  rejection with reviews**, so authors can re-plan before the process ends. Round-2 survivors
  reach reviews and a **rebuttal window**.
- The rebuttal is **scope-limited**: correct factual errors and answer specific reviewer
  questions; new results are admissible only when directly responsive, or may be promised for
  camera-ready (`mobisys-author-response`).
- Unlike MobiCom and NSDI, the rendered 2026 CFP describes accept/reject through the rebuttal,
  **not** a separate one-shot revision channel; treat any revision path as 待核实 per cycle.
- Accepted papers are published in the ACM Digital Library, so camera-ready compliance and
  artifact badges matter as much as the initial accept.

## Who reviews here

- The pool is **systems-and-services** researchers: people who build and measure mobile
  runtimes, on-device ML, sensing services, and platforms, and who read an energy or latency
  claim as something to be re-derived, not admired.
- Because MobiSys is specialized, topical matches are close; a hand-wavy device claim or an
  undefined energy boundary gets caught rather than skimmed past.
- Borderline mobile-systems papers usually fall on one of three edges: an evaluation on a
  single device or single run, an energy/thermal claim without a described instrument, or a
  contribution that is really a better model dressed as a system.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Contribution | A system mechanism forced by the device constraint | A model or algorithm with an incidental phone demo |
| On-device evidence | Distributions on real hardware across devices/states | Single-device, single-run, simulation-only numbers |
| Energy/latency rigor | Named instrument, boundary, and sustained-load behavior | "Efficient" with no measured joules or throttle trace |
| Clarity | An explicit operating point (device, workload, budget) | Latency numbers with no device or workload context |

## Stage-by-stage realism

- Round 1: triage by what a systems reviewer would weigh — is the device evidence real and is
  the contribution a system? A thin evaluation is the classic early reject.
- Rebuttal: windows are short and scope is narrow; a precise reply that fixes a factual error
  and answers the one decision-critical question beats an exhaustive one.
- Decision: one unresolved evidence objection (single-device, undefined energy boundary)
  outweighs several resolved clarity complaints.
- After accept: artifact evaluation and camera-ready are their own gates
  (`mobisys-artifact-evaluation`, `mobisys-camera-ready`).

## Output format

```text
[Current stage] submitted / round-1 / round-2 reviews / rebuttal / decision / camera-ready
[Decision actors] <reviewers / AC / chairs>
[Likely leverage] <contribution / on-device evidence / energy-latency rigor / clarity>
[Forbidden moves] <identity leak / out-of-scope new results in rebuttal>
[Next response move] <one action>
```
