---
name: jcf-identification-strategy
description: Use when designing or defending the causal identification strategy for a Journal of Corporate Finance (JCF) empirical paper — choosing and stressing a design (DID/staggered shocks, IV/GMM, RDD, event study, matching) for firm-level data with endogenous corporate decisions. It evaluates and hardens the design; it does not run the regressions.
---

# Identification Strategy (jcf-identification-strategy)

## When to trigger

- Picking a credible design for a corporate-finance question with endogenous choices
- Pre-empting the referee's "your X is endogenous / reverse-causal" objection
- Defending parallel trends, exclusion restrictions, or window cleanliness

## Why JCF needs a real design

Corporate-finance variables (leverage, governance, payout, M&A) are **choices**, so OLS-with-controls invites endogeneity, omitted-variable, and reverse-causality critiques. JCF is empirical corporate finance: a clean identification strategy is what separates a publishable paper from a desk reject. Match the design to the source of variation.

## Design menu (corporate finance)

- **Staggered DID** around law/regulation/governance shocks — use **modern estimators** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille), run **Goodman-Bacon** diagnostics, show **event-study leads** for pre-trends. Plain TWFE on staggered timing is a known pitfall.
- **IV / dynamic-panel GMM** — justify the exclusion restriction in words, report **first-stage F** and weak-IV-robust CIs; for leverage dynamics, `xtabond2`-style GMM with instrument-count discipline.
- **RDD** — voting/index/threshold cutoffs; show a **density/manipulation test** and bandwidth robustness.
- **Event study (returns)** — a **clean, narrow window**, a confounding-news screen, and CAR/BHAR robustness.
- **Matching / entropy balancing** — report **covariate balance** and common support; treat as conditioning, not identification, unless paired with a shock.

## Hardening checklist

- [ ] The **source of exogenous variation** is named and defended in one paragraph
- [ ] The key threat (selection, reverse causality, confounding shock) is addressed head-on
- [ ] Pre-trends / first stage / density / balance shown as appropriate
- [ ] At least one **alternative design or placebo** corroborates the main estimate
- [ ] Standard errors **clustered** at the right level (firm and/or time)

## Shock-quality grading for corporate-finance settings

Not every "exogenous" source of variation survives a JCF referee. Grade the shock before building on it:

```text
Variation source                       | Credibility at JCF | Known objection to pre-empt
Staggered state law adoption           | High if modern DID | Lobbying/timing endogeneity; heterogeneity bias
Federal regulation with size threshold | High               | Bunching at the cutoff; anticipation effects
Index inclusion/exclusion (RDD)        | High near cutoff   | Local estimate only; index rules changed over time
Shareholder vote near 50% (RDD)        | High               | Close votes not random across firm types — test it
Import tariff / trade shocks           | Moderate           | Industry-level treatment; exposure-measure disputes
Natural disasters / plant-level shocks | Moderate           | Location selection; general-equilibrium spillovers
CEO deaths / health shocks             | Moderate           | Small N; succession-planning selection
Instrument built from lagged choices   | Low                | Exclusion fails by construction — expect rejection
```

## Worked stress test: a staggered-adoption claim

Hypothetical, numbers illustrative: a paper claims staggered anti-takeover statutes raise leverage. TWFE gives 0.024 (t = 3.1). The JCF hardening sequence: (1) a Goodman-Bacon decomposition shows 31% of identifying weight comes from late-versus-early treated comparisons — a red flag; (2) Callaway–Sant'Anna on clean controls gives 0.015 (t = 2.2) — smaller but alive; (3) event-study leads are flat for five pre-years (joint p = 0.41); (4) one state adopting after a lobbying scandal is dropped — the estimate moves to 0.014. The paper then reports the modern estimator as the headline, TWFE as a legacy comparison, and the decomposition in the appendix. That ordering — not the TWFE number — is what survives review here.

## Selection-into-treatment: the paragraph referees look for

Every JCF design with treated firms needs one explicit paragraph: who became treated, why, and what that implies. Cover (a) the institutional reason treatment landed where it did, (b) a pre-treatment covariate comparison or trends table, (c) the direction of bias if a selection story survives, and (d) why the estimate is then a lower or upper bound. Omitting this paragraph is among the most common reasons an otherwise clean JCF design draws a second-round identification objection.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCF is corporate finance — endogeneity of corporate policies is the central threat; foreground IV/DiD identification.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- "We control for everything" as a substitute for a design.
- TWFE event-study with no modern-estimator robustness on staggered adoption.
- An IV whose exclusion restriction is asserted, never argued.

## Output

```
【Design】<DID/IV/RDD/event/matching>  【Variation】<source>
【Top threat】<x> → handled by <y>
【Diagnostics】pre-trend/first-stage/density/balance: [Y/N each]
```
