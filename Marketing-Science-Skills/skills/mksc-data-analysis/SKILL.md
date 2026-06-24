---
name: mksc-data-analysis
description: Use when estimating and validating the model for a Marketing Science manuscript — running structural estimation (GMM/MLE/SMM/Bayes), checking identification empirically, assessing model fit, computing counterfactuals, and preparing the replication package. Executes the analysis; it does not design the model (mksc-theory-development) or choose the genre (mksc-methods).
---

# Estimation, Fit & Counterfactuals (mksc-data-analysis)

## When to trigger

- The model is specified and it is time to estimate and report
- Estimates exist but identification, fit, or counterfactuals are not yet convincing
- A reviewer says "the parameters are not credibly identified" or "the counterfactual is not validated"
- You need the replication package (data + estimation code) ready for acceptance

## Estimate, then prove identification empirically

- **Run the estimator** matched to the model: GMM with the stated moment conditions (BLP), MLE/SMLE, simulated method of moments, or MCMC for hierarchical Bayes. Report standard errors that respect the estimation (e.g., GMM/sandwich, bootstrap, or posterior intervals) and the optimizer/convergence diagnostics.
- **Demonstrate identification, not just assert it**: show the identifying variation moves the relevant moments; report sensitivity of estimates to instruments; where feasible, a Monte Carlo recovering known parameters or a sensitivity-of-estimates-to-moments analysis strengthens the claim.
- **First-stage/instrument strength** for IV/GMM; relevance and exclusion discussed.

## Assess model fit before trusting counterfactuals

- Report **in-sample fit** (predicted vs. actual shares/prices/moments) and, where possible, **out-of-sample or holdout** validation.
- Check **economic plausibility** of estimates (own-/cross-price elasticities, margins implied by supply FOCs, discount factors) against priors and institutional facts.
- For Bayesian models, report convergence (R-hat, effective sample size) and posterior predictive checks.

## Counterfactuals are the payoff

- Re-solve the model under the policy/counterfactual, holding fixed only what theory says is fixed; recompute equilibrium prices/quantities where firms re-optimize.
- Report **magnitudes with uncertainty** (delta-method or simulation-based intervals), and decompose the mechanism driving the result.
- Discuss the scope and assumptions under which the counterfactual is valid.

## Robustness

- Alternative specifications (functional form, instruments, heterogeneity), subsamples, and alternative normalizations.
- Show the headline result and key counterfactual survive the changes a referee will request.

## Replication package (plan now, deposit on acceptance)

Per the Marketing Science Replication and Disclosure Policy, accepted papers submit **data and estimation code** sufficient for a peer to reproduce the essential content. For licensed data (NielsenIQ, Compustat, CRSP, Census), provide access instructions and the linking/build code rather than raw data. Keep a master script regenerating every table, figure, and counterfactual.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Marketing Science is heavily structural/analytical; the chain below serves its reduced-form / field-experiment lane — structural demand and analytical modeling are outside this causal-inference toolchain.

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

- [ ] Estimator run; appropriate SEs and convergence diagnostics reported
- [ ] Identification shown empirically (sensitivity/Monte Carlo/first stage)
- [ ] In-sample fit and (where possible) holdout/out-of-sample validation
- [ ] Estimates economically plausible (elasticities, margins, discount factor)
- [ ] Counterfactual re-solves equilibrium; magnitudes with uncertainty + mechanism
- [ ] Robustness to specification/instruments/normalization
- [ ] Replication package (code + data access/build) prepared

## Anti-patterns

- Reporting point estimates with no identification or fit evidence.
- A counterfactual that holds firm behavior fixed when firms would re-optimize.
- Elasticities/margins that are economically implausible, unaddressed.
- "Code available on request" instead of a replication-ready package.


## Evidence pass for Marketing Science

Use this as a second-pass capability check. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then test whether the manuscript addresses quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Estimator】GMM / MLE-SMLE / SMM / Bayes; SEs + convergence
【Identification evidence】sensitivity / Monte Carlo / first stage
【Fit】in-sample + holdout; economic plausibility of estimates
【Counterfactual】policy re-solved; magnitude ± uncertainty; mechanism
【Robustness】specs/instruments/normalizations
【Replication】data+code package status (licensed-data handling)
【Next step】mksc-contribution-framing
```
