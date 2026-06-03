---
name: wp-research-design
description: Use when defending the research design of a World Politics manuscript — comparative-historical and case selection, quantitative cross-national identification, qualitative process tracing, experiments, or formal-empirical linkage for cross-case questions. World Politics expects explicit research design and appropriate methods, judged on each tradition's own terms. Strengthens the design; it does not write code.
---

# Research Design (wp-research-design)

World Politics asks every article to "be explicit about its research design and use appropriate
methods," and applies separate expectations to quantitative and qualitative work. Because the journal
values **arguments that travel across cases**, the design must connect a portable argument
(`wp-theory-building`) to evidence in a way that **rules out the strongest cross-case rival**. This
skill is mode-aware: pick the section that matches your work.

## When to trigger

- Specifying case selection, identification, or experimental design for a cross-case question
- A reviewer questioned causal claims, case choice, external validity, or a confound
- Justifying why your design adjudicates the rival account from `wp-literature-positioning`

## Comparative-historical & case-based (a World Politics staple)
- **Case selection by design logic** — typical, deviant, most/least-likely, paired/structured-focused
  comparison, or set-theoretic (QCA). Say what each case is a case *of* and why the comparison
  identifies the argument. Convenience is not a design.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument in each case.
- **Travel.** Show the comparison licenses a claim beyond the cases studied (scope conditions), not
  just a within-case story.

## Quantitative / cross-national
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (parallel trends, exclusion, continuity, ignorability). Defend them; don't assert them.
- **TSCS realities.** With time-series-cross-section data, address serial correlation, unit effects,
  and cross-sectional dependence (panel-corrected SEs, Driscoll–Kraay); avoid naive TWFE on staggered
  treatment — use modern estimators.
- **Designs**: DID/event study, IV (first-stage strength, exclusion, weak-IV-robust inference), RDD,
  matching/weighting with balance + sensitivity; survival models for onset/duration.
- **Inference**: cluster at the right level (often country); sensitivity to unobserved confounding.

## Experiments & formal-empirical
- Experiments: preregister design and primary analyses; report power/MDE; address attrition and ethics
  (APSA Principles — see `wp-review-process`/`wp-submission`). State the generalization claim across
  contexts honestly.
- Formal-empirical: make the **empirical test follow from the model's comparative statics**, and
  distinguish predictions unique to your model from those shared with rivals.

## The adjudication test (World Politics–specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather than
my argument, the cases/data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify a contribution that travels.

## Anti-patterns

- Convenience case selection dressed up as theory-driven; selecting on the dependent variable
- Naive TWFE on staggered treatment; ignoring serial correlation / cross-sectional dependence in TSCS
- "Causal" language on a design that only supports cross-case association
- A within-case story over-generalized with no scope conditions
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】comparative-historical / quant cross-national / qualitative / experiment / formal-empirical
【Estimand or claim】what is being identified/shown, and across which cases
【Case selection / key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】wp-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — identification/TSCS packages, QCA, and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reviewer-guideline expectations for design and methods
