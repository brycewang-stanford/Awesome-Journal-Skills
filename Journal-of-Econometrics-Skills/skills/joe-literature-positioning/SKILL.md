---
name: joe-literature-positioning
description: Use when the contribution of a Journal of Econometrics (JoE) manuscript relative to the econometrics literature is fuzzy or undersold. Locates the paper precisely against the nearest estimators, tests, and asymptotic results so referees see the methodological delta.
---

# Literature Positioning (joe-literature-positioning)

## When to trigger

- A referee could ask "how is this different from [known estimator/test]?" and you lack a crisp answer
- The related-work section lists papers but never states the precise gap
- You cannot name the single closest prior method and the exact dimension on which you improve
- Reviewers might think the result is a special case of something already published

## Why positioning is decisive at JoE

The *Journal of Econometrics* judges a paper first on its **methodological novelty and rigor**. Editors screen submissions before sending suitable papers to a **minimum of two independent referees** (single-anonymized review), and these referees are typically specialists who know the nearest competing methods cold. A manuscript that does not locate itself precisely against the frontier reads as either redundant or unaware — both are desk- or referee-level rejections. Positioning is not a literature dump; it is an argument that a specific gap exists and that you close it.

## Positioning moves specific to econometric methodology

State the contribution along the axes referees actually use:

1. **Assumptions** — do you achieve the result under *weaker* or more *primitive* conditions (e.g., dropping homoskedasticity, allowing dependence, weak identification, fewer moment conditions)?
2. **Generality** — does the method cover a broader class of models, DGPs, or data structures (panel, time series, network, high-dimensional)?
3. **Efficiency / rate** — better asymptotic variance, faster convergence rate, semiparametric efficiency, or oracle property?
4. **Inference validity** — correct size where existing tests over/under-reject; uniform validity; robustness to nuisance parameters or tuning choices.
5. **Computation** — feasible where prior methods are intractable, with the *same* statistical guarantees.

Then tie each claimed gap to a citation and, ideally, to a Monte Carlo comparison and a theorem.

## Building the positioning

- Identify the **single nearest method** and write one sentence: "Unlike X (Author, year), which assumes/achieves ___, we ___."
- Map the **lineage**: the classical result, the modern refinements, and where you sit.
- Use **Elsevier reference style** (numbered or author-year, CSL-compatible); cite datasets with the `[dataset]` tag where relevant.
- Pre-empt the "special case" objection: show explicitly that prior results are nested or that your conditions are not implied by theirs.

## Anti-patterns

- A related-work paragraph that summarizes papers but never states *your* delta
- Claiming "novel" against a strawman while ignoring the closest competitor
- Comparing only on intuition with no Monte Carlo or analytic comparison
- Over-broad claims ("first to...") that a referee can falsify with one citation


## Positioning pass for Journal of Econometrics

Use this as a second-pass capability check. First lock the estimand or theorem, assumptions, asymptotic/simulation evidence, and applied relevance; then test whether the manuscript addresses econometrics reviewers who expect methodological novelty, assumptions, simulation or empirical illustration, and reproducibility.

- **Primary move:** Map incumbent conversation, unresolved tension, this manuscript's delta, and the sibling-venue omission a referee might notice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Econometric Theory for proof-first work, JBES for applied statistical methods, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Nearest method】Author (year): assumes/achieves ___
【Our delta】weaker assumptions / generality / efficiency / inference / computation
【One-sentence positioning】"Unlike X, we ___."
【Lineage】classical → refinement → this paper
【Evidence of the gap】theorem ref + Monte Carlo comparison
【Next step】joe-identification-strategy
```
