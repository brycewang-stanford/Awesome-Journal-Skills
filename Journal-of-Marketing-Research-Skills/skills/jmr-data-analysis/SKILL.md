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

## Result-to-claim ledger

For each table or study, write one ledger row before drafting results:

| Result | Claim it supports | Required statistic | Practical meaning |
| --- | --- | --- | --- |
| Main treatment or model estimate | What marketing decision, mechanism, or theory point changes? | Exact p-value, standard error, CI/effect size | Unit change, percentage lift, WTP/profit/customer impact |
| Mediation/process result | Which mechanism is supported and which rival is weaker? | Indirect effect with CI; moderation where relevant | Why the process matters for managers or theory |
| Robustness / alternative model | Which threat is reduced? | Same reporting discipline as main result | Whether conclusion changes in magnitude or direction |
| Counterfactual / simulation | What marketplace decision follows? | Parameter uncertainty and sensitivity | Managerial action implied by the estimate |

If the practical-meaning column is empty, the result is not ready for a JMR results paragraph. JMR reviewers expect precision, but they also expect a marketing payoff.

## Replication & robustness (AMA transparency policy)

- Provide enough detail (in-text, **Web Appendix**, or online supplements) for a reasonably trained researcher to replicate; be ready to share code, instruments/stimuli, and materials on request, and to provide data/materials before final acceptance.
- Put robustness — alternative specifications, subsamples, alternative measures, additional studies — in the **'W'-prefixed Web Appendix**, keeping the print paper within 50 pages.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMR mixes experiments, structural models, and quasi-experiments; the chain below serves the experimental and reduced-form lanes, while structural demand estimation uses its own toolkit.

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
## Anti-patterns

- Reporting "p < .05" or asterisks instead of exact three-digit p-values.
- Tables with no standard errors; significance without effect sizes.
- Causal-steps (Baron-Kenny) mediation instead of bootstrapped indirect effects.
- Ignoring clustering / non-independence; a weak or untested instrument.
- A leading zero before the decimal, or more than three decimal places.
- Results paragraphs that report significance but no practical magnitude or marketing interpretation.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric
[Estimator] matches design? SE clustering ...
[Exact stats] p three-digit / SEs / effect sizes: pass/fix
[AMA number style] no leading zero, <= 3 decimals: pass/fix
[Identification or process] diagnostics reported
[Result-to-claim ledger] claim + practical meaning complete
[Replication] Web Appendix + code/materials ready
[Next skill] jmr-contribution-framing
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
