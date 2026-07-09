---
name: sigcomm-workflow
description: Use when planning an ACM SIGCOMM project timeline around the single yearly deadline — venue fit, evidence lock, abstract registration and paper upload in February, the early-reject/rebuttal/one-shot-revision review pipeline, shepherd-run camera-ready, TAPS proceedings, artifact evaluation, and forward planning for the next edition.
---

# SIGCOMM Workflow

Use this as the project-management skill for a SIGCOMM campaign. The defining constraint is
one main-track deadline per year feeding one August conference: there is no fall gate, so the
plan is a year-long backward schedule from February, not a two-shot hedge. Replace every date
with the current official timetable.

SIGCOMM is a conference, not a journal: it has no standing editor-in-chief and no
article-processing charge. The rotating leadership is the per-edition General Chairs and
Program Committee Co-Chairs (the 2026 roster was not retrievable on 2026-07-09 — 待核实), and
the cost model is registration, not APCs; proceedings publish through ACM TAPS into the ACM
Digital Library. Chairs rotate yearly, so re-check the current organization page.

## Milestones

- **Venue fit and track**: confirm a networking-stack mechanism and pick research vs.
  experience.
- **Evidence lock**: freeze the testbed, traces, workloads, baselines, measurement
  methodology, and the tail metrics before writing hardens.
- **Abstract registration**: real title, authors, topics, conflicts on HotCRP.
- **Full-paper upload**: anonymous PDF, 12 single-spaced pre-reference pages, ACM template.
- **Review release**: triage across correctness, novelty, evaluation realism, and clarity.
- **Rebuttal**: for papers reaching the discussion phase, a concise anonymous reply.
- **Decision**: accept, one-shot revision, or reject (early or formal).
- **Revision** (if issued): resubmit ~a month later under a shepherd against the issue list.
- **Camera-ready**: shepherd sign-off, TAPS final PDF plus source, de-anonymization.
- **Artifact evaluation and presentation**: AEC badges, public release, August talk.

## Backward plan from the February paper deadline

| Weeks out (heuristic) | Systems/measurement milestone |
|---|---|
| 14+ | Mechanism designed; testbed or trace pipeline standing and repeatable |
| 10 | Core evaluation runs producing stable tails across repeated trials |
| 7 | Baselines that fight back implemented and tuned fairly |
| 5 | Full draft in ACM two-column format, figures counting against 12 pages |
| 3 | Internal mock review by a networking-minded reader; break-point experiment added |
| 2 | Reproducibility ledger and artifact skeleton assembled |
| 1 | Anonymity sweep, HotCRP fields, abstract registered |
| 0 | Full paper uploaded AoE; receipt re-read |

These offsets are planning heuristics — anchor each to the current official timetable, never
to a previous edition's calendar.

## The year has two halves, not one deadline

Because the deadline is annual, the calendar after submission matters as much as before it.
As of 2026-07-09 the SIGCOMM 2026 cycle is in its **live post-decision phase**: the February
deadline passed, decisions issued, and the work now is camera-ready finalization, shepherd
sign-off, artifact evaluation, and the August presentation — while the *next* edition's
February deadline is already the horizon for new work. Plan both halves: the run-up to the
single deadline, and the shepherd-to-proceedings tail that follows acceptance.

## Failure modes by stage

- Evidence still moving at week 5 forces last-minute metric changes nobody has re-run — the
  classic evaluation-realism reject in the making.
- Leaving ACM two-column conversion to the final week surfaces figure-driven overflow late,
  because figures count against the 12 pages.
- Skipping the mock review forfeits the only chance to hear "your baseline is a straw man"
  from a friend instead of a reviewer.
- Treating a one-shot revision as optional polish rather than a shepherd-graded contract is
  how a revision that dodged the issue list gets rejected.
- Deferring the artifact until after acceptance loses the reproducibility evidence that a
  clean rebuild would have surfaced.

## Coordination notes

- Assign one named owner for the reproducibility ledger and another for the anonymity sweep;
  shared ownership is how both slip.
- Archive the exact submitted PDF and every logged run, since rebuttal and revision replies
  must quote them precisely.

## Output format

```text
[Current stage] idea / evaluation / writing / abstract / submission / rebuttal / revision / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <format / anonymity / evaluation realism / reproducibility / shepherd>
[Owner map] <task -> person or role>
```
