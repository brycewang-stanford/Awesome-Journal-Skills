# MobiCom Reproducibility Code Adapter

This directory routes MobiCom authors to the repository-wide ML/systems conference
reproducibility kit and records what that generic kit cannot check for a mobile/wireless-
networking submission. It is deliberately not a copy of the economics (Stata/DiD/IV/RDD)
tooling used by the journal packs.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the artifact tree you intend to submit for ACM badge evaluation
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/mobicom-artifact
```

## What the generic kit cannot verify for MobiCom

The smoke checker inspects package hygiene (manifests, seeds, scripts). A MobiCom artifact
lives or dies on things it cannot see, because the evidence is physical:

- **Radio and hardware provenance** — SDR/USRP model and firmware, RF front-end, antenna
  and gain settings, carrier frequency and bandwidth, and the exact device revisions the
  numbers depend on. An evaluator with a different radio needs these to interpret a
  mismatch (`mobicom-reproducibility`).
- **Channel and environment conditions** — distance, line-of-sight vs multipath, ambient
  interference, and the RSSI/coherence traces behind each figure. A backscatter or sensing
  result without its channel context is not reproducible even with the code
  (`mobicom-experiments`).
- **Mobility realism** — walker paths, speeds, and schedules for mobility experiments, plus
  a stationary fallback an evaluator can run without recruiting people.
- **Energy accounting** — how energy-per-bit or power draw was measured (instrument, shunt,
  sampling rate), since a claimed power budget cannot be re-derived from logs alone.
- **Hardware-optional evaluation path** — a downscaled or trace-replay variant so an AEC
  member without radios can still reach a *Functional* result, since most evaluators will
  not have your testbed (`mobicom-artifact-evaluation`).

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md) and
the live pages it points to, not from this adapter.
