---
name: iclr-experiments
description: Use when designing or auditing ICLR experiments, including baselines, ablations, scaling laws, robustness, statistics, benchmarks, human evaluation, and compute reporting.
---

# ICLR Experiments

Use this before submission or during a revision pass to stress-test empirical claims. ICLR
experiments should answer the scientific question, not merely assemble a leaderboard.

## Experiment audit

- Match each experiment to a claim in the introduction.
- Compare against current strong baselines, open-source systems, and the most relevant recent
  OpenReview/arXiv papers.
- Add ablations that isolate one mechanism at a time.
- Report variance across seeds or runs when randomness can change conclusions.
- Include robustness checks for dataset shift, prompt changes, architecture variants, hyperparameter
  sensitivity, or compute scale when those affect the claim.
- State compute budget, hardware, training time, inference cost, and environmental or access limits
  where relevant.
- For human evaluation, document task, annotator instructions, aggregation, quality control, and IRB
  or ethics status when needed.

## Reviewer questions to pre-answer

- Is the baseline tuned fairly?
- Does the method win because of more compute, data, parameters, or prompt search?
- Does the effect persist outside the easiest benchmark?
- Are negative results hidden?
- Can a reviewer reproduce the headline table from the supplement or artifact?

## Output format

```text
[Claim] <paper claim>
[Experiment evidence] sufficient / needs baseline / needs ablation / needs robustness
[Fairness issue] <compute, tuning, data, prompt, metric>
[Fast fix] <experiment or analysis feasible before deadline>
[Appendix placement] <what can move out of main text>
```

