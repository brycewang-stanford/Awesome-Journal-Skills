---
name: sigmetrics-workflow
description: Use when planning an ACM SIGMETRICS project timeline across the three rolling deadlines (summer/fall/winter), from venue fit through abstract registration, submission, shepherding, the one-shot revision round, POMACS publication, and presentation, with backward-planning offsets for a performance-evaluation paper and honest handling of the rolling-deadline cadence and the 12-month resubmission bar.
---

# SIGMETRICS Workflow

Use this as the project-management skill for a SIGMETRICS submission. SIGMETRICS runs **three
rolling deadlines a year** (summer / fall / winter) into the **POMACS** journal, so the calendar is
a *choice among deadlines*, not a single annual scramble. Replace every date with the current
official timetable and work backwards from the **abstract-registration** cutoff, which precedes each
paper deadline by about a week.

SIGMETRICS has **rotating per-edition General and Program Chairs** (appointed by the SIGMETRICS
executive committee) rather than a standing conference editor-in-chief; POMACS is **open access**
with no APC, and at least one author presents each accepted paper. Re-check the current
organizing-committee page rather than carrying a name forward.

## The rolling-deadline advantage

Unlike a once-a-year venue, SIGMETRICS lets you aim at the **next** deadline that fits your
evidence. Two consequences:

- **Missing a deadline costs ~4 months, not a year** — the next rolling deadline is a quarter away.
  Do not rush a proof or a measurement campaign to hit summer if fall gives you a clean result.
- **Publication timing matters:** summer/fall acceptances appear in POMACS **before** the
  conference; a winter acceptance publishes in the following issue. Choose the deadline whose
  POMACS timing and presentation slot fit your goals.

## Milestones

- **Venue fit:** confirm SIGMETRICS over IMC/SIGCOMM/NSDI/a theory venue, and the correct **track**
  (`sigmetrics-topic-selection`).
- **Evidence lock:** freeze the model and assumptions, complete the proofs, and finish the
  simulation/measurement that validates them.
- **Abstract registration:** submit real title, abstract, authors, conflicts, and track by the
  earlier registration deadline.
- **Submission:** upload the anonymized acmsmall PDF and the artifact reference by the paper
  deadline (23:59 AoE).
- **Reviews:** triage each comment by criterion (rigor, proof correctness, assumption validity,
  evidence, novelty, reproducibility).
- **One-Shot Revision (if issued):** close the entire required-changes list and resubmit to one of
  the two subsequent deadlines — a single shot, re-read by the original reviewers.
- **Accept + shepherding:** incorporate the shepherd's required changes into the final POMACS
  version.
- **Publication + presentation:** POMACS camera-ready, artifact/badges if the cycle offers them,
  register, and present.

## Backward plan from a paper deadline

| Weeks out (heuristic) | Performance-evaluation milestone |
|---|---|
| 10+ | Model and assumptions fixed; main theorems stated; measurement/trace secured |
| 8 | Proofs complete and internally checked; simulator built with logged seeds |
| 6 | Analysis-vs-simulation agreement established; baselines chosen and tuned |
| 4 | Full draft in acmsmall; artifact (model, simulator, trace scripts) assembled and anonymized |
| 3 | Internal mock review by a performance-evaluation reader (check a proof case and an assumption) |
| 2 | Assumption-validity section hardened; related-work delta sharpened; 20-page budget met |
| 1 | Anonymity sweep on PDF and artifact; abstract registered |
| 0 | Paper + artifact reference on the correct per-deadline HotCRP site |

These offsets are planning heuristics only — anchor every one to the current call and the
per-deadline HotCRP `deadlines` page, never to a previous cycle.

## The 12-month bar and cycle-hopping

- A **reject** cannot be resubmitted to any SIGMETRICS deadline for **12 months** from the initial
  submission — a structural reject costs a full year at SIGMETRICS, so route a fundamentally
  reframed paper elsewhere meanwhile rather than idling.
- A **One-Shot Revision** is not a reject: it resubmits to a subsequent deadline within the rolling
  process. Budget the revision window to close the whole list in one shot.

## Failure modes by stage

- **A proof still has an open case at week 4** forces a rushed appendix nobody has checked — the
  classic rigor reject in the making.
- **An unvalidated assumption** (claiming M/G/1 without fitting the workload) invites the "does the
  model match reality?" objection that a One-Shot Revision then has to repair.
- **Leaving the simulator/trace scripts to the final week** is how a cluster path or a
  provenance string leaks identity under double-anonymity.
- **Rushing a One-Shot Revision into the nearer deadline** and leaving a listed item half-done turns
  a winnable single-shot into a reject.

## Coordination notes

- Assign one owner for the proofs/appendix and another for the simulator/measurement and the
  anonymity sweep; shared ownership is how both slip.
- Archive the exact submitted PDF, artifact, and (later) the required-changes list and response —
  the single-shot revision must close that list precisely.

## Output format

```text
[Current stage] idea / model+proof / evidence / registration / submitted / one-shot revision / accepted
[Chosen deadline] summer / fall / winter <cycle>, and its abstract + paper dates (source)
[Critical path] <three tasks that determine readiness>
[Risk register] <proof completeness / assumption validity / anonymity / reproducibility / page budget>
[Owner map] <task -> person or role>
```
