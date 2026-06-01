---
name: jde-data-analysis
description: Use when estimation, heterogeneity, attrition, measurement, or inference choices need to meet Journal of Development Economics (JDE) empirical norms — clustered field data, survey measurement error, and treatment-effect heterogeneity in low- and middle-income settings. Covers the analysis itself, not the identifying design.
---

# Data Analysis (jde-data-analysis)

## When to trigger

- The identification is settled but the estimation, inference, or heterogeneity analysis is unconvincing
- A referee would question standard errors, attrition, measurement error, or sample construction
- You need to decide how to present treatment-effect heterogeneity across subgroups
- You are unsure the analysis would survive JDE's replication scrutiny

## JDE empirical norms

JDE referees are experienced with the realities of **field and survey data in developing countries** — clustered sampling, panel attrition, noisy self-reports, seasonality, and small effective sample sizes. Analysis that ignores these reads as naive. Hold the work to these standards:

- **Inference matched to the data structure.** Cluster at the level of treatment assignment or sampling (village, school, market); with few clusters use wild-cluster bootstrap or randomization inference rather than naive cluster-robust t-stats.
- **Attrition and missing data.** Document panel attrition, test whether it is differential by treatment, and bound effects (Lee bounds) when it is. Survey non-response and refusal patterns belong in the appendix.
- **Measurement.** Be explicit about how key variables (consumption, income, yields, test scores, health) were measured and constructed; address recall error, social-desirability bias, and unit/seasonal issues. Pre-specify or transparently justify index construction.
- **Heterogeneity, disciplined.** Development audiences care about *for whom* effects bind, but data-mined subgroups are penalized. Pre-specify subgroups where possible; otherwise treat heterogeneity as exploratory and adjust for multiple comparisons.
- **Magnitudes in welfare terms.** Report effects in policy-comparable units (share of the poverty gap, cost-effectiveness per dollar, standard deviations) — see jde-contribution-framing.

Because JDE's **replication policy** lets editors or referees request data, programs, and computational details **at the review stage**, every number in a table must be reproducible from a script the day you submit. Build the analysis to be auditable, not just presentable.

## Robustness expected

- Alternative specifications, samples, and functional forms in an extensive online appendix
- Sensitivity to outliers, winsorization, and index/aggregation choices
- Placebo / falsification outcomes that should not move
- Spillover/SUTVA checks where treatment may leak across units (common in village-level interventions)

## Anti-patterns

- Standard errors not clustered at the design level; ignoring few-cluster bias
- Silently dropping attritors or trimming the sample without reporting it
- A wall of unadjusted subgroup interactions presented as confirmatory
- Effects reported only in raw units, leaving importance unclear
- Tables that cannot be regenerated from the submitted code

## Output format

```
【Estimator】+ why it fits the design
【Inference】clustering level / few-cluster method / MHT
【Attrition】rate, differential? bounds?
【Measurement】key variable construction + error handling
【Heterogeneity】pre-specified vs exploratory
【Robustness done / missing】[...]
【Reproducible from code today?】[Y/N]
【Next step】jde-tables-figures
```
