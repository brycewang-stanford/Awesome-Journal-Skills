# ICDM ML Reproducibility Code Adapter

This directory points ICDM authors to the repo-level ML conference methods kit. It is not an
econometrics Stata/DiD/IV/RDD library; it is a lightweight artifact/reproducibility scaffold for
data-mining conference papers, with one ICDM-specific caution: the reproduction package must obey
the **anonymity regime of the track you submit to** — triple-blind for the Research Track,
single-blind for the 2026 Applied Track.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/repro-package
```

For a Research Track submission, run the smoke check on a **freshly exported repository with no git
history, no author paths, and no institutional dataset names** — a triple-blind leak in the
artifact is as fatal as one in the PDF. Use the script as a smoke check only; venue-specific policy
still comes from [`../official-source-map.md`](../official-source-map.md), the current official
track call, and the ICDM skills for experiments, reproducibility, supplementary material, and
submission.
