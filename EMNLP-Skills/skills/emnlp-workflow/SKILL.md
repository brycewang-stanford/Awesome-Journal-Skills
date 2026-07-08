---
name: emnlp-workflow
description: Use when planning an EMNLP project calendar end to end — choosing the ACL Rolling Review cycle that feeds the conference, backward-planning experiments and annotation to the ARR deadline, scheduling the author response window, deciding commit versus revise-and-resubmit, and mapping camera-ready and Budapest presentation logistics.
---

# EMNLP Workflow

Use this as the project-management skill for an EMNLP paper. The defining fact: EMNLP has
no direct paper deadline of its own. The clock that matters is the ARR cycle aligned with
the conference, and missing it usually means committing from an *earlier* cycle or waiting
for the next conference. All dates below are the 2026 configuration (checked 2026-07-08);
re-anchor every one against the live calendar.

## The 2026 spine

| Date (2026) | Event | Owner |
|---|---|---|
| May 25 | ARR May cycle submission deadline | ARR |
| May 27 | Author registration form (EoD AoE) | ARR |
| Jul 6 | Reviews due from reviewers | ARR |
| Jul 7-13 | Author response + author-reviewer discussion | ARR |
| Jul 30 | Meta-reviews released | ARR |
| Aug 2 | Commitment deadline for EMNLP | Conference |
| Aug 20 | Acceptance notification (Main / Findings / reject) | Conference |
| Sep 20 | Camera-ready | Conference |
| Oct 24-29 | EMNLP 2026, Budapest (hybrid) | Conference |

Parallel option: the Industry Track took direct OpenReview submissions until June 16,
2026 — a genuinely different pipeline (see `emnlp-topic-selection` for routing).

## Backward plan from the ARR deadline

NLP papers die on data and annotation lead times more often than on modeling. Working
back from a late-May deadline:

- **10+ weeks out** — task definition frozen; annotation guidelines drafted and piloted;
  if human evaluation is planned, the protocol and pay budget approved now.
- **8 weeks** — datasets licensed and downloaded; contamination check on every
  evaluation set you intend to use with pretrained or API models.
- **6 weeks** — main experimental grid running; baselines reproduced *first*, because a
  baseline you cannot reproduce invalidates the comparison you were about to run.
- **4 weeks** — error analysis begun on real outputs; this is content, not garnish, and
  it cannot be written the night before.
- **2 weeks** — full draft in the ACL template; internal read by someone outside the
  project hunting for unscoped claims.
- **1 week** — Responsible NLP checklist answered against the actual draft; anonymization
  sweep; citation-resolution pass.
- **Deadline week** — freeze, upload, calendar the author registration form.

## The commitment decision — the step other venues do not have

Between meta-review (Jul 30) and commitment (Aug 2) sits a real strategic choice with a
72-hour fuse in 2026:

- **Commit** when the meta-review is positive or mixed-positive: SACs read the reviews,
  scores, and your response, and can accept to Main or Findings.
- **Revise and resubmit** to a later ARR cycle when reviews identify repairable gaps —
  the paper returns to the same reviewers where possible, so superficial edits are
  visible. But a later cycle means a later conference: check which venue the next cycle
  feeds before choosing patience.
- **Withdraw and rework** when reviewers rejected the framing, not the execution;
  resubmission with the same reviewers cannot fix a framing they already dislike.

Draft the commit/revise decision tree *before* July 30. Three days is enough to execute
a decision, not to have the argument.

## Coordination structure

```text
Role map for a 4-author EMNLP submission
- Evidence owner: experiment grid, seeds, significance tests, error analysis
- Data owner: licenses, contamination checks, annotation pipeline, agreement stats
- Compliance owner: template, checklist, anonymization, citation resolution
- Response owner: drafts the July response, tracks each reviewer thread
(One person may hold two roles; no role may have zero owners.)
```

Archive the exact submitted PDF and checklist on deadline day — the July response must
quote them precisely, and the camera-ready diff will be audited against them.

## If May 25 slips

Because ARR runs continuously, missing the aligned cycle is a detour, not a year lost —
but the detour has geometry worth knowing in advance:

- A paper reviewed in an **earlier** cycle can typically still be committed to EMNLP by
  August 2 — ACL-family conferences have historically accepted commitments of papers
  reviewed in preceding cycles. Confirm the eligible-cycle window in the current call;
  if it holds, this is the rescue path for a project that is review-ready in spring.
- A paper that misses May 25 entirely waits for the **next** cycle, which feeds whatever
  conference it is aligned with — possibly not EMNLP. Check the alignment table on the
  ARR dates page before promising the group "we'll just catch the next one."
- The Industry Track's June 16 direct deadline is not an overflow valve for main-track
  papers; it reviews against deployment criteria and will bounce a mis-routed research
  paper.

## The week-of-deadline load profile

Plan for the fact that three distinct clocks tick in the same week: the paper PDF
(May 25), the author registration form (May 27), and any reciprocal-reviewing
qualification data the form demands. In the May 2026 cycle the reviewer pool ran at
roughly one AC per twelve submissions, and ARR expanded reciprocal assignments to
cope — meaning a multi-paper group could owe several reviews landing in June, exactly
when the group planned to rest. Put the reviewing obligation on the same calendar as
the submission, with a named owner per obligated author.

## Failure modes by phase

- Annotation started at week 6 delivers labels at week 1 with no time to measure
  agreement — the reviewers will ask for kappa you cannot compute.
- Skipping baseline reproduction until late converts "our method wins" into "our method
  wins against a baseline we misconfigured," the most common EMNLP rebuttal disaster.
- Treating the July 7-13 window as vacation: it is the only synchronous contact with
  reviewers in the entire pipeline.
- Forgetting that Findings acceptance may carry no presentation slot — decide before
  commitment whether Findings satisfies the project's goals (funding reports, degree
  requirements, visibility) or whether a revise-and-resubmit aims higher.

## Output format

```text
[Current phase] scoping / data / experiments / writing / submitted / response / commitment / accepted
[Next hard deadline] <date + owner (ARR vs conference) + source URL>
[Critical path] <three tasks gating the next deadline>
[Commitment posture] commit / revise-resubmit / undecided — with rationale
[Role gaps] <unowned roles from the role map>
```
