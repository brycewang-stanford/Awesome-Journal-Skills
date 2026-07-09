---
name: icassp-review-process
description: Use when reasoning about ICASSP peer review — the IEEE Signal Processing Society technical-committee pipeline, EDICS-based assignment, single-blind reviewing, the recently added short rebuttal, oral-versus-poster allocation, the roughly-even acceptance rate, and how a signal-processing decision is actually made and should be decoded.
---

# ICASSP Review Process

Use this to reason about review-stage strategy. Reopen the current call, paper kit, and IEEE SPS
editorial and reviewer guidelines before making process claims, because the mechanics shift by
cycle and are governed by the Signal Processing Society, not by a standing program.

## Process model

- ICASSP review is organized by the **IEEE Signal Processing Society** through its **technical
  committees**; papers are routed by the **EDICS** subject category you select at submission.
- Review is **single-blind**: reviewers see author identities; authors do not see reviewers.
- Reviewers assess technical correctness, novelty and significance to the signal-processing
  community, experimental soundness with task-appropriate metrics, clarity in four pages, and
  reproducibility.
- A **short rebuttal/author-response stage** exists in recent cycles (a recent change from
  ICASSP's older no-rebuttal tradition); confirm it runs this year.
- Accepted papers are published in **IEEE Xplore** and presented in person, as **oral or poster**;
  both are full proceedings papers, and poster is not a second-class outcome.

## Who reviews here

- The pool is **signal-processing practitioners and academics** clustered by technical committee,
  so a paper is judged by people fluent in its exact task's baselines and metrics.
- Reviewers expect the **field-standard metric** and a **current strong baseline**; a novel metric
  or a stale baseline is caught quickly because the reviewers work in that subfield.
- Because the paper is four pages, reviewers reward a claim they can verify quickly and penalize
  one that hides its operating point or its comparison.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Correctness | A clearly specified mechanism with the right signal model | Hand-waved DSP steps; undefined front-end |
| Significance | A result the subfield lacked, stated in its own terms | A generic-ML result with no signal insight |
| Evidence | Task-matched metric, strong baseline, condition sweep | Accuracy where SI-SDR belongs; one-SNR result |
| Clarity | One claim, redrawable architecture, legible figures | Four pages overloaded past legibility |
| Reproducibility | Scoring ruler and split shipped or precisely cited | Metric with no ruler, no split, no seeds |

## Stage-by-stage realism

- **Assignment**: your EDICS choice decides your reviewer pool; a mis-routed paper meets reviewers
  who do not value its contribution (see `icassp-topic-selection`).
- **Reviews**: read them for what the committee will weigh, not for tone; a terse review from an
  expert can carry more decision weight than a long one from a mismatched reviewer.
- **Rebuttal** (if it runs): short and text-only; move the one decision-critical objection, do not
  relitigate everything (see `icassp-author-response`).
- **Decision**: ICASSP acceptance rates have historically sat **near half** — competitive but not
  NeurIPS-scarce; a clean, correct, well-measured four pages is a strong candidate.

## Decoding a decision letter

- "Interesting but incremental" usually means the delta versus a named baseline was not made
  explicit enough — a positioning fix, not necessarily a new experiment.
- "Insufficient evaluation" usually means a missing condition sweep or a non-standard metric, not
  a demand for a bigger model.
- A borderline reject on a correct paper often traces to a **routing or metric-fit** miss that the
  next cycle can repair.

## Output format

```text
[Current stage] submitted / reviews / rebuttal / decision / camera-ready
[Routing] EDICS category and whether it matched the claim
[Decision actors] technical committee / area organizers
[Likely leverage] correctness / significance / evidence / clarity / reproducibility
[Rebuttal move] <one decision-critical point, if a window exists>
[Next action] <one step>
```

## Currency note

Single-blind review, EDICS routing, the recent rebuttal, and the roughly-even acceptance rate
were checked 2026-07-09 against ICASSP 2026 renderings and SPS guidelines (see
`../../resources/official-source-map.md`). Any of these can change by cycle — re-verify before
relying on them.
