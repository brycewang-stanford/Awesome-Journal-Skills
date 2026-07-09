---
name: ppopp-experiments
description: Use when designing or auditing a PPoPP paper's evaluation, covering the twin bar of concurrency correctness and measured scalability — speedup curves, strong vs weak scaling, core/thread sweeps, NUMA and GPU effects, contention microbenchmarks plus real workloads, variance and measurement hygiene, and honest strong baselines.
---

# PPoPP Experiments

Design the evaluation to clear PPoPP's **twin bar**: the contribution must be **correct under
concurrency** and **measurably scalable**. A speedup with no correctness argument, or a correctness
proof with no scaling data, each fails half the venue. Reviewers are parallel-systems experts who
will interrogate the baseline, the machine, and the variance before they believe a number.

## Match evidence to the claim

| Claim shape | Evidence PPoPP expects | Common failure it catches |
|---|---|---|
| A lock-free/wait-free structure | Throughput vs. thread count under varied contention; a linearizability/progress argument; memory-reclamation overhead | Single contention level; "no race seen" instead of an argument |
| A parallel runtime/scheduler | Overhead vs. sequential; strong+weak scaling on real workloads; load-balance behavior | Microbenchmarks only; no real application |
| A GPU/accelerator technique | Speedup over a strong GPU baseline; occupancy/divergence analysis; transfer costs counted | Ignoring host-device transfer; a weak baseline kernel |
| A parallel algorithm | Scaling on real inputs; NUMA/locality effects; comparison to the best known implementation | One input; a naive baseline |
| A memory-model / race tool | Soundness/coverage claims; runtime overhead; false-positive/negative characterization | Overhead unmeasured; no ground truth |

## The scalability story

- **Show the curve.** Report performance as a function of thread/core count, not one configuration.
  The interesting information is the *shape*: linear region, saturation point, collapse.
- **Distinguish strong vs. weak scaling** and label which you show. Strong scaling (fixed problem,
  more cores) and weak scaling (problem grows with cores) answer different questions; conflating
  them is a classic PPoPP tell.
- **Sweep the topology.** Cross-socket and NUMA effects, thread pinning, and (for GPUs) occupancy
  and divergence often dominate; a single-socket-only result invites "what about NUMA?"
- **Count the hidden costs.** Memory reclamation, host-device transfer, allocation, and scheduling
  overhead belong *inside* the reported numbers, not in a footnote.

## Correctness under concurrency

- Provide an **argument**, not just testing: linearizability (with linearization points),
  lock-freedom/wait-freedom (progress), or a checked property. "Passed a stress test" bounds
  confidence but does not establish correctness.
- Name the **memory model** you assume (C/C++11 atomics, the GPU model, hardware TSO) and show your
  synchronization is correct under it, not just under sequential consistency.
- If you use a model checker or race detector to support the claim, report its configuration and
  what it covers.

## Baselines that survive scrutiny

- Compare to the **strongest real competitor**, at the competitor's best settings, on the same
  machine — not to your own unoptimized code and not to a strawman.
- Rebuild and re-tune baselines yourself where feasible; citing a competitor's paper number
  measured on different hardware is not a fair comparison.
- If you are the first at something, construct the most credible reasonable baseline and justify it.

## Measurement hygiene

```text
[Repeats]     multiple runs; report median/mean with variance (error bars / percentiles)
[Warm-up]     discard JIT/cache/allocator warm-up; state the steady-state protocol
[Pinning]     pin threads to cores; state the topology and the pinning policy
[Isolation]   quiescent machine; no co-tenants; disable turbo/frequency scaling or report it
[Inputs]      real workloads plus targeted microbenchmarks; state sizes and sources
[Provenance]  exact CPU/GPU, socket/NUMA layout, memory, compiler and flags, OS
```

A single-run bar chart with no error bars, on an unstated machine, is the evaluation a PPoPP
reviewer trusts least.

## Anticipate the rebuttal questions at design time

The two questions PPoPP reviewers ask most — **"does it still scale at higher core counts / on
another GPU?"** and **"how does it compare to baseline X?"** — cannot be answered in the short
rebuttal window if the runs were never made. Pre-run the larger core sweep and the obvious
alternative baseline *before* submission so the numbers are already in hand (see
`ppopp-author-response`).

## Output format

```text
[Twin bar] correctness argument present? scalability curve present? both required
[Scaling] strong/weak labeled, core sweep, NUMA/GPU topology, hidden costs counted? yes/no
[Correctness] hazard + argument (linearizability/progress) under a named memory model? yes/no
[Baselines] strongest real competitor, same machine, tuned? yes/no
[Hygiene] repeats+variance, warm-up, pinning, isolation, provenance? list gaps
[Rebuttal pre-runs] higher core count + alternative baseline already measured? yes/no
```
