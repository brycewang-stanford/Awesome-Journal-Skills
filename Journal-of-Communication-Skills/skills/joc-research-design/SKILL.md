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

## Anti-patterns

- Causal language on a cross-sectional survey that only supports association
- Content analysis with no reported intercoder reliability or an unstated unit of analysis
- Automated text measures used without human validation
- Convenience case/stimulus selection dressed up as theory-driven
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
