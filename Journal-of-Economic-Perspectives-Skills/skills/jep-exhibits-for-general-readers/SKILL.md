---
name: jep-exhibits-for-general-readers
description: Use when designing figures and tables for a Journal of Economic Perspectives (JEP) article aimed at a broad audience — clarity over density, self-explanatory exhibits. Handles exhibit design; defer prose evidence to jep-evidence-without-equations and overall structure to jep-narrative-arc.
---

# Exhibits for General Readers (jep-exhibits-for-general-readers)

## When to trigger

- A figure or table was lifted straight from a research paper and is dense
- A reader needs the caption *and* the body text to decode an exhibit
- The piece has too many exhibits, or exhibits that don't advance the argument
- A regression table with coefficients and asterisks is doing the explaining

## The JEP exhibit bar

A JEP exhibit must be **self-explanatory to a non-specialist** and earn its place in the *argument*. Clarity beats density: the reader should grasp the point from the exhibit and its caption alone, in seconds, without parsing the methods. JEP avoids significance asterisks and coefficient-table presentation in favor of exhibits that *show the idea*.

## Design principles

- **One exhibit, one point.** Each figure/table makes a single claim that maps to a step in the narrative arc. If it makes three points, split it or cut two.
- **Self-explanatory title + caption.** The title states the *finding* ("Pass-through has fallen since 2000"), not the *variables* ("Price on cost, 1990–2020"). The caption gives source, units, and the one thing to notice.
- **Figures over tables for trends and comparisons.** A clear line/bar chart usually beats a number grid for a general reader. Reserve tables for a few labeled, rounded quantities.
- **Round and label.** Plain units, rounded numbers, direct labels on lines/bars instead of a legend the reader must cross-reference.
- **No significance asterisks or coefficient dumps.** If uncertainty matters, show it as a shaded band or a stated range, not stars (mirrors `jep-evidence-without-equations`).
- **Minimal chartjunk.** No 3-D, no needless gridlines, no decorative color. Color should encode meaning or be dropped (and survive grayscale, since print/archives may be monochrome).
- **Few, load-bearing exhibits.** A short synthesis essay carries a handful of exhibits, each indispensable — not a research paper's full battery.

## Table discipline (when a table is right)

- Rows/columns labeled in plain words, not variable names.
- A small number of rounded figures, not full estimation output.
- A one-line note: source, units, sample/coverage, and the takeaway.
- No standard-error parentheses-and-stars apparatus; if precision matters, state a range in the note.

## Checklist

- [ ] Each exhibit makes exactly one point tied to a narrative step
- [ ] Title states the finding; caption gives source, units, and what to notice
- [ ] Figures used for trends/comparisons; tables only for a few labeled quantities
- [ ] Numbers rounded; lines/bars directly labeled (legend minimized)
- [ ] No significance asterisks, no raw coefficient tables
- [ ] Uncertainty shown as band/range, not stars
- [ ] Exhibit is legible in grayscale; no chartjunk
- [ ] Total exhibit count is small and every one is load-bearing

## Worked vignette (illustrative)

A draft transplants a research-paper Table 3: eight columns of coefficients, standard errors in parentheses, and rows of asterisks, titled "Regression results." The JEP exhibit replacing it is a single line chart titled with its finding — "Pass-through to consumer prices has roughly halved since 2000" — one line, directly labeled, a shaded band for the range across studies, source and units in a one-line note, and nothing else. The reader gets the point in three seconds, in grayscale, without reading the body — which is the entire test.

## Anti-patterns

- A regression table with coefficients, SEs, and *** transplanted from the working paper
- A figure whose point you can't state in its title
- Legends and variable names that force the reader back into the text
- Color or 3-D that carries no information (and breaks in grayscale)
- Ten exhibits where three would carry the argument
- A "kitchen-sink" table of every specification (that belongs in research, not JEP)

## Output format

```
【Exhibit】[figure/table] — one-point claim: [...]
【Finding-title】[...]
【Caption】source / units / what to notice
【Form】figure (trend/comparison) / small labeled table — chosen because [...]
【Uncertainty shown as】band / stated range (no asterisks)
【Grayscale-safe + chartjunk-free?】[Y/N]
【Count check】N exhibits, each load-bearing? [Y/N]
【Next step】jep-writing-style
```
