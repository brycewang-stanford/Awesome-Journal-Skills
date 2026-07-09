# EDBT Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp**, **OpenProceedings.org**, and the **EDBT Test-of-Time Award** announcements to confirm it
> appeared at the **International Conference on Extending Database Technology (EDBT)** — matching
> title, author list, year, and venue string. Every row is an **EDBT Test-of-Time honoree**, so each
> is both venue-confirmed and a model of "influence a decade later" at EDBT. Papers that could not
> be cleanly confirmed as EDBT (as opposed to SIGMOD, VLDB, ICDE, or the co-located ICDT) were
> **omitted and documented below**. It is deliberately a short, verified list (5 verified > 15
> guessed).
>
> **Sibling-confusion guard:** EDBT is **not** SIGMOD, **not** VLDB, **not** ICDE, and **not** ICDT.
> Many canonical database results were introduced at those venues instead; a famous author or a
> familiar system name does **not** prove EDBT. Each row was checked to be an EDBT edition
> specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, throughput numbers, or table values — read the original on
> OpenProceedings or the ACM/dblp record before citing anything. For EDBT-specific policy, scope,
> the OpenProceedings open-access model, and the multiple-cycle process, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **data-management problem practitioners recognize**, backs it with **evidence proportional
to the claim** (workloads, scale, baselines), and frames its scope — the EDBT bar (see
[`../../skills/edbt-writing-style/SKILL.md`](../../skills/edbt-writing-style/SKILL.md),
[`../../skills/edbt-topic-selection/SKILL.md`](../../skills/edbt-topic-selection/SKILL.md), and
[`../../skills/edbt-experiments/SKILL.md`](../../skills/edbt-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "EDBT-shaped."

---

## By contribution shape

### System + architecture — storage engine for modern hardware

- **"Shore-MT: a scalable storage manager for the multicore era," EDBT 2009** (honoree includes
  Nikos Hardavellas; EDBT 2019 Test-of-Time Award). Verified: dblp EDBT 2009 / EDBT Test-of-Time
  announcements. Re-engineered a database storage manager to scale on multicore hardware.
  - **Why it is an exemplar:** it takes a concrete systems problem — a storage manager that does not
    scale as cores multiply — and delivers a **re-architected system** with measurements that make
    the case, arguing that designing for scalability can be worth a single-thread cost. The
    contribution is a mechanism and a lesson others build on.
  - **Self-check:** is your systems contribution a real artifact evaluated on realistic hardware and
    workloads, with a lesson that outlives the specific prototype?

### Distributed algorithm + evaluation — parallel query processing at scale

- **Zhang, Li & Jestes, "Efficient parallel kNN joins for large data in MapReduce," EDBT 2012**
  (EDBT 2022 Test-of-Time Award). Verified: dblp / OpenProceedings; EDBT Test-of-Time
  announcement. Parallel k-nearest-neighbor joins over large data on MapReduce.
  - **Why it is an exemplar:** a well-scoped data-processing operator with an **algorithm plus a
    scalability evaluation** on large data — the classic EDBT "extend the technology to a new scale
    or platform" contribution. The result is a reusable technique, not a one-dataset finding.
  - **Self-check:** does your algorithm target a named operator or workload, and is the evaluation at
    a scale where the problem actually bites?

### System + language — data integration

- **Koutrika et al., "HIL: A High-Level Scripting Language for Entity Integration," EDBT 2013**
  (EDBT 2023 Test-of-Time Award). Verified: dblp / OpenProceedings; EDBT Test-of-Time announcement.
  A high-level language for expressing entity-integration logic.
  - **Why it is an exemplar:** it turns a messy, recurring data-integration task into a **declarative
    language** with a runtime — an "extending database technology" contribution in the literal sense,
    evaluated on real integration scenarios. The point is an abstraction practitioners can reuse.
  - **Self-check:** does your abstraction or language make a real data-management task easier to
    express and execute, demonstrated on real data rather than a toy schema?

### Applied systems experience — ingestion in a real DBMS

- **Grover & Carey, "Data Ingestion in AsterixDB," EDBT 2015** (EDBT 2025 Test-of-Time Award).
  Verified: dblp / OpenProceedings; EDBT Test-of-Time announcement. Continuous data ingestion built
  into a real big-data management system.
  - **Why it is an exemplar:** it solves an **applied systems problem inside a real DBMS** —
    ingesting fast-arriving data feeds — and reports the design and its behavior. This is EDBT's
    applied/systems heart: extending a working system to a real operational need.
  - **Self-check:** is your contribution grounded in a real system and a real operational problem,
    with an evaluation a practitioner would trust?

### Technique — privacy-preserving data mining

- **Aggarwal & Yu, "A Condensation Approach to Privacy Preserving Data Mining," EDBT 2004** (EDBT
  2014 Test-of-Time Award). Verified: dblp / OpenProceedings; EDBT/ICDT 2014 Test-of-Time page.
  A condensation technique for mining data while preserving privacy.
  - **Why it is an exemplar:** a **general technique** for a durable data-management concern
    (privacy in analysis), evaluated on real data — an idea that traveled well beyond its first
    application. The contribution is a method others adopt.
  - **Self-check:** does your technique address a data-management concern that persists across
    systems, and is it evaluated so a skeptic would accept the trade-off it claims?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified EDBT exemplar | Edition | Method |
| --- | --- | --- | --- |
| System + architecture | "Shore-MT: a scalable storage manager..." | EDBT 2009 | Multicore storage engine |
| Distributed algorithm + evaluation | Zhang, Li & Jestes, "Parallel kNN joins in MapReduce" | EDBT 2012 | Parallel operator at scale |
| System + language | Koutrika et al., "HIL" | EDBT 2013 | Integration language + runtime |
| Applied systems experience | Grover & Carey, "Data Ingestion in AsterixDB" | EDBT 2015 | Ingestion in a real DBMS |
| Technique | Aggarwal & Yu, "A Condensation Approach..." | EDBT 2004 | Privacy-preserving data mining |

> Five verified papers across five contribution shapes, each an EDBT Test-of-Time honoree. A sixth,
> **Yan, Chakraborty, Parent, Spaccapietra & Aberer, "SeMiTri: a framework for semantic annotation
> of heterogeneous trajectories," EDBT 2011** (EDBT 2021 Test-of-Time Award), models the applied
> spatio-temporal / framework shape and is safe to add if that shape matches yours.

---

## Omitted for lack of clean EDBT verification (do not attribute to EDBT without re-checking)

To keep the list zero-hallucination, canonical database results whose founding papers appeared at
**SIGMOD, VLDB, ICDE, or ICDT** are **excluded** — those are exactly the sibling-venue confusions
the header warns about. Before adding any paper, confirm it on **dblp** and **OpenProceedings.org**
by matching the venue string to an **EDBT** edition (not SIGMOD, VLDB, ICDE, or the co-located
ICDT), then record authors, year, and pages/DOI, and update the access-date header. Remember that
EDBT and ICDT share a joint conference and a proceedings platform but are **separate venues** with
separate calls — an OpenProceedings ICDT paper is not an EDBT paper. When in doubt, omit. If web
search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
