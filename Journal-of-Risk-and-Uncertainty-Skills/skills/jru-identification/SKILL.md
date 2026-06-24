---
name: jru-identification
description: Use when identifying a risk or uncertainty parameter is the bottleneck for a Journal of Risk and Uncertainty (JRU) manuscript — incentive-compatible elicitation in an experiment, or structural/empirical estimation of risk preferences, VSL, or insurance demand. Stress-tests how the data pin the primitive; it does not invent evidence or citations.
---

# Identification Strategy (jru-identification)

## When to trigger

- An experiment elicits a risk or ambiguity attitude but the mechanism may not be **incentive-compatible** (truthful revelation in doubt)
- A choice-list / BDM / matching-probability design is used and a referee questions whether it measures the parameter cleanly
- A structural model is estimated on field data and it is unclear *what variation* identifies the risk parameter (vs. beliefs, vs. constraints)
- A VSL or insurance-demand estimate rests on regressions whose exclusion or selection assumptions are not defended

## The JRU identification bar

At JRU "identification" means the **mapping from choices to the risk/uncertainty primitive** must be explicit and defended — whether that primitive is elicited in the lab or estimated from the field. Because the journal spans theory, experiment, and empirics, identification splits by branch. The unifying demand: the procedure must reveal the *intended* parameter and not confound it with utility curvature, beliefs, or constraints.

### Branch A: Experimental elicitation of risk / ambiguity preferences

- **Incentive compatibility.** State the mechanism and why it elicits truthfully: Becker–DeGroot–Marschak, multiple price lists / choice lists, the random-incentive (one-task-paid) system. Address the known threats — BDM is only IC under EU; the random-incentive system assumes isolation; multiple-switching in price lists signals confusion.
- **Estimand before estimator.** Name what the task is meant to recover — a switching point, a certainty equivalent, a matching probability — and the structural parameter it maps to (curvature, w(p), ambiguity index).
- **Design that separates u from w.** A single risk-attitude number cannot identify utility curvature and probability weighting jointly; use lottery menus designed to break that confound (e.g., varying probabilities at fixed outcomes).
- **Stakes, hypothetical vs. real, order, and house-money** effects stated and, where they matter, randomized.

### Branch B: Structural / empirical estimation (risk preferences, VSL, insurance)

- **Name the identifying variation.** For VSL hedonic-wage: the wage–fatality-risk tradeoff, conditional on the compensating-differentials assumptions; defend why risk is not proxying for unobserved job disamenities. For insurance demand: the price/loss variation that moves takeup.
- **Beliefs vs. preferences.** Field choices reflect both; say how the design separates a risk *attitude* from a subjective *belief* (e.g., independent belief elicitation, or variation that moves one but not the other).
- **Selection and measurement error** in risk exposure addressed; report the estimating equation and the inference (clustered appropriately).
- **Estimation regularity** for structural models: objective (MLE/GMM/MSM), starting values, and recovery of known parameters in simulation.

### The confounds JRU referees probe most

Three confounds recur across both branches; name how the design defeats each:

- **Utility curvature vs. probability weighting.** A single risk-attitude index cannot separate them; only a design that varies probabilities and outcomes independently can.
- **Preferences vs. beliefs.** Field and even lab choices reflect subjective probabilities; either elicit beliefs separately or use variation that moves price/cost while holding beliefs fixed.
- **Preferences vs. constraints.** Low takeup or conservative choices may reflect liquidity, not taste; control for or exploit variation in the constraint.

A clean identification section states, for each of these, whether the design breaks the confound or leaves it open — and the honest "leaves it open" entries belong in the limitations, not hidden.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JRU spans decision experiments and applied risk; randomization inference for experiments, DiD/IV for observational claims.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the choices-to-primitive mapping stated in one sentence
- [ ] Experimental: mechanism named and its incentive-compatibility (and its assumptions) defended
- [ ] Experimental: design separates utility curvature from probability weighting (or risk from ambiguity)
- [ ] Empirical: the identifying variation is named; preferences are separated from beliefs and constraints
- [ ] VSL: compensating-differentials / exclusion assumptions stated and probed
- [ ] Inference appropriate to the design (clustering at randomization or assignment level)
- [ ] The estimated parameter is not asked to carry interpretation the identification does not support

## Anti-patterns

- Calling a single risk-attitude index "the" risk preference when curvature and weighting are confounded
- Using BDM or a price list and claiming truthful revelation without noting the EU/isolation assumptions it rests on
- A VSL estimate that ignores selection of workers into risky jobs and the publication-selection debate
- Reading a field choice as a pure preference when it also reflects beliefs or liquidity constraints
- "The estimator converged" presented as if it were identification (structural)

## Referee pushback mapped to the identification fix

- *"Your 'risk preference' is just utility curvature times probability weighting — you can't tell them apart."* → Add lottery menus that vary probabilities at fixed outcomes so w(p) is identified separately from u; report both.
- *"BDM is not incentive-compatible outside expected utility."* → State the IC assumptions; where the paper studies non-EU agents, use a mechanism whose IC does not presume EU, or bound the bias.
- *"Low takeup could be misperceived risk, not a preference."* → Elicit subjective probabilities independently; use price variation that moves cost holding beliefs fixed.
- *"Your VSL is contaminated by selection into risky jobs."* → Probe selection (instrument or panel within-worker variation), and benchmark against the meta-analytic VSL distribution rather than a single estimate.

## Worked vignette (illustrative)

A field study infers high risk aversion from low flood-insurance takeup. A referee notes this confounds preferences with **beliefs** (households may think the risk is near zero) and with **constraints** (premiums vs. liquidity). The JRU fix elicits subjective loss probabilities separately, then uses exogenous premium variation (say a subsidy lottery) to move price holding beliefs fixed — so the demand elasticity identifies a preference, not a misperception. The reported elasticity (illustrative −0.3) now means what the paper claims it means.

## Second vignette: separating curvature from weighting (illustrative)

A lab paper reports a single "risk aversion" coefficient from a Holt–Laury price list. A referee points out the coefficient bundles utility curvature with probability weighting, so it cannot speak to whether the behavior is EU or CPT. The JRU revision adds a menu block that holds outcomes fixed while sweeping probabilities; the resulting certainty equivalents trace an inverse-S w(p) that pins weighting independently of u — turning one confounded number into two interpretable primitives.

## Stating what is NOT identified

Every honest identification section closes a door it leaves open. Name explicitly what the design cannot recover — a population parameter beyond the experimental sample, a belief you could not elicit, a margin you could not exogenously vary. JRU referees treat a candid "we identify the preference but not the belief" far more kindly than an overclaim that the data cannot support, and it pre-empts the most damaging review verdict: that the headline number means something other than what the paper says.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-identification
【Verdict】identified / patch design / re-estimate
【Branch】experimental elicitation / structural-empirical
【Choices-to-primitive mapping】one sentence
【Identification evidence】mechanism+IC / identifying variation + belief separation
【What it does NOT identify】<confounds left open>
【Source status】verified / 待核实 / not asserted
【Next skill】jru-robustness
```
