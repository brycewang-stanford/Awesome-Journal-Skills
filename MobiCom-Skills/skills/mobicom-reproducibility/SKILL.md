---
name: mobicom-reproducibility
description: Use when making a MobiCom result reproducible on a different testbed — recording radio, hardware, channel, and mobility provenance as the runs happen, characterizing the variance that over-the-air measurement introduces, and deciding early which traces, firmware, and deployment data can legally and safely ship for artifact evaluation.
---

# MobiCom Reproducibility

Reproducibility at MobiCom is harder than at a compute-only venue because the experiment
includes a **physical radio channel that no one else has**. The goal is not bit-identical
reruns; it is enough provenance that a reader with a *different* testbed can tell whether a
mismatch is their setup or your claim. Provenance is captured while the runs happen — it
cannot be reconstructed after the testbed is torn down.

## The provenance ledger

Keep a machine-readable record per experiment, written as the run executes:

```text
Per-run provenance record:
  radio:     SDR/NIC model, firmware/driver version, carrier freq, bandwidth, TX power
  rf_frontend: antenna type, gain, cabling, amplifiers
  topology:  node count, positions/distances, LOS/NLOS, host specs
  channel:   RSSI/CSI traces, measured interference, coherence-time estimate
  mobility:  walker paths, speeds, schedule (or "stationary")
  energy:    instrument, sampling rate, measured boundary
  software:  code commit hash, config diffs from defaults, analysis-script hash
  outputs:   raw-capture location, per-figure derivation script
```

This ledger is simultaneously the evaluation record (`mobicom-experiments`), the
artifact-evaluation seed (`mobicom-artifact-evaluation`), and the insurance policy for a
one-shot revision that asks you to re-run months later on the same setup
(`mobicom-author-response`).

## Characterize the variance, do not hide it

Over-the-air numbers move between runs. A reproducible MobiCom result states its spread:

| Source of variance | How to characterize it |
|---|---|
| Channel realization | repeat across times of day / room states; report the distribution |
| Interference | log the ambient band occupancy during runs; note co-channel activity |
| Hardware unit | test more than one radio/tag where feasible; note per-unit drift |
| Mobility | multiple walker paths and speeds; report per-path spread |
| Thermal / time | long runs to expose drift; report start-vs-end |

If a headline figure comes from one favorable channel realization, it is not yet a claim
about the mechanism — say what varied and report the range, not the best run.

## What can legally and safely ship

Decide early, because it constrains both the artifact and the anonymity sweep:

- **Raw captures and traces:** confirm the collection did not record identifiable users or
  protected content; strip or aggregate what cannot ship. IRB or site conditions may bind
  release.
- **Firmware and proprietary radio stacks:** often not redistributable — plan a description
  and a substitute rather than a broken artifact.
- **Deployment-site data:** building maps, floor plans, or site identifiers can both
  de-anonymize (`mobicom-submission`) and violate a site agreement; generalize them.
- **Third-party datasets:** ship a loader and instructions, not a re-hosted copy, unless the
  license permits.

## A hardware-optional reproduction path

Most readers and most artifact evaluators will not have your radios. Plan, from the start, a
path that does not require them:

- A **trace-replay** mode that feeds recorded captures through the same decode/analysis
  pipeline, so the processing is reproducible without a testbed.
- A **downscaled** configuration (fewer nodes, shorter distance) an evaluator can run on
  common hardware to reach a *Functional* result.
- Expected-output *and* expected-variance files, so a rerun that differs by a known margin
  reads as success, not failure.

## Audit checklist

- [ ] Provenance ledger captured per run, not reconstructed.
- [ ] RF, channel, and mobility conditions recorded with each headline result.
- [ ] Variance sources characterized; ranges reported, not single best runs.
- [ ] Legal/ethical shipping decision made for traces, firmware, and site data.
- [ ] Trace-replay or downscaled path exists for testbed-less reproduction.
- [ ] Analysis scripts version-pinned to the raw captures they consume.

## Output format

```text
[Provenance] ledger present per run? gaps named
[Variance] which sources characterized; which unmeasured
[Shipping] traces / firmware / site data — ship, strip, or substitute (each)
[Testbed-less path] trace-replay / downscaled present? y/n
[Risks] the reruns most likely to diverge, and why
```
