# KDD Mining/Deployment Code Adapter

KDD papers carry two kinds of computational evidence — mining-method experiments on
the Research Track and deployment measurements on the ADS Track — and this directory
adapts the repo-level shared ML-conference kit to both. Nothing econometric belongs
here (no Stata/DiD/IV/RDD tooling); the shared kit below is the right scaffold.

## Shared Kit

| File | Role for a KDD package |
| --- | --- |
| [`README.md`](../../../shared-resources/ml-conference-methods/README.md) | Kit overview and conventions |
| [`experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md) | Enumerate variant × dataset × seed runs — the KDD ablation matrix |
| [`reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md) | Pre-upload artifact audit |
| [`check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py) | Dependency-free smoke check of the anonymous package |

## Typical Use

```bash
# from KDD-Skills/resources/code/
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/anonymous-repro-package
```

## Why timing differs at KDD

Run the smoke check **before the paper deadline**: KDD rebuttals forbid hyperlinks,
so the repository referenced in the submission PDF is the only artifact reviewers
will ever open — there is no post-review delivery channel to fix a broken package.

## KDD-specific package additions

- **Scale metadata**: record dataset cardinalities (rows/edges/events), hardware,
  and wall-clock throughput in a manifest so headline scale numbers regenerate
  (`kdd-reproducibility` has the manifest pattern).
- **ADS evidence**: production data rarely ships; include post-launch metric
  definitions, measurement windows, and a synthetic replay generator instead
  (`kdd-artifact-evaluation`).
- **Sample-scale entry point**: a `--sample` path that completes in minutes is what
  a reviewer's realistic ten-minute budget can actually exercise.

The smoke check is a floor, not a policy source: track rules come from
`../official-source-map.md` and the current cycle's CFP for the chosen track.
