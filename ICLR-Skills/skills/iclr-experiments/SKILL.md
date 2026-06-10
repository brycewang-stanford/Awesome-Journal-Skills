---
name: iclr-experiments
description: Use when designing or auditing ICLR experiments, including baselines, ablations, scaling laws, robustness, statistics, benchmarks, human evaluation, and compute reporting. Use when a reviewer questions whether a representation-learning or model gain is real, when you must isolate one mechanism with an ablation, or when preparing a small compute-matched control that can be posted inline during the public discussion period.
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

## What ICLR reviewers reward in evidence

ICLR's empirical culture prizes honest ablations and mechanism over leaderboard position. A clean
ablation that explains *why* a representation works often outscores a larger raw number.

| Claim type | Evidence that convinces ICLR reviewers | Common reject trigger |
| --- | --- | --- |
| New objective helps | Ablate the objective with everything else fixed | Gains confounded with extra tuning |
| Method scales | Several model sizes/tasks with a trend | One large run, no scaling curve |
| Robust representation | Tests across shifts, seeds, prompts | Single-seed peak on one benchmark |
| Beats prior method | Tuned, current, open-source baseline | Stale or under-tuned baseline |

## Worked vignette

A paper claims a new self-supervised pretext task yields better linear-probe accuracy. Reviewers
ask whether the gain is the pretext task or simply longer pretraining. The author audit: hold total
pretraining compute fixed, swap only the pretext objective, and report linear-probe accuracy with
error bars over five seeds. The compute-matched ablation isolates the mechanism and is small enough
to post inline during discussion, where the table becomes part of the permanent public record.

## Reviewer-pushback patterns

- "You win because of more compute." Add a compute-matched control; report FLOPs, not just wall time.
- "Only one seed." Report mean and spread across seeds; an unstable benchmark needs variance.
- "Baseline is weak." Cite the baseline's own recommended settings and show you matched them.
- "Ablation removes two things at once." Split into single-mechanism ablations a reviewer can read.

## Output format

```text
[Claim] <paper claim>
[Experiment evidence] sufficient / needs baseline / needs ablation / needs robustness
[Fairness issue] <compute, tuning, data, prompt, metric>
[Fast fix] <experiment or analysis feasible before deadline>
[Appendix placement] <what can move out of main text>
```

