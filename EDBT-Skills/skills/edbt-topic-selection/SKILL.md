---
name: edbt-topic-selection
description: Use when deciding whether a data-management project belongs at EDBT or should be routed to SIGMOD, VLDB/PVLDB, ICDE, the co-located ICDT theory venue, or a database journal, and when choosing the EDBT paper shape (Regular / Experiments-&-Analysis / Vision) and the nearest submission cycle.
---

# EDBT Topic Selection

Decide the venue and the paper shape before drafting. EDBT — the International Conference on
**Extending Database Technology** — is the European database-systems flagship, held jointly with
**ICDT** (its theory sibling) and published open access on OpenProceedings.org. Its reviewers read
for a **contribution that extends real database technology**: systems, applied data management, and
experiments-and-analysis work. A paper whose true center is a complexity result, a pure-ML model, or
a US-flagship-scale systems marathon may be respected and then rerouted.

## The routing question that matters most

EDBT overlaps heavily with SIGMOD, VLDB, and ICDE in scope and reviewer pool, so the decisive
question is rarely "is this databases?" but **"which database community, publication model, and
cycle fits this paper now?"** Two EDBT-specific pulls tilt the answer:

- **The rolling cycle is often the nearest honest deadline.** EDBT's three cycles a year mean a
  ready paper rarely waits long; if SIGMOD/ICDE/PVLDB's next window is months out, the near EDBT
  cycle can be the rational choice for a finished contribution.
- **Open access matters to some authors and funders.** OpenProceedings' CC-BY-NC-ND, author-retained
  copyright, no-APC model is a genuine reason to prefer EDBT over the paywalled ACM/IEEE DLs.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| A contribution that *extends database technology* — systems, applied data management, experiments — ready now, EDBT cycle nearest | **EDBT** | European DB-systems flagship; OpenProceedings open access; rolling cycles |
| A flagship-scale systems result you want in the ACM DB community's marquee venue | **SIGMOD** | US flagship, ACM DL; different cycle and template |
| A polished journal-style systems paper aiming at the PVLDB monthly pipeline | **VLDB / PVLDB** | Journal-style monthly deadlines; different review model |
| A broad data-engineering contribution wanting the IEEE venue and stage | **ICDE** | IEEE DL; sibling flagship, different calendar |
| The heart is a **complexity, query-language, or dependency-theory** result | **ICDT** | EDBT's co-located theory sibling — theory belongs there, not in EDBT |
| Too long or too deep for the page budget, or a survey | **VLDBJ / TODS / TKDE** | Journals with no conference page ceiling |

## Contribution shapes EDBT rewards (and the paper shape they map to)

- **System + architecture / mechanism** — a storage, query-processing, indexing, transaction, or
  integration mechanism, embodied in a real system and measured on real workloads → **Regular**.
- **Distributed / scalable algorithm** — an operator or method that extends processing to a new
  scale, platform, or data type, with a scalability evaluation → **Regular**.
- **Experiments & Analysis** — a rigorous benchmarking, repeatability, or comparative study where
  the *measurement itself* is the contribution → **Experiments & Analysis** paper.
- **Applied data management / experience** — extending a working system to a real operational need,
  reported honestly → **Regular**.
- **Forward-looking idea** — a well-argued new direction not yet fully built or evaluated →
  **Vision** paper (short).

## The theory-vs-systems test (the EDBT/ICDT boundary)

Because EDBT and ICDT share a conference and a proceedings platform, the sharpest routing mistake is
sending a theory paper to EDBT (or an unbuilt systems idea to ICDT):

- **If the core result is a theorem** — a complexity bound, an expressiveness or decidability result,
  a query-language or constraint-theory contribution — it belongs at **ICDT**, not EDBT, even though
  they meet in the same week.
- **If the core result is a built-and-measured system or a data-analysis study**, it belongs at
  **EDBT**. Being able to co-present near the theory community is a benefit of EDBT, not a reason to
  submit theory to it.

## The scale-and-community test (EDBT vs. the US flagships)

- **Scale realism, not scale maximalism.** EDBT values evaluations on realistic workloads and honest
  scope; a paper does not need US-flagship-scale infrastructure to be strong here, but its claims
  must match its evidence.
- **Community pull.** If your bibliography and closest prior work are European DB-systems papers and
  the near cycle fits, EDBT is a natural home; if the paper is in explicit dialogue with a
  SIGMOD/PVLDB line and aims at that audience, weigh the sibling.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two EDBT programs (dblp, OpenProceedings) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Boundary] is the core a theorem (-> ICDT) or a built/measured system-or-study (-> EDBT)?
[Citations] is your bibliography majority DB venues (SIGMOD/VLDB/ICDE/EDBT/ICDT)?
          -> majority non-DB => reviewers read you as a visitor; naturalize the intro first
[Calendar] compare the next EDBT cycle with SIGMOD/PVLDB/ICDE dates -> route to the nearest
          honest fit rather than idling
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> DB systems builders / practitioners / researchers?
[Claim type] system / scalable algorithm / experiments-&-analysis / applied experience / vision / theory
[Theory check] is the heart a theorem? -> route to ICDT
[EDBT vs US flagship] all fit? -> choose by open-access preference, cycle proximity, community pull
[Shape] Regular / Experiments-&-Analysis / Vision, matched to the contribution
[Verdict] EDBT (which shape, which cycle) / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue or shape decision wastes every later step. When
the verdict is EDBT, continue with `edbt-workflow` for the cycle calendar and `edbt-writing-style`
for the paper shape.
