---
name: wacv-workflow
description: Use when planning a WACV campaign calendar across the two-round model, from track and round choice through the Round 1 submission, rebuttal, and Accept/Revise-and-Resubmit/Reject decision, into the Round 2 revision and decision, camera-ready, and the winter conference — with the branch points that a single-deadline plan misses.
---

# WACV Workflow

Use this to run a WACV campaign end to end. The defining feature is that WACV has **two
rounds with a revision path between them**, so the calendar is a branching tree, not a
single deadline. Dates below are the reported WACV 2027 timetable read on 2026-07-09 (via
search rendering — reconfirm on the live Dates page); the structure is stable, the exact
dates are not.

## The branching calendar

```text
Track + round decision  ──► Round 1 paper deadline (reported Jun 26, 2026)
                              │
                              ├─ R1 reviews (reported due Jul 24) ─► optional 1-page rebuttal
                              │
                              └─ R1 decision (reported Aug 7)
                                   ├─ Accept  ──────────────► camera-ready
                                   ├─ Reject  ──────────────► re-target / rebuild
                                   └─ Revise & Resubmit ─► revise + change summary
                                                                │
                                        Round 2 deadline (reported Aug 28) ◄─ new R2 papers also enter here
                                                                │
                                        R2 reviews (reported due Sep 25) ─ (no rebuttal)
                                                                │
                                        R2 decision (reported Oct 9) ─► Accept / Reject
                                                                │
                                        registration (reported Nov 2) ─► winter conference (Jan 2027, 待核实)
```

## Phase-by-phase

| Phase | Do this | Skill |
|---|---|---|
| Scope | Decide WACV vs sibling, Applications vs Algorithms, and R1 vs R2 | `wacv-topic-selection` |
| Draft | Write the first page for the chosen track and the two-round reviewer | `wacv-writing-style` |
| Evidence | Build matched-baseline, constraint-aware experiments with uncertainty | `wacv-experiments`, `wacv-reproducibility` |
| Submit R1 | Audit anonymity, profiles, page cap, track field | `wacv-submission`, `wacv-supplementary` |
| R1 reviews | Draft the optional one-page rebuttal, AC-first | `wacv-author-response`, `wacv-review-process` |
| R&R lap | Execute the revision as a spec; write the change summary; sync the artifact | `wacv-author-response`, `wacv-artifact-evaluation` |
| Camera-ready | De-anonymize, finalize for CVF open access + IEEE Xplore | `wacv-camera-ready` |
| Present | Prepare the winter conference talk/poster | `wacv-camera-ready` |

## Branch points a single-deadline plan misses

- **Round choice is a scheduling decision, not just a deadline.** A borderline paper
  belongs in Round 1 (rebuttal + Revise-and-Resubmit net); a polished one can go to Round 2.
  Deciding this late forfeits the safety net.
- **The Revise-and-Resubmit lap is the main event, not a detour.** Most WACV papers pass
  through it; budget real engineering time for the revision between the R1 decision and the
  R2 deadline, because Round 2 has no rebuttal to compensate for a rushed revision.
- **Two OpenReview groups.** Round 1 and Round 2 are distinct groups; do not assume a single
  submission carries over automatically — follow the current instructions for resubmitting
  a Revise-and-Resubmit paper.

## A worked mini-plan (borderline applications paper)

```text
T-3 wk: freeze track = Applications; target Round 1 for the R&R net
T-2 wk: matched-budget baselines re-run; uncertainty over seeds/sessions locked
T-1 wk: anonymity + profile + page-cap audit (wacv-submission)
  R1 deadline: submit
+reviews: one-page rebuttal fixes the top factual objection
  R1 = Revise & Resubmit: turn the three reviews into a change list; execute; write summary
  R2 deadline: resubmit revised paper + change summary
  R2 = Accept: camera-ready; register by the deadline; prep winter poster
```

## Reverify each cycle

- Both round deadlines, the review/decision dates, and the registration deadline.
- Whether the two-round model and the three R1 outcomes still hold.
- The camera-ready deadline and the winter conference dates/location (2027 dates 待核实).

## Output format

```text
[Current phase] scope / draft / R1 submit / R1 reviews / R&R / R2 / camera-ready / present
[Round + track] R1|R2 · Applications|Algorithms
[Next hard date] <deadline> — <what it gates>
[Branch risk] <the decision that, if made late, forfeits the R&R net>
[Next skill] <which WACV skill to open now>
```
