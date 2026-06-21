# Code Kit — *Journal of Applied Psychology* (I-O psychology)

A small, **runnable R** kit for the measurement-and-multilevel norms *JAP* (APA's I-O flagship) holds
manuscripts to: **CFA + measurement invariance**, **reliability and AVE**, **common-method-variance
(CMV) checks**, **aggregation diagnostics** (ICC1/ICC2/r_wg) before you move a construct to the team
level, **multilevel models with within/between separation**, **model-based mediation with bootstrap /
Monte-Carlo indirect-effect CIs**, and **psychometric meta-analysis with artifact corrections**. Every
result reports an **effect size with a CI**, under a clean confirmatory/exploratory split.

R-first by design (R + Mplus are the field's workhorses); this is *not* an econometrics pipeline,
because JAP's contribution is a **measured, multilevel theoretical claim**, not a causal-identification
estimate.

## Files

| File | Purpose | Key packages |
|------|---------|--------------|
| `R/00_setup.R` | Packages, fixed seed, and synthetic **nested** data: employees in teams, multi-indicator latent X/M/Y, plus a small effect-size meta table — so every script runs standalone | base, optional `lme4` |
| `R/01_measurement_cfa_invariance.R` | **CFA** measurement model, **omega / composite reliability / AVE**, and configural→metric→scalar **measurement invariance**; base-R Cronbach's α fallback runs without `lavaan` | `lavaan`, `semTools`, `psych` |
| `R/02_aggregation_diagnostics.R` | **ICC(1)**, **ICC(2)**, and **r_wg(j)** to justify (or refuse) aggregating an individual measure to the team level | base, `lme4` |
| `R/03_multilevel_mediation.R` | Random-intercept/slope **multilevel model** (group-mean centering for within/between), then **1-1-1 mediation** with a **Monte-Carlo indirect-effect CI** | `lme4` |
| `R/04_psychometric_meta.R` | **Psychometric (Hunter-Schmidt-style) meta-analysis**: correct correlations for **unreliability**, pool with random effects, and report **80% credibility** + **heterogeneity** | `metafor` |

## How to use

```r
source("R/00_setup.R")                       # builds nested `dat`, latent indicators, `meta_tab`
source("R/02_aggregation_diagnostics.R")     # justify team-level aggregation FIRST
source("R/03_multilevel_mediation.R")        # multilevel mediation with bootstrap/MC CI
source("R/04_psychometric_meta.R")           # artifact-corrected meta-analysis
# source("R/01_measurement_cfa_invariance.R")# CFA/invariance; install.packages("lavaan")
```

Scripts guard optional packages with `requireNamespace()`. **All five scripts were executed end-to-end
on R 4.5.2 (2026-06)** with `lme4`, `lavaan`, `semTools`, and `metafor` installed (CFA fit CFI = 1.00,
RMSEA = 0.00; invariance χ²-diff n.s.); `00`/`02`/`03`/`04` also run on a stock base-R + `lme4`/`metafor`
install, and `01`'s base-R Cronbach's α path runs without `lavaan`.

## Mapping to the skills

- `R/01` serves [`../../skills/joap-data-analysis/SKILL.md`](../../skills/joap-data-analysis/SKILL.md) and the measurement bar in `joap-study-design` — establish construct validity *before* substantive tests.
- `R/02` enforces the aggregation justification JAP referees demand before any team-level claim.
- `R/03` operationalizes JAP's requirement for **model-based indirect effects with CIs**, not causal-steps p-values.
- `R/04` supports review-grade synthesis and the artifact-correction logic central to I-O meta-analysis.
- Mplus, `psychmeta`, `simr`, and CMV remedies are catalogued in [`../external_tools.md`](../external_tools.md).

> Synthetic data only — no fabricated findings. The kit shows *how* to validate, aggregate, mediate, and
> synthesize; the science is yours. Verify version-sensitive options against current package docs.
