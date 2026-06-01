---
name: icml-topic-selection
description: Use when deciding whether a manuscript fits ICML, choosing main-track versus position paper or another venue, or rerouting an ML paper based on contribution type, evidence, and community fit.
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

## Output format

```text
[Fit] High / Medium / Low
[Recommended route] ICML main / ICML position / workshop / another conference / journal
[Contribution type] method / theory / evaluation / systems / trustworthy ML / application-driven / position
[Why ICML] <one sentence>
[Upgrade needed] <evidence, framing, related work, artifacts, impact, or reroute>
```
