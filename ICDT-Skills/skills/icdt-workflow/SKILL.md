---
name: icdt-workflow
description: Use when planning an ICDT (International Conference on Database Theory) campaign end to end, running the two-submission-cycle calendar backward from a chosen cycle deadline through abstract registration, the first-cycle revision round, LIPIcs camera-ready, and presentation at the co-located EDBT/ICDT event.
---

# ICDT Workflow

Plan the campaign backward from a chosen **cycle deadline**. ICDT's defining calendar feature is
**two submission cycles per year**, so the first planning act is not "when is the deadline" but
"which cycle, and does the Cycle-1 revision option help me?" Everything downstream — abstract
registration, the revision window, LIPIcs camera-ready, and the talk at the co-located EDBT/ICDT
event — hangs off that choice.

## The two-cycle calendar (verify live dates)

Using ICDT 2027 (Lille) as the concrete snapshot, all AoE:

```text
Cycle 1:  abstracts 3 Mar 2026 -> papers 10 Mar 2026 -> notification 1 Jun 2026 (Accept/Revise/Reject)
Cycle 2:  abstracts 3 Sep 2026 -> papers 10 Sep 2026 -> notification 1 Dec 2026 (Accept/Reject)
Event:    EDBT/ICDT 2027, Lille, France, 6-9 April 2027 (ICDT sessions 6-8 April per the CfP)
```

As of 2026-07-09, **Cycle 1 is decided and Cycle 2 (papers 10 Sep 2026) is the immediate live
target.** Reconfirm every date against the current databasetheory.org call before you commit — the
two cycles do not always both run, and the dates shift per edition.

## Choosing the cycle

| Situation | Target | Why |
|---|---|---|
| Proof is complete and polished now | Whichever cycle is nearer | No reason to wait; both publish in the same volume year |
| Main theorem holds but a case or bound may still move | **Cycle 1** | The revision option lets referees ask for the fix instead of rejecting |
| Result not yet fully proved | **Later cycle / next year** | A one-sided bound or a gap invites a reject; finish first |
| Rejected in Cycle 1 (not invited back) | **Not Cycle 2** | The cross-cycle rule blocks uninvited resubmission; reroute or wait |

## Backward plan from a paper deadline (D)

```text
D minus 8-10 weeks : freeze theorem statements; decide ICDT vs PODS (icdt-topic-selection)
D minus 6 weeks    : full proofs written; identify what goes in body vs the marked appendix
D minus 3 weeks    : draft in lipics-v2021; body within 15 pages excl. refs; appendix holds proofs
D minus 1 week     : register the abstract in the chosen cycle (abstract deadline is ~a week before D)
D minus 3 days     : anonymity sweep (icdt-submission); self-citations neutralized; metadata scrubbed
D                  : upload to Microsoft CMT; re-download and read cold
```

## After the deadline

```text
[Awaiting decision]  calibrate with icdt-review-process; prepare nothing you cannot support
[If Revise (Cycle 1)] treat the revision window as a deadline: close each named gap, document it,
                      resubmit within the cycle (icdt-author-response)
[If Accept]          LIPIcs camera-ready (icdt-camera-ready): lipics-v2021 final, CCS + keywords +
                      ORCID, complete proofs, DOI on DROPS; post/refresh the full version (arXiv)
[If Reject]          reroute per icdt-topic-selection (PODS / a journal); do not carry into Cycle 2
                      uninvited
```

## The revision window (Cycle 1)

A Cycle-1 "revise" is the highest-leverage moment in the calendar. Budget it like a submission:
list every point the referees raised, close the ones about correctness first (a missing case, an
unproved lemma), then the ones about clarity, and write a short account of what changed and where.
The same referees re-read; an unaddressed correctness point is what turns a revision into a reject.

## Presentation at EDBT/ICDT

- Accepted ICDT papers are presented at the **joint EDBT/ICDT event** — the same week and venue as
  the EDBT systems track. Expect a mixed audience; pitch the talk to the theory-literate but keep the
  data-management motivation legible to systems attendees.
- At least one author presents; plan travel around the April event window.
- Watch for co-located Test-of-Time and Best-Paper / Best-Newcomer announcements — the community
  norms your paper is measured against are visible in those talks.

## Reverify each cycle

- Which cycles run this edition and their exact AoE dates.
- The revision-window length and the exact cross-cycle resubmission wording.
- The event dates and city (EDBT/ICDT rotates: Tampere 2026, Lille 2027).
- The LIPIcs class revision and page limit for the camera-ready.

## Output format

```text
[Target] ICDT 20NN, Cycle 1 / Cycle 2, paper deadline <date, AoE>
[Cycle rationale] complete-now / revision-hedge / finish-first
[Backward plan] <milestones with dates back from D>
[Post-decision] awaiting / revising / camera-ready / rerouting
[Next skill] icdt-submission | icdt-author-response | icdt-camera-ready | icdt-topic-selection
```
