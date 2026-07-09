---
name: mobisys-reproducibility
description: Use when strengthening MobiSys reproducibility evidence — capturing device, SoC, OS build, framework and model versions, power-instrument setup, seeds, and thermal conditions so an on-device result survives a different phone, deciding what data and firmware can legally ship, and keeping the paper consistent with the artifact for the ACM badge pipeline.
---

# MobiSys Reproducibility

Use this before submission and again before the artifact-evaluation deadline. On-device
results are fragile across hardware and framework versions, so reproducibility at MobiSys is
mostly about **provenance**: recording enough of the device and measurement context that
someone on a different phone can rebuild the result.

## Evidence map

- Map each latency, energy, throughput, and accuracy claim to a verifiable location in the
  paper, appendix, or artifact package.
- For each on-device result, record device model, SoC, OS build, framework/runtime version,
  model checkpoint hash, power source, ambient temperature, and thermal state at run start.
- Record the power-instrument setup and the energy boundary so an energy figure can be
  re-derived rather than trusted.
- For stochastic results, report seeds, repeated runs, and the spread; a single number from a
  single phone is not reproducible evidence.
- Explain missing data, firmware, or hardware honestly, and describe how a reader could
  reproduce the result in principle on a different device.
- Keep the artifact consistent with the manuscript; a number in the PDF that the artifact
  cannot regenerate is a review-risk multiplier and an AEC failure.

## What survives a different device

| Provenance item | Turnkey answer | Common failure caught |
|---|---|---|
| Device + SoC + OS build | Named per experiment, in a table | "on a mobile device" with no model |
| Framework / runtime version | Pinned with hashes | Result drifts silently across a minor version |
| Energy instrument + boundary | Instrument, sampling rate, envelope stated | "efficient" with no measured joules |
| Thermal state | Ambient + steady-state trace | 30-second benchmark hides throttling |
| Model / cache version | Checkpoint hash, cache size | Accuracy irreproducible from a different weight file |

Marking a device result "reproducible" without its provenance is a recognizable MobiSys red
flag, because the AEC and reviewers cross-check the artifact against the PDF and read a gap as
carelessness about the rest of the paper.

## Vignette: an on-device inference paper

Consider a runtime that keeps CNN latency stable under load, validated on four phones. Its
reproducibility spine: the four device models and OS builds, the runtime version and model
checkpoint hashes, the power-monitor model and sampling rate, the ambient temperature and the
steady-state thermal traces, the workload trace, the seeds and run counts — plus one honest
sentence about the device it could *not* test and why the result may differ there.

## Degrees of reproducibility

- **Turnkey:** one script regenerates each figure from logged runs on the target device.
- **Scripted:** scripts exist but need the specific hardware or manual device setup.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline on
  a comparable device.

For MobiSys, the on-device measurement path should be as turnkey as the hardware allows, and a
**hardware-optional** downscaled or emulator path should let an evaluator without your exact
device reach at least *Functional* (`mobisys-artifact-evaluation`). State the achieved level
honestly rather than overpromising turnkey behavior that fails on a different phone.

## Legal and privacy provenance

- Decide early what **traces, firmware, and datasets** can ship; on-device data often carries
  user, sensor, or vendor-firmware restrictions.
- Strip identifying content from screenshots, logs, and demo media before release.
- If data cannot ship, provide a synthetic or public substitute and name which results it
  cannot reproduce.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Provenance status] complete / partial / missing (device/OS/runtime/energy/thermal)
[Reproducibility gaps] <device pinning / seeds / energy boundary / model version>
[Paper fixes] <must appear in main PDF>
[Artifact fixes] <appendix or artifact additions, incl. hardware-optional path>
```
