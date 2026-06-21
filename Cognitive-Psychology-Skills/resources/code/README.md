# Code Kit — *Cognitive Psychology* (model-driven cognitive science)

A small, **runnable R** kit for the analysis norms *Cognitive Psychology* (Elsevier) actually rewards:
**(generalized) linear mixed models** over crossed subject/item random effects, **formal model fitting
with principled comparison** (AIC/BIC/Bayes factors), **parameter and model recovery**, **signal-
detection / drift-diffusion** decomposition of RT+accuracy, and **effect sizes with uncertainty** — all
regenerable from a seeded, fresh-session run. Copy a script, swap in your data, keep the seed.

This kit is **R-first by design** (R is the lingua franca of experimental cognition); it is *not* the
econometrics/Stata pipeline vendored into economics packs, because the venue's contribution is a
**fitted cognitive model**, not a causal-identification estimate.

## Files

| File | Purpose | Key packages |
|------|---------|--------------|
| `R/00_setup.R` | Packages, fixed seed, and a synthetic **trial-level** dataset (subjects × items × condition, RT + accuracy) so every other script runs standalone | base, optional `lme4` |
| `R/01_mixed_models.R` | Log-RT **LMM** and accuracy **GLMM** (binomial) with a **maximal** random-effects structure; condition contrasts (`emmeans`) and standardized effect sizes (`effectsize`) | `lme4`, `lmerTest`, `emmeans`, `effectsize` |
| `R/02_model_comparison_recovery.R` | Maximum-likelihood fit of two candidate cognitive models, **AIC/BIC + BIC-approx Bayes factor**, then a **parameter-recovery** loop and a **model-recovery** confusion matrix | base `optim`, `stats` |
| `R/03_signal_detection_ddm.R` | **SDT** (d′, criterion) from hits/false-alarms with log-linear correction, and **EZ-diffusion** recovery of drift / boundary / non-decision time from RT+accuracy | base, `stats` |
| `R/04_bayes_and_reproducibility.R` | Hierarchical-Bayes path (`brms`/Stan) for the same LMM, **LOO** model comparison, plus an outlier-exclusion **sensitivity** sweep and a `sessionInfo()` reproducibility footer | optional `brms`, `loo` |

## How to use

```r
# from this code/ directory, or set the path inside 00_setup.R
source("R/00_setup.R")            # builds `dat` (trial-level) + helpers, sets the seed
source("R/01_mixed_models.R")     # the workhorse GLMM analysis
source("R/02_model_comparison_recovery.R")
source("R/03_signal_detection_ddm.R")
# source("R/04_bayes_and_reproducibility.R")   # needs brms/Stan; heavier
```

Scripts guard optional packages with `requireNamespace()` and fall back to base-R equivalents where a
package is absent, so the core (`00`–`03`) runs on a stock R install. **All five scripts were executed
end-to-end on R 4.5.2 (2026-06)** with `lme4`, `lmerTest`, `emmeans`, `effectsize`, and `brms`+`rstan`+
`loo` installed (the `04` model converged: Rhat ≈ 1.00, all Pareto-k good); `00`/`02`/`03` also run on a
stock base-R install via the guards.

## Mapping to the skills

- `R/01`, `R/02`, `R/03` operationalize [`../../skills/cogpsych-data-analysis/SKILL.md`](../../skills/cogpsych-data-analysis/SKILL.md) — fit, compare, recover.
- `R/02` recovery loops back the recovery demand from `cogpsych-study-design` (power lives there as design, here as model identifiability).
- `R/04` and the seed/`sessionInfo()` discipline serve [`../../skills/cogpsych-open-science-and-transparency/SKILL.md`](../../skills/cogpsych-open-science-and-transparency/SKILL.md).
- Production fitting frameworks (Stan, JAGS, PyMC, `rtdists`/`RWiener`, `hddm`) are catalogued in [`../external_tools.md`](../external_tools.md).

> Synthetic data only — no fabricated empirical findings. The kit shows *how* to fit, compare, recover,
> and report; the science is yours. Verify version-sensitive package options against current docs.
