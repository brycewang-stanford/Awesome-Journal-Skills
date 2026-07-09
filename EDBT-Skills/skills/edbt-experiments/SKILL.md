---
name: edbt-experiments
description: Use when designing or auditing EDBT empirical evaluations for database-systems work, covering real workloads and datasets, fair and tuned baselines, honest measurement across realistic scales, reproducible harnesses, and the higher bar of the Experiments & Analysis paper where the measurement itself is the contribution.
---

# EDBT Experiments

Use this before submission when the evaluation is not yet locked. EDBT reviewers are database-systems
empiricists; the evaluation is where a good idea is won or lost. The organizing principle is
**evidence proportional to the claim** — the study must measure the thing the paper actually asserts,
on workloads, datasets, and scales a skeptic would accept, against baselines a skeptic would accept.

## Evaluation audit

- **Match evidence to the claim shape.** A claim about *latency* needs latency measurements under a
  realistic workload; a claim about *scalability* needs runs across a realistic range of sizes/nodes;
  a claim about *space* needs memory/footprint numbers; a claim about *accuracy* needs a labeled
  ground truth. "Faster on a dataset" is not evidence for a scalability claim.
- **Use real workloads and datasets,** named and sourced (standard benchmarks, real query logs, real
  corpora), not a single toy input. Say how the workload was derived.
- **Choose fair, tuned baselines,** including the strongest current technique and a
  simple-but-reasonable alternative, configured with a documented, equal budget. An untuned baseline
  is the most common EDBT reviewer objection.
- **Measure honestly:** report variance across repeated runs, warm/cold state, the metric definition,
  and the hardware/cluster configuration. State what you controlled and what you did not.
- **Cover the regimes:** where the technique helps, where it is neutral, and its overhead or failure
  cases — quantified, not asserted.
- **Make the harness reproducible** (see `edbt-reproducibility`): the evaluation should re-run from
  the artifact rather than being re-measured from scratch.

## Claim-to-evidence design table

| Database claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Lower query latency" | Latency under a named workload vs. tuned baseline, with variance | "One unnamed dataset, no baseline config" |
| "Scales to large data / many nodes" | Runs across a realistic size/node range | "Only small inputs / single node tested" |
| "Lower space / memory" | Footprint measured under realistic load | "Asymptotic argument, no measurement" |
| "Robust to skew / adversarial input" | Results across skew levels incl. worst case | "Only uniform / benign inputs" |
| "General across engines / settings" | Multiple engines or configurations + explicit limits | "One engine, claimed universal" |

## Measurement discipline (database-systems flavor)

```text
[Workload]     name it, source it, say how it was derived; prefer real logs / standard benchmarks
[Baseline]     the strongest current technique, TUNED, with the configuration documented
[Scale]        realistic sizes and node counts; report where behavior changes
[Variance]     repeated runs; report spread, not a single best number
[State]        warm vs cold, cache effects, and what was controlled
[Environment]  hardware, memory, network, engine build/commit — enough to size a reproduction
```

## The Experiments & Analysis paper (a distinct, higher bar)

When the paper's contribution *is* the study — a benchmarking, repeatability, or comparative
analysis — the methodology is not support, it is the deliverable:

```text
[Subjects]     the systems/techniques compared, chosen by a stated, defensible criterion
[Coverage]     the workload and parameter space actually spanned, and what was left out and why
[Fairness]     every compared system tuned by its own experts' guidance, not just yours
[Repeatability] the harness re-runs the whole comparison from the artifact
[Findings]     the analysis, with the surprising or actionable results foregrounded
```

An Experiments & Analysis paper that tunes only its authors' preferred system, or spans a workload
space too narrow to generalize, fails on its core contribution, not on a side point.

## Vignette: evaluating a query-processing operator

Suppose the paper claims an operator lowers straggler time under skew. The matching plan: derive
workloads from real query logs at several skew levels; run the operator and a *tuned* skew-aware
baseline across 8-128 workers; report straggler time and total latency with variance; measure the
overhead on skew-free workloads to bound the worst case; and state the boundary (very short queries,
undetectable skew) with a measurement — every number traceable to a logged run in the artifact.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: workload / metric / scale>
[Baseline fairness] <baseline -> tuned? equal config? documented?>
[Scale + variance] <realistic range tested? variance reported?>
[Regimes] <helps / neutral / cost / failure all measured? yes/no>
[E&A bar (if applicable)] <methodology, coverage, fairness, repeatability adequate?>
[Decision-critical next run] <one experiment to add>
```
