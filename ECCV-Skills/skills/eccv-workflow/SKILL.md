---
name: eccv-workflow
description: Use when running an ECCV campaign end to end — the even-year calendar from February registration to the September conference, the retargeting triangle to CVPR and ICCV seen from the ECCV seat, where the 2026 cycle stands today, and backward planning a 2028 submission from the March deadline.
---

# ECCV Workflow

Use this as the project-management view of an ECCV effort. ECCV happens only
in **even years**, run by ECVA with chairs rotating per edition and no APC —
costs are registration and travel; proceedings are Springer LNCS with free
ECVA mirrors. The scarce resource is not money but *calendar*: each decision
about ECCV is implicitly a decision about CVPR and ICCV too.

## Where the 2026 cycle stands (as of 2026-07-08)

| Milestone | 2026 date | Status today |
|---|---|---|
| Registration / paper / supplement | Feb 26 / Mar 5 / Mar 12 | Closed |
| Reviews out → rebuttal due | May 2 → May 11 | Closed |
| Decisions | June 17 | Released |
| Camera-ready | June 30, AoE (extended) | Just passed |
| Open-access copies (ECVA/Springer) | ~4 weeks pre-conference | Expected ~mid-August |
| Conference, Malmö (Arena + Malmömässan) | Sept 8–13; workshops Sept 8–9 | Ahead |

Accepted teams are in the release-runway phase (`eccv-camera-ready`,
`eccv-artifact-evaluation`). Rejected teams are at the retargeting fork
below with June-dated reviews in hand.

## The retargeting triangle from the ECCV seat

The vision big three interleave so that from any ECCV event there is a next
move within roughly five months:

```text
ECCV decision (Jun, even yr) --reject--> CVPR deadline (Nov, same yr)
CVPR decision (Feb/Mar, odd yr) --reject--> ICCV deadline (Mar, odd yr)  [tight!]
ICCV decision (Jun/Jul, odd yr) --reject--> CVPR deadline (Nov, odd yr)
CVPR decision (Feb, even yr) --reject--> ECCV deadline (Mar, even yr)   [tight!]
```

The two "tight" hops are near-simultaneous decision/deadline pairs — teams
that anticipate them prepare the resubmission *before* the decision. Off the
triangle: BMVC (~spring deadline) and WACV (~summer) absorb solid work that
should not wait; ACCV shares the even-year autumn; IJCV/TPAMI take matured,
extended versions. For a paper rejected from ECCV 2026 in June, the default
path is a reviews-driven revision into CVPR's November 2026 deadline.

## Backward plan for ECCV 2028

All 2028 process details (host city, exact dates, page rules, platform) are
unannounced — 待核实 at eccv.ecva.net when posted. Plan against the stable
shape (registration late Feb, paper early Mar, conference early autumn):

- **Mar–Sep 2027**: project selection; note that ICCV 2027's March deadline
  competes for the same results — decide which venue gets the work early.
- **Oct–Dec 2027**: core method working; falsifier experiment done
  (`eccv-experiments`); CVPR 2028's November deadline is the explicit fork.
- **Jan 2028**: full experimental program; draft in the (new) author kit.
- **Feb 2028**: internal review, anonymity sweep, registration step done the
  week it opens.
- **Early Mar 2028**: paper freeze; supplement week for packaging only.

## Roles worth naming on an ECCV team

- **Deadline owner**: tracks the CET clock and the three-step chain.
- **Reviewer-duty owner**: tracks every co-author's assignments, because
  2026-style enforcement couples them to the paper's survival.
- **Release owner**: runs the June→September artifact runway.
- **Conference owner**: registration (a Springer publication precondition in
  2026), Schengen visas, poster/talk logistics for Malmö-like venues.

## Output format

```text
[Cycle position] pre-2028 planning / 2026 release-runway / 2026 retargeting
[Next hard date] <milestone, date, clock (CET vs AoE), source>
[Triangle decision] <hold for ECCV / route to CVPR-ICCV-BMVC-WACV / journal>
[Role map] <deadline / reviewer-duty / release / conference -> owner>
[Two-year risk] <what makes this work stale by the next even year>
```
