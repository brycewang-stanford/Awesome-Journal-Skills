---
name: ipsn-artifact-evaluation
description: Use when packaging an IPSN-lineage artifact for the ACM badges and the IPSN Best Research Artifact Award, covering hardware-plus-software artifacts (firmware, board files, datasets), what sensor-systems evaluators check first, DOI-issuing archives, evaluator-proof documentation for a physical system, and the separate post-acceptance timing.
---

# IPSN Artifact Evaluation

Use this for the artifact track. IPSN had a strong artifact culture — a **Best Research Artifact
Award** alongside the Best Paper Award — and its artifacts are unusual because they mix **hardware,
firmware, and data**, not just code. Two things to internalize: badges and the award are earned by
evaluators actually using your package, and the review artifact (anonymized, for the paper's
reviewers) is not the same deliverable as the public artifact (de-anonymized, DOI-archived). Because
IPSN merged into SenSys, confirm the current badge set, the award's persistence, and the deadline on
the successor call (待核实).

## Badges and the award (verify the current set)

| Target | What it certifies | What earns it |
|---|---|---|
| Artifacts Available (ACM) | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, IEEE DataPort, figshare, Software Heritage) |
| Artifacts Evaluated - Functional | The artifact runs and does what the paper says | A clean-machine (or emulated) install, a demo, documented expected outputs |
| Artifacts Evaluated - Reusable | Others can build on it | The Functional bar plus careful docs, structure, licensing, and board/firmware detail |
| Results Reproduced | An evaluator reproduced key results | A turnkey analysis path from raw traces to the headline numbers |
| IPSN Best Research Artifact Award | Community recognition of an exceptional artifact | A package an evaluator can genuinely run and reuse, hardware caveats stated honestly |

Available is low-cost, high-value (archive the package). Functional/Reusable/Reproduced require the
evaluator's own run to succeed — and for sensor systems, the failure mode is usually "needs hardware
we don't have," so a **software/analysis path that reproduces from logged traces** is what keeps the
artifact usable when the board is not on the evaluator's bench.

## What sensor-systems evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| An estimator / IP method | The scripts that turn raw traces into the paper's figures | Numbers in the PDF that no script reproduces |
| A platform / SPOTS tool | The firmware build + a run on real or emulated hardware | Undocumented toolchain; only-builds-on-authors'-bench |
| A dataset | The raw traces + the extraction/processing scripts + ground truth | Data shipped without the ground truth or the processing |
| An on-device model | Firmware + quantized model + a way to run inference | Requires the exact board and undocumented setup |
| A deployment | Raw traces + analysis, with a clear "needs the site" statement | In-field numbers no evaluator can approach |

Assume an evaluator gives your package a bounded time budget and may not have your hardware. Design
the analysis path to succeed on any machine; design the hardware path to be honest about what it
needs.

## Packaging plan

```text
[Analysis path]  a turnkey script set that regenerates each figure from logged raw traces, on any machine
[Firmware]       sources + build instructions + pinned toolchain (compiler/SDK/RTOS) + board revision
[Hardware]       BOM / board files, and a clear "you will need X" statement where the board is required
[Data]           raw traces + the ground-truth reference (with its error) + calibration data
[Mapping]        an explicit table: paper claim -> script/firmware -> expected result
[Harness]        the energy/latency measurement setup and conditions, so numbers can be re-measured
[License]        an OSI-approved license for code, an open data license for datasets
[Archive]        DOI-issuing repository for the Available badge (Zenodo / IEEE DataPort / figshare)
```

## Anonymized review artifact vs. public artifact

- **At submission:** anonymized for the paper's reviewers — no owner strings, lab-named testbeds,
  board silkscreen logos, or identity-revealing dataset DOIs; scrub scope-screenshot watermarks.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version evaluators badge, the award judges assess, and the camera-ready cites.

## Worked vignette: packaging an on-device sensing artifact

A paper contributes a TinyML detector and a deployment. To target Reusable, Reproduced, and the
award: ship firmware sources with a pinned toolchain and board revision; a `reproduce/` directory
whose scripts regenerate every figure from the bundled raw traces on any laptop; the quantized model
and a way to run inference (on the board or an emulator); the labeled field traces with ground-truth
error stated; the power-measurement harness and conditions; an MIT/Apache code license and an open
data license; and a DOI archive. State honestly which results are turnkey (analysis from traces) and
which need the physical board or the deployment site.

## Calibration

- The artifact process is typically **post-acceptance** with its own deadline; do not conflate it
  with the camera-ready. Confirm the successor's timing and whether the Best Research Artifact Award
  persists (待核实).
- Badge names, the exact set, and whether evaluation is single- or double-anonymous vary by cycle.

## Output format

```text
[Target] Available / Functional / Reusable / Reproduced / Best Research Artifact Award
[Artifact role] anonymized review artifact / public DOI-archived artifact
[Contents] <firmware / BOM / traces / ground truth / harness / license>
[Analysis path] does figure regeneration from logged traces succeed on any machine? yes/no
[Hardware honesty] is "you will need X hardware" stated clearly? yes/no
[Claim mapping] <claim -> script/firmware -> expected result present? yes/no>
[Fixes before upload] <ordered list>
```
