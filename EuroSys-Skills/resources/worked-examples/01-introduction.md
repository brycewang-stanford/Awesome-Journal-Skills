> **Illustrative teaching example.** The system, workloads, and every number below are
> **fictional**, invented solely to demonstrate EuroSys house style. No real-paper content is
> reproduced and no venue policy is invented. Corresponding skills:
> [`eurosys-writing-style`](../../skills/eurosys-writing-style/SKILL.md),
> [`eurosys-experiments`](../../skills/eurosys-experiments/SKILL.md), and
> [`eurosys-topic-selection`](../../skills/eurosys-topic-selection/SKILL.md).

# Worked Example: A EuroSys-Style Abstract + Introduction (before → after)

The target is the arc from `eurosys-writing-style`: **operational pain → structural gap in
existing mechanisms → the insight → the built system → scoped numbers**, with an insight a
reviewer can retell and claims that carry their measurement conditions.

**Fictional paper:** *"Quill: Deadline-Aware Log Compaction for Multi-Tenant Key-Value
Stores."* Fictional premise: background compaction in LSM-based stores collides with tenant
latency objectives; Quill schedules compaction work against per-tenant deadline budgets.

---

## Before (a typical systems first draft)

> **Abstract.** Key-value stores are widely used in modern data centers. Compaction is a
> well-known problem that can significantly impact performance. In this paper we present
> Quill, a novel compaction framework that leverages deadline-awareness to dramatically
> improve tail latency. Extensive experiments show that Quill outperforms state-of-the-art
> systems by up to 3.7x while maintaining high throughput.
>
> **Introduction.** With the rapid growth of cloud computing, key-value stores have become
> critical infrastructure. However, compaction interference remains challenging. Existing
> approaches fail to address this problem effectively. We propose Quill, which uses a
> deadline-aware scheduler. Our contributions are: (1) we identify compaction interference
> as an important problem; (2) we design Quill; (3) we evaluate Quill extensively.

**Why this fails the EuroSys read** (per `eurosys-writing-style` / `eurosys-experiments`):

- **No retellable insight.** "Leverages deadline-awareness" names a flavor, not a mechanism;
  a PC champion has nothing to say in the room.
- **Unscoped numbers.** "Up to 3.7x" carries no workload, metric, percentile, or baseline —
  the exact pattern that triggers the tuned-baseline question.
- **"Existing approaches fail" without names.** No systems are cited, so the structural gap
  is asserted, not argued; reviewers who built those systems will supply the names themselves,
  uncharitably.
- **Contribution list without verifiable content.** "We design Quill" is not a claim anyone
  can check; contributions should point at sections and evidence.
- **Buzzword risk markers** — "novel," "dramatically," "extensive" — the vocabulary of a
  draft that has not yet decided what it proved.

---

## After (the EuroSys arc)

> **Abstract.** In multi-tenant LSM key-value stores, background compaction and foreground
> requests contend for the same I/O bandwidth, and today's stores arbitrate that contention
> with global rate limits that know nothing about tenants' latency objectives. The result is
> a lose-lose: p99 GET latency for latency-sensitive tenants degrades by up to 4.1x during
> compaction storms in our testbed reproduction of a published multi-tenant trace, while
> throttling compaction globally lets write amplification grow unboundedly. Our insight is
> that compaction work is *deferrable but not skippable*, which makes it schedulable against
> explicit per-tenant deadline budgets — the same way EDF schedules deferrable computation.
> Quill implements this as a compaction planner that decomposes compactions into
> preemptible micro-tasks and admits them under an earliest-deadline-first budget derived
> from each tenant's latency SLO. On a 12-node cluster running YCSB-style mixed tenants and
> the reproduced trace, Quill holds latency-sensitive tenants' p99 GET within 1.2x of the
> compaction-free baseline (vs 4.1x for the global rate limiter tuned per its
> documentation), sustains 94% of peak ingest throughput, and bounds write amplification
> within 8% of the unthrottled store. Quill loses when every tenant is latency-sensitive:
> with no deferrable budget to reclaim, it converges to the rate limiter's behavior (§6.5).
>
> **Introduction (skeleton).**
> *¶1 — the pain, measured:* a reproduced multi-tenant trace shows compaction storms
> inflating p99 GETs 4.1x for tenants whose SLOs forbid it.
> *¶2 — the structural gap, named:* global rate limiting (System A, System B) throttles all
> tenants uniformly; priority I/O scheduling (System C) reorders requests but cannot defer
> the compactions that generate the load. Neither represents *when compaction debt must be
> repaid*, so both overpay or underpay.
> *¶3 — the insight:* compaction is deferrable-but-not-skippable work, therefore
> deadline-schedulable; state the invariant (debt repaid before read-amplification bound is
> breached).
> *¶4 — the system:* micro-task decomposition, per-tenant budgets from SLOs, EDF admission;
> one sentence each on the failure path and the cost (planner CPU, metadata).
> *¶5 — contributions, each with a pointer:* the characterization (§3), the planner and its
> invariant (§4–5), the evaluation including where Quill loses (§6), and the artifact.

**Why the "after" version passes the same read:**

- **The insight survives retelling** — "compaction is deferrable-but-not-skippable, so
  schedule it like EDF" is one sentence, system name not required.
- **Every number is scoped** — metric, percentile, workload, cluster size, and baseline
  tuning provenance travel with each claim; nothing is "up to" anything.
- **The gap is structural and named** — two mechanism families are shown *unable to
  represent* the needed information, which is an argument, not an insult.
- **The worst case is in the abstract** — §6.5's losing regime is volunteered, buying the
  credibility that `eurosys-experiments` calls the boundary layer.
- **Contributions are checkable** — each maps to a section and an artifact, matching the
  claims-to-evidence discipline the artifact evaluation will later audit.

---

Next steps: compare against real award-line papers in
[`../exemplars/library.md`](../exemplars/library.md), then verify current formatting and
round policy in [`../official-source-map.md`](../official-source-map.md) before drafting to
this template.
