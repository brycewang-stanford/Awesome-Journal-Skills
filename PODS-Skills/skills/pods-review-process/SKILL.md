---
name: pods-review-process
description: Use when reasoning about how an ACM PODS submission is evaluated, covering lightweight double-anonymous review, the multi-cycle-per-year calendar, the two reviewing rounds within a cycle, the 48-hour rebuttal, the accept/reject/revision decision with a shepherded revision, PACMMOD-track publication, and how PODS differs from SIGMOD's rounds and ICDT's process.
---

# PODS Review Process

Model the pipeline before interpreting any single review. PODS review is done by **database
theoreticians** who will read your proofs, and the process is **multi-cycle** with a **revision**
round: a paper is not simply accepted or rejected on the first read — a **revision** decision (minor
or major) with a shepherd is a first-class outcome. The most consequential mental shift for authors
arriving from a plain accept/reject conference is that the **revision** is a real, shepherded second
round inside the same cycle.

## Process model

- Submission and review run on **EasyChair** with **lightweight double-anonymity**: author identities
  are hidden from reviewers, self-citations are third-person, and a conflict-of-interest list is
  declared at submission.
- Each cycle has **two reviewing rounds** to accommodate revisions. Reviewers assess the **correctness
  and completeness of the proofs**, the significance and novelty of the result, the precision of the
  model, and the tightness of the bounds.
- Authors get a short **rebuttal** window (about 48 hours, a few thousand characters) to correct
  factual misreadings before decisions.
- First decisions are **accept / reject / revision**. A **revision** (minor or major) invites a revised
  version within a set window; a **shepherd** judges whether the revision is satisfactory, and only
  then is the paper accepted.
- Accepted papers publish in the **PACMMOD PODS track** and are invited for presentation at the PODS
  symposium.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | The result and proofs hold; at most cosmetic changes | Camera-ready + arXiv full version; do not reopen scope |
| Revision (minor) | A fixable gap: a clarified proof step, a stated assumption, a tightened bound | Implement precisely within the window; satisfy the shepherd |
| Revision (major) | A larger but plausibly closeable gap: a missing case, an unproven direction | Treat as a real second round; complete it or the shepherd declines |
| Reject | Structural: a wrong proof, an un-closable gap, or out-of-scope for a theory venue | Fix fully and route to a later cycle/ICDT/journal — no immediate resubmission |

The strategic reading: design the submission so its weakest point is **repairable in a revision** (a
proof step to clarify, an assumption to state, a case to add) rather than **structural** (a main
theorem that is false or unproven). The revision round rewards papers whose gaps are closeable.

## How PODS differs from its siblings

- **vs. SIGMOD/VLDB/ICDE:** those systems flagships judge measured performance; PODS judges proofs.
  Even co-located with SIGMOD, PODS shares neither the acceptance bar nor the evidence type — a
  benchmark cannot rescue a missing proof here.
- **vs. ICDT:** ICDT is PODS's sister theory venue in the EDBT/ICDT federation with an overlapping
  community; the reviewing cultures are close, but the calendars and proceedings differ. Do not assume
  a shared deadline or template.
- **vs. a once-a-year venue:** PODS's multiple cycles mean a reject is only a season from another
  chance — but the resubmission embargo (roughly a year for rejected work) means a premature
  submission can still cost more than one cycle.

## Who reads you

Expect theory reviewers who check the mathematics. They will read the key proofs, look in the appendix
for the deferred ones, and catch a circular lemma, an unjustified "it is easy to see," or a lower bound
that does not match the claimed upper bound. Because PODS spans logic, complexity, and algorithms, a
paper is matched to reviewers in its subarea — a hand-waved proof is caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission] topic tags + a precise abstract -> reviewer match           (large lever)
[Rebuttal]          correct factual misreadings and pointer errors in ~48 hours; not a place for new proofs
[Revision]          the strongest lever: close the identified gap, satisfy the shepherd, resubmit in the window
[After reject]      no appeal; fix fully, then a later cycle / ICDT / journal (mind the resubmission embargo)
```

The rebuttal moves a paper when it shows a reviewer misread a definition or missed an existing appendix
proof; it does not move a paper by arguing taste or promising a proof you have not written. In a
revision, an unaddressed required item is what turns the shepherded round into a reject.

## Reading a review packet

Weight reviews before answering. A review that engages your theorem statements and points to a specific
proof step read the paper closely and will re-check the revision — that reviewer or the shepherd is your
path to acceptance if the fix holds. A review that only discusses significance has left correctness to
the others; answer each reviewer on the axis they raised (correctness, tightness, novelty, modeling).

## Misreadings to avoid

- **Treating a revision as a guaranteed accept** — the shepherd's second read is real; complete the
  required items, do not do half.
- **Using the rebuttal to add new proofs** — reviewers cannot verify unwritten mathematics in 48 hours;
  reserve substantive fixes for the revision.
- **Assuming co-location with SIGMOD means a systems-friendly bar** — PODS judges proofs, full stop.
- **Projecting last cycle's calendar** — cycle count and dates are decided per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / revision / final / accepted
[Decision category] accept / revision (minor|major) / reject, with the criterion driving it
[Criterion map] each review point -> correctness | tightness | significance | modeling | clarity
[Leverage plan] the next-stage action that can actually change the outcome (rebuttal fix / revision item)
[Forbidden moves] identity leak / new unverifiable proof in the rebuttal / ignoring a required revision item
```
