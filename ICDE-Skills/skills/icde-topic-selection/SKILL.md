---
name: icde-topic-selection
description: Use when deciding whether a project is a strong IEEE ICDE fit, routing among the three database venues from ICDE's seat (SIGMOD's quarterly rounds vs PVLDB's monthly deadlines vs ICDE's two rounds), choosing ICDE research vs industry track, applying the data-management-primitive test, and comparing with TKDE, EDBT, or systems venues.
---

# ICDE Topic Selection

Use this before writing. ICDE is strongest for **data engineering** — the design, building,
management, and evaluation of data-intensive systems — where the contribution is a
reconstructable data-management primitive with a systems-grade evaluation.

## The data-management-primitive test

Ask what primitive the paper advances: an **access method**, a **query operator**, an
**execution or storage mechanism**, a **transaction or concurrency protocol**, a **data
integration/cleaning/provenance technique**, or a **scalable analytics engine**. If no
primitive exists — if the database is merely a container for a result that lives elsewhere —
the ICDE framing does not exist either.

## Routing from ICDE's seat: the three-venue triangle

The scopes of ICDE, SIGMOD, and VLDB overlap almost entirely, so routing is usually about
**calendar geometry and house culture**, not topic. Deciding from ICDE's seat:

| If the deciding factor is... | Lean toward | Because |
|---|---|---|
| You want two fixed shots a year and IEEE-Xplore proceedings | **ICDE** | Two rounds per edition (≈June + November), single-blind, IEEE format |
| You want quarterly journal-style rounds with a formal revision and a rejection embargo | **SIGMOD / PACMMOD** | Four rounds on the 17th, double-anonymous, 12-month embargo |
| You want to pick any month and submit on a rolling calendar | **VLDB / PVLDB** | Twelve monthly deadlines on the 1st, single-blind, revise verdict |
| The work is a shipped production system with deployment evidence | **ICDE industry track** (or SIGMOD industrial) | Non-academic co-author, production-scale story |
| The work needs journal-length treatment | **IEEE TKDE** or **The VLDB Journal** | Full-length exposition; ICDE best papers are invited to extend into TKDE anyway |
| The work is European-database-community facing | **EDBT** | Overlapping scope, different community and calendar |

## Fit signal table

| Signal in the project | ICDE reading |
|---|---|
| A new index, operator, or storage layout with a systems evaluation | Core fit — the house genre |
| A concurrency/transaction protocol exploiting new hardware | Core fit (cf. the Bw-Tree exemplar) |
| A platform primitive an ecosystem can build on | Core fit (cf. the SpatialHadoop exemplar) |
| A production cloud-database architecture with deployment lessons | Industry and applications track |
| An ML model that happens to run on data | Route to an ML venue unless the DB primitive is the contribution |
| A pure theory result with no system or workload | Route to a theory or journal venue |

## Sharpening moves before committing

- **Name the primitive in one sentence.** "We make ordering a read-time cost so ingestion is
  write-bandwidth-bound" is a primitive; "we improve time-series databases" is a topic.
- **Check the round you can actually hit.** Because a Round 1 reject skips you to the next
  edition, do not aim a half-built system at Round 1 just because it is sooner.
- **Decide research vs. industry honestly.** If the evidence is production scale and the
  novelty is engineering-at-scale rather than a new mechanism, the industry track fits better
  and reviews you on the right axis.
- Topic emphasis and track boundaries drift between editions; scan the current call's topic
  list before final routing.

## Output format

```text
[Fit] strong ICDE / possible ICDE / better elsewhere
[Primitive] <one-sentence data-management primitive, or "none">
[Best venue] ICDE-research / ICDE-industry / SIGMOD / PVLDB / TKDE / EDBT / other
[Round target] Round 1 or Round 2 of which edition, if ICDE
[Top rejection risk] <novelty / evaluation / scope / wrong-track>
[Next action] <build, measure, reframe, or venue switch>
```
