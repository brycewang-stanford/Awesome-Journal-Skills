# EctJ Econometrics Methods Code Adapter

This directory points EctJ authors to the repo-level econometrics methods kit.
It is not the applied causal-inference code library; it is a lightweight
simulation, estimator, empirical-illustration, and replication-package scaffold
for econometric methods papers.

## Shared Kit

- [`../../../shared-resources/econometrics-methods/README.md`](../../../shared-resources/econometrics-methods/README.md)
- [`../../../shared-resources/econometrics-methods/simulation-and-replication-checklist.md`](../../../shared-resources/econometrics-methods/simulation-and-replication-checklist.md)
- [`../../../shared-resources/econometrics-methods/code/check_simulation_package.py`](../../../shared-resources/econometrics-methods/code/check_simulation_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/econometrics-methods/code/check_simulation_package.py /path/to/ectj-simulation-package
```

Use the script as a smoke check only. EctJ-specific rules still come from
`../official-source-map.md`, the current RES/OUP instructions, and the EctJ
skills for data analysis, replication, identification, and submission.
