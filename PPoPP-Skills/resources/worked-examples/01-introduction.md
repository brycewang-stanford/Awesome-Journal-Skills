> **Illustrative teaching example.** The paper, system, machine, and every number below are
> **fictional** and exist only to demonstrate PPoPP house style. No real-paper facts, systems, or
> results are stated, and no policy is invented. Corresponding skills:
> [`ppopp-writing-style`](../../skills/ppopp-writing-style/SKILL.md),
> [`ppopp-topic-selection`](../../skills/ppopp-topic-selection/SKILL.md), and
> [`ppopp-experiments`](../../skills/ppopp-experiments/SKILL.md).

# Worked Example: A PPoPP-Style Abstract + Introduction (before → after)

This demonstrates the **PPoPP first-page arc** from `ppopp-writing-style`:
**parallel-programming problem → why the current state stalls → contribution (the mechanism) →
the twin claim (correct under concurrency *and* how much it scales) → evidence on a real machine** —
with the PPoPP expectations that **parallelism is the point** (not a compiler pass or a proof in
disguise) and that **correctness and scalability are shown together**, not one at the expense of the
other.

The framing also reflects `ppopp-topic-selection`: PPoPP is strongest when the lesson is about a
**parallel program's behavior** — here, a concurrent index that stays correct *and* scales under
contention — rather than a compiler optimization (which would route to CGO/PLDI), a pure concurrency
logic (POPL), or a microarchitecture result (ASPLOS/HPCA).

**Illustrative paper (fictional):** *"FanoutMap: A Lock-Free Ordered Index that Scales Through the
NUMA Wall."* Fictional artifact: a concurrent ordered map with a redesigned reclamation scheme,
evaluated on a fictional multi-socket server.

---

## Before (buries the parallelism; one number, no correctness) — typical first draft

> **Abstract.** Ordered indexes are everywhere. We present FanoutMap, a new concurrent ordered map
> with a clever node layout. Our implementation is fast: on our server it achieves 42 million
> operations per second, outperforming existing maps. This shows the promise of careful engineering
> for concurrent data structures.
>
> **Introduction.** Concurrent data structures are important for modern multicore machines. Many
> maps exist, but they can be slow. In this paper we describe FanoutMap, which uses a new layout and
> is implemented in C++. We evaluate it on a server and show it is fast. Section 2 covers related
> work, Section 3 the design, Section 4 experiments, and Section 5 concludes.

**What's wrong (against `ppopp-writing-style` / `ppopp-topic-selection` / `ppopp-experiments`):**

- **No parallel-programming problem on the first page** — it leads with "indexes are everywhere"
  and a single throughput number, not with what *breaks under concurrency* (contention, reclamation
  cost, cross-socket traffic). PPoPP wants the parallelism framed as the point.
- **One number, no curve.** "42 Mops on our server" hides where it scales and where it collapses;
  PPoPP reviewers read a single configuration as a microbenchmark, not a result.
- **No correctness claim.** It never says the structure is lock-free or linearizable, nor under
  which memory model — half the PPoPP bar is simply missing.
- **Unnamed baseline and unnamed machine.** "Outperforming existing maps" on "our server" invites a
  reject: which competitor, at what settings, on what topology?
- **Engineering-as-contribution.** "Careful engineering" with no general parallel-programming lesson
  reads as a report, not a principle — and if the win is one machine's constant factor, the
  `ppopp-topic-selection` swap-the-machine test fails.
- **Over-signposted roadmap** substituting for an argument.

---

## After (PPoPP arc — problem → stall → mechanism → twin claim → real-machine evidence)

