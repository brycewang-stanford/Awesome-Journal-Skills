---
name: ecj-writing-style
description: Use when polishing the prose of a The Economic Journal (EJ) manuscript into its clear, generalist-legible, economics-first register. Tightens voice, structure, and citation/format house style; it does not fix the economic argument itself (see ecj-theory-model / ecj-identification).
---

# Writing Style & House Conventions (ecj-writing-style)

## When to trigger

- The draft is wordy, hedged, or buries the result under qualifications
- Prose explains procedure before establishing economic purpose
- A reader outside your subfield gets lost; the writing assumes too much
- This is the **late polish** stage — identification and model are already sound

## The EJ voice: exposition is part of the contribution

EJ prose must be **clear, precise, and legible to a broad international readership**. EJ has long valued *clear exposition* alongside substance: a generalist economist should follow the argument; a specialist should find it rigorous. This is the journal's distinguishing register — at EJ, an unreadable paper underperforms its own substance, so the writing earns real weight in the decision. The writing carries an argument; every paragraph advances the economic case, and the economic intuition is stated in words before the algebra.

Register rules:
- Lead with the economics, then the method. "Higher entry costs reduce competition; we estimate this using..." not "We run a regression of price on entry cost."
- State results plainly. Replace "our findings appear to suggest a potentially meaningful relationship" with "entry costs raise prices by X%."
- Write for the generalist: define field-specific terms on first use; do not assume the reader knows your subfield's acronyms.
- Active voice for what the paper does; reserve hedging for genuine uncertainty.
- Define notation once, use it consistently; explain each equation's economic content in prose.
- Cut throat-clearing ("It is important to note that...", "In this paper, we will...").

## Structure conventions

- **Sections**: Introduction → (Model / Theory) → Data / Institutional setting → Empirical strategy → Results → Mechanisms / Robustness → (Counterfactuals) → Conclusion. Order theory before empirics when the model leads.
- **Introduction** does the heavy lifting (see `ecj-literature-positioning`): question, why a generalist cares, what is known, the gap, what you do, findings and the broad lesson.
- **Conclusion** states what economics learned and the portable lesson — not a summary of every table.
- **Short paper** (AER:Insights-style): compress hard to <6,000 words and ~5 exhibits (检索于 2026-06；以官网为准) — every sentence earns its place; one clean idea, no scaffolding.
- Footnotes for genuine asides, not for results that belong in the text.

## House-style format

- **References: author-date** style, with an alphabetized reference list. Verify EJ's *current* reference and formatting requirements on the official OUP author guidelines before submission — formatting details are updated periodically and the exact style name is 待核实.
- Submit as a **single PDF** including appendices (检索于 2026-06；以官网为准). Equations numbered and referenced as "equation (3)."
- Abstract: state the question, what you do, the headline magnitude, and the broad implication; verify the current abstract word limit on the official page (待核实).
- JEL classification codes and keywords are requested at submission via Editorial Express.
- Acknowledge all sources of research funding in the manuscript (EJ requirement).

## Checklist

- [ ] Each paragraph advances the economic argument; throat-clearing removed
- [ ] Results stated plainly with magnitudes, hedging reserved for real uncertainty
- [ ] Economics stated before method in every key passage
- [ ] Written for a generalist — subfield jargon defined or removed
- [ ] Every equation has a sentence of economic interpretation
- [ ] Citations are author-date and consistent; reference list complete
- [ ] Conclusion states the portable economic lesson, not a table-by-table recap
- [ ] Funding acknowledged; JEL codes and keywords prepared
- [ ] (Short paper) within the word/exhibit budget
- [ ] Format and reference style checked against EJ's current official guidelines

## Anti-patterns

- Hedged, passive prose that obscures a result the evidence actually supports
- Method-first writing that makes the reader hunt for the economics
- Writing for the subfield — unexplained jargon that a generalist cannot follow (EJ's core failure mode)
- Equations dropped in with no verbal economic interpretation
- A conclusion that recaps every table instead of stating what was learned
- Padding a short paper past its budget, or starving a full-length argument of needed exposition

## Output format

```
【Voice】economics-first, generalist-legible, unhedged where warranted? [y/n + fixes]
【Hedging removed】list of softened claims tightened
【Jargon】defined/removed for a generalist? [y/n]
【Equations interpreted】all have prose meaning? [y/n]
【Citation style】author-date verified against current EJ guidelines
【Length mode】full-length / short paper (budget respected? [y/n])
【Conclusion】states portable lesson? [y/n]
【Next】ecj-referee-strategy
```
