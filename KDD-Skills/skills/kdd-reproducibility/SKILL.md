---
name: kdd-reproducibility
description: Use when hardening the reproducibility story of a KDD paper, where reproducibility is an explicit decision factor for area chairs. Covers claim-to-evidence tiers for mining pipelines, seeds and splits on large graphs and streams, baseline-tuning disclosure, compute reporting, and honest limits for ADS deployment results.
---

# KDD Reproducibility

Use this before the paper freezes. The KDD 2026 CFP lists **reproducibility of
results** among the factors area chairs weigh in acceptance recommendations — at this
venue it is a scored dimension, not a virtue. The bar is shaped by what KDD papers
claim: pipelines over large, messy, sometimes proprietary data, where the reader must
be able to tell exactly which parts they can rerun, which they can rebuild, and which
they must take on documented trust.

## Three-tier honesty model

Declare every result in the paper as one of:

1. **Rerunnable** — public data, shipped code, fixed seeds; a reader regenerates the
   number. This should cover the headline comparison table.
2. **Rebuildable** — method fully specified (pseudocode + hyperparameters + data
   schema), but data is proprietary or too large; a reader can reconstruct the pipeline
   on their own data.
3. **Attested** — post-launch/production measurements that no outsider can repeat;
   reproducibility here means the *measurement protocol* is fully specified.

An ADS paper is usually tier 2-3; a Research Track paper claiming tier 1 while
shipping tier 2 is what burns trust in review.

## Mining-pipeline disclosure checklist

The stages that silently decide results in data-mining papers, and what to pin:

| Pipeline stage | What must be pinned | Classic KDD reviewer catch |
|---|---|---|
| Data acquisition | Version/date of each dataset, filtering rules, dedup | "Which snapshot of the graph?" |
| Preprocessing | Feature construction code, normalization, leakage guards | Target leakage via time-travel features |
| Splits | Split logic (temporal vs random), exact seeds, cold-start handling | Random splits on temporal data inflating results |
| Negative sampling | Ratio, distribution, per-epoch resampling or not | Baselines run with a different sampling scheme |
| Baselines | Source of implementation, tuning budget per baseline | Own method tuned for weeks, baselines run at defaults |
| Hardware/compute | Machines, memory, wall-clock per experiment | Throughput claims with no hardware context |

Equal-tuning-budget disclosure matters more at KDD than almost anywhere: the venue's
history is full of boosting/embedding/GNN comparisons decided by tuning asymmetry.

## Config-as-artifact discipline

Every reported number should trace to a committed config, and the mapping should be
mechanical:

```python
# repro/manifest.py - emitted next to every result file
import json, subprocess, time

def write_manifest(cfg, dataset_stats, out="results/manifest.json"):
    manifest = {
        "config_file": cfg.path,              # one config per table row
        "seed": cfg.seed,                     # and the full seed list for repeats
        "dataset": dataset_stats,             # {"name":..., "rows":..., "edges":..., "snapshot":...}
        "git_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"]).decode().strip(),
        "wall_clock_sec": cfg.elapsed,
        "hardware": cfg.hardware,             # e.g. "1x A100-80GB, 256GB RAM"
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    json.dump(manifest, open(out, "w"), indent=2)
```

Tables generated from manifests cannot drift from the artifact — the failure mode
where the PDF says 0.847 and the repo reproduces 0.831 is a rebuttal-phase disaster,
and KDD rebuttals cannot even link to a corrected artifact.

## Stochasticity on large data

- Repeat runs are expensive at KDD scale; the honest compromise is repeats on the
  small/medium datasets plus a variance statement, and single seeded runs at the
  largest scale with the seed published.
- State what is nondeterministic even under a fixed seed (parallel reductions, GPU
  atomics, hash-partitioned sampling), so a near-miss reproduction reads as expected
  rather than as failure.
- Never present a best-of-k run as a typical run; if model selection used validation
  metrics, say k and the selection rule.

## ADS attested-results protocol

For post-launch numbers, reproducibility means specification: metric definitions,
measurement window, traffic allocation, ramp schedule, guardrails, and any seasonal
confounders in the window. A reader should be able to *audit the measurement*, even
though they cannot repeat it. Blur only what confidentiality forces (absolute
denominators can become relative lifts), and say explicitly what was blurred and why.

## Vignette: the tier audit that changed a claim

A recommendation paper reports wins on two public datasets and one "large industrial
dataset." The tier audit finds: public results are rerunnable (good); the industrial
result is attested but the paper's abstract says "we release all code and data" —
written before the legal review pulled the industrial set. Left uncorrected, that
sentence is the kind of paper-vs-reality contradiction a practitioner reviewer
catches in minutes and generalizes from ("what else is oversold?"). The repair:

- Abstract sentence rewritten to "code and the two public datasets are released; the
  industrial pipeline is fully specified in Section 4."
- The industrial section gains the schema, size, and collection-window spec that
  makes it rebuildable-in-principle.
- The headline claim re-anchored on the public results, with the industrial run as
  corroboration rather than as the primary evidence.

Reproducibility review at KDD is largely consistency review: the checklist is the
paper against itself.

## Pre-freeze reproducibility gate

Run this list the week before the paper freezes, while fixes are still cheap:

1. Every number in the abstract traces to a table, and every table row traces to a
   committed config.
2. Tier labels (rerunnable/rebuildable/attested) assigned per result and reflected in
   the availability sentence — no tier inflation anywhere in the text.
3. Split logic re-derived from the code, not from memory; temporal data confirmed
   time-ordered end to end.
4. Baseline provenance table complete: implementation source, version, tuning budget.
5. The manifest of the single largest run (hardware, wall-clock, dataset cardinality)
   exists — it anchors both the scale claim and the compute disclosure.
6. Repository smoke-tested from a clean clone by someone who did not write it.

## Output format

```text
[Tier map] <headline table: rerunnable/rebuildable/attested, per major result>
[Pipeline pins] <acquisition/preprocessing/splits/sampling/baselines/compute status>
[Tuning symmetry] <our budget vs baseline budget, disclosed where>
[Variance story] <repeats + seeds at which scales>
[ADS measurement spec] complete / gaps: <...> / N-A
[Trust risks] <paper-artifact drift, leakage, undeclared selection>
```
