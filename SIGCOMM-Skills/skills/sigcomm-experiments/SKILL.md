---
name: sigcomm-experiments
description: Use when designing or auditing ACM SIGCOMM experiments — climbing the evidence ladder from microbenchmarks to testbed and trace replay to deployment, choosing baselines that match the deployed state of the art, reporting tail percentiles and variance over repeated trials, mapping break points, and holding the fair variable fixed.
---

# SIGCOMM Experiments

Use this before submission when the evaluation is not yet locked. At SIGCOMM the experiments are
where a mechanism is believed or disbelieved, and the reviewer culture reads a setup for
realism, fairness, and honesty about where the mechanism breaks.

## Experiment audit

- Map each performance claim to a specific microbenchmark, testbed run, trace replay,
  deployment measurement, or documented break point.
- Choose **baselines that fight back**: the strongest deployed alternative, tuned fairly, not a
  straw man the mechanism was built to beat.
- **Report the distribution.** Give the relevant percentiles (P50, P99, and the tail that
  hurts) with variance over repeated trials, and hold the fair variable — throughput, offered
  load, fairness — fixed while you compare.
- Document the setup completely: topology, buffer sizes, workload or trace and its provenance,
  parameters, environment versions, run counts, and seeds.
- Map the **break point**: the workload or condition where the mechanism degrades to the
  baseline. A paper that never shows where its idea stops working invites the reviewer to
  assume it stops everywhere interesting.
- Audit for leakage between motivation and evaluation, unrepresentative traffic, and any
  mismatch between the claimed operating regime and the one actually tested.

## The evidence ladder

| Rung | Evidence | What it proves | Limit |
|---|---|---|---|
| Microbenchmark | Isolated mechanism in a controlled setup | The mechanism does what the principle claims | Says nothing about real traffic |
| Testbed / emulation | Real switches or a faithful emulator under a workload | Behavior under contention and topology | Scale and workload realism bounded |
| Trace replay | A production or representative trace driving the testbed | Behavior under realistic traffic structure | Trace provenance must be defensible |
| Deployment | The mechanism in real operation | It survives the messy real world | Hard to isolate cause; strongest evidence |

Climb as high as the contribution's claim requires. A fabric or transport claim generally needs
at least testbed-plus-trace evidence; simulation-only or mean-only results read as
under-evaluated for such claims.

## What experiments are for here

```text
Not: "we beat every baseline on average across many workloads"
But: "under the traffic that causes the pain we measured, this mechanism
      cuts the tail that hurts, at matched throughput, and here is exactly
      where it stops helping."
```

One decisive experiment under the workload that motivated the paper outweighs five extra
datasets that never stress the mechanism.

## Vignette: evaluating a routing mechanism

A paper proposes backlog-aware rerouting. The matching plan: a microbenchmark showing the
rerouting reacts at the intended timescale; a testbed replaying a production RPC trace to show
the tail-FCT win at matched throughput; sweeps over incast ratio and buffer size to show the
win is not a single-point artifact; and an adversarial workload that removes flowlet gaps to map
the break point where the mechanism degrades to ECMP — each result tied to a numbered claim.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: microbenchmark / testbed / trace / deployment>
[Baseline check] <strongest deployed alternative, tuned fairly? yes/no>
[Tail reporting] <percentiles + variance + matched fair variable>
[Break point] <where the mechanism degrades, and to what>
[Decision-critical next run] <one experiment>
```
