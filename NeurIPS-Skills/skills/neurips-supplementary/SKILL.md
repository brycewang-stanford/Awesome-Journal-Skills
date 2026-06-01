---
name: neurips-supplementary
description: Use when deciding what NeurIPS material belongs in the main PDF, references, text appendices, mandatory checklist, separate code/data ZIP, or external public artifact.
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

## Output format

```text
[Main-paper must stay] <items>
[Move to appendix] <items>
[Move to ZIP/artifact] <items>
[Anonymity fixes] <items>
[Reviewer navigation] <one sentence telling reviewers where to find support>
```

