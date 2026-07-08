---
name: sigmod-experiments
description: Use when designing or auditing the evaluation of a SIGMOD paper, covering workload realism and standard benchmark usage, baseline tuning fairness, scalability and tail-latency methodology, ablations that isolate the mechanism, and the setup disclosure a data-systems PC demands before trusting any speedup.
---

# SIGMOD Experiments

The evaluation section decides most SIGMOD verdicts. A data-systems PC does
not ask whether your system is fast; it asks whether the experiments would
convince the person who built the baseline you beat. Design the evaluation
to survive that specific reader.

## The setup table comes first

Before any result, the paper owes a complete experimental contract: hardware
(CPU, memory, storage class, network), software versions, datasets with
scale, workloads with skew and mix parameters, baseline versions and tuning
provenance, repetition counts, and warm-up policy. At SIGMOD this is not
appendix material — reviewers skim to it before reading the design.

## Workload realism ladder

| Rung | Example | Evidentiary weight |
|---|---|---|
| Microbenchmark | Single-operator stress loop | Explains mechanisms; proves little alone |
| Standard benchmark | TPC-style, YCSB-style suites at stated scale | Comparable across papers; known blind spots |
| Trace-derived | Public or characterized production traces | High, if provenance is disclosed |
| End-to-end application | Full query mix on realistic schema | Highest, rarely achieved |

A SIGMOD-strong evaluation climbs the ladder: microbenchmarks to expose the
mechanism, a standard suite for comparability, and at least one workload
that argues real deployments look like this. An evaluation living entirely
on rung one gets the "toy workloads" objection regardless of speedups.

## Baseline fairness protocol

The evaluation's credibility ceiling is the weakest baseline treatment:

- Use current versions, compiled with the same optimization effort as your
  system, configured per their documentation or authors.
- Enable the competitor's relevant features — comparing your tuned build
  against a default-config rival is the field's best-known foul.
- Where a baseline's own paper reports numbers on similar hardware,
  reconcile: if you measure it slower than its authors did, say why.
- Include the boring-but-strong baseline (a mature engine, a well-indexed
  Postgres, a hand-tuned flat scan); beating only research prototypes
  invites the question you least want.

## Curves, not points

- Scalability: sweep threads/cores/nodes and show the shape; a single-point
  "64-core" result hides the knee reviewers care about.
- Data size: sweep scale factors; crossover points against baselines are
  more informative than any fixed-size win.
- Skew and contention: sweep the skew parameter; uniform-only evaluation of
  a concurrency or caching contribution is near-disqualifying.
- Latency: percentiles across the sweep, since p99 behavior under load is
  frequently where the contribution actually lives (or dies).

## Ablations that isolate the mechanism

If the system adds three techniques, the evaluation must attribute the gain:
a cumulative build-up (base, +A, +A+B, full) or leave-one-out grid. The
review question being preempted is "is the win just the rewrite?" — so where
feasible, include the strongest possible *your-system-minus-the-idea*
configuration as its own baseline.

## Run hygiene

```text
For every plotted point:
  runs >= 5 (or stated justification), report median + spread
  cold vs. warm state declared; caches handled identically across systems
  same measurement harness for all systems; harness in the artifact
  seeds pinned for generated data and workload shuffles
  outlier policy stated before running, not after seeing results
```

Numbers that move between the submitted and revised versions without an
explained cause are a specific, remembered failure mode in multi-round
review — hygiene at first submission protects the revision.

## Matching metrics to contribution type

- Storage/index structures: throughput plus space amplification plus
  build/maintenance cost — one without the others invites the "what did it
  cost" question.
- Transaction/concurrency work: abort rates and tail latency under
  contention, not just committed-throughput peaks.
- Query processing: per-query breakdowns alongside suite totals; a suite
  geomean can hide one catastrophic regression reviewers will find.
- Distributed systems: report behavior during failures and rebalancing,
  not only steady state.
- ML-for-systems: include the training/adaptation cost and the stale-model
  regime; the "what happens when the workload shifts" question is now
  standard at this venue.

## Negative-result honesty

Show where the system loses: the workload regime where the incumbent wins,
the overhead paid on the unfavorable mix. A measured, explained loss buys
more trust with this PC than any additional win, and it pre-writes the
limitations paragraph reviewers will otherwise draft as an objection.

## Output format

```text
[Setup contract] complete / missing items listed
[Ladder position] rungs covered; realism gap
[Baseline audit] versions, tuning, features, reconciliation
[Curve coverage] scalability / size / skew / percentile sweeps present
[Attribution] ablation design isolates each claimed technique yes/no
[Loss map] regimes where the system loses, disclosed or hidden
[Decisive missing run] the one experiment to add before the round
```
