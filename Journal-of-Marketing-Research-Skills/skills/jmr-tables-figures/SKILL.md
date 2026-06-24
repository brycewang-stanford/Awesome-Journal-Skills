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

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMR mixes experiments, structural models, and quasi-experiments; the chain below serves the experimental and reduced-form lanes, while structural demand estimation uses its own toolkit.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Asterisk-and-threshold tables instead of exact p-values and SEs.
- Overstuffing the print paper and blowing the 50-page budget.
- Web Appendix exhibits not labeled with the 'W' prefix, or scattered across files instead of one PDF.
- Tables that cannot be read without the body text.


## Exhibit pass for Journal of Marketing Research

Run this as a concrete capability pass. First lock the marketing construct, data or study design, inference threat, and managerial or consumer implication; then test whether the manuscript addresses marketing reviewers who expect measurement, experiments, consumer behavior, or empirical strategy to answer a marketing question.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Marketing Science for quantitative modeling, Journal of Marketing for strategic managerial contribution, Journal of Consumer Research for consumer-theory depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

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
