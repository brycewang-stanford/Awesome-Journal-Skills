> **Illustrative teaching example.** The system, workloads, and every number below are
> **fictional**, invented only to demonstrate the OSDI narrative arc. No real-paper
> facts or results are stated and no venue policy is invented. Corresponding skills:
> [`osdi-writing-style`](../../skills/osdi-writing-style/SKILL.md),
> [`osdi-topic-selection`](../../skills/osdi-topic-selection/SKILL.md), and
> [`osdi-experiments`](../../skills/osdi-experiments/SKILL.md).

# Worked Example: An OSDI-Style Abstract + Introduction (before → after)

This demonstrates the **OSDI design-narrative arc** from `osdi-writing-style`:
**operational pain → why existing designs cannot fix it → the abstraction or mechanism →
what was built → what the measurements show → what the design trades away.** Two OSDI
pressures shape the rewrite: everything reviewers weigh must fit the **12-page reviewed
body** (no appendices at submission in the 2026 cycle), and with **no author-response
period**, the introduction must answer the skeptical reviewer pre-emptively — there is
no second conversation.

**Illustrative paper (fictional):** *"Ledger: Crash-Consistent Metadata for
Disaggregated Block Storage."* Fictional design: a per-tenant metadata log that makes
crash recovery independent of cluster size.

---

## Before (engineering tour — typical first draft)

> **Abstract.** Cloud storage is increasingly disaggregated. We present Ledger, a new
> metadata service for disaggregated block storage. Ledger uses a novel log-structured
> design with many optimizations, including batching, sharding, and caching. We
> implemented Ledger in 28K lines of Rust. Experiments show Ledger is up to 7.3x faster
> than existing systems on several benchmarks and scales well.
>
> **Introduction.** Disaggregated storage separates compute from storage and is widely
> used. Metadata management is important in such systems. Prior systems have various
> limitations. In this paper we design Ledger, which has a log-structured architecture
> with several components described in Section 3. We evaluate Ledger extensively in
> Section 5 and show significant improvements. Our contributions are: a new
> architecture; several optimizations; an extensive evaluation.

**What fails (against `osdi-writing-style` / `osdi-topic-selection` / `osdi-experiments`):**

- **No operational pain.** "Metadata is important" motivates nothing; nothing breaks,
  stalls, or costs money in this telling — a systems reviewer has no stakes.
- **No named abstraction.** "Log-structured with many optimizations" is an
  implementation inventory. What is the *idea* that another builder could reuse?
- **The 7.3x is unanchored** — no baseline named, no workload named, no statement of
  what was traded to get it. Uncontextualized speedups read as benchmark shopping.
- **"Scales well" is not a claim.** Scales in what dimension, to what point, degrading
  how?
- **Contribution list restates the table of contents**, spending first-page budget the
  12-page cap cannot spare.
- **Nothing pre-empts the obvious objection** (why not shard an existing metadata
  service?), fatal in a cycle with no rebuttal to catch it later.

---

## After (OSDI arc — pain → gap → mechanism → build → measure → trade-off)

