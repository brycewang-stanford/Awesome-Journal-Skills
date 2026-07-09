---
name: sensys-artifact-evaluation
description: Use when packaging a SenSys artifact for the Artifact Evaluation Committee — choosing which of the three ACM badges (Available, Functional, Reproduced) to pursue, building a hardware-optional evaluation path for reviewers without your testbed, documenting energy and hardware provenance, and passing the smoke run that proves functionality.
---

# SenSys Artifact Evaluation

SenSys awards **three independent ACM badges** through an Artifact Evaluation Committee:
**Artifacts Available**, **Artifacts Evaluated — Functional**, and **Results Reproduced**. They
are independent — you may pursue one, two, or all three — and awarded badges are printed on the
paper and recorded in the ACM DL. The hard part at SenSys is that your evidence is **physical**:
an evaluator usually does not have your motes, your harvester, or your deployment, so the
artifact must be built to be judged *without* them.

## Choose the badges deliberately

| Badge | Bar | Hardest part at SenSys |
|---|---|---|
| **Artifacts Available** | Artifact deposited in a permanent public archive with a DOI | Deciding what firmware/traces you can legally and safely release |
| **Artifacts Evaluated — Functional** | The artifact runs and does what the paper says | Giving an evaluator without your hardware a way to reach "it runs" |
| **Results Reproduced** | Key results re-obtained by the evaluator | Reproducing hardware-measured energy/latency numbers off your testbed |

Available is the cheapest and worth claiming almost always. Functional and Reproduced are where
the **hardware-optional path** earns its keep.

## Build the hardware-optional path first

Most AEC members will not have your testbed. Give them a graded way in:

```text
Tier 0 — Available:   archived repo (DOI), firmware sources, traces, README.
Tier 1 — Bench/replay: recorded sensor + power traces the analysis re-runs on any laptop,
                       reproducing the paper's figures from stored data.
Tier 2 — Emulation:   a QEMU/renode-class emulator or a single dev board that reaches
                       "it runs" without the full deployment.
Tier 3 — Full HW:     scripts + BOM for an evaluator who does have the platform.
```

A **trace-replay** path is the single most valuable thing you can ship: it lets an evaluator
reproduce your figures from your recorded energy and sensor data even if they cannot re-run the
deployment. Document exactly which figures/tables the replay reproduces and which need hardware.

## Document the provenance the AEC cannot infer

```text
artifact/
  README.md            # claims → which script/trace reproduces each figure/table
  firmware/            # sources + toolchain version + build flags
  traces/              # recorded power + sensor data behind each figure
  analysis/            # scripts that turn traces into the paper's plots
  hardware/            # BOM, board revision, wiring, instrument model + settings
  ENERGY.md            # instrument, sampling rate, integration boundaries
  GROUND_TRUTH.md      # how reference labels were obtained and their error
  LICENSE
```

The `ENERGY.md` and `GROUND_TRUTH.md` files are SenSys-specific: an evaluator reproducing a
number needs the measurement method, not just the code (see `sensys-reproducibility`).

## Smoke-run before you submit

Prove the package installs and runs from clean before an evaluator ever sees it:

```bash
# Package hygiene (manifests, seeds, scripts) — see resources/code/README.md
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py ./artifact
# Then the SenSys-specific smoke: does the trace-replay reproduce a headline figure?
cd artifact/analysis && ./reproduce_fig4.sh   # should regenerate Fig. 4 from traces/, no hardware
```

If the replay does not regenerate a figure on a clean machine, no badge claim is safe yet.

## Work with the AEC's iteration

The committee may ask for revisions and iterate with you. Respond fast and concretely: a missing
dependency or an unclear step is a quick fix, and the AEC is trying to award the badge, not deny
it. Keep the anonymity rules of the round if evaluation overlaps the review window.

## Output format

```text
[Badges]   which of the three you are pursuing, and why each is reachable
[HW-path]  the graded path (Available/Replay/Emulation/Full-HW) — which tiers exist
[Provenance] ENERGY.md + GROUND_TRUTH.md + firmware toolchain present? pass/gap
[Smoke]    does trace-replay reproduce a headline figure on a clean machine? Y/N
[Open]     the gap most likely to block Functional or Reproduced
```
