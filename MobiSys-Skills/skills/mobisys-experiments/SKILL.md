---
name: mobisys-experiments
description: Use when designing or auditing the evaluation of a MobiSys submission — building real-device testbeds, instrumenting energy and thermal behavior, measuring latency and frame-rate tails, bounding memory footprint, choosing tuned system baselines, and running deployments or user studies, so systems reviewers see where the system wins and breaks on the device.
---

# MobiSys Experiments

A MobiSys result becomes believable only when it is **measured on real hardware, driven to
steady state, and reported in latency, energy, memory, and thermal terms**. Simulation-only or
single-run numbers read as under-done. The evaluation axis here is the *device and platform* —
compute, energy, latency, memory, heat — not the radio or channel a wireless venue grades, and
not the traffic-and-topology an infrastructure venue grades. Build the evaluation as one
device-behavior claim per experiment.

## Turn each claim into one device experiment

The clean structure gives each subsection a claim about the running system, then the one
experiment that settles it. The opposite habit — run a benchmark suite and describe whatever
survives — is the unfocused evaluation MobiSys reviewers push back on. The claim-to-experiment
map for a running mobile system:

| Claim about the system | Experiment that settles it | Metrics |
|---|---|---|
| It meets the target in the motivating scenario | on-device run under the real workload | p50/p95 latency, throughput, task success |
| Its energy cost is acceptable | instrumented run on a power monitor | energy-per-operation, average and peak power |
| It survives sustained use | multi-minute run to thermal steady state | frame-rate stability, temperature trace, throttle onset |
| Each mechanism earns its place | component breakdown / ablation | per-mechanism contribution |
| It fits within device memory | peak-memory and storage accounting | peak RSS, model and cache size |
| Its failure mode is understood | hot, low-memory, low-battery device states | the state where a baseline wins |

## What the setup must state

- **The full device context:** phone/board model, SoC, OS build, framework/runtime
  version, battery vs. wall power, and ambient temperature. A number without its device is not
  interpretable.
- **Define the energy boundary:** the power instrument (on-device rail, external monitor,
  shunt + DAQ), the sampling rate, and what is inside the measured envelope (SoC only? whole
  device?). Do not let "efficient" stand in for a measured joules figure.
- **Make load explicit:** the workload trace, its duration, and whether the run reached
  thermal steady state; a 30-second benchmark hides the throttling that a 20-minute run shows.
- **Report ground truth honestly:** for a service or inference claim, how correctness was
  established and its own error.

## Making energy and heat auditable

Battery, energy, and thermal claims are common at MobiSys and are held to instrument-level
scrutiny:

```text
Energy/thermal report checklist:
  instrument: power monitor / on-device rail / shunt + DAQ, sampling rate
  quantity: energy-per-operation (mJ), not just average power (mW)
  boundary: what is inside the measured envelope (SoC? whole device?)
  thermal: skin/SoC temperature trace and whether steady state was reached
  battery: state-of-charge span, or wall power stated explicitly
```

An energy or thermal claim that cannot be re-derived from a described setup should not survive
your own audit.

## Comparators a systems reviewer will trust

- Compare against the **system people actually run**, configured the way its own documentation
  prescribes — an untuned baseline is the most common credibility wound in systems reviewing.
- Include the **do-less** baseline: the trivial fix (a smaller model, a fixed low frame rate,
  more aggressive quantization). If the system cannot beat it at equal quality, that is the
  finding.
- When a competitor cannot be run (proprietary runtime, unavailable device), reimplement and
  label it a reimplementation, or compare on published numbers with the configuration deltas
  stated.

## Report the spread, never a lone peak

- Report **percentiles and confidence intervals** for latency, energy, and throughput; a
  single "up to N×" without the distribution is a review risk (`mobisys-writing-style`).
- Show **tails and CDFs** for headline latency results, and repeat runs across enough
  devices, thermal states, or battery levels to expose run-to-run spread.
- On-device results are **device- and state-dependent** — a number from one phone at full
  charge in a cool room is not a claim about the system until the spread is characterized.

## Pre-submission evaluation pass

- [ ] Every evaluation subsection answers a named question.
- [ ] Device, OS, runtime version, power source, and ambient fully specified per experiment.
- [ ] Energy measured with a described instrument and boundary, not estimated.
- [ ] Sustained-load run reaches steady state; thermal behavior reported.
- [ ] Incumbent-grade baseline present and tuned; do-less baseline present.
- [ ] Percentiles + tails for headline latency; multi-device or multi-state spread reported.
- [ ] At least one device state the system does not win, discussed rather than buried.
- [ ] Numbers in abstract/intro regenerate from the recorded runs.
- [ ] A hardware-optional or downscaled variant exists for artifact evaluators
      (`mobisys-artifact-evaluation`).

## Output format

```text
[Evidence form] on-device measurement / deployment / user study / trace / simulation (claimed vs actual)
[Question map] question -> experiment -> metric (gaps flagged)
[Device+energy] setup and boundary specified? y/n per headline experiment
[Sustained load] steady state reached and thermal reported? y/n
[Baseline audit] incumbent tuned? do-less present?
[Break condition] device state where the system loses: <named or MISSING>
[Priority additions] ordered by review-risk reduction per bench-day
```
