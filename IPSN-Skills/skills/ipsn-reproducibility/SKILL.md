---
name: ipsn-reproducibility
description: Use when strengthening IPSN-lineage reproducibility for a hardware/embedded/deployment artifact, covering firmware and board files, pinned toolchains, raw traces and calibration, honest degrees of reproducibility for a physical system, anonymized-but-runnable artifacts, and consistency between the paper and the package.
---

# IPSN Reproducibility

Use this before submission and again before camera-ready. IPSN's artifact and Best Research Artifact
culture makes reproducibility a scored dimension — but a sensor-systems artifact is harder than a
software one: it involves firmware, hardware, physical ground truth, and measurements that depend on
the bench. The goal is that a competent reader could rebuild as much of your evidence as the physical
setup allows, and knows exactly which parts need your hardware.

## Evidence map

- Map each claim and reported number to a **verifiable location** — a paper section, a figure
  generated from logged traces, a firmware build, or a script in the artifact.
- For an **IP-track** method, give the algorithm, parameters, and the analysis scripts that turn raw
  traces into the paper's figures.
- For a **SPOTS-track** platform, ship firmware sources, build instructions, a bill of materials or
  board files, and the pinned toolchain (compiler, SDK, RTOS versions).
- For a **deployment**, ship the raw sensor traces, the ground-truth reference, and the calibration
  data — not only the derived metrics.
- Keep the paper and artifact **consistent**: a number in the PDF that no script or trace in the
  artifact produces is the contradiction reviewers read as carelessness.

## What a sensor-systems artifact contains

| Component | Weak version | IPSN-ready version |
|---|---|---|
| Firmware | "Available on request" | Sources + build instructions + pinned toolchain, flashable or emulatable |
| Hardware | "We built a custom board" | BOM / board files, or a clear statement of what needs the physical board |
| Datasets | "Dataset available on request" | Anonymized raw traces + the exact processing scripts, DOI-archived after acceptance |
| Ground truth | Nothing | Surveyed positions / labels / reference-instrument data with its own error |
| Energy/latency | "Measured on our setup" | The measurement harness + conditions (rail, instrument, clock, runs) |
| Calibration | Implicit | Procedure, date, and drift data |

"Available on request" is treated as *not available*; convert every such line into a concrete,
anonymized package or an explicit, justified exception (e.g., proprietary board, private deployment
site).

## Provenance pinning

```text
[Firmware]   pin compiler/SDK/RTOS versions; record board revision; make the build deterministic
[Traces]     archive raw sensor data with timestamps; record the sensor and sampling regime
[Ground truth] archive the reference data and state its measurement error
[Energy]     record the measurement harness (rail, shunt, instrument, sampling rate) and the platform clock
[Learned parts] record model versions, quantization, seeds; cache inputs/outputs for any offline step
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey (software path):** one documented command regenerates each figure from logged traces.
- **Hardware-in-the-loop:** reproducing requires the board/sensor; you provide firmware, BOM, and a
  clear "you will need X hardware" statement.
- **Deployment-bound:** the in-field result cannot be re-run without the site; you provide the raw
  traces and analysis so the *processing* reproduces even if the *collection* cannot.

For IPSN, aim turnkey for the analysis path (traces → figures) and be explicit about the
hardware/deployment parts that cannot be reproduced without your equipment. Stating the achieved
level honestly beats promising turnkey behavior that fails on an evaluator's bench.

## Anonymized but runnable (double-blind)

- No author/lab strings in firmware repos, board silkscreen, dataset DOIs, or file paths.
- Board photos and scope screenshots stripped of lab logos and watermarks; testbed/site names
  generalized.
- The artifact opens clean: no `.git` history, credentials, or lab-identifying README.

## Consistency and camera-ready pass

- Before submission: every scored number traces to the artifact; the release statement matches
  reality; the package is anonymized.
- Before camera-ready: swap anonymized links for permanent, DOI-issuing archives (Zenodo / IEEE
  DataPort / figshare), restore real names, and align with the badges and Best Research Artifact
  Award you are pursuing (`ipsn-artifact-evaluation`).

## Vignette: a deployment plus estimator

A paper deploys nodes and proposes an estimator. Its reproducibility spine: firmware sources with a
pinned toolchain and board revision; the raw traces and the surveyed ground truth; the calibration
procedure and drift log; the analysis scripts that turn traces into every figure; the
power-measurement harness and conditions; and one honest paragraph on what needs the physical board
and the deployment site and therefore cannot be re-collected — only re-processed.

## Output format

```text
[Claim inventory] <claim -> evidence location (section / figure / firmware / trace / script)>
[Artifact completeness] firmware / BOM / traces / ground truth / calibration / harness present?
[Reproducibility level] turnkey / hardware-in-the-loop / deployment-bound, stated honestly
[Provenance gaps] <toolchain pins / trace archive / energy conditions / seeds>
[Anonymity] package + hardware imagery clean of identity? passed/issues
[Fixes] <paper fixes that must appear + artifact additions before upload>
```
