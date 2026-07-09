---
name: recsys-workflow
description: Use when planning an ACM RecSys project timeline from venue fit through abstract, full paper, the anonymous repository, rebuttal, decision, ACM camera-ready, registration, and presentation, with backward-planning offsets for an offline-evaluation recommender paper and per-track date awareness (Main, Reproducibility, Industry, Resource, R&P Notes).
---

# RecSys Workflow

Use this as the project-management skill for a RecSys submission. Replace all dates with the
current official timetable and work backwards from the submission-system cutoffs.

RecSys is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chairs and Program Chairs (2026 General
Chairs: Joseph A. Konstan, George Karypis, Gediminas Adomavicius; Program Chairs: Minmin Chen, Bart
Goethals, Martijn Willemsen — verified 2026-07-09), and the cost model is registration fees, with
proceedings in the ACM Digital Library. Chairs rotate yearly, so re-check the current committees
page rather than carrying a name forward.

## Per-track dates are not the same

The 2026 cycle ran several tracks on **different** timetables — do not assume the Main Track dates
apply to your track.

| Track (2026, AoE) | Abstract | Paper | Notification | Camera-ready |
|---|---|---|---|---|
| Main (long/short/PPF) | Apr 14 | Apr 21 | Jul 9 | 待核实 |
| Reproducibility | Apr 28 | May 5 | Jul 9 | Jul 27 |
| Industry | (site Mar 2) | May 21 | Jul 9 | Jul 27 |
| Resource / Dataset | Apr 28 | May 5 | Jul 9 | 待核实 |
| R&P Notes / Demos | — | Jul 15 | — | — |

The Main-Track rebuttal window was June 4-9, 2026. Anchor every one of these to the current CFP;
they are historical anchors, not permanent rules.

## Milestones

- Venue fit: confirm the contribution is genuinely a recommendation result (see
  `recsys-topic-selection`).
- Evidence lock: freeze datasets, the split protocol, tuned baselines, seeds, ablations, and the
  anonymous repository contents.
- Abstract deadline: submit real title, abstract, authors, and topic areas.
- Paper deadline: upload the anonymous PDF, the in-paper anonymous repository link, and required
  fields.
- Rebuttal: draft a concise anonymous narrative on the central evaluation objection.
- Decision: archive reviews, rebuttal, and the submitted version.
- Acceptance: prepare the ACM camera-ready, rights form, registration, presentation, and the
  public artifact release.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Offline-evaluation recommender milestone |
|---|---|
| 8+ | Datasets, versions, and split protocol frozen |
| 6 | Baselines tuned under an equal budget; grids logged |
| 4 | Ablations and the off-policy/simulator bridge complete, seeds logged |
| 3 | Full draft in the ACM two-column template |
| 2 | Internal mock review by a reproducibility-minded reader |
| 1 | Anonymity sweep; anonymous repository builds on a clean machine |
| 0 | Abstract then full paper on the submission system |

These offsets are planning heuristics only — anchor them to the current official timetable.

## Failure modes by stage

- Baselines still on default configs at week 3 forces an unfair-comparison reject in the making.
- Leaving template conversion to the final week surfaces two-column overflow late.
- Skipping the mock review forfeits the only chance to hear "this split leaks the future" from a
  friend instead of a reviewer.
- Building the anonymous repository under deadline pressure is how commit-author leaks ship.

## Coordination notes

- Assign one owner for the tuning-and-seeds protocol and another for the anonymity sweep.
- Archive the exact submitted PDF and repository state, since the rebuttal must quote them.

## Output format

```text
[Current stage] idea / experiments / writing / abstract / submission / rebuttal / accepted
[Track + next deadline] <track> - <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <baseline tuning / split / anonymity / repository / presentation>
[Owner map] <task -> person or role>
```
