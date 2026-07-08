---
name: vldb-author-response
description: Use when a PVLDB paper receives a revision verdict and the response package must be built, covering the one-shot revision rule, the three-month window, reading the reviewers' required-changes list, planning new experiments against the clock, and writing the change document that VLDB reviewers re-evaluate against.
---

# VLDB Author Response

Use this when PVLDB reviews arrive — typically around the 15th of the month
after your deadline — and the verdict is **revise**. PVLDB has no rebuttal
phase before decisions: the reviews and the outcome land together, so the
author-response genre at this venue *is* the revision package. You get exactly
one revision, and up to three months to deliver it.

## Read the verdict as a contract

A PVLDB revision request is written to be specific: reviewers state what the
revision must contain. Treat that list as the acceptance test.

- Extract every required item into a numbered ledger before anyone starts
  editing; ambiguous requirements get a clarifying interpretation written down,
  not ignored.
- Separate **required** changes from **suggested** ones. Required items decide
  the outcome; suggestions earn goodwill when cheap.
- Estimate honestly whether the heaviest requirement — usually a new experiment
  or a stronger baseline — fits inside three months on your hardware. If it
  cannot, decide now between a scoped-down response and a withdrawal, because a
  failed revision consumes the only attempt.

## Budgeting the three months

| Weeks | Activity |
|---|---|
| 1 | Ledger built, requirements interpreted, infeasible items escalated |
| 2-7 | New runs, added baselines, corrected analyses |
| 8-9 | Text integration; every change traceable to a ledger item |
| 10-11 | Change document drafted; internal re-review against the ledger |
| 12 | Buffer for rerun failures; submit early, not at the wire |

The same reviewers return. They remember what they asked for, and they check
the ledger items first — new prose that dodges a required experiment is the
canonical failed revision.

## Writing the change document

- Open with a one-paragraph summary of what changed and where.
- Then answer requirement by requirement: quote the reviewer's ask, state what
  was done, and point to the exact section, figure, or table in the revised PDF.
- Where results moved against you, say so plainly and interpret the movement.
  Reviewers at a systems venue respect a measured regression explained; they
  punish one discovered.
- Do not smuggle in an expanded contribution. The revision is re-reviewed
  against the original claims plus the required changes — a rewritten paper
  restarts skepticism instead of resolving it.

## Response skeleton

```text
Summary of revision (5-8 lines)

R1.1 [quoted requirement]
  Done: <change made>
  Where: <section / figure / table>
  Note: <result movement, if any>

R2.3 [quoted requirement]
  Done / Partially done because <honest constraint>
  Where: ...
```

## Judgment calls

- A requirement you believe is mistaken still gets an experiment or a careful
  argument with evidence — never a bare disagreement.
- If two reviewers conflict, satisfy both where possible; otherwise state the
  conflict explicitly and justify the path chosen.
- Nothing stops you asking the assigned meta-level contact (where the volume
  provides one) about genuinely uninterpretable requirements early — 待核实
  the current escalation channel on the live guidelines.

## Output format

```text
[Verdict] revise (one-shot) / clarification needed
[Requirement ledger] <numbered items, required vs. suggested>
[Feasibility] fits window / at risk (item, reason) / infeasible
[Heaviest item] <experiment or analysis, est. weeks>
[Change-document status] <drafted sections / gaps>
[Submit-by] <own target, ahead of the 3-month limit>
```
