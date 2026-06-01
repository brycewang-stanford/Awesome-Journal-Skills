---
name: psci-data-analysis
description: Use when analyzing and reporting results for a Psychological Science manuscript. The journal requires effect sizes with confidence intervals, full disclosure of exclusions/conditions/measures, and a clear confirmatory/exploratory split, with analysis scripts and data shared. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (psci-data-analysis)

Psychological Science holds analyses to high credibility standards: **effect sizes with confidence
intervals** for major results, **full disclosure** of how the data were handled, and a clean
**confirmatory vs. exploratory** separation. Analysis scripts and data are shared and can be checked.

## When to trigger

- Running and reporting the main and supporting analyses
- A reviewer asked for effect sizes, intervals, robustness, or disclosure
- Reconciling preregistered analyses with exploratory follow-ups
- Preparing analysis scripts and a data dictionary for deposit

## Reporting norms Psychological Science expects

1. **Effect sizes + uncertainty.** Report a standardized or unstandardized effect size **and a measure
   of uncertainty (e.g., confidence intervals)** for major results — not just p-values and stars.
2. **Full disclosure (the "21-word-solution" spirit).** Report **how sample size was determined**,
   **all** data exclusions (and reasons), **all** manipulations/conditions, and **all** measures. Total
   excluded observations must be stated.
3. **Confirmatory vs. exploratory.** Label preregistered confirmatory analyses separately from
   exploratory ones; do not present exploratory results as predicted (no HARKing).
4. **Appropriate inference.** Justify the model; report assumptions/diagnostics; correct for multiple
   comparisons when testing many outcomes; consider robust or Bayesian alternatives where apt.
5. **Replicability of the analysis.** Provide analysis scripts and a data dictionary; results should
   regenerate from the shared data in a fresh session (see `psci-open-science-and-transparency`).

## Robustness

- Show the result survives reasonable alternative specifications and exclusion choices; report
  sensitivity rather than a single fragile model. For small samples, be candid about uncertainty.

## Anti-patterns

- p-values and stars with no effect size or confidence interval
- Selectively reporting conditions, measures, or exclusions (undisclosed flexibility)
- HARKing exploratory findings into confirmatory hypotheses
- Optional-stopping / garden-of-forking-paths analyses presented as planned
- Analysis code that does not reproduce the reported numbers

## Output format

```
【Main result】effect size + confidence interval + meaning
【Disclosure】N-determination + all exclusions + all conditions + all measures reported? [Y/N]
【Confirmatory vs exploratory】clearly separated? [Y/N]
【Inference】assumptions/diagnostics, MHT handled?
【Reproducible】scripts + data dictionary + fresh-session check? [Y/N]
【Next】psci-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `effectsize`, `emmeans`, `metafor`, JASP/jamovi, reproducible-report tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — statistical and disclosure requirements
