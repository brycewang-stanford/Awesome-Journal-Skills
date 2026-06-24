---
name: jeem-identification
description: Use when the identification argument is the bottleneck for a Journal of Environmental Economics and Management (JEEM) manuscript — an environmental-policy causal design, a climate/weather IV, or a revealed- or stated-preference valuation. Stress-tests the data-to-welfare mapping before exhibits are finalized; it does not invent evidence or citations.
---

# Identification Strategy (jeem-identification)

## When to trigger

- A regulation/permit-market effect rests on TWFE with staggered adoption, or on OLS + controls
- A hedonic or travel-cost estimate could be confounded by **spatial sorting** or omitted amenities
- A stated-preference WTP could be contaminated by hypothetical bias, scope insensitivity, or yea-saying
- A weather/pollution IV's exclusion restriction or its adaptation interpretation is challenged
- You are unsure the design recovers a **welfare-relevant** parameter, not just a reduced-form effect

## The JEEM identification bar

JEEM identification is judged on two axes at once: the **causal/preference-recovery argument** must be credible, *and* the recovered object must be **welfare-relevant** — a marginal damage, a WTP, a pass-through, an abatement cost. Environmental data carry field-specific threats (spatial dependence, sorting, monitoring-station selection, weather endogeneity through adaptation) that generic applied-micro referees miss but JEEM referees will not. Pick the branch and make the mapping from data to the welfare object explicit.

## Branch A — Environmental-policy causal design

- **Regulation / standards DiD:** with staggered rollout, abandon plain TWFE for heterogeneity-robust estimators (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show a clean event study with pre-period leads; report a Goodman-Bacon decomposition. Argue the regulation timing is not driven by prior pollution trends.
- **Cap-and-trade / permit markets:** the price and the cap are equilibrium objects — instrument or bound the endogeneity; watch for **leakage** to uncovered sources and **reshuffling**, which change the welfare sign.
- **RD in standards / eligibility:** sharp thresholds (an attainment cutoff, a plant-size or emissions threshold) — McCrary/Cattaneo–Jansson–Ma density test, covariate smoothness, bias-corrected CIs.
- **Inference:** cluster at the regulatory/assignment level; use spatial (Conley) SEs when units are geographic and shocks are correlated across space.

## Branch B — Climate / weather IV and damages

- Argue weather realizations are **as-good-as-random** conditional on location and time fixed effects; defend exclusion (weather affects the outcome only through the modeled channel).
- Separate **weather** (short-run shock) from **climate** (long-run expectation) — the adaptation margin is the contribution; a panel weather coefficient is not a long-run climate-damage estimate without an adaptation argument.
- Handle spatial and serial correlation in errors; report the estimand (marginal damage at current vs. future climate).

## Branch C — Revealed-preference valuation (hedonics, travel cost)

- **Hedonics:** the amenity coefficient is biased by **sorting** (Tiebout) and omitted correlated amenities. Use a quasi-experimental shock to the amenity (a plant opening/closing, a Superfund listing, a regulation), boundary discontinuities, or a sorting model; do not present a cross-sectional hedonic as causal WTP.
- **Travel cost:** address endogenous trip cost, multi-purpose trips, and the recreation-demand censoring (count models, Kuhn–Tucker demand systems).
- Be explicit about **what welfare measure** the capitalization or demand estimate recovers (marginal WTP vs. total amenity value) and its partial- vs. general-equilibrium scope.

## Branch D — Stated-preference valuation (CV, discrete-choice experiments)

- Survey design is the identification: incentive compatibility, a credible payment vehicle, a consequential decision, and a **scope test** (WTP rises with the size of the good).
- Address hypothetical bias (cheap-talk, certainty calibration, inferred valuation), protest responses, and status-quo/yea-saying effects.
- Pre-specify the choice model (RUM / mixed logit / latent class) and report welfare (compensating variation) with its uncertainty, not just utility coefficients.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEM is environmental economics — policy/regulation designs and non-market valuation; the causal chain serves its program-evaluation lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch named; the data-to-welfare-object mapping stated in one sentence
- [ ] Policy-causal: heterogeneity-robust estimator where TWFE would bias; clean pre-trends; leakage/reshuffling addressed
- [ ] Climate: weather vs. climate distinguished; adaptation margin and estimand explicit
- [ ] RP valuation: sorting/omitted-amenity threat answered with a shock, boundary, or sorting model
- [ ] SP valuation: incentive compatibility + scope test + hypothetical-bias treatment
- [ ] Inference matches the data: cluster at assignment level; spatial (Conley) SEs for geographic units
- [ ] The welfare claim never exceeds what the identification supports (marginal vs. total; PE vs. GE)

## Anti-patterns

- A cross-sectional hedonic presented as causal amenity WTP (sorting ignored)
- Staggered TWFE on a regulation rollout with no heterogeneity-bias discussion
- Treating a panel weather coefficient as a long-run climate-damage estimate (no adaptation)
- A contingent-valuation WTP with no scope test and no hypothetical-bias correction
- Permit-market effects ignoring leakage/reshuffling, so the welfare sign is unproven
- Default (non-spatial) standard errors on spatially correlated environmental data

## Worked vignette (illustrative)

A hedonic finds homes near a closed coal plant rose 6% in value and reports this as the WTP for cleaner air. A referee flags sorting: cleaner air may attract higher-income buyers. The JEEM fix is to exploit the **closure timing** in a DiD with parcel fixed effects, restrict to a narrow boundary band, and show pre-closure price trends were parallel; the spatial-clustered estimate settles at, say, 4.5% (illustrative), now defensible as a capitalization of the air-quality change rather than a sorting artifact.

## Referee pushback mapped to the identification fix

- *"This hedonic is sorting, not WTP."* → Exploit a quasi-experimental amenity shock with parcel/boundary FE; show parallel pre-shock price trends.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; display flat event-study leads.
- *"Your weather coefficient is not a climate-damage estimate."* → Separate the short-run shock from the long-run expectation; model the adaptation margin and state the estimand.
- *"The CV number could be hypothetical bias."* → Report a scope test, an incentive-compatible payment vehicle, and a cheap-talk or certainty calibration.
- *"Permit-market leakage flips your welfare sign."* → Bound the response of uncovered sources and show the net welfare conclusion holds.

## From identification to a welfare number

The JEEM-specific discipline is that identification is only half the job — the identified object must map to welfare. A clean DiD on emissions identifies an *effect*; the contribution is the *implied marginal damage avoided* or the *cost per ton abated* that a regulator can use. State, for your branch, the assumptions that license the welfare mapping (a VSL for mortality, a behavioral model for capitalization, a utility specification for choice WTP) and carry them into `jeem-theory-model` and `jeem-tables-figures` so the welfare claim is auditable rather than asserted.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-identification
【Branch】policy-causal / climate-IV / RP-valuation / SP-valuation
【Data-to-welfare mapping】one sentence
【Identification evidence】pre-trends+leads / weather-exogeneity / amenity-shock+boundary / scope-test
【Inference】clustering level + spatial SEs if geographic
【What it does NOT identify】marginal vs total; PE vs GE; weather vs climate
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-theory-model
```
