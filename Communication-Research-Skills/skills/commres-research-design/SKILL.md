---
name: commres-research-design
description: Use when defending the research design of a Communication Research (CR) manuscript — experiments (lab/online), panel surveys, and content analysis with intercoder reliability. CR is quantitative and demanding about identification, measurement, and confound control. Strengthens the design; it does not write code.
---

# Research Design (commres-research-design)

CR is a **quantitative** journal and demanding about each design. The design must credibly connect the
hypotheses (`commres-theory-building`) to evidence and defeat the strongest rival explanation. This
skill is mode-aware — pick the section that matches your study and defend it on social-science terms.

## When to trigger

- Specifying an experiment, panel survey, or content-analysis protocol
- A reviewer questioned causal claims, sampling, coding reliability, validity, or a confound
- Preparing a **preregistration** / pre-analysis plan (note it in the cover letter)
- Justifying why your design adjudicates the rival account from `commres-literature-positioning`

## Experiments (lab / online / survey-embedded)
- Preregister design and primary analyses; report **a-priori power / MDE**; pre-specify subgroups.
- **Stimulus sampling**: treat messages as a sample, not a fixture — multiple exemplars per condition;
  model message as a random factor so the *feature* effect is not one text's idiosyncrasy.
- Manipulation and attention checks; treatment realism; report and model attrition.
- Pre-specify the **mediation/moderation** test that operationalizes H2/H3; for causal mediation,
  prefer manipulating the mediator or a measurement-of-mediation design with stated assumptions.
- Ethics/IRB and informed consent; debrief where deception is used.

## Surveys / panels
- Sampling frame, mode, and generalization claims; weighting where appropriate.
- **Validated multi-item measures**; report reliability (alpha/omega) and, ideally, a CFA/measurement
  model; guard against **common-method variance** (procedural and statistical remedies).
- For process claims, prefer **panel (lagged) or experimental** leverage — cross-sectional mediation
  cannot license a temporal/causal story; say so plainly if you are cross-sectional.

## Content analysis
- A documented **codebook**; trained coders; report **intercoder reliability** (Krippendorff's alpha
  or equivalent) on an adequate subsample, and the **unit of analysis**.
- Justify text sampling (timeframe, sources); establish construct validity of categories, not just
  reliability — reliable coding of the wrong construct is still wrong.

## Computational / text-as-data (when hypothesis-testing)
- **Validate** automated measures against human-coded gold-standard samples; report agreement.
- Document model/version, hyperparameters, seeds; report stability; do not treat outputs as ground truth.

## The adjudication test (CR-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my hypothesis, the data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify the contribution.

## Reviewer-pushback patterns and the CR-specific fix

| Reviewer objection | Why it lands at CR | Design-stage fix |
|--------------------|--------------------|------------------|
| "Single-message confound" | one stimulus cannot separate the message *feature* from the text | sample multiple messages per condition; model message as a random factor |
| "Measurement validity unclear" | a scale or coded category may not be the construct | report CFA / construct validity, not just reliability |
| "Common-method variance" | same-survey predictor and outcome inflate the path | procedural separation + a statistical CMV check |
| "Cross-sectional process claim" | mediation on one wave cannot license a causal story | move to an experiment/panel, or hedge the claim |
| "Effect without mechanism" | a main effect alone does not advance theory | measure and pre-specify the mediator/moderator before collection |

## Worked micro-example: framing survey-experiment design (illustrative)

A study claims **gain- vs. loss-framed** vaccine messages change intention via **perceived
response-efficacy**, moderated by prior knowledge. A CR-defensible design: 2 (frame) × 3 (message
exemplars per frame) factorial so the frame effect is estimated across six texts — defeating the
single-message confound. Validated multi-item efficacy and intention scales (report alpha + a CFA),
target **N sized to the registered MDE**, preregister the moderated-mediation model (frame →
response-efficacy → intention, moderated by knowledge) with bootstrap CIs, plus an attention check.
The adjudication sentence: if "any health message moves intention" were true, the gain/loss contrast
would be null while overall intention rose; instead the contrast runs through efficacy and only for
low-knowledge audiences — advancing framing theory rather than re-documenting persuasion.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Communication Research is experiment- and survey-heavy; emphasize randomization inference, mediation done right, and family-wise corrections.

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

- Causal language on a cross-sectional survey that only supports association
- Content analysis with no reported intercoder reliability or an unstated unit of analysis
- A single-message stimulus carrying a claim about a message *feature*
- Scales used with no reliability/validity evidence; ignoring common-method variance
- A design that cannot distinguish your hypothesis from the leading alternative

## Output format

```
【Mode】experiment / survey-panel / content-analysis / computational
【Estimand or claim】what is being identified/tested
【Key assumption(s)】and how each is defended (incl. reliability/validity, CMV)
【Rival ruled out】the adjudication sentence
【Mediation/moderation】design supports the causal ordering? [Y/N]
【Robustness/sensitivity】planned checks
【Next】commres-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design, reliability, SEM, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and APA reporting notes
