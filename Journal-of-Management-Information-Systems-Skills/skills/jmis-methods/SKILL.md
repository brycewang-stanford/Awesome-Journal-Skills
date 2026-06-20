---
name: jmis-methods
description: Use when choosing and defending the research design for a Journal of Management Information Systems (JMIS) manuscript — IT-value/platform econometrics, a behavioral survey or experiment, an analytical/economic model, or a design-science/data-science artifact. Matches the method to the IS claim and the ≤50-page budget; it designs the study and hands estimation/evaluation to jmis-data-analysis.
---

# Research Design & Methods (jmis-methods)

## When to trigger

- You have a mechanism or propositions but no defensible way to test/evaluate them
- The method may not match the claim (a causal IT-value claim resting on a cross-sectional correlation)
- A reviewer asks "what identifies this effect?" or "how do you know the artifact is useful?"
- You need to decide what evidence fits inside the **50-page** complete-manuscript ceiling

## Match the design to the JMIS research style and the strength of the claim

JMIS is methodologically broad but the design must earn the causal/economic verb in the claim.

| Style | Typical designs | The design must establish |
|-------|-----------------|----------------------------|
| **IT business value / firm** | Panel econometrics, natural experiment, DiD, IV, matching | Credible identification of IT's causal value against endogenous IT investment |
| **Platform / e-commerce** | Quasi-experiments on platform shocks, structural demand, field experiments | The network/two-sided mechanism, controlling for selection on platform data |
| **Behavioral IS** | Lab/online/field experiment, multi-wave survey, panel | Internal + construct validity and *procedural* remedies for common-method bias |
| **Economics of IS** | Analytical model; empirical test of a model's prediction | A coherent model with stated assumptions, or a test that maps to the prediction |
| **Design-science / data-science** | Build-and-evaluate of an IT/ML artifact | Novelty *and* managerial utility vs. credible baselines — not "it ran" |

## IT-value and platform empirics: identify, do not just control

IT investment and platform participation are chosen, not random. Anchor identification in a real source of exogenous variation — a policy change, a staggered system rollout, a platform redesign, a security breach, a pricing shock — and pre-commit the comparison and the assumptions you will defend. With staggered adoption, plan a modern estimator (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille) rather than naive TWFE, and design the event-study leads up front. Endogeneity that is only "controlled for" with covariates will draw reviewer fire.

## Behavioral IS: design out the threats before you collect data

Build *procedural* separations against common-method bias — temporal/source/psychological separation, validated and pretested scales, attention and manipulation checks — because statistical fixes (e.g., a marker variable) alone will not convince reviewers later. For experiments, make the IT manipulation realistic and the estimand explicit; report power.

## Design-science / data-science: plan the utility evaluation up front

A JMIS artifact paper lives on **managerial utility**, not algorithmic novelty alone. Decide before building how you will demonstrate utility: held-out benchmarks against credible (not strawman) baselines, a controlled experiment or A/B field deployment, simulation, or expert evaluation — each tied to the artifact's design rationale and to a real managerial decision. State the problem's relevance and the evaluation criteria so reviewers judge rigor *and* relevance.

## Scope the evidence to the 50-page budget

The complete manuscript is capped at **≤50 pages** (12pt, double-spaced). Online appendixes are permitted, but the main paper must be self-contained and the core claims established in the body — do not design a study whose key evidence only fits by exporting it. Survey instruments go as separate anonymized attachments. (检索于 2026-06；以官网为准.)

## Worked vignette: identifying IT business value (illustrative)

A team wants to claim that an ERP go-live raised plant productivity. A cross-section of ERP-adopters vs. non-adopters cannot carry that claim — adopters differ systematically (larger, better-managed firms self-select). The JMIS design uses the **staggered go-live timing** across plants as the variation, estimates with Callaway–Sant'Anna (not naive TWFE), pre-specifies the event-study window, and checks that pre-trends are flat before go-live. The identifying assumption — that go-live timing is not driven by anticipated productivity shocks — is argued from the institutional rollout schedule and falsified with a placebo on plants whose go-live slipped. That is the difference between "ERP correlates with productivity" and "ERP go-live raised productivity by X%."

## Referee pushback mapped to a design fix

- *"Selection — adopters are not comparable to non-adopters."* → Switch from cross-section to within-firm timing variation or a defended IV; show balance/pre-trends.
- *"How do you know the artifact is actually useful?"* (design-science) → Add an evaluation against credible baselines tied to a real managerial decision, not a benchmark of convenience.
- *"Common-method bias undermines your survey."* → Show the procedural separations you built in *ex ante*, then the statistical test; do not rely on the test alone.

## Checklist

- [ ] Design matches the style and the strength of the claim
- [ ] IT-value/platform: a named source of exogenous variation; modern estimator where TWFE would bias
- [ ] Behavioral: validity threats and CMB designed out procedurally, not just measured
- [ ] Economic model: assumptions stated; empirical test maps to a model prediction
- [ ] Design-science: utility evaluated vs. credible baselines, tied to a managerial decision
- [ ] Core evidence fits ≤50 pages; appendix carries only support, not load-bearing claims

## Anti-patterns

- A causal IT-value claim resting on a cross-sectional or correlational design
- Endogenous IT/platform choice "handled" only with control variables
- Single-source, single-wave self-report with no procedural CMB remedies
- A design-science artifact benchmarked only against strawman baselines, or with no managerial relevance
- A design that "fits" only by exporting half the evidence to an online appendix

## Output format

```text
【Style & design】firm econometrics / platform quasi-exp / survey-experiment / analytical / build-and-evaluate
【Identification or evaluation】source of variation OR evaluation plan + credible baselines
【Validity threats handled】endogeneity / CMB / construct validity / external validity
【Fits ≤50pp?】yes / trim
【Next step】jmis-data-analysis
```
