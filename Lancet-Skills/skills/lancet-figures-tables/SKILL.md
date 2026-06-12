---
name: lancet-figures-tables
description: Use to build and check The Lancet's clinical display items — the Table 1 baseline characteristics, Kaplan–Meier curves with numbers at risk, forest plots for subgroups/meta-analyses, the CONSORT/study-flow diagram, and maps for multi-country studies — all with confidence intervals shown.
---

# Clinical Figures & Tables (lancet-figures-tables)

## When to trigger

- The manuscript lacks a Table 1, a flow diagram, or a survival/forest plot the design calls for.
- Effect estimates are shown without confidence intervals.
- Kaplan–Meier curves have no numbers-at-risk row.
- A multi-country study has no map and the reader cannot see where the data came from.

## The standard Lancet clinical display items

### Table 1 — baseline characteristics

- [ ] One column per arm/group (plus overall if helpful); rows = key demographic and clinical characteristics.
- [ ] Report **n (%)** for categorical and **mean (SD)** or **median (IQR)** for continuous — matched to distribution.
- [ ] Include the equity-relevant characteristics the study warrants (sex/gender, age, race/ethnicity where relevant, socioeconomic/PROGRESS-Plus factors) — coordinate with `lancet-ethics`.
- [ ] **Do not** include P values comparing randomised arms at baseline (in an RCT, baseline imbalance is by chance) unless specifically justified.

### Kaplan–Meier curves (time-to-event)

- [ ] Plot survival/cumulative-incidence by arm with a **numbers-at-risk** table beneath the x-axis at each time point.
- [ ] Show the hazard ratio with **95% CI** and the (log-rank) p; censoring indicated.
- [ ] Axes labelled with time unit and the clinical event; truncate y-axis only with justification.

### Forest plots

- [ ] For **pre-specified subgroups**: point estimate + 95% CI per subgroup, with the overall estimate and the **interaction p value** (not within-subgroup P values) — see `lancet-statistics`.
- [ ] For **meta-analyses**: per-study estimate + CI, pooled estimate (diamond), heterogeneity (I², τ²), and the model (fixed/random).

### CONSORT / study-flow diagram

- [ ] The participant flow diagram (CONSORT for RCTs, PRISMA for reviews) — see `lancet-reporting`. It is a required display item; numbers must reconcile with Table 1 and the analysis populations.

### Maps (multi-country / global-health studies)

- [ ] For international or LMIC studies, a map showing participating countries/sites or the geographic distribution of the outcome — supports the global-relevance framing.

## Cross-cutting specs

- [ ] **Confidence intervals shown** on every effect estimate in figures (error bars defined as 95% CI).
- [ ] Colourblind-safe palette; meaning never conveyed by colour alone; legible at print size.
- [ ] Every figure legend defines the estimate, the uncertainty (95% CI), n, and the test.
- [ ] Display-item count within the journal's allowance; overflow → appendix.

## What Lancet reviewers scan a display item for

The Lancet's clinical readership reads tables and figures before the prose, so a display item that hides uncertainty or contradicts the text is an immediate credibility problem. The statistical reviewer checks that every effect carries a 95% CI, that Kaplan–Meier curves expose the thinning denominator via a numbers-at-risk row, and that subgroup forests report an interaction test, not within-subgroup P values. Desk-reject-adjacent problems: effects with no CI; baseline P values in an RCT Table 1; survival curves with no numbers at risk; a subgroup figure with no interaction test; a multi-country study with no map. Confirm the display-item allowance and figure specifications in the journal's author guidelines.

## Worked micro-example (illustrative numbers — not real data)

A hypothetical cardiovascular RCT, composite MACE outcome over 36 months.

```
Kaplan-Meier (illustrative): 36-mo event rate 12.4% vs 16.8%
  Hazard ratio 0.73 (95% CI 0.62-0.86), log-rank p=0.0002
  Numbers at risk (0/36 mo): 2 050/1 690 vs 2 048/1 588
  Absolute risk difference 4.4 pp; NNT ~23 over 3 years (illustrative).
Subgroup forest: 6 pre-specified, overall HR 0.73 (0.62-0.86), interaction p=0.41.
Table 1: arm columns, mean (SD) / n (%), NO baseline P column.
```

The numbers-at-risk row shows the curves stay reliable, the NNT gives the magnitude the relative HR hides, and the interaction P keeps the subgroup figure honest.

## Reviewer-pushback patterns and the venue-specific fix

- *"Figures report effects without confidence intervals."* → Add 95% CIs to every estimate; define error bars in each legend.
- *"The survival curves have no numbers at risk."* → Add a numbers-at-risk row at each time point and report the HR with 95% CI.
- *"Subgroup panels show within-subgroup P values."* → Replace with a forest plot carrying the overall estimate and an interaction P; restrict to pre-specified subgroups. For a multi-country study, add a site/outcome map to make the global relevance visible.

## Output format

```
【Table 1】 present? arms × characteristics, correct summaries, no baseline P in RCT, equity vars? → gaps
【Kaplan–Meier】 needed? numbers-at-risk + HR(95% CI) present? yes/no/NA
【Forest plot】 subgroups (interaction p) / meta-analysis (pooled + heterogeneity)? yes/no/NA
【Flow diagram】 CONSORT/PRISMA present + reconciles? yes/no
【Map】 multi-country study has a map? yes/no/NA
【CIs shown on all estimates?】 yes/no
【Next】 lancet-research-in-context
```

## Anti-patterns

- **Do not** show effect estimates without confidence intervals.
- **Do not** put baseline P values in an RCT Table 1.
- **Do not** present Kaplan–Meier curves without a numbers-at-risk row.
- **Do not** display subgroups with within-subgroup P values instead of interaction tests.
