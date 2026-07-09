---
name: atc-experiments
description: Use when designing or auditing the evaluation of an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) systems paper — matching evidence to the claim with real testbeds, fair baselines, end-to-end plus microbenchmark results, tail-latency and variance reporting, workload realism, and honest cost accounting.
---

# ATC Experiments

Match the evidence to the claim. ATC is the systems community's **implementation-and-measurement**
venue: reviewers read for measured behavior on a real system, not asymptotics or accuracy on a
dataset. In round two, 3-4 reviewers close to your subarea will open the artifact and probe whether
the numbers are end-to-end, fair, and honest about cost. Design the evaluation so their first three
objections are already answered.

## Match evidence to claim shape

| If your claim is... | The evidence ATC expects |
|---|---|
| "Faster / lower latency" | End-to-end latency **including tails (p99/p999)** and throughput at a **matched** operating point, on a described testbed |
| "Lower overhead / cheaper" | The resource cost (CPU, memory, writes, energy) measured, at matched function — not just the headline win |
| "Scales" | Measurements across a real range of load/nodes/cores with the scaling curve and where it bends |
| "More reliable / correct" | Fault-injection or crash/recovery experiments, not just steady-state runs |
| "Useful in practice" (experience) | Production-derived workloads and lessons; what broke and what generalizes |

## Real testbeds and workloads

- **Describe the testbed** so results are reproducible: CPU/NIC/SSD models, core counts, memory,
  kernel/OS versions, network topology, and any co-location. A result without its testbed is not a
  systems result.
- **Use realistic workloads.** Production-derived traces, standard benchmarks, or documented
  generators beat hand-picked inputs. State how the workload was obtained and why it is
  representative; if it is synthetic, justify the parameters.
- **Warm-up and steady state.** Say how you handled cold start, warm-up windows, and measurement
  duration — systems reviewers know where transient effects hide.

## Fair baselines

- Compare against the **strongest reasonable** alternative, configured well (a strawman baseline is
  caught immediately). If you tuned your system, tune the baseline.
- Compare at a **matched cost or operating point**: same memory budget, same flash-write budget,
  same load. An unmatched comparison is the classic systems-reviewer objection.
- If no baseline exists, say so and use the **unmodified system** or an ablation of your own design
  as the reference.

## End-to-end plus microbenchmarks

ATC reviewers want both:

- **End-to-end** results show the contribution matters for the whole system under a real workload.
- **Microbenchmarks** isolate the mechanism, attributing the win (or cost) to your design rather
  than to unrelated system effects. A paper with only end-to-end numbers cannot explain *why*; one
  with only microbenchmarks cannot show it *matters*.

## Tails, variance, and honest reporting

- Report **tail latency** (p99, often p999), not just means — the tail is where systems pain lives.
- Report **variance across repeated runs** (multiple trials, min/max or CIs). A single run is a data
  point, not a result.
- **Report the cost beside the gain**, at the matched operating point (see `atc-writing-style`). A
  win with an unstated cost reads as a hidden weakness.
- State negative or neutral regions honestly — "where the working set fits, our policy neither helps
  nor hurts" builds more trust than a uniformly rosy curve.

## Provenance you cannot reconstruct later

Pin these at collection time — they cannot be recovered at the deadline (see `atc-reproducibility`):

```text
[Hardware]   CPU/NIC/SSD models, core/memory counts, firmware where it matters
[Software]   kernel/OS versions, library and compiler versions, config flags
[Workload]   trace source and date, generator version and seeds, request mix
[Method]     warm-up window, measurement duration, number of runs, aggregation
[Code]       commit SHAs for the system and every baseline
```

## Special cases

- **Concurrency/nondeterminism:** report the distribution and the scheduling/affinity settings, not
  a lucky run.
- **Energy/power claims:** name the measurement instrument and boundary (wall vs. component).
- **Security/isolation claims:** state the threat model and what the measurement does and does not
  cover.
- **Experience papers:** the "evaluation" is the deployment itself — scale, duration, incidents, and
  transferable lessons; ATC's Deployed Systems lane values this even without a new mechanism.

## Output format

```text
[Claim -> evidence] each claim mapped to the experiment that supports it; gaps flagged
[Testbed] hardware/software/workload described enough to reproduce? yes/no
[Baselines] strongest alternative, well-configured, at a matched operating point? yes/no
[Depth] end-to-end AND microbenchmarks present? tails + variance reported?
[Honesty] costs reported beside gains? neutral/negative regions stated?
[Provenance] hardware/software/workload/method/code pinned at collection time? yes/no
```
