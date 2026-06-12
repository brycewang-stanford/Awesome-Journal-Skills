---
name: qe-writing-style
description: Use when polishing prose, abstract, and introduction for a Quantitative Economics (QE) manuscript so a quantitative method and its economic payoff land for a general-interest Econometric Society readership. Reflects QE house rules (no significance asterisks; report SEs/coverage sets). Polishes exposition; it does not change results or estimation.
---

# Writing Style (qe-writing-style)

## When to trigger

- The prose buries the economic question under method or notation
- The abstract describes the topic but never states what was found or built
- The introduction reaches the model/estimator before the reader sees the question
- Statistical claims lean on asterisks or vague intensifiers instead of magnitudes and uncertainty

## QE house style: a quantitative method serving a substantive question

QE is read across all of economics through an **Econometric Society** lens, so a paper must make **both** the substantive economic question **and** the quantitative apparatus (structural model, estimator, experiment, or simulation) legible to a smart non-specialist early. Format facts that shape the writing: the **abstract is ≤150 words**; the title page carries keywords and affiliations; the manuscript is **1.5/double-spaced, ≥12pt, ≤32 lines per page**, with figures and tables **in-text**. Crucially, QE's **house rules forbid asterisks and boldface for statistical significance** — the prose and exhibits must communicate findings through **point estimates with standard errors and confidence/coverage sets**, so write magnitudes and uncertainty into the sentences themselves. QE also applies its own reference style at copyediting, so keep citations consistent rather than chasing a format.

## The introduction arc (QE template)

1. **The question** — one or two sentences, plain language, stakes clear.
2. **Why it is hard quantitatively** — the measurement, identification, or computational obstacle.
3. **The approach** — the data + model/estimator/experiment that resolves it, in one paragraph.
4. **The headline result** — the key estimate or quantity, with units **and a standard error / coverage set**, stated early.
5. **Mechanism & interpretation** — what it means; the economic frame in a sentence.
6. **Contribution & lesson** — placement in the literature + what transfers beyond this setting.
7. **Roadmap** — brief.

## Abstract: state the finding (≤150 words)

- Open with the question and the approach in one breath, then **state the result with a number and its uncertainty**.
- For structural/computational work, name the quantity (an elasticity, a welfare number, a counterfactual) and the model that delivers it.
- Close with the broad lesson. No throat-clearing; stay within 150 words.

## Sentence-level craft

- Active voice; short declaratives for the key claims.
- Define notation once; do not make the reader hold five symbols to parse a sentence.
- Quantify with uncertainty ("a 7.3% rise, s.e. 1.1") rather than "significantly affects" or asterisks.
- Calibrated confidence reads as competence; hedge only where the evidence requires it.
- Relocate heavy derivations and extra results to the Supplemental Appendix (≤25 pages); the main paper stays self-contained.

## Checklist

- [ ] Abstract states the actual finding with a number **and** its uncertainty, ≤150 words
- [ ] The question is on page one in plain language
- [ ] The headline estimate appears early in the intro, with units and a standard error / coverage set
- [ ] The broad lesson ("beyond this setting") is explicit
- [ ] No significance asterisks or boldface in prose or exhibits
- [ ] Magnitudes are quantified, not vaguely intensified
- [ ] Notation introduced once; references consistent (QE styles at copyediting)

## Anti-patterns

- An abstract that names the topic but never the result, or runs past 150 words
- Leading the intro with the estimator ("We use indirect inference...") instead of the question
- Reporting significance with asterisks/boldface (QE forbids this)
- Vague magnitude language ("significantly", "substantially") with no number or uncertainty
- Notation overload in the introduction

## Worked vignette: an abstract rewrite (illustrative)

A draft abstract reads: "We study how minimum wages affect employment using a structural model of labor demand, and discuss policy implications." It names a topic, never a finding. The QE rewrite states the quantity with its uncertainty: "Estimating labor demand on firm-level data, a $1 minimum-wage rise lowers low-wage employment 1.2% (s.e. 0.4) but raises retained workers' earnings 3.1% (s.e. 0.7); net surplus rises in low-turnover sectors and falls in high-turnover ones." (Illustrative, ≤150 words.) The reader leaves with a number, its uncertainty, and the lesson.

## Referee pushback and the prose fix

- *"The abstract never states what you found."* → Lead the second sentence with the headline quantity and its standard error.
- *"The intro reaches the estimator before the question."* → Re-order to the QE arc: question, hardness, approach, result early.
- *"Magnitudes are vague."* → Replace every intensifier with a number and a coverage set.

## Output format

```
【Abstract verdict】states finding + number + uncertainty, ≤150 words? [Y/N] — fix: ...
【Intro arc】question / hardness / approach / result / interpretation / contribution present? [Y/N each]
【Headline estimate in intro】present + units + SE/coverage? [Y/N]
【Significance reporting】asterisk-free, SEs/coverage shown? [Y/N]
【Broad lesson stated】[Y/N]
【Next step】qe-replication-and-data-policy or qe-review-process
```
