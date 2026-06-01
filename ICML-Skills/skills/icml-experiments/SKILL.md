---
name: icml-experiments
description: Use when stress-testing ICML experimental evidence, including baselines, ablations, seed variance, compute, data leakage, reproducibility, negative results, and soundness/originality/significance fit.
---

# ICML Experiments

Use this before submission or rebuttal when the central issue is whether experiments are sound
enough for ICML. The question is not just "does it win"; it is whether the evidence supports the ML
claim under fair comparison.

## Experiment audit

- Baselines: current, strong, tuned, and correctly implemented.
- Ablations: isolate mechanism, architecture, objective, data, or optimization change.
- Variance: report seeds, confidence intervals, standard deviations, or a reason variance is not
  meaningful.
- Data: check leakage, split construction, duplication, filtering, licensing, and representative
  coverage.
- Compute: disclose hardware, training cost, inference cost, and comparison fairness.
- Scaling: show whether gains persist across model sizes, datasets, horizons, or domains when that
  supports the claim.
- Negative results: use failures to define boundaries rather than hide them.
- Appendix: put supporting detail there, but keep decisive evidence in the main 8 pages.

## Rebuttal-ready result

During response, prefer a small decisive table, corrected baseline, missing ablation, or concise
error analysis over a broad new experimental section.

## Output format

```text
[Evidence status] strong / adequate / weak
[Most vulnerable claim] <claim>
[Critical missing result] <baseline/ablation/variance/leakage/compute>
[Small response result] <feasible clarification>
[Claim narrowing] <text if evidence is not enough>
```

