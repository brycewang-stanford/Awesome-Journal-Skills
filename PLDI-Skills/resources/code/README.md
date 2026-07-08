# PLDI Artifact & Benchmark Code Adapter

This directory routes PLDI authors to the repo-level conference methods kit and
explains how to bend it toward PLDI's artifact-evaluation culture. It is not an
econometrics library and it is not a substitute for the current AE call.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## PLDI-specific adaptations

The shared kit was written for ML conferences, so translate its vocabulary:

- "seeds and hyperparameters" becomes **compiler flags, optimization levels, and
  benchmark-suite versions** — pin all three in a lockfile or Dockerfile.
- "training runs" becomes **benchmark executions**: script warmup iterations,
  repetition counts, and statistics so the evaluator reruns your exact protocol.
- "dataset cards" becomes **benchmark provenance**: where each program came from,
  which were excluded and why (the SIGPLAN Empirical Evaluation Guidelines'
  principled-benchmark-choice item).
- Target the PLDI badge ladder: a `README` + smoke test for **Functional**,
  documented extension points for **Reusable**, and a Zenodo DOI snapshot for
  **Available**.

## Smoke check

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/pldi-artifact
```

Treat a passing check as necessary, never sufficient: PLDI artifact evaluators
build your system inside a fresh VM or container and follow your README literally.
Badge criteria and the AE timetable come from the current research-artifacts track
page recorded in [`../official-source-map.md`](../official-source-map.md), together
with the `pldi-artifact-evaluation` and `pldi-reproducibility` skills.
