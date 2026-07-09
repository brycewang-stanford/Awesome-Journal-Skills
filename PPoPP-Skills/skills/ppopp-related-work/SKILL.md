---
name: ppopp-related-work
description: Use when writing or auditing a PPoPP paper's related-work and positioning, covering the parallel-programming literature lanes (concurrent data structures, runtimes/schedulers, GPU/accelerators, memory models, parallel algorithms), delta-first comparison against the nearest competitor, double-blind self-citation, and separating PPoPP work from CGO/PLDI/POPL/SC neighbors.
---

# PPoPP Related Work

Position the paper against the parallel-programming literature, not the whole of systems. A PPoPP
reviewer is an expert in your subarea and will know the two or three works you must beat. The job is
**delta-first**: state precisely what your structure/runtime/algorithm does that the nearest prior
parallel-programming work does not, in measurable terms.

## Cover the right lanes

Map your contribution onto the PPoPP literature lanes and cover the ones you touch:

- **Concurrent data structures** — lock-free/wait-free lists, maps, queues, skip lists; progress
  guarantees; memory reclamation (hazard pointers, epoch-based, RCU).
- **Runtimes and schedulers** — work-stealing, task graphs, futures, fork/join, load balancing,
  parallel-loop scheduling.
- **GPU and accelerator programming** — kernel design, occupancy/divergence, heterogeneous
  scheduling, memory movement, warp-level primitives.
- **Memory models and concurrency correctness** — weak-memory reasoning, race detection,
  linearizability checking, verified concurrency.
- **Parallel algorithms in practice** — graph, sparse, numerical kernels; locality/NUMA
  engineering.
- **Parallel languages/compilers-for-parallelism** — DSLs, parallel IRs, runtime-coupled
  compilation (cite, but position *against* CGO/PLDI so the boundary is clear).

Missing the lane your reviewer works in is the fastest way to look like a visitor.

## Delta-first, in measurable terms

- Lead each comparison with the **delta**: "Unlike <competitor>, which requires a global lock on
  resize, our structure resizes lock-free, giving <X>× throughput at 64 threads." Contrast on the
  axis PPoPP cares about — progress guarantee, contention behavior, scalability, memory overhead.
- Do not merely list neighbors; say what each one *cannot* do that you do, and where you inherit
  from them honestly.
- If your only delta over the state of the art is a single-machine constant-factor speedup with no
  qualitative difference, say so plainly — reviewers will find the gap faster than you can hide it.

## The nearest-competitor test

For every contribution, name the **single closest** prior parallel-programming work and answer:

```text
[Same problem?]   are they solving the same parallel-programming problem, or an adjacent one?
[Progress/model]  do you offer a stronger guarantee (wait-free vs lock-free, stronger memory model)?
[Scaling]         where does their approach saturate that yours does not, and by how much?
[Cost]            what do you pay (space, single-thread overhead) that they do not — stated honestly?
```

If you cannot articulate the delta on at least one of these axes, the paper is not yet positioned.

## Double-blind self-citation

PPoPP review is **double-blind**. Cite your own prior work in the **third person** ("Prior work [12]
introduced...") — never "our earlier system [12]." Watch the parallel-systems-specific leaks:

- A distinctive **system/library/runtime name** carried from your prior paper that identifies the
  group.
- A results repository or benchmark suite hosted under a personal/lab account, cited in-line.
- Acknowledgement of a specific named machine or grant that pins the institution.

Anonymize the artifact link and describe carried-over systems neutrally until camera-ready.

## Separating PPoPP from its neighbors in the prose

Because PPoPP shares its week with CGO/CC and its subject with PLDI/POPL/SC, reviewers watch for
scope drift in the related work:

- Cite compiler-optimization work but frame your delta as a **parallel-execution** result, not a
  pass — otherwise you invite a "this is a CGO paper" comment.
- Cite concurrency-theory work but anchor your contribution to a **measured system** — a pure-logic
  framing reads as POPL.
- Cite HPC-at-scale work but keep the lesson a **general parallel-programming** one, not a
  single-deployment report — otherwise SC is the home.

## Common failures

- **A wall of citations with no deltas** — reads as a literature dump, not positioning.
- **Missing the reviewer's own lane** — the one omission that most reliably angers a PC member.
- **First-person self-citation** — a double-blind violation that is easy to miss under deadline.
- **Comparing only to old baselines** — the state of the art in concurrent structures and GPU
  kernels moves fast; a 5-year-old baseline is not the frontier.

## Output format

```text
[Lanes covered] which parallel-programming lanes your positioning addresses
[Nearest competitor] named, with the delta on progress/model | scaling | cost
[Delta statements] each measurable and axis-specific? yes/no
[Anonymity] self-citations third-person? system name / repo / machine anonymized? yes/no
[Scope guard] framed as parallel-programming (not CGO/POPL/SC)? yes/no
```
