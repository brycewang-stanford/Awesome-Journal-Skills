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

## Claim-to-evidence ladder

NeurIPS reviewers read experiments against the claim type. Put every headline claim on the ladder
before deciding whether the evidence is strong enough.

| Claim type | Minimum evidence | Strong evidence |
| --- | --- | --- |
| Beats prior methods | tuned current baselines, same data splits, comparable compute | multiple suites, budget-matched tuning, significance or variance reporting |
| Mechanism explains gains | ablation tied to the proposed mechanism | intervention or diagnostic that rules out the obvious rival mechanism |
| Scales better | at least two meaningful scales and fixed protocol | trend across scales with compute, memory, and failure modes disclosed |
| Robust to distribution shift | one out-of-domain or stress split | several shifts with error analysis and narrowed claims where it fails |
| Useful in the real world | task-relevant metric and realistic constraint | deployment-like evaluation, safety/fairness/privacy caveats, and cost analysis |
| Negative result | faithful implementation and fair reproduction attempt | explains when the prior claim holds, fails, or needs qualification |

If the evidence only clears the minimum column, write the claim in minimum-column language. Reserve
strong-column language for results that survive the stronger checks.

## Baseline fairness table

Before submission, make a table the reviewer could audit without trusting your narrative.

| Baseline issue | Required disclosure | Reviewer failure mode |
| --- | --- | --- |
| Tuning budget | search space, number of trials, early stopping, compute cap | new method gets more tuning than baselines |
| Implementation source | official code, reimplementation, or third-party fork | weak reproduced baseline blamed on prior work |
| Data protocol | splits, leakage checks, preprocessing, augmentation | accidental train/test contamination |
| Resource match | hardware, batch size, wall-clock, memory, total cost | speed/accuracy tradeoff hidden |
| Selection rule | validation metric and checkpoint choice | cherry-picked best seed or test-set tuning |

Missing baselines are acceptable only when the omission is named and justified: unavailable code,
incompatible task, prohibitive compute, licensing, safety, or a scope mismatch. Do not silently omit
the strongest comparison.

## Review-dimension stress test

Map the experimental section to the dimensions reviewers will naturally score.

| Dimension | Experiment question |
| --- | --- |
| Quality | Does the design isolate the proposed contribution rather than a confound? |
| Clarity | Can a reader reproduce the protocol from the paper, appendix, and checklist? |
| Significance | Does the effect matter beyond a narrow benchmark increment? |
| Contribution fit | Do the experiments match General, Theory, Use-Inspired, Concept & Feasibility, or Negative Results framing? |
| Ethics/reproducibility | Are data, compute, privacy, bias, and artifact limits disclosed honestly? |

## Rebuttal triage gate

Not every missing experiment is rebuttal-feasible. Sort reviewer requests by value and risk.

| Request | Rebuttal action | Camera-ready or future-work action |
| --- | --- | --- |
| Missing variance / seed concern | run a small seed sweep or report existing variance | expand seed grid if accepted |
| Missing obvious baseline | add it only if implementation and tuning are fair in time | otherwise explain omission and add after review |
| Mechanism unclear | add a diagnostic ablation or error slice already supported by the code | rewrite mechanism framing if evidence stays indirect |
| Dataset contamination worry | add leakage check and describe split construction | archive scripts and checklist support |
| New benchmark family | usually too large for response unless already prepared | narrow claim and schedule full evaluation later |

## Rebuttal-ready evidence

Prepare small, high-signal clarifications that can fit in an author response: a missing baseline
table, a sanity check, an error analysis, a variance estimate, or a concise proof sketch. Do not
depend on a complete post-review paper rewrite.

## Output format

```text
[Evidence status] strong / adequate / weak
[Main unsupported claim] <claim>
[Critical missing experiment] <baseline/ablation/robustness/data/compute>
[Review dimension at risk] quality / clarity / significance / contribution fit / ethics-reproducibility
[Baseline fairness] tuned / comparable compute / same splits / missing justified
[Small rebuttal result] <result feasible during response>
[Claim rewrite] <narrower claim if evidence stays as is>
```
