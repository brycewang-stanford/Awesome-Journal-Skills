---
name: jibs-methods
description: Use when designing the empirical study for a Journal of International Business Studies (JIBS) manuscript — matching a cross-country and/or multilevel design to the question, planning for measurement equivalence, common-method variance, and endogeneity before data collection. Designs the study; it does not run the estimation (jibs-data-analysis) or build the mechanism (jibs-theory-development).
---

# Cross-Country & Multilevel Research Design (jibs-methods)

## When to trigger

- You are choosing a design for a cross-border or multi-country question
- Your data are nested (individuals in firms in countries) and you need the right structure
- You anticipate reviewers probing measurement equivalence, CMV, or endogeneity
- A reviewer says "the design cannot support a cross-country inference"

## JIBS is method-pluralistic; rigor is the gatekeeper

JIBS is **paradigmatically and methodologically pluralistic** by policy — quantitative, qualitative, mixed, and pure-theory work are all in scope. There is **no single mandated method**. But its practical center of gravity is **theory-driven, hypothesis-testing empirical work on cross-country or multilevel data**, held to demanding standards. Pick the design that fits the phenomenon, then engineer in the three rigor demands JIBS reviewers apply most insistently.

## Match the design to the claim

| Phenomenon / claim                                   | Design                                                        |
|------------------------------------------------------|---------------------------------------------------------------|
| Country/culture shapes a firm or individual outcome  | Multilevel (firm/individual nested in country), with country-level predictors |
| Internationalization as a path-dependent process     | Longitudinal/dynamic panel of firms over time (FDI, entry, commitment) |
| Cross-cultural attitudes/behavior                    | Multi-country survey with translated, back-translated instruments |
| Entry-mode / location / governance choice            | Discrete-choice archival design on cross-border deals (SDC, fDi Markets) |
| Deep contextual MNE puzzle                            | Comparative / multi-country case study (qualitative)          |

## Build in JIBS's three rigor demands at the design stage

1. **Cross-national measurement equivalence.** Because constructs are studied across countries and cultures, plan multi-group measurement from the outset: identical (translated/back-translated) instruments, and a plan to test configural, metric, and scalar invariance. Equivalence is a *first-order* concern at JIBS, not an afterthought.
2. **Common-method variance (CMV).** JIBS actively gatekeeps CMV: survey/same-respondent designs that appear to suffer from CMV are routinely asked to run validity checks and resubmit, per a dedicated "From the Editors" CMV editorial. Design *procedural* remedies now — temporal/source separation, different respondents for predictor and outcome, archival anchors, a marker variable.
3. **Endogeneity / "dynamic endogeneity."** For internationalization-as-process designs, JIBS names dynamic endogeneity as a recurring demand: past internationalization, performance, and unobserved firm heterogeneity co-evolve. Plan identification now — instruments, dynamic-panel GMM, lag structure, or a natural experiment — rather than bolting it on later.

## Consult the methods-editorial canon

The AIB Research Methods SIG curates ~28 JIBS "From the Editors" methods editorials (2008–2022) on endogeneity, multilevel models, interaction effects, QCA, replication/reproducibility, CMV, and p-values. Reviewers treat these as de facto standards — align your design with the relevant editorial and cite it.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIBS is international business — cross-country panels with confounded institutions; emphasize fixed effects, clustering, and endogeneity of location / entry choices.

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
## Output format

```
【Design】multilevel / dynamic-panel / multi-country survey / archival choice / case ...
【Levels & nesting】 ... ; SE-clustering/aggregation plan
【Measurement equivalence plan】translation + configural/metric/scalar test ...
【CMV plan】procedural separations designed ...
【Endogeneity/dynamic-endogeneity plan】identification strategy ...
【FTE editorial alignment】which editorial(s) the design answers to ...
【Next step】jibs-data-analysis
```

## Anti-patterns

- Pooling countries with no plan to test measurement invariance.
- A single-source, single-wave, same-respondent cross-country survey with no CMV remedy.
- Internationalization-process design with no endogeneity strategy.
- Choosing a method by habit rather than fit to the phenomenon.
