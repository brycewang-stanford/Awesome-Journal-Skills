---
name: jole-data-analysis
description: Use when executing the empirical analysis for a Journal of Labor Economics (JOLE) manuscript — labor sample construction (CPS/ACS/registers), wage decompositions, standard errors, and robustness to labor norms, with replicability built in from the start. Operational guidance; pairs with jole-identification-strategy.
---

# Data Analysis (jole-data-analysis)

## When to trigger

- You are building the analysis sample from CPS/ACS/IPUMS, administrative, or register data
- You are running wage decompositions (Oaxaca / RIF) or AKM firm–worker models
- Standard errors, weighting, or robustness need to meet labor-referee expectations
- You want to make sure the empirical work will be replicable before you write it up

## Labor empirical norms at JOLE

JOLE publishes empirical / simulation / experimental labor papers **only if the data are documented and available for replication**, so build the analysis so it can be deposited later (data + programs + documentation) to the JOLE Dataverse (see jole-replication-and-data-policy). Beyond reproducibility, labor referees expect disciplined data work:

- **Sample construction is part of identification.** Document the universe, age/labor-force restrictions, top-coding handling, and how you treat zeros/imputed earnings (CPS allocation flags, ACS PUMS edits). Report sample sizes at each restriction.
- **Weights and design.** Use survey weights appropriately (CPS/ACS) and account for complex sampling; for registers, be explicit about coverage and linkage rules.
- **Earnings measures.** Be precise: hourly vs. weekly vs. annual; nominal vs. real (state the deflator); winsorizing/top-coding decisions and their sensitivity.
- **Standard errors.** Cluster at the level of the variation (often state or firm); use heteroskedasticity-robust SEs by default; wild-cluster bootstrap with few clusters; randomization inference for experiments.

## Common labor estimations (and their pitfalls)

- **Wage decompositions:** Blinder–Oaxaca for mean gaps; RIF / unconditional-quantile (`rifreg`) for distributional gaps. State the reference group and the index-number problem; do not over-interpret the "unexplained" component as discrimination without argument.
- **Two-way (AKM) firm–worker FE:** estimate on the connected set; correct **limited-mobility bias** (leave-out / KSS) before decomposing wage variance; report the share of movers.
- **Labor-supply elasticities:** be explicit about extensive vs. intensive margin, and about which elasticity (Marshallian/Hicksian/Frisch) is identified.
- **Returns to schooling/training:** distinguish OLS from IV/RDD estimates; report both and reconcile.
- **Event studies / DID:** use modern estimators on staggered timing (see jole-identification-strategy) and plot leads.

## Robustness a labor referee will ask for

- Alternative samples (age bands, full-time/part-time, with/without imputed earnings)
- Alternative SE clustering and few-cluster corrections
- Specification curve / leave-one-out on key controls or sub-populations
- Placebo outcomes and placebo timing/cutoffs
- Heterogeneity by the labor-relevant dimensions (gender, education, age, sector) where theory predicts it

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JOLE is labor economics — the home of clean identification; DiD/IV/RDD and selection corrections are the binding constraint.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample restrictions documented with counts at each step
- [ ] Earnings measure and deflator stated; top-coding/winsorizing sensitivity shown
- [ ] Survey weights / register coverage handled correctly
- [ ] SEs clustered at the variation level; few-cluster issues addressed
- [ ] Decompositions report reference group; AKM corrects limited-mobility bias
- [ ] Robustness covers samples, SEs, placebos, and theory-motivated heterogeneity
- [ ] Every table/figure regenerable from a master script (replicability built in)

## Anti-patterns

- Undocumented sample cuts that drive the result
- Ignoring CPS/ACS allocation flags and imputed-earnings issues
- Default i.i.d. SEs when variation is at the state/firm level
- Interpreting the Oaxaca "unexplained" gap as discrimination with no further argument
- Reporting AKM firm-effect dispersion without limited-mobility-bias correction
- Leaving reproducibility to the end instead of scripting it as you go

## Output format

```
【Data】source(s) + sample universe + restrictions (with counts):
【Earnings measure】hourly/weekly/annual, real/nominal, deflator:
【Estimator】OLS / Oaxaca / RIF / AKM / IV / DID:
【SEs】clustering level + few-cluster handling:
【Robustness done】[samples, SEs, placebos, heterogeneity]:
【Replicability】master script regenerates all exhibits? [Y/N]
【Next step】jole-contribution-framing or jole-tables-figures
```
