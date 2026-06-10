---
name: jbf-writing-style
description: Use when polishing Journal of Banking & Finance prose, structure, abstracts, introductions, variable definitions, result paragraphs, and Elsevier author-date reference style for a concise finance-journal manuscript.
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

- First submission is free-format, but use a consistent author-date style.
- Prepare 1-7 keywords and JEL codes.
- Highlights are encouraged; make them result-forward and short.
- Declare generative-AI use when applicable.
- Keep anonymization intact under double-anonymized review.

## Common fixes

- Replace "significant" with the effect size and confidence interval.
- Move dataset details from the introduction into data/methods unless they create
  the contribution.
- Give every acronym on first use.
- Put limitations before the referee finds them.

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
[Submission polish] keywords / JEL / highlights / declarations
[Next step] jbf-submission
```
