# AAMAS Multiagent Reproducibility Code Adapter

This directory points AAMAS authors to the repo-level ML-conference methods kit. It is not an
econometrics library and not an AAMAS-only framework; it is a lightweight
artifact/reproducibility scaffold that adapts cleanly to multiagent experiments - self-play
sweeps, population-based training, Monte Carlo game simulations, and mechanism evaluations.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

Run the script as a smoke check on the anonymous supplement zip before upload. For multiagent
work, extend the experiment matrix with the axes reviewers actually probe: number of agents,
opponent or population set, training regime (independent, centralized-training/decentralized-
execution, self-play), evaluation opponents, and the random seeds behind every reported
mean. Venue-specific policy still comes from [`../official-source-map.md`](../official-source-map.md),
the current official CFP, and the AAMAS skills for experiments, reproducibility,
supplementary material, and submission.
