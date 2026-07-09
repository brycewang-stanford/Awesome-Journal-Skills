---
name: icassp-experiments
description: Use when designing or auditing ICASSP experiments across signal-processing modalities — matching the metric to the task law (WER, SI-SDR, PESQ/STOI, EER/minDCF, PSNR/SSIM, BER, RMSE), anchoring baselines to current strong methods and standard corpora, sweeping the operating condition, and reporting spread over runs within the four-page limit.
---

# ICASSP Experiments

Use this before submission when the empirical story is not yet locked. ICASSP reviewers are
subfield experts who know the right metric and the right baseline for your task, so the fastest
route to rejection is the **wrong ruler or a stale comparison**. The four pages force a small
number of decisive experiments, not a large number of weak ones.

## Experiment audit

- Map each empirical claim to a specific table, figure, or condition sweep.
- Use the **field-standard metric** for the task; a novel or convenient metric invites the
  "that is not how this task is measured" review.
- Anchor to a **current strong baseline** and a **standard corpus/benchmark**, not to a weak or
  dated reference that flatters the result.
- **Sweep the operating condition** that matters (SNR, reverberation, bit rate, noise level); a
  single-condition number rarely convinces a signal reviewer.
- Report spread over runs (multiple seeds), and say in the caption whether bars are standard
  deviations, standard errors, or confidence intervals.
- Audit for train/test leakage, speaker/scene overlap across splits, and metric computed on the
  wrong crop, alignment, or normalization.

## Match the metric to the task law

| Task | Standard metric(s) | Standard evaluation anchor |
|---|---|---|
| Speech recognition | WER / CER | LibriSpeech, WSJ, or task corpus with fixed split |
| Enhancement / separation | SI-SDR, PESQ, STOI | Matched mixture set, reference-aligned scorer |
| Speaker / language ID | EER, minDCF | Standard trial lists (e.g., VoxCeleb-style) |
| Sound event / audio tagging | mAP, F1, error rate | Fixed labeled set, defined operating point |
| Image / video restoration | PSNR, SSIM | Standard test set, defined borders and depth |
| Communications | BER / BLER vs SNR | Defined channel model and decoder |
| Estimation / detection | RMSE, ROC/AUC | Monte-Carlo trials, bound (Cramér-Rao) if apt |

Reporting the wrong metric family (e.g., classification accuracy for a separation paper) is a
first-round reject pattern; match the ruler to the task before anything else.

## What experiments are for at this venue

- ICASSP experiments exist to **demonstrate a signal-processing mechanism works under realistic
  conditions**, not to top a leaderboard by any margin. One clean condition sweep beats five
  extra datasets at a single point.
- The strongest design isolates the claimed mechanism with an **ablation** and shows it holds
  across the operating range, with the standard baseline drawn on the same axes.
- Where a theoretical bound exists (estimation, detection, coding), compare against it rather than
  only against another method.

## Ablation and sweep stub

```text
Fig. 2: metric vs condition (e.g., SI-SDR vs input SNR, 0-20 dB)
  - proposed (mean ± sd over 3 seeds)
  - strong baseline (same corpus, same scorer)
Table 1: ablation — remove one component at a time, same protocol
  - full method | -component A | -component B | baseline
Report: corpus + split, scorer config, seeds, run count, hardware/runtime
```

## Vignette: a dereverberation paper

A submission claims improved dereverberation. The matching plan: evaluate on a standard reverberant
set with **PESQ and STOI** using a fixed scorer, **sweep reverberation time (RT60)** rather than
reporting one room, ablate the key module, draw a current strong baseline on the same axes, and
report the mean and spread over seeds — every panel tied to the claim it supports.

## Reporting floor

- Seeds and run counts for every stochastic figure; captions state what the error bars are.
- The actual compute and, for real-time claims, the measured latency or real-time factor — not a
  feasibility assertion.
- Honest disclosure of the condition you did **not** test, so a reviewer does not infer you hid it.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Metric fit] task-matched? <metric -> task>
[Baseline] current-strong / standard-corpus? yes/no
[Condition sweep] present over <axis>? yes/no
[Missing evidence] <ablation / spread / baseline / condition>
[Decision-critical next run] <one experiment>
```
