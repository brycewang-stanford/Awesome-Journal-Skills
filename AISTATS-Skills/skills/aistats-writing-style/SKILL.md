---
name: aistats-writing-style
description: Use when revising an AISTATS paper for concise AI-statistics framing, theorem-and-experiment clarity, 8-page two-column compression, double-blind wording, reproducibility clarity, statistically careful claims, and assumption-labeling discipline that survives statistician reviewers.
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

## Theorem-presentation discipline

- Number assumptions and cite them by label inside every theorem statement; AISTATS readers
  audit assumption flows the way software reviewers audit imports.
- Give each major theorem a proof sketch in the body; the appendix proof supports the sketch
  but never replaces it.
- Keep problem-dependent constants visible or explicitly deferred; silently absorbing
  dimension or condition numbers into O-notation is a standing statistician complaint.
- Define notation once in one location — two-column pages punish redundant redefinition.
- Phrase remarks after theorems as interpretation, not as extra unproved claims; AISTATS
  reviewers treat every declarative sentence near a theorem as something they may verify.
- When a result is conjectured or only empirically supported, label it so; mixing proved and
  observed statements in one paragraph is a credibility leak at this venue.

## Sentence-level rewrites

| Draft pattern | AISTATS-safe rewrite |
|---|---|
| "Our method significantly outperforms..." | "reduces mean error by X (SE Y) over Z seeded runs" |
| "Under mild conditions..." | "Under Assumptions 1-3 (boundedness, ...)" |
| "It is easy to see that..." | "By Lemma 2 and the triangle inequality..." |
| "Achieves state-of-the-art..." | Claim scoped to the regimes actually tested |

## Vignette: compressing into eight two-column pages

A draft with three theorems, six figures, and a sprawling related-work section: keep all
theorem statements, one sketch each, and the two decision-critical figures (the rate plot
and the coverage plot); compress related work into contribution contrasts; move secondary
lemmas and four figures to the appendix with explicit forward references. The test of a good
cut: a reviewer should reconstruct the whole argument without ever opening the supplement.

## Output format

```text
[Writing diagnosis] clear / under-justified / overclaimed / overloaded
[First-page fix] <new framing>
[Claim discipline] <claim -> proof/experiment/limitation>
[Compression cuts] <move/delete/merge>
[Anonymity edits] <phrases to rewrite>
```
