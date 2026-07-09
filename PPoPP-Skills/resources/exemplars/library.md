# PPoPP Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and/or the **ACM Digital Library** to confirm it appeared at the **ACM SIGPLAN
> Symposium on Principles and Practice of Parallel Programming (PPoPP)** — matching title, authors,
> year, and venue string. Papers that could not be cleanly confirmed as PPoPP (as opposed to PLDI,
> CGO, POPL, SPAA, PODC, DISC, or a journal) were **omitted and documented below**. It is
> deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** PPoPP is **not** PLDI, **not** CGO, **not** POPL, **not** SPAA, and
> **not** PODC/DISC. Several canonical parallel-computing results were introduced at those venues
> instead; a famous author or a familiar system name does **not** prove a PPoPP placement. Each row
> was checked to be a PPoPP edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, speedups, or table numbers — read the original on ACM DL before
> citing anything. For PPoPP-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **parallel-programming problem practitioners recognize**, argues **correctness under
concurrency**, and backs a **scalability claim with a real baseline** — the PPoPP twin bar (see
[`../../skills/ppopp-writing-style/SKILL.md`](../../skills/ppopp-writing-style/SKILL.md),
[`../../skills/ppopp-topic-selection/SKILL.md`](../../skills/ppopp-topic-selection/SKILL.md), and
[`../../skills/ppopp-experiments/SKILL.md`](../../skills/ppopp-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "PPoPP-shaped."

---

## By contribution shape

### Parallel runtime + scheduler — work-stealing

- **Blumofe, Joerg, Kuszmaul, Leiserson, Randall & Zhou, "Cilk: An Efficient Multithreaded Runtime
  System," PPoPP 1995, pp. 207-216.** Verified: dblp/ACM (early version at the 5th PPoPP, Santa
  Barbara, July 1995; a journal version later appeared in JPDC). Introduced the **Cilk work-stealing
  runtime** for multithreaded parallelism.
  - **Why it is an exemplar:** it pairs a **runtime mechanism** (work stealing) with both an
    **analytic** argument about its efficiency and an **empirical** demonstration on real
    applications — the classic PPoPP "principle *and* practice" shape.
  - **Self-check:** does your runtime contribution come with both a reasoned efficiency argument and
    measured scaling on real workloads, not just microbenchmarks?

### Concurrent data structure — optimistic concurrency

- **Bronson, Casper, Chafi & Olukotun, "A Practical Concurrent Binary Search Tree," PPoPP 2010,
  pp. 257-268.** Verified: ACM DL / dblp. A concurrent relaxed-balance tree using optimistic
  concurrency control with fixed, ahead-of-time read/write sets and a linearizable clone.
  - **Why it is an exemplar:** a **concurrent data structure** delivered with a **correctness story**
    (linearizable operations) *and* throughput measured against a highly tuned competitor across
    contention levels — PPoPP's twin bar in one paper.
  - **Self-check:** do you argue linearizability/progress *and* show throughput vs. thread count
    against the strongest real competitor, not your own unoptimized code?

### Shared-memory framework — parallel graph processing

- **Shun & Blelloch, "Ligra: A Lightweight Graph Processing Framework for Shared Memory," PPoPP
  2013, pp. 135-146.** Verified: dblp `rec/conf/ppopp/ShunB13`. A minimal shared-memory graph
  framework (vertexMap/edgeMap over vertexSubsets).
  - **Why it is an exemplar:** it makes a **parallel-programming abstraction** the contribution —
    the interface is the idea — and shows it competes with far heavier distributed systems on real
    graphs. The lesson survives a change of graph and machine.
  - **Self-check:** is your abstraction general across workloads, and does the evaluation compare to
    the real state of the art rather than a strawman?

### Multi-GPU programming model — irregular computation

- **Ben-Nun, Sutton, Pai & Pingali, "Groute: An Asynchronous Multi-GPU Programming Model for
  Irregular Computations," PPoPP 2017.** Verified via PPoPP 2017 proceedings / dblp `conf/ppopp`.
  An asynchronous programming model for irregular workloads across multiple GPUs.
  - **Why it is an exemplar:** it targets a **heterogeneous, multi-accelerator** setting where the
    parallel-programming challenge (asynchrony, load imbalance across GPUs) *is* the contribution,
    with scaling shown across GPU counts.
  - **Self-check:** if your GPU result is a single-device speedup that would not survive a second
    GPU or generation, is the parallelism really the point (an `ppopp-topic-selection` re-route
    signal)?

### GPU kernel technique — work decomposition

- **Osama, Merrill, Cecka, Garland & Owens, "Stream-K: Work-Centric Parallel Decomposition for
  Dense Matrix-Matrix Multiplication on the GPU," PPoPP 2023.** Verified via the PPoPP 2023
  proceedings / SIGPLAN OpenTOC. A work-centric decomposition for GEMM that improves GPU
  utilization.
  - **Why it is an exemplar:** a focused **parallel-decomposition** idea for a core kernel,
    evaluated for occupancy/utilization against strong GPU baselines — a tight, measurable
    parallel-programming contribution.
  - **Self-check:** is your kernel technique compared to the best existing implementation with the
    hidden costs (transfer, load imbalance) counted inside the numbers?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified PPoPP exemplar | Edition | Method |
| --- | --- | --- | --- |
| Parallel runtime + scheduler | Blumofe et al., "Cilk" | PPoPP 1995 | Work stealing |
| Concurrent data structure | Bronson et al., "A Practical Concurrent BST" | PPoPP 2010 | Optimistic concurrency |
| Shared-memory framework | Shun & Blelloch, "Ligra" | PPoPP 2013 | Parallel graph abstraction |
| Multi-GPU programming model | Ben-Nun et al., "Groute" | PPoPP 2017 | Asynchronous multi-GPU |
| GPU kernel technique | Osama et al., "Stream-K" | PPoPP 2023 | Work-centric decomposition |

> Five verified papers across five parallel-programming contribution shapes. Note how each pairs a
> **mechanism/abstraction** with **measured scaling on real workloads** — the PPoPP signature — and
> how correctness (Cilk's efficiency argument, the BST's linearizability) travels alongside
> performance.

---

## Omitted for lack of clean PPoPP verification (do not attribute to PPoPP without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Michael & Scott, "Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue
  Algorithms"** — verified to be **PODC 1996**, *not* PPoPP, despite being a canonical concurrent
  data structure. A direct sibling-venue trap; listed only as a guardrail.
- **Frigo, Leiserson & Randall, "The Implementation of the Cilk-5 Multithreaded Language"** —
  **PLDI 1998**, not PPoPP; do not conflate it with the PPoPP 1995 Cilk paper above.
- **Cilk++ reducers / hyperobjects (Frigo et al.)** — the SPAA line, **not** PPoPP.
- **Blumofe & Leiserson, "Scheduling Multithreaded Computations by Work Stealing"** — the theory
  paper appeared at **FOCS 1994** (journal version JACM 1999), not PPoPP.
- **Transactional Locking II (TL2; Dice, Shalev & Shavit)** — **DISC 2006**, a distributed-computing
  venue, not PPoPP. Omitted.
- **Galois, "Optimistic Parallelism Requires Abstractions"** — **PLDI 2007**, not PPoPP. Omitted.

Before adding any paper, confirm it on **dblp** (`db/conf/ppopp/`) and **ACM DL** by matching the
venue string to a PPoPP edition (not PLDI, CGO, POPL, SPAA, PODC, or DISC), then record authors,
year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
