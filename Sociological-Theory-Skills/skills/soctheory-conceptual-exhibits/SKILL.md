---
name: soctheory-conceptual-exhibits
description: Use when building the figures and typologies of a Sociological Theory (ST) manuscript — mechanism diagrams, process models, 2x2 typologies, and concept maps that carry theoretical work (never regression tables or data plots). Designs conceptual exhibits; it does NOT build the underlying theory (soctheory-theory-construction) or write the prose (soctheory-writing-style).
---

# Conceptual Exhibits: Typologies, Mechanism Diagrams, Process Models (soctheory-conceptual-exhibits)

## When to trigger

- The theory is built and you need a figure or typology to make it legible
- Your figure is "boxes and arrows" with no readable mechanism
- A typology's cells are not all distinct, defined concepts
- You are tempted to include a data plot or a results table (ST has neither)

> Every exhibit at ST is **conceptual**. There are no regression tables, no scatterplots, no
> coefficient figures — ST does not test, so it has nothing to plot. The exhibit must carry
> *theoretical* work: it shows a mechanism, a process, or a classification that the prose alone
> conveys less clearly.

## The exhibit types ST uses

| Exhibit | Carries | Design rule |
|---------|---------|-------------|
| **Mechanism diagram** | the social process linking concepts | every arrow is a stated mechanism, not a vague "influences" |
| **Process model** | sequence/feedback over time | each stage is a defined concept; loops are theorized, not decorative |
| **Typology (2x2 / nxm)** | a classification along dimensions | dimensions are clearly named; every cell is a distinct, defined type |
| **Concept map** | the relations among a concept family | hierarchy/overlap shown deliberately; no orphan nodes |
| **Comparison table** | this theory vs. rivals, conceptually | rows are theoretical properties, never empirical results |

## Design discipline (the "earn its keep" test)

A conceptual exhibit must do work the prose cannot do as efficiently. Before including it, pass
all three tests:

1. **Readability test.** Can a reader reconstruct the core argument from the figure plus its
   caption alone? If not, it is decoration.
2. **Concept test.** Is every box/cell/node a concept that is *defined in the text* and labeled
   identically? A box with an undefined label is a hole in the theory.
3. **Mechanism test.** Does every arrow / transition name the mechanism it represents? "A → B"
   with no mechanism is exactly the failure `soctheory-theory-construction` warns against,
   reproduced graphically.

## Typology construction

A good ST typology is a theoretical claim, not a filing system:

- The **dimensions** must be conceptually motivated (why these two axes?), not convenient.
- Every **cell** must be a real, distinct type — name it and define it; an empty or forced cell
  signals the dimensions are wrong.
- The typology should generate **propositions** (e.g., types in cell 3 behave differently
  because of mechanism M), tying back to `soctheory-theory-construction`.
- Watch scope: a typology that implies coverage beyond the stated domain over-claims (see
  `soctheory-boundary-conditions`).

## Propositions table (optional, for proposition-heavy papers)

If the paper has many propositions, a compact table listing P1…Pn with their one-line
mechanisms helps reviewers track the theory. It is a *theoretical* table — propositions and
mechanisms only, never coefficients or significance.

## Format notes

- Figures should meet the publisher's resolution/format requirements; confirm exact specs on
  the SAGE/ST author page (检索于 2026-06；以官网为准).
- Figures and tables count toward ST's overall length limit (all material is inclusive of the
  word cap; see `soctheory-writing-style` / `soctheory-submission`), so an exhibit must earn its
  space against the cap, not just against the page.

## Checklist

- [ ] Every exhibit is conceptual (mechanism / process / typology / concept map / theory-comparison)
- [ ] No data plot, scatterplot, coefficient figure, or results table anywhere
- [ ] Each box/cell/node is a concept defined in the text with an identical label
- [ ] Each arrow/transition names its mechanism
- [ ] The figure passes the readability test (argument recoverable from figure + caption)
- [ ] Typology dimensions are motivated and every cell is a distinct, defined type
- [ ] Exhibits respect the stated boundary conditions and the word/length cap

## Anti-patterns

- Boxes-and-arrows with undefined labels or unlabeled arrows
- A data plot or regression table imported from an empirical template (impossible at ST)
- A 2x2 with a forced or empty cell, revealing mis-chosen dimensions
- A figure that merely restates a sentence, adding nothing
- Labels in the figure that differ from the concept names in the text
- A typology that implies coverage outside the theory's domain

## Output format

```
【Exhibit type】mechanism diagram / process model / typology / concept map / theory-comparison
【Concepts in exhibit】all defined in text + identically labeled: yes / fix [...]
【Arrows】each names a mechanism: yes / fix [...]
【Readability test】argument recoverable from figure+caption: yes / no
【Typology】dimensions motivated; every cell distinct: yes / n/a
【Next step】soctheory-contribution-framing
```
