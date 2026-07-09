---
name: recsys-reproducibility
description: Use when strengthening the reproducibility of an ACM RecSys paper or preparing a RecSys Reproducibility Track submission — pinning dataset versions and splits, tuning baselines under an equal budget, reporting seeds and variance, avoiding sampled-metric distortion, and structuring a reproduction study with honest divergence analysis.
---

# RecSys Reproducibility

Reproducibility is unusually load-bearing at RecSys for two reasons. First, the venue runs a
dedicated **Reproducibility Track** for papers that repeat, refute, or re-scope prior results and
for datasets and frameworks that enable future reproduction. Second, the field's own literature
documented how often reported recommender gains fail to survive a fair re-evaluation, so reviewers
of *regular* papers read reproducibility signals as a proxy for whether the gains are real.

## Why recommender results drift: the usual suspects

| Drift source | Typical symptom | Pin it by |
|---|---|---|
| Dataset version / filtering | "MovieLens" numbers differ across papers | Exact version id, k-core filter, and checksums |
| Split protocol | Session results inflated | Temporal or leave-one-last split, not random; document it |
| Baseline tuning asymmetry | Neural method "beats" everything | Equal search budget per system, grid and selected config logged |
| Sampled vs full-ranking metrics | Recall/nDCG off by a lot | Rank over the full item set, or state sampling and cutoff |
| Seeds and nondeterminism | ±0.005 nDCG run to run | Multiple seeds; report mean ± sd, not the best run |
| Metric implementation | nDCG differs at the 3rd decimal | One canonical scorer with cutoff and tie-handling recorded |
| Off-policy propensities | Counterfactual estimate irreproducible | Release logged propensities and the estimator variant (IPS/SNIPS/DR) |

A reproducibility-strong RecSys paper closes each row with an artifact, not a promise: the config
file *is* the documentation.

## Minimum reporting block for any empirical RecSys paper

Put this in the paper (it fits in ~0.3 page and pre-empts three review objections):

- Datasets with versions and filtering; train/validation/test usage; the **split protocol**.
- Tuning protocol: search space, budget, selection metric, validation split — **symmetric across
  systems, baselines included**.
- Metrics: which ones, the cutoff, and whether ranking is over the full item catalog or a sampled
  candidate set.
- Seeds: how many, and whether tables show mean, sd, and a significance test on close results.
- For any deployment or off-policy claim: the estimator, its assumption, and the logged
  propensities.

## The Reproducibility Track specifically

A reproduction paper is first-class work here, not a lesser contribution.

```text
[reproduction scope]  which prior papers, which claims, which datasets
[matched setup]       identical splits, metrics, and — critically — equal tuning budget
[divergence report]   where results reproduce, where they do not, and the diagnosed cause
[new context]         a new domain, dataset, or baseline that tests generality
[artifact]            a runnable pipeline others can extend
```

Honest divergence is the contribution: "we could not reproduce claim X under matched tuning, and
here is why" is publishable when the diagnosis is rigorous.

## Vignette: a session-model reproduction

Consider reproducing three published session recommenders. Its reproducibility spine: the exact
dataset versions and k-core filter, a temporal split shared across all systems, an equal tuning
budget so no method is advantaged by search, full-ranking metrics at a fixed cutoff, five seeds
with mean ± sd, and one honest paragraph on the one result that did not reproduce and the
preprocessing difference that explains it.

## Degrees of reproducibility

- Turnkey: one command regenerates each ranking table from logged seeds.
- Scripted: scripts exist but need documented manual steps or an external dataset download.
- Descriptive: prose detailed enough that a competent reader could rebuild the pipeline.

For RecSys, the offline pipeline should be turnkey because reviewers actually re-run it; a
production A/B result may stay descriptive with the deviation documented. State the achieved level
honestly rather than overpromising a turnkey build that fails on a clean machine.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Reproducibility status] strong / partial / weak
[Drift risks] <dataset version / split / baseline tuning / sampled metrics / seeds / propensities>
[Paper fixes] <must appear in main PDF>
[Repository fixes] <anonymous-repo additions>
```
