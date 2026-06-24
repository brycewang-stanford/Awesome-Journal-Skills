---
name: bjps-research-design
description: Use when defending the research design of a British Journal of Political Science (BJPS) manuscript — causal identification for quantitative work, case selection and process tracing for qualitative work, experimental and survey-experimental design, or formal-empirical linkage. BJPS judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (bjps-research-design)

BJPS accepts many methodologies but is demanding about each. The design must credibly connect the
argument (`bjps-theory-building`) to evidence, and — because BJPS is international and cross-subfield —
make the case generalize beyond a single setting. This skill is mode-aware: pick the section that
matches your work and defend it against the strongest alternative explanation.

## When to trigger

- Specifying identification, case selection, or experimental design
- A reviewer questioned causal claims, case choice, external validity, or a confound
- Preparing a **pre-analysis plan** for an experiment or observational study
- Justifying why your design adjudicates the rival account from `bjps-literature-positioning`

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
  comparison) — not convenience. Say what the case is a case *of*, and what it generalizes to.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument.
- **Source transparency**: archives, interviews, fieldnotes — plan how they will be documented and
  cited (see `bjps-transparency-and-data`).

## Experiments (lab / survey / field)
- Preregister the design and primary analyses; report power/MDE; pre-specify subgroups.
- Address attention/manipulation checks, attrition, and ethics/consent.
- For survey experiments: sampling frame, treatment realism, and the generalization claim — BJPS
  reviewers ask whether a single-country experiment speaks to a general mechanism.

## Formal-empirical linkage
- Make the **empirical test follow from the model's comparative statics**, not a loose analogy.
- Distinguish predictions that are unique to your model from those shared with rivals.

## The adjudication test (BJPS-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my argument, the data would look like ___; instead they look like ___."* Then add the
**generalization sentence**: *"This design speaks beyond my case because ___."* If you cannot write
both, the design does not yet identify a contribution of general interest.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). BJPS is comparative/IR-heavy — cross-country panels with confounded institutions; emphasize fixed effects, clustering, and weak-IV-robust inference.

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
- A single-country experiment over-generalized to "people" with no caveat about context
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】quant-causal / qualitative / experiment / formal-empirical
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Generalizes because】the cross-case generalization sentence
【Robustness/sensitivity】planned checks
【Next】bjps-data-analysis
```

## What BJPS reviewers ask of each design mode

| Mode | The decisive design question | The move that satisfies it |
|------|------------------------------|----------------------------|
| Quant-causal | Does the design license the causal word, and does it travel? | Estimand + assumption + sensitivity, plus the generalization sentence |
| Qualitative | Is case selection design-driven, and a case *of* what? | Justify selection logic; state the population the case speaks to |
| Experiment | Is a single-country result framed as a general mechanism? | Pre-register; report MDE; caveat context; argue the mechanism travels |
| Formal-empirical | Do the tests follow the comparative statics? | Map each prediction to a parameter the model moves |

## Calibration anchors (hedged)

- BJPS judges each tradition **on its own terms** — do not force a regression template onto qualitative,
  formal, or interpretive work, and do not excuse a weak design by appeal to pluralism.
- The international remit adds a second bar beyond identification: a clean design that cannot speak past
  its single setting is a positioning weakness as well as a generalization one.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python) and CAQDAS for qualitative work
- [`../../resources/code/`](../../resources/code/) — modern DiD/IV/RDD/DML command chain to adapt
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and transparency notes
