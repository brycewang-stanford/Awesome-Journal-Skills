---
name: icml-topic-selection
description: Use when deciding whether a manuscript fits ICML, choosing the main research track versus the ICML Position Papers track or another venue (NeurIPS, ICLR, AISTATS, UAI, COLT, MLSys, TMLR, JMLR), or rerouting an ML paper based on its contribution type, strength of evidence, theory-versus-empirical balance, and interest to the broad ICML machine-learning community. Use before committing effort to an ICML submission.
---

# ICML Topic Selection

Use this before committing to ICML. ICML rewards original, rigorous machine-learning research of
significant interest to the ML community. It is not the best route for every AI application or
position argument.

## Strong fit

- A core ML method, theory, optimization, probabilistic model, RL algorithm, evaluation method,
  systems contribution, or trustworthy-ML result.
- A use-inspired paper where the ML technique, evaluation, or insight is itself important to the ML
  community.
- A theory paper with clear assumptions and meaningful implications.
- An empirical study that improves how ML is evaluated, reproduced, scaled, or understood.
- A paper that can show soundness, originality, significance, clarity, and reproducibility within
  ICML's format.

## Weak fit

- A domain deployment with little ML novelty.
- A benchmark win without mechanism or fair baselines.
- A position or argument paper better suited to the ICML Position Papers track.
- A replication, survey, dataset report, or engineering system better matched to another venue.
- A paper that needs more than appendices or supplement to make the main contribution intelligible.

## Routing decisions

- Main-track ICML: rigorous ML contribution with strong evidence.
- Position Papers: thesis-driven argument about the field rather than a standard research result.
- NeurIPS/ICLR/AISTATS/UAI/COLT/MLSys: choose based on theory, representation learning, statistics,
  uncertainty, learning theory, or systems emphasis.
- TMLR/JMLR: choose for journal-style depth, long revision cycles, or results needing more space.

## Fit-versus-reroute table

| Manuscript shape | ICML verdict | Better route if not ICML |
| --- | --- | --- |
| New method with theory plus tuned benchmarks | Strong main-track fit | - |
| Pure learning-theory result, no experiments | Fits if significant | COLT for theory depth |
| Field-level argument or call for rigor | Reroute | ICML Position Papers track |
| Application with little ML novelty | Weak | Domain venue or applied track |
| Long result needing more than 8 pages | Reconsider | TMLR or JMLR |

## Worked vignette: where does the optimizer paper go

A new adaptive-step method has a non-convex convergence theorem and deep-learning benchmarks. This is
a textbook ICML main-track fit because the ML mechanism, the rate, and the empirical gain are all of
broad interest. If the same authors instead wrote an essay arguing the community over-relies on
adaptive methods, that belongs in the Position Papers track, which uses a separate call and
OpenReview site; check the current year's CFP for both tracks before deciding.

## Output format

```text
[Fit] High / Medium / Low
[Recommended route] ICML main / ICML position / workshop / another conference / journal
[Contribution type] method / theory / evaluation / systems / trustworthy ML / application-driven / position
[Why ICML] <one sentence>
[Upgrade needed] <evidence, framing, related work, artifacts, impact, or reroute>
```
