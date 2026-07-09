> **Illustrative teaching example.** The paper, system, testbed, and every number below are
> **fictional** and exist only to demonstrate ATC house style. No real-paper facts, systems, or
> results are stated, and no policy is invented. Corresponding skills:
> [`atc-writing-style`](../../skills/atc-writing-style/SKILL.md),
> [`atc-topic-selection`](../../skills/atc-topic-selection/SKILL.md), and
> [`atc-experiments`](../../skills/atc-experiments/SKILL.md).

# Worked Example: An ATC-Style Extended Abstract + Introduction (before → after)

ATC 2026 reviews in **two rounds**: a two-page **extended abstract** is read first by two reviewers
who cut below-bar papers, and only survivors get a full read by 3-4 reviewers. The extended abstract
is **review-only, not published, and must stand alone** — a reviewer may see it *instead of* the
paper. So the ATC first-page arc must live in the abstract itself:
**systems problem practitioners recognize → why the current design is inadequate → the system/technique →
measured evidence on a real testbed → what changes in practice** — with ATC's expectations that the
contribution is a *built and measured* systems contribution, evidence is **end-to-end plus
microbenchmarks with tails and variance**, and the honest costs of the design are visible from the
start (not buried in a limitations paragraph).

The framing also reflects `atc-topic-selection`: ATC is strongest for a **solid, useful, measured**
systems result across its broad scope — even one a flagship might call incremental — rather than a
paper whose only claim is conceptual novelty with no implementation (which routes to a workshop like
HotOS) or whose depth is a networked-systems design better suited to NSDI.

**Illustrative paper (fictional):** *"Tiered-TTL: A Deployment-Driven Admission Policy for Flash
Read Caches."* Fictional system: an admission-control policy for an SSD-backed read cache in a
storage server, evaluated on a real multi-tenant testbed under production-derived traces.

---

## Before (buries the systems contribution — typical first-draft extended abstract + intro)

> **Extended Abstract.** Caching is important for storage systems. We present Tiered-TTL, a novel
> caching system that uses a new machine-learning-inspired admission policy. Our system is
> implemented and achieves high hit rates and outperforms existing baselines on a large dataset,
> demonstrating the promise of intelligent caching for modern storage.
>
> **Introduction.** Storage systems are critical. Flash caches are widely used to accelerate reads.
> In this paper we propose a new admission policy and build a caching system around it, and we
> evaluate it on traces, showing strong results. Section 2 covers background, Section 3 our design,
> Section 4 evaluation, Section 5 related work, and Section 6 concludes.

**What's wrong (against `atc-writing-style` / `atc-topic-selection` / `atc-experiments`):**

- **No self-standing problem in the extended abstract.** A round-one reviewer reading only these two
  paragraphs cannot tell what deployment pain this solves or why existing admission policies fall
  short — so the paper risks an early cut before anyone reads the full PDF.
- **Wrong evidence shape.** "High hit rate" on "a large dataset" is not a systems result: no
  end-to-end latency, no tail behavior, no comparison at matched cost, no statement of the testbed.
  ATC reviewers read for measured behavior on a real system.
- **Costs hidden.** Every admission policy trades something (write amplification, warm-up time, CPU
  on the fast path). Concealing the cost signals the evaluation will not be trusted.
- **Novelty-as-contribution.** "Novel, ML-inspired" is asserted, not motivated; ATC rewards a design
  justified by the deployment constraint, not by adjectives.
- **No artifact posture** — a double-blind ATC reviewer expects a runnable, anonymized artifact and
  a path to the headline numbers.

---

## After (ATC arc — problem → inadequacy → system → real-testbed evidence → what changes)

