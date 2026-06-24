---
name: demog-data-analysis
description: Use when executing and reporting the analysis for a Demography (PAA / Duke University Press) manuscript so it survives expert, double-blind review — correct rate construction, honest uncertainty, and demographic methods done right (life tables, decomposition, event history, age-period-cohort). Guides analysis norms; it does not fabricate results.
---

# Data Analysis (demog-data-analysis)

Demography reviewers are expert demographers and the journal expects **reproducible code** behind the
results (see `demog-data-and-reproducibility`). Analyze as if a methodologist will re-derive your rates
and re-run your decomposition — because they may. This skill covers execution and reporting norms;
method choice lives in `demog-research-design`.

## When to trigger

- Constructing rates and life tables; building the results section
- Running a decomposition, event-history, APC, or projection analysis
- A reviewer asked for robustness, sensitivity, or alternative specifications
- Making the analysis reproducible before deposit

## Analysis norms Demography expects

1. **Get the denominators right.** Exposure (person-years), the correct base population, and
   age/period alignment are where demographic analyses live or die. Document how rates were built.
2. **Report uncertainty honestly.** Confidence/credible intervals for rates, life-expectancy
   contributions, and derived quantities — not just point estimates or stars. Bootstrap or delta-method
   intervals for decomposition components and life-table functions.
3. **Decomposition with clear components.** State precisely what each component (rate vs. composition,
   age contribution, factor) represents; ensure components sum to the total being explained.
4. **APC discipline.** Be explicit about the identification problem; report results under the stated
   constraint and show sensitivity to plausible alternatives — never imply a unique decomposition.
5. **Survival/event-history rigor.** Check proportional hazards; handle censoring, truncation, and
   competing risks correctly; report on the right time scale (age, duration, period).
6. **Right inference for the data.** Survey weights and complex-design variance where applicable;
   cluster at the appropriate level; small-sample corrections when groups are few.

## Demographic computation specifics
- Document data version/vintage (e.g., HMD/HFD release), harmonization steps, and any smoothing/
  graduation applied to rates.
- For microsimulation/projection: report seeds, number of runs, and convergence; show sensitivity to
  the key transition-rate and base-population assumptions.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table, figure, life table, and decomposition from the
  (raw or constructed) data.
- **Set and report seeds** for bootstrap, simulation, and microsimulation.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers in the manuscript matched to script outputs (Demography expects runnable,
  commented code — see `demog-data-and-reproducibility`).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Demography is formal + empirical demography; the causal chain serves its reduced-form lane, while formal demographic modeling uses its own tools — decomposition (`oaxaca` / `gelbach`) is often central.

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

- Mismatched numerator/denominator or wrong exposure (the classic demographic error)
- Point estimates of life expectancy or decomposition components with no uncertainty
- An APC model presented as the uniquely correct partition
- Ignoring censoring/competing risks in survival analysis
- A results section whose rates and decompositions the code cannot reproduce


## Evidence pass for Demography

Run this as a concrete capability pass. First lock the demographic process, data source, time scale, selection/migration/mortality issue, and uncertainty; then test whether the manuscript addresses population-science reviewers who inspect demographic process, measurement, cohort/period logic, and population validity.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Population and Development Review for policy synthesis, JMF for family process, Social Forces for broader sociology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Main quantity】rate / e0 / decomposition / hazard + magnitude + interval
【Exposure / denominator check】correctly constructed? [Y/N]
【Decomposition】components defined + sum to total? [Y/N/NA]
【APC】identifying constraint stated + sensitivity shown? [Y/N/NA]
【Inference】weights/clustering/competing risks handled? [Y/N]
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】demog-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — life-table, decomposition, survival, APC, and simulation packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and reproducible-code expectations
