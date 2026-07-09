---
name: sensys-experiments
description: Use when designing or auditing a SenSys evaluation — energy and low-power measurement with a named instrument, real-testbed and deployment realism, honest sensor ground truth, on-device latency and memory, and same-hardware baselines, so the evidence meets SenSys's built-and-measured bar rather than a simulation or offline-benchmark one.
---

# SenSys Experiments

At SenSys the evaluation *is* the contribution's proof. A mechanism is only as strong as the
measurements that show it behaving on real hardware, under real energy budgets, against honest
ground truth. This skill audits an evaluation for the failure modes SenSys reviewers flag first:
unmeasured energy, simulation standing in for deployment, and accuracy scored against an unstated
truth.

## The five measurement axes

Every SenSys evaluation should be explicit about these; a gap in any one is a reviewer question.

| Axis | What to report | Common failure |
|---|---|---|
| **Energy / power** | Energy per operation, average current (µA/mA), duty cycle — with instrument + sampling rate + wake/sleep boundaries | "Low-power" as an adjective; no method |
| **Latency** | On-device latency as a **distribution** (median, tail), not a single number | One workstation timing, no tail |
| **Accuracy vs. ground truth** | Metric plus **how truth was obtained** and its own error | Accuracy with unstated reference |
| **Deployment realism** | Node count, placement, environment, duration, uptime/failures | One-run bench result called a deployment |
| **Footprint (embedded AI)** | Quantized model size, RAM/flash peak on the actual MCU | Offline model size on a workstation |

## Measure energy like it is the headline

Because it is. State the **instrument** (source-meter, shunt + DAQ, or power monitor), its
**sampling rate**, and the **boundaries** of what you integrated (does "energy per inference"
include sensor acquisition and radio, or only compute?). Report energy with the same rigor as a
latency CDF — ideally a power trace annotated with the phases it covers.

```text
Energy reporting template (put the method in the paper, not just the number):
  Instrument:     Keithley/Otii/INA-class monitor, model + firmware
  Sampling rate:  e.g. 10 kHz; enough to resolve the wake spike
  Integration:    from sensor-on to label-out; radio TX included? Y/N
  Boundaries:     sleep floor measured separately; not inferred from datasheet
  Report:         energy/op + duty cycle + projected lifetime with battery/harvester spec
```

A projected battery life or harvesting budget must be **derived from measured draw**, not from a
datasheet's nominal current — reviewers who have deployed will catch the difference.

## Ground truth is a first-class artifact

An accuracy number is only as trustworthy as the truth it is scored against. State how reference
labels were obtained — a reference instrument, a controlled stimulus, or a documented human
annotation protocol — and the truth's **own** uncertainty. Sensor experiments where "ground
truth" is another uncalibrated sensor, or where labels were assigned by the authors without a
protocol, invite exactly the challenge that sinks the result in review.

## Deployment vs. bench, kept separate

Bench experiments *control* variables to isolate a mechanism; deployments *expose* it to reality.
Report both and label which is which. A deployment carries node count, placement, environmental
conditions, **duration**, and honest **uptime/failure accounting** — a node that died on day 3
is data, not an embarrassment to hide. A single controlled bench run is not a deployment claim.

## Baselines on the same hardware

Compare against the right prior system **on the same platform**, tuned as well as your own. An
apples-to-oranges comparison — your system on an optimized MCU against a baseline you ran
untuned, or against numbers copied from a paper that used different silicon — is the most common
reviewer objection. If you must cite cross-hardware numbers, say so and bound the comparison.

## Intermittent power and harvesting

For batteryless or energy-harvesting systems, the evaluation must include the **energy source's
behavior**: the harvest trace (indoor light, RF, vibration), the capacitor/energy-buffer sizing,
and behavior across power failures. A harvesting claim without the input-energy conditions is not
reproducible even with the code (see `sensys-reproducibility`).

## Audit checklist

```text
[ ] Energy reported with instrument + sampling rate + integration boundaries.
[ ] Latency as a distribution (median + tail), measured on the target device.
[ ] Accuracy paired with ground-truth provenance and the truth's own error.
[ ] Deployment: node count, environment, duration, uptime/failures stated.
[ ] Baselines run on the same hardware, tuned; cross-hardware numbers flagged.
[ ] Embedded-AI: quantized size + RAM/flash peak on the actual MCU.
[ ] Harvesting: input-energy trace + buffer sizing + power-failure behavior.
[ ] No simulation-only or single-run claim standing in for deployed behavior.
```

## Output format

```text
[Axes]     which of the five measurement axes are covered / missing
[Energy]   method stated? instrument + sampling rate + boundaries — pass/gap
[Truth]    ground-truth provenance and its error — pass/gap
[Deploy]   deployment realism + honest uptime — pass/gap
[Baseline] same-hardware, tuned comparison — pass/gap
[Open]     the single measurement whose absence most weakens the paper
```
