---
name: aaai-workflow
description: Use when planning an AAAI project timeline from topic selection through abstract, OpenReview submission, two-phase review, rebuttal, decision, camera-ready, registration, presentation, and public artifact release.
---

# AAAI Workflow

Use this as the project-management skill for an AAAI submission. Replace all dates with the current
cycle's official timetable and work backwards from OpenReview cutoffs.

AAAI is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition Program Chairs (AAAI-26: Chad Jenkins and Matthew
Taylor, verified 2026-06-22), and the cost model is registration fees, not APCs — at least one author
must register at the in-person rate to present. Conference organizers rotate yearly, so re-check the
current CFP and conference-organizers page rather than carrying a name or contact forward.

## Milestones

- Venue fit: choose Main Track, AI for Social Impact, AI Alignment, or another AAAI program.
- Evidence lock: freeze contribution, baselines, ablations, checklist answers, and supplement.
- Abstract deadline: submit real metadata, title, abstract, authors, subject areas, and conflicts.
- Paper deadline: upload anonymous PDF, reproducibility checklist, supplement, and OpenReview fields.
- Phase 1 risk check: ensure the paper can be understood quickly and does not look checklist-thin.
- Review release: identify whether the paper is in Phase 2 and triage reviews, including AI review
  if present.
- Rebuttal: draft a compact, no-URL, no-new-results response using only submitted evidence.
- Decision: archive reviews, rebuttal, decision, and final submitted version.
- Acceptance: submit source files, copyright, camera-ready PDF, registration, presentation plan, and
  public artifacts.

## Operating rules

- Keep a single checklist for page limit, anonymity, supplement integrity, author limit, and
  multiple-submission policy.
- Run a fresh anonymity audit after every PDF or ZIP export.
- Verify ZIP files open and reproduce expected paths before submission.
- Do not leave core evidence to rebuttal.

## Backward-planning table

Because AAAI runs a two-phase review with hard OpenReview cutoffs and no second feedback round, the
timeline is unforgiving. Anchor each gate to the prior one and to the official date, not a guess.

| Gate | Depends on | Slip consequence |
| --- | --- | --- |
| Abstract deadline | title, authors, conflicts locked | cannot submit the paper |
| Paper deadline | anonymous PDF, checklist, supplement | summary reject or no entry |
| Phase-1 cut | clarity and checklist done early | no feedback, paper dies |
| Feedback round | submitted evidence only | wasted on new-results bans |
| Camera-ready | acceptance, copyright, registration | dropped from proceedings |

## Phase-1 readiness gate

Treat the Phase-1 cut as the real deadline, earlier than acceptance. Before the paper deadline, a
non-specialist colleague should be able to state your contribution, find the evidence, and confirm
the checklist matches the paper. If they cannot, the broad-AI reviewer will not either.

## Worked vignette

A team plans to "finish experiments in rebuttal." The workflow flags this as fatal: AAAI bars new
results at feedback and may cut the paper in Phase 1 before feedback exists. The critical path moves
to locking evidence and the checklist a week before the paper deadline, leaving the feedback window
only for clarifying already-submitted material.

## Output format

```text
[Current stage] idea / experiments / writing / submission / Phase 1 / rebuttal / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page, anonymity, checklist, supplement, policy>
[Owner map] <task -> person or role>
```

