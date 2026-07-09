---
name: ppopp-topic-selection
description: Use when deciding whether a parallel/concurrent-computing project belongs at PPoPP or should be routed to PLDI, CGO, POPL, ASPLOS, HPCA, SC, SPAA, or OOPSLA, and when distinguishing PPoPP's "the parallelism is the point" scope from a compiler contribution (CGO/PLDI), a concurrency logic (POPL), or a microarchitecture result (ASPLOS/HPCA).
---

# PPoPP Topic Selection

Decide the venue before drafting. PPoPP — the ACM SIGPLAN Symposium on Principles and Practice of
Parallel Programming — is the premier forum for work whose **center of gravity is parallelism and
concurrency**: parallel languages, compilers, and runtimes; lock-free/wait-free data structures;
GPU/accelerator and NUMA performance; parallel algorithms; and scalability studies. A technically
strong paper whose real contribution is a compiler pass, a program logic, or a cache design is
respected here and then rejected as out of scope. The question PPoPP reviewers ask first is: **is
the parallelism the point, or is it the setting?**

## The routing question that matters most

PPoPP sits inside the co-located **HPCA/CGO/PPoPP/CC** week, so its nearest neighbors are one
hallway away and the boundary is real. Use the "is the parallelism the point?" test: if you removed
the concurrency/parallel-performance story, is there still a paper? If yes, the contribution lives
elsewhere.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| The contribution *is* a parallel algorithm, runtime, synchronization mechanism, or a concurrency-correctness + scalability result | **PPoPP** | This is PPoPP's center; both correctness and speedup are judged |
| The contribution is a **compiler optimization or code-generation** technique | **CGO** (or **PLDI**) | Backend/optimization is CGO's named center; PLDI for broader PL implementation |
| The contribution is a **new program logic, type system, or semantics** for concurrency | **POPL** | Foundational concurrency *theory* over a measured parallel system |
| The contribution is **hardware/microarchitecture** (coherence, memory system, accelerator design) | **ASPLOS / HPCA** | The result is about the machine, not the parallel program |
| The core is a **large-scale HPC application or systems-at-scale** deployment | **SC / ICS / IPDPS** | Application/HPC-systems framing over a general parallel-programming lesson |
| The core is a **theoretical parallel-algorithm** bound with no implementation | **SPAA** | Theory of parallelism; PPoPP wants practice alongside principle |
| A concurrency feature of a managed language / object system | **OOPSLA / PLDI** | Language-design framing dominates |

## Contribution shapes PPoPP rewards

- **Concurrent data structures** — a new lock-free/wait-free structure or synchronization primitive
  with a correctness argument (linearizability, progress) *and* throughput/scalability under
  contention.
- **Parallel runtimes and schedulers** — work-stealing, task graphs, futures, load balancing, with
  measured overhead and scaling on real workloads.
- **GPU / accelerator programming** — techniques, languages, or libraries that raise occupancy,
  reduce divergence, or exploit heterogeneity, with speedups over strong GPU baselines.
- **Parallel algorithms in practice** — graph, numerical, or sparse kernels whose parallel design
  and NUMA/locality engineering deliver a measured win.
- **Memory-model and concurrency-correctness work** — race/linearizability checking, weak-memory
  reasoning, or verified concurrency, positioned as a parallel-programming enabler.
- **Compilers/languages *for parallelism*** — DSLs, parallel IRs, and runtime-coupled compilation
  where the parallel-execution lesson (not a generic pass) is the contribution.

## The remove-the-parallelism and swap-the-machine tests

Two quick tests sharpen a borderline verdict:

- **Remove-the-parallelism test:** delete the concurrency and the scaling story. If a contribution
  remains (a better pass, a cleaner semantics, a faster core), route to CGO/PLDI/POPL/ASPLOS.
- **Swap-the-machine test:** if your result is a single-configuration speedup that would vanish or
  reverse on another core count, socket topology, or GPU generation, it is a microbenchmark, not a
  parallel-programming contribution — PPoPP wants a lesson that survives the sweep.

## Evidence maturity, without the cliché

Fit is necessary but not sufficient. A synchronization idea shown only at one thread count is a
workshop poster; a runtime evaluated only on microbenchmarks needs real workloads before the
research track; a scalability claim with no baseline is not yet a paper. PPoPP's twin bar —
**correct under concurrency and measurably scalable** — is what promotes an idea from "interesting"
to "PPoPP-shaped."

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two PPoPP programs (dblp, conf.researchr.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = mismatch or a CGO/ASPLOS home
[Citations] is your bibliography majority PPoPP/PLDI/ASPLOS/SC/SPAA parallel venues?
          -> majority elsewhere => reviewers read you as a visitor; reframe the intro
[Calendar] PPoPP's summer deadline vs CGO/PLDI/ASPLOS/SC dates (same co-located family)
          -> route to the nearest honest fit; a marginal preference rarely justifies a year
```

## Decision procedure

```text
[Point test] remove the parallelism -> is there still a contribution? yes => reroute
[Claim type] concurrent structure / runtime / GPU / parallel algorithm / memory-model / parallel-language
[PPoPP vs CGO/PLDI] is a compiler pass the real result? -> CGO/PLDI
[PPoPP vs POPL] is it concurrency theory with no measured system? -> POPL
[PPoPP vs ASPLOS/HPCA] is it about the machine? -> ASPLOS/HPCA
[Verdict] PPoPP research track / sibling venue, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is PPoPP, continue with `ppopp-workflow` for the calendar and `ppopp-writing-style` for the
paper shape.
