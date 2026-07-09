---
name: vis-workflow
description: Use when planning an IEEE VIS project timeline from area fit through the abstract and full-paper deadlines, the two-phase review, the conditional-accept second round, the IEEE TVCG camera-ready, the Graphics Replicability Stamp, and presentation, with backward-planning offsets for a visualization paper and honest handling of the annual cycle and the second-round revision window.
---

# VIS Workflow

Use this as the project-management skill for an IEEE VIS submission. Replace every date with the
current official timetable and work backwards from the **abstract** deadline — which precedes the
full-paper deadline and locks your author list. VIS publishes in **IEEE TVCG**, so plan for a likely
**conditional-accept second round** inside the review cycle, not just an accept/reject.

VIS is a conference whose full papers are journal articles: the **conference** has no standing
editor-in-chief, and the rotating analogue is the per-edition VIS Executive Committee, Overall Paper
Chairs, and the six Area Paper Chairs (verify the roster on the current organizing page — **待核实**
beyond named chairs). The cost model is conference registration; at least one author presents.

## Milestones

- **Area fit:** confirm VIS over a sibling venue and pick the **primary area** among the six
  (`vis-topic-selection`).
- **Evidence lock:** freeze the contribution type, the design rationale, the study/benchmark design,
  and the supplemental video plan.
- **Abstract:** submit real title, abstract, **final author list**, primary area, and keywords by
  the abstract deadline (VIS 2026: 21 March 2026).
- **Full paper:** upload the PDF (VIS 2026: 31 March 2026); title/abstract/PDF then freeze.
- **Supplemental:** finish and anonymize the video, code, and data in the one-week window (VIS 2026:
  7 April 2026).
- **First-round reviews:** triage each comment by criterion (novelty, impact, evidence, methodology,
  encoding rationale, reproducibility).
- **Conditional accept (if issued):** execute a revision plus a summary-of-changes, re-read by the
  same reviewers against the required changes.
- **Decision:** archive reviews, response, and every submitted version.
- **Acceptance:** prepare the TVCG camera-ready, complete Open Practices disclosures, pursue the
  Graphics Replicability Stamp on its own track, register, and present.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Visualization-paper milestone |
|---|---|
| 10+ | Contribution type fixed; data/task abstraction and design rationale settled |
| 8 | Technique/system implemented; study or benchmark designed; preregistration filed if used |
| 6 | Study run / benchmark complete; effect sizes and CIs computed; figures drafted |
| 4 | Full draft in the VGTC/TVCG template; supplemental video shot |
| 3 | Internal mock review by a visualization reader |
| 2 | Encoding rationale hardened, related-work delta sharpened, 9-page budget met |
| 1 | Abstract submitted with final authors; anonymity sweep on PDF + video (if double-blind) |
| 0 | Full PDF uploaded; supplemental finished and anonymized in its extra week |

These offsets are planning heuristics only — anchor every one to the current call, never to a
previous cycle's calendar.

## The annual-cycle reality

VIS runs a single annual full-paper cycle. Two planning consequences:

- **A conditional accept has a hard second-round window.** Under-budgeting the revision turns a
  winnable R&R into a reject; treat the required changes as a scored deadline, not a formality.
- **Missing the annual deadline costs roughly a year** at VIS; a sibling venue (EuroVis, PacificVis)
  or the **TVCG journal track** may have a nearer date — factor that into routing rather than idling.

## Failure modes by stage

- **Evidence still moving at week 4** forces last-minute studies nobody has audited — the classic
  methodology reject in the making.
- **Leaving the video to the final week** wastes VIS's extra supplemental week and ships an
  unpolished or identity-leaking video that reviewers judge harshly.
- **Skipping the mock review** forfeits the one chance to hear "your encoding is not justified" from
  a friend instead of a reviewer.
- **Treating a conditional accept as an accept** and under-budgeting the revision turns it into a
  rejection.
- **Adding an author after the abstract deadline** — not permitted; finalize authorship early.

## Coordination notes

- Assign one owner for the supplemental video/code and another for the anonymity sweep; shared
  ownership is how both slip.
- Archive the exact submitted PDF, supplemental, and (later) summary-of-changes — the second round
  must quote them precisely and, if double-blind, stay anonymous through phase one.

## Output format

```text
[Current stage] idea / evidence / writing / abstract / submitted / conditional accept / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / anonymity / evidence / encoding rationale / video / second round>
[Owner map] <task -> person or role>
```
