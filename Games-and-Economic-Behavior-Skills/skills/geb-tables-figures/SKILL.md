---
name: geb-tables-figures
description: Use when building exhibits for a Games and Economic Behavior (GEB) manuscript — payoff matrices, extensive-form game trees, equilibrium/result tables, and experimental plots. Makes strategic structure and results readable to a game-theory audience.
---

# Tables & Figures (geb-tables-figures)

## When to trigger

- A game's structure is described in prose instead of shown as a tree or matrix
- A results/comparison table is dense or hard to map to the theorems
- Experimental plots do not show convergence, distributions, or uncertainty clearly
- You are preparing exhibits for the elsarticle-formatted version

## What exhibits do at GEB

GEB papers are game-theoretic, so the most valuable exhibits make **strategic structure** and **formal results** instantly legible to a specialist reader. Figures and tables should let the Editor in Charge and referees verify the setup and see the result without re-deriving it. Format note: the published format is **elsarticle** (`elsarticle-num` citations), and both LaTeX and Word are accepted at submission — but exhibits should be print-clear and self-contained regardless of stage.

## Exhibit types and standards

### Game representations
- **Normal-form payoff matrices** — clean, labeled players/strategies; mark equilibria explicitly.
- **Extensive-form trees** — show information sets, action labels, and payoff vectors at leaves; use `tikz` for crisp vector output.
- **Mechanism / timing diagrams** — stages, messages, and the order of moves where relevant.

### Result exhibits
- **Theorem/assumption maps** — a table relating assumptions to which results use them, so generality is visible at a glance.
- **Comparison tables** — your result versus the nearest prior results (assumptions, class of games, what is proved).
- **Equilibrium tables** — for worked examples, list strategies and payoffs; consistent with the solver output.

### Experimental exhibits
- **Distributions of play and convergence-over-rounds** plots; show the equilibrium prediction as a reference line.
- **Treatment comparisons** with uncertainty shown (CIs or session-level scatter); cluster-aware.
- Avoid chartjunk (no 3D, minimal color); vector output (PDF/EPS) for print.

## Standards (all exhibits)

- Self-contained notes: a reader understands the exhibit without hunting through the text.
- Numbered, called out in order, and tied to the specific theorem or hypothesis they support.
- Notation in exhibits matches the body exactly.
- Legible at print size; equilibria/key cells visually flagged.

## Anti-patterns

- A complex extensive-form game described only in words
- A payoff matrix that does not mark the equilibria
- Experimental bar charts hiding session-level variation and uncertainty
- Tables whose symbols differ from the body's notation
- Color-only encodings that fail in grayscale print

## Output format

```
【Game shown】matrix / tree / mechanism diagram present where needed? [Y/N]
【Equilibria flagged】[Y/N]
【Assumption→result map】present? [Y/N]
【Experimental plots】distributions + convergence + uncertainty? [Y/N / NA]
【Self-contained notes】[Y/N]   【Notation matches body】[Y/N]
【Next step】geb-writing-style
```
