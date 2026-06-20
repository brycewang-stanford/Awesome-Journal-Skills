---
name: jel-comprehensiveness-and-balance
description: Use when calibrating completeness vs. selectivity and ensuring fairness across schools, authors, and controversies in a Journal of Economic Literature (JEL) survey — including not over-promoting the author's own work. Audits coverage and even-handedness; it does not design the framework (jel-organizing-framework) or write prose (jel-writing-style).
---

# Comprehensiveness & Balance (jel-comprehensiveness-and-balance)

## When to trigger

- The framework is set and you are filling cells with the literature
- You are unsure whether to cite *everything* or curate
- The field has rival schools, a live controversy, or conflicting empirical results
- You are a contributor to this literature and worry the survey tilts toward your own work

## Completeness vs. selectivity: the JEL contract

A JEL survey must be **comprehensive in coverage** yet **selective in emphasis**. The reader should trust that nothing important is missing, while the prose foregrounds what matters. Resolve the tension by **tiering** the corpus:

| Tier | Treatment |
|------|-----------|
| **Foundational / field-defining** | discussed in the text, with what they established and their limits |
| **Important contributions** | grouped and weighed within the framework's cells; cited with their finding |
| **Confirmatory / incremental** | cited in clusters ("see also …") to demonstrate coverage without bloating prose |
| **Tangential** | cited only where they bear on a specific claim; not every adjacent paper belongs |

Comprehensiveness is proven by the *citation set* (the saturation log from `jel-literature-synthesis`); selectivity is exercised in the *prose*. A survey that discusses every paper at equal length has abdicated the editorial judgment that is its value.

## Fairness across schools, authors, and findings

JEL is the **survey of record**: its account of a debate becomes the field's shared reference. That obliges genuine even-handedness:

- **Steelman every camp.** State each school's strongest case in terms its proponents would accept *before* noting its weaknesses. Refute positions at their best, never at their worst.
- **Weigh, don't tally.** Conflicting results are reconciled by *credibility* (identification, data, replication) and by *what each estimates*, not by vote-counting "7 studies find positive, 4 negative."
- **Attribute ideas correctly.** Credit originators, not just popularizers; this is a recurring referee complaint.
- **Handle live controversies without resolving by fiat.** Lay out the disagreement, what evidence would settle it, and where the author's own read sits — labelled as the author's read, not as consensus.

## The self-citation trap

If you have published in the field, the survey must **not** read as a retrospective of your program. Guardrails:

- Your own work is cited at the tier its *importance to the field* warrants — no more.
- Rivals to your work are given their strongest statement.
- A reader who does not know who wrote the survey cannot tell from the emphasis.
- When the field disagrees with you, say so plainly and represent the other side fairly.

## Checklist

- [ ] Corpus tiered (foundational / important / confirmatory / tangential); prose emphasis matches tier
- [ ] Comprehensiveness provable from the citation set + saturation log
- [ ] Every rival school stated at its strongest before critique (steelman)
- [ ] Conflicting findings reconciled by credibility and estimand, not vote-counting
- [ ] Idea attribution traces to originators
- [ ] Live controversies presented with what evidence would settle them; author's read labelled as such
- [ ] Self-citation audited: own work at field-warranted tier; rivals steelmanned; emphasis is identity-blind
- [ ] No important author/school an informed referee could say was slighted or omitted

## Anti-patterns

- Comprehensiveness theatre: equal-length summaries of every paper (no editorial judgment)
- Vote-counting conflicting results instead of weighing credibility and estimand
- Strawmanning the camp the author disagrees with
- A survey that doubles as the author's CV (the most-punished JEL balance failure)
- Declaring a live controversy "resolved" by assertion rather than by laying out the evidentiary state
- Crediting the popularizer of an idea over its originator

## Output format

```
【Tiering】corpus split foundational/important/confirmatory/tangential? Y/N
【Comprehensiveness evidence】saturation log + citation set support "nothing important missing"? Y/N
【Steelman】each rival school stated at its strongest? Y/N
【Conflict handling】reconciled by credibility + estimand (not vote-count)? Y/N
【Controversy】evidence-to-settle stated; author's read labelled? Y/N
【Self-citation audit】own work at warranted tier; emphasis identity-blind? Y/N
【Next step】→ jel-tables-figures (who-found-what tables) → jel-writing-style
```
