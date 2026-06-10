---
name: jae-tables-figures
description: Use when building the exhibits for a Journal of Accounting and Economics (JAE) manuscript — variable-definition appendix, sample-construction table, descriptive statistics and correlations, regression tables with clustered standard errors, and event-study/DiD figures — in Elsevier house style so each exhibit is self-contained and reproducible.
---

# Tables & Figures for JAE (jae-tables-figures)

## When to trigger

- Regression output is pasted in raw and not yet reader-ready
- Tables do not state the sample, the SE clustering, or variable definitions
- A reviewer cannot tell which coefficients are the test of the hypothesis
- You need a variable-definition appendix or a sample-waterfall table

## The standard JAE exhibit set

Archival JAE papers carry a recognizable table sequence; build it deliberately:

1. **Variable definitions** (often an appendix): every variable, its construction, and the data source (Compustat/CRSP/I/B/E/S/Execucomp/DealScan/Audit Analytics). Reviewers check this first.
2. **Sample construction**: the waterfall from population to final N with counts at each exclusion.
3. **Descriptive statistics**: N, mean, median, SD, and key percentiles; note winsorization (e.g., 1%/99%).
4. **Correlation matrix**: Pearson (and often Spearman) correlations among main variables.
5. **Main regressions**: the hypothesis tests, with the coefficient of interest visually identifiable.
6. **Cross-sectional / mechanism tables**: partitions showing the effect concentrates where the friction is severe.
7. **Robustness tables**: alternative proxies, specifications, placebo/falsification, identification diagnostics.

## Reporting conventions reviewers expect

- Report **coefficients with t- or z-statistics (or standard errors)** and state the **SE clustering** (firm, or two-way firm-and-year) in the table note.
- Indicate the **fixed effects** included (firm, year, industry) in each column.
- Use consistent **significance markers** and define them in the note; report **economic magnitude**, not only stars.
- Every table note must make the exhibit **self-contained**: sample, period, units, FE, clustering, and what the key coefficient tests.

## Figures

- **Event studies**: plot cumulative abnormal returns around the information event with confidence bands.
- **DiD dynamics**: plot event-time coefficients to show parallel pre-trends and the post-treatment effect.
- **Comparative statics** (analytical papers): plot the model's predicted relations.
Keep figures clean, labeled, and grayscale-legible; Elsevier renders single-column native format.

## Elsevier house style

JAE follows Elsevier author-date (Harvard) referencing and numbered sections (1, 1.1, 1.1.1). Number tables/figures in citation order, reference each in the text, and keep the in-text discussion interpreting—not merely repeating—the numbers. Remember the manuscript also requires **Highlights** (2-5 bullets, ≤125 characters each) summarizing the findings.

## Checklist

- [ ] Variable-definition appendix with data sources
- [ ] Sample-construction waterfall table
- [ ] Descriptives + correlation matrix; winsorization noted
- [ ] Main tables: key coefficient identifiable; t-stats/SEs shown
- [ ] FE and SE clustering stated in every table note
- [ ] Mechanism and robustness tables present
- [ ] Event-study/DiD figures with pre-trends and bands
- [ ] Every exhibit self-contained; Highlights drafted

## Anti-patterns

- **Raw software dumps** with unlabeled columns.
- **No clustering/FE disclosure** in table notes.
- **Stars without magnitudes.**
- **Undefined variables** or missing data-source attribution.
- **DiD with no event-time figure** to support parallel trends.


## Exhibit pass for Journal of Accounting and Economics

Use this as a second-pass capability check. First lock the economic mechanism, accounting setting, identification or model, and market/contracting consequence; then test whether the manuscript addresses accounting-economics reviewers who expect economics discipline, identification, and market or contracting implications.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAR for accounting research breadth, TAR for accounting flagship breadth, Review of Accounting Studies for archival/accounting focus; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Exhibit list】vars / sample / descriptives / corr / main / mechanism / robustness / figures
【Each main table note】sample, period, FE, SE clustering, sig. definitions
【Figures】event-study CARs / DiD dynamics / comparative statics
【Highlights drafted?】2-5 bullets ≤125 chars
【Next step】jae-writing-style
```
