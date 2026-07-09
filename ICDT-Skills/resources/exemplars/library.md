# ICDT Exemplars Library (contribution shape × subarea)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ICDT proceedings / databasetheory.org awards pages** to confirm it appeared at
> the **International Conference on Database Theory (ICDT)** — matching title, authors, year, and
> the ICDT venue string — and, where noted, that it received the **ICDT Test-of-Time Award**. Papers
> that could not be cleanly confirmed as ICDT (as opposed to **PODS**, STOC, or a journal) were
> **omitted and documented below**. It is deliberately a short, verified list (4 verified > 15
> guessed).
>
> **Sibling-confusion guard:** ICDT is **not PODS**, **not** STOC/LICS/ICALP, and **not** a journal.
> Several canonical data-management results were introduced at **PODS** or in journals instead; a
> famous author or a familiar result does **not** prove an ICDT placement. Each row was checked to be
> an ICDT edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, bounds, or proofs — read the original on DROPS/dblp or the arXiv full
> version before citing anything. For ICDT-specific policy and the two-cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × subarea** is closest to yours, then study how that paper
states a **precise database-theory problem**, proves a **complete result** (often with matching
bounds), and makes its **consequence for data management** explicit — the ICDT bar (see
[`../../skills/icdt-writing-style/SKILL.md`](../../skills/icdt-writing-style/SKILL.md),
[`../../skills/icdt-topic-selection/SKILL.md`](../../skills/icdt-topic-selection/SKILL.md), and
[`../../skills/icdt-experiments/SKILL.md`](../../skills/icdt-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "ICDT-shaped."

All four rows are **ICDT Test-of-Time** honorees, so they also model what "influence a decade later"
looks like at this venue.

---

## By contribution shape

### Foundational framework — data integration / data exchange

- **Fagin, Kolaitis, Popa & Miller, "Data Exchange: Semantics and Query Answering," ICDT 2003.**
  Verified: dblp `conf/icdt`; databasetheory.org ICDT awards (Test-of-Time honoree); a journal
  version appeared in *Theoretical Computer Science* (2005). Founded the theory of **data exchange**:
  a semantics for materializing a target instance under schema mappings, and the notion of **certain
  answers** for querying it.
  - **Why it is an exemplar:** it takes a practical data-integration problem and gives it a **precise
    formal semantics** plus a complexity analysis, creating a framework the community built on for
    two decades. The database-management payoff is explicit, not decorative.
  - **Self-check:** does your paper give a *definition and semantics* a whole subarea could adopt, not
    just a single bound?

### Provenance / probabilistic databases — compilation and complexity

- **Jha & Suciu, "Knowledge Compilation Meets Database Theory: Compiling Queries to Decision
  Diagrams," ICDT 2011, pp. 162-173.** Verified: dblp `conf/icdt/JhaS11`; **ICDT 2021 Test-of-Time
  Award**. Connects **query lineage** to knowledge-compilation target languages (read-once formulae,
  OBDD, FBDD, d-DNNF) of increasing power, linking a query's static structure to the size of the
  resulting diagram.
  - **Why it is an exemplar:** it bridges two fields with a **precise complexity result** — which
    queries compile efficiently into which target language — the kind of crisp, consequence-bearing
    theorem ICDT prizes.
  - **Self-check:** is your result a *characterization* (which inputs admit an efficient object) with
    the boundary proved, not just an upper bound on one case?

### Query-result representation — factorised databases

- **Olteanu & Závodný, "Factorised Representations of Query Results: Size Bounds and Readability,"
  ICDT 2012.** Verified: dblp `conf/icdt`; **ICDT 2022 Test-of-Time Award**. Introduced **factorised
  representations** of query answers, building relations from singleton tuples via union and product
  to avoid redundancy, with **size bounds** tied to query structure.
  - **Why it is an exemplar:** a new **representation system** with matching size bounds — a
    contribution that is simultaneously a definition, a set of tight bounds, and a practical lever for
    query evaluation.
  - **Self-check:** if you propose a representation or data structure, do you prove **both** how small
    it can be and when it cannot be smaller?

### Data markets / privacy theory — pricing

- **Li, Li, Miklau & Suciu, "A Theory of Pricing Private Data," EDBT/ICDT 2013 (ICDT track), Genoa,
  pp. 33-44.** Verified: researchr `LiLMS13`; dblp; a journal version appeared in *ACM TODS* (2014);
  **ICDT Test-of-Time honoree**. A framework for **pricing noisy query answers** as a function of
  accuracy, and for dividing the price among data owners compensated for privacy loss.
  - **Why it is an exemplar:** it opens a **new problem space** for database theory with a formal
    model and provable properties (arbitrage-freeness), showing ICDT rewards foundational framing of an
    emerging topic, not only bounds on an old one.
  - **Self-check:** if your paper opens a new area, does it give **axioms/properties and proofs** that
    a follow-on literature could stand on, rather than a single motivating example?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified ICDT exemplar | Edition | Subarea |
| --- | --- | --- | --- |
| Foundational framework | Fagin, Kolaitis, Popa & Miller, "Data Exchange…" | ICDT 2003 | Data integration / exchange |
| Characterization + complexity | Jha & Suciu, "Knowledge Compilation Meets Database Theory" | ICDT 2011 | Provenance / probabilistic DB |
| Representation + tight bounds | Olteanu & Závodný, "Factorised Representations…" | ICDT 2012 | Query-result representation |
| New-area framework | Li, Li, Miklau & Suciu, "A Theory of Pricing Private Data" | EDBT/ICDT 2013 | Data markets / privacy |

> Four verified ICDT Test-of-Time honorees across four contribution shapes. They also show ICDT's
> range: from founding a subarea (data exchange) to opening a new one (data pricing), always via a
> precise theorem with a data-management consequence.

---

## Omitted for lack of clean ICDT verification (do not attribute to ICDT without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Data Exchange: Getting to the Core" (Fagin, Kolaitis, Popa)** — the companion core-computation
  paper appeared at **PODS 2003**, *not* ICDT, despite the shared authors and topic with the ICDT 2003
  data-exchange paper. A direct sibling-venue trap; listed only as a guardrail.
- **"Consistent Query Answers in Inconsistent Databases" (Arenas, Bertossi & Chomicki)** — the
  founding consistent-query-answering paper is **PODS 1999**, not ICDT. Omitted.
- **"Optimal Implementation of Conjunctive Queries in Relational Databases" (Chandra & Merlin)** —
  the containment/minimization classic is **STOC 1977**, not ICDT. Omitted.
- **Any ICDT journal-version attribution** — several ICDT papers have extended journal versions (TCS,
  TODS, LMCS); cite the ICDT conference paper for the ICDT attribution and the journal article
  separately, never conflate them.

Before adding any paper, confirm it on **dblp** and the **ICDT proceedings** by matching the venue
string to an ICDT edition (not PODS, STOC, LICS, or a journal), then record authors, year, and
pages/DOI, and update the access-date header. When in doubt, omit. If web search is unavailable, add
the row as **待核实 / TO VERIFY** with **no attribution**.
