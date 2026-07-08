# UIST Systems Reproducibility Code Adapter

This directory adapts the repo-level ML-conference methods kit for UIST use. It is
emphatically not the econometrics Stata/DiD/IV kit; and even the ML kit fits UIST only
partially, because an interface-systems paper's artifact is a running system (often with
hardware), not a training run.

## Shared kit entry points

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the anonymous supplement archive before PCS upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/uist-supplement
```

## Where the generic kit applies at UIST

- Recognition/learning components: seeds, splits, configs, and checkpoint pinning.
- The supplement's structural hygiene: README, manifest, dependency pinning,
  no-identity sweep.
- Experiment matrices for benchmark grids in the technical evaluation.

## What the generic kit cannot check (UIST-specific passes)

1. **Video-figure spec** — duration/resolution/codec and anonymized frames and audio
   (`uist-supplementary` has the ffprobe/ffmpeg commands).
2. **Hardware reconstruction** — BOM completeness, design-file formats, firmware
   versions, calibration procedure with expected readings (`uist-reproducibility`).
3. **Measurement-protocol pinning** — latency boundaries, ground-truth apparatus,
   closed-loop vs component benchmarks (`uist-reproducibility`).
4. **Claim → artifact mapping** — one command or clip per paper claim
   (`uist-artifact-evaluation`).
5. **Overlap attachment** — the anonymized copy of heavily overlapping prior
   submissions that UIST's 2026 rules require (`uist-submission`).

Venue policy always comes from the live `uist.acm.org` pages recorded in
[`../official-source-map.md`](../official-source-map.md), never from tooling defaults.
