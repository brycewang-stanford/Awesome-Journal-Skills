---
name: jmf-data-analysis
description: Use when executing and reporting the analysis for a Journal of Marriage and Family (JMF) manuscript so it survives expert double-blind review — honest uncertainty, robustness, attention to selection and non-independence, and correct handling of complex-survey, longitudinal, and dyadic data. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (jmf-data-analysis)

JMF reviewers are methodologically sophisticated and family data are tricky: complex-survey weights,
panel attrition, missingness, and the non-independence of partners and family members all bite. This
skill covers execution and reporting norms; design decisions live in `jmf-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, selection checks, or alternative specifications
- Reconciling preregistered vs. exploratory analyses
- Making the analysis reproducible before deposit

## Analysis norms JMF expects

1. **Report uncertainty and magnitude honestly.** Confidence intervals and effect sizes (not stars
   alone); state the substantive size in family terms (months to divorce, percentage-point change in a
   transition, points on a relationship-quality scale).
2. **Address selection explicitly.** In observational family research, show what survives within-person/
   couple fixed effects, sibling comparisons, propensity adjustment + sensitivity, or honest scoping.
3. **Respect the data structure.** Apply **complex-survey** weights/clusters/strata for PSID, NSFG,
   Add Health, etc.; cluster or model **non-independence** for dyads and families; use survival models
   for time-to-event outcomes.
4. **Handle missingness principled-ly.** Multiple imputation or FIML rather than listwise deletion;
   report the missing-data mechanism assumption and the share imputed; probe panel **attrition**.
5. **Robustness that probes, not decorates.** Alternative measures, samples, estimators, and
   specifications that could *break* the result — and what you learn.
6. **Heterogeneity with discipline.** Pre-specify subgroups (by gender, family structure, race/
   ethnicity, cohort) where possible; correct for multiple comparisons; do not mine interactions.

## Family-data specifics
- Report the analytic sample and how it was derived from the full dataset (eligibility, attrition,
  missingness) — reviewers will check the funnel.
- For dyadic models, report actor and partner effects and whether dyads are distinguishable.
- For growth/event-history models, report the time metric, censoring, and competing risks.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for imputation, bootstrap, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers in the manuscript matched to script outputs.

## What JMF referees check in a results section

| Check | Passes review | Triggers a revision request |
|-------|---------------|------------------------------|
| Survey design | PSID/NSFG/Add Health weights, strata, clusters applied | Unweighted estimates from a complex sample |
| Non-independence | Dyads/families clustered or modeled (APIM, multilevel) | Partners treated as independent rows |
| Selection | Within-couple FE, sibling, PSM+sensitivity, or honest scoping | "Effect of" language on raw associations |
| Magnitude | Effect in family units (months to divorce) + CI | Stars only, no substantive size |

For the flagship journal of the National Council on Family Relations, the fastest desk-reject-adjacent
outcome is an analysis that ignores the survey design or the dependence built into couple and family data.

## Worked micro-example (illustrative)

A divorce-timing study uses discrete-time event-history on national-panel marriages. Numbers illustrative.

- *Naive (flagged):* a logit pooling person-years with no clustering reports OR = 1.40 for job loss on
  divorce, stars only.
- *JMF-grade:* a discrete-time hazard with survey weights and SEs clustered on the couple; job loss raises
  the divorce hazard ~28% (HR 1.28, 95% CI 1.09–1.50), shifting modeled median time to divorce earlier by
  ~1.6 years. Selection probe: within-couple fixed effects leave a smaller HR ≈ 1.18, so it is not purely
  sorting. Competing risks are modeled and the sample funnel reported.

## Referee-pushback patterns and the venue-specific fix

- *"Dyadic dependence ignored."* Re-estimate with members nested in couples; for distinguishable dyads
  report actor and partner effects separately and test equality.
- *"Selection into family transitions."* Add a within-unit (couple/sibling) comparison or a sensitivity
  bound, and soften causal language to match.
- *"Survey design ignored."* Apply the dataset's weight/strata/PSU variables and report design-based SEs.

*Calibration (hedged):* for family panels (PSID, Fragile Families, Add Health, NSFG), design-based inference
and principled missing-data handling are defaults; confirm dataset-specific guidance with provider
documentation.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMF is quantitative family demography/sociology; emphasize identification, selection, and decomposition methods.

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

- Stars-only tables with no effect sizes, intervals, or substantive interpretation
- Ignoring survey weights/design or treating dyad members as independent
- Listwise deletion that silently changes the sample; ignoring attrition
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- A results section whose numbers the code cannot reproduce

## Output format

```
【Main estimate】magnitude + interval + substantive (family) meaning
【Selection check】(per research-design) result
【Data structure】weights/clusters/dyad-family non-independence handled? [Y/N]
【Missing data】MI/FIML + attrition probed? [Y/N]
【Robustness】specs that could break it → what held
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】jmf-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, survey, dyadic, survival, and imputation packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — replication-detail and data expectations
