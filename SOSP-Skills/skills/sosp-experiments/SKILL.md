---
name: sosp-experiments
description: Use when designing or auditing the evaluation of a SOSP paper — mapping every claim to an experiment, choosing baselines a systems PC will accept as fair, mixing microbenchmarks with end-to-end and failure runs, reporting tails and overheads honestly, and isolating the mechanism the design credits.
---

# SOSP Experiments

Use this while the evaluation is being designed — it determines whether the paper is
writable at all. SOSP reviews concentrate their negative weight on evaluation
soundness, and the venue's response phase forbids new experiments (CFP, 2026 cycle,
checked 2026-07-08), so a hole discovered in review stays a hole. The evaluation's
job is to make each claim's evidence findable, fair, and attributable to the
mechanism the paper credits.

## Claims first, experiments second

Write the claim list before designing runs; every evaluation subsection should open
by naming the claim it discharges.

| Claim type | Required evidence | Classic hole |
|---|---|---|
| "Foo improves throughput/latency" | End-to-end runs vs tuned state-of-the-art baselines, real + synthetic workloads | Baseline in default config while Foo is hand-tuned |
| "The gain comes from mechanism M" | Ablation: Foo with M disabled, or M grafted onto the baseline | Whole-system win credited to one component on faith |
| "Overhead is acceptable" | Cost measured where it hurts: memory, CPU, write amplification, the workload M does not help | Only the favorable workload reported |
| "Foo survives failures" | Kill/partition/restart runs with recovery-time distributions | Availability claimed, only steady state measured |
| "Foo scales" | Sweep to the knee, with the bottleneck at the knee identified | Straight-line plot ending before saturation |
| "Correctness holds under concurrency" | Stress + targeted schedules, or a verification argument | "We ran it for days" |

## Baselines a systems PC accepts

- Compare against the **published state of the art**, not only your own strawman
  variants; if the strongest system is unrunnable (dead code, unobtainable
  hardware), say so in the paper and compare against its published numbers with
  the configuration deltas spelled out.
- Tune the baseline with the same care as your system, and document both tunings.
  "We used X's defaults" invites the PC member who built X to explain what the
  defaults are for.
- Match the fairness surface: same kernel, same mitigations, same NIC firmware,
  same warm-up policy. An OS-level artifact changes the platform under everything,
  so baseline runs need the environment pinned too (see `sosp-reproducibility`).

## Workloads: three layers, each with a job

1. **Microbenchmarks** isolate mechanisms and expose costs; they prove *why*.
2. **Application-level or end-to-end workloads** (real applications on top of the
   system) prove the *why* matters; a syscall-path win that vanishes under a real
   application is a finding, not a failure to report.
3. **Trace-driven runs** on production or public traces prove relevance; when the
   trace is private, characterize it and pair it with a matched synthetic
   generator (the tiering that artifact evaluation later formalizes).

## Tails, variance, and the numbers reviewers check first

Systems effects live in distributions, and SOSP reviewers reach for the tail:

- Report p50/p99 (p999 where the claim warrants) with repetition counts and spread;
  a single-run p99 will be called folklore.
- State the load point for every latency number — latency without offered load is
  meaningless, and latency-throughput curves beat point pairs.
- Account for the denominator: speedups over a baseline that is itself
  misconfigured are the fastest way to lose the room at the PC meeting.

```text
Evaluation matrix (one row per claim; freeze before the writing sprint)

claim                      experiment            workload/trace     baseline+tuning   metric+spread      figure
throughput at scale        e2e sweep to knee     YCSB-B + trace T1  X v2.3 tuned §6.1 ops/s, 5 runs, CI  Fig 6
gain attributable to M     ablation Foo-noM      YCSB-B             Foo itself        delta ops/s        Fig 7
recovery independent of    kill @ 3 log sizes    trace T1           X                 p50/p99 recov, 10x Fig 9
  log size
overhead where M is idle   read-only run         YCSB-C             X                 CPU%, mem, 5 runs  Tab 4
```

## Honesty as a strategy

The evaluation section is also where credibility is banked for the PC meeting. Report
the workload where the design loses, and explain the regime boundary — a measured
loss with a mechanism story reads as understanding; a suspiciously uniform sweep of
wins reads as curation. Reviewers at this venue have written these sections
themselves; the fastest way to earn a champion is an evaluation that anticipates the
attack they were about to write.

## Output format

```text
[Claim map] every paper claim -> experiment row? orphans: <list>
[Baseline audit] SOTA present? tuning documented both sides?
[Layer coverage] micro / end-to-end / trace — gaps
[Tail discipline] spreads + load points on all latency numbers?
[Attribution] ablations isolate the credited mechanism?
[Adverse results] where the design loses + is it in the paper?
```
