---
name: icdm-experiments
description: Use when designing or auditing the empirical evaluation for an ICDM (IEEE International Conference on Data Mining) paper - mining-task definition, strong and fairly-tuned baselines, ablations that isolate the named mechanism, scalability curves that test scale claims, and discovery-validity checks that separate real findings from evaluation artifacts.
---

# ICDM Experiments

Design the evaluation an ICDM reviewer will trust: a defined mining task, baselines tuned as
carefully as your method, ablations that isolate the mechanism, a measured scale story, and a
discovery-validity argument. ICDM's data-centric reviewers punish leaderboard-only wins and
un-checkable discovery claims, and the whole evaluation must fit inside the 10-page
all-inclusive cap.

## Define the mining task before the metric

- State the task operationally: inputs, outputs, and what a correct answer is. "Anomaly
  detection" is a genre; "rank edges by anomalousness in a one-pass stream, evaluated against
  injected ground truth" is a task.
- Fix the evaluation protocol — splits, negatives, thresholds, ranking cutoffs — before
  running anything, and describe it precisely enough to reproduce inside the page cap.

## The four evidence axes

| Axis | Question it answers | Typical evidence |
|---|---|---|
| Quality | Is the mining result good on the task? | Ranking/accuracy vs baselines with variance |
| Scale | Does the scale claim hold? | Latency/memory curves across data sizes |
| Mechanism | Is the *named mechanism* the reason? | Ablations toggling exactly that component |
| Validity | Is the finding real, not an artifact? | Controlled injections, known-truth checks |

A strong ICDM paper touches all four; missing "mechanism" or "validity" is the usual reason a
methodologically fine paper reads as thin.

## Baselines and tuning symmetry

- Compare against current strong baselines, and tune them with the **same budget** you gave
  your method; an under-tuned baseline is the fastest way to lose reviewer trust.
- Include the obvious simple baseline. If a cheap method nearly matches you, say so and argue
  the regime where your mechanism pays off.
- Report every number with variance over seeded runs; a single-run table invites the "is this
  noise?" review.

## Ablations that isolate the mechanism

The mechanism-attached novelty of `icdm-writing-style` must be *demonstrated*, not asserted.

```text
Mechanism: single-pass isolation sketch with m random partitions.
Ablation grid:
  - remove the sketch, keep full storage      -> isolates the streaming contribution
  - vary m (partition count)                  -> maps the accuracy/memory knob
  - swap the hash family                       -> tests sensitivity to the mechanism's core
  - replace isolation score with density score -> isolates the isolation principle
Each row answers "was THIS the reason it worked?"
```

## Test the scale claim, do not assert it

- If you claim scalability, plot behavior across at least an order of magnitude of data size,
  and report the cost model (linear, sub-linear memory, amortized constant update).
- Separate wall-clock from asymptotic claims; hardware-dependent speedups need the hardware
  stated and, ideally, an operation count that is not hardware-dependent.

## Discovery validity: the ICDM instinct

- Where truth is unknown, build a setting where it is: injected anomalies, planted patterns,
  synthetic graphs with known structure — so you can show the method recovers *known* signal.
- Guard against leakage: temporal tasks need time-respecting splits; graph tasks need to avoid
  train/test edge overlap. State the guard explicitly.
- Do not overclaim when differences are within variance; an honest "matches at lower cost" is
  stronger here than a fragile "outperforms."

## Vignette: an ablation that saved the claim

A team reports strong stream-anomaly numbers but reviewers cannot tell whether the sketch or
the underlying isolation criterion did the work. Adding two ablation rows — full-storage
isolation (isolating the streaming contribution) and a density-score swap (isolating the
isolation principle) — showed the sketch preserved batch quality while the isolation principle
drove detection. The claim survived because the mechanism was *shown*, not stated, and both
rows fit in the appendix inside the 10-page cap.

## Output format

```text
[Task] <operational task definition>
[Axes covered] quality / scale / mechanism / validity - list gaps
[Baselines] strong + tuned symmetrically: yes / no
[Ablation] isolates the named mechanism: yes / no
[Validity] known-truth or leakage-guarded: yes / no
[Top evidence gap] <single most important missing experiment>
```
