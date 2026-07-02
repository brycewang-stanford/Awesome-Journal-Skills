---
name: nejm-figures-tables
description: Use to build NEJM clinical display items correctly — Table 1 baseline characteristics by group (with standardized differences, not P values), Kaplan-Meier curves with numbers-at-risk, forest plots for subgroups and meta-analyses, and the CONSORT participant flow diagram.
---

# Clinical Display Items (nejm-figures-tables)

## When to trigger

- Table 1 reports P values comparing randomized groups (current guidance discourages this).
- A Kaplan–Meier plot has no numbers-at-risk row.
- Subgroup results are in text rather than a forest plot.
- The RCT lacks a CONSORT flow diagram, or its denominators don't reconcile.

## Table 1 — baseline characteristics by group

Table 1 describes the **baseline characteristics of the enrolled population, by group**.

- Columns are the randomized/study groups (and often an overall column); rows are characteristics (demographics, key clinical variables, disease severity).
- **Do not report P values comparing baseline characteristics in a randomized trial** — by design, baseline differences are due to chance. Current guidance is to report **standardized differences** if balance must be summarized.
- Report continuous variables as mean (SD) or median (IQR) per the distribution; categorical as n (%).
- Denominators must match the analysis populations and the CONSORT flow diagram.

## Kaplan–Meier curves (time-to-event)

- Show the survival/event curves per group over the follow-up period.
- **A numbers-at-risk row beneath the time axis is required** — readers must see how many remain at each time point.
- Consider showing the **hazard ratio with 95% CI** and the log-rank/Cox result on the panel.
- Censor marks or a clear censoring description; cumulative-incidence curves when competing risks matter.
- Do not extend curves into time ranges where almost no one remains at risk.

## Forest plots (subgroups & meta-analyses)

- For **subgroup analyses**: one row per pre-specified subgroup, the effect estimate with 95% CI, and the **interaction P value** (see `nejm-statistics`). A reference line at the null. Make clear which subgroups were pre-specified.
- For **meta-analyses**: per-study estimates with CIs, weights, the pooled estimate (diamond), and heterogeneity (I², τ²).
- Keep the scale honest (log scale for ratio measures); annotate which direction favors which arm.

## CONSORT participant flow diagram (RCTs)

The flow diagram is mandatory for trials (see `nejm-reporting`): Enrollment → Allocation → Follow-up → Analysis, with excluded/lost numbers and reasons at each stage. **Its numbers must reconcile** with Table 1 and the analysis populations.

## Figure specifications

- Legible at print size; sans-serif labels; avoid tiny fonts and hairlines.
- **Show uncertainty**: CIs on estimates, error bars defined in the legend, numbers-at-risk on K–M.
- Colorblind-safe palette; do not encode group by color alone (use line style/markers too).
- Each legend stands alone: what is shown, the groups, the statistic, n, and the error/CI definition.
- De-identify any patient images; remove protected health information from all panels (see `nejm-ethics`).

## Display-item budget and placement

The ~2700-word Original Article format imposes a hard display-item budget. Main-paper slots go to what a clinician needs to judge the trial: Table 1, the primary-outcome figure (often Kaplan–Meier), the subgroup forest plot, and a safety table. Everything else moves to the **supplementary appendix** — which NEJM reviewers do read.

- [ ] Every display item is cited in the text, in numerical order; an uncited item gets cut.
- [ ] One message per figure — split or simplify a panel that needs a paragraph of caption.
- [ ] Safety tables report **absolute event counts and rates per arm** (see `nejm-statistics`).

## Worked micro-example — one Table 1 row (before → after)

- Before (off-style): `Age, years | 63.4 | 62.9 | P=0.71`
- After: `Age — yr, mean ±SD | 63.4±9.2 | 62.9±9.5` — the P column deleted; the unit riding in the row label. If balance must be summarized, a standardized-difference column replaces the P column — never both. (Values invented for illustration.)

## Output format

```
【Table 1】 by group, n(%)/mean(SD)/median(IQR), NO baseline P values (standardized diffs ok)? yes/no
【Budget】 main paper limited to decision-critical items; appendix items still cited in order? yes/no
【Kaplan–Meier】 numbers-at-risk row present? HR+CI shown? censoring clear? yes/no
【Forest plot】 subgroups pre-specified + interaction P? / meta heterogeneity reported? yes/no
【CONSORT flow diagram】 present and reconciles with Table 1 + analysis n? yes/no
【Figure specs】 CIs shown / colorblind-safe / legends standalone / de-identified? yes/no
【Fixes】 [...]
【Next】 nejm-ethics
```

## Anti-patterns

- **Do not** put P values on baseline-comparison rows of Table 1 in a randomized trial.
- **Do not** show a Kaplan–Meier curve without a numbers-at-risk row.
- **Do not** bury subgroup results in prose — use a forest plot with interaction tests.
- **Do not** let the CONSORT flow numbers disagree with Table 1 or the analyzed populations.
- **Do not** display identifiable patient images or PHI.
