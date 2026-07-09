---
name: recsys-writing-style
description: Use when revising an ACM RecSys paper for a recommendation-first first page, honest offline-versus-online framing, equal-budget baseline claims, leakage-aware evaluation wording, ACM two-column 8-page compression, double-blind phrasing, and claims scoped to what the ranking evidence actually supports rather than to leaderboard language.
---

# RecSys Writing Style

Use this when revising the main paper. RecSys papers need a compact statement of why a
**recommendation** result matters and enough evaluation detail to survive a reproducibility-minded
reviewer.

## Revision rules

- Put the recommendation contribution on the first page: problem, gap, method, offline evidence,
  and the offline-to-deployment bridge.
- Make the evaluation protocol explicit early: the split (temporal vs random), whether metrics are
  full-ranking or sampled, and that baselines are tuned under an equal budget.
- Pair every empirical claim with a table, an ablation, or an off-policy/A-B result — not with a
  superlative.
- Use the 8-page body for core logic; move tuning grids, extra datasets, and per-dataset
  breakdowns to the appendix (which counts inside the budget) without making the body unreadable.
- Avoid leaderboard framing ("state of the art," "outperforms all baselines") when the gain is
  small, the variance unreported, or the baselines under-tuned.
- Maintain double-blind style in self-citations, platform names, acknowledgements, funding, and
  the repository description.

## Claim-discipline for recommender papers

- State the split protocol in words, not just in a config: "we use a temporal leave-one-last
  split" pre-empts the leakage objection.
- Say the baselines were tuned with the **same budget** as the method; this one sentence defuses
  the field's central reproducibility complaint.
- When an offline metric is the only evidence, scope the claim to offline; do not let "nDCG rose"
  masquerade as "users are better served."
- Report variance (mean ± sd over seeds), and in captions say whether bars are sd, confidence
  intervals, or quantiles.
- Label beyond-accuracy goals (diversity, fairness, exposure) as measured quantities, not
  asserted virtues.

## Sentence-level rewrites

| Draft pattern | RecSys-safe rewrite |
|---|---|
| "Our model significantly outperforms all baselines." | "improves nDCG@20 by X (sd Y) over equal-budget-tuned baselines" |
| "We evaluate on a standard split." | "We use a temporal leave-one-last split to avoid future leakage." |
| "Achieves state-of-the-art recommendation." | Claim scoped to the datasets and cutoff actually tested |
| "Users will benefit from better recommendations." | "our off-policy estimate of engagement rises; deployment is future work" |
| "We use Recall@20." | "Recall@20 over the full item catalog (not a sampled candidate set)" |

## Vignette: compressing into eight two-column pages

A draft with a model, five datasets, and a sprawling related-work section: keep the method, the
assumption, the headline tuned table, one mechanism ablation, and the offline-online bridge in the
body; compress related work into contribution contrasts; move the tuning grid, two datasets, and
per-dataset breakdowns to the appendix with explicit forward references. The test of a good cut: a
reviewer should reconstruct the whole argument, including *how the baselines were tuned*, without
opening the repository.

## Output format

```text
[Writing diagnosis] clear / under-justified / overclaimed / leakage-ambiguous
[First-page fix] <new recommendation-first framing>
[Claim discipline] <claim -> table / ablation / off-policy result / scoped limitation>
[Evaluation wording] <split protocol / metric type / tuning-budget statement>
[Compression cuts] <move / delete / merge>
[Anonymity edits] <phrases to rewrite>
```
