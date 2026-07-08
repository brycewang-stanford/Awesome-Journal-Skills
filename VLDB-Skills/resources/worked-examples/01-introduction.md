> **Illustrative teaching example.** The system, workload, numbers, and authors below are
> **invented** solely to demonstrate PVLDB house style; no real paper is quoted and no
> venue policy is invented. Companion skills:
> [`vldb-writing-style`](../../skills/vldb-writing-style/SKILL.md),
> [`vldb-experiments`](../../skills/vldb-experiments/SKILL.md), and
> [`vldb-topic-selection`](../../skills/vldb-topic-selection/SKILL.md).

# Worked Example: A PVLDB-Style Abstract + Introduction (before → after)

PVLDB reviewers are system builders reading on a monthly clock. The first page has to
answer four questions fast: **what workload breaks today's systems, what design decision
fixes it, what was actually built, and what the headline measurement shows** — with every
performance claim scoped to the hardware and data scale where it was measured.

**Fictional paper:** *"Meridian: Adaptive Log Compaction for Multi-Tenant LSM Stores."*
Fictional design: a compaction scheduler that reallocates I/O budget across tenants using
observed write-amplification, with an isolation guarantee per tenant.

---

## Before (a first draft that would struggle in review)

> **Abstract.** With the explosion of big data, LSM-tree storage engines have become
> increasingly popular. However, compaction remains a challenging problem. In this paper
> we propose Meridian, a novel adaptive compaction framework. Extensive experiments
> demonstrate that Meridian significantly outperforms state-of-the-art systems.
>
> **Introduction.** Modern applications generate enormous volumes of data. LSM-trees are
> widely used in systems such as key-value stores. Compaction can interfere with
> foreground traffic, which is undesirable. We design a new scheduler that is adaptive
> and efficient. Our contributions are: (1) we propose Meridian; (2) we implement it;
> (3) we evaluate it extensively.

**Why this fails the PVLDB read:**

- "Explosion of big data" is filler; no reviewer learns which workload is broken.
- "Significantly outperforms" is unscoped — no baseline named, no scale, no metric, no
  hardware. Systems reviewers treat unscoped superlatives as a credibility tax.
- The contribution list restates the paper's existence ("we propose, we implement, we
  evaluate") instead of naming design decisions.
- No tension is stated. Every storage paper "reduces interference"; the draft never says
  what must be traded away, so the design sounds free — and free designs read as
  unexamined designs.
- Nothing signals the artifact: in a venue with an availability badge and a
  reproducibility evaluation, silence about code is a missed trust signal.

---

## After (the PVLDB first-page contract)

> **Abstract.** In multi-tenant LSM stores, one tenant's compaction burst can double
> another tenant's p99 write latency, because compaction I/O is scheduled globally while
> latency objectives are per-tenant. Meridian schedules compaction per tenant against an
> explicit I/O budget derived from each tenant's observed write amplification, and
> guarantees that no tenant's budget is depleted by a neighbor's ingest spike. We
> implemented Meridian in [open-source LSM engine] by replacing its compaction picker
> and adding per-tenant accounting (~4K LOC). On a 16-node cluster with a skewed
> 200-tenant YCSB-derived workload, Meridian holds p99 write latency within 1.4x of an
> isolated-tenant baseline where the stock scheduler degrades to 5.8x, while total
> compaction throughput stays within 7% of stock. Code, workload generators, and plot
> scripts are available at [artifact URL].
>
> **Introduction, ¶1 (the broken workload).** Cloud key-value services pack hundreds of
> tenants onto shared LSM storage engines. The engine schedules compaction globally —
> whichever level is most overfull wins the I/O — but operators sell per-tenant latency
> SLOs. Under skewed ingest, these two facts collide: a single heavy writer inflates
> compaction debt that the scheduler pays with I/O charged, in effect, to everyone.
>
> **¶2 (why existing designs don't close the gap).** Rate-limiting compaction smooths
> the interference but delays it, growing read amplification for the victim tenants it
> is meant to protect. Physical isolation — one LSM tree per tenant — restores fairness
> at the cost of the memory and write batching that made multi-tenancy economical.
> Priority-based pickers reorder work but still draw from one undifferentiated budget.
> *(Each alternative gets a named mechanism and a named cost.)*
>
> **¶3 (the design decision and its price).** Meridian's bet: compaction budgets, not
> compaction order, are the right isolation boundary. It meters I/O per tenant,
> replenishes budgets from measured write amplification, and lets tenants trade unused
> budget through a bounded exchange. The price is bookkeeping on the compaction path
> and up to 7% lower aggregate compaction throughput under uniform load — we report
> this cost in §6.4 rather than hiding it. *(The trade-off is in the introduction, not
> discovered by reviewer 2.)*
>
> **¶4 (what exists and what was measured).** We built Meridian in [engine] (~4K LOC,
> compaction picker + accounting). Across 200-tenant skewed workloads on 16 nodes we
> measure tail write latency, read amplification, and aggregate throughput against the
> stock scheduler, a rate-limited variant, and per-tenant physical isolation. Headline:
> near-isolation tail latency at multi-tenant cost. All experiments, generators, and
> figures regenerate from the released artifact. *(Claims carry their scale, cluster,
> baselines, and regeneration story.)*

---

## What changed, mapped to the pack's rules

| Draft symptom | Fix applied | Rule source |
| --- | --- | --- |
| "Big data" throat-clearing | Opens on the workload/SLO collision | `vldb-writing-style`: page-one contract |
| Unscoped "significantly outperforms" | p99 figures tied to cluster, tenants, baseline | `vldb-writing-style`: scoped claims |
| "We propose/implement/evaluate" list | Contributions stated as design decisions with costs | `vldb-writing-style` |
| Free-lunch framing | The 7% throughput price stated up front | `vldb-experiments`: loss disclosure |
| No artifact signal | Artifact URL + regeneration promise in the abstract | `vldb-artifact-evaluation` |
| Baseline vagueness | Three named baselines including the strong one (physical isolation) | `vldb-experiments`: fair baselines |

> Next step: compare against the real award-anchored papers in
> [`../exemplars/library.md`](../exemplars/library.md), then verify current submission
> mechanics in [`../official-source-map.md`](../official-source-map.md) before the
> abstract deadline on the 25th.