> **Abstract.** In disaggregated block stores, metadata recovery after a controller
> crash stalls every tenant: recovery replays a cluster-wide metadata log, so recovery
> time grows with cluster size even though each tenant's state is small. We present
> **Ledger**, a metadata service that makes recovery **per-tenant**: each tenant's
> mappings live in an independently ordered log, and a lease protocol lets surviving
> controllers adopt a crashed peer's tenants without global replay. The cost is
> deliberate: Ledger gives up cross-tenant atomic operations, which we argue (and
> measure) are rare in block workloads. We built Ledger in 28K lines of Rust and
> evaluated it on a 64-node testbed against two production-derived baselines under
> reconstructed cloud block traces. Ledger bounds recovery to under 900 ms regardless
> of cluster size — versus recovery that grows linearly for the baselines — while
> matching their steady-state throughput within 4%, and costing 11% extra metadata
> write amplification. *(pain → mechanism → admitted trade → build → anchored numbers.)*
>
> **Introduction.** *(¶1 — the pain, made operational.)* When a metadata controller in
> a disaggregated block store crashes, tenants do not lose data — they lose **time**:
> volumes stay unattached until the controller's metadata log is replayed. Because
> that log is ordered cluster-wide, replay time tracks cluster growth, so the tail of
> recovery gets worse precisely as the deployment succeeds. *(a failure mode with a
> trend, not "metadata is important.")*
>
> *(¶2 — why existing designs cannot fix it.)* The obvious remedies each fail for a
> nameable reason. Sharding the log by volume reduces replay per shard but recovery
> still waits on the slowest shard, and cross-volume operations reintroduce global
> ordering. Aggressive checkpointing shrinks the log but stalls foreground writes at
> checkpoint boundaries — the same tail moved elsewhere. Replicating the controller
> masks single crashes but doubles correlated-failure blast radius without bounding
> replay. *(each alternative gets a specific failure — this paragraph is the rebuttal
> the no-response process will never let us deliver.)*
>
> *(¶3 — the abstraction, named, and its price.)* Ledger's design premise is that
> **recovery scope should equal failure scope**: a crash should cost each affected
> tenant only that tenant's log. Ledger therefore orders metadata per tenant, and a
> lease-adoption protocol transfers a crashed controller's tenants to survivors
> without global coordination. The premise has a price — Ledger cannot offer atomic
> operations spanning tenants — and we quantify how rarely block workloads want them
> rather than asserting it. *(one reusable idea; the trade-off stated where the
> mechanism is, not in a limitations footnote.)*
>
> *(¶4 — build and measurement, anchored.)* We implemented Ledger (28K lines of Rust)
> and evaluated it on 64 nodes against a replay-based and a checkpoint-based baseline,
> both re-implemented from published production designs, under reconstructed cloud
> block traces. Recovery stays under 900 ms from 8 to 64 nodes while both baselines
> grow linearly; steady-state throughput is within 4% of the best baseline; the cost
> is 11% metadata write amplification, which we break down by component. *(baselines
> named, workload named, the win and its cost in the same sentence.)*
>
> *(¶5 — contributions as claims.)* This paper contributes: the recovery-scope
> principle and a per-tenant log design that realizes it; a lease-adoption protocol
> with a proof sketch of safety under partition; and a 64-node evaluation showing
> size-independent recovery at bounded overhead. *(three claims a reviewer can test,
> not three section titles.)*

---

## Why the "after" meets the OSDI bar

- **Pain first** — a failure mode that worsens with scale gives the design stakes
  (`osdi-writing-style`: open with what breaks, not with the research area).
- **Gap paragraph does rebuttal work in advance** — every plausible alternative is
  dispatched with a mechanism-level reason, which is where author leverage lives when
  the cycle offers no response period (`osdi-author-response`).
- **One named idea** — "recovery scope = failure scope" is quotable and reusable; the
  batching/sharding/caching inventory is demoted to design sections.
- **Trade-off admitted and measured** — giving up cross-tenant atomicity is stated
  next to the mechanism and then quantified, the honesty move OSDI reviewers reward
  and its exemplars model (`osdi-experiments`: measure the cost, not only the win).
- **Numbers are anchored** — baseline identity, workload provenance, scale range, and
  overhead all travel with the headline number; nothing "scales well."
- **12-page discipline** — the introduction spends its length on argument, and the
  proof sketch and trace-reconstruction detail are flagged for the design/evaluation
  sections, since the submitted PDF has no appendix to absorb them
  (`osdi-supplementary`).

> Next: [`../exemplars/library.md`](../exemplars/library.md) shows real, verified OSDI
> papers whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) carries the policy facts
> (page budget, no-appendix rule, no-response cycle) this example leans on.
