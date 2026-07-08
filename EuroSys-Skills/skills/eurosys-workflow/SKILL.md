---
name: eurosys-workflow
description: Use when planning a EuroSys campaign end to end — choosing between the spring and fall gates of an edition, backward-scheduling system building and evaluation from the abstract deadline, handling the notification-to-revision-to-resubmission pipeline, and landing camera-ready, artifacts, and April travel for the conference.
---

# EuroSys Workflow

Use this as the project plan around a EuroSys submission. The venue's calendar
is its most distinctive constraint: one April conference fed by two
submission gates roughly four months apart. Dates below are the EuroSys 2027
cycle as rendered on 2026-07-08 (`2027.eurosys.org/cfp.html`); re-pull the live
CFP before committing the team to any of them.

## The 2027 board

| Milestone | Date | Status on 2026-07-08 |
|---|---|---|
| Spring abstracts / papers | May 7 / May 14, 2026 | Closed |
| Spring notification | August 21, 2026 | ~6 weeks away |
| Fall abstracts / papers | September 17 / 24, 2026 | ~10 / 11 weeks away |
| Fall notification | January 29, 2027 | — |
| Camera-ready (both cohorts) | ~March 5, 2027 (third-party, 待核实) | — |
| Conference, Rabat, Morocco | April 19–23/24, 2027 (end date 待核实) | — |

So a team starting today has one live target: the fall gate. A team with a
spring submission under review is in the quiet zone — the right use of that
zone is artifact preparation and boundary experiments, both of which pay off
regardless of the August outcome.

## Backward plan to the fall paper gate (Sep 24, 2026)

```text
T-10w  now      System feature-frozen for the paper's claims; eval matrix written
T-8w   late Jul Decomposition + cost experiments running nightly; plots automated
T-6w   mid Aug  Full draft exists in acmart[sigplan] review mode; internal read #1
T-4w   late Aug Boundary/worst-case runs done; related-work sweep incl. dblp pass
T-3w   early Sep External mock review by a systems colleague outside the project
T-2w   Sep 10   Claims-to-evidence audit; every number has provenance
T-1w   Sep 17   ABSTRACT GATE — title/abstract/authors/topics/conflicts final
T-0    Sep 24   Paper gate — identity sweep on the final PDF, upload with margin
```

The two-gate structure is a gift: the abstract week is for polishing, and the
title and abstract registered at T-1w determine which reviewers bid — write
them for bidding, not as placeholders.

## Branching after notification

- **Accept** → camera-ready lane (ACM forms, final build) plus the sysartifacts
  artifact lane in parallel; they contend for the same people, so name owners.
- **One-shot revision** → the condition list becomes the plan of record; the
  resubmission target is the next round's gate. Feasibility call within one
  week (see `eurosys-author-response`).
- **Reject** → the same round next edition is the earliest legal EuroSys
  return. Decide between a genuine year of strengthening or retargeting a
  sibling venue whose next deadline fits the work's maturity
  (`eurosys-topic-selection` has the routing table).

## Standing risks and their owners

| Risk | Early symptom | Owner |
|---|---|---|
| Eval starts too late | No automated plots by T-8w | Experiments lead |
| Baseline dispute | Tuning provenance undocumented | Whoever runs baselines |
| Anonymity leak | Repo/PDF never swept | Submission owner |
| Revision-condition overrun | No feasibility call in week one | Project lead |
| Travel/visa for Rabat | Unchecked entry requirements post-accept | Presenting author |

## Using the quiet zones

The two-gate calendar creates long author-side silences (submission to
notification is ~14 weeks). Teams that treat them as vacations pay later:

- **Artifact runway:** build the claims map and environment contract now;
  AE and camera-ready will collide with each other after notification.
- **Boundary experiments:** the worst-case runs cut on deadline week are
  exactly what a revision condition list will demand — run them anyway.
- **Preprint and talk policy:** decide, against the round's anonymity
  wording (待核实), what can be presented publicly while under review.
- **Next-gate insurance:** keep the evaluation harness runnable; if the
  outcome is a revision, the conditions arrive with a four-month fuse.

## Coordination notes for multi-author teams

- One person owns the HotCRP record (fields, conflicts, uploads); shared
  ownership of forms produces last-minute permission surprises.
- The evaluation lead and the writing lead exchange the claims-to-evidence
  map weekly from T-6w; prose drifting ahead of data is how overclaiming
  enters a draft innocently.
- Book the mock reviewer at T-4w for a T-3w read; systems colleagues who
  can simulate a EuroSys review are scarce in September.

## Two-gate portfolio thinking

Groups with multiple projects should stagger them across the two gates rather
than crowding the fall: a spring submission gets its decision in August with
time to revise into the fall, while a fall submission's revision path crosses
into the *next* edition. Maturity at gate time — not preference for a season —
should pick the gate.

## Output format

```text
[Live target] <gate and days remaining>
[Stage now] building / evaluating / drafting / submitted / revising / accepted
[Backward-plan health] <milestones behind or on track>
[Post-notification branch] <accept / revision / reject plan sketch>
[Owners] <risk -> named person>
```
