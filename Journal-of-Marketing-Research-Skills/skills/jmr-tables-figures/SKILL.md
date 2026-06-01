---
name: jmr-tables-figures
description: Use when building exhibits for a Journal of Marketing Research (JMR) manuscript — result tables, study-flow figures, interaction plots, and model summaries in AMA style, and deciding the split between main-text exhibits (inside the 50-page limit) and 'W'-prefixed Web Appendix exhibits (outside it). Enforces JMR's exact-statistics conventions inside every table.
---

# Tables & Figures (jmr-tables-figures)

## When to trigger

- Tables are cluttered, off AMA style, or not self-explanatory
- You must decide what stays in the print paper vs. the Web Appendix
- Statistics in exhibits use thresholds/asterisks instead of exact values
- Interaction or mediation results need a clear plot

## The 50-page split is the first decision

JMR's **50-page limit** is all-inclusive of title, abstract, keywords, text, footnotes, references, tables, and figures. The **Web Appendix does not count** toward it. So every exhibit is a budget decision:

- **Main text**: the exhibits a reader needs to follow the core argument — the key result table(s), the main interaction/mediation figure, the model summary, the design figure.
- **Web Appendix**: everything supplementary — full descriptive tables, robustness, additional studies, estimation details, full stimuli. Label these with a **'W' prefix**: "Table W1", "Figure W1" — a JMR/AMA-specific convention. The Web Appendix is a **single separate PDF**.

Push analyses to the Web Appendix to protect the 50-page budget; do not pad the print paper.

## Exact-statistics conventions inside exhibits

Every table must obey the journal-level reporting rules:

- Report **standard errors** for parameter estimates (typically in parentheses below the estimate).
- Report **exact p-values to three digits** where p-values appear — **no asterisk legends**, no "p < .05".
- **No leading zero** before the decimal; **no more than three decimals**.
- Report or enable **effect sizes** (e.g., cell means with SDs, eta-squared, standardized coefficients).

## Build exhibits by genre

- **Behavioral**: a table of cell means (SDs, n) per condition; an interaction plot with error bars; a mediation figure or table with bootstrapped indirect effects and bias-corrected CIs; simple-slopes plots for moderation.
- **Modeling / econometric**: a regression/structural table with coefficients and SEs; first-stage / identification diagnostics; a counterfactual or fit figure where the contribution depends on it.

## House-style essentials

- Each exhibit is **self-contained**: a descriptive title, defined variables, units, sample size, and a note explaining estimator and SE type.
- Reference every table/figure in the text in order; keep numbering consistent across text, main exhibits, and Web Appendix.
- Follow AMA author-year style in notes and captions.

## Anti-patterns

- Asterisk-and-threshold tables instead of exact p-values and SEs.
- Overstuffing the print paper and blowing the 50-page budget.
- Web Appendix exhibits not labeled with the 'W' prefix, or scattered across files instead of one PDF.
- Tables that cannot be read without the body text.

## Output format

```text
[Target] JMR
[Main-text exhibits] list (within 50pp)
[Web Appendix exhibits] W-prefixed, single PDF
[Exact stats in tables] SEs / 3-digit p / effect sizes: pass/fix
[AMA number style] no leading zero, <=3 decimals: pass/fix
[Self-contained & numbered] pass/fix
[Next skill] jmr-writing-style
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
