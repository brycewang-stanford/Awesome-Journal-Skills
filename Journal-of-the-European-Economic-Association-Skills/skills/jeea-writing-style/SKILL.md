---
name: jeea-writing-style
description: Use when revising the prose, abstract, and introduction of a Journal of the European Economic Association (JEEA) manuscript so the idea lands for a general-interest readership. Shapes how the argument reads; it does not change the result, identification, or exhibits.
---

# Writing Style (jeea-writing-style)

## When to trigger

- The abstract or intro buries the question and the answer
- A general-interest reader cannot tell what the paper establishes by the end of page one
- The intro leads with machinery (the estimator or the model's solver) instead of the question
- Prose is correct but the lesson does not travel

## The JEEA writing bar

JEEA is **general interest**, so the writing must make **both the substantive question and the result legible early** to an economist outside the subfield. The introduction arc that works: **question → why it is hard (clean identification needed, or a disciplined model) → approach → headline result with its uncertainty → mechanism → contribution & lesson → brief roadmap.** Two house rules: the **headline estimate appears early with units and a standard error / confidence set, never a significance asterisk**, and the **abstract is short and answer-first** (state the finding, not just the topic). This is a late-stage polish — write the intro **last**, after identification, the model, and robustness have settled.

## The introduction arc

1. **Question first.** A non-specialist economist should grasp the question in the first sentence — not the estimator, not the solver.
2. **Why it is hard.** The obstacle (identification, or a tension a model resolves) in one or two sentences.
3. **Approach.** Data + design, or the model, in a paragraph — legible to a generalist.
4. **Headline result with uncertainty.** The number, with units and a standard error / confidence set, in the first breath (no asterisks).
5. **Mechanism.** Why the result holds, in words.
6. **Contribution & lesson.** What is new and what travels beyond the setting; state the scope limit.
7. **Brief roadmap.** One or two sentences, not a section-by-section recital.

## Prose discipline

- **Answer-first abstract.** Lead with the finding and the lesson, not "this paper studies…".
- **Plain economic English.** Define notation when first used; keep the intuition in words alongside the math.
- **Cut throat-clearing** ("has been studied extensively"); every sentence in the intro should advance the argument.
- **Calibrated claims.** State what the paper does and does not establish; over-claiming is punished by general-interest referees.
- **No significance asterisks in the prose** — write the magnitude and its standard error into the sentence.

## Checklist

- [ ] First paragraph states the question + the headline result + its uncertainty (no asterisks)
- [ ] Both substance and approach are legible to a non-specialist by end of page one
- [ ] Abstract is answer-first and concise
- [ ] Intro arc complete: question → hardness → approach → result → mechanism → contribution → roadmap
- [ ] Claims calibrated; scope limit stated
- [ ] Intro written last, after the analysis settled

## Abstract craft

The abstract is the co-editor's first (and sometimes only) read, so it must do the general-interest work:

1. **Sentence 1 — the question**, in plain language a non-specialist grasps.
2. **Sentence 2 — the approach**, in a phrase (design or model), not jargon.
3. **Sentence 3 — the headline finding with its magnitude** (and, where natural, its uncertainty) — the answer, not the topic.
4. **Sentence 4 — the lesson/contribution** that travels beyond the setting.

Avoid "this paper studies / examines / investigates" openings; lead with what you found. Keep it within the JEEA author-guideline length (confirm on the live OUP page).

## Worked vignette (illustrative)

A draft abstract reads: "This paper studies the relationship between trade exposure and local labor markets using regional data and a fixed-effects approach." It names the topic and the method but never the finding. The JEEA-grade rewrite: "Does import competition cost local jobs, or just reshuffle them? Using a region's pre-existing industry mix as exposure, we find a 10 percentage-point rise in import penetration lowers manufacturing employment by 2.4 points (s.e. 0.5) with no offsetting service-sector gain — so the adjustment is reallocation away from work, not across it." Question, approach, magnitude with uncertainty, and lesson, in four sentences, no asterisks.

## Anti-patterns

- Leading the intro with the estimator or the model's solver instead of the question
- An abstract that names the topic but never states the finding
- "Significant at the 1% level (\*\*\*)" anywhere — JEEA forbids significance asterisks; report the SE/CI
- Over-signposting ("Section 2… Section 3…") doing the work the argument should do
- Throat-clearing and a survey-style literature recital in the intro
- Over-claiming a general lesson the result does not support
- Jargon in the abstract that a non-specialist co-editor cannot parse

## Output format

```
【Abstract】answer-first, finding stated? [Y/N]
【First paragraph】question + result + uncertainty (no asterisks)? [Y/N]
【Intro arc】question→hardness→approach→result→mechanism→contribution→roadmap? [Y/N]
【Claims】calibrated + scope limit? [Y/N]
【Next step】jeea-replication-package
```
