> **Illustrative teaching example.** The paper, system, dataset, and every number below are
> **fictional** and exist only to demonstrate EDBT house style. No real-paper facts, systems, or
> results are stated, and no policy is invented. Corresponding skills:
> [`edbt-writing-style`](../../skills/edbt-writing-style/SKILL.md),
> [`edbt-topic-selection`](../../skills/edbt-topic-selection/SKILL.md), and
> [`edbt-experiments`](../../skills/edbt-experiments/SKILL.md).

# Worked Example: An EDBT-Style Abstract + Introduction (before → after)

This demonstrates the **EDBT first-page arc** from `edbt-writing-style`:
**data-management problem → why current systems fall short → contribution (technique/system) →
evidence on real workloads at realistic scale → what it enables and where it is honest about its
limits** — with the EDBT expectations that the contribution *extends database technology*, that the
evaluation would convince a skeptical systems reviewer, and that the work is reproducible enough for
an open-access record.

The framing also reflects `edbt-topic-selection`: EDBT is strongest when the lesson is about how
data is **stored, queried, integrated, or processed** in a real system — here, adaptive
partitioning for skewed join workloads — rather than a complexity result (which would route to the
co-located **ICDT**) or a pure-ML modeling result whose data-systems consequence is incidental
(which would route elsewhere), and when the paper's natural home is the European database-systems
community and its nearest cycle.

**Illustrative paper (fictional):** *"SkewCut: Adaptive Partitioning for Skewed Distributed Joins."*
Fictional artifact: a partitioning operator that detects key skew at runtime and re-splits hot
partitions, evaluated on real analytical query workloads on a cluster.

---

## Before (buries the systems contribution — typical first-draft abstract + intro)

> **Abstract.** Distributed joins are important in big data systems. We propose a new partitioning
> method that uses a novel algorithm and achieves better performance than existing approaches on a
> large dataset, demonstrating the power of our technique for modern data processing.
>
> **Introduction.** Data is growing rapidly and distributed query processing is everywhere. Many
> systems perform joins across machines. In this paper we present a new partitioning approach and
> evaluate it on a dataset, showing it is faster than baselines. Section 2 covers related work,
> Section 3 our approach, Section 4 experiments, and Section 5 concludes.

**What's wrong (against `edbt-writing-style` / `edbt-topic-selection` / `edbt-experiments`):**

- **No concrete data-management problem on the first page** — it leads with "data is growing," not
  with the specific failure (skew) that current partitioners hit. EDBT wants the systems problem up
  front.
- **Vague claim shape.** "Better performance on a large dataset" names neither the workload, the
  baseline, the scale, nor the metric — a database reviewer cannot tell what was actually shown.
- **No sense of scale or realism** — one unnamed dataset invites the "does this hold on real
  workloads and cluster sizes?" rejection.
- **No baseline identity.** "Existing approaches" is not a comparison; the reviewer needs the
  strongest current partitioner named and tuned.
- **No reproducibility posture** — no artifact, workload provenance, or hardware, which an EDBT
  reviewer and the open-access record both expect.
- **Over-signposted roadmap** substituting for an argument.

---

## After (EDBT arc — problem → inadequacy → contribution → real-workload evidence → what it enables)

> **Abstract.** Distributed hash joins degrade sharply under **key skew**: a handful of hot keys
> overload a few workers while the rest idle, and static partitioning cannot react once a query is
> running. We present **SkewCut**, a partitioning operator that **detects skew at runtime and
> re-splits hot partitions** without reshuffling cold data. On **12 analytical workloads over
> real query logs**, at cluster sizes from 8 to 128 workers, SkewCut reduces straggler time
> relative to a **tuned range- and hash-partitioning baseline** (measurements with variance across
> repeated runs; workloads, cluster configuration, and scripts are in the artifact). We report where
> it helps most (high-skew joins), where it is neutral (uniform keys), and its overhead on
> skew-free workloads. *(problem → inadequacy → system → real-workload, multi-scale evidence →
> honest scope — all on the first page.)*
>
> **Introduction.** *(¶1 — the data-management problem, first breath.)* In a distributed join, one
> overloaded worker sets the query's wall-clock time. When a join key is skewed — a few values
> dominating — static partitioning sends those values to the same worker, and the query waits on a
> straggler while most of the cluster sits idle. The engineering question is not "can we partition
> data?" but **"can a running query notice skew and repair its own partitioning before the straggler
> dominates?"**
>
> *(¶2 — why the current state is inadequate.)* Systems today choose a partitioning at plan time and
> commit to it. Hash partitioning spreads uniform keys well but collapses under skew; range
> partitioning needs a distribution known in advance; and re-partitioning mid-query usually means
> reshuffling everything, whose cost erases the benefit. No widely used operator **selectively**
> re-splits only the hot partitions while a query runs.
>
> *(¶3 — contribution, stated as systems claims.)* We contribute **SkewCut**, an operator that (i)
> estimates per-key load from a lightweight running sketch, (ii) identifies hot partitions above a
> cost threshold, and (iii) re-splits only those, leaving cold partitions in place. We integrate it
> into a distributed query engine and describe the mechanism precisely enough to reimplement.
>
> *(¶4 — evidence on real workloads, each claim paired.)* We tie every claim to evidence: straggler
> reduction is measured on 12 workloads derived from real query logs (Table 1); scaling behavior is
> reported from 8 to 128 workers (Fig. 2); the re-split cost model is validated against measured
> overhead (Fig. 3); and a skew-free workload set quantifies the worst-case overhead we impose when
> there is nothing to fix (Table 2). Workloads, engine configuration, and analysis scripts are in
> the artifact.
>
> *(¶5 — scope and what it enables.)* We are explicit about limits: SkewCut helps when skew is
> concentrated and detectable within the query's lifetime; for briefly running queries the detection
> window is too short, which we quantify rather than hide. The payoff is concrete: analytical engines
> can keep static planning's simplicity and still survive the skewed joins that dominate real logs.
> Section 2 positions SkewCut against prior partitioning work; Section 3 details the operator;
> Section 4 the evaluation; scope and overhead are discussed alongside the results, not deferred.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the EDBT bar

Mapped to the skill checklists:

- **Data-systems contribution on the first page** — the abstract and ¶1 pose a concrete
  storage/query-processing problem (skew stragglers) before any algorithm detail
  (`edbt-writing-style`: "lead with the data-management contribution").
- **Evidence proportional to the claim** — the claim is about straggler time under skew, so the
  evidence is straggler measurements across real workloads and multiple cluster sizes against a
  tuned baseline, not a single unnamed dataset (`edbt-experiments`: match the evidence to the claim
  shape, at realistic scale).
- **Scope engaged, not hidden** — the overhead on skew-free workloads and the short-query
  limitation are quantified in the body, which is how an EDBT reviewer's first two objections are
  pre-empted (`edbt-writing-style`: discuss limits alongside results).
- **Right venue** — the lesson is a query-processing mechanism and its measured behavior, an
  *extending database technology* contribution, not a complexity theorem (which routes to the
  co-located ICDT) (`edbt-topic-selection`).
- **Reproducible by default** — workloads, cluster configuration, and scripts are in an artifact,
  matching EDBT's reproducibility culture and the open-access OpenProceedings record
  (`edbt-reproducibility`, `edbt-artifact-evaluation`).
- **Fair, named baseline** — a *tuned* range- and hash-partitioning comparison, at scale, pre-empts
  the "unfair baseline" and "toy scale" rejections (`edbt-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified EDBT
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for EDBT-specific submission policy, the
> OpenProceedings open-access model, and the multiple-cycle process.
