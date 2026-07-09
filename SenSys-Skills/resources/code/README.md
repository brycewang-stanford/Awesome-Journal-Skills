# SenSys Reproducibility Code Adapter

This directory routes SenSys authors to the repository-wide reproducibility kit and records
what that generic kit **cannot** check for an embedded / sensing / on-device-AI submission. It
is deliberately not the economics (Stata/DiD/IV/RDD) tooling used by the journal packs, and it
is not a benchmark-leaderboard harness.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the artifact tree you intend to submit for ACM badge evaluation
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/sensys-artifact
```

Treat the script as a hygiene check on manifests, seeds, and scripts only — it never sees the
physical evidence a SenSys result stands on.

## What the generic kit cannot verify for SenSys

A SenSys artifact lives or dies on measurements the smoke checker cannot read, because the
evidence is physical and time-bound:

- **Energy and power accounting** — how energy-per-operation, average current draw (µA/mA), or
  duty cycle was measured: the instrument (source-meter, shunt, power monitor), its sampling
  rate, and the wake/sleep boundaries. A claimed battery life or energy-harvesting budget
  cannot be re-derived from logs alone (`sensys-experiments`, `sensys-reproducibility`).
- **Hardware and firmware provenance** — MCU/SoC part and clock, sensor make and sampling
  configuration, radio and transmit power, board revision, RTOS/toolchain and compiler flags,
  and battery/harvester specifics. An evaluator on different silicon needs these to read a
  mismatch rather than call it a failure.
- **Sensor ground truth** — how labels or reference values were obtained (reference
  instrument, controlled stimulus, human annotation protocol) and their own error bars.
  Reported accuracy is meaningless without the provenance of the truth it is scored against.
- **On-device model footprint** — for embedded-AI papers, the quantized model size, RAM/flash
  peak, inference latency and its distribution, and the measurement rig — not just offline
  accuracy on a workstation (`sensys-topic-selection`, `sensys-experiments`).
- **Deployment realism and longevity** — placement, environmental conditions, duration, node
  count, and failure/uptime accounting for any long-term deployment, plus a **bench or
  trace-replay fallback** an AEC member can run without your testbed
  (`sensys-artifact-evaluation`).

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md) and the
live pages it points to, not from this adapter.
