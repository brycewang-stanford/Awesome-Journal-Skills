---
name: vldb-topic-selection
description: Use when deciding whether a project belongs at VLDB and in which PVLDB category, applying the data-management-primitive test, choosing among Regular, EA&B, Scalable Data Science, and Vision papers, and routing against SIGMOD, ICDE, CIDR, EDBT, PODS, KDD, systems venues, and The VLDB Journal.
---

# VLDB Topic Selection

Use this before a line is written. Two decisions hide in "let's send it to
VLDB": whether the work is a data-management contribution at all, and which
PVLDB category gives it the friendliest reviewer expectations.

## The primitive test

VLDB rewards work whose core object is a **data-management primitive**:
storage layout, index, query optimization or execution, transaction and
consistency machinery, data integration and cleaning, streaming state, or the
data infrastructure under ML. Two probes:

- Strip the application narrative. Is what remains a reusable mechanism for
  managing data at scale? If what remains is a model architecture or an
  application result, the primitive is missing.
- Would the evaluation chapter naturally measure throughput, latency,
  scalability, or result quality on data systems? If the natural evaluation
  is task accuracy alone, an ML or applied venue fits better.

## Category routing inside PVLDB

| Your situation | Category | Watch out |
|---|---|---|
| New mechanism + built system + systems evidence | Regular Research (12 pp) | The default; full evaluation burden |
| Rigorous measurement of existing systems, no new system | EA&B (12 pp) | Reproducibility evaluation is mandatory; conclusions must generalize |
| Scale-forward data-science pipeline, practice first | Scalable Data Science (8 pp) | Must still show the data-management lesson, not just an application win |
| Argued agenda without a full system yet | Vision (6 pp) | Small budget; needs a genuinely new direction, not a survey |

Category budgets and continuation for the live volume: verify on the
guidelines page before committing (see the source map's 待核实 ledger).

## Neighborhood routing

| Signal in the project | Better home |
|---|---|
| Quarterly-round rhythm preferred; identical scope | SIGMOD (PACMMOD rounds) — the closest sibling; pick by calendar fit and portfolio, not prestige folklore |
| Formal results: complexity, expressiveness, bounds | PODS or ICDT |
| Provocative architecture argument, prototype-grade evidence | CIDR |
| Solid engineering contribution, broader engineering scope | ICDE or EDBT |
| Mining/learning contribution where data infra is incidental | KDD or an ML venue |
| OS/network mechanism that happens to touch storage | SOSP/OSDI, NSDI, EuroSys |
| Outgrown 12 pages; wants archival depth | The VLDB Journal or TODS |
| Deployed production system, lessons-forward | VLDB industrial track (separate call) |

The practical VLDB-vs-SIGMOD tiebreaker in this collection's experience:
PVLDB's monthly gate and three-month revision suit projects whose evidence
matures unpredictably; SIGMOD's fixed rounds suit groups that plan in
quarters. Scope overlap is nearly total.

## Commitment checklist

```text
[ ] Primitive named in one sentence, no application words needed
[ ] Category chosen; its page budget fits the evidence plan
[ ] The one plot that would convince a builder is specified
[ ] Nearest three prior systems identified (see vldb-related-work)
[ ] If EA&B: willing and able to hand everything to the repro committee
[ ] Live volume's topics-of-interest list scanned for explicit fit
```

## Re-route triggers mid-project

- The system never gets built → Vision now, or CIDR.
- The interesting output became the measurement study → EA&B, embrace it.
- The contribution drifted into the model, not the data path → ML venue.
- Twelve pages cannot hold the proofs → PODS split or journal lane.

## Output format

```text
[Primitive] <one sentence> / absent (re-route)
[Category] regular / EA&B / SDS / vision — with page-budget check
[Venue ranking] <top choice + two alternates, one reason each>
[Convincer plot] <the decisive figure, described>
[Risk] <novelty / evidence scale / fit — the one that kills it>
[Next action] <build, measure, reframe, or switch venue>
```
