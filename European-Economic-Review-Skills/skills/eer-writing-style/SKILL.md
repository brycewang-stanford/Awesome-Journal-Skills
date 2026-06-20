---
name: eer-writing-style
description: Use when revising prose for a European Economic Review (EER) manuscript — the abstract, introduction arc, research highlights, and Elsevier house conventions. Makes the general-interest idea land; it does not establish identification, theory, or exhibits.
---

# Writing Style (eer-writing-style)

## When to trigger

- The introduction buries the question under data or machinery
- The abstract is a method recital, not a result a generalist can grasp
- Research highlights, keywords, or JEL codes are missing or weak
- The prose reads as field-internal and loses the general-interest reader

## The EER writing bar

EER is **general-interest**, so the writing must make a **non-specialist economist** see the question, the answer, and why it matters — fast — while satisfying specialists on rigor. Elsevier economics house elements: a **structured/concise abstract**, **research highlights** (a few bullet points capturing the core findings), **JEL codes** and **keywords**, a **declaration of interest**, and SEs reported in the text rather than significance-star prose. The introduction must execute a clear arc and the **headline result with its uncertainty** should appear early.

## The EER introduction arc

1. **Question** — a first-order economic question a generalist cares about (one sentence).
2. **Why it is hard / open** — the obstacle (identification, theory gap, measurement).
3. **Approach** — data + design or model, in plain terms.
4. **Headline result with uncertainty** — the magnitude **with a standard error / CI**, early, in units.
5. **Mechanism / interpretation** — what drives it; what it means.
6. **Contribution & lesson** — the checkable delta + the portable lesson (ties to `eer-literature-positioning`).
7. **Scope** — what the result does *not* establish.
8. **Brief roadmap** — short, no over-signposting.

## House elements

- **Abstract**: concise, result-forward, generalist-legible; state the headline finding, not just the method (re-confirm any word limit on the guide for authors — 检索于 2026-06；以官网为准).
- **Research highlights**: a few short bullets, each a concrete finding (Elsevier requirement).
- **JEL codes + keywords**: accurate and cross-field where the result travels.
- **Declaration of interest** and funding statement present.
- **Numbers in prose**: report point estimate + SE/CI, never an asterisk in a sentence.

## Checklist

- [ ] First paragraph states the question + headline quantity + its uncertainty
- [ ] A non-specialist can state the contribution after reading the intro
- [ ] Abstract is result-forward, not a method recital
- [ ] Research highlights present (concrete findings, not topics)
- [ ] JEL codes + keywords accurate; cross-field where relevant
- [ ] Declaration of interest + funding statement included
- [ ] In-text numbers carry SEs/CIs, no significance asterisks in sentences
- [ ] Scope sentence states what is NOT claimed; roadmap is brief

## Anti-patterns

- Leading the intro with the estimator/solver instead of the economic question
- An abstract that says what you did but not what you found
- "Significant at the 1% level (***)" prose instead of an estimate with an SE
- Throat-clearing ("X has been studied extensively") with vague stakes
- Field jargon that loses the general-interest reader on page one
- Over-signposted roadmap doing the work the argument should do
- Missing research highlights / declaration of interest (Elsevier requirements)

## Worked vignette (illustrative)

Before: "We estimate a structural model by SMM and find the pass-through elasticity is significant at the 1% level (***)." After: "When an input cost rises, how much reaches consumers? We find a 10% cost shock raises retail prices 6.2% (s.e. 0.7) — about a third is absorbed by consumer search — implying that wherever shoppers can compare sellers, measured pass-through understates the underlying shock." Question + magnitude + uncertainty + portable lesson, no stars, in two sentences. See `resources/worked-examples/01-introduction.md`.

## Output format

```
【Intro arc】question→hard→approach→result(w/ SE)→mechanism→contribution→scope→roadmap present? [Y/N]
【Abstract】result-forward + generalist-legible? [Y/N]
【Highlights】concrete-finding bullets present? [Y/N]
【House elements】JEL + keywords + declaration of interest + funding? [Y/N]
【Numbers】SEs/CIs in prose, no asterisks? [Y/N]
【Next step】eer-replication-package (assemble deposit) or eer-referee-strategy
```
