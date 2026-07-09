# RecSys ML Reproducibility Code Adapter

This directory points RecSys authors to the repo-level ML conference methods kit. It is not the
economics Stata/DiD/IV/RDD code library; it is a lightweight artifact/reproducibility scaffold
for recommender-systems conference papers, where a runnable offline pipeline and an anonymous
repository link carry unusual weight.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

Use the script as a smoke check only. For RecSys specifically, the artifact should let a reviewer
regenerate a **top-N ranking table** end to end: fixed dataset version and split, tuned baselines,
a canonical ranking scorer with the cutoff recorded, and seeds. Venue-specific policy still comes
from `../official-source-map.md`, the current official Call for Contributions, and the RecSys
skills for experiments, reproducibility, supplementary material, and submission.
