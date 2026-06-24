---
name: jpube-identification-strategy
description: Use when the causal identification strategy is the bottleneck for a Journal of Public Economics (JPubE) manuscript — bunching at tax kinks/notches, regression kink (RKD), DID off reform rollout, IV from policy instruments, RDD at eligibility thresholds. Stress-tests the design against public-finance norms before tables are drafted.
---

# Identification Strategy (jpube-identification-strategy)

## When to trigger

- The empirical core is OLS + controls with an undefended causal claim
- A reform DID uses two-way fixed effects (TWFE) on staggered timing
- A bunching estimate lacks a defensible counterfactual density
- An IV's policy instrument has an unargued exclusion restriction
- You are unsure the design clears the JPubE public-finance bar

## The JPubE identification bar

JPubE rewards **credible identification of a policy-relevant parameter**, evaluated by public-finance specialists under single anonymized review (a minimum of two reviewers, with author identity known to them). Because the field's payoff is usually a behavioral elasticity feeding a welfare formula, the design must pin down the response to a tax, transfer, or program rule cleanly. The credibility ranking referees implicitly apply (strong → weaker):

1. **Bunching / notch designs** at a known kink or eligibility threshold, recovering an elasticity from excess mass
2. **RDD / RKD** at a sharp policy cutoff (eligibility, benefit schedule kink)
3. **DID / event study** off a credibly exogenous reform rollout, with modern estimators
4. **IV** with a policy instrument, strong first stage, and a defended exclusion restriction
5. **Selection-on-observables** — acceptable only as a complement, rarely as the spine

JPubE's comparative advantage is the **policy-induced discontinuity** — a tax kink, a benefit cliff, a reform date — so make the identifying variation an institutional feature a reader can see.

## Branch paths

### Branch A: Bunching at kinks / notches
- Estimate excess mass against a smooth counterfactual fit away from the kink; report the implied elasticity.
- Round-number / focal-point diagnostics; bin-width and excluded-region robustness.
- For notches, address the dominated region and optimization frictions; bound attenuation from frictions.

### Branch B: RDD / RKD
- McCrary / Cattaneo–Jansson–Ma density test for manipulation at the cutoff.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik), bias-corrected CIs, bandwidth robustness.
- For RKD, identify off the slope change in the policy schedule; placebo kinks and covariate smoothness.

### Branch C: DID / event study off a reform
- Staggered adoption? Move beyond TWFE — Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille; report a Goodman-Bacon decomposition.
- Clean pre-trends via an event-study plot; cluster at the level of treatment (often state/jurisdiction).

### Branch D: IV from a policy instrument
- First-stage F strong; weak-IV-robust inference (Anderson–Rubin) where needed.
- Exclusion argued in three registers: theory, institutional detail, falsification.
- Report reduced form and OLS; state the LATE / compliers interpretation.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPubE is public economics — tax/transfer/program designs; DiD/IV/RDD and bunching are central, magnitudes in policy units.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Policy-induced identifying variation named in one sentence and defended as exogenous
- [ ] Design-appropriate diagnostics done (excess-mass fit / density / first-stage F / pre-trends)
- [ ] Modern estimator used where TWFE would be biased (staggered reform)
- [ ] Inference matched to assignment level (often jurisdiction); few-cluster handling
- [ ] Frictions / manipulation / placebo tests reported
- [ ] The recovered parameter maps to the welfare quantity the paper claims

## Anti-patterns

- Bunching with an arbitrary excluded region chosen to maximize the estimate
- TWFE on staggered reform timing with no heterogeneity-bias discussion
- IV that is "policy shock × lagged endogenous variable" with no exclusion argument
- An elasticity identified locally but sold as a global structural parameter

## Design-credibility pushback (and the pre-emptive fix)

Address these in the manuscript before a specialist referee raises them.

| Likely objection | Design weak spot | Pre-empt with |
|------------------|------------------|---------------|
| "Bunching leans on functional form" | Counterfactual density fit | Multiple excluded regions + polynomial orders; show stability |
| "Manipulation at the cutoff" | RD assignment | McCrary / Cattaneo–Jansson–Ma density test + covariate smoothness |
| "Reform timing is endogenous" | DID exogeneity | Clean pre-trends, placebo dates, institutional narrative |
| "Weak / invalid instrument" | IV exclusion | First-stage F, Anderson–Rubin CI, falsification |

## Worked example: a kink-bunching elasticity, stress-tested (illustrative)

Suppose excess mass at a tax kink yields a taxable-income elasticity of **e = 0.25** (illustrative). The skill's bar asks three things before any table: (1) is the counterfactual a smooth density fit away from the kink, with round-number bunching handled? (2) does the estimate survive bin-width and excluded-region variation — here it stays within **0.21–0.29** (illustrative)? (3) does e map to the welfare object the paper claims — the marginal DWL of the kink rate? Only when all three hold is the design ready for `jpube-data-analysis`. If the elasticity swung from 0.1 to 0.5 across reasonable excluded regions, the identification is not yet credible, regardless of the headline.

## Output format

```
【Design】bunching / RDD / RKD / DID / IV / other
【Identifying variation】one sentence (the policy discontinuity)
【Diagnostics done】[excess-mass fit, density, first-stage F, pre-trends, ...]
【Diagnostics missing】[...]
【Inference】clustering level + few-cluster handling
【Parameter → welfare】elasticity / sufficient stat mapped? [Y/N]
【Next step】jpube-data-analysis
```
