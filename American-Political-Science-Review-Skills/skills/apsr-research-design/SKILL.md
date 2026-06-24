---
name: apsr-research-design
description: Use when defending the research design of an American Political Science Review (APSR) manuscript — causal identification for quantitative work, case selection and process tracing for qualitative work, experimental and survey-experimental design, or formal-empirical linkage. APSR judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (apsr-research-design)

APSR accepts many methodologies but is demanding about each. The design must credibly connect the
argument (`apsr-theory-building`) to evidence. This skill is mode-aware: pick the section that matches
your work and defend it against the strongest alternative explanation.

## When to trigger

- Specifying identification, case selection, or experimental design
- A reviewer questioned causal claims, case choice, external validity, or a confound
- Preparing a **pre-analysis plan** or a **Registered Report** Stage 1 design
- Justifying why your design adjudicates the rival account from `apsr-literature-positioning`

## Quantitative / causal inference
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them, don't assert them.
- **Designs**: experiments (incl. survey/conjoint), DID/event study (use modern staggered-adoption
  estimators, not naive TWFE), IV (first-stage strength, exclusion, weak-IV-robust inference), RDD
  (density/manipulation tests, bandwidth robustness), matching/weighting with balance + sensitivity.
- **Inference**: cluster at the level of treatment assignment; randomization inference for
  experiments; multiple-comparison adjustment when testing many implications.
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result?

## Qualitative / case-based
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired
  comparison) — not convenience. Say what the case is a case *of*.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument.
- **Source transparency**: archives, interviews, fieldnotes — plan how they will be documented and
  cited (see `apsr-transparency-and-data-policy`).

## Experiments (lab / survey / field)
- Preregister the design and primary analyses; report power/MDE; pre-specify subgroups.
- Address attention/manipulation checks, attrition, and ethics/IRB and consent.
- For survey experiments: sampling frame, treatment realism, and generalization claims.

## Formal-empirical linkage
- Make the **empirical test follow from the model's comparative statics**, not a loose analogy.
- Distinguish predictions that are unique to your model from those shared with rivals.

## The adjudication test (APSR-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my argument, the data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify the contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). APSR is general-interest political science — observational causal designs (DiD/IV/RDD) and survey/field experiments alike; cluster by the right unit and foreground identification.

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

- Naive TWFE on staggered treatment; clustering at the wrong level
- "Causal" language on a design that only supports association
- Convenience case selection dressed up as theory-driven
- Conjoint/survey experiments over-generalized to real-world behavior with no caveat
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】quant-causal / qualitative / experiment / formal-empirical
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】apsr-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python) and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and Registered Reports notes
