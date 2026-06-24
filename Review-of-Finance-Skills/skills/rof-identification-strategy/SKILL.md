---
name: rof-identification-strategy
description: Use when the credibility core of a Review of Finance (RoF) manuscript is the bottleneck — causal identification for empirical finance (DID, IV, RDD, event study, natural experiments) OR assumptions, results, and proof exposition for theoretical finance. Stress-tests the design or model to the top-three-finance-journal standard.
---

# Identification & Theory Strategy (rof-identification-strategy)

## When to trigger

- The empirical core is panel regressions with controls and an undefended causal claim
- A DID uses two-way fixed effects on staggered timing without modern estimators
- An IV's first stage is weak or its exclusion restriction is unargued
- The paper is **theoretical** and the assumptions, generality, or proof exposition are the weak link

## The RoF credibility bar

RoF referees apply **top-three-finance-journal standards** to the inferential or logical spine. Because RoF publishes **both empirical and theoretical** finance, "identification" means two different things — pick the branch matching your paper.

### Branch E1 — Empirical: causal design for finance

- **Natural experiments / shocks**: regulatory changes, index reconstitutions, staggered law adoption. Name the identifying variation in one sentence and defend its exogeneity.
- **DID / event study**: under staggered adoption, move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); report a Goodman-Bacon decomposition and clean pre-trends.
- **IV**: strong first stage (report F); weak-IV-robust inference when needed; defend the exclusion restriction on economic, institutional, and falsification grounds.
- **RDD**: density/manipulation test, optimal bandwidth plus robustness, covariate smoothness.
- **Asset-pricing inference**: correct standard errors (Newey–West, two-way clustering, Shanken for Fama–MacBeth); guard against data-snooping in factor/anomaly work; cluster at the assignment level.

### Branch T1 — Theoretical: assumptions, results, proof exposition

- **Assumptions**: state them economically; flag substantive vs. technical; discuss what breaks if each is relaxed.
- **Results**: lead with the proposition and its economic message, not the algebra; show it is **non-obvious** and **general** enough to matter.
- **Proof exposition**: keep proofs self-contained in an appendix with intuition in the body; proofs count against the **60-page cap**.
- **Numerical work**: report solver tolerances, convergence, and seeds (see `rof-replication-and-data-policy`).

## Diagnostics placement grid — body vs. internet appendix

| Design | Must sit in the body | Goes to the internet appendix |
|--------|----------------------|-------------------------------|
| Staggered DID | event-study plot with pre-trends; heterogeneity-robust estimate next to TWFE | Bacon decomposition detail; alternative comparison groups |
| IV | first-stage table with effective F; the exclusion argument in prose | weak-IV-robust CIs; alternative instruments |
| RDD | density test; the main RD plot | bandwidth grid; donut; placebo cutoffs |
| Return event study | abnormal-return model choice; clustering by event date | alternative factor models; bootstrap inference |
| Fama–MacBeth / sorts | Shanken or NW errors; microcap screen statement | alternative breakpoints; subperiods |

RoF's editors want the identification spine self-contained inside the 60-page envelope; the appendix carries the battery, the body carries the logic.

## Worked vignette — a staggered short-sale-ban DID

Illustrative numbers. Twelve European exchanges ban short sales on financial stocks on different 2008–2012 dates. TWFE yields −1.9% on a liquidity outcome; Callaway–Sant'Anna with not-yet-treated controls yields −3.4% — TWFE was diluted by already-treated comparisons. The RoF-grade presentation: lead with the event-study figure (flat pre-trends, 95% bands, joint pre-trend test p = 0.41 reported, not just plotted); one table with both estimators; one sentence naming the identifying variation ("ban dates set by national regulators' crisis calendars, not by stock-level liquidity trends"); and the magnitude translated — 3.4% of the average bid–ask spread, roughly the trading-cost jump of moving the median bank stock one liquidity decile.

## Referee pushback and the venue-specific repair

- "Ban timing is endogenous to crisis severity" → show timing is uncorrelated with pre-ban outcome trends; add severity-bin interactions; isolate a subset where the trigger was plausibly external.
- "The exclusion restriction is asserted, not argued" → add a falsification outcome the instrument should not move and cite the institutional document that created the variation — RoF referees reward institutional specificity over econometric hand-waving.
- "Your proposition rides on CARA plus normality" → prove the comparative static for a wider preference class or locate numerically where it breaks; the breaking point goes in the body, the proof in the appendix (which still counts toward the 60 pages).
- "Anomalies like this die out of sample" → pre-commit an international split (e.g., Datastream non-US sample) or a post-publication window before the referee demands one.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Review of Finance is the EFA flagship — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- TWFE on staggered treatment with no heterogeneity-bias discussion.
- An anomaly "discovered" via repeated sorts with no multiple-testing or out-of-sample discipline.
- A theory result that is true by assumption, dressed in heavy notation.
- Over-claiming a local empirical estimate as a universal law, or a knife-edge model as general.

## Output format

```
【Branch】empirical (E1) / theory (T1)
【Spine】identifying variation OR key assumption+result
【Diagnostics done / missing】[...]
【Inference / rigor】clustering & SE OR proof completeness
【Over-claim check】never exceeds design/model? [Y/N]
【Next step】rof-data-analysis
```
