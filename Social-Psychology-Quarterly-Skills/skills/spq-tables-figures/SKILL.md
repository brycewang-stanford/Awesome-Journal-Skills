---
name: spq-tables-figures
description: Use when building tables and figures for a Social Psychology Quarterly (SPQ) manuscript so exhibits are self-contained, accessible, and formatted to the ASA Style Guide. SPQ exhibits must communicate the structure–individual link clearly to a mixed sociology/psychology readership and fit within the word budget. Designs exhibits; it does not run the analysis.
---

# Tables & Figures (spq-tables-figures)

Exhibits are where an expert reviewer checks whether the result is real and whether it actually shows the
**structure–individual link** the paper claims. At SPQ exhibits follow the **ASA Style Guide** and must
stand on their own for a reader who works in a different tradition (a group-processes reviewer reading an
SSP survey table, or vice versa).

## When to trigger

- Designing the main results table/figure or a key descriptive/measurement exhibit
- Deciding what belongs in the article vs. supplementary materials
- A reviewer found an exhibit unclear, mislabeled, or non-self-contained
- Presenting measurement models, multilevel results, or interaction effects clearly

## Principles

1. **Self-contained.** A reader should understand each exhibit from its title, row/column or axis labels,
   and note alone — without hunting through the text. State units, sample, N, and what the estimate is.
2. **Show magnitude and uncertainty.** Predicted-probability and marginal-effects plots, coefficient
   plots with intervals, and clear path/SEM diagrams communicate better than a wall of coefficients.
3. **Make the social-psychological link visible.** Plot the effect of the structural/status variable on
   the individual outcome; show the moderation or mediation that carries the mechanism.
4. **Accessible to a mixed readership.** Colorblind-safe palettes; legible in grayscale; no chartjunk.
   Define construct names a reader outside your tradition may not know.
5. **ASA Style Guide formatting.** Table and figure conventions, notes, and significance reporting per
   ASA style; keep numbering consistent with the text.

## Tradition-specific exhibits
- Group processes/experiments: cell-means/interaction plots, treatment-effect plots with intervals.
- SSP/survey: coefficient/marginal-effects plots, multilevel results tables, measurement (CFA) summaries.
- Interpretive: evidence tables linking claims to interaction excerpts/sources; process diagrams; timelines.

## Article vs. supplementary materials
- Keep the few exhibits that carry the argument in the article; move balance checks, full specifications,
  scale items, and extended robustness to **supplementary materials** (excluded from the ~10,000-word
  budget) — this is also how you fit the cap.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SPQ spans lab/survey experiments and observational work; randomization inference and mediation done right matter for the experimental lane.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Tables that require the prose to be intelligible (not self-contained)
- Reporting significance stars with no effect size or interval
- Burying the structure–individual effect in a coefficient wall instead of plotting it
- Color-only encoding that fails in grayscale or for colorblind readers
- Construct labels meaningful only to your own subfield


## Exhibit pass for Social Psychology Quarterly

Run this as a concrete capability pass. First lock the social-psychological process, measurement, design, and boundary condition across groups or contexts; then test whether the manuscript addresses social-psychology reviewers who expect interaction, identity, group process, or status mechanisms grounded in sociological theory.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against JPSP for psychology breadth, ASR/AJS for sociology theory stakes, Social Forces for broader empirical sociology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Main exhibit】what it shows + why a figure/table
【Shows the structure–individual link?】[Y/N]
【Self-contained?】title + labels + note + N/units present? [Y/N]
【Accessible?】grayscale-legible + colorblind-safe + ASA-style? [Y/N]
【Article vs supplementary】split decided, word-budget impact noted
【Next】spq-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting, SEM-diagram, and exhibit packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ASA Style Guide and word-count rule
