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

| Design feature | Defensible at JMF | Vulnerable | Likely reviewer verdict |
|----------------|-------------------|-----------|--------------------------|
| Unit of analysis | Matches the family process (dyad/family) and the estimand | Person-rows for a couple-level question | "Unit mismatch — re-specify" |
| Selection rival | Named and adjudicated (FE, sibling, IV, sensitivity, or scoped) | Asserted away | "Selection into family transitions" |
| Temporal structure | Longitudinal leverage for a dynamic process | Cross-section for change | "Cross-sectional claim about a dynamic process" |
| Non-independence | Clustering/APIM/multilevel structure modeled | Independence assumed | "Dyadic dependence ignored" |
| Measurement | Validated, reliability + invariance reported | Single-item, untested comparisons | "Measure not established across groups" |
| Generalizability | Scope conditions matched to sample | Universal claim from one cohort | "Overgeneralized" |

For the flagship journal of family science, the design section is judged on whether the *unit of analysis*
and the *temporal leverage* fit the family process being theorized — not on method fashion. JMF welcomes
quantitative, qualitative, and multi-method work, but each tradition is held to its own rigor bar.

## Worked micro-example (illustrative)

A study claims cohabitation "causes" lower relationship quality, comparing cohabiting and married
respondents in one cross-sectional wave. Numbers illustrative.

- *Vulnerable design:* a between-person snapshot showing married respondents score 0.4 SD higher on
  quality. Referees read this as selection (who marries) plus a cross-sectional claim about a process that
  unfolds over time.
- *Strengthened design:* a panel of 2,100 couples tracked from cohabitation forward, using within-couple
  change as partners transition (or not) to marriage, with the couple as the unit and members modeled via
  APIM. The estimand becomes the *within-couple* change in dyadic quality around the transition (an
  illustrative −0.08 SD, 95% CI −0.16 to 0.00), not a between-group gap. Selection adjudication sentence:
  "If sorting rather than the transition drove this, quality gaps would predate cohabitation; instead they
  emerge only after." Distinguishability of partners is tested before pooling actor/partner effects.

## Referee-pushback patterns and the design fix

- *"Selection into family transitions."* Add within-unit leverage (couple/sibling FE), a sensitivity
  analysis, or a credible natural experiment; if none is available, scope the claim to association.
- *"Dyadic dependence ignored."* Specify APIM, dyadic SEM, or multilevel nesting; state whether dyads are
  distinguishable and test it rather than assuming.
- *"Cross-sectional claim about a dynamic process."* Re-anchor on a longitudinal estimand (growth, change-
  score, event-history) so the design matches the life-course logic of the framework.
- *"Convenience case dressed as theory."* For qualitative work, state the sampling logic (theoretical,
  maximum-variation, paired) and what the case is a case *of*.

## Calibration anchors (hedged where uncertain)

- The default rival at JMF for observational family research is selection; designs that visibly confront it
  travel further than designs that mention it. This is a venue-norm heuristic, not a coded rule.
- Longitudinal panels and dyadic/multilevel structures are the methodological backbone for family-process
  questions; preregistration and power for the relevant unit are encouraged but their exact expectation is
  evolving — confirm against the journal's current author guidance.

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
