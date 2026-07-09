# ACM PODS Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at the **ACM SIGMOD/SIGACT
> Symposium on Principles of Database Systems (PODS)** — matching title, author list, year, and
> venue string. Papers that could not be cleanly confirmed as PODS (as opposed to SIGMOD, VLDB,
> ICDT, ICDE, LICS, or a journal) were **omitted and documented below**. It is deliberately a
> short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** PODS is **not** SIGMOD, **not** VLDB, **not** ICDE (those are the
> systems-DB flagships), **not** ICDT (its sister theory venue in the EDBT/ICDT federation), and
> **not** PODC (Principles of *Distributed* Computing). A famous author or a familiar result does
> **not** prove PODS; several database-theory landmarks appeared at ICDT, LICS, STOC, or in TODS/JACM
> instead. Each row was checked to be a PODS edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorem statements, bounds, or proofs — read the original on ACM DL before
> citing anything. For PODS-specific policy, scope, and the multi-cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
**names a clean model and problem**, states a **precise result** (a bound, a dichotomy, a semantics,
an algorithm with a matching guarantee), and supplies a **complete proof** — the PODS bar (see
[`../../skills/pods-writing-style/SKILL.md`](../../skills/pods-writing-style/SKILL.md),
[`../../skills/pods-topic-selection/SKILL.md`](../../skills/pods-topic-selection/SKILL.md), and
[`../../skills/pods-experiments/SKILL.md`](../../skills/pods-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "PODS-shaped."

Several rows are ACM PODS **Alberto O. Mendelzon Test-of-Time** or **Best Paper** honorees, so they
also model what "influence a decade later" looks like at this venue.

---

## By contribution shape

### New semantics / framework — querying inconsistent data

- **Arenas, Bertossi & Chomicki, "Consistent Query Answers in Inconsistent Databases," PODS 1999,
  pp. 68-79.** Verified: dblp `db/conf/pods/pods99` / ACM DL. Introduced **consistent query
  answering (CQA)** — the certain answers over all minimal repairs of a database violating its
  integrity constraints.
  - **Why it is an exemplar:** it turns a vague practical worry ("my data violates its constraints")
    into a **precise semantics** with a decidability/complexity program, opening a research area that
    ran for two decades. The model is simple to state and the results are provable.
  - **Self-check:** does your paper define a clean semantics for a problem the field only had
    informal notions of, and then prove something about deciding or computing it?

### Logic of data integration — schema-mapping composition

- **Fagin, Kolaitis, Popa & Tan, "Composing Schema Mappings: Second-Order Dependencies to the
  Rescue," PODS 2004, pp. 83-94** (DOI 10.1145/1055558.1055572; journal version TODS 30(4), 2005).
  Verified: dblp `db/conf/pods/pods2004`. Showed that composing source-to-target tgds requires
  **second-order tgds**, giving data exchange its logical foundations.
  - **Why it is an exemplar:** it identifies the *right* logical language for an operation
    (composition) the field needed but could not express, and proves both a positive
    (expressiveness) and a negative (first-order insufficiency) result — the classic PODS "we found
    the correct formalism" move.
  - **Self-check:** does your contribution pin down the exact expressive power a data-management
    operation demands, with a matching upper and lower bound?

### Algebraic framework — provenance

- **Green, Karvounarakis & Tannen, "Provenance Semirings," PODS 2007, pp. 31-40** (DOI
  10.1145/1265530.1265535). Verified: ACM DL / dblp; later a Gems-of-PODS / Test-of-Time subject.
  Unified why-, lineage-, and trust-provenance as **annotations in a commutative semiring**.
  - **Why it is an exemplar:** one algebraic abstraction explains several previously ad-hoc
    provenance notions and shows `N[X]` is universal — a framework whose payoff is that everyone
    else's special case falls out of it. Elegance with a proof of universality.
  - **Self-check:** does your framework subsume several existing notions as instances, and do you
    prove the generality rather than assert it?

### Complexity dichotomy — probabilistic query evaluation

- **Dalvi & Suciu, "The Dichotomy of Conjunctive Queries on Probabilistic Structures," PODS 2007,
  pp. 293-302.** Verified: ACM DL / dblp. Proved that every self-join-free conjunctive query on a
  tuple-independent probabilistic database is **either polynomial-time or #P-hard** to evaluate —
  a sharp dichotomy.
  - **Why it is an exemplar:** it is the archetypal PODS result shape — a **complete classification**
    with no middle ground, drawing a hard line across a whole query class. The contribution is the
    dichotomy theorem, not a system.
  - **Self-check:** can you classify *every* instance in your space as tractable or hard, and prove
    both sides — or do you only have scattered examples?

### Optimal algorithm + matching bound — join processing

- **Ngo, Porat, Ré & Rudra, "Worst-case Optimal Join Algorithms," PODS 2012.** Verified: ACM DL /
  dblp; **PODS 2012 Best Paper Award** and later an ACM PODS Alberto O. Mendelzon Test-of-Time
  honoree. Gave a join algorithm meeting the **AGM bound** (Atserias-Grohe-Marx) on output size,
  which no traditional pairwise plan achieves.
  - **Why it is an exemplar:** a theory result (a size bound) is turned into an **algorithm with a
    matching worst-case guarantee**, and the technique later resonated in practice (Leapfrog
    Triejoin). Provable optimality, then real influence — the PODS ideal.
  - **Self-check:** does your algorithm come with a **matching lower bound** proving it optimal in
    the stated model, rather than "faster in our runs"?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified PODS exemplar | Edition | Method |
| --- | --- | --- | --- |
| New semantics / framework | Arenas, Bertossi & Chomicki, "Consistent Query Answers..." | PODS 1999 | Repairs + certain answers |
| Logic of data integration | Fagin, Kolaitis, Popa & Tan, "Composing Schema Mappings" | PODS 2004 | Second-order tgds |
| Algebraic framework | Green, Karvounarakis & Tannen, "Provenance Semirings" | PODS 2007 | Semiring annotations |
| Complexity dichotomy | Dalvi & Suciu, "The Dichotomy of Conjunctive Queries..." | PODS 2007 | PTIME/#P-hard classification |
| Optimal algorithm + bound | Ngo, Porat, Ré & Rudra, "Worst-case Optimal Join Algorithms" | PODS 2012 | AGM-bound-matching join |

> Five verified papers across five contribution shapes. Together they show PODS's core modes:
> **defining a semantics**, **finding the right logic**, **building a unifying framework**,
> **classifying complexity**, and **proving an algorithm optimal** — every one carried by a theorem
> and a proof, not a benchmark.

---

## Omitted for lack of clean PODS verification (do not attribute to PODS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Data Exchange: Semantics and Query Answering" (Fagin, Kolaitis, Miller, Popa)** — the founding
  data-exchange paper appeared at **ICDT 2003** (and in TCS), *not* PODS. A direct sister-venue
  trap; the composition paper above *is* PODS 2004, but this one is not.
- **The AGM size bound itself (Atserias, Grohe & Marx)** — published at **FOCS 2008**, a theory
  conference, not PODS. Cite it for the bound; cite Ngo et al. PODS 2012 for the algorithm.
- **Leapfrog Triejoin (Veldhuizen)** — appeared at **ICDT 2014**, not PODS. Omitted.
- **Codd / Vardi / Chandra-Merlin foundational complexity results** — the canonical query-complexity
  papers are **STOC/JACM/TODS**, not PODS; do not backfill them as PODS placements.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to a
PODS edition (not SIGMOD, VLDB, ICDE, ICDT, LICS, or a PL/theory venue), then record authors, year,
and DOI/pages, and update the access-date header. When in doubt, omit. If web search is unavailable,
add the row as **待核实 / TO VERIFY** with **no attribution**.
