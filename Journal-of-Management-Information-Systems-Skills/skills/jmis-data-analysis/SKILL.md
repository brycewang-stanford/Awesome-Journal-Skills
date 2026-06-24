---
name: jmis-data-analysis
description: Use when the estimation, identification, construct validity, or modeling is the bottleneck for a Journal of Management Information Systems (JMIS) manuscript — econometrics on firm/platform data, SEM/PLS for behavioral constructs, analytical-model derivations, or ML/analytics evaluation. Executes and stress-tests the analysis the design (jmis-methods) chose; it does not redesign the study.
---

# Data Analysis (jmis-data-analysis)

## When to trigger

- A regression "works" but the identifying variation and threats are not pinned down
- A survey model is run but reliability, validity, and common-method bias are not established
- An ML/analytics artifact reports accuracy but no credible-baseline comparison or robustness
- A reviewer says results are "not robust," "not identified," or "could be reverse causality"

## Run the analysis to the JMIS standard for your evidence type

JMIS reviewers are method-literate across econometrics, psychometrics, analytical modeling, and data science. The bar is that the analysis credibly supports the verb in your claim.

### Empirical IT-value / platform econometrics
- **Identification, made visible.** Show the source of variation (shock/rollout/breach), not just the regression. With staggered timing, use Callaway–Sant'Anna / Sun–Abraham / de Chaisemartin–D'Haultfœuille and report a clean event study with leads; for naive TWFE, run a Goodman-Bacon decomposition to expose contamination.
- **Endogeneity head-on.** For IT investment and platform participation, address reverse causality and selection: IV with a defended exclusion restriction and a strong first stage (weak-IV-robust inference if not), or a credible quasi-experiment; do not lean on "we control for X."
- **Inference.** Cluster at the assignment/treatment level; handle few clusters (wild-cluster bootstrap); report robustness to specification, sample, and functional form.

### Behavioral IS (survey / experiment)
- **Measurement first.** Report reliability (composite reliability / α), convergent and discriminant validity (AVE, HTMT), and confirm the measurement model before the structural model.
- **Common-method bias.** Go beyond Harman's single-factor test — use a marker/measured latent-method variable and report whether structural paths survive.
- **Structural model.** SEM (CB-SEM) or PLS as the theory and sample justify; for moderation/mediation use proper interaction or indirect-effect tests (bootstrapped indirect effects), not a chain of separate regressions.

### Analytical / economic models
- State assumptions; prove the propositions; present comparative statics as the result. Sketch proofs in the body, full proofs in an appendix. Show the insight is not an artifact of a knife-edge assumption (robustness to functional form / parameter ranges).

### Design-science / ML artifacts
- Benchmark against **credible** baselines (strong incumbents, not strawmen); report appropriate metrics with variance/uncertainty; validate out-of-sample; tie performance back to the managerial decision the artifact serves.

## Report effects so a manager can read them

JMIS values managerial relevance: report **economic magnitude** (elasticities, marginal effects, dollar value, lift), not only significance. Translate the headline coefficient into what it means for a firm, platform, or decision.

## Worked vignette: making robustness answer a threat (illustrative)

A referee writes "the result is not robust." A weak reply adds ten specifications and reports they are "all significant." A JMIS-grade reply names the *threat each check defends against*: a placebo on a period before the platform change rules out a secular trend; an alternative control group rules out a coincident shock; a sensitivity analysis (e.g., Oster-style bounds on selection) shows the estimate survives plausible unobserved confounding; an alternative measure of the construct rules out operationalization artifacts. Robustness is not a quantity of regressions; it is a mapping from each surviving threat to the check that kills it.

## Translate the headline into a managerial number

Suppose the main coefficient implies the ranking redesign cut marginal-seller retention by 6 percentage points. State it that way, then carry it to the platform decision: at the observed seller base that is roughly N exits per quarter and a Y% variety reduction (illustrative). A JMIS reader wants the economic magnitude and its managerial reading, not just `p < 0.01`.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMIS is empirical IS — survey-based SEM and econometric panels; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

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

- [ ] Empirical: identifying variation named; modern estimator where TWFE would bias; endogeneity addressed, not just controlled
- [ ] Behavioral: reliability + convergent/discriminant validity reported; CMB tested beyond Harman's
- [ ] Mediation/moderation tested with proper indirect-effect / interaction methods
- [ ] Analytical: assumptions stated, propositions proven, robustness to functional form shown
- [ ] ML: credible baselines, uncertainty reported, out-of-sample validation
- [ ] Inference: clustering correct; robustness to spec/sample shown
- [ ] Magnitudes, not just significance, are reported and interpreted for managers
- [ ] Reverse causality/selection pre-empted (timing, within-unit, sensitivity bounds)
- [ ] Body is self-contained; sample construction, estimator, and inference are traceable

## Pre-empt the reverse-causality reflex

On IT-value and platform papers, the most common first-round attack is "this could be reverse causality or selection." Do not wait for it — pre-empt it in the analysis. Show the timing (the cause precedes the effect), use within-unit variation that differences out fixed selection, lean on a quasi-experimental shock where you have one, and where you must use an instrument, defend the exclusion restriction on institutional grounds and report weak-IV-robust inference if the first stage is not strong. Then bound what remains: a selection-sensitivity analysis (e.g., Oster-style δ/bounds) tells a referee how much unobserved confounding it would take to overturn the result. Anticipating the endogeneity objection inside the paper is worth more than answering it in a rebuttal.

## Anti-patterns

- "The coefficient is significant" presented as if it were identification
- Endogenous IT/platform variables left to control variables
- Reporting only Harman's single-factor test as the CMB defense
- Discriminant validity skipped; constructs that empirically overlap treated as distinct
- ML accuracy against strawman baselines, or with no out-of-sample check
- Significance stars with no economic magnitude or managerial interpretation
- Waiting for the reverse-causality objection instead of pre-empting it with timing/within-unit/sensitivity evidence
- A robustness section that adds specifications without naming the threat each one defends against
- A load-bearing analysis that exists only in the online appendix, not the body

## Keep the analysis reproducible and self-contained

JMIS submissions are double-anonymized and capped at 50 pages, which shapes how you present analysis. Online appendixes are permitted, but the body must stand on its own: a reviewer should be able to follow the identification and the headline result without the appendix, and should never find that a load-bearing robustness check exists only there. Document the sample construction, the estimator, the software/version, and the inference choices clearly enough that the result is traceable; if you reference your own prior code or data, phrase it so it does not de-anonymize you. Tighten the analysis narrative — full diagnostic batteries and secondary specifications belong in the appendix, while the body carries the chain that establishes the contribution.

## Hand a stable headline to the next stage

Do not move to `jmis-contribution-framing` while the headline number is still drifting across specifications. The contribution sentence and the exhibits both depend on a settled effect size and a settled inference, so lock the preferred specification, confirm it survives the robustness battery, and fix the economic-magnitude interpretation before framing the claim. A contribution built on a coefficient that later moves forces a rewrite of the intro, the discussion, and the abstract.

## Output format

```text
【Evidence type】firm/platform econometrics / survey-SEM / experiment / analytical / ML
【Identification or validity】variation source + diagnostics / measurement model + CMB test / proof + robustness
【Inference】clustering / weak-IV-robust / bootstrap as applicable
【Magnitude】economic/managerial interpretation of the headline effect
【Robustness done】spec / sample / functional-form / out-of-sample
【Next step】jmis-contribution-framing
```
