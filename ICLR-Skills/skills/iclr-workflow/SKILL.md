---
name: iclr-workflow
description: Use when planning an ICLR project timeline from topic selection through OpenReview submission, discussion, revision, decision, camera-ready, poster, video, and public artifact release.
---

# ICLR Workflow

Use this as the project-management skill for an ICLR submission. Always replace dates with the
current cycle's official deadlines and work backwards from OpenReview cutoffs.

## Milestones

- Fit decision: confirm the paper has a learning-representation contribution and a credible ICLR
  audience.
- Evidence lock: freeze the main claim, core baselines, ablations, and reproducibility path.
- Abstract deadline: submit a real abstract and verify author list, conflicts, subject areas, and
  OpenReview profiles.
- Paper deadline: upload anonymized PDF, supplement, code/data package, disclosures, and required
  fields.
- Review release: triage reviewer concerns and assign owners for evidence, wording, and revision.
- Discussion: respond, upload allowed revisions, maintain a concise changelog, and escalate only
  through official channels.
- Decision: archive reviews, meta-review, author discussion, and final submitted version.
- Acceptance: complete camera-ready, poster, slides, video, project page, public artifacts, and
  registration.

## Operating rules

- Maintain one source-of-truth checklist for OpenReview fields and file names.
- Run an anonymity audit after every PDF, supplement, code, or demo change.
- Keep a "reviewer can verify this in five minutes" path for each major claim.
- Do not add new experiments during discussion unless they clarify an already submitted claim and
  current rules allow the revision.

## Output format

```text
[Current stage] idea / experiments / writing / submission / discussion / accepted
[Next deadline] <official date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Anonymity checkpoint] pass / needs audit
[Owner map] <task -> person or role>
```

