---
name: psychbull-theory-integration
description: Use when turning the synthesis results of a Psychological Bulletin manuscript into a genuine theoretical contribution — reconciling conflicting findings, building or refining a model, and stating scope conditions and a research agenda. Makes the synthesis matter; it does not run the analysis.
---

# Theory Integration (psychbull-theory-integration)

A Psychological Bulletin paper is judged not by the size of its table but by **what the synthesis
means for psychology**. The journal publishes **evaluative and integrative** reviews — the value is in
**interpreting** an existing literature, reconciling its contradictions, and advancing or refining a
theoretical account. (Note: a *purely* new theory with no synthesis belongs to *Psychological Review*;
here the theory is grounded in the synthesized evidence.) This skill builds the contribution; the
numbers come from the analysis skills.

## When to trigger

- The pooled effect, moderators, and bias analyses exist and you must say what they *mean*
- A literature has conflicting findings you can now reconcile
- Building or refining a theoretical model from the synthesized evidence
- A reviewer says the review is "a competent meta-analysis but not a contribution"

## From results to contribution

1. **Answer the field's open question.** State what the synthesis resolves: the size of an effect, why
   studies disagreed, which moderator explains the pattern, whether an effect survives bias correction.
2. **Reconcile conflict with the moderators.** Use the moderator/meta-regression results to explain
   *why* prior studies clashed — different populations, measures, designs, or conditions.
3. **Build or refine a model.** Translate the empirical pattern into a theoretical statement: an
   integrative framework, boundary conditions, a mediating/moderating mechanism, or a corrected estimate.
4. **State scope conditions honestly.** Where does the effect hold, and where not? Heterogeneity and
   the prediction interval discipline the claim.
5. **Set the agenda.** What should primary researchers do next — the gaps, the under-powered cells, the
   untested moderators the synthesis exposes.

## Calibrate claims to evidence

- Match the strength of the theoretical claim to **heterogeneity, k, and bias robustness**.
- Distinguish **confirmatory** (pre-specified) from **exploratory** patterns when theorizing.
- Avoid over-reading a fragile or bias-sensitive effect into a strong theory.

## Anti-patterns

- A "results dump" with no interpretive or theoretical payoff
- Theorizing past the evidence (strong claims on small k or bias-sensitive effects)
- Ignoring heterogeneity when stating a general law
- Presenting an exploratory moderator as if it were the confirmatory story
- Submitting a pure new theory that should have gone to *Psychological Review*

## The integration bar that defines a Bulletin paper

This is the calibration anchor that separates the APA's flagship review journal from a methods-only
meta-analysis: a competent pooled estimate is necessary but not sufficient. The genuine theoretical
advance is the threshold reviewers police.

| Synthesis delivers… | Methods-only meta-analysis (reject risk) | Psychological Bulletin contribution |
|---------------------|-------------------------------------------|--------------------------------------|
| A pooled number | "The effect is g = 0.34" and stops | Explains what that resolves for the field |
| Heterogeneity | Reports I² = 68% as a nuisance | Uses moderators to say *why* studies disagreed |
| A model | None — tallies effects | Advances or refines a theoretical account |
| Scope | Implies the effect is universal | States boundary conditions from the PI |

## Worked vignette — turning numbers into theory

*Illustrative numbers only.* The self-affirmation synthesis yields g = 0.34 [0.24, 0.44], I² = 68%,
with delivery format explaining an R²-analog of 0.22 and bias diagnostics pulling the effect toward
≈ 0.25. The integrative payoff under this skill's rules:

- **Open question resolved**: self-affirmation has a small-to-moderate but real effect, smaller than the
  early enthusiastic literature implied once selective reporting is modeled.
- **Conflict reconciled**: the disagreement tracks *delivery format* — facilitated, in-person formats
  outperform brief written prompts — not a true-versus-null split.
- **Model refined**: this sharpens the timing/fit account rather than proposing a brand-new theory
  (which would belong to *Psychological Review*).
- **Scope conditions**: the wide prediction interval [−0.10, 0.78] disciplines the claim — the effect can
  vanish in some settings, so no universal law is asserted.
- **Agenda**: pre-registered trials varying delivery format, and direct tests of the underutilized cells.

## Referee pushback → venue-specific fix

- *"Competent meta-analysis, but not a contribution."* → Add the interpretive layer: state the field
  question and how the moderators resolve the conflict, not just the pooled number.
- *"You theorize past your evidence."* → Down-calibrate to k, heterogeneity, and bias robustness.
- *"This is really a new theory."* → If the model is not grounded in the synthesized evidence, it belongs
  to *Psychological Review*.

## Output format

```
【Open question resolved】one sentence
【Conflict reconciled】via which moderator(s)
【Model / framework】what is advanced or refined
【Scope conditions】where it holds / breaks
【Research agenda】top gaps for primary work
【Claim calibration】matched to k / heterogeneity / bias? [Y/N]
【Next】psychbull-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — synthesis/reporting standards that frame the contribution
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Psychological Bulletin's evaluative/integrative scope (vs. Psychological Review for theory)
