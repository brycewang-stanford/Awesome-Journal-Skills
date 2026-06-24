---
name: etp-data-analysis
description: Use when executing or defending the analysis for an Entrepreneurship Theory and Practice (ETP) manuscript — estimation, event-history, SEM, endogeneity, and qualitative coding rigor, with the new-venture inference problems front of mind.
Runs the analysis; it does not choose the design (etp-methods) or frame the contribution (etp-contribution-framing).
---

# Data Analysis (etp-data-analysis)

## When to trigger

- The estimator is chosen but endogeneity, selection, or survivorship is not yet addressed in the numbers
- You used TWFE/OLS on staggered or time-varying venture data without checking for bias
- A time-to-event outcome (founding, exit, failure, IPO) is modeled with a linear regression
- A reviewer asks for robustness, an alternative specification, or an IV/control-function
- Qualitative coding needs an analysis plan a methods reviewer will accept

## The ETP analysis bar

ETP wants analysis that the **theory can stand on** and that survives the new-venture inference traps.
Because the journal is method-plural, "analysis" differs by branch — but every branch must (a) match the estimator to the outcome and the entrepreneurial data structure, (b) confront endogeneity/selection head-on, and (c) report uncertainty honestly.
ETP house style follows **APA**: report effect sizes and confidence intervals, not a forest of significance asterisks standing in for substance.

## Branch paths

### Quantitative — outcome-appropriate estimation
- **Time-to-event** (founding, exit, failure, IPO): use survival / event-history (Cox, discrete-time hazard, competing risks).
  Modeling "did it exit (0/1)" with OLS throws away timing and censoring information.
- **Counts / rare events** (patents, hires, funding rounds): negative binomial / zero-inflated where overdispersion or excess zeros bite, not OLS.
- **Bounded / proportion** outcomes (survival rate, equity share): fractional/beta models, not naive linear.
- **Panel with staggered timing** (policy/financing shocks across cohorts): beyond TWFE — Callaway–Sant'Anna, Sun–Abraham — with a clean event-study and pre-trend evidence.

### Endogeneity and selection (the ETP reflex)
- **Selection into founding / survival**: Heckman / control-function when the sample conditions on success; report the exclusion restriction's logic.
- **IV**: strong first stage; with weak instruments use weak-IV-robust inference; defend exclusion in institutions and theory, not just statistically.
- **Reverse causality** (does growth cause financing or vice versa): lagged designs, shocks, or dynamic panel (system-GMM) with instrument-count discipline.

### SEM / measurement models
- Report CFA fit (CFI, RMSEA, SRMR), composite reliability, AVE, and discriminant validity (HTMT) for entrepreneurial constructs; test common-method bias when self-report dominates (marker variable, not just Harman's single factor).

### Qualitative analysis
- A transparent coding scheme, the Gioia data structure as an exhibit, inter-coder agreement where appropriate, and traceability from quotation → code → theoretical dimension.
  The output is a process model, not a code count.

## Make the magnitude mean something for practice

ETP's dual mandate reaches the results: translate coefficients into the venture-relevant scale (a hazard ratio as "ventures with X fail 30% faster," a marginal effect as "one more co-founder shifts funding probability by Y points").
A practitioner implication needs a magnitude, not a p-value.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ETP is entrepreneurship, where selection and survival bias are pervasive — foreground identification and selection corrections.

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

- [ ] Estimator matches the outcome type (hazard for time-to-event; count/fractional models where appropriate)
- [ ] Selection/survivorship addressed in the analysis, not just acknowledged
- [ ] Endogeneity strategy stated with a defended exclusion/identification logic
- [ ] Staggered designs use modern DID with pre-trend evidence (no naive TWFE)
- [ ] SEM: fit indices, reliability, AVE, discriminant validity, CMB test reported
- [ ] Qualitative: data structure, coding transparency, quotation traceability
- [ ] Effects reported with magnitudes and CIs (APA), translated for practice

## Anti-patterns

- **Linear regression on a time-to-event outcome** (ignores censoring and timing)
- **Selection/survivorship acknowledged in prose but absent from the model**
- **Asterisk theater** — significance stars substituting for effect sizes and CIs
- **Naive TWFE** on staggered venture/policy data with no heterogeneity-bias check
- **Harman's single factor** offered as if it settled common-method bias
- **Code counts** presented as if they were a process theory

## Worked vignette (illustrative)

A team wants to test whether accelerator participation raises venture survival, using cohorts admitted across several years and a binary "survived to year 3" outcome.
The first draft runs OLS on the 0/1 outcome with year and region controls.
Three ETP-specific upgrades: (1) the outcome is fundamentally *time-to-event* — recast as a discrete-time hazard or Cox model with competing risks (acquired vs. shut down vs. still operating), recovering the timing and censoring OLS discards; (2) accelerators *select* promising ventures, so survival differences may be selection, not treatment — exploit a plausibly exogenous admission threshold (a scoring cutoff supports a regression-discontinuity or fuzzy-RD design) rather than controls alone; (3) because cohorts enter in staggered years and the program changed over time, a naive two-way fixed-effects "treatment" coefficient can be biased — use a modern staggered-DID estimator with a pre-trend check.
Finally, report the hazard ratio with a CI and translate it: "admitted ventures fail roughly 25% slower over three years," a magnitude an accelerator director can act on.

## Output format

```text
【Journal】Entrepreneurship Theory and Practice
【Branch】quantitative / SEM / qualitative
【Outcome→estimator】outcome type + matched model
【Selection/survivorship】how addressed in the numbers
【Endogeneity】IV / control-function / lagged / dynamic panel + exclusion logic
【Inference】effect sizes + CIs (APA); CMB if self-report
【Magnitude for practice】coefficient translated to venture scale
【Next skill】etp-contribution-framing
```
