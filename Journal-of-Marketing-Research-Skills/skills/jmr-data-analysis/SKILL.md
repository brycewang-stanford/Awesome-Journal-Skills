---
name: jmr-data-analysis
description: Use when running and reporting the analysis for a Journal of Marketing Research (JMR) manuscript — selecting the estimator that matches the design, and meeting JMR's hard journal-level reporting mandate of exact p-values, standard errors, and effect sizes, plus replication-ready disclosure. Executes and reports; jmr-methods designs the study and jmr-contribution-framing states the payoff.
---

# Data Analysis & Reporting (jmr-data-analysis)

## When to trigger

- Data are collected (experimental or observational) and it is time to estimate and report
- You are unsure whether your estimator matches your design
- You must conform to JMR's exact-statistics reporting rules
- A reviewer says "the analysis does not support the inference" or "report effect sizes"

## JMR's hard reporting mandate (journal-level)

JMR enforces statistics reporting more explicitly than generic top journals. Empirical papers must report:

- **Actual p-values to three digits** — *not* thresholds (no "p < .05"), *not* asterisks.
- **Standard errors** of parameter estimates in tables.
- **Effect sizes** — and a discussion of practical magnitude, not just significance.

AMA results-reporting style: **no leading zero** before the decimal (write `.97`, `p = .032`), and **no more than three decimal places**. Apply this to every table and in-text statistic.

## Choose the estimator that matches the design

| Design / claim                                  | Estimator                                                        |
|-------------------------------------------------|-----------------------------------------------------------------|
| Experiment (factorial, between/within)          | ANOVA / regression; estimated marginal means; planned contrasts |
| Behavioral mediation                            | Bootstrapped indirect effects (e.g., PROCESS), bias-corrected CIs |
| Moderation / moderated mediation                | Interaction term + simple slopes; conditional indirect effects   |
| Panel / observational causal                    | FE / DiD (modern staggered estimators); cluster-robust SE        |
| Endogenous regressor                            | IV/2SLS, control function; report first stage and instrument tests |
| Discrete choice / demand                        | Logit/probit; random-coefficient (BLP-style) demand              |
| Heterogeneity                                   | Hierarchical Bayes / mixture models                              |
| Counts / limited DV                             | Poisson/NB, Tobit, as the outcome requires                       |

Cluster standard errors to the sampling/assignment structure (e.g., by participant, store, or market).

## Behavioral analysis specifics

- Report manipulation- and attention-check results before the main effect.
- Mediation: bootstrap indirect effects with bias-corrected CIs (e.g., 5,000 resamples); for moderated mediation report the conditional indirect effect.
- Moderation: report the interaction coefficient, plot simple slopes, and give effect sizes per cell.

## Modeling / econometric specifics

- Report identification diagnostics (first-stage strength, parallel-trends/pre-trends, balance, overidentification) as relevant.
- Report structural parameter estimates with standard errors; show fit and counterfactuals where the contribution rests on them.

## Replication & robustness (AMA transparency policy)

- Provide enough detail (in-text, **Web Appendix**, or online supplements) for a reasonably trained researcher to replicate; be ready to share code, instruments/stimuli, and materials on request, and to provide data/materials before final acceptance.
- Put robustness — alternative specifications, subsamples, alternative measures, additional studies — in the **'W'-prefixed Web Appendix**, keeping the print paper within 50 pages.

## Anti-patterns

- Reporting "p < .05" or asterisks instead of exact three-digit p-values.
- Tables with no standard errors; significance without effect sizes.
- Causal-steps (Baron-Kenny) mediation instead of bootstrapped indirect effects.
- Ignoring clustering / non-independence; a weak or untested instrument.
- A leading zero before the decimal, or more than three decimal places.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric
[Estimator] matches design? SE clustering ...
[Exact stats] p three-digit / SEs / effect sizes: pass/fix
[AMA number style] no leading zero, <= 3 decimals: pass/fix
[Identification or process] diagnostics reported
[Replication] Web Appendix + code/materials ready
[Next skill] jmr-contribution-framing
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
