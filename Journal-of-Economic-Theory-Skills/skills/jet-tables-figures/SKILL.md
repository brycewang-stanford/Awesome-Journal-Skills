---
name: jet-tables-figures
description: Use when designing the exhibits in a Journal of Economic Theory (JET) paper — mostly schematic theory figures (best-response/phase diagrams, lattices, timing trees, mechanism flow) and small illustrative tables, kept consistent with the body's notation and rendered as vector graphics. Light for a theorem-proof journal; numerical tables only when grounded in theory.
---

# Exhibits: Tables & Figures (jet-tables-figures)

## When to trigger

- You need a diagram to convey an equilibrium, a mechanism, or a comparative-static
- You have a small numerical table illustrating a theorem
- You are formatting exhibits for elsarticle submission

## What exhibits look like at JET

JET is a **theorem-proof** journal, so most exhibits are **schematic, not data-driven**. The typical
JET figure clarifies an argument:

- **Best-response / phase diagrams**, indifference maps, region partitions of a parameter space
- **Lattices / Hasse diagrams** for order-theoretic results; **timing / extensive-form trees** for games
- **Mechanism / information flow** diagrams; revelation or allocation schematics
- **Bound / tightness plots** showing where a characterized object sits

Numerical tables are **light and subordinate** — admitted only to illustrate or test a theoretical
result (see jet-data-analysis), never as the paper's payload.

## Construction rules

- **Notation must match the body exactly** — same symbols, same names for regions/agents/types. A figure
  that renames objects costs the referee more than it saves.
- **Vector output (PDF/EPS)** for print; build diagrams in **TikZ/PGF** (native to elsarticle LaTeX) or
  `pgfplots`; export matplotlib/Julia plots to PDF.
- **Self-contained captions/notes**: define every symbol, axis, and shaded region in the note so the
  exhibit reads without the surrounding text.
- **Label the economics, not just the math**: name what a region/curve means (e.g., "pooling region"),
  not only the inequality that defines it.
- Number figures/tables and call them out in order in the text.

## Exhibit necessity test

Keep an exhibit only if it does one of four jobs:

- Makes a theorem's domain or partition visible.
- Shows a counterexample or tightness construction.
- Clarifies a mechanism, timing, information flow, or allocation rule.
- Reproduces a small numerical illustration that is subordinate to a formal result.

If the exhibit is decorative or repeats a proof step without reducing cognitive load, delete it. JET
referees value proof clarity more than visual volume.

## Anti-patterns

- A figure introducing notation that conflicts with the proof
- Raster screenshots or low-resolution diagrams
- A large numerical table presented as a result in a theory paper
- A diagram with no self-contained note, unreadable away from its paragraph

## Output format

```
【Exhibit】<schematic type> | small illustrative table
【Notation match】identical to body? [Y/N]
【Format】vector (TikZ/PDF), self-contained note? [Y/N]
【Role】clarifies argument | illustrates theorem (subordinate)
【Next】jet-writing-style / jet-submission
```
