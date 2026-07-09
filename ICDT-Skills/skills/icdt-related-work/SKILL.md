---
name: icdt-related-work
description: Use when positioning an ICDT (International Conference on Database Theory) paper against the database-theory literature — covering the ICDT/PODS lineage, finite model theory and complexity, delta-first positioning against the nearest prior theorem, honest treatment of overlapping bounds, and keeping self-citations anonymous under the since-2024 rule.
---

# ICDT Related Work

Position the paper against the **exact prior theorems** it advances. At ICDT the related-work
section is where a referee checks whether your result is genuinely new or a re-proof of something in
the ICDT/PODS canon, so vague "much work has been done" prose is a liability. Every neighboring
result should be named, its bound stated, and your delta made precise.

## Cover the database-theory lanes

A database-theory paper usually sits in one or more of these literatures; name the relevant ones and
the closest results in each:

- **Query languages and expressiveness** — CQs/UCQs, Datalog and its fragments, FO, regular path
  queries, and the separations between them.
- **Complexity of query evaluation** — combined/data/query complexity, dichotomies, parameterized
  and fine-grained bounds.
- **Finite model theory** — locality, games, zero-one laws, descriptive complexity as it applies to
  databases.
- **Constraints and reasoning** — TGDs/EGDs, the chase, decidability of implication and query
  answering under constraints.
- **Consistent query answering and inconsistency** — repairs, certain answers, complexity of CQA.
- **Provenance and semiring semantics** — annotated relations, provenance polynomials.
- **Data integration and exchange** — schema mappings, certain answers, the theory behind ETL.

## Delta-first positioning

State your advance against the nearest theorem, not against a field:

> "For [class], [Author, ICDT/PODS year] established a [complexity] upper bound but left the lower
> bound open; we close it, showing the problem is [class]-complete, and extend the result to
> [broader class]."

- Name the **closest prior bound** and say precisely how yours differs — tighter, broader, a matching
  lower bound, a new model, a removed assumption.
- If a prior result **subsumes a special case** of yours, say so and explain what your generality
  buys.
- If two lines of work **appear to conflict** with yours (e.g., a claimed hardness vs your
  tractability), reconcile them — usually a difference in the model or complexity measure — rather
  than ignoring one.

## Honesty about overlapping and concurrent results

- **Concurrent work** at the other flagship: if a PODS or arXiv result overlaps, cite it and
  delineate the independent contribution; the database-theory community is small and referees know
  the concurrent papers.
- **Journal versions:** distinguish a conference result from its extended journal version when both
  exist; attribute the bound to the right one.
- **Do not inflate novelty** by omitting the nearest neighbor — a referee who knows the omitted paper
  reads the omission as either ignorance or evasion.

## Anonymous self-citation (since 2024)

ICDT regular submissions are anonymous, so your own prior theorems need third-person handling:

- Write "Building on the chase-based construction of [17]…", never "our earlier ICDT paper [17]."
- Do not let a self-citation pattern (citing one author cluster heavily, in the first person)
  de-anonymize you.
- If your result critically depends on an unpublished companion paper, cite it anonymously
  ("[Anon]") per the current call's wording rather than naming yourself — confirm the exact
  mechanism in the live CfP.

## What not to do

- **Related work as a bibliography dump** — a paragraph of citations with no bound stated proves
  nothing about your delta.
- **Positioning against systems papers only** — an ICDT contribution is positioned against theorems;
  cite EDBT/SIGMOD work for motivation, not for the technical delta.
- **Claiming an open problem is open** without checking the recent ICDT/PODS programs — it may have
  been closed last cycle.

## Output format

```text
[Lanes covered] <which database-theory literatures the paper touches>
[Nearest prior] <closest theorem, its bound, its venue/year>
[Delta] <tighter | broader | matching lower bound | new model | removed assumption>
[Concurrent] <overlapping PODS/arXiv results cited and delineated? yes/no>
[Anonymity] self-citations third-person and non-identifying? yes/no
[Fix queue] <ordered edits>
```
