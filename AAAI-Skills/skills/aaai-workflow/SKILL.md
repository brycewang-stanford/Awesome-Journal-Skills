---
name: aaai-workflow
description: Use when planning an AAAI project timeline from topic selection through abstract, OpenReview submission, two-phase review, rebuttal, decision, camera-ready, registration, presentation, and public artifact release.
---

# AAAI Workflow

Use this as the project-management skill for an AAAI submission. Replace all dates with the current
cycle's official timetable and work backwards from OpenReview cutoffs.

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

## Output format

```text
[Current stage] idea / experiments / writing / submission / Phase 1 / rebuttal / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page, anonymity, checklist, supplement, policy>
[Owner map] <task -> person or role>
```

