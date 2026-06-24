---
name: aejpol-identification
description: Use when the credibility of the causal evaluation of a policy is the bottleneck for an AEJ: Economic Policy manuscript — DID/event study, IV, RDD/bunching, or RCT of a program. Stress-tests the quasi-experimental policy-evaluation design to the AEJ: Policy bar before exhibits are finalized; it does not build the welfare mapping or write exhibits.
---

# Identification — Credible Policy Evaluation (aejpol-identification)

## When to trigger

- The causal effect of a policy rests on OLS + controls, or TWFE on staggered policy adoption
- A reform / threshold / experiment exists but the design's assumptions are not pinned down
- A referee questions whether the estimated effect is really *caused by the policy*
- You are unsure the design clears AEJ: Policy's credible-causal-evidence bar

## The AEJ: Policy identification bar

AEJ: Policy is an empirical policy journal: the **effect attributed to the policy must be credibly causal**, the **estimand must be the policy-relevant one**, and the design must survive the obvious confound that the policy was not random. The policy variation *is* the research design — name it explicitly (a reform date, an eligibility cutoff, a formula kink, a randomized rollout) and defend the assumption that makes it causal. Report **standard errors** (no significance asterisks; see `aejpol-tables-figures`) and make the design reproducible for the AEA Data Editor.

## Design paths

### Path A: DID / event study (reforms, staggered policy adoption)
- With staggered adoption move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, Borusyak–Jaravel–Spiess, de Chaisemartin–D'Haultfœuille); report a Goodman-Bacon decomposition to show the bias TWFE would induce.
- Show a clean **event study with pre-period leads** flat around zero; do not assert parallel trends, demonstrate it (and probe with Rambachan–Roth honest-DID where pre-trends are imperfect).
- Define the policy-relevant estimand (ATT on treated jurisdictions; weight by population/exposure if the policy lesson requires it).
- Cluster at the policy-assignment level (often state/jurisdiction); address few-cluster issues (wild-cluster bootstrap).

### Path B: IV / instrumented policy exposure
- Strong first stage; with weak instruments use Anderson–Rubin / weak-IV-robust sets and report the effective F.
- Defend the exclusion restriction in **institutions and theory**, not just statistically; argue the instrument affects outcomes only through the policy channel.
- State the LATE complier population and whether it is the policy-relevant margin.

### Path C: RDD / bunching (eligibility thresholds, tax/benefit schedules)
- RDD: McCrary / Cattaneo–Jansson–Ma density test; data-driven bandwidth; covariate smoothness at the cutoff; bias-corrected robust CIs (`rdrobust`).
- Bunching at kinks/notches in tax or benefit schedules: defend the counterfactual density and the structural elasticity it implies.
- Be explicit that the estimate is **local** to the threshold and argue its policy relevance.

### Path D: RCT / field experiment of a program
- **Pre-registration** with a pre-analysis plan; report deviations. Detailed instructions / protocol included.
- Randomization balance; attrition (Lee bounds if differential); multiple-hypothesis adjustment; explicit estimand and a take-up / intent-to-treat vs. treatment-on-treated distinction.
- Tie the experimental effect to the cost of the program so a welfare reading is possible.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AEJ: Policy evaluates programs and reforms; the design must carry a policy-relevant magnitude, not just statistical significance.

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Checklist

- [ ] The policy variation is named and the identifying assumption stated in one sentence
- [ ] Design-appropriate diagnostics shown (pre-trends / density / first-stage F / balance)
- [ ] Modern heterogeneity-robust estimator used where TWFE would bias
- [ ] Estimand is the policy-relevant one (right population, right weighting)
- [ ] Inference clustered at the assignment level; few-cluster handled
- [ ] SEs reported (no asterisks); the causal claim never exceeds what the design supports

## Anti-patterns

- TWFE on staggered policy rollout with no heterogeneity-bias discussion
- Asserting parallel trends instead of showing flat, precisely-estimated leads
- An exclusion restriction defended only by a significant first stage
- An RDD estimate generalized far from the cutoff without argument
- An RCT with no pre-registration, no attrition analysis, or no link to program cost
- Reporting significance with asterisks instead of standard errors

## Referee pushback mapped to the fix

- *"Staggered TWFE here is biased."* → Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show flat leads + Bacon decomposition.
- *"Pre-trends look slightly off."* → Honest-DID (Rambachan–Roth) bounds; show the conclusion survives plausible violations.
- *"This is just the effect at the threshold."* → State the local estimand; argue why the threshold population is policy-relevant or extrapolate cautiously.

## Output format

```
【Design】DID / IV / RDD-bunching / RCT
【Policy variation】the reform/cutoff/rollout that identifies the effect
【Identifying assumption】one sentence + how it is defended
【Diagnostics shown】[pre-trends / density / first-stage F / balance + attrition]
【Estimand】policy-relevant population + weighting; inference/clustering
【What it does NOT identify】[...]
【Next step】aejpol-theory-model (welfare mapping) or aejpol-robustness
```
