---
name: ipsn-experiments
description: Use when designing or auditing IPSN-lineage evaluations, covering real testbeds and deployments, ground-truth instrumentation, energy/latency/footprint measurement on real hardware, on-device/TinyML profiling, estimation-theoretic baselines and bounds, and matching evidence to the shape of each sensing claim across the IP and SPOTS tracks.
---

# IPSN Experiments

Use this before submission when the evaluation is not yet locked. IPSN reviewers are sensor-systems
and information-processing specialists; the evaluation is where a good idea is won or lost. The
organizing principle is **evidence measured on real hardware against real ground truth** — the
evaluation must test the sensing claim the paper actually makes, on platforms and baselines a
skeptic would accept.

## Evaluation audit

- **Measure on real hardware, not just simulation.** Simulation can motivate or scale-test, but a
  sensing claim needs real sensors: an estimator run on real traces, a pipeline profiled on the
  actual MCU, a deployment in a real environment. "Simulation only" is IPSN's classic reject.
- **Instrument ground truth.** Localization needs surveyed positions; detection needs hand-labeled
  events; a physical estimate needs a co-located reference instrument. Report the ground truth's own
  error — perfect ground truth is a red flag.
- **Measure energy, latency, and footprint on the platform.** Report joules/µJ per operation from an
  instrumented power rail (name the shunt/instrument/sampling rate), end-to-end latency on the real
  SoC at a stated clock, and RAM/flash used vs available. Estimated energy is not measured energy.
- **Choose fair, real baselines.** Include the strongest prior method and a simple-but-reasonable
  alternative (often a classical-DSP or analytic baseline), run under equal conditions on the same
  hardware. For IP-track claims, compare to an estimation-theoretic bound (e.g., a Cramér-Rao-style
  lower bound) where one exists.
- **Isolate the learning's marginal value (on-device/TinyML).** Ablate the learned component against
  a heuristic/DSP baseline so "did the model help, or the sensing setup?" is answered.
- **Design limits in, not on.** Know before you deploy which site-specificity, calibration drift, and
  generalization limits the study will have, and instrument to bound them.

## Claim-to-evidence design table

| Sensing claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Estimator is more accurate" | Error vs ground truth on real traces, with CIs, vs a tuned baseline / a bound | "Simulated inputs only" |
| "Runs within an energy budget" | Measured µJ/op on an instrumented rail on the real MCU | "Energy estimated from datasheet" |
| "Localizes to X meters" | Surveyed ground-truth positions; error distribution, not just mean | "Ground truth from the same model being tested" |
| "Deploys reliably" | Yield, sync error, packet loss over a real deployment duration | "Idealized single-run numbers" |
| "The on-device model adds value" | Ablation vs classical DSP / heuristic on the same hardware | "Model's marginal contribution never isolated" |
| "Scales to N nodes" | Real or emulated multi-hop at realistic scale, with the bottleneck named | "Two-node bench test, universal claim" |

## On-device / TinyML measurement floor

```text
[Platform]   exact MCU/SoC, clock, RAM/flash; the sensor and sampling regime
[Energy]     µJ per inference/op, instrument named; duty cycle if always-on
[Latency]    end-to-end on-device latency; number of runs and variance
[Footprint]  model/pipeline RAM+flash vs available; what had to be quantized/pruned
[Contamination] for learned components, keep train/field data disjoint; report the split
[Ablation]   learned component vs DSP/heuristic baseline on the same node
```

## Ground-truth and calibration floor

- Name the ground-truth reference and its own measurement error; a claim can be no better than its
  reference.
- Document calibration: procedure, when it was done, and drift over the deployment.
- Archive raw sensor traces and the calibration data, not just derived metrics (see
  `ipsn-reproducibility`).

## Deployment reporting floor

- Report yield (fraction of expected data received), synchronization error, packet loss, and energy
  over the *actual* deployment duration, not a best single run.
- State the environment and why it is representative (or not) — external validity for a physical
  system is site-bound.
- Report failures: nodes that died, data gaps, and what caused them. Honest deployment reporting is
  itself a contribution and a reviewer trust signal.

## Vignette: evaluating a localization estimator (IP track)

The paper claims a new estimator localizes better than the prior method. The matching plan: collect
real RF/acoustic traces at **surveyed** positions; run both estimators on the same traces under equal
tuning; report the full error distribution (not just the mean) with confidence intervals; compare
against the relevant estimation-theoretic bound; and state the environments (indoor/outdoor,
multipath regimes) as a bounded external-validity limit — every number traceable to a logged run and
the surveyed ground truth in the artifact.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: platform / ground truth / metric / statistic>
[Real-hardware check] measured on real sensors/MCU, not simulation only? yes/no
[Energy accounting] <µJ/op measured? instrument named? footprint reported?>
[Baseline fairness] <strongest prior + simple baseline, equal conditions, same hardware?>
[Limits-by-design] <site / calibration / generalization -> instrumentation to bound it>
[Decision-critical next run] <one experiment or deployment extension>
```
