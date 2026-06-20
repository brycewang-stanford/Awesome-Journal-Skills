---
name: jmis-tables-figures
description: Use when the exhibits are the bottleneck for a Journal of Management Information Systems (JMIS) manuscript — regression/SEM tables, platform/value figures, measurement-model exhibits, or artifact-evaluation charts that must carry the argument inside the 50-page budget. Finalizes exhibits and labeling; it does not run the analysis (jmis-data-analysis) or polish prose (jmis-writing-style).
---

# Tables and Figures (jmis-tables-figures)

## When to trigger

- A reader cannot get the headline result from the tables/figures without the text
- Exhibits are dense, mislabeled, or report estimates without economic magnitude
- The exhibit count is pushing the manuscript over the **50-page** ceiling
- Survey papers lack the measurement-model exhibits reviewers expect (reliability/validity, loadings, HTMT)

## Make each exhibit answer one question

A JMIS exhibit should be readable on its own: a self-contained title, defined variables and units, the sample and period, and a note stating the estimator, clustering, and what the stars/SEs mean. The reader should be able to state the finding from the table alone. Order exhibits to track the argument — descriptive/measurement first, main result next, mechanism and robustness after.

## Report magnitudes, not just significance

JMIS values managerial relevance, so a coefficient table that shows only significance underdelivers. Report **economic magnitude** — marginal effects, elasticities, dollar value, or lift — alongside (or instead of) raw coefficients, and put the number that matters in the table the reader will actually look at. Report standard errors (and the clustering level) clearly; a figure with confidence intervals often communicates an effect better than a wall of asterisks.

## Exhibits by evidence type

| Evidence type | Exhibits reviewers expect |
|---------------|----------------------------|
| **IT-value / platform econometrics** | Descriptives + balance; main DiD/IV table; an **event-study figure with leads** for parallel-trends; robustness table; magnitude in interpretable units |
| **Behavioral survey (SEM/PLS)** | Measurement model (loadings, CR, AVE), discriminant validity (HTMT / Fornell-Larcker), structural-path diagram with coefficients and significance |
| **Experiment** | Cell means with CIs, manipulation-check results, treatment-effect figure, mediation/moderation exhibit |
| **Design-science / ML** | Benchmark table vs. credible baselines with uncertainty; ablation; a figure tying performance to the managerial decision |
| **Analytical model** | Comparative-static figures showing how the key outcome moves with the parameter that carries the insight |

## Respect the page budget and the appendix boundary

The complete manuscript is capped at **≤50 pages** (12pt, double-spaced), so exhibits compete with text for space. Keep in the body the exhibits that establish the contribution; move secondary robustness, full measurement batteries, and large parameter tables to the online appendix — but never let a load-bearing result live only in the appendix. Figures should be legible in grayscale and not rely on color alone. (检索于 2026-06；以官网为准.)

## Checklist

- [ ] Every exhibit is self-contained (title, variables, units, sample, period, note)
- [ ] The headline finding is readable from the main exhibits without the prose
- [ ] Economic magnitude (not just significance) is reported for the key effect
- [ ] SEs and clustering level are stated; CIs used where they communicate better
- [ ] Survey papers include measurement-model and discriminant-validity exhibits
- [ ] Empirical papers include an event-study/leads figure where parallel trends matter
- [ ] Body holds the contribution-establishing exhibits; appendix holds only support; ≤50pp respected

## Anti-patterns

- A coefficient table with stars but no magnitude or interpretation
- Exhibits the reader cannot parse without hunting through the text
- A load-bearing result relegated to the online appendix
- A staggered-DID paper with no event-study/leads figure
- A survey paper missing discriminant-validity evidence
- Color-only figures that fail in grayscale

## Output format

```text
【Headline exhibit】reads alone? magnitude shown? [Y/N]
【Diagnostics shown】event-study/leads | measurement model + HTMT | benchmarks + uncertainty
【Inference labeling】SEs + clustering stated; CIs where clearer [Y/N]
【Body vs. appendix】contribution exhibits in body; ≤50pp respected [Y/N]
【Next step】jmis-writing-style
```