> **Abstract.** Lock-free ordered indexes deliver high throughput on a single socket but **collapse
> across the NUMA boundary**: safe memory reclamation forces cross-socket coordination whose cost
> grows with the socket count, so adding a second or fourth socket often *reduces* throughput. We
> present **FanoutMap**, a lock-free ordered map whose reclamation scheme confines coordination to a
> single socket in the common case. We prove FanoutMap's operations are **linearizable** and its
> lookups **wait-free** under the C++11 memory model, and we show it **scales to all 4 sockets (96
> cores)** where a state-of-the-art lock-free map saturates at one socket — a fictional 3.1×
> throughput at 96 threads under high contention, with the crossover and the saturation point
> reported, not hidden. *(problem → stall → mechanism → correctness + scaling → real machine — all
> on the first page.)*
>
> **Introduction.** *(¶1 — the parallel-programming problem, first breath.)* On a multi-socket
> server, the scarcest resource for a concurrent index is not CPU cycles but **cross-socket
> coordination**. A lock-free map can retire memory safely only by agreeing, across threads, that no
> reader still holds a pointer — and when those threads span sockets, that agreement crosses the
> interconnect on every operation. The engineering question is therefore not "can we make a fast map
> on one socket?" but **"can an ordered lock-free index keep scaling as sockets are added, without
> giving up linearizability?"**
>
> *(¶2 — why the current state stalls.)* Existing lock-free ordered maps use epoch- or
> hazard-pointer reclamation whose bookkeeping is global. Our measurements (Fig. 1) show their
> throughput is flat or negative beyond one socket under contention: the reclamation traffic, not
> the map operations, becomes the bottleneck. Prior NUMA-aware structures relax ordering or
> correctness to avoid this; we do not.
>
> *(¶3 — the contribution, framed as parallelism.)* We contribute **FanoutMap** and its
> **socket-local reclamation** scheme: readers publish liveness to a per-socket structure, and
> reclamation coordinates across sockets only at a bounded, amortized rate. The mechanism — not a
> compiler pass, not a new logic — is the contribution, and it is what lets the index cross the NUMA
> wall.
>
> *(¶4 — the twin claim, correctness and scaling together.)* We establish both halves of the bar.
> **Correctness:** we give linearization points for every operation and prove lookups wait-free and
> updates lock-free under the C++11 memory model (Section 4); a model-checked harness for the
> reclamation protocol is in the artifact. **Scalability:** on a fictional 4-socket, 96-core server
> we report throughput as a function of thread count from 1 to 96 under three contention levels,
> against the strongest lock-free competitor rebuilt and tuned on the same machine, with median and
> variance over repeated, pinned runs (Section 5).
>
> *(¶5 — honest limits and what changes.)* We report where FanoutMap stops helping: below one socket
> its extra per-socket state costs a fictional 8% single-thread overhead, and at low contention the
> gap to prior work narrows. The payoff for parallel programming is a concrete design principle —
> confine reclamation coordination to the socket — that other ordered structures can adopt.
> Section 3 details the design; Section 4 the correctness argument; Section 5 the evaluation;
> reproduction (topology, pinning, seeds) is in the artifact. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the PPoPP bar

Mapped to the skill checklists:

- **Parallelism is the point, on the first page** — the abstract and ¶1 pose a *concurrency*
  problem (cross-socket reclamation traffic) before any implementation detail, and the
  swap-the-machine test passes because the lesson is a scaling principle, not one server's constant
  factor (`ppopp-writing-style`, `ppopp-topic-selection`).
- **The twin claim is explicit** — linearizable + wait-free lookups *under a named memory model*
  **and** a speedup that scales to 96 cores; neither half is left implicit
  (`ppopp-experiments`: correctness argument *and* scaling curve).
- **The curve, not a point** — throughput is reported across thread counts and contention levels
  with the saturation point and crossover shown, not a single "42 Mops" headline
  (`ppopp-writing-style`: show the curve).
- **Named baseline, named machine, variance** — the competitor is rebuilt and tuned on the *same*
  4-socket server, and runs are pinned and repeated with variance
  (`ppopp-experiments`: baselines that survive scrutiny; measurement hygiene).
- **Honest about limits** — the single-thread overhead and the low-contention narrowing are stated,
  which strengthens rather than weakens the paper (`ppopp-experiments`).
- **Reproducibility captured** — topology, pinning, and seeds are in the artifact, matching the
  post-acceptance, CGO-shared AE expectations (`ppopp-reproducibility`,
  `ppopp-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified PPoPP
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for PPoPP-specific submission policy and
> the co-located-week cycle model.
