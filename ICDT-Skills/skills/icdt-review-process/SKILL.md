---
name: icdt-review-process
description: Use when reasoning about how an ICDT (International Conference on Database Theory) submission is evaluated, covering the two-submission-cycle model, the first-cycle revision (Accept / Revise / Reject) decision, anonymous review since 2024, the cross-cycle resubmission restriction, proof-correctness scrutiny by a database-theory PC, and how ICDT's process differs from PODS and from the co-located EDBT systems track.
---

# ICDT Review Process

Model the pipeline before interpreting any single review. ICDT's process is built around **two
submission cycles per year** and a **first-cycle revision option**, and the reviewing bar is
**proof correctness**: the referees are database theorists who will check the argument, not just
weigh the idea. The most consequential mental shift for authors arriving from a systems venue is
that a wrong or incomplete proof is not a "revise" — it is often a reject, because the contribution
*is* the theorem.

## Process model

- Submission and review run on **Microsoft CMT** with **anonymous** review (regular track, since
  2024): the PC does not see author identities.
- Each cycle has an **abstract deadline** then a **paper deadline** about a week later; the PC bids
  and is assigned from the registered abstracts.
- **Cycle 1 decisions are Accept, Revise-and-resubmit, or Reject.** A "revise" is a genuine
  invitation to fix identified gaps and return within the cycle for a second read.
- **Cycle 2** reaches a final Accept/Reject. A paper **rejected in Cycle 1 cannot be resubmitted to
  Cycle 2 unless the reviewers explicitly invited it** — the cycles are not two independent lotteries.
- Accepted papers publish **open access in LIPIcs** (Schloss Dagstuhl), so camera-ready proof
  completeness and metadata matter as much as the verdict.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | The theorem holds and the advance is real; polish only | Camera-ready; finalize the full-version proofs; do not reopen scope |
| Revise-and-resubmit (Cycle 1) | A fixable gap: a case in a proof, a missing bound, an unclear model | Treat as a deadline: fix each identified point and document it in the revised version |
| Reject | Structural: a broken proof, a known result, a model with no consequence | Do not resubmit to Cycle 2 uninvited; repair deeply or reroute (PODS / a journal) |

The strategic reading: an ICDT referee distinguishes **a gap you can close** (a missing lemma, a
special case) from **a claim that is wrong** (the main theorem fails). Write so that any weakness a
referee finds is of the first kind — an argument you can complete in the revision — not the second.

## How ICDT differs from its siblings

- **vs. PODS:** PODS is the *other* database-theory flagship, but North-American-leaning, co-located
  with **SIGMOD**, and now published in ACM **PACMMOD**. ICDT is the European venue, co-located with
  **EDBT**, published **open access in LIPIcs**, and runs a **two-cycle calendar with a revision
  option** rather than PODS's ACM-journal framing. The scope overlaps heavily; the calendar,
  publisher, and revision mechanics do not. Never assume a shared deadline or template.
- **vs. EDBT (the co-located systems track):** EDBT reviews systems and experimental data-management
  work with reproducibility expectations; ICDT reviews theorems. Being in the same building and the
  same week does not mean the same reviewer culture — an ICDT referee wants a proof, not a benchmark.
- **vs. LICS / ICALP / STACS:** these EATCS-adjacent theory venues share ICDT's proof rigor but not
  its data-management framing; ICDT rewards a result whose *consequence for querying, constraints,
  or data* is clear, not theory for its own sake.

## Who reads you

Expect referees from your subarea of database theory — query languages, finite model theory,
complexity of query evaluation, consistent query answering, provenance, or data-integration theory.
They will **read the proofs**, look for the model of computation and the exact complexity class,
check whether upper and lower bounds match, and notice an unstated assumption that makes a theorem
easier than advertised. Vague "it can be shown that" statements are caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  precise abstract + subject areas -> the right referees   (largest lever)
[Cycle choice]       target Cycle 1 if the proof might still move (revision option)
[Revision round]     the strongest lever: close every identified gap and say where you did
[After reject]       no uninvited Cycle-2 carry; reroute to PODS or a journal (TODS/LMCS/TheoretiCS)
```

A revision succeeds when it **closes the specific gap the referees named** and documents the change;
it fails when it argues that the gap does not matter. Silent non-fixes — an identified missing case
left unaddressed — turn the second read into a reject.

## Misreadings to avoid

- **Treating "revise" as an accept** — the second read re-checks the proof; budget the revision
  window like a deadline.
- **Treating Cycle 2 as a retry lane** — the cross-cycle rule blocks uninvited resubmission of a
  Cycle-1 reject.
- **Assuming a systems-style rebuttal exists** — ICDT's mechanism is the *revision*, not a
  short rebuttal letter (confirm the current cycle's exact author-interaction rules; **待核实**).
- **Confusing ICDT with PODS process** — different publisher, calendar, and revision model.

## Output format

```text
[Process stage] pre-submission / awaiting Cycle-N decision / revising / final / accepted
[Decision category] accept / revise / reject, with the criterion (correctness | novelty | consequence)
[Referee map] each point -> proof gap | model unclear | known result | bound not tight | scope
[Leverage plan] the next-stage action (which gap to close) that can change the outcome
[Forbidden moves] uninvited Cycle-2 resubmission / identity leak / unproved claim left standing
```
