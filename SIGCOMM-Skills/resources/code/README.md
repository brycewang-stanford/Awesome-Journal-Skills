# SIGCOMM Reproducibility Code Adapter

This directory points SIGCOMM authors to the repo-level systems/ML conference methods kit.
It is not the economics Stata/DiD/IV/RDD code library; it is a lightweight artifact and
reproducibility scaffold for networking-systems conference papers.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/artifact-package
```

Use the script as a smoke check only. SIGCOMM artifacts also need networking-specific evidence the
generic tool cannot judge: the topology or testbed description, the traffic workload or trace
provenance, packet-level and tail-latency measurement methodology, and the run count behind every
reported percentile. Venue-specific policy still comes from `../official-source-map.md`, the current
official CFP and Call for Artifacts, and the SIGCOMM skills for experiments, reproducibility,
supplementary material, and artifact evaluation.
