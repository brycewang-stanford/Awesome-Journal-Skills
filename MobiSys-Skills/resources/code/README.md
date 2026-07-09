# MobiSys On-Device Reproducibility Code Adapter

This directory points MobiSys authors to the repo-level ML-conference methods kit. It is not
the economics Stata/DiD/IV/RDD code library; it is a lightweight artifact/reproducibility
scaffold for mobile-systems conference papers, extended with the device-level checks a
MobiSys artifact reviewer actually runs.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-artifact
```

## MobiSys-only checks the generic script cannot make

The shared script verifies README/entry-script/seed hygiene. A MobiSys artifact lives or dies
on device provenance, so add these by hand before an AEC submission:

- **Device and OS provenance.** Record exact phone/board model, SoC, OS build, thermal state
  at run start, and battery vs. wall power; a latency or energy number without its device is
  not interpretable.
- **Energy boundary.** State the power instrument (on-device rail, external monitor, shunt +
  DAQ), the sampling rate, and what is inside the measured envelope (SoC only? whole device?).
- **Hardware-optional path.** Provide a downscaled or emulator path so an evaluator without
  your exact handset can still reach *Functional*, and name which claims that path cannot
  reproduce.
- **Model-version pinning.** Pin framework, runtime, and model checkpoint hashes; on-device ML
  results drift silently across framework minor versions.

Use the script as a smoke check only. Venue-specific policy still comes from
`../official-source-map.md`, the current official CFP and Artifact Evaluation page, and the
MobiSys skills for experiments, reproducibility, supplementary material, and submission.
