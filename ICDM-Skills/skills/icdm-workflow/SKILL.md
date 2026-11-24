---
name: icdm-workflow
description: Use when planning an ICDM (IEEE International Conference on Data Mining) project timeline from venue fit through the abstract and full-paper deadlines, the long summer wait to the August notification, the no-rebuttal review, the possible short-paper acceptance branch, IEEE camera-ready, and in-person presentation on a single annual deadline.
---

# ICDM Workflow

Use this as the project-management skill for an ICDM submission. ICDM runs a **single
annual deadline**, so the plan is a one-shot sprint to June and then a long wait, not a
KDD-style cycle loop. Replace every date with the current edition's official timetable and
work backwards from the paper deadline.

ICDM is an IEEE conference, not a journal: there is no standing editor-in-chief and no
article-processing charge. The rotating analogue is the per-edition **General Chairs and
Program (PC) Co-Chairs**, appointed anew each year (2026 chairs 待核实 on the committee
page); the cost model is **registration**, and at least one author must present in person
for the paper to appear in the IEEE proceedings.

## Milestones (2026 anchors — verify live)

- Venue + track fit: confirm Research vs Applied vs Blue Sky (see `icdm-topic-selection`).
- Evidence lock: freeze the mining task, mechanism, baselines, ablations, and scaling runs.
- No abstract gate in 2026: title, abstract, authors and topics go in with the paper.
- Full-paper deadline (2026-06-06, AoE): upload the anonymized 10-page PDF (Research) and
  complete the reproducibility checklist in the submission system.
- The summer wait: reviews proceed triple-blind with **no rebuttal** (none in the 2026 calls);
  do not post or publicize a new preprint during review.
- Notification (2026-08-16): Accept (designated Regular or Short) / Reject.
- Camera-ready (2026-09-09; the Applied call says 2026-09-16): IEEE PDF eXpress and copyright,
  de-anonymization, in-person registration, and an e-poster (due 2026-10-12).
- Conference (Nov 12-15, Shenyang): present; the paper enters IEEE Xplore.

## Backward plan from the June paper deadline

| Weeks out (heuristic) | Data-mining-methods milestone |
|---|---|
| 8+ | Mechanism fixed; mining task and baselines chosen |
| 6 | Ablations designed to isolate the mechanism |
| 4 | Scalability runs complete, seeds logged |
| 3 | Full draft compiled in IEEE two-column, measured against the 10-page all-inclusive cap |
| 2 | Internal mock review by a data-mining-minded reader |
| 1 | Triple-blind sweep, anonymized artifact export, appendix trimmed inside the cap |
| 0 | Abstract, then full paper on the submission system before AoE |

These offsets are heuristics — anchor every one to the current official timetable, never a
prior edition's calendar.

## The two ICDM-specific branches

- **No-rebuttal posture.** Plan as if you will get no chance to reply after reviews. That
  means the submitted PDF and its cited anonymized repository must pre-answer the obvious
  reviewer questions. If the current edition *does* open a response window, treat it as a
  bonus, not the plan (see `icdm-author-response`).
- **Short-paper branch.** Acceptance may arrive designated "Short." In 2026 Short papers kept
  the ten-page limit, so no compression was forced; keep a light compression plan only as
  insurance against a cycle that shortens them (see `icdm-camera-ready`).

## Failure modes by stage

- Treating the appendix as free space and discovering at week 1 that references plus
  appendix push the PDF past 10 pages — a no-review reject born of planning, not science.
- Building the anonymized artifact after the deadline, under time pressure, is how a
  triple-blind identity leak ships.
- Assuming a rebuttal exists and leaving a known weakness "for the response" that never
  comes.
- Forgetting the in-person presentation requirement until camera-ready, when travel and
  registration logistics are hardest.

## Coordination notes

- Assign one owner for the triple-blind sweep and another for the 10-page arithmetic;
  shared ownership is how both slip.
- Archive the exact submitted PDF and anonymized repository; if a response window opens,
  replies must quote them precisely.
- Diarize the August notification date so the short-paper branch can start immediately.

## Output format

```text
[Current stage] fit / experiments / writing / abstract / submission / waiting / decision / camera-ready
[Track] Research / Applied / Blue Sky
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <10-page cap / anonymity / scale evidence / no-rebuttal exposure / presentation>
[Branch readiness] short-paper compression plan: ready / not ready
```
