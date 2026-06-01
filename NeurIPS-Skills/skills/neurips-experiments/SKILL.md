---
name: neurips-experiments
description: Use when stress-testing NeurIPS experimental evidence, including baselines, ablations, data splits, compute, negative results, real-world use, and claim-to-evidence calibration.
---

# NeurIPS Experiments

Use this skill before submission or rebuttal when the main question is whether the evidence supports
the NeurIPS claim. It is not enough to win a leaderboard; reviewers need to know why the result is
scientifically meaningful.

## Experiment audit

- Baselines: include strong, current, tuned baselines and explain any missing comparison.
- Ablations: isolate the mechanism, not just remove components at random.
- Robustness: test across seeds, datasets, distribution shifts, scales, hyperparameters, or
  realistic deployment conditions when relevant.
- Compute: disclose hardware, training time, resource assumptions, and whether comparisons are fair.
- Data: document splits, contamination controls, license, demographic or domain coverage, and
  privacy/consent limits.
- Negative results: use them to calibrate claims; NeurIPS has a contribution type for negative
  results, but the bar remains high.
- Use-inspired work: connect results to the real task without turning the paper into an application
  report with no ML contribution.

## Rebuttal-ready evidence

Prepare small, high-signal clarifications that can fit in an author response: a missing baseline
table, a sanity check, an error analysis, a variance estimate, or a concise proof sketch. Do not
depend on a complete post-review paper rewrite.

## Output format

```text
[Evidence status] strong / adequate / weak
[Main unsupported claim] <claim>
[Critical missing experiment] <baseline/ablation/robustness/data/compute>
[Small rebuttal result] <result feasible during response>
[Claim rewrite] <narrower claim if evidence stays as is>
```

