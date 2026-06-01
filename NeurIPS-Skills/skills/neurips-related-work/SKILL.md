---
name: neurips-related-work
description: Use when positioning a NeurIPS submission against current-cycle ML literature, contemporaneous work, preprints, neighboring conferences, and the exact technical delta from prior methods.
---

# NeurIPS Related Work

Use this skill when novelty or positioning is the main risk. NeurIPS reviewers will often know
recent papers from neighboring AI venues and preprint streams; stale comparisons are a serious
weakness.

## What to cover

- Direct technical ancestors: methods with the same objective, architecture, proof technique,
  benchmark, dataset, or deployment problem.
- Neighboring venues: ICML, ICLR, AAAI, IJCAI, AISTATS, UAI, COLT, MLSys, KDD, CVPR, ACL, EMNLP,
  SIGIR, ICRA, CHI, and other subfield venues as relevant.
- Contemporaneous work: papers that appeared during the current review window. The 2026 handbook
  treats work appearing online after March 1, 2026 as contemporaneous for review purposes, but
  authors still need to cite and discuss it when feasible.
- Preprints: public preprints are not automatically disqualifying, but they must not be used to
  advertise a submission aggressively under review.

## Delta-writing template

For each close paper, write:

```text
<Prior work> solves <problem> by <mechanism>. It does not address <gap>.
Our paper differs by <technical delta>, which matters because <evidence or theory>.
```

## Failure modes

- Listing citations without explaining technical differences.
- Omitting a close arXiv or prior conference paper because it is inconvenient.
- Claiming novelty over broad topic labels rather than mechanisms.
- Hiding dependence on prior code, data, prompts, or evaluation protocols.

## Output format

```text
[Closest prior work] <3-5 papers or categories>
[Missing citation risk] High / Medium / Low
[Technical delta] <one-sentence difference>
[Contemporaneous work handling] <cite/compare/acknowledge>
[Rewrite] <related-work paragraph>
```

