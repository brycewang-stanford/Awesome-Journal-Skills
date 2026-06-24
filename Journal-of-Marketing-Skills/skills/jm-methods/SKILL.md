---
name: jm-methods
description: Use when choosing and defending the research design for a Journal of Marketing (JM) manuscript — matching a "big tent" method (experiment, field study, survey, secondary data, qualitative) to a substantive marketing question, with field realism and identification in mind. Designs the study; it does not run the estimation (jm-data-analysis) or frame the contribution (jm-contribution-framing).
---

# Research Design, Big-Tent (jm-methods)

## When to trigger

- The question is set and you must choose a design that can actually answer it
- A reviewer will ask whether the method supports a *causal* or *managerial* claim
- You are deciding between a clean lab experiment and a messier but realer field study
- You have secondary (scanner/CRM/financial) data and need an identification strategy

## JM's "big tent" — let the question pick the method

JM is methodologically pluralistic: it welcomes **primary data** (experiments, field studies, surveys, interviews, observational data) and **secondary data**, and champions **empirics-first** research grounded in real-world phenomena. No single method is privileged. The design rule at JM is therefore: choose the method that most credibly answers a **substantive** question and supports a **managerially relevant** claim — not the most sophisticated technique. Work centered on mathematical/statistical methods for their own sake is out of scope (route to Marketing Science / JMR); methods here are **servants** of the substantive insight.

## Match design to claim

| Substantive claim / data situation                          | Design                                                      |
|-------------------------------------------------------------|-------------------------------------------------------------|
| Causal effect of a marketing action on consumer response    | Randomized experiment (lab or online panel)                 |
| Causal effect *in a real market* with realism/external validity | Randomized **field experiment** with a firm/platform     |
| Process / mechanism (why an effect occurs)                  | Experiment with mediation + moderation-of-process designs   |
| Preferences, trade-offs, willingness-to-pay                 | Survey / choice-based conjoint / discrete-choice experiment |
| Market-level dynamics from observational data               | Panel with FE; DiD / event study; synthetic control; IV     |
| Customer-base behavior (CLV, churn, response)               | Longitudinal CRM/transaction modeling                       |
| Meaning, emergent constructs, theory-building from practice | Qualitative (interviews, ethnography, archival text)        |

Combine methods (multi-study or mixed) when one design cannot establish both *internal validity* (the effect is real) and *external/managerial validity* (it matters in the market).

## Field realism and managerial validity

JM prizes evidence that travels to real decisions. Strengthen the design by: securing a **field setting or firm partner** where feasible; choosing **outcomes managers act on** (sales, CLV, conversion, welfare) over proxy attitudes alone; sampling a population the claim should generalize to; and documenting the real-world stimulus, market, and time frame so a practitioner recognizes the setting.

## Design for transparency up front

JM requires a replication packet at conditional acceptance and **encourages preregistration**. Build this in now: preregister experiments (you will later supply anonymized links and an attestation), version-control analysis scripts, and log sample-construction and exclusion rules as you go — not retroactively.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JM is empirical marketing — field experiments, panel/CRM data, and quasi-experiments; randomization inference for experiments, DiD / IV for observational claims.

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

- [ ] Method chosen to fit the substantive claim, not for sophistication
- [ ] Internal validity (randomization/identification) addressed
- [ ] External/managerial validity (field realism, actionable outcomes) addressed
- [ ] Multi-study / mixed design where one method cannot do both
- [ ] Outcomes managers/policy makers care about are measured
- [ ] Preregistration planned (experiments); scripts and exclusion rules logged
- [ ] Power/sample-size justified a priori for experiments

## Anti-patterns

- **Method-driven paper**: a clever estimator in search of a question (out of scope at JM).
- **Lab-only causal claim** asserted to hold in the market with no field/external evidence.
- **Endogenous treatment** in secondary data with no identification strategy.
- **Attitude proxies** standing in for outcomes managers actually move.
- **Retrofitted transparency**: no preregistration, exclusions documented after the fact.

## Output format

```
【Substantive claim】[...]
【Design】experiment / field experiment / survey-conjoint / panel-DiD / qualitative / mixed
【Internal validity】randomization / identification: [...]
【External & managerial validity】field realism, actionable outcomes: [...]
【Multi-study plan】[...]
【Transparency】preregistration + script/exclusion logging: [...]
【Next step】jm-data-analysis
```
