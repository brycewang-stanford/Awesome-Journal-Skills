---
name: icdt-topic-selection
description: Use when deciding whether a database-theory project belongs at ICDT (International Conference on Database Theory) or should be routed to PODS, the co-located EDBT systems track, a pure-TCS venue (LICS, ICALP, STACS), or a journal (ACM TODS, LMCS, TheoretiCS), and when distinguishing ICDT from its sibling database-theory flagship PODS by calendar, publisher, and community.
---

# ICDT Topic Selection

Decide the venue before drafting. ICDT — the International Conference on Database Theory — is the
**European foundations-of-data-management** venue, held jointly with **EDBT** and published **open
access in LIPIcs**. Its referees read for a **precise theorem with a clear consequence for data
management**: query languages, the complexity of query evaluation, finite model theory over
databases, consistent query answering, provenance, and the theory of data integration. A technically
strong paper whose real content is generic complexity theory, pure logic, or a systems benchmark is
respected and then rejected as out of scope.

## The routing question that matters most

ICDT and **PODS** are the two database-theory flagships and overlap almost completely in scope, so
the decisive question is rarely "is this database theory?" but **"which of the two theory venues,
and which calendar and publisher, fits this paper now?"** Both want a real theorem with a
data-management payoff. Use the finer signals below and the live deadlines to choose.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Foundational data-management theorem; you want European co-location and the next ICDT cycle is nearer | **ICDT** | Two-cycle LIPIcs venue with a Cycle-1 revision option; co-located with EDBT |
| Same kind of theorem, but PODS's single annual cycle lands better or you want the SIGMOD stage | **PODS** | The other database-theory flagship; ACM PACMMOD, co-located with SIGMOD |
| The contribution is a *system*, an algorithm with an experimental evaluation, or a benchmark | **EDBT** (co-located) or a systems venue | Experimental data management, not a theorem — the reproducibility track lives here |
| The core is generic finite model theory / logic with no data-management consequence | **LICS / ICALP / STACS** | EATCS/logic venues reward the theory itself; ICDT wants the querying/constraints payoff |
| The result is too long, or wants a full journal treatment with all proofs | **ACM TODS / LMCS / TheoretiCS** | Journals with no page ceiling; some are the natural home for the extended version |
| A neat connection between database theory and a neighboring field, short | **ICDT "Database Theory in Action"** | The 4-page non-anonymous track for bridging results and applications |

## What makes a paper ICDT-shaped

- **A theorem about querying or data.** A new expressiveness result, a tight complexity bound for
  evaluating a query language, a decidability/undecidability result for a class of constraints, a
  dichotomy — with the database-theory consequence stated, not implied.
- **Matching upper and lower bounds** where the field expects them; a one-sided bound is often a
  "revise," not an accept.
- **A model that connects to data management.** Finite structures, relational/graph/semistructured
  data models, incomplete or inconsistent databases, provenance semirings, integration mappings —
  the "database" in the name is load-bearing.
- **Foundational or conceptual advances** — a new framework, a semantics, or a proof technique that
  the data-management theory community can build on.

## The two sharpening tests

- **PODS-swap test:** could this paper appear at PODS and read as native there? Almost certainly yes
  — so the choice is by **calendar, publisher preference (open-access LIPIcs vs ACM PACMMOD), and
  community pull**, not by scope. Pick the nearer honest deadline unless a specific reason favors the
  other.
- **Consequence test:** strip the data-management framing — is there still a database-theory lesson,
  or just a complexity/logic result? If only the latter survives, a pure-TCS venue fits better and
  ICDT referees will say the data connection is decorative.

## Maturity, without the ladder cliché

An idea sits at different doors depending on how finished the proof is. A conjecture with partial
evidence is a workshop or "in action" contribution, not a regular ICDT paper; a theorem with a gap
you can close belongs in **Cycle 1** where the revision option exists; a fully worked, book-length
treatment belongs in a **journal**. Submitting a one-sided bound when the field expects a matching
one costs a cycle.

## Cheap reconnaissance before committing

```text
[Scope]    scan the last two ICDT and PODS programs (dblp, databasetheory.org) for your subarea
           -> present at both = pick by calendar; present at neither = mismatch or a new opening
[Citations] is your bibliography majority ICDT/PODS/LICS/TODS/LMCS?
           -> majority systems venues => you may actually have an EDBT/SIGMOD paper
[Calendar] compare the next ICDT cycle deadline with the PODS deadline and journal timelines
           -> route to the nearest honest fit; ICDT's two cycles give you two shots a year
```

## Decision procedure

```text
[Consequence] who in data management cares if the theorem holds? -> real payoff or decorative?
[Claim type] expressiveness / complexity / decidability / semantics / framework
[ICDT vs PODS] both fit? -> choose by calendar, open-access LIPIcs vs PACMMOD, community pull
[Sibling check] systems+experiments -> EDBT; pure logic -> LICS/ICALP; over-long -> journal
[Verdict] ICDT regular track / PODS / EDBT / TCS venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is ICDT, continue with `icdt-workflow` for the two-cycle calendar and `icdt-writing-style` for the
theorem-proof shape.
