---
name: rje-data-analysis
description: Use when executing and stress-testing the empirical analysis for a RAND Journal of Economics (RJE) industrial-organization manuscript — estimating structural demand/supply, entry, auction, or reduced-form models, then running the robustness, counterfactual, and inference checks IO referees expect. Analysis discipline, not study design.
---

# Data Analysis & Robustness (rje-data-analysis)

## When to trigger

- Estimates are in hand and you need the robustness suite IO referees demand
- A structural counterfactual needs validation before it goes in the article
- You must report inference correctly for market-level / clustered data

## Analysis norms at the IO flagship

RJE referees apply **industrial-organization empirical norms**. Whether the work is structural or reduced-form, the analysis must show the estimates are **credible, well-behaved, and economically sensible**, and that **counterfactuals are disciplined** by the model.

### Structural work
- **Estimation diagnostics:** report objective-function value, convergence, and sensitivity to **starting values** (non-convex objectives); use multiple starts and report them.
- **Economic sanity:** elasticities, markups, and marginal costs in plausible ranges; own-price elasticities negative and large enough for positive markups.
- **Identification-in-practice:** show which moments move which parameters (sensitivity / informativeness of moments).
- **Counterfactuals:** state maintained assumptions (e.g., fixed product set, conduct unchanged), report them as ranges/bounds, and validate against any out-of-sample episode (a known merger, entry, or price change).

### Reduced-form work
- **Modern DID** where timing is staggered (Callaway–Sant'Anna / Sun–Abraham), with event-study leads and a Goodman-Bacon decomposition.
- **Weak-IV-robust inference** where instruments are weak; report the first-stage F.
- **Placebo / falsification** on markets or periods that should not respond.

### Inference (both)
- Cluster at the level of treatment/market variation; with few clusters use **wild-cluster bootstrap**.
- Set and report **seeds** for simulation, bootstrap, and randomization.

## Robustness suite to stage

- Alternative demand specification / functional form (structural) or alternative controls and sample (reduced-form)
- Alternative instruments and conduct assumptions
- Subsample and alternative market-definition checks
- Sensitivity of the headline **counterfactual / welfare** number to key assumptions

## Page-cap discipline

RJE's caps are hard (main text **<=40 pp**, total **<=50 pp**). Put the core estimates and one or two decisive robustness exhibits in the main text; **move the full robustness battery to the appendix** (within the <=10-page appendix+references budget), not into discouraged supporting information.

## Diagnostic triage table (structural estimates that IO referees flag)

When a structural estimate looks off, diagnose the symptom first.

| Symptom | Likely cause | First check to stage |
|---|---|---|
| Positive own-price elasticity | Price endogeneity unhandled or weak instruments | First-stage strength of cost shifters / BLP instruments |
| Implausibly large markups (>60%) | Conduct misspecified or marginal cost too low | Re-estimate under alternative conduct; inspect cost FOCs |
| Estimates jump across starting values | Non-convex GMM objective, flat ridges | Multi-start grid; report objective at each start |
| Counterfactual price swings wildly | Extrapolation outside observed variation | Bound the counterfactual; restrict to in-support changes |
| Substitution ignores obvious rivals | Too few random coefficients / no micro-moments | Add micro-moments or a nesting structure |

## Worked vignette: validating a merger simulation

Suppose you estimate random-coefficients logit demand for ready-to-eat cereal, recover marginal costs from Bertrand-Nash FOCs, and simulate a two-brand merger (illustratively, median markup 35%, predicted price rise 4.2% for the merging brands).

- **Economic sanity**: own-price elasticities near -3.5 are plausible for branded cereal; report that 35% markups sit within the literature's range.
- **Identification-in-practice**: show cost-shifter instruments move the price coefficient and differentiation instruments move the random-coefficient variances.
- **Counterfactual discipline**: hold product set and conduct fixed, state it, and report the rise as a range (3.1%-5.4%) across specifications.
- **Validation**: if a comparable merger occurred nearby, check whether the model predicts its realized price path.

A bare "+4.2%" with no band and no validation invites the first referee pushback below.

## Referee-pushback patterns and the venue fix

- **"Your counterfactual extrapolates outside observed price variation."** Fix: restrict the simulated change to the support of observed prices, or report bounds and flag the extrapolation explicitly.
- **"Markups are mechanical artifacts of the conduct assumption."** Fix: test conduct where the data allow, or show the markup ranking is robust across Bertrand, Cournot, and partial-collusion assumptions.
- **"Inference ignores within-market correlation."** Fix: cluster at the market level; with few markets, switch to wild-cluster bootstrap and report the seed.
- **"Robustness lives only in a footnote."** Fix: stage one decisive robustness exhibit in the main text and route the full battery to the appendix.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAND is industrial organization — endogeneity of prices/entry and structural demand; the reduced-form chain for causal claims, structural IO outside it.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A single structural run with no starting-value or specification sensitivity
- Counterfactuals reported as point estimates with no assumption bounds
- TWFE on staggered policy timing presented as the headline
- Default robust SEs when variation is at the market level

## Output format

```
【Estimator】structural (demand/conduct/entry/auction) / reduced-form
【Economic sanity】elasticities/markups plausible? [Y/N]
【Robustness done】[specifications, instruments, conduct, subsamples]
【Counterfactual】assumptions stated + bounded? [Y/N]
【Inference】clustering / weak-IV / seeds set? [Y/N]
【Page budget】main robustness in appendix? [Y/N]
【Next step】rje-tables-figures
```
