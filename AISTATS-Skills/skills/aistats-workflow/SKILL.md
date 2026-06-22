---
name: aistats-workflow
description: Use when planning an AISTATS project timeline from venue fit through abstract submission, full-paper upload, supplementary material, review release, author-reviewer discussion, decision, camera-ready, PMLR publication, registration, presentation, and artifact release, with backward-planning offsets for theory-plus-experiments papers.
---

# AISTATS Workflow

Use this as the project-management skill for an AISTATS submission. Replace all dates with
the current official timetable and work backwards from OpenReview cutoffs.

AISTATS is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chairs and Program Chairs (2026 General
Chairs: Emtiyaz Khan and Yingzhen Li; Program Chairs: Arno Solin and Aaditya Ramdas, verified
2026-06-22), and the cost model is registration fees, not APCs — PMLR proceedings are open-access
with no author fee. Conference organizers rotate yearly, so re-check the current CFP and organization
page rather than carrying a name forward.

## Milestones

- Venue fit: confirm the contribution is genuinely at the AI, ML, and statistics interface.
- Evidence lock: freeze theorem statements, assumptions, experiments, simulations,
  baselines, reproducibility checklist, and supplement contents.
- Abstract deadline: submit real title, abstract, authors, subject areas, and conflicts.
- Full-paper deadline: upload anonymous PDF and required OpenReview fields.
- Supplement deadline: upload anonymized appendix/code/data if current cycle allows or
  requires separate supplementary material.
- Review release: triage correctness, statistical validity, novelty, clarity, and
  reproducibility concerns.
- Discussion period: draft concise anonymous text-only clarifications; avoid forbidden links
  or unsupported new results.
- Decision: archive reviews, discussion, meta-review, decision, and submitted versions.
- Acceptance: prepare PMLR camera-ready files, registration, in-person presentation, and
  public artifact release.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Theory-plus-experiments milestone |
|---|---|
| 8+ | Theorems proved, assumption set frozen |
| 6 | Simulations designed against each theorem |
| 4 | Real-data runs complete, seeds logged |
| 3 | Full draft sitting in AISTATS two-column format |
| 2 | Internal mock review by a statistics-minded reader |
| 1 | Checklist pass, anonymity sweep, supplement assembly |
| 0 | Abstract then full paper on OpenReview; supplement by its own cutoff |

These offsets are planning heuristics only — anchor every one of them to the current
official timetable, never to a previous cycle's calendar.

## Failure modes by stage

- Theory still moving at week 3 forces last-minute theorem edits nobody has verified — the
  classic AISTATS correctness reject in the making.
- Leaving format conversion to the final week surfaces overflow late, because two-column math
  is far tighter than a one-column working draft.
- Skipping the mock review forfeits the only chance to hear "your experiments violate
  Assumption 2" from a friend instead of a reviewer.
- Building the supplement after the paper deadline under time pressure is how anonymity
  leaks ship.

## Coordination notes

- Assign one named owner for the reproducibility checklist and another for the anonymity
  sweep; shared ownership is how both slip.
- Archive the exact submitted PDF, supplement, and checklist, since discussion-phase replies
  must quote them precisely.

## Output format

```text
[Current stage] idea / experiments / writing / abstract / submission / supplement / discussion / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page/anonymity/statistical evidence/supplement/reproducibility/presentation>
[Owner map] <task -> person or role>
```
