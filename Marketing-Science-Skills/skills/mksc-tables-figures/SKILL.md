---
name: mksc-tables-figures
description: Use when building the exhibits for a Marketing Science manuscript — estimate tables, model-fit tables, comparative-statics figures, and counterfactual/policy-simulation exhibits in INFORMS house style. Designs the exhibits; it does not run the estimation (mksc-data-analysis) or write the prose (mksc-writing-style).
---

# Tables & Figures (mksc-tables-figures)

## When to trigger

- Estimate or counterfactual tables are cluttered or not self-explanatory
- Comparative statics / elasticities are buried in text instead of an exhibit
- A figure does not make the model's mechanism or policy result legible
- Exhibits are off INFORMS house style

## The exhibits a modeling paper needs

A Marketing Science paper is read through its model and its counterfactuals, so the core exhibits differ from an experiments paper:

- **Estimates table.** Structural parameters (preferences, dynamics, supply) with standard errors; group by demand vs. supply; label normalizations. Report elasticities (own/cross-price) and implied margins, not just raw coefficients.
- **Model-fit table/figure.** Predicted vs. actual moments/shares/prices; in-sample and holdout. Make goodness-of-fit visible.
- **Comparative-statics figure** (analytical papers). Plot how equilibrium prices/profit/advertising move with the key parameter; annotate the counterintuitive region that is the contribution.
- **Counterfactual/policy table.** Baseline vs. counterfactual outcomes (prices, shares, profit, consumer surplus/welfare) with uncertainty intervals; decompose the driving mechanism.
- **Identification/sensitivity exhibit** where helpful (sensitivity of estimates to moments; first-stage strength).

## INFORMS house style

- Number tables and figures consecutively; give each a self-contained caption that states the model/sample and what the reader should conclude.
- Define every symbol and notation used; report units and the estimand.
- Note the estimator and standard-error type in the table notes (e.g., "GMM; standard errors in parentheses").
- Keep figures clean and grayscale-legible; the model's intuition should survive black-and-white printing.
- Heavy supporting exhibits (full parameter sets, additional counterfactuals, derivations) belong in the online appendix to keep the main text succinct.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Marketing Science is heavily structural/analytical; the chain below serves its reduced-form / field-experiment lane — structural demand and analytical modeling are outside this causal-inference toolchain.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Estimates table reports elasticities/margins, not just coefficients; SEs + estimator noted
- [ ] Model-fit exhibit (in-sample + holdout) included
- [ ] Comparative-statics figure for analytical results, annotated
- [ ] Counterfactual table: baseline vs. policy, with uncertainty + mechanism
- [ ] Every symbol/notation defined; captions self-contained; units stated
- [ ] Secondary exhibits moved to the online appendix

## Anti-patterns

- A coefficient dump with no elasticities, margins, or interpretation.
- Counterfactual numbers with no uncertainty or baseline comparison.
- Figures relying on color that vanish in grayscale.
- Captions that name the table but not the conclusion.


## Exhibit pass for Marketing Science

Treat this skill as an executable review pass, not a prose hint. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then judge whether the current manuscript answers the venue's real reader: quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Estimates】params + elasticities/margins; SEs + estimator in notes
【Fit】predicted vs actual (in-sample/holdout) exhibit present?
【Comparative statics】figure for analytical claim, annotated?
【Counterfactual】baseline vs policy + uncertainty + mechanism
【Style】notation defined; captions self-contained; grayscale-safe
【Appendix】secondary exhibits relocated
【Next step】mksc-writing-style
```
