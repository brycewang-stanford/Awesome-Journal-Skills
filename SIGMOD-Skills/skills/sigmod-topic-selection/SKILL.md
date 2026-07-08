---
name: sigmod-topic-selection
description: Use when judging whether a project belongs at SIGMOD's research track, comparing it against PVLDB's rolling model, ICDE, PODS, KDD, CIDR, and TODS, weighing the industrial track for deployment papers, and testing whether the contribution is genuinely a data-management result rather than an application that touches data.
---

# SIGMOD Topic Selection

SIGMOD's research track wants contributions *to* data management — storage,
query processing, transactions, data integration, systems for and with ML,
data engineering at scale — where the advance would matter to someone
building or theorizing a data system. The commonest misroute is the
application paper that uses databases heavily but advances only its
application. Run the fit test before any writing investment.

## The core fit question

State the contribution in one sentence and inspect the direct object. "We
make **query optimization** better under X" is SIGMOD-shaped. "We make
**fraud detection** better using a database" is not, unless the fraud
workload forced a reusable data-management technique — in which case *that
technique* is the paper.

## Neighbor-venue decision table

| Signal in the project | Better home | Why |
|---|---|---|
| Data-management advance, evaluation ready now | SIGMOD round or PVLDB | Pick by calendar and model, below |
| Formal semantics, complexity, lower bounds | PODS | Co-located theory sibling with its own PC |
| Mining/ML method where data infra is incidental | KDD or an ML venue | SIGMOD PCs route these out fast |
| Provocative architecture vision, thin evaluation | CIDR | Evidence bar differs by design |
| Deployed-system experience, lessons, scale war stories | SIGMOD industrial track | Needs ≥1 non-academic author; separate CFP |
| Mature line needing definitive long-form treatment | TODS | Journal pace; also invites best SIGMOD papers |
| Broad data-engineering result, DB framing weak | ICDE | Same community, different flagship |

## SIGMOD vs. PVLDB: same field, different machinery

The two flagships overlap almost completely in scope; the choice is
mechanical, and worth making deliberately:

- **Cadence:** SIGMOD batches quarterly rounds into PACMMOD issues; PVLDB
  accepts monthly on a rolling basis into the year's volume.
- **Failure cost:** a SIGMOD rejection locks the track for 12 months; PVLDB's
  monthly gate makes retry geometry different — check its current
  resubmission rules rather than assuming symmetry.
- **Revision shape:** both use journal-style revisions now; the calendars
  and letter mechanics differ by cycle.
- **Practical rule:** with a result ready in week X, compute time-to-first-
  verdict at each venue's next gate and weigh it against where the work's
  nearest neighbors have been landing recently.

## Research vs. industrial track

If the contribution's strength is *that it runs in production* — scale,
operational lessons, design retrospectives of a shipped engine — the
industrial track evaluates it on those terms, while the research track would
demand novelty the deployment story may not carry. Requirements differ
(non-academic co-author, separate deadline calendar, own PC), and the SIGMOD
2027 industrial CFP was not yet posted as of 2026-07-08 — verify before
planning around it.

## Fit-sharpening moves

- Name the data-management primitive touched: an index, an optimizer rule,
  a consistency protocol, a storage layout, a data-cleaning operator. No
  primitive, no research-track paper.
- Check the current CFP's topics list; scope wording shifts by cycle, and
  ML-for-systems / systems-for-ML emphasis has been growing.
- Probe generality: does the technique survive outside your prototype?
  A PC of engine builders will ask "would this help Postgres/RocksDB/
  Spark," concretely.
- Read the last two PACMMOD issues in your area; if nothing there shares
  your problem statement, either you found a gap or you found a fit
  problem — decide which with evidence.

## Reading the venue's current appetite

Beyond the CFP's topic list, three observable signals calibrate fit:

- Scan the most recent PACMMOD issue's table of contents: the distribution
  of storage vs. query vs. ML-adjacent vs. data-integration papers is the
  revealed preference of the current PC structure.
- Award choices telegraph values — the Test-of-Time lineage (see
  `resources/exemplars/library.md`) consistently honors work that changed
  what systems *do*, not what benchmarks report.
- Keynote and tutorial themes at the last edition mark where the community
  believes its frontier is; a paper swimming with that current gets read
  more generously than the CFP text alone predicts.

```text
Quick probe: title your paper, then find five PACMMOD/PVLDB papers from
the last two years that would cite it. Cannot name five -> the fit
problem is upstream of the writing.
```

## One project, routed three ways

A fictional team builds learned cardinality estimation into a production
cloud optimizer. Three legitimate papers hide inside: the estimation
technique with guarantees and controlled evaluation (SIGMOD research or
PVLDB); the deployment retrospective with fleet-scale lessons (SIGMOD
industrial); the formal analysis of when learned estimators can beat
histograms (PODS). Shipping all three as one manuscript serves none of the
three PCs — and PACMMOD's overlap rule means the split must be genuine, with
disjoint results.

## Output format

```text
[Fit verdict] research track / industrial track / neighbor venue
[Primitive] the data-management object the paper advances
[One-sentence claim] with the direct object underlined
[Venue race] time-to-verdict SIGMOD round vs. PVLDB gate
[Split risk] salami-slicing vs. legitimate multi-paper plan
[Next step] write / re-scope / re-route, with rationale
```
