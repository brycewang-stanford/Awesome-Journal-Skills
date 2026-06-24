---
name: io-data-analysis
description: Use when executing and reporting the empirical analysis (or the formal-model results) for an International Organization (IO) manuscript so it survives expert double-blind IR review and IO's pre-publication verification. The IO editorial staff re-run quantitative analyses and check formal proofs before final acceptance, and IR data raise distinctive estimation problems (dyadic dependence, selection into treaties/alliances/conflict, gravity structure). Guides analysis and reporting; it does not fabricate results.
---

# Data Analysis (io-data-analysis)

Two facts shape how you analyze for IO. First, IO publishes **international-relations** work, so the
estimation problems are IR-specific — dyads are not independent, states select into treaties and wars,
trade follows a gravity structure, and many "variables" are estimated constructs. Second, IO's editorial
staff later **re-run your quantitative analyses and verify your formal proofs before final acceptance**
(see `io-transparency-and-data-policy`). This skill covers execution and reporting; identification choices
live in `io-research-design`.

## When to trigger

- Estimating the main international effect and supporting analyses; writing the results section
- A referee asked for robustness, heterogeneity by issue area, or an alternative estimator
- Deriving and presenting the results/comparative statics of a formal model
- Separating preregistered from exploratory analyses on a foreign-policy experiment

## IR-specific estimation concerns

- **Dyadic and network dependence.** Directed/undirected dyads share members, so observations are not
  independent. Use two-way or multiway clustering, dyadic-robust SEs, or latent-space/AME network models
  rather than naive OLS standard errors.
- **Selection at the international level.** States choose into alliances, treaties, IO membership, and
  conflict. Model or bound that selection; do not read a compliance correlation as an institutional effect.
- **Gravity and trade.** For bilateral flows, prefer PPML with high-dimensional fixed effects over
  log-linear OLS; handle zeros honestly.
- **Estimated regressors.** Ideal points, institutional-design indices, latent regime scores, and
  text-derived measures carry estimation uncertainty — propagate it rather than treating point estimates
  as observed data.
- **Few effective units.** With a small number of countries/IGOs as clusters, use wild-cluster bootstrap
  or randomization inference, not asymptotic clustered SEs.

## Reporting standards IO referees expect

1. **Substantive magnitude, not stars.** Give the size of the international effect with an interval and
   interpret it in IR terms (probability of conflict, change in trade, shift in compliance).
2. **Probing robustness.** Vary the operationalization of the international construct, the dyad/year
   sample, the estimator, and the fixed effects; report what *breaks* the result, not only what survives.
3. **Disciplined heterogeneity.** Pre-register or pre-state cuts by issue area, regime type, or region;
   adjust for multiple comparisons; never harvest one significant interaction and theorize it afterward.
4. **Construct validity.** Show the finding is not an artifact of one conflict coding, one alliance
   dataset, or one scaling decision; cross-walk to an alternative source where one exists.

## Formal-model results
- Present equilibrium results and comparative statics so a reader can map them to the empirics.
- Keep a **complete proof appendix** — IO staff verify proofs before final acceptance, so derivations
  must be checkable, not sketched.

## Verification-readiness (engineer it during analysis)
- A single driver script reproduces every reported number from the raw/constructed data in one run.
- Record seeds for every bootstrap, simulation, and randomization-inference step.
- Pin the toolchain (`renv.lock`, `requirements.txt`, logged `ssc`/`net install` lines) and the dataset
  versions (COW vX, V-Dem vY, UCDP release Z).
- The numbers printed in the manuscript must equal the script's output exactly — the IO re-run will compare them.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). International Organization is IR — country/dyad panels with difficult identification; foreground the source of variation and robustness to alternative explanations.

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

- Treating dyads as independent; ignoring selection into treaties/alliances/conflict
- Log-OLS on trade flows where zeros and heteroskedasticity bias the gravity estimates
- Plugging in estimated ideal points/indices as if measured without error
- Asymptotic clustered SEs with a handful of country clusters
- A formal section with results stated but proofs left incomplete (verification will stall)

## Output format

```
【Estimand】the international effect + how identified (per io-research-design)
【IR estimation】dyadic dependence / selection / gravity / few-cluster handled? [Y/N]
【Magnitude】effect size + interval + IR interpretation
【Robustness】which specs could break it → what held
【Heterogeneity】pre-stated by issue area/regime? MHT-adjusted?
【Formal proofs】complete + checkable appendix? [Y/N/NA]
【Verification-ready】one-run driver script, seeds, pinned data/toolchain? [Y/N]
【Next】io-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — dyadic/network/gravity estimation, few-cluster inference, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — verification of results and formal proofs before final acceptance
