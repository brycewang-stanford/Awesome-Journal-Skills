---
name: jppm-data-analysis
description: Use when estimating and stress-testing results for a Journal of Public Policy & Marketing (JPP&M) manuscript — treatment effects from experiments, DiD/RDD/synthetic-control policy evaluations, subgroup analyses for vulnerable populations, and policy-interpretable reporting. Runs the analysis; it does not choose the design (jppm-methods).
---

# Data Analysis (jppm-data-analysis)

## When to trigger

- A DiD around a policy rollout needs modern estimators and a pre-trend defense
- An RDD's bandwidth, density, or placebo checks are unbuilt
- Experimental effects are significant but not yet expressed in units a regulator can use
- Subgroup results for vulnerable populations look like fishing rather than a plan
- A reviewer will ask "how big is this in the market, and for whom?" and you cannot answer

## Estimate for the decision, not the asterisk

At JPP&M the estimate feeds a **policy judgment**, so the analysis has two jobs the sibling journals weigh less: (1) make the causal claim survive an econometrics-literate reviewer, and (2) express magnitudes in **decision units** — percentage points of prevalence, dollars per household, calories per purchase, share of consumers misled — with uncertainty attached. A p-value cannot tell an agency whether a warning is worth mandating; an effect of "−2.1 percentage points in purchase incidence, 95% CI [−3.4, −0.8], concentrated among households below median income" can. Every headline estimate should be convertible into the language of a regulatory impact analysis.

## The evaluation battery

| Design | Core estimate | The checks reviewers expect |
|--------|---------------|------------------------------|
| DiD (staggered adoption) | group-time ATTs (Callaway–Sant'Anna, Sun–Abraham) | event-study plot; Goodman-Bacon decomposition; honest-DiD sensitivity to pre-trend violations |
| Canonical 2×2 DiD | TWFE with clustered SEs | pre-trend test; placebo outcomes; composition stability |
| RDD | local polynomial at the cutoff (rdrobust) | McCrary density test; bandwidth sensitivity; covariate smoothness; donut variants |
| Synthetic control | treated-vs-synthetic gap | pre-period fit; in-space and in-time placebos; leave-one-out donors |
| Experiment | ANOVA/OLS on manipulated conditions | randomization/balance check; effect sizes with CIs; multiple-outcome corrections |

Inference discipline: cluster at the policy-assignment level (state, market), and when treated clusters are few, use wild-cluster bootstrap or randomization inference rather than pretending N is large.

## Heterogeneity as welfare analysis

Subgroup effects are not garnish here — they are often the finding. Pre-specify the policy-relevant splits (income, literacy/numeracy, age, race/ethnicity where the policy debate concerns targeting, prior usage of the harmful product), report them all rather than the flattering subset, and correct for the family of tests. An intervention with a null average effect that protects the most-exposed decile is a policy success; a positive average driven entirely by the already-safe is a policy failure. Interactions need probing (simple effects at policy-meaningful levels), and null subgroup effects deserve equivalence-style interpretation, not silence.

## Translating estimates into policy terms

- **Rescale to the affected population**: effect × exposed base = market-level consequence (with CI carried through).
- **Benchmark against instruments**: compare the effect to what taxation, education, or existing labels achieve.
- **Report the compliance-adjusted effect**: an ITT under partial firm compliance understates the mandate's potential; show both ITT and, where instruments allow, the complier-adjusted estimate.
- **Bound the unintended consequences**: quantify substitution and boomerang outcomes, even (especially) when noisy.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPP&M lives on policy evaluation and policy-realistic experiments; the counterfactual checks and welfare-relevant subgroup corrections are where reviewers concentrate fire.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate what the design still owes.
- **Staggered policy adoption:** `callaway_santanna` / `sun_abraham`, then
  `bacon_decomposition` and `honest_did_from_result` for the pre-trend sensitivity a
  policy audience needs.
- **Cutoff-assigned exposure:** `rdrobust` + `mccrary_test` (firms sort around
  thresholds — test it, don't assert it).
- **Experiments and subgroup families:** randomization inference plus `romano_wolf` /
  `benjamini_hochberg` across the vulnerable-population splits.
- **Inference with few treated clusters:** `wild_cluster_bootstrap`; spatial policy
  spillovers → `conley`.
- **Exhibits from the handle:** `etable` / `did_summary_to_latex` and
  `plot_from_result`, so table numbers never drift from the fitted model.

Keep the decisive counterfactual evidence in the body and the exhaustive battery in the
web appendix; a worked end-to-end run lives in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).

## Checklist

- [ ] Headline effects reported in decision units with CIs, not asterisks
- [ ] DiD uses heterogeneity-robust estimators; event study + sensitivity to pre-trend violations shown
- [ ] RDD shows density, bandwidth, and placebo checks; synthetic control shows placebos
- [ ] SEs clustered at the assignment level; small-cluster inference handled honestly
- [ ] Vulnerable-population subgroups pre-specified, all reported, family-corrected
- [ ] Market-level rescaling and instrument benchmarking included
- [ ] Unintended-consequence outcomes estimated or explicitly bounded

## Anti-patterns

- **TWFE autopilot**: a staggered rollout estimated with plain two-way fixed effects, no diagnostics
- **Eyeball parallel trends**: a raw-trends plot standing in for a sensitivity analysis
- **Subgroup roulette**: the one significant split reported, the pre-specified family hidden
- **Unitless effects**: standardized betas a regulator cannot map to any decision
- **Cherry-dropped clusters**: excluding inconvenient states/markets without a stated rule
- **Silent substitution**: claiming success while consumers shifted to an equally harmful alternative

## Output format

```text
【Design & estimator】DiD (CS/SA) / RDD / synthetic control / experiment (+ inference choice)
【Headline estimate】effect in decision units + CI
【Counterfactual checks】pre-trends/sensitivity, density/placebos — status of each
【Heterogeneity】pre-specified subgroups, corrected; who is protected vs. missed
【Policy translation】market-level magnitude + benchmark vs. alternative instruments
【Unintended effects】substitution/boomerang estimates or bounds
【Next skill】jppm-contribution-framing
```
