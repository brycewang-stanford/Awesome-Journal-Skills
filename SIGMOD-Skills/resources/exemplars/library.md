# SIGMOD Exemplars Library (award-anchored)

> **Verified via web search, access date 2026-07-08.** Every entry below is anchored to an
> **official award or ACM DL record**: the SIGMOD Test-of-Time award citations on
> `sigmod.org`, the ACM DL proceedings entry, or the conference's own awards page. Direct
> fetches of `dl.acm.org` and `dblp.org` were blocked from the verification network (see the
> access-method note in [`../official-source-map.md`](../official-source-map.md)), so each
> entry was cross-confirmed through at least two independent renderings. Entries that could
> not be cleanly confirmed were **excluded and documented** at the bottom — including two
> cases where search renderings actively mislabeled the award year. Short and verified beats
> long and guessed.
>
> **Sibling-venue guard:** the database flagships publish look-alike work. A paper being
> famous in data management does **not** make it a SIGMOD paper — PVLDB/VLDB, ICDE, PODS,
> TODS, and even OSDI own several of the field's classics. Check the actual proceedings
> record before attributing anything to SIGMOD.
>
> **Zero-hallucination rule:** this library provides positioning patterns only. It states no
> result numbers, no theorem contents, and no claims beyond venue, year, authorship, and the
> award citation. Read the originals in the ACM DL before citing.

---

## How to use this library

These papers are chosen for *lineage*, not recency: four carry SIGMOD's Test-of-Time
stamp or equivalent classic status, which is the venue's own statement about what durable
data-management contributions look like. Match your project to the nearest row, then study
how that paper (a) names its data-management primitive on page one and (b) pairs each claim
with system evidence — the twin disciplines taught in
[`../../skills/sigmod-writing-style/SKILL.md`](../../skills/sigmod-writing-style/SKILL.md) and
[`../../skills/sigmod-experiments/SKILL.md`](../../skills/sigmod-experiments/SKILL.md).

## Verified exemplars

### The query-optimizer foundation (systems + principled cost model)

- **Selinger, Astrahan, Chamberlin, Lorie & Price, "Access Path Selection in a Relational
  Database Management System," SIGMOD 1979.**
  Verified: ACM DL record `dl.acm.org/doi/10.1145/582095.582099` (Proceedings of the 1979
  ACM SIGMOD international conference on Management of data).
  - **Positioning lesson:** the primitive is unmistakable — how System R chooses access
    paths for single-relation and join queries. Nearly half a century later it remains the
    reference point for cost-based optimization, and the model for stating a mechanism so
    concretely that every later system can implement, measure, and dispute it.
  - **Self-check:** can a stranger implement your mechanism from your Section 4 alone?

### Interactive approximation (rethinking a core interface, ToT 2007)

- **Hellerstein, Haas & Wang, "Online Aggregation," SIGMOD 1997.**
  Verified: 2007 SIGMOD Test-of-Time citation,
  `sigmod.org/sigmod-awards/citations/2007-sigmod-test-of-time-award/`, naming its lasting
  influence on approximate query processing and stream aggregation research.
  - **Positioning lesson:** the contribution reframes *what a query returns* (progressive
    estimates with running confidence) rather than accelerating the existing contract — a
    template for papers whose novelty is an interface, backed by statistics and a working
    system together.
  - **Self-check:** if your paper changes a contract rather than a constant factor, does
    page one say so in the user's terms?

### Privacy meets data publishing (ToT 2024)

- **Zhang, Cormode, Procopiuc, Srivastava & Xiao, "PrivBayes: Private Data Release via
  Bayesian Networks," SIGMOD 2014.**
  Verified: 2024 SIGMOD awards page `sigmod.org/2024-sigmod-awards/`, citing widespread
  impact on synthetic data generation inside and beyond the data-management community.
  - **Positioning lesson:** imports a guarantee regime (differential privacy) into a
    database task (data release) and makes the combination *practical* — the SIGMOD-shaped
    move being the engineering that turns a theory constraint into a usable pipeline.
  - **Self-check:** does your paper's guarantee survive contact with realistic data sizes,
    and is that survival demonstrated rather than asserted?

