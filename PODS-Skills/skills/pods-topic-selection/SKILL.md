---
name: pods-topic-selection
description: Use when deciding whether a data-management project belongs at ACM PODS (the database-theory symposium) or should be routed to SIGMOD/VLDB/ICDE (systems), ICDT (its sister theory venue), LICS/ICALP/STOC (pure theory), or a journal (TODS/LMCS/JACM), by contribution shape, the result-swap test, and the PODS-vs-ICDT community fit.
---

# PODS Topic Selection

Decide the venue before drafting. **PODS** — the ACM SIGMOD/SIGACT Symposium on **Principles of
Database Systems** — is the theoretical-foundations symposium held jointly with SIGMOD each year. Its
papers are **theorems about data management**: models, query languages, complexity bounds,
dichotomies, logic, and provably optimal algorithms. A technically strong paper whose real
contribution is a faster system, a benchmark win, or an engineering artifact is respected and then
rejected as out of scope — that paper is SIGMOD/VLDB/ICDE. PODS reviewers read for a **provable,
foundational** statement about a cleanly defined model.

## The routing question that matters most

The decisive question is rarely "is this about databases?" but **"is the contribution a theorem or a
system?"** If the headline is a bound, a dichotomy, a semantics, an expressiveness result, or an
algorithm with a *matching lower bound*, it is PODS-shaped. If the headline is throughput, latency,
or accuracy on real workloads — even with clever theory inside — its home is a systems-DB flagship.
PODS and SIGMOD share a week and a hallway but not a bar for acceptance.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| A bound, dichotomy, semantics, or provably optimal algorithm in a data model | **PODS** | The database-theory symposium; results are theorems with proofs |
| A system, index, or optimizer evaluated on real workloads for performance | **SIGMOD / VLDB / ICDE** | The systems-DB flagships; evidence is measured, not proved |
| Database theory, but you want the EDBT/ICDT federation or missed the PODS cycle | **ICDT** | PODS's sister theory venue; overlapping community and reviewer pool, different calendar |
| Pure logic / finite model theory with no data-management payoff | **LICS / ICALP / STOC / FOCS** | Theory venues; PODS wants the data-management motivation to be central |
| A deep, long development beyond a 15-page symposium result | **TODS / LMCS / JACM / VLDBJ** | Journals with no symposium page ceiling; often the full-version home |
| Applied ML-for-data with empirical validation as the point | **SIGMOD / VLDB / a ML venue** | Not a PODS theorem; route to where the evidence is measured |

## Contribution shapes PODS rewards

- **A new semantics or framework** for an ill-defined problem — consistent query answering, provenance
  semirings, a data model for uncertainty — stated precisely and studied for decidability/complexity.
- **A complexity classification** — a dichotomy (PTIME vs. hard), a fine-grained bound, a
  data-vs-combined-complexity separation over a query class.
- **An expressiveness or logic result** — which logical language captures an operation (composition,
  view definition, path querying), with matching upper and lower bounds.
- **A provably optimal algorithm** — a worst-case-optimal join, a constant-delay enumeration
  procedure, an MPC-round bound — the guarantee is a *theorem*, not a measured speedup.
- **Foundations of emerging data problems** — differential privacy for queries, learning-theoretic
  guarantees for data tasks, graph-query theory — where PODS supplies the rigor.

## The result-swap and re-label tests

Two quick tests sharpen a borderline verdict:

- **Result-swap test:** if you replaced your specific algorithm or construction with a different one,
  would a theorem still remain (a bound, a classification, an impossibility)? If not, the artifact is
  the contribution and a systems venue fits better.
- **Re-label test:** could this paper be submitted to SIGMOD unchanged and read as native there? If
  its heart is a measured system with theory as garnish, route to SIGMOD/VLDB; if its heart is a
  proof, PODS is home. The mirror also holds for ICDT — if the paper is pure logic with no
  data-management question driving it, ICDT or LICS may fit better than PODS.

## Maturity, without the ladder cliché

Fit is necessary but not sufficient. A conjecture with partial evidence but no proof is a workshop or
a Gems-of-PODS talk, not a research paper; a theorem whose proof only handles a special case needs
the general result or an honest scope; a sprawling development that cannot breathe in 15 pages plus
appendix may belong in a journal first, with a PODS extended abstract of the core theorem. Submitting
a half-proved result costs a full cycle even when the topic is perfect.

## Cheap reconnaissance before committing

```text
[Scope]     scan the last two PODS proceedings (dblp db/conf/pods, PACMMOD PODS track) for your
            subarea -> 3+ recent papers = a reviewer pool exists; 0 = mismatch or ICDT/LICS territory
[Citations] is your bibliography majority PODS/ICDT/LICS/TODS/JACM, or majority SIGMOD/VLDB?
            -> majority systems venues => reviewers may read you as a systems paper; reframe the intro
[Calendar]  PODS runs two cycles a year; compare the next PODS cycle with ICDT's and the systems
            deadlines, and route to the nearest honest fit rather than idling
```

## Decision procedure

```text
[Contribution] theorem (bound/dichotomy/semantics/optimal algorithm) or measured system?
[Model]        is there a cleanly defined data/query model the result is about?
[PODS vs ICDT] data-management theory with the SIGMOD community pull -> PODS; EDBT/ICDT federation
               fit or calendar -> ICDT
[Systems check] performance is the headline -> SIGMOD/VLDB/ICDE, not PODS
[Verdict]      PODS / ICDT / systems flagship / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is PODS, continue with `pods-workflow` for the two-cycle calendar and `pods-writing-style` for the
paper shape.
