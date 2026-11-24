---
name: mobisys-workflow
description: Use when planning a MobiSys project timeline backward from the single early-December paper deadline through registration, two-round review with an early-reject cut, the rebuttal, notification, artifact evaluation, camera-ready, and the June conference — with device-experiment lead time built in and the one-deadline-per-year risk made explicit.
---

# MobiSys Workflow

Use this as the project-management skill for a MobiSys submission. Replace every date with the
current official timetable and work backward from the one hard December cutoff on the
`mobisys<yy>.hotcrp.com/deadlines` page.

MobiSys is a conference, not a journal: no standing editor-in-chief. The rotating leadership
is the per-edition General Chairs and PC Chairs (MobiSys 2027: General Chairs VP Nguyen and Anh
Nguyen; PC Chairs Jun Han and Falko Dressler, read 2026-11-24). Committees rotate yearly —
re-check the current organizing-committee page rather than carrying a name forward. Papers
publish open access in the ACM DL: authors whose institutions are not in ACM Open pay an
**APC** ($500 ACM/SIG members, $750 non-members in 2027, the final year of ACM's subsidy) —
budget it alongside registration (at least one author at a non-student rate, in person).

## The MobiSys 2027 clock (re-verified 2026-11-24)

| Milestone | Date |
|---|---|
| Abstract registration | November 27, 2026, 23:59 AoE |
| Paper submission | December 4, 2026, 23:59 AoE |
| Early rejection | January 26, 2027 |
| Rebuttal | February 8–12, 2027 |
| Final decision | March 6, 2027 |
| Camera-ready | April 14, 2027 |
| Conference | June 21–25, 2027, Ho Chi Minh City, Vietnam |

## The one-deadline calendar

Unlike MobiCom and NSDI, which run two deadlines a year, **MobiSys runs a single paper
deadline in early December feeding the following June conference**. There is no second gate
this cycle to catch a slip. That single fact governs the whole plan: the device experiments
must be finished, not started, before December.

## Milestones

- Venue fit: confirm the contribution is a mobile/embedded *system* whose device behavior is
  the result (`mobisys-topic-selection`).
- Evidence lock: freeze the system design and finish the on-device measurement campaign —
  energy, latency, memory, thermal, and any deployment/user study.
- Abstract registration: register title, an abstract of at least 100 words, the full author
  list, and conflicts on HotCRP before the registration cutoff that precedes the paper upload.
- Paper deadline: upload the 12-page double-column PDF **with the author block** (review is
  single-blind since 2026) and the required HotCRP fields (ethics certification, Emerging
  Ideas checkbox if applicable).
- Round-1 outcome: early-reject notifications go out; survivors proceed to round 2.
- Round-2 reviews + rebuttal: read reviews, then draft a scope-limited rebuttal
  (`mobisys-author-response`).
- Notification: archive reviews, rebuttal, and decision; accepts are conditional.
- Acceptance: clear the anonymous shepherd (who may ask for more evaluation), then prepare the
  ACM camera-ready, artifact-evaluation submission, APC/registration, the pitch video (details
  to be announced), and the June in-person talk.

## Backward plan from the December deadline

| Weeks out (heuristic) | Mobile-systems milestone |
|---|---|
| 12+ | System built; measurement harness and power instrument working end to end |
| 8 | On-device runs complete on all target devices; energy/latency logged with provenance |
| 6 | Deployment or user study done if the claim is a service |
| 4 | Full draft sitting in the 12-page ACM double-column template |
| 3 | Internal mock review by a systems reader; break-condition experiment added |
| 2 | Author block, conflicts, LLM-text disclosure and ethics certification checked; artifact package smoke-tested |
| 1 | Numbers regenerated from logs so PDF and artifact cannot diverge |
| 0 | Registration then paper on HotCRP before the AoE cutoff |

These offsets are planning heuristics only — anchor each to the current official timetable,
never to a previous cycle's calendar.

## Failure modes by stage

- Starting device measurement in November forces single-device, single-run results that read
  as under-evaluated — the classic MobiSys evidence reject.
- Leaving format conversion to the final week surfaces overflow late; the 12-page
  double-column budget is tighter than a working draft once figures are placed.
- Skipping the mock review forfeits the only chance to hear "your energy boundary is
  undefined" from a colleague instead of a reviewer.
- Building the artifact after the paper deadline forfeits the ACM badges, which need a working
  script-first package the AEC can run on its own machines (`mobisys-artifact-evaluation`).

## Coordination notes

- Assign one named owner for the on-device measurement provenance and another for the
  submission metadata (author list, conflicts, declarations); shared ownership is how both
  slip — and the author list cannot change after the deadline.
- Archive the exact submitted PDF, supplement, and artifact commit, since rebuttal replies
  must quote them precisely and camera-ready must match the reviewed version.
- Because a miss costs a full year, decide the go/no-go on evidence completeness by the
  four-week mark, not on deadline night.

## Output format

```text
[Current stage] idea / building / measuring / writing / registration / submitted / rebuttal / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <device evidence / page budget / author list+conflicts / artifact / one-deadline slip>
[Owner map] <task -> person or role>
```
