---
name: cav-workflow
description: Use when planning a CAV (Computer Aided Verification) project timeline from venue and category selection through submission, the two-stage review with early reject and rebuttal, artifact evaluation by the AEC, and the LNCS open-access camera-ready, with backward-planning offsets for a verification-tool paper and honest handling of the single-annual-deadline cycle.
---

# CAV Workflow

Use this as the project-management skill for a CAV submission. Replace every date with the current
official timetable and work backward from the AoE paper deadline. CAV publishes open access in
**Springer LNCS**, reviews in **two stages** (an early-reject filter, then a rebuttal), and runs
artifact evaluation in two rounds — **mandatory and in parallel with review for Tool Papers**,
optional after notification for everything else — plan for all three, not just accept/reject.

CAV is a conference with **no standing editor-in-chief**; the rotating leadership is the per-edition
Program Chairs and Steering Committee. For CAV 2027 the PC Chairs (also General Chairs) are
**Marieke Huisman and Joost-Pieter Katoen** (verified 2026-11-24), and the venue is **Amsterdam
(KIT), July 19-23, 2027**. Chairs rotate yearly; re-check the organizing-committee page rather
than carrying a name forward.

## Milestones

- **Venue + category fit:** confirm CAV over TACAS/FMCAD/VMCAI and pick the category (Regular /
  Tool / Application-Industrial-Case Study) (`cav-topic-selection`).
- **Evidence lock:** freeze the theorem/algorithm, the benchmark set (revision pinned), the baseline
  tools and versions, the resource limits, and the artifact contents.
- **Submission:** upload the LNCS-formatted PDF in the right category, anonymized if Regular, with
  the **artifact-intent declaration** set (CAV 2027: 20 Jan 2027 AoE; at most 5 submissions per
  author).
- **Stage-1 filter:** each paper gets two reviews; weak papers are rejected early (CAV 2027 early
  rejection notification: 4 Mar 2027).
- **Tool-paper artifact (mandatory):** register by 8 Mar 2027 and submit by 11 Mar 2027; smoke-test
  response 22-25 Mar 2027; the artifact outcome feeds the paper decision.
- **Rebuttal:** papers passing stage 1 get two more reviews and an author-response window (CAV 2027:
  5-8 Apr 2027).
- **Notification:** accept/reject (CAV 2027: 23 Apr 2027); archive all reviews and versions.
- **Artifact evaluation, other categories (optional):** register by 26 Apr 2027 and submit by
  3 May 2027 (artifact notification 28 May 2027), pursuing Available / Functional / Reusable badges.
- **Camera-ready:** due 18 May 2027 (20 pages for regular/tool, 12 for application papers); present
  at the conference (CAV 2027: 19-23 Jul 2027, Amsterdam).

## Backward plan from the submission deadline

| Weeks out (heuristic) | Verification-paper milestone |
|---|---|
| 10+ | Technique/algorithm fixed; the soundness/completeness statement drafted |
| 8 | Tool implemented and stable; benchmark set and baseline tools/versions chosen and pinned |
| 6 | Full evaluation run under fixed resource limits; per-instance data and logs archived |
| 4 | Full draft in `llncs`; proofs complete (in body or clearly-marked appendix); artifact assembled |
| 3 | Internal mock review by a verification-literate reader; differential/soundness cross-check done |
| 2 | Scope and limits sharpened; related-work delta tightened; page limit met |
| 1 | Anonymity sweep on PDF and artifact (Regular); artifact-intent decided; Tool Paper artifact draft runs on a clean machine |
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
- **Leaving anonymization to the final week** (Regular Papers) is how a solver name or a
  benchmark path leaks identity under double-blind review.
- **Treating stage 1 as a formality** and saving the strongest framing for the rebuttal forfeits the
  paper before the rebuttal exists.
- **Getting the artifact rule backwards by category** — in CAV 2027 it is **mandatory** for Tool
  Papers (the paper is accepted only if the artifact earns at least Functional, with artifact
  submission in March, before notification) and optional and non-conditional for every other
  category. A tool paper whose artifact is not ready in March is not ready to submit.

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
