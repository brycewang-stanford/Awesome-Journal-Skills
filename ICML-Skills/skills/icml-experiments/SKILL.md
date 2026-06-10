---
name: icml-experiments
description: Use when stress-testing ICML experimental evidence before submission or rebuttal, including strong tuned baselines, mechanism-isolating ablations, seed variance and confidence intervals, compute disclosure, data leakage and split construction, reproducibility, negative results, and fit to ICML soundness, originality, and significance scoring.
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

## Reviewer-pushback patterns and the ICML fix

| Pushback | Why it lands at ICML | Fix |
| --- | --- | --- |
| "Convergence guarantees under assumptions the experiments violate" | Theory paper asserts a rate under smoothness or bounded variance, but the deep-learning runs break it | State assumptions honestly, add a figure showing the rate holds empirically in-regime, flag where it does not |
| "Missing strong, tuned baselines" | The leaderboard win used an undertuned competitor | Re-tune the baseline with matched budget, report the search protocol |
| "No variance, single seed" | One run cannot separate signal from noise | Report seeds with confidence intervals or justify determinism |
| "Compute not disclosed" | ICML expects hardware and training-cost transparency | Add a compute table and confirm comparison fairness |

## Worked vignette: optimizer claim audit

A paper claims a new adaptive step-size method beats Adam with a non-convex convergence guarantee.
The audit asks: is Adam tuned with the same budget, do the benchmark losses actually satisfy the
proof's assumptions, and do gains survive across seeds and model sizes? If the win shrinks under a
tuned baseline or the assumptions hold only on toy quadratics, the right move is to narrow the claim
to the regime where both theory and experiments agree, rather than overclaim a universal speedup.

## Rebuttal-ready result

During response, prefer a small decisive table, corrected baseline, missing ablation, or concise
error analysis over a broad new experimental section. ICML gives one discussion round, so a single
tuned-baseline row or in-regime variance plot moves a reviewer more than a sprawling new study.

## Output format

```text
[Evidence status] strong / adequate / weak
[Most vulnerable claim] <claim>
[Critical missing result] <baseline/ablation/variance/leakage/compute>
[Small response result] <feasible clarification>
[Claim narrowing] <text if evidence is not enough>
```

