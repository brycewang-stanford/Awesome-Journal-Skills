# External Tools — *Econometric Theory*

Use these tools only as aids. ET-specific facts must be checked against
[`official-source-map.md`](official-source-map.md) before giving submission advice.

## Official pages

- Cambridge Core journal home: <https://www.cambridge.org/core/journals/econometric-theory>
- Cambridge author instructions: <https://www.cambridge.org/core/journals/econometric-theory/information/author-instructions>
- Cambridge supplementary-material instructions: <https://www.cambridge.org/core/journals/econometric-theory/information/instructions-contributors/author-instructions-for-online-publication-of-supplementary-material>

## Proof and manuscript tooling

- LaTeX theorem environments: keep assumptions, lemmas, propositions, theorems, corollaries, and proofs consistently numbered and cross-referenced.
- `amsmath`, `amsthm`, `mathtools`, `bm`, and `bbm`: standard theorem-proof notation support.
- `latexmk -pdf`: compile the main PDF and supplementary material repeatedly enough to catch missing references.
- `chktex` or editor linting: catch common LaTeX syntax and spacing problems before submission.

## Simulation and implementation checks

- Stata, R, Julia, Python, or MATLAB may be appropriate for simulations, but the code must serve the theorem: boundary cases, size/power, convergence, or estimator behavior.
- Fix random seeds, record package versions, and separate data-generation code from analysis code.
- Save simulation settings in a machine-readable file (`.json`, `.yaml`, `.toml`, or a table) so a referee can see which parameter grid produced each table.

## Reproducibility package skeleton

For any computational supplement:

```text
supplement/
  README.md
  main_simulation.*
  config/
  output/
  tables/
  figures/
```

The README should state the software versions, seed policy, expected runtime, and exact command sequence.
Do not use a computation supplement to introduce results that were not reviewed with the manuscript.
