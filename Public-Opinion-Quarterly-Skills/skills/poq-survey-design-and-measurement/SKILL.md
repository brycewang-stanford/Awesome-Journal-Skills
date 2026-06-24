---
name: poq-survey-design-and-measurement
description: Use when defending the survey design and measurement of a Public Opinion Quarterly (POQ) manuscript through the Total Survey Error framework — coverage, sampling, nonresponse, measurement (question wording/order/scales), mode effects, and weighting. POQ is the leading survey-methodology journal and expects AAPOR-standard rigor. Strengthens the design; it does not write code.
---

# Survey Design & Measurement (poq-survey-design-and-measurement)

This is the POQ core. Reviewers are survey scientists who will probe every link in the **Total Survey
Error (TSE)** chain. The design must credibly connect the hypotheses (`poq-theory-and-hypotheses`) to
data that measure what you claim, and you must be able to **disclose every methodological element to
AAPOR standards**. Defend each error source against the strongest alternative.

## When to trigger

- Specifying the sampling frame, questionnaire, mode, or weighting scheme
- A reviewer questioned coverage, nonresponse, question wording, mode, or representativeness
- Building the **Appendix A: Disclosure Elements** (do this here, not at the end)
- Designing a survey experiment (wording/order split-ballot, conjoint, list experiment)

## Walk the Total Survey Error chain

- **Coverage.** Frame vs. target population; who is missed (online/RDD/ABS undercoverage). State the
  target population precisely.
- **Sampling.** Probability vs. nonprobability; stratification, clustering, PSUs; selection
  probabilities. Nonprobability/online panels need an explicit representativeness argument.
- **Nonresponse.** Report unit and item nonresponse; the **response rate computed per AAPOR Standard
  Definitions** (say RR1–RR6 and show the disposition-code calculation); assess nonresponse bias, not
  just the rate.
- **Measurement.** Question wording, order, response scales, reference periods, social desirability,
  acquiescence. Validate constructs; pretest (cognitive interviews, behavior coding).
- **Mode.** Single vs. mixed mode; quantify and adjust for mode effects; do not conflate a mode
  artifact with a substantive change.
- **Adjustment / weighting.** Design weights, nonresponse adjustment, calibration/raking,
  post-stratification (incl. MRP). Report what the weights correct for and the resulting design effect.

## AAPOR disclosure (build Appendix A now)

POQ requires you to disclose — for all data reported — or link to public documentation: **funding**;
**exact question wording**; **population under study**; **sample design**; **method and dates of
collection**; **response rate and how it was calculated** (AAPOR definitions); **sample sizes and
precision of findings**; and any **design effect due to clustering and weighting**. Assemble these in
**"Appendix A: Disclosure Elements"** as you design — see `poq-transparency-and-data-policy`.

## Survey experiments
- Split-ballot wording/order experiments: randomize, report the manipulation, isolate the measurement effect.
- Conjoint / list experiments / vignettes: pre-specify estimands; address attention checks and attrition.
- Preregister design and primary analyses; report power/MDE.

## The artifact-vs-effect test (POQ-specific)

For the headline result, write one sentence: *"If this were a survey artifact (coverage / nonresponse
/ wording / order / mode / weighting) rather than a real opinion signal, the data would look like ___;
instead they look like ___."* If you cannot, the design does not yet isolate the contribution.

## Design audit table

Build a one-page audit before submission:

| TSE component | Design choice | Residual risk | Evidence or disclosure |
| --- | --- | --- | --- |
| Coverage | Frame and eligibility rule | Who is systematically absent? | Benchmark comparison or limitation |
| Sampling | Selection probabilities / panel recruitment | Selection into the sample | Weighting, calibration, or sensitivity |
| Nonresponse | Contact protocol and disposition codes | Nonresponse bias | AAPOR RR calculation plus bias check |
| Measurement | Wording, order, scale, translation | Construct mismatch or satisficing | Pretest/cognitive evidence and exact wording |
| Mode | Web/phone/mail/mixed mode | Mode-specific response pattern | Mode controls, split test, or caveat |
| Weighting | Design, nonresponse, calibration weights | Inflated variance / model dependence | Design effect and weighted/unweighted comparison |

The final article should not merely say these issues were considered; it should point readers to the appendix row, table, or supplement where each was handled.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Public Opinion Quarterly is survey methodology and public opinion; the chain serves causal/experimental claims, while survey-design and measurement contributions use their own standards (sampling, weighting, measurement error).

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

- Reporting a response rate with no AAPOR definition or calculation shown
- Treating a nonprobability online sample as representative with no argument or benchmark
- Ignoring mode effects in a mixed-mode design; conflating mode artifacts with opinion change
- Weighting the point estimate but ignoring weights/clusters in the variance (see `poq-data-analysis`)
- Leaving Appendix A disclosure until submission
- Naming the target population broadly while the frame covers only reachable or panelized respondents

## Output format

```
【Target population & frame】coverage gaps named
【Sample design】probability/nonprobability; strata/clusters/PSUs
【Nonresponse】RR definition + value + bias assessment
【Measurement】wording/order/scale + validation + pretest
【Mode】single/mixed; mode effect handled?
【Weighting】what it corrects + design effect
【Artifact ruled out】the artifact-vs-effect sentence
【Design audit】TSE table complete; residual risks disclosed
【Appendix A started?】[Y/N]
【Next】poq-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — complex-survey, weighting, measurement, and pretesting tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AAPOR disclosure elements and Standard Definitions
