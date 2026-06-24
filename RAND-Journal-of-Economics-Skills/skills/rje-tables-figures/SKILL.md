---
name: rje-tables-figures
description: Use to design tables and figures for a RAND Journal of Economics (RJE) industrial-organization manuscript — parameter, elasticity, markup, merger-simulation, and counterfactual-welfare exhibits — formatted under the RJE Style Guide (numbered sections, unnumbered subsections, flush-right equations) and disciplined by the hard page caps. Exhibit design, not estimation.
---

# Tables & Figures (rje-tables-figures)

## When to trigger

- Turning IO estimates into the article's main exhibits
- Deciding which tables stay in the 40-page main text and which go to the appendix
- Formatting exhibits and equations to the RJE Style Guide

## What RJE exhibits carry

As the **industrial-organization flagship**, RJE expects exhibits that communicate **market behavior and welfare**, not just regression output:

- **Demand / cost parameter tables** with standard errors and the estimation method noted.
- **Elasticity matrices** (own/cross-price) demonstrating sensible substitution.
- **Markup / marginal-cost tables** tying estimates to conduct.
- **Merger-simulation and counterfactual tables** reporting price, output, and **welfare (consumer/producer surplus)** changes, with the maintained assumptions stated in the note.
- **Reduced-form work:** clean event-study plots (leads and lags, confidence bands) and treatment-effect tables.

Each exhibit should be **self-contained**: a reader sees the market, the specification, the units, and the assumption set from the note alone.

## RJE Style Guide formatting

- **Sections numbered consecutively; subsections unnumbered** — match table/figure callouts to that scheme.
- **Equations numbered flush right**, with **(1a)/(1b)** for multi-part equations.
- Author-date references in notes (no page numbers, no issue numbers).
- Vector output (PDF/EPS) for print; keep figures legible in greyscale; avoid chartjunk.

## Page-cap discipline (hard)

Main text **<=40 pp**, total **<=50 pp**, double-spaced. Exhibits eat pages fast:

- Keep in the main text the **decisive** exhibits: headline estimates, the key elasticity/markup table, and the central counterfactual/welfare result.
- Move full parameter dumps, alternative specifications, and robustness exhibits to the **appendix** (within the <=10-page appendix+references budget).
- Do not offload core exhibits into supporting information, which RJE discourages and may decline.

## Exhibit-placement table (main text vs appendix)

Every exhibit must earn its main-text page. Sort by whether it carries the article's core argument or supports it.

| Exhibit | Carries | Placement |
|---|---|---|
| Headline demand/cost parameters | The estimated structural primitives | Main text |
| Own/cross-price elasticity matrix | Substitution credibility | Main text (one matrix) |
| Markup / marginal-cost summary | The conduct-to-cost mapping | Main text (compact) |
| Central merger-sim / counterfactual welfare | The policy payoff of the article | Main text |
| Full random-coefficient parameter dump | Completeness | Appendix |
| Alternative specifications / robustness battery | Defense, not headline | Appendix |
| Event-study leads/lags (reduced-form) | Identification credibility | Main text plot, full table appendix |

## Worked vignette: a self-contained counterfactual table

Suppose your central exhibit reports a merger simulation. Built to RJE standards, the table note alone tells the reader everything:

- **Rows**: merging brands, key rivals, market aggregate. **Columns**: pre-merger price, predicted post-merger price, % change, consumer-surplus change, producer-surplus change.
- **Illustrative content**: merging brands +4.2% price, rivals +1.1%, consumer surplus -$31m/year, producer surplus +$44m/year, with a bracketed range across demand specifications.
- **Note (self-contained)**: states the demand model, the conduct assumption (Bertrand-Nash), that the product set is held fixed, that costs are recovered from FOCs, and the units (annualized dollars), plus author-date sources with no page or issue numbers.

A reader who sees only this table should grasp the market, the specification, the maintained assumptions, and the welfare verdict — no hunting through the text.

## Referee-pushback patterns and the venue fix

- **"The welfare table has no maintained-assumption note."** Fix: state the conduct, the fixed-product-set assumption, and the demand specification in the note itself.
- **"The elasticity matrix implies implausible substitution."** Fix: flag the suspect cells, explain the market reason, or revisit the random-coefficient specification driving them.
- **"Main-text tables blow the page cap."** Fix: keep one decisive table per claim in the body and route full parameter dumps to the appendix within the budget.
- **"Figures are illegible in greyscale print."** Fix: use vector output, distinguish series by line style not color, and avoid chartjunk.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAND is industrial organization — endogeneity of prices/entry and structural demand; the reduced-form chain for causal claims, structural IO outside it.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A wall of parameter tables in the main text blowing the 40-page cap
- Counterfactual/welfare tables with no maintained-assumption note
- Elasticity matrices that imply implausible substitution, unexplained
- Numbered subsections or inline equation numbers (off RJE style)
- Low-resolution raster figures illegible in print/greyscale

## Output format

```
【Main-text exhibits】[headline estimates, key elasticity/markup, central counterfactual]
【Appendix exhibits】[full params, robustness, alt specs]
【Self-contained notes】units + specification + assumptions? [Y/N]
【Style】sections numbered/subsections not; eqns flush-right (1a)/(1b)? [Y/N]
【Page budget】main __/40, total __/50 — within cap? [Y/N]
【Next step】rje-writing-style
```
