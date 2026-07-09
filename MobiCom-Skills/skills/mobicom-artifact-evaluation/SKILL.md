---
name: mobicom-artifact-evaluation
description: Use when packaging a MobiCom artifact for the evaluation committee — choosing among the three ACM badges as a calibration of what you can prove, building a hardware-optional reproduction path for evaluators without radios, writing the smoke run that establishes functionality, and making code, data, and traces available.
---

# MobiCom Artifact Evaluation

MobiCom accepted papers may earn the three **ACM badges** — *Artifacts Available*,
*Artifacts Evaluated — Functional*, and *Results Reproduced* — from a separate
artifact-evaluation committee (AEC). The badges are independent: you may pursue one, some, or
all. The engineering problem specific to MobiCom is that the evaluation depends on a **radio
testbed the AEC does not have**, so the packaging must let an evaluator get as far as
possible without one.

## Choose badges as a claim of what you can prove

| Badge | What it asserts | What the AEC needs |
|---|---|---|
| Artifacts Available | the artifact is publicly and permanently retrievable | a stable public archive (DOI-backed) |
| Artifacts Evaluated — Functional | the artifact runs and does what the paper describes | a working build + smoke run on reachable hardware |
| Results Reproduced | the paper's key results regenerate | a path from artifact to the headline numbers |

Pick badges honestly. *Available* is almost always worth claiming and is the lowest-friction.
*Functional* requires a path that runs without your specific radios. *Results Reproduced* is
hardest for a wireless paper because the channel is not portable — claim it only where a
trace-replay or downscaled path can regenerate the numbers (`mobicom-reproducibility`). The
exact 2027 badge deadlines and process are 待核实 — read the current artifact call.

## The hardware-optional path is the core deliverable

Most AEC members will not have your SDRs, tags, or testbed. Design the package so a reviewer
without hardware still reaches *Functional*:

```text
artifact/
  README            # claims, badge targets, hardware needed vs optional, time budget
  env/              # container or pinned deps; no radio required to build
  smoke/            # runs in ~minutes on a laptop, no radio; proves the pipeline
  replay/           # recorded captures + decode/analysis -> regenerates key figures
  hardware/         # optional: scripts + exact radio/firmware to reproduce on a testbed
  data/             # traces that can legally ship (or a loader + instructions)
  expected/         # expected outputs AND expected variance ranges
```

- The **smoke run** is the functionality proof: a short, laptop-only command that exercises
  the pipeline end-to-end on bundled data and prints a recognizable result.
- The **replay path** feeds recorded captures through the same processing that produced the
  paper's figures, so results regenerate without the radio.
- The **hardware path** is documented for the rare evaluator (or future reader) with a
  matching testbed, with exact radio model, firmware, and channel setup.

## Make availability real

- Deposit in a **permanent, DOI-backed archive**, not a personal URL that rots.
- Confirm what can legally ship: firmware and proprietary radio stacks often cannot;
  user-identifiable captures must be stripped or aggregated; site data may be bound by an
  agreement (`mobicom-reproducibility`).
- If part of the artifact cannot be released, say so explicitly and ship the largest
  functional subset rather than a broken whole.

## Document variance honestly

An over-the-air result differs run to run. Ship **expected-variance** files alongside
expected outputs so a rerun that lands within a stated margin reads as a reproduction, not a
failure. An AEC member who sees a number move and has no variance guidance will log it as a
non-reproduction.

## Pre-submission checklist

- [ ] Badge targets chosen to match what the package can actually prove.
- [ ] Smoke run works on a clean laptop with no radio, in a stated time budget.
- [ ] Replay path regenerates the key figures from bundled captures.
- [ ] Hardware path documents exact radio/firmware/channel for testbed reproduction.
- [ ] Available artifact is in a permanent DOI-backed archive.
- [ ] Legal/ethical shipping decision made for firmware, traces, and site data.
- [ ] Expected outputs and expected variance both provided.

## Output format

```text
[Badges] targeted vs justified by the package
[Smoke] laptop-only run present + time budget
[Replay] key figures regenerate without hardware? y/n
[Hardware path] radio/firmware/channel documented? y/n
[Availability] archive + DOI + legal-shipping decision
[Gaps] what blocks each targeted badge
```
