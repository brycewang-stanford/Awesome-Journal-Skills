---
name: eursr-data-analysis
description: Use when executing and reporting the analysis for a European Sociological Review (ESR) manuscript so it survives expert double-blind review — correct multilevel and longitudinal modeling, honest uncertainty, robustness, and small-macro-N inference on comparative survey or register data. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (eursr-data-analysis)

ESR reviewers are quantitatively demanding and comparative by instinct. Whether your evidence is
multilevel coefficients, hazard ratios, growth trajectories, or decompositions, the analysis must be
transparent, correctly specified for the data structure, and reproducible. Design decisions live in
`eursr-research-design`; the replication package lives in `eursr-transparency-and-data`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, the right clustering/level, heterogeneity, or alternative specifications
- Reporting cross-level interactions or country-level effects from few clusters
- Making the analysis reproducible before depositing materials

## Analysis norms ESR expects

1. **Report uncertainty and magnitude**, not just significance — confidence intervals and substantive
   effect sizes (predicted probabilities, marginal effects), respecting survey design (weights,
   clustering, strata; design-based SEs).
2. **Model the data structure correctly.** Multilevel data → random effects or cluster-robust /
   country fixed effects with the *right* level; panel data → within estimators matched to the quantity;
   durations → event-history with correct risk set and time scale.
3. **Small macro-N honesty.** With ~20-30 countries, country-level SEs are fragile: too few clusters
   bias cluster-robust SEs, and a single cross-level interaction can rest on a handful of higher-level
   units. Use df-appropriate methods (e.g., Satterthwaite/Kenward-Roger df, wild cluster bootstrap, or
   a Bayesian multilevel model) and do not over-interpret macro coefficients.
4. **Robustness that probes, not decorates.** Alternative measures, samples, codings, and estimators
   that could *break* the result; report what you learn, not just that it "holds."
5. **Heterogeneity with discipline.** Pre-specify or justify subgroups and cross-level interactions;
   adjust for multiple comparisons; do not mine an interaction and theorize it post hoc.
6. **Measurement.** Validate latent constructs (CFA, reliability) and, for comparison, report the
   invariance level reached and what it licenses.

## Reproducibility while you work
- One **master script** regenerates every table/figure from the (constructed) data.
- **Set and report seeds** for any stochastic step (imputation, bootstrap, MCMC).
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep the harmonization/recoding code (ISCED/CASMIN, ISCO/ISEI/EGP) auditable — reviewers check it.

## What an ESR analyst-reviewer is checking

| Reviewer probe | Clears the ESR bar | Triggers a revision flag |
|----------------|--------------------|---------------------------|
| "Right level / clustering?" | SEs at the correct level; df-aware macro inference | individual SEs on a country-level claim |
| "Just a significant coefficient?" | marginal effect + interval tied to the mechanism | stars-only, no interpretation |
| "Few clusters handled?" | wild bootstrap / Bayesian / df correction | naive cluster SEs on ~20 countries |
| "Measures comparable?" | invariance reported; partial invariance bounded | latent comparison with no invariance test |
| "Heterogeneity real or mined?" | pre-specified / MHT-adjusted | one fished cross-level interaction |

## Worked micro-example (illustrative numbers)

A hypothetical ESR study links active labor-market policy (macro) to unemployment scarring (micro)
across 24 countries with harmonized panel data.

```
Main effect: a past spell lowers later wages 6.1% (95% CI 4.0–8.2), within-person fixed effects
Cross-level interaction: scar is 3.4 pp smaller per 1 SD of activation spending (CI 1.1–5.7) —
  the macro × micro hypothesis from eursr-theory-building
Few-cluster inference: wild cluster bootstrap (countries), p = 0.012; macro claim kept modest (24 df)
Robustness: holds dropping any one country (leave-one-out), and under register- vs survey-measured wages
Reproducible: one master script, seed = 2026, renv.lock pinned; harmonization code archived
```

The interval carries the micro claim, the cross-level term names the portable mechanism, and the
few-cluster inference is handled honestly rather than asserted.

## Referee pushback → ESR-specific fix

- *"Your country-level SEs are too optimistic."* → Re-estimate with a wild cluster bootstrap or a
  Bayesian multilevel model; report the df and temper the macro claim.
- *"Robustness agrees by construction."* → Add a spec that could break it (alternative harmonization,
  leave-one-country-out, placebo period) and report what you learned.
- *"Significant but does it matter?"* → Give a predicted-probability or marginal-effect scenario and
  name what changes for the comparative debate.

## Calibration anchors

- **Get the level right or nothing else counts.** ESR's signature error is mismatched SEs/clustering on
  a multilevel or comparative claim — fix the variance structure first.
- **Few clusters demand humility.** ~20-30 countries cannot support strong macro-level inference with
  naive SEs; df-aware methods and modest claims are expected.
- **Magnitude over significance.** Report marginal effects and intervals a comparative reader can
  interpret, not stars.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ESR is comparative quantitative sociology; cross-country panels with confounded institutions — foreground fixed effects and clustering.

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

- Individual-level SEs on a country-level coefficient; naive cluster SEs on ~20 countries
- Stars-only tables with no effect sizes or intervals; ignoring survey weights
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / HARKing an exploratory cross-level interaction into a hypothesis
- Latent cross-national comparisons reported without an invariance check

## Output format

```
【Main result】marginal effect + interval
【Data structure handled】level / clustering / panel estimator correct? [Y/N]
【Cross-level / macro inference】few-cluster method + df honest? [Y/N]
【Robustness】what held (incl. leave-one-country-out)
【Reproducible】master script + seeds + pinned versions + harmonization code? [Y/N]
【Next】eursr-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — multilevel, event-history, SEM, and decomposition packages
- [`../../resources/code/`](../../resources/code/) — reproducible estimation skeleton (DiD/IV/RDD/DML + robustness)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ESR replication and reporting norms
