---
name: ipsn-writing-style
description: Use when revising an IPSN-lineage paper for a real sensing problem on the first page, a load-bearing information-processing or platform contribution, ground-truth methodology, energy/latency/accuracy budgets, honest deployment reporting, double-blind wording, and disciplined use of the ≤12-page ACM two-column budget.
---

# IPSN Writing Style

Use this when revising the main paper. IPSN papers are read by sensor-systems and
information-processing reviewers, so they need a **real sensing problem on the first page** and
evidence measured on **real hardware against ground truth**. The failure this skill prevents is a
technically fine paper that reads like an offline ML result, or a hardware report with no measured
trade-off.

## Revision rules

- **Lead with the sensing problem and its physical budget:** the phenomenon being sensed, why current
  sensing/processing is inadequate, the contribution (an estimator/inference method and/or a
  platform), the real-hardware evidence, and the energy/latency/accuracy budget that makes it
  deployable.
- **Make the information processing load-bearing (IP track).** State the estimator, inference, or
  learning method precisely enough to re-implement, and tie it to a quantity that matters (error
  bound, joules, bits, latency) — not just "accuracy improved."
- **Make the platform reusable and measured (SPOTS track).** Give the MCU/SoC, sensor, radio, and
  toolchain, and justify design choices with measured power, timing, and robustness — a datasheet is
  not a contribution.
- **Pair every claim with proportional, real-hardware evidence** — a measured energy number, a
  ground-truth-referenced accuracy, a deployment yield — not adjectives.
- **Report deployments honestly.** Yield, synchronization error, packet loss, and energy as
  *measured*; an idealized deployment reads as a tell.
- **Respect the ≤12-page ACM two-column budget** as a design constraint; a paper that only fits by
  cutting the measurement setup or the limits is over-scoped.
- **Maintain double-blind** in self-citations, tool/testbed names, board photos, acknowledgements,
  funding, and dataset links.

## Sensor-systems paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Sensing problem, inadequacy, contribution, real-hardware evidence preview, budget — first page | Leads with a model/technology trend, not a sensing problem |
| Background | The modality, the platform constraints, why this is hard physically | Motivation by assertion; no physical grounding |
| Method / System | The estimator/inference (IP) or the platform/tool (SPOTS), reproducibly | Method too thin to re-implement; platform under-specified |
| Evaluation | Each claim answered with measured, ground-truth evidence | Simulation or offline accuracy standing in for on-device/in-field results |
| Energy/latency budget | Joules, memory, timing as measured on the real platform | "Feasible on embedded devices" with no numbers |
| Limits / threats | Site-specificity, generalization, calibration drift, bounded | Generic paragraph untethered from this system |
| Related work | Delta-first against the sensing literature | Citation catalog with no contrast |

## Sentence-level rewrites

| Draft pattern | IPSN-safe rewrite |
|---|---|
| "Our method significantly improves accuracy." | "reduces localization error to X m (95% CI ...) vs <baseline> on <N real traces>" |
| "It is energy-efficient." | "consumes X µJ per inference on <MCU> at <clock>, measured on an instrumented rail (Table 2)" |
| "We deploy it in the real world." | "deployed <N> nodes for <duration>; packet yield Y%, sync error < Z µs (Fig. 4)" |
| "Runs in real time on embedded devices." | "end-to-end latency X ms on <SoC>; fits <RAM/flash> footprint" |
| "The model detects the event well." | "detection rate D at F false alarms/hour on hand-labeled field audio, per site" |

## Energy/latency/ground-truth discipline

```text
[Energy]     joules or µJ per operation, measured (rail/shunt/instrument named), not estimated
[Latency]    end-to-end timing on the real SoC/MCU at a stated clock; number of runs
[Footprint]  RAM/flash used vs available; where the model/pipeline had to shrink
[Ground truth] the reference (labels, co-located instrument, surveyed positions) and its own error
[Limits]     site-specificity / calibration drift / generalization -> stated next to the result
```

## Vignette: compressing a deployment paper

A draft with a long system tour, six figures, and a thin evaluation: keep the system description at
the level needed to reproduce, the two figures that carry the energy and yield story, a per-site
false-alarm table, and a limits subsection; move the full protocol and secondary plots to the
artifact with forward references. The test of a good cut: a reviewer should be able to answer "what
was measured, on what hardware, against what ground truth, and how well did it hold up?" from the
body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / evidence-mismatched / over-scoped
[First-page fix] <new framing leading with the sensing problem and its budget>
[Claim audit] <claim -> measured evidence -> on real hardware / ground truth? yes/no>
[Budget check] <energy / latency / footprint reported? where>
[Anonymity edits] <tool/testbed names / board photos / self-citations / dataset links to fix>
```
