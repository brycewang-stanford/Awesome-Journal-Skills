---
name: pom-data-analysis
description: Use when executing and reporting the analysis for a Production and Operations Management (POM) manuscript — proving and numerically illustrating an analytical model, or estimating and validating an empirical / behavioral / operations-data-science study. Executes and reports; it does not pick the method (pom-methods) or frame the contribution (pom-contribution-framing).
---

# Analysis & Results (pom-data-analysis)

## When to trigger

- The model is built or the data are collected and it is time to produce results
- You are unsure your numerics, identification, or validation will satisfy reviewers
- A reviewer says "the analysis does not support the inference" or "magnitude is unclear"

## Analytical / modeling papers (POM's anchor track)

For optimization, stochastic, and game-theoretic work, the "analysis" is **proof plus numerical illustration**:

- **Proofs.** State each result as a numbered proposition/theorem; give clean, complete proofs. Per POM's format, push full proofs and supporting lemmas to the unlimited online **e-companion**, leaving intuition and the key steps in the main text.
- **Structural insight.** Report the structure of the optimal policy (base-stock, threshold, (s, S)) and comparative statics — how the decision moves with cost, lead time, or competition.
- **Numerical study.** Calibrate to realistic operational parameters; report sensitivity across plausible ranges; show the managerial magnitude of the effect, not just its sign.
- **Game-theoretic checks.** Confirm equilibrium existence/uniqueness; report off-equilibrium robustness where relevant.

## Empirical, behavioral, and data-science papers

- **Identification (empirical OM).** Make the causal logic explicit; report the design (DiD/IV/RD/matching), parallel-trends or instrument validity, placebo tests, and clustered/robust standard errors matched to the operational sampling.
- **Experiments (behavioral OM).** Report randomization checks, power, manipulation and attention checks, and effect sizes; tie the result to the operational decision (e.g., order quantity, not just a rating).
- **Operations data science.** Report validation design, guard against leakage, and — decisively — the **operational value**: does the prediction improve a feasible policy or reduce a real operating cost (predict-then-optimize)?
- **Simulation.** Document parameter sources, seeds, warm-up, replications with confidence intervals, and sensitivity.

## POM-specific reporting risks

- Operational variables named but measured in units a manager cannot act on.
- Statistical significance reported in place of managerial magnitude.
- ML accuracy reported with no link to an operations policy or cost.
- Same data used in prior work without the required cover-letter disclosure.

## Checklist

- [ ] Analytical: proofs complete (in e-companion), structural results + calibrated numerics + sensitivity
- [ ] Empirical: identification stated; placebo/robustness; SE clustering matches sampling
- [ ] Experiment: randomization, power, manipulation checks, effect sizes
- [ ] Data science: validation, leakage checks, operational value demonstrated
- [ ] Results expressed in decision-relevant operational magnitude
- [ ] Same-data disclosure prepared for the cover letter

## Output format

```
【Analysis type】analytical-proof / causal / experiment / simulation / predictive
【Core result】policy structure / estimate / treatment effect / decision gain
【Main threat】proof gap / identification / leakage / measurement / power
【Managerial magnitude】effect in operational units (cost, fill rate, wait time)
【e-companion】proofs / extra analyses moved online
【Next step】pom-contribution-framing
```
