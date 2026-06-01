---
name: aistats-author-response
description: Use when drafting AISTATS author responses or author-reviewer discussion replies under OpenReview, text-only discussion, no-link guidance, no revised-paper upload, anonymity requirements, and decision-focused clarification strategy.
---

# AISTATS Author Response

Use this after AISTATS reviews are released. Reopen the current OpenReview instructions and
author-discussion policy before drafting because response mechanics are cycle-specific.

## Triage

- Answer concerns that affect correctness, novelty, statistical validity, clarity,
  reproducibility, or fit for AISTATS.
- Use existing submitted evidence: paper sections, appendices, supplementary material,
  theorem statements, experiments, checklist entries, and code/data descriptions.
- Keep the reply anonymous. Do not reveal institution, authorship, grants, private URLs, or
  repository ownership.
- Treat discussion as clarification, not revision. Do not depend on uploading a revised paper
  or new supplement unless current instructions explicitly allow it.
- If current rules prohibit links, do not use URLs in the discussion. AISTATS 2026
  author-reviewer discussion was text-only and links were not allowed.
- Correct factual errors first, then address requests for missing comparisons, uncertainty
  estimates, proofs, or hyperparameters.

## Drafting pattern

1. State the decision-critical correction or concession.
2. Point to exact submitted evidence.
3. Explain the statistical or theoretical consequence.
4. Promise a camera-ready wording fix only if it does not add unsupported new claims.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] correctness / novelty / statistical validity / clarity / reproducibility
[Draft response] <AISTATS-ready anonymous text>
[Evidence anchor] <paper/appendix/supplement item>
[Forbidden content removed] <links, identity leaks, new unsupported claims>
```
