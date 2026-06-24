---
name: jams-data-analysis
description: Use when running and reporting the analysis for a Journal of the Academy of Marketing Science (JAMS) manuscript — selecting the estimator that matches the design (SEM/PLS, HLM, regression/econometrics, experiments, meta-analysis), reporting effect sizes and uncertainty, and translating estimates into managerial magnitudes. Executes and reports; jams-methods designs the study and jams-contribution-framing states the payoff.
---

# Data Analysis & Reporting (jams-data-analysis)

## When to trigger

- Data are collected and it is time to estimate and report
- You are unsure whether the estimator matches the design or the data structure
- A reviewer says "the analysis does not support the inference" or "report effect sizes"
- Significance is reported but the managerial magnitude is missing

## Choose the estimator that matches the design

| Design / claim | Estimator |
|---|---|
| Latent constructs + structural paths (survey) | Covariance-based **SEM** (Mplus / lavaan / AMOS); **PLS-SEM** when prediction or formative constructs dominate |
| Nested data (consumers in stores, firms in industries) | **HLM / multilevel** models; random intercepts/slopes; report ICC |
| Mediation (process) | Bootstrapped indirect effects (PROCESS / lavaan), **bias-corrected CIs**; report the indirect effect, not just Baron–Kenny steps |
| Moderation / moderated mediation | Interaction term + simple slopes; conditional indirect effects (index of moderated mediation) |
| Experiment (factorial) | ANOVA / regression; estimated marginal means; planned contrasts; effect sizes per cell |
| Panel / observational causal | FE / **DiD** (modern staggered estimators); cluster-robust SE |
| Endogenous marketing regressor | IV/2SLS or Gaussian-copula control function; report first stage / instrument strength |
| Discrete choice / demand | Logit/probit; random-coefficient (mixed) logit |
| Meta-analysis | Random-effects effect-size synthesis; moderator meta-regression; publication-bias diagnostics |

Match SE clustering to the sampling/assignment structure (participant, store, market, firm).

## JAMS reporting conventions

- **APA results style.** Report exact statistics (coefficients, SEs or *t*-values, CIs, exact *p* where shown). Avoid asterisk-only tables where the journal asks for precision; let the magnitude, not the star count, carry the result.
- **Effect sizes and uncertainty, always.** Standardized coefficients, *R²*/*f²*, η²/Cohen's *d*, or odds ratios as the model requires — significance without magnitude is not a JAMS result.
- **SEM reporting:** measurement model first (loadings, AVE, CR, discriminant validity), then the structural model (standardized paths, *R²* for endogenous constructs, overall fit: CFI, TLI, RMSEA, SRMR).
- **PLS reporting:** loadings/weights, CR, AVE, HTMT, *R²*, *Q²* (predictive relevance), and *f²*; bootstrap the path significances.

## Translate every result into a managerial magnitude

This is the JAMS-distinguishing step. For each headline result, write a ledger row before drafting the results paragraph:

| Result | Theory point it supports | Required statistic | Managerial magnitude |
|---|---|---|---|
| Main path / treatment effect | which hypothesis / mechanism is confirmed | std. coef. + CI / *d* | sales lift, share, CLV, margin, retention, brand-equity points |
| Mediation (process) | which mechanism carries the effect | indirect effect + bias-corrected CI | why the process matters for the decision |
| Moderation (contingency) | when the effect strengthens/reverses | interaction + simple slopes | the managerial guardrail / segmentation rule |
| Robustness / alternative model | which threat (CMV, endogeneity) is reduced | same discipline as the main result | whether the conclusion's direction/size holds |

If the managerial-magnitude column is empty, the result is not yet ready for a JAMS results section.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAMS is empirical marketing with much survey-based SEM; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Estimator matches design and data structure; SE clustering correct
- [ ] SEM: measurement model reported before structural; full fit indices given
- [ ] PLS: HTMT, *R²*, *Q²*, *f²* reported; paths bootstrapped
- [ ] Mediation via bootstrapped indirect effects with bias-corrected CIs
- [ ] Moderation: simple slopes + index of moderated mediation where relevant
- [ ] Effect sizes and uncertainty reported throughout (APA style)
- [ ] Every headline result has a managerial-magnitude translation
- [ ] Robustness addresses the design's specific threat (CMV / endogeneity / pre-trends)

## Robustness that targets the design's real threat

Generic robustness ("we also ran model B") rarely persuades JAMS reviewers; the robustness must answer the *specific* threat to the genre's inference:

- **Survey/SEM:** rule out CMV with a marker-variable / CFA-marker model and report whether paths survive; test an alternative measurement specification; show results hold on a holdout or second sample.
- **Secondary data:** placebo tests, alternative instruments, pre-trend/parallel-trends evidence, sensitivity to the identifying assumption, and alternative fixed-effect structures.
- **Experiment:** replication across stimuli/samples, a confound-ruling-out study, and a test of the alternative-mechanism account.
- **Meta-analysis:** sensitivity to coding decisions, trim-and-fill / PET-PEESE for publication bias, and influence diagnostics for outlier studies.

State, for each robustness check, *which threat it neutralizes* — a list of checks with no mapped threat reads as box-ticking.

## Anti-patterns

- Baron–Kenny causal-steps mediation instead of bootstrapped indirect effects
- Reporting fit indices but no standardized paths or *R²*
- Significance with no effect size and no managerial magnitude
- Ignoring nesting (consumers within stores) and clustering
- A weak/untested instrument, or endogeneity waved away
- Asterisk tables that hide the size of the effect
- Robustness checks listed with no statement of which threat each addresses

## Output format

```text
【Design】survey-SEM / PLS / HLM / experiment / panel-causal / choice / meta
【Estimator】matches design? SE clustering: [...]
【Measurement (if SEM/PLS)】AVE/CR/discriminant + fit/HTMT: pass/fix
【Effect sizes + uncertainty】reported (APA)? pass/fix
【Mediation/moderation】bootstrapped indirect / simple slopes: done?
【Managerial-magnitude ledger】every headline result translated? yes/fix
【Robustness】design-specific threat addressed: [...]
【Next skill】jams-contribution-framing
```
