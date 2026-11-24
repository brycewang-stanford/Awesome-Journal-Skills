---
name: eurosys-workflow
description: Use when planning a EuroSys campaign end to end — choosing between the spring and fall gates of an edition, backward-scheduling system building and evaluation from the abstract deadline, handling the notification-to-revision-to-resubmission pipeline, and landing camera-ready, artifacts, and April travel for the conference.
---

# EuroSys Workflow

Use this as the project plan around a EuroSys submission. The venue's calendar
is its most distinctive constraint: one April conference fed by two
submission gates roughly four months apart. Dates below are the EuroSys 2027
cycle as re-verified on 2026-11-24 (`2027.eurosys.org/cfp.html`); re-pull the live
CFP before committing the team to any of them.

## The 2027 board

| Milestone | Date | Status on 2026-11-24 |
|---|---|---|
| Spring abstracts / papers | May 7 / May 14, 2026 | Closed |
| Spring reviews / responses / notification | July 29 / July 31 / August 21, 2026 | Done |
| Spring artifacts / camera-ready | August 31 / September 25, 2026 | Done |
| Fall abstracts / papers | September 17 / 24, 2026 | Closed |
| Fall reviews / responses due | January 6 / January 8, 2027 | ~6 weeks away |
| Fall notification | January 29, 2027 | — |
| Fall artifacts / camera-ready | February 8 (to be confirmed) / March 5, 2027 | — |
| Conference, Rabat, Morocco | April 2027 (official page: April 19—22 and "April 19 to 23"; end date 待核实) | — |

So a team starting today has no open EuroSys 2027 gate: the next target is the
**EuroSys 2028 spring round**, whose call was not published on 2026-11-24 (the 2028
site did not serve a page). A team with a fall submission under review is in the
quiet zone — pre-draft the two-day response, and use the rest for artifact
preparation and boundary experiments, both of which pay off regardless of the
January outcome.

## Backward plan to a paper gate (template: the fall 2027 gate, Sep 24, 2026)

Shift these offsets onto the next gate once its date is published.

```text
T-10w  mid Jul  System feature-frozen for the paper's claims; eval matrix written
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
- **Revise-and-resubmit** → the list of concerns becomes the plan of record; the
  resubmission target is the following cycle's gate. Feasibility call within one
  week (see `eurosys-author-response`).
- **Reject** → the paper is ineligible for the immediately following cycle, so the
  same round next edition is the earliest legal EuroSys return. Decide between a genuine year of strengthening or retargeting a
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
- **Preprint and talk policy:** the 2027 CFP allows arXiv, talks and posts during
  review only under a substantially different title and system name — decide the
  public name before anything goes out.
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
