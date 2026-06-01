---
name: rje-writing-style
description: Use to make a manuscript conform to The RAND Journal of Economics (RJE) Style Guide — author-date citations with no page numbers, references with no issue numbers, numbered sections with unnumbered subsections, flush-right equation numbering, and the journal's distinctive house usage rules. Style and usage polish, not content drafting.
---

# RJE House Style (rje-writing-style)

## When to trigger

- Final language and citation polish before submission to RJE
- Converting a draft from a numbered/footnote citation style to RJE author-date
- Catching the journal's specific usage rules that copy editors enforce

## The RJE Style Guide (verified 2026-06-01)

RJE maintains its own Style Guide (rje.org/styleguide.html), which directs authors to the **Chicago Manual of Style** (edition 待核实). Its load-bearing rules:

### Citations and references
- **In-text:** author-date, **name and year only, no page numbers** — e.g., "(Jones, 1991)" or "Jones (1991)".
- **Reference list:** alphabetical, **unnumbered**, at the end of the text, with **no issue numbers** in journal citations.

### Structure and numbering
- **Sections numbered consecutively; subsections are NOT numbered.** This is a frequent slip for authors coming from journals that number 2.1, 2.2.
- **Equations numbered consecutively, flush right**, using **(1a)/(1b)** for multi-part equations.
- **Footnotes kept short** — roughly 50 words / 3 typeset lines each.
- Abstract **<=100 words**; main text **<=40 pp**, total **<=50 pp**, double-spaced.

### Distinctive house usage rules
- Use **"because"** or **"as"** instead of **"since"** when the meaning is causal (reserve *since* for time).
- Use **"whereas"** or **"although"** instead of **"while"** when the meaning is contrastive (reserve *while* for simultaneity).
- Use **"article,"** not **"paper,"** to refer to the manuscript.

## Tone for the IO flagship

Write for an industrial-organization audience: name the **market, the firms' strategic problem, and the policy/welfare stake** plainly. Define the structural primitives or the identifying variation early, and let demand/cost parameters, elasticities, and counterfactual welfare numbers carry the argument. Avoid general-interest throat-clearing; RJE readers want the economics of the market.

## Anti-patterns

- Page numbers in in-text cites, or issue numbers in the reference list
- Numbered subsections (2.1, 2.2) — RJE leaves subsections unnumbered
- "Since" for causation and "while" for contrast; calling the manuscript a "paper"
- Sprawling footnotes; an over-length abstract
- Left-aligned or inline equation numbers instead of flush-right (1a)/(1b)

## Output format

```
【Citations】author-date, no page numbers? [Y/N]
【References】alphabetical, unnumbered, no issue numbers? [Y/N]
【Numbering】sections numbered, subsections unnumbered, eqns flush-right? [Y/N]
【House usage】because/as, whereas/although, "article" not "paper"? [Y/N]
【Limits】abstract <=100w; footnotes short? [Y/N]
【Next step】rje-replication-and-data-policy → rje-submission
```
