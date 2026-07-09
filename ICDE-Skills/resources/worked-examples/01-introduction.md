> **Illustrative teaching example.** The paper, system, workload, and every number below are
> **fictional** and exist only to demonstrate ICDE house style. No real-paper facts, datasets,
> or results are stated, and no policy is invented. Corresponding skills:
> [`icde-writing-style`](../../skills/icde-writing-style/SKILL.md),
> [`icde-topic-selection`](../../skills/icde-topic-selection/SKILL.md), and
> [`icde-experiments`](../../skills/icde-experiments/SKILL.md).

# Worked Example: An ICDE-Style Abstract + Introduction (before → after)

This demonstrates the **ICDE first-page contract** from `icde-writing-style`:
**data-engineering problem → why current systems fall short → the mechanism → measured
evidence → who can build on it** — with the ICDE rules that the contribution is a
**reconstructable engineering artifact**, that **performance claims are scoped to the
workloads actually run**, and that a **running example** carries the intuition. Because ICDE
is **single-blind**, author names stay on the paper; there is no anonymity theater to perform
in the prose.

The framing also reflects `icde-topic-selection`: ICDE is strongest when the contribution is a
**data-management primitive** — an access method, an operator, an execution or storage
mechanism — with a systems-grade evaluation, not a machine-learning result that merely uses a
database.

**Illustrative paper (fictional):** *"Wavevault: A Write-Optimized Index for Append-Heavy Time
Series on NVMe."* Fictional mechanism: a two-tier index that batches appends into
hardware-aligned segments and defers ordering to read time.

---

## Before (buries the engineering — typical first-draft abstract + intro)

> **Abstract.** Time-series data is growing rapidly and is very important for many
> applications. In this paper we propose a new index for time series that is faster than
> existing indexes. Our approach uses a novel data structure and achieves excellent
> performance on several datasets, outperforming state-of-the-art baselines in most
> experiments.
>
> **Introduction.** Time-series databases have become popular. Many indexes have been
> proposed, including B-trees, LSM-trees, and specialized structures. In this paper, we
> introduce a new index that improves insertion and query performance. We implement it and
> evaluate it on real and synthetic data, showing that it works well. Section 2 covers related
> work, Section 3 presents our design, Section 4 has experiments, and Section 5 concludes.

**What's wrong (against `icde-writing-style` / `icde-topic-selection` / `icde-experiments`):**

- **No data-engineering primitive on the first page** — it leads with "data is growing," not
  with the mechanism or the bottleneck it removes. ICDE reviewers want the engineering
  contribution up front.
- **The bottleneck is never named** — "faster" against what workload, what hardware, what cost
  metric? A systems claim with no operating point is unfalsifiable.
- **Overclaims** ("outperforming in most experiments," "works well") with **no measured
  quantities, no variance, no cost disclosed** — the exact reject pattern `icde-experiments`
  targets.
- **No mechanism** — "a novel data structure" hides the one idea a builder would need to
  reconstruct the system.
- **Over-signposted roadmap** substitutes for an argument.

---

## After (ICDE contract — problem → gap → mechanism → measured evidence → who builds on it)