> **Extended Abstract.** Flash read caches in multi-tenant storage servers must decide *what to
> admit*, and the common size- or frequency-based admission policies waste flash write budget on
> one-hit objects while evicting the reused ones — inflating tail read latency exactly when a tenant
> is busiest. We present **Tiered-TTL**, an admission policy that assigns each object a short
> probationary residency and promotes only objects reused within it, spending flash writes on the
> objects that repay them. Tiered-TTL is implemented in a production-style storage server and
> evaluated on a **12-node multi-tenant testbed** driven by **production-derived traces**; we report
> end-to-end read latency (median and p99), hit rate at **matched flash-write budget**, warm-up
> time, and fast-path CPU cost, with variance across five runs. We are explicit about the trade:
> Tiered-TTL adds a small metadata structure on the fast path and a warm-up penalty after cold
> start, and we quantify both. *(problem → inadequacy → system → real-testbed evidence → honest cost
> — all in a self-standing two pages.)*
>
> **Introduction.** *(¶1 — the deployment problem, first breath.)* In a multi-tenant storage server,
> the flash cache is a shared, write-limited resource, and its admission policy silently decides
> which tenant's tail latency suffers. Operators see it as a busy tenant's p99 reads spiking while
> the cache churns on objects that are never read again.
>
> *(¶2 — why the current design is inadequate.)* Size- and frequency-threshold admission policies
> admit on a signal available *before* an object has proven itself, so under bursty multi-tenant
> traffic they spend scarce flash writes on one-hit objects and evict reused ones. The result is not
> a lower average hit rate — it is a **worse tail under load**, the metric operators actually watch,
> and no admission policy we know evaluates itself at a *matched write budget*, which is where the
> real trade lives.
>
> *(¶3 — contribution, stated as a systems design.)* We contribute **Tiered-TTL**, a probationary
> admission policy: a newly seen object is held in a short time-to-live probation and only promoted
> to durable cache residency if it is reused within that window, concentrating flash writes on
> objects that earn them. We implement it in a production-style server behind the existing cache
> interface, so it is a drop-in policy change rather than a new subsystem.
>
> *(¶4 — evidence on a real testbed, each claim paired.)* We evaluate on a 12-node testbed under
> production-derived multi-tenant traces: end-to-end median and p99 read latency (Fig. 3), hit rate
> at matched flash-write budget against three admission baselines (Table 2), warm-up time from cold
> (Fig. 4), and fast-path CPU and metadata overhead (Table 3), each with variance across five runs.
> Microbenchmarks isolate the promotion logic from the trace effects.
>
> *(¶5 — honest cost and what changes for practice.)* We state the cost plainly: Tiered-TTL adds a
> per-object probation record on the fast path and pays a warm-up penalty after a cold start, both
> quantified in §4; where a tenant's working set is smaller than the cache, it neither helps nor
> hurts. The payoff for operators is concrete: at the same flash-write budget, busy tenants see a
> lower read tail. §2 details the design; §3 the implementation; §4 the evaluation, with costs
> reported beside gains, not deferred. Code, trace-processing scripts, and configs are in the
> anonymized artifact. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ATC bar

Mapped to the skill checklists:

- **The extended abstract stands alone** — a round-one reviewer gets the problem, the design, the
  testbed, and the honest cost without the full paper (`atc-writing-style`: "the extended abstract
  is a self-contained argument, because a reviewer may read only it").
- **Evidence proportional to a systems claim** — the claim is about tail latency at matched cost, so
  the evidence is p99 on a real testbed at matched flash-write budget with variance, not average hit
  rate on "a dataset" (`atc-experiments`: match evidence to the claim, report tails and variance).
- **Costs reported beside gains** — the probation record and warm-up penalty are named up front and
  quantified, which is how ATC reviewers learn to trust an evaluation (`atc-writing-style`).
- **Right venue** — it is a built, measured system across ATC's broad scope, useful to operators;
  it is not a HotOS position piece and not an NSDI-shaped networked-systems design
  (`atc-topic-selection`).
- **Artifact by default** — code, trace scripts, and configs are in an anonymized artifact, matching
  ATC's double-blind review and its Available/Functional/Reproduced badge culture
  (`atc-reproducibility`, `atc-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified USENIX ATC
> papers** whose openings execute this arc, and [`../official-source-map.md`](../official-source-map.md)
> for ATC-specific submission policy, the two-round review, and the SIGOPS transition.
