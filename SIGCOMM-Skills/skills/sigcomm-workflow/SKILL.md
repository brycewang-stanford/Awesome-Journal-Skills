---
name: sigcomm-workflow
description: Use when planning an ACM SIGCOMM project timeline around the single yearly deadline — venue fit, evidence lock, the single February paper deadline (February 2, 2027 for SIGCOMM 2027), collaborative reviewing with no rebuttal, the conference/CCR/reject decision, shepherd-run camera-ready, video and in-person presentation, TAPS proceedings, artifact evaluation, and forward planning for the next edition.
---

# SIGCOMM Workflow

Use this as the project-management skill for a SIGCOMM campaign. The defining constraint is
one main-track deadline per year feeding one August conference: there is no fall gate, so the
plan is a year-long backward schedule from February, not a two-shot hedge. Replace every date
with the current official timetable.

SIGCOMM is a conference, not a journal: it has no standing editor-in-chief. The rotating leadership is the per-edition General Chairs and
Program Chairs (SIGCOMM 2027: General Chairs Kanchana Kanchanasut and Jim Kurose; Program
Chairs Ranjita Bhagwan, Nate Foster, Aurojit Panda and Scott Shenker, checked 2026-11-24), and
the cost model is registration; proceedings publish through ACM TAPS into the ACM Digital
Library. The SIGCOMM 2027 pages state no APC, but ACM proceedings are now fully open access and
ACM charges an APC to authors outside ACM Open institutions (2027 subsidized rates of $500 for
ACM/SIG members and $750 for non-members, as the SIGMOBILE MobiCom 2027 CFP states them) —
check whether your institution is in ACM Open (待核实 for SIGCOMM specifically). Chairs rotate yearly, so re-check the current organization page.

## Milestones

- **Venue fit and track**: confirm a networking-stack mechanism and pick research vs.
  experience.
- **Evidence lock**: freeze the testbed, traces, workloads, baselines, measurement
  methodology, and the tail metrics before writing hardens.
- **HotCRP record**: title, authors with ORCIDs, topics, track, ethics description,
  conflicts, and a named reciprocal reviewer (check the HotCRP clock for any registration step).
- **Paper upload**: anonymous PDF, 12 single-spaced pre-reference pages, 200-word abstract,
  ACM template — SIGCOMM 2027 deadline **February 2, 2027** (hard, no extensions).
- **Collaborative review**: no author action; there is **no rebuttal and no one-shot revision**
  in 2027.
- **Decision**: accepted into the conference (with a shepherd), accepted into CCR (may be
  declined), or rejected; one consensus review explains it.
- **Camera-ready**: shepherd sign-off, TAPS final PDF plus source, de-anonymization; official
  publication date **July 18th, 2027**.
- **Artifact evaluation and presentation**: AEC badges, public release, a video for every
  paper, in-person discussion-session presentation (plus a plenary talk for a subset), August
  8-12, 2027 in Bangkok.

## Backward plan from the February paper deadline

| Weeks out (heuristic) | Systems/measurement milestone |
|---|---|
| 14+ | Mechanism designed; testbed or trace pipeline standing and repeatable |
| 10 | Core evaluation runs producing stable tails across repeated trials |
| 7 | Baselines that fight back implemented and tuned fairly |
| 5 | Full draft in ACM two-column format, figures counting against 12 pages |
| 3 | Internal mock review by a networking-minded reader; break-point experiment added |
| 2 | Reproducibility ledger and artifact skeleton assembled |
| 1 | Anonymity sweep, HotCRP fields (ORCIDs, reciprocal reviewer, ethics text) complete |
| 0 | Full paper uploaded AoE; receipt re-read |

These offsets are planning heuristics — anchor each to the current official timetable, never
to a previous edition's calendar.

## The year has two halves, not one deadline

Because the deadline is annual, the calendar after submission matters as much as before it.
As of 2026-11-24 SIGCOMM 2026 (Denver, August 2026) has met and **SIGCOMM 2027** is the live
cycle: CFP posted October 19, 2026, one paper deadline **February 2, 2027**, conference
**August 8-12, 2027, Bangkok**. Plan both halves: the run-up to the single deadline, and the
shepherd-to-proceedings tail (camera-ready, video, artifact evaluation, travel) that follows
acceptance. Because there is no rebuttal in 2027, the run-up carries all of the persuasion.

## Failure modes by stage

- Evidence still moving at week 5 forces last-minute metric changes nobody has re-run — the
  classic evaluation-realism reject in the making.
- Leaving ACM two-column conversion to the final week surfaces figure-driven overflow late,
  because figures count against the 12 pages.
- Skipping the mock review forfeits the only chance to hear "your baseline is a straw man"
  from a friend instead of a reviewer.
- Counting on a rebuttal to fix a misunderstanding: SIGCOMM 2027 has none, so an objection
  the paper does not pre-empt stands. (In the 2026 model, treating a one-shot revision as
  optional polish was the equivalent failure.)
- Writing only for subarea experts: the 2027 general-accessibility criterion lets the PC
  reject a paper whose motivation a networking generalist cannot follow.
- Deferring the artifact until after acceptance loses the reproducibility evidence that a
  clean rebuild would have surfaced.

## Coordination notes

- Assign one named owner for the reproducibility ledger and another for the anonymity sweep;
  shared ownership is how both slip.
- Archive the exact submitted PDF and every logged run, since the shepherd revision, the CCR
  decision and any resubmission elsewhere must quote them precisely.

## Output format

```text
[Current stage] idea / evaluation / writing / HotCRP record / submission / under review / CCR choice / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <format / anonymity / evaluation realism / reproducibility / shepherd>
[Owner map] <task -> person or role>
```
