# IPSN Replication-Package Code Adapter

This directory routes IPSN authors to the repository-level shared tooling. It stays deliberately
thin: IPSN-specific *policy* (the IP/SPOTS tracks, double-blind review, CPS-IoT Week logistics, the
Best Research Artifact Award, the SenSys merger) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any artifact.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the IPSN double-blind
  rebuttal in [`../../skills/ipsn-author-response/SKILL.md`](../../skills/ipsn-author-response/SKILL.md).

## Typical use for an IPSN package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ipsn-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current successor
(SenSys) call and the IPSN skills for experiments, reproducibility, and artifact evaluation.

## IPSN-specific checks the generic tooling cannot make

- **Hardware and firmware are part of the artifact.** A sensor-systems artifact is not just Python:
  it includes firmware sources and build instructions, a bill of materials or board files, pinned
  toolchain versions (compiler, SDK, RTOS), and — where the hardware is bespoke — a clear statement
  of what a reviewer without the board can and cannot reproduce
  (`../../skills/ipsn-reproducibility/SKILL.md`).
- **Ground truth and calibration are logged, not assumed.** For a deployment or an estimator, ship
  the ground-truth reference (labels, a co-located reference instrument, surveyed positions), the
  calibration procedure, and the raw sensor traces — not only the derived metrics
  (`../../skills/ipsn-experiments/SKILL.md`).
- **Energy and timing measurements are reproducible.** Document the power-measurement harness (rail,
  shunt, sampling rate, instrument), the compute platform (MCU/SoC and clock), and the number of
  runs, so "X µJ per inference" or "Y ms latency" can be re-measured, not just re-quoted
  (`../../skills/ipsn-experiments/SKILL.md`).
- **The artifact is double-blind at submission.** IPSN review is double-blind, and hardware papers
  leak identity easily: strip lab watermarks from board photos and scope screenshots, anonymize
  firmware-repo owners and dataset/DOI links, and rename testbed/building identifiers
  (`../../skills/ipsn-submission/SKILL.md`).
- **DOI-archived datasets target the Best Research Artifact Award.** Deposit datasets and firmware in
  a DOI-issuing archive (Zenodo / IEEE DataPort / figshare) with an open license; that, plus
  evaluator-proof reuse docs, is what the IPSN Best Research Artifact Award and ACM badges reward
  after acceptance (`../../skills/ipsn-artifact-evaluation/SKILL.md`).
- **Route to the successor.** IPSN merged into SenSys; the artifact deadline, badge set, and award
  are the successor venue's — confirm them on the current SenSys call, not an archived IPSN page.

This is not the econometrics/Stata kit used by the journal packs in this repository, and IPSN
evidence is not offline-leaderboard evidence: do not import DiD notebooks or clean-dataset accuracy
framing here.
