---
name: rof-data-analysis
description: Use when auditing Review of Finance empirical or theoretical analysis: sample construction, identification, asset-pricing tests, corporate-finance variables, robustness, code reproducibility, and evidence that can satisfy top-three-finance-journal standards.
---

# Review of Finance Data Analysis

Use this when the finance result is not yet credible enough for RoF. Reopen the current
author guidelines and code-sharing policy before final submission.

## Audit

- Map every finance claim to a table, figure, model result, identification test, or
  robustness check.
- For empirical work, document sample construction, variable definitions, filters, winsorizing
  or trimming, identifiers, timing, and economic magnitudes.
- For theory work, connect assumptions to equilibrium, comparative statics, or pricing
  implications that a broad finance audience can evaluate.
- Use strong benchmarks: standard asset-pricing factors, corporate-finance controls, market
  microstructure alternatives, or banking/household-finance baselines as relevant.
- Prepare code and data documentation early; RoF publication is conditional on receiving
  replication programs when the policy applies.

## Finance-result stress test

For each headline result, record:

```text
Result | Economic magnitude | Identification/model threat | Benchmark | Replication file
```

Then ask whether the claim would survive a top-three-finance referee:

- Does the magnitude matter economically, not only statistically?
- Is the benchmark the right one for asset pricing, corporate finance, banking, household finance, or
  market microstructure?
- Are timing, sample filters, and variable construction strong enough to rule out mechanical effects?
- For theory, do assumptions generate finance implications rather than only mathematical existence?
- Can the code package reproduce the exact result and the robustness check that protects it?

If the answer is weak, repair the analysis before rewriting the introduction.

## European and international data discipline

RoF's EFA readership expects cross-market evidence handled with the same care US-only
papers give CRSP. Known traps an RoF referee will catch:

- Datastream/Refinitiv equity returns: remove padded post-delisting observations, stale
  repeated prices, and non-trading-day zeros; report screen-by-screen sample counts.
- Delisting and survivorship: merge dead-firm lists back into Datastream samples and
  delisting returns into CRSP samples; a performance result built on survivors only is a
  mechanical effect, not a finding.
- Bankscope/Orbis (Bureau van Dijk): consolidated and unconsolidated statements duplicate
  the same banking groups — filter on consolidation codes; record the database vintage,
  because BvD overwrites history and a later re-pull will not rebuild your sample.
- Currency and fiscal timing: convert at observation-date exchange rates; align
  heterogeneous fiscal-year ends; lag accounting data enough to rule out look-ahead.
- ECB SDW, Eurostat, and national-supervisor series: store exact series codes and download
  dates; revisions silently change merged regressors.

## Estimation defaults an RoF referee assumes

| Setting | Expected default | Objection if absent |
|---|---|---|
| Firm/bank panel | firm + time FE; cluster by firm, two-way when shocks are common | "standard errors understated" |
| Fama–MacBeth | Newey–West lags matched to horizon; Shanken correction | errors-in-variables attack |
| Portfolio sorts | value-weighted headline plus equal-weighted check; microcap screen | "driven by tiny illiquid stocks" |
| Staggered adoption | heterogeneity-robust DID alongside TWFE | negative-weights critique |
| Cross-country panel | country-by-year FE or equivalent; cluster at country | "one country's shock in disguise" |
| Anomaly/factor claim | multiple-testing discipline; international or out-of-sample split | data-snooping objection |

Put one defining specification in the body and route the grid of variants to the internet
appendix — RoF editors prize clean identification and economic magnitudes over
kitchen-sink regressions.

## Worked vignette — a euro-area bank-margin paper

Illustrative numbers only. The headline: after the 2014 negative-policy-rate cut,
high-deposit banks lowered lending margins 28 bp more than low-deposit banks; sample of
412 euro-area banks from Bankscope, 2010–2019.

- Magnitude: 28 bp on a 180 bp mean margin is roughly 16% — state it that way, not as a
  t-statistic.
- Mechanical check: consolidation duplicates double-count the largest groups; rerun on
  unconsolidated statements. If 28 bp falls to 9 bp, the result is a filtering artifact.
- Benchmark: contrast with matched non-euro banks to separate the negative-rate channel
  from the post-crisis trend; that contrast belongs in the body.
- Replication hook: the Bankscope extract cannot ship; queue the pseudo-dataset and run
  logs now (see `rof-replication-and-data-policy`).

## Pipeline discipline from raw pull to exhibit

One reproducible path, because RoF can hold publication until programs arrive:

```text
raw/        immutable vendor pulls (Datastream, Bankscope, CRSP), dated
build/      cleaning scripts: screens, delisting merges, winsorize 1/99
analysis/   one numbered script per manuscript table or figure
out/        exhibits regenerated end-to-end by run_all; diffs reviewed
```

- Winsorize or trim ratio variables and state the percentile in every table note.
- Fix seeds for any bootstrap or simulation inference and log them.
- Maintain a variable dictionary mapping each manuscript symbol to its construction line.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Review of Finance is the EFA flagship — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Analysis readiness] strong / adequate / weak
[Claim -> evidence] <claim: table, figure, model, or robustness>
[Top-three-standard gap] <one issue>
[Replication blocker] <data, code, pseudo-data, or logs>
[Next analysis] <single task>
```
