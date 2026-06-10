# IJCAI ML Reproducibility Code Adapter

This directory points IJCAI authors to the repo-level ML conference methods kit.
It is not the economics Stata/DiD/IV/RDD code library; it is a lightweight
artifact/reproducibility scaffold for AI/ML conference papers.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

Use the script as a smoke check only. Venue-specific policy still comes from
`../official-source-map.md`, the current official CFP, and the IJCAI skills for
experiments, reproducibility, supplementary material, and submission.
