---
name: eccv-experiments
description: Use when designing or auditing the experimental program of an ECCV paper — benchmark selection that survives a September conference, matched-substrate baseline fairness in the foundation-model era, ablations that isolate the claimed mechanism, qualitative failure evidence, and run sequencing toward a March freeze.
---

# ECCV Experiments

Use this while the experimental plan is still changeable. ECCV's calendar
shapes the evidence problem: results freeze in early March, reviews weigh
them in May against everything published since, and the field first reads
the paper at a **September** conference — the numbers must still look
current six months after the freeze.

## The six-month-staleness test

For each headline table, ask: *if the strongest lab in this niche publishes
their CVPR camera-ready in June, does this table still support the claim in
September?* Evidence that passes: mechanism-isolating ablations, efficiency
frontiers (accuracy vs compute), and generality sweeps across datasets.
Evidence that fails: a raw leaderboard number 0.2 points above a moving SOTA.
Build the paper's claim on the first kind and let the leaderboard row be
corroboration, not the thesis.

## Matched-substrate fairness

The first thing a 2026-era vision reviewer checks is whether wins come from
the method or from what it was fed:

| Axis to match | Unfair pattern | Fair protocol |
|---|---|---|
| Backbone / pretraining | Your ViT-L vs their ResNet-50 numbers | Re-run the top baselines on your backbone, or add a matched-backbone row |
| Training data | Extra pseudo-labeled or web data only on your side | A same-data row, with the extra-data row labeled as such |
| Input resolution / TTA | Higher test resolution quoted against lower | State resolution and TTA per row |
| Compute / epochs | 4x schedule vs baselines' 1x | Report schedule; add an equal-budget row |
| Foundation-model access | API model in your pipeline, none in baselines | Give baselines the same tool or ablate it out |

One honest matched row protects the paper better than three inflated rows —
the mismatched-substrate objection is the most common substantive ECCV
review attack and cannot be answered in a one-page rebuttal without a
matched number already in hand.

## Ablations that isolate, not decorate

- Each claimed component gets exactly one toggle row; combinatorial grids go
  to the supplement.
- Include the "replace with the dumb version" row (attention → average,
  learned prior → uniform): it distinguishes mechanism from capacity.
- Ablate on the mid-sized benchmark, not the smallest one, so effects clear
  seed noise (`eccv-reproducibility` for the variance bar).

## Qualitative evidence discipline

Vision panels weigh pixels. Ship, in body or supplement: same-scene
comparisons against the two strongest baselines; a random-sample grid (not
curated) for at least one dataset; and a failure panel tied to the
limitations paragraph. A paper with only curated successes reads as hiding
something — the failure panel is credibility infrastructure.

## Run sequencing toward March 5

```text
T-10 weeks:  falsifier first — the experiment most likely to kill the
             claim (matched-substrate row on the main benchmark)
T-8:         main-table runs launched; seeds x3 on deciding rows
T-6:         ablation toggles; efficiency/frontier measurements
T-4:         cross-dataset generality; qualitative harvesting begins
T-2:         freeze new runs; regenerate all tables from logged results
T-1:         random-sample grids, failure panel, supplement tables
T-0 (Mar 5): body tables locked; supplement week polishes, never adds
```

Launching the falsifier first is the ECCV-specific discipline: with a
biennial venue, discovering at T-2 that the matched row erases the win
wastes not a cycle but two years.

## Output format

```text
[Evidence verdict] mechanism-backed / leaderboard-fragile / incomplete
[Staleness test] <headline table -> survives September? why>
[Substrate audit] <axis -> matched / mismatched -> repair row needed>
[Ablation map] <claimed component -> isolating toggle present?>
[Run queue] <next runs in falsifier-first order with weeks-to-freeze>
```
