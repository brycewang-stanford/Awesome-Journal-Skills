---
name: revacc-data-analysis
description: Use when running and reporting the empirical analysis for a Review of Accounting Studies (RAST) manuscript — standard-error clustering, executing the identification, validating accounting constructs, and the robustness battery referees expect, plus the data provenance trail. Executes and reports; it does not choose the identification strategy (revacc-methods) or frame the contribution (revacc-contribution-framing).
---

# Data Analysis & Robustness (revacc-data-analysis)

## When to trigger

- Data are built and it is time to estimate and report
- You are unsure how to cluster standard errors for your accounting panel
- Referees will probe endogeneity, construct measurement, or the channel
- You must document the Compustat/CRSP/I/B/E/S/audit-data provenance behind the sample
- An analytical paper needs a stylized empirical illustration of its comparative statics

## Get the standard errors right (a RAST signature check)

Empirical-accounting referees scrutinize inference. Default to **clustering by firm**, and consider **two-way clustering by firm and year** (Petersen) when both cross-sectional and time-series dependence are present. With **few clusters** (e.g., a state- or country-level policy), use the **wild-cluster bootstrap** rather than asymptotic cluster-robust SEs. Match the clustering to the source of correlated shocks implied by your design, and report the choice explicitly — an unjustified SE choice is a fast credibility hit at a journal that often decides in one round.

## Execute the identification, don't just assert it

- **DiD:** report pre-trends and use heterogeneity-robust estimators for staggered timing (Callaway–Sant'Anna / Sun–Abraham), not naive two-way FE.
- **RD:** report the optimal bandwidth, robust bias-corrected estimates, a manipulation (density) test, and covariate balance at the cutoff.
- **IV/2SLS:** report the first stage and instrument strength (e.g., F-statistic) and defend the exclusion in words.
- **Event studies:** report abnormal returns with a defensible benchmark and window, and confront confounding events — central for value-relevance and information-content claims.

## Measure accounting constructs credibly

Use measures with precedent in prior RAST/JAR/JAE/TAR work (discretionary accruals, accruals quality, earnings persistence/smoothness, disclosure indices, comparability, audit-quality proxies, bid-ask spread / PIN for information asymmetry). Show the proxy behaves sensibly (validation, correlation with established measures) and **test sensitivity to alternative proxies** — proxy fragility is one of the most common RAST rejection reasons. For analyst/forecasting work, document I/B/E/S handling (actuals definition, stale-forecast screens, splits adjustments).

## The robustness battery referees expect

- Alternative specifications: controls in/out, alternative fixed effects, alternative key-construct measures.
- Subsamples and falsification/placebo tests (effect absent where theory says it should be).
- Sensitivity of identification assumptions (alternative instruments, donut RD, bounds).
- Cross-sectional partitions that confirm the **predicted channel** (the conditional predictions from `revacc-theory-development`).
- Sample-construction, winsorization, and screen choices documented and varied.

## Provenance is a deliverable, not a courtesy

RAST does not run JAE's mandatory archive or JAR's posted package as the headline, but referees and the editor still expect a credible, reconstructable sample. Keep top-to-bottom runnable scripts that regenerate every table from raw extracts; document **screens, vintages, and access dates** for each source; respect database terms of use. If the work entered through the **RAST Conference** path, keep the version history clean for the conference-issue timeline. Confirm current data/code expectations on the official page (待核实; 检索于 2026-06).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAST is empirical accounting; emphasize identification of disclosure / governance effects and the multiple-testing haircut for mined associations.

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

- [ ] SE clustering matches the design (firm / firm-and-year; wild bootstrap if few clusters), stated explicitly
- [ ] Identification executed with diagnostics (pre-trends / bandwidth / first-stage / balance)
- [ ] Modern DiD estimators used for staggered treatment timing
- [ ] Key construct validated; results robust to alternative proxies
- [ ] Robustness, falsification/placebo, and channel partitions reported
- [ ] Winsorization/screens documented and varied; I/B/E/S handling documented where relevant
- [ ] Provenance trail (sources, vintages, screens) reconstructable; scripts runnable end-to-end

## Anti-patterns

- **White/robust SEs on panel data** ignoring within-firm correlation.
- **Naive two-way-FE DiD** with staggered adoption.
- **One proxy, no validation** for a contested accounting construct.
- **Significance fishing** across windows, bandwidths, or specifications.
- **Confounded event windows** in value-relevance/information-content tests.
- **Black-box sample:** screens and vintages undocumented, results unreproducible.

## Output format

```text
【Estimator & SEs】model; clustering (firm / firm×year / wild bootstrap) + justification
【Identification executed】diagnostics reported (pre-trends/bandwidth/first-stage/balance)
【Construct measurement】proxy + validation + alt-proxy robustness
【Robustness/falsification】[...]
【Channel partitions】conditional predictions confirmed? [...]
【Provenance】sources/vintages/screens documented; scripts runnable
【Open issues for referees】[...]
【Next skill】revacc-contribution-framing
```
