---
name: acmmm-experiments
description: Use when designing or auditing the experiments of an ACM MM (ACM Multimedia) paper — matched baselines per modality, ablations that isolate the cross-modal fusion, user studies or QoE measurement where the claim is subjective, dataset and media licensing, and honest compute reporting, so evidence supports a multimedia claim.
---

# ACM MM Experiments

Use this to make an ACM Multimedia paper's evidence match its claim. The reviewer's implicit
questions are: does it work, **does the cross-modal part cause the gain**, when does it fail,
and — if the target is perceptual — do people actually prefer it.

## The four questions and how to answer them

| Question | Evidence that answers it |
|---|---|
| Does it work? | The headline metric on a recognized benchmark, against strong, matched baselines |
| Does the *fusion* cause the gain? | A leave-one-modality-out / component ablation isolating the cross-modal term |
| When does it fail? | Failure cases per modality (e.g., noisy audio, missing captions) shown honestly |
| Do people prefer it? | A user study with reported N, protocol, and inter-rater agreement — for subjective claims |

The second row is what separates an ACM MM experiment section from a single-modality one:
if removing a modality does not move the result, the paper is not really cross-modal.

## Matched baselines

- Compare against the **strongest** existing method, re-run under your data and preprocessing
  where feasible, not a weakened reimplementation.
- Include a **late-fusion / naive-concatenation** baseline so the reader sees what the fancy
  fusion buys over the obvious one.
- Hold everything but the mechanism fixed: same backbone, same features, same training budget,
  so the delta is attributable.

## Ablations that isolate the cross-modal claim

```text
Full model .................... reference
- audio stream ................ tests whether audio carries signal
- text/caption stream ......... tests whether language carries signal
- alignment / fusion module ... replaced by concatenation: tests the MECHANISM
- synchronization assumption .. shuffled timing: tests whether cross-modal timing matters
```

Report each ablation with the same metric and variance as the headline, and state which term
carries most of the gain — reviewers reward a paper that can point to *why* it works.

## User studies and QoE

When the claim is subjective (quality, naturalness, engagement, aesthetics), a benchmark
number is not enough:

- Pre-register the protocol: task, number of raters, stimuli, and the question asked.
- Report **inter-rater agreement** and a significance test, not just a mean preference.
- Describe compensation and consent briefly; a study a reviewer cannot assess is discounted.

## Data, media, and compute honesty

- State dataset **licenses** and any consent/usage terms for media, especially for
  user-generated or scraped content.
- Report **compute** (hardware, training time) so cost is legible; a cross-modal model that
  only wins at 10x compute should say so.
- Fix and report **seeds**; report variance over runs where the margin is small.

## Benchmarks and metrics per modality

A cross-modal paper is judged against each community's expectations at once, so pick metrics
each sub-field recognizes rather than a single convenient number.

- **Retrieval / recommendation** — report ranking metrics (Recall@K, mAP, NDCG) *and* say which
  gallery/query split, because cross-modal retrieval numbers are split-sensitive.
- **Generation / synthesis** — pair a distributional metric with a **human/QoE** judgment;
  automatic scores for generated media correlate imperfectly with perceived quality.
- **Recognition / detection** — use the standard task metric, but show the *multimodal* case, not
  only the clean single-modality one.
- **Systems / delivery** — report latency, throughput, and bitrate/quality trade-offs, not just
  accuracy.

State the metric's direction and any threshold, and keep the same metric across the headline
table and every ablation so the reader can trace the fusion's contribution row by row.

## Statistical reporting

- Report **variance** (standard deviation or confidence interval) over runs when margins are
  small; a single-seed win on a close benchmark is not persuasive.
- For **user studies**, report a significance test and inter-rater agreement, not a bare mean.
- Do not average away modality-specific behavior: a model that helps on audio-rich clips and
  hurts on silent ones should show that split, not hide it in a global mean.

## Common ACM MM experiment failures

- **Fusion that does not matter** — ablations show no modality is load-bearing.
- **Weak baselines** — beating only a vision-only or text-only strawman.
- **Asserted perception** — "more natural" with no user study.
- **Unlicensed media** — datasets used without stating rights.
- **Hidden cost** — big gains that quietly require far more compute.

## Output format

```text
[Works] strong/matched baselines / weak or unmatched: <which>
[Fusion causal] ablation isolates the mechanism / does not
[Failure analysis] present per modality / missing
[Perceptual claim] user study with agreement / asserted
[Data + compute] licenses and cost reported / gaps: <list>
[Top fixes] <ordered before submission or rebuttal>
```
