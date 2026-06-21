---
name: arsoc-comprehensiveness-and-balance
description: Use when calibrating completeness vs. selectivity and ensuring fairness across theoretical schools, methods, authors, and debates in an Annual Review of Sociology (ARSoc) review — including not over-promoting the author's own work. Audits coverage and even-handedness; it does not design the framework (arsoc-organizing-framework) or write prose (arsoc-writing-style).
---

# Comprehensiveness & Balance (arsoc-comprehensiveness-and-balance)

## When to trigger

- The framework is set and you are filling cells with the literature
- You are unsure whether to cite *everything* or curate
- The subfield has rival theoretical schools, a live debate, or conflicting empirical findings
- You are a contributor to this literature and worry the review tilts toward your own work or method

## Completeness vs. selectivity: the ARSoc contract

An ARSoc review must be **comprehensive in coverage** yet **selective in emphasis**. The reader should trust that nothing important is missing, while the prose foregrounds what matters. Resolve the tension by **tiering** the corpus:

| Tier | Treatment |
|------|-----------|
| **Foundational / field-defining** | discussed in the text, with what they established and their limits |
| **Important contributions** | grouped and weighed within the framework's cells; cited with their finding |
| **Confirmatory / incremental** | cited in clusters ("see also …") to demonstrate coverage without bloating prose |
| **Tangential** | cited only where they bear on a specific claim; not every adjacent study belongs |

Comprehensiveness is proven by the *citation set* (the saturation log from `arsoc-literature-synthesis`); selectivity is exercised in the *prose*. A review that discusses every study at equal length has abdicated the editorial judgment that is its value.

## Fairness across schools, methods, authors, and findings

ARSoc is the **survey of record** for a subfield: its account of a debate becomes the discipline's shared reference. That obliges genuine even-handedness:

- **Steelman every camp.** State each theoretical school's strongest case in terms its proponents would accept *before* noting its weaknesses. Refute positions at their best, never at their worst.
- **Respect methodological pluralism.** Sociology runs on quantitative, qualitative, computational, and theoretical traditions; weigh ethnographic and interpretive evidence on its own terms rather than measuring it against a regression yardstick (or vice versa). Dismissing a whole mode is a classic ARSoc balance failure.
- **Weigh, don't tally.** Conflicting results are reconciled by *credibility* (design, data, transparency) and by *what each studies*, not by vote-counting "7 studies find positive, 4 negative."
- **Attribute ideas correctly.** Credit originators, not just popularizers; this is a recurring referee complaint, sharpened in a discipline attentive to whose contributions get erased.
- **Handle live debates without resolving by fiat.** Lay out the disagreement, what evidence would settle it, and where the author's own read sits — labelled as the author's read, not as consensus.

## The self-citation trap

If you have published in the subfield, the review must **not** read as a retrospective of your program. Guardrails:

- Your own work is cited at the tier its *importance to the field* warrants — no more.
- Rival schools and rival methods to your own are given their strongest statement.
- A reader who does not know who wrote the review cannot tell from the emphasis or the method mix.
- When the field disagrees with you, say so plainly and represent the other side fairly.

## Checklist

- [ ] Corpus tiered (foundational / important / confirmatory / tangential); prose emphasis matches tier
- [ ] Comprehensiveness provable from the citation set + saturation log
- [ ] Every rival school stated at its strongest before critique (steelman)
- [ ] Quantitative, qualitative, computational, and theoretical traditions each weighed on their own terms
- [ ] Conflicting findings reconciled by credibility and what-is-studied, not vote-counting
- [ ] Idea attribution traces to originators
- [ ] Live debates presented with what evidence would settle them; author's read labelled as such
- [ ] Self-citation audited: own work at field-warranted tier; rivals/other methods steelmanned; emphasis identity-blind
- [ ] No important author/school/method an informed referee could say was slighted or omitted

## Anti-patterns

- Comprehensiveness theatre: equal-length summaries of every study (no editorial judgment)
- Vote-counting conflicting results instead of weighing credibility and what-is-studied
- Privileging quantitative findings and treating qualitative/interpretive work as decorative (or the reverse)
- Strawmanning the school the author disagrees with
- A review that doubles as the author's CV (the most-punished ARSoc balance failure)
- Declaring a live debate "resolved" by assertion rather than by laying out the evidentiary state
- Crediting the popularizer of an idea over its originator

## Output format

```text
【Tiering】corpus split foundational/important/confirmatory/tangential? Y/N
【Comprehensiveness evidence】saturation log + citation set support "nothing important missing"? Y/N
【Steelman】each rival school stated at its strongest? Y/N
【Method balance】quant/qual/computational/theoretical each weighed fairly? Y/N
【Conflict handling】reconciled by credibility + what-is-studied (not vote-count)? Y/N
【Debate】evidence-to-settle stated; author's read labelled? Y/N
【Self-citation audit】own work at warranted tier; emphasis identity-blind? Y/N
【Next step】→ arsoc-tables-figures (who-found-what tables + conceptual figure)
```
