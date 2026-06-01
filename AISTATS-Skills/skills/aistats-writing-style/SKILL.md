---
name: aistats-writing-style
description: Use when revising an AISTATS paper for concise AI-statistics framing, theorem-and-experiment clarity, 8-page submission compression, double-blind wording, reproducibility clarity, and statistically careful claims.
---

# AISTATS Writing Style

Use this when revising the main paper. AISTATS papers need compact statements of why a
statistical or ML contribution matters and enough detail for technical validation.

## Revision rules

- Put the AI/statistics contribution in the first page: problem, gap, method or theorem,
  evidence, and why existing methods are insufficient.
- Make assumptions explicit. AISTATS reviewers are sensitive to hidden distributional,
  asymptotic, optimization, or data-generating assumptions.
- Pair every major claim with either proof structure, simulation design, empirical table, or
  reproducibility detail.
- Use the 8-page body for core logic; move long derivations, extra simulations, and extended
  ablations to the appendix without making the main paper unintelligible.
- Avoid overclaiming empirical wins when differences are small or variance is unreported.
- Maintain double-blind style in self-citations, prior code references, acknowledgements,
  funding, and artifact descriptions.

## Output format

```text
[Writing diagnosis] clear / under-justified / overclaimed / overloaded
[First-page fix] <new framing>
[Claim discipline] <claim -> proof/experiment/limitation>
[Compression cuts] <move/delete/merge>
[Anonymity edits] <phrases to rewrite>
```
