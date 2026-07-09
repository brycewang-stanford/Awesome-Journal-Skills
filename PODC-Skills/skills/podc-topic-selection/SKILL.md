---
name: podc-topic-selection
description: Use when deciding whether a distributed-computing result belongs at ACM PODC or should be routed to DISC, SPAA, OPODIS/SIROCCO/SSS, STOC/FOCS/SODA, a systems venue (ICDCS/DSN/OSDI/NSDI), a blockchain-theory venue (AFT/FC), or a journal (JACM / Distributed Computing) — and how to avoid the PODC-vs-PODS naming trap by reasoning about the distributed model and the cost measure.
---

# PODC Topic Selection

Decide the venue before drafting. PODC — the ACM Symposium on Principles of Distributed Computing —
is the SIGACT-SIGOPS home for the **theory** of distributed computing. Reviewers read for a
**provable guarantee in a precisely stated distributed model**: an algorithm with a complexity
bound, an impossibility, or a matching lower bound. A technically strong paper whose real
contribution is a *sequential* algorithm, a *measured system*, or a *database* result is respected
and then rejected as out of scope.

## The naming trap, first

**PODC is not PODS.** PODS is the ACM Symposium on **Principles of Database Systems** (SIGMOD week);
its theory is query languages, dependencies, and database complexity. If your result is about data
management rather than distributed processes, agents, or memory, you want PODS, not PODC. One letter,
two communities — check before you submit.

## The routing question that matters most

PODC, **DISC**, and **SPAA** overlap heavily in scope and share much of a reviewer pool, so the
decisive question is rarely "is this distributed theory?" but **"which model, which cost measure, and
which calendar fit this result now?"** Use the finer signals below and the live deadlines to choose.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Provable guarantee in a distributed model (consensus, shared memory, LOCAL/CONGEST, self-stabilization, population protocols), ready now, PODC's Feb deadline is nearer | **PODC** | The ACM distributed-theory flagship; proofs-centric |
| Same distributed-theory flavor but DISC's fall cycle lands better, or the result is very European-community-facing | **DISC** | The EATCS distributed-theory flagship; LIPIcs proceedings; **shares** the Dijkstra Prize and Dissertation Award with PODC |
| Core is **parallel** algorithms/architectures, work-span/PRAM, shared-memory throughput, scheduling | **SPAA** | Parallelism is its named center; co-located with PODC 2026 but a distinct scope |
| Networks, mobile agents, self-stabilization with a specific community fit | **OPODIS / SIROCCO / SSS** | Focused distributed-theory venues; often a better match for niche models |
| The algorithm is **sequential** — the distribution is incidental | **STOC / FOCS / SODA** | Sequential theory flagships; no distributed model to reward |
| A **built system** with measurements and no analyzed guarantee | **ICDCS / DSN / OSDI / NSDI / SOSP** | Systems venues reward implementation and evaluation, not a proof |
| Blockchain/DeFi with a financial-mechanism or cryptographic-protocol core | **AFT / FC / CCS** | Financial-technology and security venues; PODC takes distributed-*ledger theory* but not applied crypto engineering |
| A result too long/deep for 10 pages, or a definitive journal statement | **JACM / Distributed Computing** | The journals PODC papers are invited to; some results are journal-first |

## Contribution shapes PODC rewards

- **A distributed algorithm with a complexity bound** — round, message, bit, or space complexity in
  a named model, against the best prior bound.
- **An impossibility result** — a proof that no algorithm in a model solves a problem (FLP-style
  arguments, valency, indistinguishability, covering).
- **A matching lower bound** — turning an algorithm into an *optimality* result, the venue's most
  prized shape (see the exemplars library).
- **A new model or paradigm** — defining a minimal model and characterizing its power (the population
  protocols lineage).
- **A shared-memory / concurrency result** — wait-free/lock-free constructions, consensus numbers,
  the complexity of concurrent objects.
- **Distributed-ledger / BFT theory** — consensus under Byzantine faults, agreement complexity,
  provable properties of blockchain protocols — *as theory*, not as a deployed system.

## The model-swap and re-label tests

Two quick tests sharpen a borderline verdict:

- **Model-swap / de-distribute test:** if you removed the distribution (ran it on one machine), would
  a result remain? If the whole contribution survives as a sequential algorithm, it is a STOC/SODA
  paper. PODC's value must live in the *distributed* difficulty (faults, asynchrony, locality,
  concurrency).
- **Re-label test:** could this be submitted to SPAA or a systems venue unchanged and read as native
  there? If its heart is parallel throughput, route to SPAA; if it is an implemented system measured
  on a cluster, route to a systems venue. PODC rewards the *proved guarantee*.

## Evidence maturity, theory-style

Fit is necessary but not sufficient. The same idea sits at different doors depending on how finished
the *proof* is. An algorithm with a plausible-but-unproved bound is a Brief Announcement or a
work-in-progress talk, not a regular paper; a construction with an upper bound but no lower bound is
publishable but stronger *with* the matching bound; a result too long for 10 pages of merits belongs
in a journal. Submitting a regular paper with a proof gap earns a fast rejection, because the proof
*is* the paper.

## Cheap reconnaissance before committing

```text
[Scope]    scan the last two PODC programs (dblp db/conf/podc, podc.org) for your model
           -> 3+ recent papers in your subarea = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority PODC/DISC/SPAA/JACM/Distributed Computing?
           -> majority STOC/FOCS or majority systems venues => reviewers read you as a visitor
[Calendar] compare the next PODC (Feb) deadline with DISC (spring), SPAA, and journal timelines
           -> route to the nearest honest fit rather than waiting a year for a marginal preference
```

## Decision procedure

```text
[Model] state it: network (message-passing/shared-memory), timing, faults, adversary, cost measure
[Contribution] algorithm+bound / impossibility / matching lower bound / new model / concurrency object
[De-distribute test] does the value survive removing distribution? no => STOC/SODA
[Sibling check] parallelism core -> SPAA; built system -> ICDCS/DSN/OSDI; database -> PODS; ledger-as-system -> AFT/FC
[PODC vs DISC] both fit? -> choose by calendar and community; the prize/award ecosystem is shared
[Verdict] PODC regular / PODC Brief Announcement / sibling venue / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is PODC, continue with `podc-workflow` for the calendar and `podc-writing-style` for the paper shape.
