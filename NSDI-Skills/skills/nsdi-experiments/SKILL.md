---
name: nsdi-experiments
description: Use when designing or auditing the evaluation of an NSDI submission — choosing traces, testbeds, and deployment evidence, sizing scale and failure-injection experiments, picking baselines that fight back, and reporting tail behavior so networked-systems reviewers can see where the design wins, loses, and breaks.
---

# NSDI Experiments

NSDI's phrase is "practical evaluation," and its reviewer culture decodes that as:
realistic traffic, honest baselines, visible tails, and at least one experiment where
the system is *hurt on purpose*. Design the evaluation as a set of questions the
paper must answer, then build the smallest experiment matrix that answers them.

## The evidence ladder

Climb as high as the project honestly can, and say plainly which rung you are on:

1. **Synthetic microbenchmarks** — isolate mechanism costs. Necessary, never
   sufficient; a microbenchmark-only evaluation reads as a workshop draft.
2. **Trace-driven or production-derived workloads on a testbed** — the venue's
   workhorse rung. Provenance of the trace matters as much as its size: say where the
   call graphs, flow mixes, or arrival processes come from and what was scaled.
3. **Real deployment** — production or long-running operational use. This is
   operational-track territory and the strongest evidence NSDI recognizes; do not
   imply it with wording if you are on rung 2 (`nsdi-topic-selection`).

## Questions before benchmarks

Write the evaluation section's subsection titles as questions first — *Does the lease
mechanism help under regional congestion? What does it cost at baseline? When does it
misfire?* — then design one experiment per question. The inverted approach (run
everything, narrate survivors) produces the benchmark tour that NSDI reviews call
unfocused.

A minimal matrix for a design-track paper:

| Question | Experiment | Metrics that answer it |
|---|---|---|
| Does it work under the motivating pain? | replay of the incident-class workload | p99/p99.9 latency, goodput during events |
| What does it cost when the pain is absent? | baseline weeks, no faults | median latency, CPU/memory/bandwidth overhead |
| Why does it work? | component breakdown / ablation | per-mechanism contribution |
| Does it scale? | node / connection / load sweeps | knee location, per-node cost curve |
| When does it break? | adversarial or boundary regimes | the regime where baselines win |
| Does it survive failures? | injected partitions, crashes, stragglers | recovery time, correctness under churn |

## Baselines that fight back

- Compare against the **deployed** incumbent (the mature system operators actually
  run), not only the nearest academic prototype — and tune it the way its own
  documentation says to. An untuned baseline is the most common credibility wound in
  systems reviewing.
- Include the **do-less** baseline: the trivial fix (bigger timeout, more replicas,
  overprovisioning). If the paper cannot beat overprovisioning at equal cost, that is
  the finding.
- When a competitor cannot be run (closed source, unavailable hardware), reimplement
  the mechanism and label it a reimplementation, or compare on published numbers with
  the configuration deltas stated.

## Tails, variance, and time

Networked-systems phenomena live in distributions and in time:

- Report **p99 and above** for any latency claim; medians alone are treated as
  hiding something. Show distributions (CDFs) for headline results.
- Congestion and failover results are **time-dependent** — plot the event timeline
  (before/during/after), not just aggregates over the run.
- Repeat runs across enough trace segments or days to show run-to-run spread; state
  what varies between repeats (seeds, trace slices, background load) and report
  ranges, not single best runs.
- "Up to N×" without the distribution behind it should not survive review — or your
  own audit (`nsdi-writing-style`).

## Testbed and trace hygiene

```text
Per-experiment provenance record (kept as the runs happen, machine-readable):
  topology: nodes, cores/RAM, NIC speed, switch model, RTT matrix
  software: kernel, framework versions, config diffs from defaults
  workload: trace id + collection context + scaling transform
  fault schedule: what was injected, when, by what tool
  outputs: raw logs location + commit hash of analysis scripts
```

This record is simultaneously the reproducibility ledger (`nsdi-reproducibility`),
the artifact-evaluation seed (`nsdi-artifact-evaluation`), and the insurance policy
for a one-shot revision that demands re-running experiments months later on the same
setup (`nsdi-author-response`).

## Budgeting machine time against the two-deadline calendar

Evaluation scope should be sized to the gate being targeted (`nsdi-workflow`): the
question map above, costed in machine-days, tells you whether the fall gate is
reachable or the plan is quietly a spring plan. Two rules of thumb from systems
deadline archaeology: trace-replay pipelines take twice as long to stabilize as to
run, and the break-it experiments — the ones reviewers value most — are always the
ones cut when the schedule slips. Protect them by running the failure-injection
matrix *before* the final scale sweeps, not after.

## Audit checklist

- [ ] Every evaluation subsection answers a named question.
- [ ] Trace/workload provenance stated; scaling transforms disclosed.
- [ ] Incumbent-grade baseline present and tuned; do-less baseline present.
- [ ] Tail percentiles + distributions for latency claims; event timelines for
      dynamic behavior.
- [ ] At least one experiment the design does not win, discussed rather than buried.
- [ ] Failure injection covers the failure modes the design claims to handle.
- [ ] Numbers in abstract/intro regenerate from the recorded runs.
- [ ] Downscaled variant of the headline experiment exists (artifact evaluators and
      revision reviewers will not have your topology).
- [ ] Overheads reported at baseline, not only under the motivating stress.

## Output format

```text
[Evidence rung] micro / trace+testbed / deployment (claimed vs actual)
[Question map] question -> experiment -> metric (gaps flagged)
[Baseline audit] incumbent? tuned? do-less alternative?
[Tail report] percentiles + distribution figures present? y/n per claim
[Break experiment] regime where the design loses: <named or MISSING>
[Priority additions] ordered by review-risk reduction per machine-week
```
