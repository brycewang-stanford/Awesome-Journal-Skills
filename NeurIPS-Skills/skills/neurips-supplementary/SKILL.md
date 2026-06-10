---
name: neurips-supplementary
description: Use when deciding what NeurIPS material belongs in the main PDF body, the references, text appendices, the mandatory Paper Checklist, the separate code/data ZIP, or an external public artifact, and how to keep every supplemental component anonymous under double-blind review.
---

# NeurIPS Supplementary

Use this skill to prevent two common NeurIPS failures: hiding the main contribution in the appendix
and overloading the main paper with details that belong in supplemental material.

## Placement rules

- Main paper: problem, contribution, method, essential theory, core experiments, limitations, and
  enough detail for reviewers to judge correctness.
- References: complete, verified citations; do not rely on AI-generated references without manual
  verification.
- Text appendices: proofs, derivations, additional ablations, dataset details, model cards, extended
  limitations, and supporting analyses.
- Checklist: mandatory and placed according to current template instructions.
- Separate ZIP: code, data, scripts, configuration files, logs, lightweight demo assets, or other
  review artifacts when allowed by current rules.

## NeurIPS-specific guardrails

- The supplement does not rescue an unclear main claim. Reviewers are not required to read every
  supplemental detail.
- Supplementary material must be anonymized during double-blind review.
- Links must preserve anonymous browsing and comply with current policy.
- Code and data that support central claims should include exact commands and environment details,
  not just a repository dump.

## Placement decision table

NeurIPS assembles the final PDF from distinct zones plus a separate review ZIP. Misplacing material
is a recurring weakness: a proof that a reviewer cannot find, or a contribution buried where it does
not count. Map each item to exactly one home before submission; reopen the current template for the
authoritative zone list.

| Material | Home | Reason it goes there |
| --- | --- | --- |
| Central claim, headline result | Main body | reviewers judge the contribution here |
| Full proofs and derivations | Text appendix | body states the theorem; appendix carries the proof |
| Extra ablations, seeds, scaling | Text appendix | supports but does not replace core experiments |
| Dataset/model cards, datasheets | Text appendix + ZIP | provenance reviewers expect, anonymized |
| Mandatory Paper Checklist | Template-specified slot | desk-reject risk if missing or misplaced |
| Runnable code, configs, logs | Separate ZIP | review-only artifact, not body pages |
| Broader-impact discussion | Main body | a NeurIPS norm reviewers look for, not appendix-only |

## Datasets & Benchmarks supplement note

For a Datasets & Benchmarks track submission, the datasheet, license, intended-use statement, and
hosting/maintenance plan are not optional appendix garnish; they are part of what reviewers score.
Keep them anonymized for review and stage a de-anonymized public version for release. Hedge the exact
required documentation to the current year's track call.

## Worked vignette: a benchmark paper

Authors put their 40-page datasheet, croissant metadata, and loading code only in the appendix and
leave the main body to leaderboard tables. A NeurIPS reviewer cannot judge dataset quality from
tables alone. The fix: lift provenance, licensing, consent, and intended-use sentences into the main
body so the contribution is visible; keep the full datasheet and loaders in the appendix and ZIP; and
add one navigation sentence telling reviewers exactly where the documentation lives.

## Output format

```text
[Main-paper must stay] <items>
[Move to appendix] <items>
[Move to ZIP/artifact] <items>
[Anonymity fixes] <items>
[Reviewer navigation] <one sentence telling reviewers where to find support>
```

