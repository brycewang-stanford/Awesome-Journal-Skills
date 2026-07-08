> **Illustrative teaching example.** The system, workloads, numbers, and citations sketched
> below are **entirely fictional**, invented to demonstrate SIGMOD house style; no real
> paper's results are reproduced and no venue policy is invented. Companion skills:
> [`sigmod-writing-style`](../../skills/sigmod-writing-style/SKILL.md),
> [`sigmod-experiments`](../../skills/sigmod-experiments/SKILL.md), and
> [`sigmod-topic-selection`](../../skills/sigmod-topic-selection/SKILL.md).

# Worked Example: A SIGMOD-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening for a fictional storage-engine paper and rework it
until it honors the SIGMOD **page-one contract** — workload pressure, incumbent failure
with a number, the mechanism in one concrete sentence, a scoped headline result, and
verifiable contributions — plus the venue's signature **running example** device.

**Fictional paper:** *"TidalStore: Access-Aware Compaction Scheduling for LSM-Based Storage
Engines."* Invented premise: an LSM-tree engine whose compaction scheduler observes query
access patterns instead of relying on size ratios alone.

---

## Before (how systems drafts actually start)

> **Abstract.** The amount of data generated worldwide is growing at an unprecedented rate,
> making efficient storage systems more important than ever. Log-structured merge trees are
> widely used in modern key-value stores. However, compaction remains a significant
> challenge. In this paper we present TidalStore, a novel compaction scheduling approach.
> Extensive experiments demonstrate that TidalStore significantly outperforms
> state-of-the-art systems while guaranteeing correctness.
>
> **Introduction.** Big data applications are everywhere, from social networks to IoT.
> LSM-trees have become the dominant storage structure for write-intensive workloads, and
> many systems adopt them. Compaction merges sorted runs and reclaims space, but it consumes
> resources. Many works have studied compaction. In this paper, we propose TidalStore, which
> uses a novel scheduling algorithm. Our contributions are: (1) we propose TidalStore; (2)
> we implement TidalStore; (3) we conduct extensive experiments.

**Why this fails the SIGMOD read** (per `sigmod-writing-style` and `sigmod-experiments`):

- Opens with data-growth boilerplate instead of the specific bottleneck — the reviewer's
  first-page skim finds no workload, no number, no mechanism.
- "Significantly outperforms state-of-the-art" is an unscoped superlative: no workload,
  no baseline named, no boundary — the exact claim shape a builder-heavy PC distrusts.
- "Guaranteeing correctness" gestures at an invariant it never states.
- The contribution list enumerates activities ("we implement," "we conduct"), not
  verifiable artifacts.
- No running example anywhere; the design sections that follow will have to teach in
  symbols what three keys and two sorted runs could show.
- "Many works have studied compaction" is a related-work placeholder that a PC of people
  who wrote those works will read as unfamiliarity.

---

## After (the page-one contract, honored)

> **Abstract.** In LSM-based key-value stores, compaction schedulers pick merge targets
> from *size ratios alone*, blind to which key ranges queries actually read. Under skewed
> read workloads this misallocates I/O: in our measurements of a fictional-but-typical
> cloud trace mix, up to 41% of compaction bandwidth is spent on ranges that serve under
> 2% of reads, inflating read tail latency behind avoidable merge work. We present
> **TidalStore**, a compaction scheduler that treats observed access frequency as a
> first-class scheduling input alongside size ratio, prioritizing merges on read-hot
> ranges and deferring cold ones under an explicit space-amplification budget. TidalStore
> preserves the engine's snapshot-consistency invariant (Sec. 4.2) and bounds worst-case
> space amplification to a configurable factor (Theorem 1). On skewed YCSB-style mixes at
> 100M keys, TidalStore reduces p99 read latency by 2.3× versus a tuned size-ratio
> scheduler with 6% additional space; on uniform workloads the two are within 4%
> (medians over 5 runs; full setup in Sec. 6.1). The scheduler, workloads, and per-figure
> scripts are available in our artifact.
>
> **Introduction (¶1 — the bottleneck, concretely).** Consider a key-value store holding
> user-session state: 100M keys, writes uniform, reads concentrated on the ~5% of keys
> belonging to active sessions. *(This three-line scenario is the running example; every
> design section revisits it.)* A size-ratio compaction scheduler sees only bytes: it
> merges the coldest archive ranges with the same urgency as session-hot ones, so hot-range
> reads keep paying multi-run lookup costs while I/O drains into merges no query benefits
> from.
>
> **(¶2 — why incumbents fail, each for a named reason.)** Size-ratio and level-budget
> schedulers [fictional 12, 17] optimize write amplification under an implicit
> uniform-read assumption; they cannot express "this range is hot." Read-triggered
> compaction [fictional 23] reacts per-lookup and thrashes under shifting skew. Static
> temperature tiering [fictional 31] classifies at ingest time and never reclassifies, so
> session churn defeats it. *(Nearest neighbors are named, each with a mechanism-level
> failure — and each reappears as a tuned baseline in Sec. 6.)*
>
> **(¶3 — mechanism and invariant.)** TidalStore maintains a decayed per-range read
> counter in the existing manifest, scores candidate merges by (read heat × lookup depth)
> per byte of merge I/O, and schedules under a hard space-amplification cap. Deferral
> never violates snapshot consistency: we state the invariant in Sec. 4.2 and sketch its
> proof, with the full argument in the extended report.
>
> **(¶4 — contributions as artifacts.)** (1) An access-aware compaction scoring rule and
> scheduler (Sec. 4); (2) a proof that deferral preserves the consistency invariant and a
> bound on space amplification (Sec. 4.2, Theorem 1); (3) an implementation inside a
> fictional open LSM engine (Sec. 5); (4) an evaluation across skew levels, scale factors,
> and four tuned baselines, including the regimes where TidalStore loses (Sec. 6).

---

## What changed, mapped to the skills

| Draft defect | Fix applied | Skill rule |
| --- | --- | --- |
| Data-growth opener | Bottleneck stated inside a concrete workload | Page-one contract (`sigmod-writing-style`) |
| Unscoped "significantly outperforms" | 2.3× p99 on skewed mixes; within 4% on uniform; runs and setup cited | Claim scoping table |
| "Guaranteeing correctness" | Named invariant + where it is proved | Architecture before algebra |
| Activity-list contributions | Artifact-list contributions with section pointers | Page-one contract |
| No example | Session-store running example introduced in ¶1 | The running example |
| "Many works have studied..." | Three neighbor families, each with a mechanism-level failure and a benchmarked return in Sec. 6 | Contrast form (`sigmod-related-work`) |
| No loss disclosure | Uniform-workload parity and 6% space cost stated up front | Negative-result honesty (`sigmod-experiments`) |

Two further venue notes. First, the "after" text quantifies its own motivation (the 41%
misallocation figure) — SIGMOD introductions earn their problem statements with
measurements, not adjectives. Second, everything here remains anonymity-safe: no lab name,
no production system identified, artifact referenced without an identifying URL — the
discipline `sigmod-submission` enforces for the whole multi-round review.

> Next: study real award-anchored openings via [`../exemplars/library.md`](../exemplars/library.md),
> then verify current-cycle rules in [`../official-source-map.md`](../official-source-map.md)
> before formatting a submission.
