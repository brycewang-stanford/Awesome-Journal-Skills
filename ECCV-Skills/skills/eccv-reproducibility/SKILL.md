---
name: eccv-reproducibility
description: Use when hardening the reproducibility story of an ECCV paper — training recipes and schedules readers can re-run, dataset versioning and split provenance, pinned foundation-model dependencies, compute disclosure, and seed/variance honesty for benchmark deltas, sized for the 14-page LNCS body plus supplement.
---

# ECCV Reproducibility

Use this before the ECCV paper freeze. ECCV publishes through Springer LNCS
with no standing mandatory reproducibility checklist across cycles (whether
the current cycle adds one: 待核实 against the live author guidelines), so
the reproducibility bar is enforced socially: by reviewers who try to match
your numbers, and by the two-year gap before you could publish a correction
at the same venue.

## The two-year checkability horizon

A CVPR paper's errors are challenged within a year; an ECCV paper sits as
the venue's latest word on the topic until the *next even year*. Write the
paper so a lab starting from only the PDF plus supplement in 2027 can
rebuild the result — that is the horizon reviewers implicitly price in.

## Recipe ledger (goes in paper or supplement, never nowhere)

| Ingredient | Minimum disclosure | Common ECCV-draft omission |
|---|---|---|
| Training schedule | Optimizer, LR schedule, epochs/iterations, batch size, augmentations | Augmentation list "standard" with no definition |
| Initialization | Pretrained checkpoint identity + source | "ImageNet-pretrained" without which checkpoint |
| Data | Dataset version, split definition, filtering rules | Custom val split described only as "held out" |
| Evaluation | Metric implementation source, input resolution, TTA on/off | Resolution mismatch between method and baselines |
| Compute | GPU type, count, wall-clock, total runs behind the paper | Only the final run's cost reported |

## Foundation-model era pinning

Modern ECCV pipelines sit on moving substrates. Pin all of them by exact
identity, because "CLIP features" is not reproducible information:

```yaml
# pinned-substrate block for the supplement
backbone:      dinov2-vitl14, weights sha256:<hash>, source: <url>
vlm:           <model name + exact release tag>, accessed 2026-02
sam_variant:   <checkpoint id>
inference:     fp16, single-crop, resolution 518x518
api_models:    none   # if any API model is used, record date + version string
```

An API-served model that silently updates invalidates comparisons; record
access dates and version strings, and prefer frozen open-weight substrates
for headline tables.

## Variance honesty on benchmark deltas

- A +0.3 mAP or +0.2 mIoU headline delta needs seed evidence: report
  mean ± std over ≥3 seeds for your method *and* your strongest baseline,
  or scope the claim down.
- State which numbers are your re-runs versus quoted from prior papers —
  mixed provenance inside one table is a classic silent irreproducibility.
- If full re-training is too expensive to repeat, say so and report seeds
  on the cheapest deciding component (e.g., the head, not the backbone).

## Split the story across the 14 pages and the supplement

- Body: enough recipe to judge plausibility — schedule summary, data
  versions, compute order-of-magnitude.
- Supplement: the full ledger, per-experiment configs, the pinned-substrate
  block, and negative-result notes ("we tried X at lr=1e-3, diverged").
- Code archive: configs as files, not prose; the paper should never be the
  only serialization of a hyperparameter.

## Honest-failure statement

One paragraph reviewers reward at this venue: name the regime where the
method breaks (small objects, low light, out-of-distribution categories),
with a pointer to a supplement figure showing it. It signals the numbers
were probed rather than curated.

## Output format

```text
[Repro grade] rebuildable-from-paper / rebuildable-with-code / not-rebuildable
[Ledger gaps] <schedule / init / data / eval / compute rows missing>
[Substrate pinning] <unpinned dependency -> exact identity to record>
[Variance status] <headline delta -> seed evidence present?>
[Placement plan] <body vs supplement vs code archive>
```
