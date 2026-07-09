---
name: icdm-reproducibility
description: Use when strengthening reproducibility for an ICDM (IEEE International Conference on Data Mining) paper - seeds, configs, compute and data reporting, and an anonymized reproduction package that survives the Research Track's triple-blind regime while every detail fights for room inside the single 10-page IEEE all-inclusive cap.
---

# ICDM Reproducibility

Make the mining result reproducible as *science*, under two ICDM-specific pressures: the
Research Track is **triple-blind**, so the reproduction package cannot reveal identity, and
the reporting all competes for space inside the **10-page all-inclusive cap**. Reproducibility
at ICDM is not a separate checklist form (verify per edition); it is evidence that the
discovery is real rather than a lucky configuration.

## What must be reproducible

- The mining task setup: exact datasets, versions, preprocessing, splits, and how ground truth
  or injections were generated.
- The method: hyperparameters, model selection procedure, the mechanism's knobs (e.g. sketch
  size, partition count), and the random seeds.
- The evaluation: metrics, thresholds/cutoffs, variance estimation, and the hardware behind any
  timing claim.

## Reproducibility tiers

| Tier | What a reviewer can do | How to reach it |
|---|---|---|
| Rerunnable | Re-execute your scripts and get your tables | Pinned deps, seeds, config files, entry script |
| Rebuildable | Reconstruct the pipeline from description alone | Precise protocol in the paper + appendix |
| Attested | Trust numbers that cannot be shared (private data) | Documented protocol + synthetic proxy + honest scope |

Aim for rerunnable on any public-data result; use attested only where data genuinely cannot be
released, and say so plainly.

## Configs as artifacts

Put the run behind a config, not scattered command-line flags, so a reviewer reproduces a table
by pointing at a file.

```yaml
# repro/config.yaml  (anonymized; no author paths, no institutional dataset names)
task: stream_anomaly_ranking
dataset: public_edge_stream_v3      # public source + version, not an internal name
seeds: [0, 1, 2, 3, 4, ... , 19]    # the 20 seeds behind the reported variance
method:
  sketch_partitions: 128            # the mechanism knob mapped in the ablation
  hash_family: multiplicative
eval:
  metric: precision_at_k
  k: 100
  time_respecting_split: true
compute:
  hardware: "1x consumer GPU, 16GB"  # generic; states the basis of any timing claim
```

## Triple-blind the package

- Export a **fresh repository with no git history** — commit metadata routinely leaks author
  names and institutions.
- Remove author paths, usernames, internal dataset names, cluster hostnames, and README
  acknowledgements.
- Host it so the link in the PDF resolves to an anonymized location, not a named account.
- Because ICDM traditionally offers no rebuttal, this package is often the only extra evidence
  a reviewer ever sees — it must be complete and anonymous *at submission time*.

## Report inside the page cap

- The full reproduction protocol can live in an in-cap appendix and the cited repository; the
  body must still state seeds, key hyperparameters, and the compute basis of timing claims.
- Prefer a compact reproducibility paragraph plus a repository over a sprawling appendix that
  eats pages the body needs.

## Vignette: the seed table that answered a review before it was written

A team worried reviewers would read their close margins as noise. Rather than hope for a
rebuttal that ICDM might not offer, they reported every metric with a standard deviation over
20 seeds, shipped the seed list and configs in an anonymized, history-scrubbed repository cited
in the PDF, and stated the exact GPU behind their latency numbers. The "is this just noise?"
review never came, because the paper had already answered it — and nothing in the package
revealed who they were.

## Output format

```text
[Repro tier] rerunnable / rebuildable / attested (per result)
[Seeds+variance] reported: yes / no
[Config-as-artifact] present: yes / no
[Anonymized package] history-scrubbed + no institutional names: yes / leaks found
[Compute basis] hardware behind timing claims stated: yes / no
[Top gap] <single most important missing reproducibility detail>
```
