---
name: cav-workflow
description: Use when planning a CAV (Computer Aided Verification) project timeline from venue and category selection through submission, the two-stage review with early reject and rebuttal, artifact evaluation by the AEC, and the LNCS open-access camera-ready, with backward-planning offsets for a verification-tool paper and honest handling of the single-annual-deadline cycle.
---

# CAV Workflow

Use this as the project-management skill for a CAV submission. Replace every date with the current
official timetable and work backward from the AoE paper deadline. CAV publishes open access in
**Springer LNCS**, reviews in **two stages** (an early-reject filter, then a rebuttal), and runs an
**optional** artifact evaluation after notification — plan for all three, not just accept/reject.

CAV is a conference with **no standing editor-in-chief**; the rotating leadership is the per-edition
Program Chairs and Steering Committee. For CAV 2026 the Program Chairs are **Anthony W. Lin, Eva
Darulova, and Philipp Rümmer** (verified 2026-07-09), and the venue is **Lisbon, part of FLoC
2026**. Chairs rotate yearly; re-check the organization page rather than carrying a name forward.

## Milestones

- **Venue + category fit:** confirm CAV over TACAS/FMCAD/VMCAI and pick the category (Regular /
  Tool / Application / Industrial) (`cav-topic-selection`).
- **Evidence lock:** freeze the theorem/algorithm, the benchmark set (revision pinned), the baseline
  tools and versions, the resource limits, and the artifact contents.
- **Submission:** upload the LNCS-formatted PDF in the right category, anonymized if Regular or
  Application, with the **artifact-intent declaration** set (CAV 2026: 28 Jan 2026 AoE).
- **Stage-1 filter:** each paper gets two reviews; weak papers are rejected early (tentative
  first-round outcome ~4 Mar 2026).
- **Rebuttal:** papers passing stage 1 get two more reviews and an author-response window (CAV 2026:
  30 Mar - 2 Apr 2026).
- **Notification:** accept/reject (CAV 2026: 17 Apr 2026); archive all reviews and versions.
- **Artifact evaluation (optional):** register and submit to the AEC on its own deadline (CAV 2026
  artifact registration: 22 Apr 2026), pursuing Available / Functional / Reusable badges.
- **Camera-ready:** prepare the LNCS open-access final version and complete Springer metadata and
  rights; present at the conference (CAV 2026: 26-29 Jul 2026, Lisbon / FLoC).

## Backward plan from the submission deadline

| Weeks out (heuristic) | Verification-paper milestone |
|---|---|
| 10+ | Technique/algorithm fixed; the soundness/completeness statement drafted |
| 8 | Tool implemented and stable; benchmark set and baseline tools/versions chosen and pinned |
| 6 | Full evaluation run under fixed resource limits; per-instance data and logs archived |
| 4 | Full draft in `llncs`; proofs complete (in body or clearly-marked appendix); artifact assembled |
| 3 | Internal mock review by a verification-literate reader; differential/soundness cross-check done |
| 2 | Scope and limits sharpened; related-work delta tightened; page limit met |
| 1 | Anonymity sweep on PDF and artifact (Regular/Application); artifact-intent decided |
| 0 | Upload in the correct category via the live portal; re-download to confirm |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle's calendar.

## The two-stage cycle: plan for the early reject

CAV's stage-1 filter means a paper can be **rejected before the rebuttal ever happens**. Two
planning consequences:

- **The first two reviews must be able to defend the paper on their own.** A contribution that only
  becomes convincing after the rebuttal may never reach stage 2. Make the soundness and the headline
  benchmark result legible in the first read.
- **Missing the annual deadline costs roughly a year at CAV.** A sibling flagship (TACAS in spring,
  FMCAD, VMCAI) may have a nearer date — factor that into routing rather than idling
  (`cav-topic-selection`).

## Failure modes by stage

- **Tool still unstable at week 6** forces a rushed evaluation nobody audited — the classic
  reproducibility/soundness doubt in the making.
- **Benchmarks or baselines unpinned** means the comparison cannot be reproduced and the reviewer
  discounts the numbers.
- **Leaving anonymization to the final week** (Regular/Application) is how a solver name or a
  benchmark path leaks identity under double-blind review.
- **Treating stage 1 as a formality** and saving the strongest framing for the rebuttal forfeits the
  paper before the rebuttal exists.
- **Assuming artifact evaluation is required** — it is optional and non-conditional at CAV; plan it,
  but do not block the camera-ready on it.

## Coordination notes

- Assign one owner for the artifact (benchmarks, versions, seeds, resource limits) and another for
  the anonymity sweep; shared ownership is how both slip.
- Archive the exact submitted PDF, the artifact, and (later) the rebuttal — a stage-2 review and any
  camera-ready must quote them precisely.

## Output format

```text
[Current stage] idea / evidence / writing / submitted / stage-1 / rebuttal / accepted / artifact
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <category / page limit / anonymity / benchmarks+baselines / soundness / artifact>
[Owner map] <task -> person or role>
```
