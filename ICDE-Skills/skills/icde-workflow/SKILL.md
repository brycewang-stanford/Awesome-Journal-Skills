---
name: icde-workflow
description: Use when planning an IEEE ICDE project timeline around the two-round-per-edition calendar, choosing between the June and November research deadlines, checking whether the edition offers a revise-and-resubmit window (ICDE 2027 does not), and backward-planning a data-engineering systems paper from CMT submission through review, camera-ready, and IEEE Xplore publication.
---

# ICDE Workflow

Use this as the project-management skill for an ICDE research submission. Replace every date
with the current edition's official timetable and plan backward from the round you target.

ICDE is a conference, not a journal-of-the-conference: it has no standing editor-in-chief and
no article-processing charge. Leadership rotates per edition (General and Program Chairs named
on each `icdeYYYY.github.io` site), the cost model is registration, and accepted papers publish
in **IEEE Xplore** — not in a PACMMOD- or PVLDB-style venue journal. Re-check the current
organization page rather than carrying a name forward.

## The two-round unit

Unlike SIGMOD's four quarterly PACMMOD rounds or PVLDB's twelve monthly deadlines, ICDE gives
you **two shots per edition** and no more. ICDE 2027's Round 1 paper deadline was June 11,
2026 and Round 2 closed November 11, 2026 (rebuttal January 8-15, notification February 10,
2027), both at 5:00 PM Pacific Time; as of 2026-11-24 no ICDE 2028 call exists, so the next
ICDE deadline is not yet known. Because a Round 1
reject cannot re-enter Round 2, the round choice is a real commitment, not a convenience.

## Milestones

- **Venue and round fit:** confirm the contribution is a data-management primitive and that the
  chosen round is reachable without rushing the evaluation.
- **Evidence lock:** freeze the mechanism, workloads, baselines, scale grid, and the claims map.
- **Paper deadline (CMT):** upload the IEEE-format PDF plus supplemental material; file all
  co-author conflicts.
- **Review release:** triage correctness, novelty, evaluation soundness, and reproducibility.
- **Rebuttal window:** about one week (ICDE 2027: August 8-15, 2026 / January 8-15, 2027);
  block it in the team calendar at submission time.
- **Revision window (only if the edition has one):** ICDE 2026 granted invited revisions a
  **4-week** window; ICDE 2027 has **no revisions** — decisions are Accept/Reject after the
  rebuttal.
- **Decision:** archive reviews, the revision, and the submitted versions.
- **Camera-ready + Xplore:** IEEE eCF/PDF-eXpress checks, copyright form, final artifact
  release, registration, and in-person presentation.

## Backward plan from the round paper deadline

| Weeks out (heuristic) | Systems-paper milestone |
|---|---|
| 10+ | System implemented; workloads and baselines chosen |
| 8 | Scale grid running; measurement harness logging seeds and variance |
| 6 | All main-result runs complete; crossover/cost analysis drafted |
| 4 | Full draft sitting in IEEE two-column format |
| 3 | Internal mock review by a builder who did not write the system |
| 2 | Supplement assembled: run_all.sh, run_small.sh, README, generators |
| 1 | CMT profiles + conflicts filed; page count and format sweep |
| 0 | PDF and supplement in CMT before the round cutoff |

These offsets are planning heuristics — anchor each to the current important-dates page, never
to a past edition's calendar.

## Revision-bandwidth reasoning

- Under the ICDE 2027 model there is no revision to absorb late fixes: the evidence must be
  complete at submission, and the only post-submission bandwidth needed is the one-week
  rebuttal. If a future edition restores Revise & Resubmit (as in 2026), the honest question
  becomes whether the team has **four weeks of free bandwidth** in that window.
- The two-round structure means a missed Round 1 pushes you to Round 2 of the **same** edition
  (five months later) but a Round 1 *reject* pushes you a whole **edition** back — price both
  outcomes before choosing.

## Failure modes by stage

- Treating the two rounds as interchangeable and burning Round 1 on an unfinished evaluation,
  losing the whole edition.
- Leaving IEEE format conversion to the final week, when two-column overflow surfaces late.
- Skipping the builder mock review — the one chance to hear "your baseline is untuned" from a
  colleague instead of a reviewer.
- Assuming a revision window exists for the current edition without confirming it.

## Output format

```text
[Current stage] idea / building / measuring / writing / submission / revision / accepted
[Target round] Round 1 or Round 2 (edition), with next official deadline + source
[Critical path] <three tasks that determine readiness>
[Revision reserve] <rebuttal week booked; R&R bandwidth only if the edition offers it>
[Risk register] <round-choice / format / evaluation / reproducibility / presentation>
[Owner map] <task -> person or role>
```
