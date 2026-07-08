---
name: kdd-experiments
description: Use when designing or auditing the empirical section of a KDD paper, where evidence combines quality deltas with scalability and efficiency measurements, temporal-leakage-safe splits, mechanism-isolating ablations, tuning-symmetric baselines, and, for the ADS track, post-launch measurement design that survives the desk check.
---

# KDD Experiments

Use this while the experimental plan is still cheap to change. A KDD empirical
section answers four questions in order: does the method win, **at what scale**, at
what computational price, and **because of which mechanism**? Papers that answer only
the first question read as ML-flagship rejects retargeted at KDD — a pattern this
venue's reviewers name openly.

## The four-axis evidence plan

| Axis | Minimum credible evidence | Upgrade that wins reviews |
|---|---|---|
| Quality | Headline metric vs tuned baselines on named datasets with stated sizes | Multiple data regimes (sparse/dense, small/large, static/drifting) showing where the method does and does not help |
| Scale | Largest-dataset run with hardware stated | Scaling curve (time and memory vs data size) with the complexity claim overlaid |
| Efficiency | Wall-clock and memory vs baselines, same hardware | Throughput per component, so the O(·) claim is checkable per stage |
| Mechanism | One ablation removing the claimed contribution | Full mechanism matrix: each named design decision toggled independently |

A missing axis should be a stated limitation, never a silent hole.

## Data hygiene the practitioner-reviewers hunt for

- **Temporal integrity**: any data with a timestamp gets time-ordered splits.
  Random splits on temporal interaction data are the single most-caught flaw in KDD
  reviews — they leak future behavior into training.
- **Leakage audit**: feature construction must be causally valid at prediction time
  (no post-outcome aggregates, no target-derived normalizations).
- **Popularity effects**: for graph/recsys data, report performance stratified by
  node degree or item popularity at least once; aggregate wins that come entirely
  from the head of the distribution are a known illusion.
- **Dataset provenance**: name the snapshot/version; "the Twitter dataset" is not an
  identifiable object.

## Baseline discipline

- Include the boring strong baselines. At KDD, a well-tuned gradient-boosting model,
  a popularity heuristic, or a classical index structure regularly embarrasses
  elaborate architectures — reviewers know it and check for their absence.
- Equalize tuning budgets and disclose them (`kdd-reproducibility`); a grid of 200
  configs for yours vs defaults for theirs is a soundness objection, not a detail.
- Re-implementations must be validated: reproduce the original paper's reported
  number on its dataset before comparing on yours, and say so.

## Ablation logging that isolates mechanisms

```python
# ablations.py - one row per (variant, dataset, seed); the paper's ablation
# table is a groupby over this log, never hand-assembled.
VARIANTS = {
    "full":            dict(drift_weighting=True,  sketch_family=True),
    "-drift_weight":   dict(drift_weighting=False, sketch_family=True),
    "-sketch_family":  dict(drift_weighting=True,  sketch_family=False),
    "base":            dict(drift_weighting=False, sketch_family=False),
}
for name, flags in VARIANTS.items():
    for ds in DATASETS:               # each with row/edge counts in its metadata
        for seed in SEEDS:            # repeats where scale permits
            m = run(config(**flags), dataset=ds, seed=seed)
            log_row(variant=name, dataset=ds.name, seed=seed,
                    auprc=m.auprc, mem_mb=m.peak_mem, evps=m.throughput)
```

The point of the matrix: the paper's central claim ("the gain comes from the drift
weighting") must be attributable from the log alone. Report efficiency columns in the
ablation table too — a component that adds +0.4 quality for 3x memory is a different
result from +0.4 for free.

## ADS-track measurement design

Post-launch quantification is a desk-check item on the 2026 ADS CFP, so design the
measurement, don't just harvest it:

- Prefer a controlled rollout (A/B or interleaving) with stated traffic share and
  duration; where only pre/post is possible, name the confounders in the window
  (seasonality, concurrent launches) and how they were handled.
- Define every online metric exactly once (numerator, denominator, window) and map
  each offline metric to the online metric it was supposed to predict — the
  offline-online correlation discussion is high-value ADS content.
- Report guardrail metrics (latency, cost, complaint rates), not only the success
  metric; practitioners on the committee ask what the win cost.
- If deployment was blocked, the CFP's exception path needs documented evidence of
  the blocker, not a hypothetical deployment story.

## Vignette: auditing a recommendation paper's evidence

A draft claims a new sequential recommender beats five neural baselines on three
datasets. The four-axis audit finds: quality covered; scale absent (largest dataset
is 1M interactions — small for the claim "industrial-scale"); efficiency absent
(training time never reported); mechanism partial (one ablation, but it removes two
components at once). The hygiene audit finds random splits on timestamped data and
no popularity stratification. Repair plan, ordered by review impact:

1. Rebuild splits time-ordered and rerun everything — a result that dies here was
   never real, and finding out pre-submission is the whole point.
2. Split the joint ablation into per-component toggles (the matrix pattern above).
3. Add one genuinely large public interaction dataset or delete the word
   "industrial-scale" from the paper.
4. Add a training-cost column to the main table; if the method is slower, say by how
   much and argue the trade.
5. Add the degree-stratified breakdown for the headline dataset.

Steps 3-5 are a week of compute; step 1 can invalidate the paper. Run it first.

## Reporting floor

- Every stochastic table cell: repeat count and dispersion (IQR or std), or an
  explicit single-seed disclosure at the largest scales.
- Every dataset at first mention: cardinalities (users/items/edges/events), time
  span, and version or snapshot date.
- Every efficiency figure: hardware, software versions, and whether times include
  data loading.
- Every ablation row: identical budget and splits as the full method, or the row is
  not evidence.

## Output format

```text
[Axis coverage] quality/scale/efficiency/mechanism: <present-missing per axis>
[Split integrity] temporal-safe: yes/no; leakage audit: done/open items
[Baseline symmetry] tuning budgets equal + disclosed: yes/no
[Ablation matrix] mechanisms isolated: <list>; efficiency logged alongside: yes/no
[ADS measurement] design: A-B / pre-post / blocked-exception / N-A
[Decision-critical missing run] <the one experiment to do next>
```
