---
name: joc-research-design
description: Use when defending the research design of a Journal of Communication (JoC) manuscript — experimental and survey design, content analysis with intercoder reliability, computational/text-as-data validation, or qualitative/critical inquiry. JoC judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (joc-research-design)

JoC accepts many methodologies but is demanding about each. The design must credibly connect the
argument (`joc-theory-building`) to evidence. This skill is mode-aware: pick the section that matches
your work and defend it against the strongest alternative explanation.

## When to trigger

- Specifying an experiment, survey, content-analysis protocol, computational pipeline, or fieldwork plan
- A reviewer questioned causal claims, sampling, coding reliability, validity, or a confound
- Preparing a **preregistration** / pre-analysis plan (note it in the cover letter)
- Justifying why your design adjudicates the rival account from `joc-literature-positioning`

## Experiments (lab / online / survey / field)
- Preregister the design and primary analyses; report **a-priori power / MDE**; pre-specify subgroups.
- Treatment realism and ecological validity; manipulation and attention checks; attrition.
- Stimuli sampling: treat messages as a sample, not a fixture (consider stimulus-as-random-factor).
- Ethics/IRB and informed consent; debrief where deception is used.

## Surveys / panels
- Sampling frame, mode, and generalization claims; weighting where appropriate.
- Validated multi-item measures; report reliability; guard against common-method variance.
- For cross-sectional mediation, be explicit about causal limits; prefer panel/experimental designs for process claims.

## Content analysis
- A documented **codebook**; trained coders; report **intercoder reliability** (Krippendorff's alpha or
  equivalent) on an adequate subsample, and the unit of analysis.
- Sampling of texts justified (timeframe, sources); construct validity of categories.

## Computational / text-as-data
- **Validate** automated measures against human-coded gold-standard samples; report agreement.
- Document model/version, hyperparameters, seeds; report stability; do not treat outputs as ground truth.
- Address platform/ToS and ethics for collected data.

## Qualitative / critical
- Justify case/site/text selection by design logic, not convenience; say what it is a case *of*.
- Trustworthiness: reflexivity, audit trail, transparent coding; state what evidence would **complicate** the reading.

## The adjudication test (JoC-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my argument, the data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify the contribution.

## Reviewer-pushback patterns and the JoC-specific fix

JoC referees at the ICA flagship rarely reject on a single statistic; they reject when the design
cannot bear the **theoretical** weight the paper puts on it. The recurring objections and their
venue-specific repairs:

| Reviewer objection | Why it lands at JoC | Design-stage fix |
|--------------------|---------------------|------------------|
| "Single-message confound" | one stimulus cannot separate the message *feature* from the specific text | sample multiple messages per condition; treat message as a random factor; report a stimulus-sampling check |
| "Measurement validity of message features" | a hand-coded or model-coded "frame" may not be the construct claimed | pre-validate the feature against human gold-standard coding; report construct validity, not just reliability |
| "Effect without mechanism" | a main effect alone does not advance communication theory | design the mediator/moderator measurement in *before* collection; pre-specify the indirect-effect test |
| "Exposure is assumed, not measured" | self-reported "saw the news" is a weak proxy | build a behavioral or attention-anchored exposure measure |
| "Cross-sectional process claim" | mediation on one wave cannot license a causal story | move the mediator to an experiment or panel, or hedge the claim |

## Worked micro-example: framing survey-experiment design (illustrative)

A planned study claims that **gain- vs. loss-framed** vaccine messages change intention via
**perceived risk**. A JoC-defensible design: 2 (frame) × 3 (message exemplars per frame) factorial
so the frame effect is estimated across six distinct texts, not one — defeating the single-message
confound. Target **N ≈ 900** (illustrative; size to the registered MDE), preregister the mediation
path frame → perceived risk → intention with bootstrap CIs, and add an attention check plus a
behavioral exposure proxy. The adjudication sentence writes itself: if the rival "any health message
moves intention" were true, the gain/loss contrast would be null while overall intention rose;
instead the contrast is non-null and runs through perceived risk — advancing framing theory rather
than re-documenting a persuasion effect.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Communication spans experiments, surveys, and content analysis; randomization inference for experiments, DiD/IV for observational media-effects claims.

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
- Automated text measures used without human validation
- Convenience case/stimulus selection dressed up as theory-driven
- A single-message stimulus carrying a claim about a message *feature*
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】experiment / survey / content-analysis / computational / qualitative
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended (incl. reliability/validity)
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】joc-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design, reliability, and text-as-data packages (R/SPSS/Mplus/Python) and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and Open Science Badge notes