> **Abstract.** Append-heavy time-series workloads on NVMe stall existing indexes because
> both B-trees and LSM-trees pay ordering cost **at write time**, when appends arrive faster
> than a single sorted structure can absorb them. We present **Wavevault**, a two-tier index
> that batches appends into **hardware-aligned segments** and **defers ordering to read
> time**, so ingestion cost becomes sequential-write-bound rather than compare-bound. On an
> append-dominant workload at 1.2M inserts/s, Wavevault sustains ingestion where an LSM
> baseline falls back to write stalls, at a read-latency cost we bound and measure: median
> range-scan latency rises by a factor we report with its full distribution, not just the
> median. We characterize the exact crossover — the append-to-scan ratio above which
> Wavevault wins — so an engineer can decide *a priori* whether to adopt it. *(problem → gap
> → mechanism → measured evidence → decision rule, all on the first page.)*
>
> **Introduction.** *(¶1 — the bottleneck, first breath.)* Consider a fleet-telemetry store
> ingesting 1.2 million sensor appends per second while serving recent-window range scans.
> *(running example, introduced once, reused throughout.)* The appends are almost ordered by
> arrival but not perfectly, so every insert into a sorted index pays a comparison-and-shift
> cost that, at this rate, saturates the CPU long before the NVMe device's sequential-write
> bandwidth is reached. The device is idle; the index is the bottleneck.
>
> *(¶2 — gap: why current systems fall short, each named specifically.)* B-trees keep the
> structure fully ordered on every insert, so they pay the ordering cost precisely when it is
> most expensive. LSM-trees defer some of it via memtables, but compaction re-introduces it as
> background write amplification that competes with foreground ingestion for the same device
> bandwidth. Specialized time-series indexes assume near-perfect arrival order and degrade when
> it is merely approximate. *(each prior approach gets a specific failure, not "prior work is
> limited.")*
>
> *(¶3 — the mechanism, stated so a builder could rebuild it.)* Wavevault splits the index into
> a **write tier** of append-only, hardware-aligned segments and a **read tier** of lazily
> merged summaries. Appends land sequentially in the current segment with no comparison;
> ordering happens only when a read touches a segment, and the result is cached. The single
> idea is: **move ordering off the write path and pay it, amortized, on the read path that
> actually needs it.**
>
> *(¶4 — evidence, each claim tied to a measurement.)* We evaluate on a fleet-telemetry trace
> and a synthetic generator whose append-to-scan ratio we sweep. Wavevault sustains 1.2M
> inserts/s with no write stalls where the LSM baseline stalls above 0.9M (Figure 4, five runs,
> variance reported); read-tier lazy merge raises median range-scan latency by a measured
> factor whose tail we plot in full (Figure 6); and we report the device-bandwidth and
> memory cost of the write tier so the trade is legible (Table 3). We identify the crossover
> append-to-scan ratio above which Wavevault is the right choice (Section 5). *(every claim →
> figure, table, or measured crossover.)*
>
> *(¶5 — who builds on it + roadmap.)* Wavevault is a drop-in write tier for any system that
> can tolerate read-time ordering, so a builder can adopt it behind an existing scan
> interface. Section 3 details the segment layout, Section 4 the lazy-merge algorithm, Section 5
> the evaluation and crossover analysis. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ICDE bar

Mapped to the skill checklists:

- **Engineering primitive on the first page** — the abstract and ¶1 name the bottleneck (write
  stalls under append rate) and the mechanism (defer ordering to read time) before any
  structural detail (`icde-writing-style`: put the data-engineering contribution first).
- **Bottleneck and operating point named** — 1.2M inserts/s, NVMe, append-to-scan ratio; a
  systems claim that can be checked, not "faster in general" (`icde-experiments`).
- **Mechanism reconstructable** — write tier / read tier / lazy merge is enough for a competent
  engineer to rebuild, which is the ICDE novelty test, not a vague "novel structure."
- **Every claim measured, cost disclosed** — ingestion, read-latency tail, and the memory and
  bandwidth cost all reported with variance; no "outperforms in most experiments"
  (`icde-experiments`: throughput and tail latency with declared variance, and a loss map).
- **Running example** — the fleet-telemetry store is introduced once and reused, carrying the
  intuition through the paper (`icde-writing-style`).
- **Right venue and track** — a storage/execution-layer primitive with a systems evaluation is
  a strong ICDE research-track fit, not a machine-learning re-route (`icde-topic-selection`).
- **12-page discipline** — the crossover analysis and segment-layout details fit the body;
  full trace documentation and additional sweeps go to supplemental material
  (`icde-writing-style`: use the page budget for the mechanism and the decision rule).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, award-anchored
> ICDE papers** whose first pages execute this contract, and
> [`../official-source-map.md`](../official-source-map.md) for ICDE-specific submission policy.
