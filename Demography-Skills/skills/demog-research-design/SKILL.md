---
name: demog-research-design
description: Use when defending the research design of a Demography (PAA / Duke University Press) manuscript — choosing among demographic methods (life tables, decomposition, event-history/survival, age-period-cohort, multistate, microsimulation, projections) and, where the question is causal, defending identification. Demography judges each method on its own terms. Strengthens the design; it does not write code.
---

# Research Design (demog-research-design)

Demography accepts a wide variety of methodological approaches but is demanding about each. The design
must credibly connect the argument (`demog-theory-building`) to the demographic evidence. This skill is
method-aware: pick the section that matches your question and defend it against the strongest rival
explanation.

## When to trigger

- Choosing the demographic method that actually answers the question
- A reviewer questioned the rate construction, the identification, or the projection assumptions
- Specifying an age-period-cohort, multistate, or microsimulation design
- Justifying why your design adjudicates the rival account from `demog-literature-positioning`

## Match the method to the question

- **Life tables** — for survival, life expectancy, and exposure: period vs. cohort, abridged vs.
  complete; multiple-decrement (cause-specific) and multistate (healthy/disabled) where relevant.
- **Decomposition** — to attribute a difference or change in a rate to components: Kitagawa
  (rate vs. composition), Arriaga (age contributions to e0), Horiuchi continuous, Das Gupta
  (multi-factor). Say exactly **what each component means**.
- **Event-history / survival** — for timing and transitions: Cox, parametric, discrete-time, with
  **competing risks** and **multistate** models when several destinations matter; check the
  proportional-hazards assumption.
- **Age-period-cohort** — confront the **identification problem head-on**: APC effects are linearly
  dependent, so state the constraint or modeling assumption (and its substantive justification) you
  rely on; do not present a single "identified" APC partition as if it were assumption-free.
- **Multistate / projections / microsimulation** — make transition rates, the base population, and the
  assumptions (closed/open, period/cohort) explicit; report sensitivity to key assumptions.

## When the question is causal
- **Identification first.** State the estimand and the assumptions licensing a causal reading
  (ignorability, parallel trends, exclusion, continuity); defend them, don't assert them.
- **Selection and exposure** are demographic hazards: mortality selection, migration selection, and
  differential exposure can masquerade as effects — address them explicitly.
- **Inference.** Cluster at the right level (e.g., household, region, cohort); use survey weights and
  design for complex samples; report uncertainty for derived demographic quantities.
- **Sensitivity.** How strong must an unobserved confounder (or a violated rate assumption) be to
  overturn the result?

## The adjudication test (Demography-specific)

For the **single strongest rival explanation** (e.g., compositional change, selection, tempo
distortion), write one sentence: *"If the rival were true rather than my account, the age/cohort
pattern would look like ___; instead it looks like ___."* If you cannot, the design does not yet
identify the contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Demography is formal + empirical demography; the causal chain serves its reduced-form lane, while formal demographic modeling uses its own tools — decomposition (`oaxaca` / `gelbach`) is often central.

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

- Running a regression when the question calls for a life table, a decomposition, or an event-history model
- Presenting an APC decomposition without naming the identifying constraint
- Period rates read as cohort experience (or vice versa) without justification
- Ignoring mortality/migration selection in a survival or panel design
- Projections whose assumptions are buried instead of varied and reported

## Output format

```
【Method】life table / decomposition / event history / APC / multistate / microsim / projection / causal
【Quantity / estimand】what is being measured or identified
【Key assumption(s)】and how each is defended (name the APC constraint if used)
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】demog-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — life-table, decomposition, survival, APC, and microsimulation packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Demography scope and methodological breadth
