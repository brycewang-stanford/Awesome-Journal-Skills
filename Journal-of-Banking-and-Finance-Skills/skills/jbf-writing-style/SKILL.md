---
name: jbf-writing-style
description: Use when polishing Journal of Banking & Finance prose, structure, abstracts, introductions, variable definitions, result paragraphs, and Elsevier numbered-reference readiness for a concise finance-journal manuscript.
---

# Writing Style (jbf-writing-style)

## When to trigger

- The manuscript is technically complete but reads slowly
- Results paragraphs describe coefficients without interpretation
- References, keywords, highlights, or declarations need Elsevier/JBF polish

## Style principles

- **Lead with the finance question** before the method.
- **State the design plainly**: what variation, what unit, what controls, and why it
  is credible.
- **Translate coefficients into economics**: basis points, assets, loan spreads,
  capital ratios, abnormal returns, default probabilities.
- **Use active, compact prose**. Avoid "it is worth noting" and long literature
  throat-clearing.
- **Keep claims bounded** to the design and sample.

## Results paragraph pattern

```text
Table X tests [claim]. Column (Y) includes [fixed effects/controls] and clusters
standard errors by [level]. A one-standard-deviation increase in [treatment] is
associated with [magnitude] change in [outcome], equal to [economic benchmark].
The estimate is robust to [key check], supporting [mechanism].
```

## Elsevier/JBF submission style notes

- First submission has no strict reference-format requirement if references are complete and consistent; prepare for JBF's proof-stage numbered Elsevier reference style.
- Prepare 1-7 English keywords; keep JEL codes as useful finance metadata rather than a verified hard requirement.
- Highlights are encouraged; make them 3-5 result-forward bullets, each no more than 85 characters.
- Declare generative-AI use when applicable.
- Keep anonymization intact under double-anonymized review.

## Common fixes

- Replace "significant" with the effect size and confidence interval.
- Move dataset details from the introduction into data/methods unless they create
  the contribution.
- Give every acronym on first use.
- Put limitations before the referee finds them.

## Abstract calibration for JBF

A JBF-ready abstract typically runs four to six sentences: question, setting and data, design, headline magnitude in finance units, and one bounded implication. The current Guide caps the abstract at **250 words**.

```text
[Question] Does X friction change Y bank/market outcome?
[Setting] data + period + unit (e.g., bank-quarter Call Reports, 2005-2019)
[Design] the variation in one clause (staggered adoption / threshold / exposure)
[Result] magnitude with units (basis points, pp of assets, capital-ratio points)
[Implication] one sentence, inside the identified margin
```

## Worked rewrite (illustrative)

Before: "The coefficient on the regulation dummy is negative and significant at the 1% level, confirming our hypothesis."

After: "Following adoption, treated banks cut commercial lending by 0.9 percentage points of assets (illustrative), about one quarter of average pre-period loan growth, consistent with a liquidity-hoarding channel and concentrated among banks below the median deposit franchise."

The rewrite names the unit, the benchmark, the mechanism, and the heterogeneity in one sentence — the cadence JBF results sections reward.

## Banking terminology hygiene

- Distinguish CET1, Tier 1, and total capital ratios; never write "capital ratio" alone where the Basel definition matters.
- Define the NPL ratio (nonperforming loans over gross loans) and the delinquency threshold used.
- State whether the Z-score uses rolling or full-sample volatility, with the construction in the variable appendix.
- Report spreads in basis points and balance-sheet effects in percentage points of assets; never mix the two in one paragraph without labels.

## Introduction pacing for JBF

- Page 1: question, setting, design, and the headline magnitude in finance units.
- Page 2: mechanism evidence and the two or three literature deltas.
- Keep any roadmap paragraph to three sentences or fewer; JBF readers skip longer ones.

## Prose pushbacks JBF referees make

- "I cannot tell which results are causal." → label each claim causal, predictive, or descriptive in the text itself.
- "The policy section reads like advocacy." → tie every recommendation to an estimated margin and its boundary.
- "Variable definitions are scattered." → consolidate into one appendix table and reference it from every exhibit.

## Finance-result sentence

Use this pattern for every headline result:

```text
In [sample/design], [shock or treatment] changes [finance outcome] by [magnitude in finance units],
relative to [benchmark], consistent with [mechanism] and bounded by [main limitation].
```

This prevents significance-only prose and forces the mechanism into the result paragraph.

## Output format

```text
[Section] abstract / introduction / data / results / conclusion
[Main edit] ...
[Magnitude wording] ...
[Claim boundary] ...
[Submission polish] keywords / optional JEL / highlights / declarations
[Next step] jbf-submission
```
