# Mathematical Finance Resources

Action-oriented resources for the *Mathematical Finance* (Wiley) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a theorem-first section and benchmark against
verified exemplars. Pair these with the relevant `skills/mathfin-*/SKILL.md`.

This is a **theory-first** venue (stochastic analysis, pricing theory, proofs). The journal evaluates
submissions on *methodological novelty and contribution to financial modelling*, and explicitly states
that *routine application of computational methods to financial data will not be considered*.
Accordingly, this resource layer is shaped for proof-based work, not empirical estimation.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in *Mathematical Finance* house style — the theorem-first arc (modelling problem → obstruction → main theorem + assumptions → financial payoff → scope). Illustrative **fictional** model; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified *Mathematical Finance* papers** organized by theme × method (risk measures, arbitrage theory, term-structure & rough-volatility models, Lévy pricing, transaction-cost control). Design positioning only — no fabricated theorems or numbers. Includes a sibling-confusion guardrail (NOT *Finance and Stochastics* / SIAM J. Financial Math / *Quantitative Finance* / J. Math. Economics). |
| [`official-source-map.md`](official-source-map.md) | ***Mathematical Finance*-specific policy & facts:** Wiley Research Exchange LaTeX submission, self-contained-proofs / appendix conventions, numerics-must-support-theory rule, single-blind review, Wiley Data Availability Statement, Bachelier Finance Society affiliation, ISSNs, current Wiley editor metadata, and live-check entry points for volatile fee/APC/author-rule details. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and references useful for an MF submission: LaTeX/`amsthm`/`cleveref` workflow, JEL + AMS/MSC classification, symbolic/numerical tools for *illustrative* experiments, and the mathematical toolkit by subfield. |

## No empirical-econometrics code kit (by design)

Unlike the empirical-economics packs in this repository, this pack **does not vendor a causal-inference
/ econometrics code directory** (no Stata `.do` pipeline, no DID/IV/RDD/DML templates). *Mathematical
Finance* is a proof-based venue: there is no JAE-style mandatory replication archive, and routine
computation on financial data is out of scope. The relevant "tooling" here is the LaTeX proof workflow
and *illustrative* numerical experiments that **support a theorem** (convergence rates, error bounds),
covered in prose in [`external_tools.md`](external_tools.md) rather than as a vendored code kit.

## Suggested workflow

1. Scope and frame the contribution with
   [`../skills/mathfin-topic-selection`](../skills/mathfin-topic-selection/SKILL.md) and
   [`../skills/mathfin-contribution-framing`](../skills/mathfin-contribution-framing/SKILL.md); model
   the introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Position at the theorem level with
   [`../skills/mathfin-literature-positioning`](../skills/mathfin-literature-positioning/SKILL.md), and
   polish definitions / assumptions / theorem statements with
   [`../skills/mathfin-writing-style`](../skills/mathfin-writing-style/SKILL.md).
3. If you include numerics, keep them subordinate to the theory with
   [`../skills/mathfin-data-analysis`](../skills/mathfin-data-analysis/SKILL.md); set up the LaTeX /
   classification workflow from [`external_tools.md`](external_tools.md).
4. Benchmark against verified *Mathematical Finance* papers in
   [`exemplars/library.md`](exemplars/library.md); confirm submission, proof, and data-statement policy
   in [`official-source-map.md`](official-source-map.md) before submitting via Wiley Research Exchange.
