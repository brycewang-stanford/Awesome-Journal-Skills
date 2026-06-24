---
name: joap-data-analysis
description: Use when analyzing and reporting results for a Journal of Applied Psychology (JAP) manuscript using SEM, multilevel (HLM) models, mediation/moderation, or meta-analysis. JAP requires effect sizes with confidence intervals, model-based indirect effects with bootstrap CIs, fit indices, full disclosure, and a clean confirmatory/exploratory split. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (joap-data-analysis)

JAP analyses must be **model-appropriate, fully reported, and reproducible**. The house toolkit is
**SEM/CFA**, **multilevel (HLM) models**, **mediation and moderation** with proper inference, and
**meta-analysis**. The journal expects **effect sizes with confidence intervals**, **fit indices**,
**bootstrap CIs for indirect effects**, full disclosure of how data were handled, and a clean
**confirmatory vs. exploratory** separation, with data and code shareable under TOP.

## When to trigger

- Specifying and reporting the main and supporting analyses
- A reviewer asked for fit indices, indirect-effect CIs, robustness, or disclosure
- Reconciling preregistered analyses with exploratory follow-ups
- Preparing analysis scripts and a data/codebook for deposit

## Reporting norms JAP expects

1. **Measurement before structure.** Report the measurement model (CFA fit: χ²/df, CFI, TLI, RMSEA,
   SRMR) and reliability/AVE before interpreting the structural model; report measurement invariance
   when comparing groups or waves.
2. **Effect sizes + uncertainty.** Give standardized and/or unstandardized estimates **with confidence
   intervals** for key paths — not just p-values and stars.
3. **Mediation done right.** Report the **indirect effect with a bootstrap (or Monte Carlo) CI** (not
   only the Baron-Kenny steps or a Sobel z); for multilevel mediation use the appropriate (e.g.,
   1-1-1, 2-1-1, 2-2-1) decomposition and within/between separation.
4. **Multilevel correctly.** Report ICC(1)/ICC(2), center predictors appropriately (group-mean vs
   grand-mean), model random effects, and justify the estimator; do not run OLS on nested data.
5. **Full disclosure.** Report how sample size was determined, **all** exclusions (careless responding,
   attrition) and reasons, all conditions, and all measures. Label confirmatory vs. exploratory.
6. **Meta-analysis (if applicable).** Report the model (random vs fixed), heterogeneity (Q, I²),
   artifact corrections, publication-bias checks, and a transparent coding protocol.
7. **Reproducibility.** Provide scripts and a codebook; results should regenerate from shared data in a
   fresh session (see `joap-open-science-and-transparency`).

## Worked micro-example (illustrative numbers)

The servant-leadership package: a multilevel mediation in the field and a causal test in the lab.

```
Measurement model (field, N = 612 in 74 teams)
  CFA: χ²/df = 2.1, CFI = .96, TLI = .95, RMSEA = .045, SRMR = .04
  Reliabilities ω: leadership .91, safety .88, performance .87
  Aggregation: ICC(1) = .16, ICC(2) = .77, r_wg(j) = .85 → team-level OK
Confirmatory (preregistered) — multilevel mediation (2-2-2)
  a (leadership→safety) = .42 [.27, .57]; b (safety→performance) = .31 [.14, .48]
  Indirect = .13, 95% Monte Carlo CI [.05, .23] → mediation supported
  Direct (leadership→performance | safety) = .09 [-.06, .24], ns
Confirmatory (preregistered) — lab experiment (causal leg)
  Servant vs control on safety: d = 0.46, 95% CI [0.21, 0.71]
  H3 boundary: interaction with interdependence, ΔR² = .03, CI excludes 0
Exploratory (labeled): voice as a serial L1 mediator surfaced post hoc;
  reported as exploratory, flagged for confirmation in future work.
```

Why this passes JAP scrutiny: the measurement model is reported before structure; the indirect effect
carries a bootstrap/Monte Carlo CI; nesting is modeled and aggregation justified; the experimental leg
supplies causal warrant; and the post hoc serial path is honestly demoted to exploratory.

## Analysis-stage reviewer pushback and the venue fix

| Reviewer pushback | What it signals | JAP fix |
|-------------------|-----------------|---------|
| "Mediation by Sobel/steps only" | outdated inference | report indirect effect + bootstrap/Monte Carlo CI |
| "OLS on nested data" | dependence ignored | multilevel model; report ICC, centering, random effects |
| "No fit indices / measurement model" | construct validity unchecked | report CFA fit + reliability before structure |
| "Which exclusions were preregistered?" | forking-paths concern | disclosure table: rule, count, preregistered vs post hoc, result with/without |
| "Is this confirmatory?" | HARKing concern | point to the preregistration; relabel post hoc analyses exploratory |
| "Reviewer 2 couldn't rerun your code" | reproducibility gate | ship a fresh-session run log (see open-science skill) |

## Calibration anchors

- Report measurement before structure: a beautiful path model on a misfitting measurement model
  convinces no JAP reviewer.
- Prefer estimation language with CIs to dichotomous "significant/not"; bare p-value sentences read as
  pre-reform.
- For mediation and cross-level effects, the *interval on the carrying effect* is the result — design
  and report so that interval is defensible.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAP is organizational psychology — multilevel survey/field data and experiments; cluster at the right level and apply mediation/moderation discipline.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the supplement. See
the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- p-values and stars with no effect size, CI, or fit indices
- Mediation claimed via Baron-Kenny steps or Sobel z without a bootstrap/Monte Carlo CI
- Ignoring nesting (OLS on multilevel data) or aggregating without ICC/r_wg justification
- Selectively reporting conditions, measures, or exclusions (undisclosed flexibility)
- HARKing exploratory findings into confirmatory hypotheses
- Code that does not reproduce the reported numbers

## Output format

```
【Measurement model】CFA fit + reliability + invariance reported? [Y/N]
【Main result】effect size(s) + CI(s) + meaning
【Mediation/multilevel】indirect-effect bootstrap/Monte Carlo CI; nesting modeled? [Y/N/NA]
【Disclosure】N-determination + all exclusions + all conditions + all measures? [Y/N]
【Confirmatory vs exploratory】clearly separated? [Y/N]
【Reproducible】scripts + codebook + fresh-session check? [Y/N]
【Next】joap-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Mplus, `lavaan`, `lme4`/`nlme`, `psych`, `metafor`/`metaSEM`, bootstrap/Monte Carlo tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — statistical and disclosure requirements
