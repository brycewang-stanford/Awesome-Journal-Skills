---
name: iclr-workflow
description: Use when planning an ICLR project timeline from topic selection through OpenReview submission, discussion, revision, decision, camera-ready, poster, video, and public artifact release. Use when sequencing milestones against the current cycle's OpenReview deadlines, budgeting time for the long public discussion phase, or assigning owners for anonymity audits and reviewer-verifiable evidence paths.
---

# ICLR Workflow

Use this as the project-management skill for an ICLR submission. Always replace dates with the
current cycle's official deadlines and work backwards from OpenReview cutoffs.

ICLR is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chair, Senior Program Chair, and Program
Chairs (2026 General Chair: Carl Vondrick; Senior PC: Bharath Hariharan; PCs: Raffel, Pinto, Yang,
Faust, verified 2026-06-22), and the cost model is registration fees, not APCs — proceedings are
open-access on OpenReview. Conference organizers rotate yearly, so re-check the current CFP and
committees page rather than carrying a name forward.

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

## Phase ownership and risk

ICLR's timeline differs from venues with a short rebuttal: the public discussion phase is long, and
revisions you upload remain visible. Plan for an extended, public exchange, not a one-shot rebuttal.

| Phase | Owner focus | ICLR-specific risk |
| --- | --- | --- |
| Abstract deadline | Profiles, conflicts, real abstract | Placeholder abstract or incomplete profile |
| Paper deadline | Anonymized PDF, supplement, disclosures | Identity leak in code or links |
| Review release | Triage, assign evidence owners | Reacting to every score instead of the AC's concern |
| Discussion | Replies, allowed revisions, changelog | Promising runs the cycle's rules disallow |
| Camera-ready | De-anonymize, fulfill promises | Final PDF drifts from the meta-review |

## Worked vignette

A two-person team plans backward from the OpenReview paper deadline for an interpretability paper.
They lock the main claim and core ablation early, reserve the final days for an anonymity audit of
the PDF and code ZIP, and pre-assign discussion roles: one owns evidence replies, one owns wording
and the changelog. When reviews land they already have a "verify in five minutes" probe script, so
the public thread stays concrete.

## Reviewer-pushback patterns to schedule around

- "We need a new experiment fast." Pre-build a probe or ablation harness so small results are cheap.
- "Anonymity slipped after an edit." Re-run the audit after every PDF, supplement, or code change.
- "Deadline confusion." Treat the current cycle's OpenReview dates as the single source of truth.

## Output format

```text
[Current stage] idea / experiments / writing / submission / discussion / accepted
[Next deadline] <official date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Anonymity checkpoint] pass / needs audit
[Owner map] <task -> person or role>
```

