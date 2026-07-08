# ASPLOS Reproducibility Code Adapter

This directory routes ASPLOS authors to the repo-level ML/systems conference methods
kit and lists the ASPLOS-specific checks the shared tooling cannot make. It is not an
econometrics kit; it is a scaffold for packaging systems artifacts.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/artifact-package
```

## What the shared kit does NOT cover for ASPLOS

The generic checker validates package hygiene (manifests, seeds, environment files).
An ASPLOS artifact has hardware-shaped obligations on top of that — check these by
hand against `asplos-artifact-evaluation` and `asplos-reproducibility`:

1. **Simulator pinning** — exact simulator commit/version, configuration scripts, and
   the checkpoint or region-selection method, or the numbers are unrepeatable.
2. **Hardware dependency declaration** — the Artifact Appendix must say what silicon,
   FPGA board, or expander the evaluator needs, and what happens if they lack it
   (scaled-down path, provided access, or a simulator fallback).
3. **Kernel and firmware state** — kernel version and config, microcode, BIOS knobs
   (prefetchers, turbo, SMT, NUMA policy) recorded per experiment.
4. **Badge mapping** — which of the Available / Functional / Reproducible badges you
   are requesting and which experiment validates each key result.

Venue policy always comes from the current official pages recorded in
[`../official-source-map.md`](../official-source-map.md), never from this scaffold.
