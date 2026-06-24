---
name: io-research-design
description: Use when defending the research design of an International Organization (IO) manuscript on international-level questions — causal identification with dyadic/TSCS/network data, case selection and process tracing for international cases, survey/conjoint experiments on foreign-policy attitudes, or formal-empirical linkage. IO judges each IR tradition on its own terms and verifies results and proofs before final acceptance. Strengthens the design; it does not write code.
---

# Research Design (io-research-design)

IO accepts quantitative, formal, and qualitative IR work but is demanding about each. The design must
credibly connect the **IR theory** (`io-theory-building`) to evidence at or across the **international
level**, and rule out the strongest rival international explanation. This skill is mode-aware: pick the
section that matches your work.

## When to trigger

- Specifying identification, case selection, or experimental design for an IR question
- A reviewer questioned causal claims, the level of analysis, generalization, or a confound
- Preparing a pre-analysis plan for a foreign-policy experiment
- Justifying why the design adjudicates the rival IR account from `io-literature-positioning`

## Quantitative / causal inference (often dyadic, TSCS, or network)
- **Get the level of analysis right.** State the unit (state-year, dyad-year, IGO, directed dyad,
  sub-state, transnational) and why it matches the theory. Many IR mistakes are unit/level mistakes.
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity); defend them, don't assert them.
- **IR-specific inference traps**: non-independence in **dyadic data** (cluster on both members /
  multiway, or use AME/network models); spatial and temporal dependence in TSCS; selection into
  alliances/treaties/conflict; reverse causation (does the institution cause the behavior or vice versa).
- **Designs**: natural experiments and DID/event study (modern staggered estimators, not naive TWFE),
  IV with credible exclusion at the international level, RDD where thresholds exist, matching/weighting
  with balance + sensitivity, gravity/PPML for trade flows.
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result?

## Qualitative / case-based (international cases)
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired comparison
  across dyads or institutions) — say what the case is a case *of* in IR terms.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the international mechanism.
- **Source transparency**: archives, diplomatic records, elite interviews — plan documentation and
  citation now (QDR; see `io-transparency-and-data-policy`).

## Experiments (survey / conjoint / lab on foreign-policy attitudes)
- Preregister design and primary analyses; report power/MDE; pre-specify subgroups.
- Be explicit about **external validity**: from public-opinion or elite-survey results to actual
  state behavior is a real inferential leap — caveat it.

## Formal-empirical linkage (a core IO design)
- Make the **empirical test follow from the model's comparative statics**, not a loose analogy.
- Distinguish predictions **unique to your model** from those shared with rival IR theories.
- Plan the **proof appendix** the IO editorial staff will verify before final acceptance.

## The adjudication test (IO-specific)

For the **single strongest rival international explanation**, write one sentence: *"If the rival were
true rather than my argument, the international data/cases would look like ___; instead they look like
___."* If you cannot, the design does not yet identify the IR contribution.

## Worked design vignette (illustrative): a treaty-ratification design

Claim: ratifying an international monitoring treaty raises later compliance. The naive cross-section
confounds the effect with **selection into membership** — states that mean to comply ratify. An
IO-credible design exploits **variation in ratification timing**: among eventual ratifiers, treat the
staggered timing as identification with a modern staggered DID/event-study estimator (not naive TWFE) and
report pre-trends. The adjudication sentence: *if selection drove compliance, the gain would appear
before ratification; instead it appears only after and tracks monitoring intensity.* A sensitivity check
then asks how strong an unobserved confounder must be to overturn it (say, twice the observed regime-type
effect — illustrative). Timing-based identification, a rival-ruling counterfactual, and a sensitivity
bound convert an association into an IR causal claim at IO.

## Identification-threat table (IR-specific confounds and the design answer)

| Threat | Where it appears | Design answer |
|--------|------------------|---------------|
| Selection into treaty/alliance/IO membership | compliance, cooperation studies | ratification-timing, instrument, or selection model + sensitivity |
| Dyadic / network non-independence | any dyad-level outcome | multiway/dyadic-robust SEs or AME/latent-space models |

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). International Organization is IR — country/dyad panels with difficult identification; foreground the source of variation and robustness to alternative explanations.

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

- Ignoring dyadic non-independence; clustering at the wrong level; naive TWFE on staggered treatment
- A domestic-level design used to support an international-level claim (level mismatch)
- "Causal" language on a design that only supports association across states
- Convenience case selection dressed up as theory-driven
- Over-generalizing survey-experiment attitudes to real state behavior with no caveat
- Treating treaty membership as exogenous when ratification is plainly a choice

## Output format

```
【Mode】quant-causal / qualitative / experiment / formal-empirical
【Level of analysis】unit + why it matches the IR theory
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended (incl. dyadic/TSCS dependence)
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity / proof appendix】planned
【Next】io-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — dyadic/network/gravity packages and CAQDAS for qualitative IR
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — formal-proof and quantitative-result verification policy