### Data mining with systems discipline (ToT 2025)

- **Paparrizos & Gravano, "k-Shape: Efficient and Accurate Clustering of Time Series,"
  SIGMOD 2015.**
  Verified: `sigmod.org/sigmod-2025-test-of-time-award/`, citing the synthesis of accuracy,
  computational efficiency, and broad-domain applicability.
  - **Positioning lesson:** an analytics method survives at SIGMOD when efficiency is a
    first-class contribution, not an afterthought — the award citation itself names the
    accuracy-efficiency pairing. Method papers targeting this venue should read as
    algorithms-with-systems-costs, not as accuracy leaderboards.
  - **Self-check:** is your method's computational profile measured and compared as
    carefully as its quality metric?

### The industrial-track voice (deployed-system evidence)

- **Yang, Zhang, Chen, Li et al., "PolarDB-MP: A Multi-Primary Cloud-Native Database via
  Disaggregated Shared Memory," SIGMOD 2024 — Industry Track best paper.**
  Verified: Alibaba Cloud's announcement cross-checked against the SIGMOD 2024 awards
  listings (`2024.sigmod.org/sigmod_awards.shtml`).
  - **Positioning lesson:** the industrial track rewards architecture-in-production: the
    claim is a deployed design and the evidence is what it took to ship it. Use this lane
    when the deployment *is* the contribution (see
    [`../../skills/sigmod-topic-selection/SKILL.md`](../../skills/sigmod-topic-selection/SKILL.md)).
  - **Self-check:** does your paper have at least one non-academic author and evidence that
    only production access could produce?

## Lineage table

| Era | Exemplar | Venue record | Award anchor |
| --- | --- | --- | --- |
| 1979 | Access Path Selection (Selinger et al.) | SIGMOD 1979, ACM DL 10.1145/582095.582099 | Canonical classic |
| 1997 | Online Aggregation (Hellerstein, Haas & Wang) | SIGMOD 1997 | Test of Time 2007 |
| 2014 | PrivBayes (Zhang et al.) | SIGMOD 2014 | Test of Time 2024 |
| 2015 | k-Shape (Paparrizos & Gravano) | SIGMOD 2015 | Test of Time 2025 |
| 2024 | PolarDB-MP (Yang et al.) | SIGMOD 2024 industry track | Industry best paper 2024 |

## Excluded after checking (do not attribute to SIGMOD without re-verification)

- **"DFI: The Data Flow Interface for High-Speed Networks" (Thostrup et al.)** — multiple
  search renderings surfaced this as a "SIGMOD 2024/2025 best paper," but it is widely
  recorded as the **SIGMOD 2021** research best paper. The year conflict in live renderings
  is exactly the failure mode this library guards against: **待核实** against the ACM DL
  before citing any year for it.
- **"Efficiently Compiling Efficient Query Plans for Modern Hardware" (Neumann)** — a
  field-defining compilation paper, but it is **PVLDB (2011)**, not SIGMOD. Excluded.
- **"Fast Algorithms for Mining Association Rules" (Agrawal & Srikant)** — **VLDB 1994**,
  not SIGMOD (the 1993 Agrawal et al. association-rules paper is the SIGMOD one). A
  one-year, one-venue trap; excluded rather than risked.
- **"C-Store: A Column-oriented DBMS" (Stonebraker et al.)** — **VLDB 2005**. Excluded.
- **"MapReduce" (Dean & Ghemawat)** — **OSDI 2004**; heavily cited by database papers but
  not a database-venue paper at all. Excluded.
- **SIGMOD 2025 research best papers** — renderings conflated 2021 and 2025 winners during
  verification; no 2025 research-track title is asserted here. **待核实** via
  `sigmod.org/2025-sigmod-awards/` opened directly.

Before adding a row: locate the paper's ACM DL proceedings record (or its award citation on
`sigmod.org`), confirm the venue string names the SIGMOD conference or a PACMMOD SIGMOD
issue, record authors and year from that page, and update this file's access-date header.
When two renderings disagree, exclude and mark 待核实 — never average.
