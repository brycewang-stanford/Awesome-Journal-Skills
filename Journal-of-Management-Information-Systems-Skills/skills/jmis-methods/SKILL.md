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

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMIS is empirical IS — survey-based SEM and econometric panels; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design matches the style and the strength of the claim
- [ ] IT-value/platform: a named source of exogenous variation; modern estimator where TWFE would bias
- [ ] Behavioral: validity threats and CMB designed out procedurally, not just measured
- [ ] Economic model: assumptions stated; empirical test maps to a model prediction
- [ ] Design-science: utility evaluated vs. credible baselines, tied to a managerial decision
- [ ] Core evidence fits ≤50 pages; appendix carries only support, not load-bearing claims
- [ ] The design section states why this method is the right tool for this specific claim
- [ ] Platform designs address two-sided feedback and algorithmic confounding

## Platform and e-commerce data: design around its pathologies

Platform and marketplace data — a JMIS staple — carry built-in threats that the design must anticipate, not patch later. Participation and intensity are endogenous (sellers/buyers self-select into features); two-sidedness means a shock to one side feeds back to the other, so a naive one-side regression is mis-specified; ranking/recommendation systems create feedback loops where the outcome you measure was partly caused by the system you study; and platform redesigns are often rolled out non-randomly. Build the identification around a genuine source of exogenous variation (a staged redesign, an exogenous policy or pricing change, a randomized experiment the platform ran) and state explicitly how you handle cross-side feedback and algorithmic confounding. Reviewers on platform papers will probe exactly these points.

## Anti-patterns

- A causal IT-value claim resting on a cross-sectional or correlational design
- Endogenous IT/platform choice "handled" only with control variables
- Single-source, single-wave self-report with no procedural CMB remedies
- A design-science artifact benchmarked only against strawman baselines, or with no managerial relevance
- A design that "fits" only by exporting half the evidence to an online appendix
- Method chosen for fashion (deep learning where transparent regression answers the claim better)
- A platform analysis that ignores two-sided feedback or algorithmic confounding in the data
- No statement of why this method is the right tool for this specific claim

## Make the method serve the claim, not fashion

JMIS reviewers reward a method chosen because the *claim and phenomenon* demand it, and they penalize method for method's sake. A flashy deep-learning model where a transparent regression would answer the managerial question better is a liability, not an asset; conversely, a simple OLS where the design clearly calls for a quasi-experiment will not carry a causal claim. State, in the design section, *why this method is the right tool for this claim* — what it identifies or evaluates that a simpler or fancier alternative would not. Where you combine methods (e.g., an experiment to establish a mechanism plus field data for external validity), say what each leg buys you. The method should read as the inevitable consequence of the question, not a showcase.

## Output format

```text
【Style & design】firm econometrics / platform quasi-exp / survey-experiment / analytical / build-and-evaluate
【Identification or evaluation】source of variation OR evaluation plan + credible baselines
【Validity threats handled】endogeneity / CMB / construct validity / external validity
【Fits ≤50pp?】yes / trim
【Next step】jmis-data-analysis
```
