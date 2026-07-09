---
name: ppopp-reproducibility
description: Use when making a PPoPP paper's parallel-performance results reproducible, covering the hardware and topology description reviewers re-run, thread pinning and NUMA control, seeds and warm-up, compiler/driver/flag provenance, and building an environment that reproduces the paper's scaling trend on different machines.
---

# PPoPP Reproducibility

Build the reproducibility story that a parallel-performance paper needs. Unlike a deterministic
algorithm, a PPoPP result depends on the **machine, the topology, and the run conditions** — and an
evaluator or a future reader will not have your exact node. Reproducibility here means someone else
can rebuild the environment and recover the **scaling trend and the relative comparison**, even when
their absolute numbers differ. Pin everything you can at run time; you cannot reconstruct it after
the machine is released.

## The environment description reviewers actually re-run

State enough that a stranger could stand up the same experiment:

```text
[CPU]        exact model, sockets, cores/threads, base/turbo policy, NUMA node layout
[Memory]     size, channels, speed; per-socket bandwidth if it bounds you
[GPU]        model, count, driver + CUDA/ROCm version, connection (PCIe/NVLink)
[Interconnect] for multi-node: fabric and topology
[Software]   OS + kernel, compiler + version + exact flags, libraries + versions, allocator
[Runtime]    thread count(s), pinning/affinity policy, scheduler settings, env vars
```

An evaluation whose machine is described only as "a Linux server" is the one reviewers trust least
and cannot reproduce.

## Control the sources of parallel non-determinism

- **Thread pinning / affinity.** Pin threads to cores and state the policy; unpinned runs migrate
  and produce unrepeatable numbers. Document NUMA placement (e.g., `numactl`, first-touch policy).
- **Warm-up.** Discard JIT, cache, and allocator warm-up; report the steady-state measurement
  protocol and how many iterations you drop.
- **Seeds.** Fix and record seeds for any randomized workload, input generator, or scheduler.
- **Frequency scaling.** Disable turbo/DVFS or report that it is on; otherwise speedups drift with
  temperature and neighbors.
- **Isolation.** Run on a quiescent machine with no co-tenants; note it.
- **Repeats.** Multiple runs with reported variance — reproducibility includes the spread, not just
  the mean.

## Reproduce the trend, not just the number

Because evaluators have different hardware, design the package so the **conclusion** survives a
change of machine:

- Provide a **scaled-down configuration** whose curve *shape* (linear region, saturation point)
  matches the paper, runnable on modest hardware.
- State the **minimum configuration** on which the claim still holds, and the **tolerance** within
  which you consider a result reproduced (e.g., "monotone speedup to the machine's core count," or
  "within 10% at matched core counts").
- Separate machine-dependent absolute throughput from machine-independent claims (relative speedup,
  scaling shape, correctness).

## Data and workloads

- Ship or point to the **exact inputs** (graphs, matrices, traces) with sizes and provenance, not
  just a generator script — or ship the generator *with* its seed.
- For real-application workloads, document versions and how they were built; a benchmark suite name
  without a version pin is not reproducible.

## Correctness reproducibility

- If a model checker or race detector supports your correctness claim, ship its configuration and
  the harness so the check itself can be re-run, not just described.

## Pre-submission reproducibility pass

```text
[Fresh checkout]  build from a clean clone in the pinned container -> succeeds?
[Blind re-run]    a colleague re-runs a scaling figure on a *different* machine -> trend matches?
[Provenance]      every number in the paper traces to a script + a recorded machine config?
[Anonymity]       the review-time package hides machine names, accounts, and personal repos?
```

## Output format

```text
[Environment] CPU/GPU/memory/interconnect/software/runtime fully stated? gaps: <...>
[Non-determinism] pinning, warm-up, seeds, frequency, isolation, repeats controlled? list gaps
[Trend portability] scaled config + minimum config + tolerance stated? yes/no
[Data] exact inputs or seeded generator shipped/pinned? yes/no
[Pass result] fresh-checkout build + cross-machine trend match? yes/no
```
