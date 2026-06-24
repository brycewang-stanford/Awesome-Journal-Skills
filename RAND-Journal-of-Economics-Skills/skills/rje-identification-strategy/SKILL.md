---
name: rje-identification-strategy
description: Use when the identification or estimation strategy is the bottleneck for a RAND Journal of Economics (RJE) industrial-organization manuscript — structural demand/supply, entry and dynamic games, auctions, or reduced-form designs off mergers and regulation. Stress-tests the design to the IO-flagship bar before tables are drafted.
---

# Identification Strategy (rje-identification-strategy)

## When to trigger

- Your structural model's identification (instruments, functional form, moments) is unargued
- A merger/regulation evaluation rests on TWFE over staggered timing with no modern estimator
- An IV's first stage or exclusion restriction is weak in an IO setting
- You are unsure your design clears the RJE industrial-organization bar

## The RJE identification bar

RJE is the **flagship industrial-organization journal**, so identification is judged by IO norms: the **economic model and the source of identifying variation must be explicit**, and counterfactuals must be disciplined by the model and the data. Both **structural** and **reduced-form** work is welcomed — there is no preference for one, but each carries field-specific obligations.

## Branch A: Structural demand (BLP-style)

- **Price endogeneity** is the central threat. Instrument price with cost shifters, rival/own product characteristics (BLP instruments), or Gandhi–Houde differentiation instruments; argue their validity in market terms.
- Add **micro-moments** (consumer-level data) where available to pin down substitution and heterogeneity.
- State functional-form assumptions (random-coefficients distribution) and show key elasticities are reasonable, not artifacts.

## Branch B: Supply, conduct & markups

- Be explicit about the **conduct assumption** (Nash-Bertrand, Cournot, collusion) and, where possible, **test conduct** rather than assume it.
- Identify marginal cost from the supply-side FOCs; show pass-through and markups are economically sensible.

## Branch C: Entry / dynamic games

- For static entry, address **multiplicity of equilibria** (bounds, equilibrium selection).
- For dynamic models, justify the **CCP / two-step (Hotz–Miller)** approach or full-solution estimation, and state the state space and discount factor handling.

## Branch D: Auctions

- Map the **observed bids to the value distribution** through the equilibrium first-order conditions; state the information paradigm (private vs common values).

## Branch E: Reduced-form (mergers / regulation)

- Name the **policy or merger shock** giving exogenous variation; defend it institutionally.
- Staggered timing? Move beyond **TWFE** — use Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille, with an event-study plot and a Goodman-Bacon check.
- For IV: strong first stage, weak-IV-robust inference, and an exclusion restriction argued from market institutions.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAND is industrial organization — endogeneity of prices/entry and structural demand; the reduced-form chain for causal claims, structural IO outside it.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Economic model / identifying variation stated in one sentence
- [ ] Price endogeneity (structural) or treatment exogeneity (reduced-form) defended
- [ ] Instruments named and their validity argued in market terms
- [ ] Conduct / equilibrium-selection assumptions made explicit
- [ ] Modern estimator used where TWFE would be biased
- [ ] Counterfactual assumptions bounded and stated
- [ ] Claims never exceed what the model + data support

## Variation-to-parameter map (what pins down which primitive)

RJE referees want an explicit account of which variation identifies which structural object.

| Structural object | Identifying variation | Threat if absent |
|---|---|---|
| Own-price elasticity | Cost/input-price shifters orthogonal to demand shocks | Endogeneity biases elasticity to zero |
| Substitution / random coefficients | Rival characteristics across markets; micro-moments | Restrictive IIA, wrong merger effects |
| Marginal cost | Supply-side FOCs given conduct and demand | Cost confounded with markup |
| Conduct parameter | Demand rotations (slope- vs level-shifters) | Conduct assumed, not identified |

## Worked vignette: identifying conduct in an entry model

Suppose you study airline entry on city-pair routes (illustratively 1,200 routes over six years, one potential entrant each) and ask whether incumbents deter entry.

- **Identifying variation**: endpoint market-size shifters move entry value; slot/gate cost shifters move fixed costs independently.
- **Multiplicity**: simultaneous entry admits multiple equilibria — use Ciliberto-Tamer-style bounds or an explicit selection rule, and report the parameter set.
- **One-sentence map**: "Demand shifters identify entry value, cost shifters identify fixed costs, and incumbent presence correlating with non-entry net of profitability identifies deterrence."

## Referee-pushback patterns and the venue fix

- **"Demand identification rests on functional form, not variation."** Fix: show which excluded instruments move price versus substitution, and perturb the random-coefficient distribution to prove the elasticities are not artifacts.
- **"The exclusion restriction is asserted, not defended."** Fix: argue why the cost shifter is plausibly orthogonal to the demand shock here, and probe with an overidentification or placebo-instrument check.
- **"Conduct is assumed Nash-Bertrand without test."** Fix: run a conduct test (Rivers-Vuong or a markup restriction) or report results under competing conduct models.
- **"Pre-trends violate the reduced-form design."** Fix: show event-study leads, use the heterogeneity-robust estimator, and report the Goodman-Bacon decomposition.

## Anti-patterns

- A demand system with price treated as exogenous, or weak/unargued price instruments
- Assuming Nash-Bertrand conduct when the data could test it
- TWFE on staggered merger/regulation timing with no heterogeneity-robust estimator
- Selling an in-sample fit as a credible far-out-of-sample counterfactual

## Output format

```
【Approach】structural demand / conduct / entry-dynamics / auctions / reduced-form
【Identifying variation】one sentence
【Key assumptions】[instruments, conduct, equilibrium selection, exclusion]
【Diagnostics done】[elasticities, first-stage F, pre-trends, conduct test]
【Diagnostics missing】[...]
【Next step】rje-data-analysis
```
