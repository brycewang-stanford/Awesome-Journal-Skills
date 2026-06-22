---
name: ijcai-workflow
description: Use when planning an IJCAI or IJCAI-ECAI project timeline from venue fit through abstract registration, full-paper upload, author information, PPI payment, summary-reject risk, author response, notification, camera-ready, in-person presentation, and artifact release.
---

# IJCAI Workflow

Use this as the project-management skill for an IJCAI submission. Replace all dates with the
current official timetable and work backwards from Chairing Tool cutoffs.

IJCAI is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition Conference Chair and Program Chair (IJCAI-ECAI
2026: Conference Chair Francesca Toni; Program Chair Diego Calvanese, verified 2026-06-22), and the
cost model is registration fees, not APCs. The Primary Paper Initiative fee below applies only to an
author's non-primary (extra) submissions and is a submission-volume disincentive, not a per-article
publication charge. Conference organizers rotate yearly, so re-check the current CFP and
conference-committee page rather than carrying a name forward.

## Milestones

- Venue fit: choose main track, a special track, Survey Track, or a different AI venue.
- Evidence lock: freeze contribution, experiments, proofs, datasets, reproducibility story,
  supplement, and resubmission package.
- Abstract deadline: register a real title, brief abstract, authors, contact details, and
  keywords. Placeholder abstracts are unsafe.
- Author-information deadline: ensure every coauthor has confirmed authorship, ORCID status,
  and required profile fields.
- Full-paper deadline: upload anonymous PDF, supplementary material, resubmission files, and
  Chairing Tool fields.
- Payment checkpoint: handle any non-primary paper fee by the current deadline.
- Phase 1: plan for summary-reject risk by making the contribution obvious within two reads.
- Response period: answer only pressing questions, factual errors, or unethical-review issues.
- Acceptance: submit camera-ready files, copyright/metadata, registration, presentation plan,
  and public artifact release.

## Critical-path coupling

IJCAI separates abstract registration from full-paper upload and freezes the author set at the
author-information deadline, so dependencies bite earlier than at venues with a single
deadline. Track what each milestone blocks.

| Milestone | Hard precondition | What it blocks if missed |
| --- | --- | --- |
| Abstract registration | Real title, abstract, authors, keywords | No paper slot exists; placeholder is unsafe |
| Author-information close | Every coauthor confirmed, ORCID/profile set | Author set locks; cannot add authors later |
| Full-paper upload | Anonymous PDF, supplement, resubmission file | All review-stage evidence is fixed here |
| PPI/payment checkpoint | Fee handled where applicable | Paper may be ineligible |
| Phase 1 | Contribution legible to a broad PC | Summary reject before any response |
| Camera-ready | Acceptance, registration, copyright | Publication and presentation blocked |

## Worked vignette: a planning team's backward plan

A four-author planning team targets the main track. Work backward from Chairing Tool cutoffs:
freeze the contribution and benchmark suite two weeks before full-paper upload; collect all
ORCID confirmations before the author-information close because no author can be added after;
register a real abstract early since the abstract deadline precedes the paper; and budget for
phase-1 summary-reject risk by having a non-specialist read the first page well before
submission, since the response stage may never arrive. Replace every date with the current
official timetable.

## Risk register and the venue-specific fix

- "Abstract slot never created." Register a real title and abstract by the abstract deadline,
  not a placeholder.
- "Coauthor confirmed late." Chase ORCID and confirmations before author-information close; the
  set locks afterward.
- "Counting on the rebuttal." Treat phase 1 as potentially terminal and make the contribution
  obvious within two reads.

## Output format

```text
[Current stage] idea / experiments / writing / abstract / submission / phase 1 / response / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page/anonymity/authors/PPI/resubmission/reproducibility/presentation>
[Owner map] <task -> person or role>
```
