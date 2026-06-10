---
name: orgsci-data-analysis
description: Use when analyzing and reporting results for an Organization Science manuscript across its eclectic methods — establishing trustworthiness for qualitative work, the right estimator for quantitative/multilevel data, transparency for simulation/formal models, and mechanism-supported inference where causal identification is impossible. Executes and reports the analysis; it does not design the study (orgsci-methods) or frame the contribution (orgsci-contribution-framing).
---

# Data Analysis & Transparency (orgsci-data-analysis)

## When to trigger

- Data are collected (or a model built) and it is time to analyze and report
- A reviewer says "the analysis does not support the inference"
- You are unsure how to demonstrate rigor for qualitative, computational, or formal work
- Your estimator may not match your design (nested, time-to-event, latent constructs)

## Rigor is method-specific — report what your design demands

Because Organization Science is methodologically eclectic, "rigor" looks different by method. Report the standard that fits, transparently.

- **Qualitative / inductive.** Validity becomes **trustworthiness**: a data structure (first-order codes → second-order themes → aggregate dimensions), an audit trail, and representative quotations so the path from raw data to constructs is traceable; state case-selection logic, saturation, and how disconfirming evidence was handled.
- **Quantitative / multilevel.** Match the estimator to the design: multilevel/HLM for nested data (justify aggregation with ICC(1), ICC(2), r_wg), SEM for latent constructs and mediation, fixed/random effects and event-history for panel/founding-failure data; cluster SEs to the nesting structure.
- **Experimental.** Report manipulation and attention checks, randomization balance, and effect sizes — not just p-values; pre-register where feasible.
- **Computational / simulation.** Report parameter ranges, sensitivity analyses, seeds, and number of runs; show the qualitative pattern's robustness and make the mechanism visible.
- **Formal-analytical.** State assumptions and prove or numerically verify the comparative statics; show which results are general and which are knife-edge.

## Inference without identification

The venue holds that causal inference is valued but "not necessary and often impossible." Where clean identification is unavailable, support inference with **mechanism evidence, theoretical logic, institutional knowledge, triangulation, and falsification/placebo logic**, and rule out alternatives empirically where possible. Do not overclaim causality; do not abandon a credible mechanism for want of an instrument.

## Replicability (not a deposit mandate)

Provide enough detail and references that others could replicate the work; be prepared to provide raw data for editorial review on request and to retain data after publication. Organization Science applies a replicability/data-retention-on-request standard rather than Management Science's mandatory code-and-data deposit mandate — but keep clean, regenerable scripts regardless.

## Anti-patterns

- OLS on nested data (use HLM); causal-steps mediation instead of bootstrapped indirect effects.
- Qualitative findings with no data structure or audit trail — thick description as "analysis."
- Simulation from a single parameter set with no sensitivity analysis.
- Causal language the design cannot support; specification fishing.


## Evidence pass for Organization Science

Use this as a second-pass capability check. First lock a level map, a mechanism paragraph, and the cover-letter contribution statement; then test whether the manuscript addresses interdisciplinary organization reviewers who ask whether the mechanism travels across levels of analysis.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against AMJ for empirical management framing, ASQ for organization-theory depth, Management Science for formal/quantitative operations; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Method】qualitative / multilevel / panel-EH / experiment / simulation / formal
【Rigor evidence】trustworthiness (data structure, audit trail) OR estimator + SE clustering OR sensitivity/seeds OR proofs
【Inference】identification? if not — mechanism + design logic + falsification; alternatives ruled out
【Replicability】detail/scripts retained; data-on-request ready
【Next step】orgsci-contribution-framing
```
