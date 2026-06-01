---
name: neurips-submission
description: Use when auditing a NeurIPS main-track submission for current-cycle CFP, OpenReview, formatting, anonymity, track, contribution-type, checklist, code/data, dual-submission, and LLM/agent policy compliance.
---

# NeurIPS Submission

Use this skill for a submission-readiness audit before a paper enters OpenReview. Treat every
annual rule as volatile: reopen the current CFP, Main Track Handbook, paper template, and submission
portal before final advice.

## Core checks

- Target the right track. NeurIPS main track, Evaluations & Datasets, Position Papers,
  Reproducibility/MLRC, competitions, workshops, and Journal-to-Conference tracks have separate
  calls and portals; do not assume transfer is possible after submission.
- Confirm that all authors have active OpenReview profiles and that author names are entered by the
  abstract deadline. After that, only author order may change under the 2026 handbook.
- Verify the yearly LaTeX style file, PDF-only submission format, content-page limit, file-size
  limit, and whether references, text appendices, checklist, and code/data are handled separately.
- Confirm double-blind compliance across the main PDF, supplement, repository links, uploaded ZIPs,
  acknowledgments, self-citations, prompts, demos, model cards, dataset cards, and metadata.
- Check dual-submission exposure. Overlapping archival submissions can cause desk rejection; do not
  submit the same work to another archival venue while it is under NeurIPS review.

## NeurIPS-specific risks

- Missing checklist is a desk-rejection risk.
- A submission that has strong benchmark wins but weak scientific explanation is vulnerable.
- A paper with copied, hallucinated, or unverifiable citations creates academic-integrity risk.
- Public preprints are allowed in the 2026 policy, but aggressive advertising of a submitted paper
  can violate the spirit of double-blind review.
- Non-standard agent or LLM use that is part of the method should be documented in the experimental
  setup; ordinary editing and basic code assistance generally do not need a methods statement.

## Audit workflow

1. Identify the intended track and contribution type: General, Theory, Use-Inspired,
   Concept & Feasibility, Negative Results, or the current-cycle equivalent.
2. Compare the PDF to the live template and page rules.
3. Walk every link, repository, dataset, artifact, and supplement for anonymity.
4. Confirm code/data ZIP handling and whether the artifact is review-only or intended for public
   release after acceptance.
5. Inspect the checklist answers for unsupported "yes" responses, missing justifications, and
   claims that are broader than the evidence.
6. Record all unresolved current-cycle items in the output.

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Track] Main / E&D / Position / MLRC / other
[Contribution type] General / Theory / Use-Inspired / Concept & Feasibility / Negative Results / current-cycle label
[Blocking official checks] <CFP/template/OpenReview/anonymity/checklist/code-data/dual-submission>
[Highest desk-reject risk] <one issue>
[Fix list] <ordered fixes before submission>
```

