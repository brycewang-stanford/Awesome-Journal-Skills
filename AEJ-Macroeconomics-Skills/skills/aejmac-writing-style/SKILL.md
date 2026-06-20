---
name: aejmac-writing-style
description: Use when revising prose, the abstract, or the introduction of an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript for AEA house style and the broad-interest macro arc. Late-stage polish on framing and clarity; it does not fix identification, the model, or exhibits.
---

# Writing Style (aejmac-writing-style)

## When to trigger

- The introduction leads with the model block or the estimator, not the macro question
- The abstract is over 100 words or buries the headline quantity
- A general macroeconomist cannot tell from page 1 what is measured and why it matters
- The prose is technically correct but the idea does not land

## The AEJ: Macro writing bar

AEJ: Macro is **broad-interest**, so the writing must make the macro question and the headline quantity legible to a *general* macroeconomist early — before the DSGE notation or the SVAR machinery. Follow **AEA house style** (active voice, plain prose, quantities with units, standard errors / bands reported). The hard constraint to design around: the **abstract is ≤100 words** (检索于 2026-06；以官网为准) — far tighter than most economics journals — so every word in it must earn its place.

## The AEJ: Macro introduction arc

1. **The macro question + headline quantity, in the first breath.** "How much does a monetary tightening lower output?" — then the number with units and uncertainty, e.g., "we find a 100 bp shock lowers output by 0.6% (90% band [0.2, 1.0]) at its peak."
2. **Why it is hard.** The identification or quantification obstacle (anticipation, simultaneity, short samples; or what disciplines the model).
3. **The approach.** Data + design (SVAR/LP/narrative) and/or model (DSGE/HANK) — in one paragraph, after the question, not before it.
4. **The result restated with mechanism and uncertainty.** What drives the number; carry the band into any counterfactual.
5. **Contribution + lesson with scope.** What general macroeconomists learn; where it holds and where it does not.
6. **Brief roadmap.** One or two sentences, not a section-by-section recital.

## The ≤100-word abstract

- Sentence 1: the macro question.
- Sentence 2–3: the approach (one clause) and the **headline quantity with uncertainty**.
- Sentence 4: the mechanism or policy lesson.
- Cut: literature, method jargon, signposting. At ≤100 words there is no room for throat-clearing.

## Prose discipline

- **Quantities, not adjectives.** "Large" → "0.6% at peak." Report SEs/bands in the sentence where the number appears.
- **Active voice, short sentences.** AEA house style favors plain prose.
- **Define before you deploy** notation; minimize symbols in the intro.
- **One idea per paragraph**; topic sentence first.
- **Policy relevance stated, not implied** — AEJ: Macro readers want the decision-relevant takeaway.

## Checklist

- [ ] Abstract ≤100 words, with the headline quantity and its uncertainty
- [ ] First paragraph states the macro question and the number (units + band/SE)
- [ ] Approach appears after the question, not before it
- [ ] Mechanism and scope/limits stated; no over-claiming
- [ ] Active voice, AEA plain style; quantities not adjectives
- [ ] Roadmap is one or two sentences
- [ ] A general macroeconomist could state your contribution after reading page 1

## Anti-patterns

- Leading the intro with the model's equations or the estimator (reads as a field/methods paper)
- An abstract over 100 words, or one with no number in it
- "Significant effects" with no point estimate or band in the abstract/intro
- Over-signposted roadmap doing the argument's job
- Subfield jargon on page 1 that a general macro reader cannot parse
- Burying the policy lesson in the conclusion

## Worked vignette: before → after first sentence (illustrative)

- **Before:** "We build a medium-scale New Keynesian DSGE model with financial frictions and estimate it by Bayesian methods to study monetary transmission." (machinery first; no question, no number)
- **After:** "How much of a recession does a surprise monetary tightening cause, and through which channel? Using high-frequency policy surprises in a proxy-VAR, we find a 100 bp shock lowers output by 0.6% (90% band [0.2, 1.0]) at its peak, two-thirds of it through investment." (question + quantity + uncertainty + mechanism, in the first breath)

> For a full before→after introduction in AEJ: Macro house style, see [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md).

## Output format

```
【Abstract word count】 ≤100? [Y/N] (current: __)
【First-paragraph test】question + quantity + uncertainty present? [Y/N]
【Arc】question → why hard → approach → result+mechanism → contribution+scope → roadmap? [Y/N]
【Style】active voice, quantities-not-adjectives, SEs/bands in sentences? [Y/N]
【Next step】aejmac-replication-package
```
