---
name: respol-methods
description: Use when research design, identification, or measurement is the bottleneck for a Research Policy (RP) manuscript — choosing and defending a method (patent/bibliometric, causal policy evaluation, survey, case study, or mixed) appropriate to an innovation-studies claim. Sets the design; it does not execute the estimation/coding (respol-data-analysis).
---

# Methods (respol-methods)

## When to trigger

- The design is a default (OLS + controls, or a single case) and a referee questions whether it can support the claim
- A patent or bibliometric indicator is used as if it transparently measures "innovation" or "knowledge"
- A policy-evaluation paper rests on before/after comparison without an identification strategy
- A survey reports correlations vulnerable to common-method bias or selection
- A mixed-methods paper is really two studies stapled together with no integration logic

## The Research Policy methods bar: pluralism with construct discipline

RP privileges **no single technique** — econometrics, bibliometrics/patent analysis, surveys, case studies, and mixed methods are all first-class — but it demands that the method *fit the innovation-studies claim* and that **constructs be defended**. The recurring RP failure is not weak statistics; it is treating an indicator (patents, citations, R&D spend) as if it were the latent thing (invention, knowledge flow, innovation effort). State what each measure does and does not capture, and design around its known biases.

## Design paths by method

### Patent / bibliometric quantitative
- **Construct validity first.** Patents measure *patentable invention propensity*, not innovation; citations measure *traceable knowledge linkage*, not knowledge value. Justify the indicator for your claim and acknowledge truncation, sectoral propensity, and home/strategic bias.
- **Citation hygiene.** Distinguish examiner- vs. applicant-added citations; correct self-citations; handle citation truncation (fixed windows or quasi-structural correction).
- **Endogeneity.** Patent/co-patent measures of spillovers are endogenous to firm location and choices — defend with design (instruments, natural experiments) or bound the bias, don't assume exogeneity.
- **Family/coverage.** State the patent office(s), family definition (DOCDB/INPADOC), and the matching of patents to firms/regions.

### Causal policy evaluation (R&D subsidies, missions, IP reform)
- Move beyond naive before/after: DID with a credible control (and, for staggered policy rollout, Callaway-Sant'Anna / Sun-Abraham / de Chaisemartin-D'Haultfœuille rather than plain TWFE); IV with a defended exclusion restriction; RDD at an eligibility threshold with density and covariate-smoothness checks.
- Tie the estimand to the **innovation mechanism** (additionality vs. crowding-out, direction vs. rate of innovation), and argue policy-invariance for any counterfactual.

### Survey (firm innovation behavior, CIS-style)
- Report sampling frame, response rate, and non-response/selection checks; address common-method bias by design (separated sources, marker variables, Harman is necessary not sufficient).
- Establish measurement validity (construct definitions, reliability, discriminant validity) before structural claims; state the population the estimates generalize to.

### Case study / qualitative
- Justify case selection on theoretical grounds (typical, extreme, polar); specify data sources and triangulation; pursue analytic (not statistical) generalization; show how rich data became constructs.

### Mixed methods
- State the **integration logic**: does the qualitative work generate the mechanism the quantitative work tests, or do the strands triangulate a construct? RP rejects "two papers in one" with no sequencing rationale.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Research Policy is innovation studies — patent/firm panels with selection; foreground identification and the selection objection.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The method is chosen to fit the innovation-studies claim, not by convenience or fashion
- [ ] Each patent/bibliometric indicator's construct meaning and known biases are stated
- [ ] Citation measures handle examiner/applicant, self-citation, and truncation
- [ ] Causal designs use a credible counterfactual and modern staggered-treatment estimators where TWFE would bias
- [ ] Surveys report response/selection and address common-method bias by design
- [ ] Qualitative work defends case selection and generalization type
- [ ] Mixed methods state an explicit integration logic

## Anti-patterns

- "Patents = innovation" with no construct caveat
- Spillover claims from co-location/citations treated as exogenous
- Plain TWFE on a staggered policy rollout with no heterogeneity discussion
- Survey structural models with unaddressed common-method bias
- A single case framed as if it gave statistical generalization
- Mixed methods with no sequencing or integration rationale

## Output format

```text
【Journal】Research Policy
【Skill】respol-methods
【Method】patent-bibliometric / causal-policy-eval / survey / case / mixed
【Construct defense】what the measure captures and its biases
【Identification / validity】counterfactual / first-stage / selection / triangulation
【Innovation-mechanism link】how the design speaks to the mechanism
【What it does NOT support】...
【Verdict】pass / revise / reroute
【Next skill】respol-data-analysis
```
