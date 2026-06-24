---
name: jmf-research-design
description: Use when defending the research design of a Journal of Marriage and Family (JMF) manuscript — longitudinal and life-course designs, dyadic and family-level analysis, family-demographic methods, experiments, and qualitative/multi-method designs. JMF judges each tradition on its own terms and is alert to selection. Strengthens the design; it does not write code.
---

# Research Design (jmf-research-design)

JMF accepts quantitative, qualitative, and multi-method work but is demanding about each. The design
must connect the framework (`jmf-theory-and-conceptual-framework`) to evidence while respecting the
**unit of analysis** (individual, dyad, family, household, cohort) and the **non-independence** of
people who share a relationship. This skill is mode-aware: pick the section that fits your work.

## When to trigger

- Specifying the design, sample, measures, and identification strategy
- A reviewer questioned **selection**, causal claims, generalizability, or the handling of dyads
- Designing a longitudinal, dyadic, family-level, or comparative study
- Preparing a pre-analysis plan or planning a replication

## Quantitative — longitudinal / family demography
- **Life-course / panel**: growth curves, cross-lagged panel, fixed effects within persons or
  couples, change-score models; be explicit about timing, sequencing, and time-varying covariates.
- **Event history / survival**: discrete- or continuous-time hazards for marriage, cohabitation,
  divorce, fertility; competing risks where multiple exits are possible.
- **Family demography**: rates, life tables, decomposition, standardization; complex-survey weights,
  clusters, and strata applied correctly.
- **Selection is the default rival.** State how you address it — fixed effects, sibling/twin designs,
  propensity methods with sensitivity, natural experiments/IV, or honest scoping to association.

## Quantitative — dyadic & family-level
- **Couples/dyads**: Actor–Partner Interdependence Model (APIM), dyadic SEM, multilevel models with
  members nested in couples; distinguish distinguishable vs. indistinguishable dyads.
- **Families with multiple members/children**: multilevel/mixed models; account for clustering within
  families; model coparenting and sibling structure where relevant.
- **Measurement**: validate constructs; report reliability; test invariance across partners, groups,
  or time before comparing.

## Experiments (lab / survey / field)
- Preregister design and primary analyses; report power/MDE for the relevant unit (often the dyad or
  family, not the person); pre-specify subgroups. Address attrition, manipulation checks, and ethics/
  IRB and consent for couples, children, and families.

## Qualitative / multi-method
- **Sampling and case logic** stated by design (theoretical, maximum-variation, paired), not
  convenience; say what the case is a case *of*.
- **Multi-perspective family data** (both partners, parents and children): plan how interdependent
  accounts are analyzed and reconciled.
- **Integration** in mixed methods: explicit joint displays; say what each strand adds.

## The selection-and-interdependence test (JMF-specific)

For the strongest rival (usually **selection**), write: *"If selection rather than my mechanism drove
this, the data would look like ___; instead they look like ___."* Then confirm the model **respects
non-independence** of partners/family members. If either fails, the design does not yet identify the
contribution.

## Design-defensibility table JMF referees apply

| Design feature | Vulnerable | Likely reviewer verdict |
|----------------|-----------|--------------------------|
| Unit of analysis | Person-rows for a couple-level question | "Unit mismatch — re-specify" |
| Selection rival | Asserted away | "Selection into family transitions" |
| Temporal structure | Cross-section for a dynamic process | "Cross-sectional claim about a dynamic process" |
| Non-independence | Independence assumed | "Dyadic dependence ignored" |

For the flagship journal of family science, the design section is judged on whether the *unit of analysis*
and *temporal leverage* fit the family process being theorized. JMF welcomes quantitative, qualitative, and
multi-method work, each on its own rigor bar.

## Worked micro-example (illustrative)

A study claims cohabitation "causes" lower relationship quality from one cross-sectional wave (illustrative).

- *Vulnerable:* a between-person snapshot where married respondents score 0.4 SD higher — read as selection
  (who marries) plus a cross-sectional claim about a process that unfolds over time.
- *Strengthened:* a panel tracking couples from cohabitation forward, using within-couple change as
  partners transition to marriage, the couple as the unit, members modeled via APIM. The estimand becomes
  *within-couple* change in dyadic quality (illustrative −0.08 SD). Adjudication: "If sorting drove this,
  gaps would predate cohabitation."

## Referee-pushback patterns and the design fix

- *"Selection into family transitions."* Add within-unit leverage (couple/sibling FE), a sensitivity
  analysis, or a credible natural experiment; else scope the claim to association.
- *"Dyadic dependence ignored."* Specify APIM, dyadic SEM, or multilevel nesting; test whether dyads are
  distinguishable rather than assuming.
- *"Cross-sectional claim about a dynamic process."* Re-anchor on a longitudinal estimand matching the
  life-course logic of the framework.

*Calibration (hedged):* preregistration and unit-appropriate power are encouraged but evolving — confirm
against the journal's current author guidance.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMF is quantitative family demography/sociology; emphasize identification, selection, and decomposition methods.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Treating couple or family data as independent observations
- "Causal" language on an observational design with unaddressed selection
- Naive cross-sectional snapshots for inherently longitudinal family processes
- Ignoring panel attrition or differential dropout in family studies
- Convenience case selection dressed up as theory-driven

## Output format

```
【Mode】longitudinal-demographic / dyadic-family / experiment / qualitative-mixed
【Unit of analysis】individual / dyad / family / household / cohort
【Estimand or claim】what is being identified/shown
【Selection handled】the adjudication sentence
【Non-independence】how clustering/dyad structure is modeled
【Robustness/sensitivity】planned checks
【Next】jmf-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — dyadic/multilevel/survival packages and family datasets
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JMF methods scope and replication guidance
