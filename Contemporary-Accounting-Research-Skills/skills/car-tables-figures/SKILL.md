---
name: car-tables-figures
description: Use when building the exhibits of a Contemporary Accounting Research (CAR) manuscript — descriptive/correlation/results tables for archival work, experimental cell-means and ANOVA tables, model figures, and appendices — formatted to the CAR Style Guide (each exhibit on a new page, variable definitions, footnotes not endnotes). Builds exhibits; it does not run the analysis (car-data-analysis).
---

# Tables & Figures (car-tables-figures)

## When to trigger

- Exhibits are cluttered, not self-contained, or off CAR house style
- A variable-definitions appendix is missing (an archival reviewer staple)
- Experimental results lack a clean cell-means / contrast table
- You are paginating exhibits for the 50-page limit and online appendix

## CAR Style Guide exhibit rules

CAR's format rules (author guidelines + CAR Style Guide) govern exhibits directly:

- **Each exhibit (appendix, table, figure) begins on a new page.**
- In-text notes are **footnotes, not endnotes**; tables use table notes to define every variable, sample, and significance convention.
- Pages are numbered sequentially after the abstract page; the manuscript itself is **blind** (no author identifiers in exhibit titles, file names, or footnotes).
- The main text is held to **30 pages** within a **50-page overall** limit; push large or supplementary exhibits into the **online-only supplementary appendix** rather than padding the main body.
- LaTeX authors may use Wiley's New Journal Design (NJD) template for accepted papers; confirm exact table/figure formatting against the current CAR Style Guide.

## Build exhibits the reviewers expect, by tradition

- **Archival / capital-markets.** Provide (1) a **variable-definitions appendix** with exact construction and data sources — this is mandatory in spirit under the Data Integrity policy; (2) a descriptive-statistics table (N, mean, median, SD, key percentiles), noting winsorizing/truncating; (3) a correlation table (Pearson/Spearman); (4) results tables with coefficients, standard errors (clustered), and the SE-clustering and fixed-effects structure stated in the notes. Report economic magnitude, not just stars.
- **Experimental.** Provide a cell-means table (means, SDs, n per condition), the ANOVA/contrast table, and manipulation-check results; a figure of the predicted interaction aids interpretation.
- **Analytical.** Present propositions/results cleanly; figures should illustrate comparative statics or equilibrium regions, with parameter assumptions noted.

## Self-containment

Every exhibit must be readable without the text: title, sample/period, variable definitions, units, and the meaning of each significance marker all appear in the notes.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CAR is archival/empirical accounting; the DiD / IV / RDD chain serves its causal designs around reporting and regulation.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each exhibit starts on a new page; footnotes (not endnotes) used throughout
- [ ] Variable-definitions appendix present (archival) with sources and construction
- [ ] Descriptive, correlation, and results tables report clustered SEs and FE structure
- [ ] Experimental cell-means, ANOVA/contrasts, and manipulation checks tabulated
- [ ] Economic magnitudes (not only significance) reported
- [ ] Exhibits blind; supplementary material routed to the online-only appendix
- [ ] Numbers reconcile exactly with the code repository and the text

## Anti-patterns

- **Stars without magnitudes**; **endnotes** where CAR requires footnotes.
- **Undefined variables** or a missing definitions appendix.
- **Author identifiers** leaking into exhibit titles or file names.
- **Padding the main body** past 30/50 pages instead of using the online appendix.


## Exhibit pass for Contemporary Accounting Research

Use this as a second-pass capability check. First lock the accounting construct, setting, identification or theory, and disclosure/market/organizational implication; then test whether the manuscript addresses accounting reviewers who expect accounting-specific constructs, credible design, and contribution to reporting, auditing, tax, or governance debates.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against The Accounting Review for US flagship breadth, JAR for Chicago-style accounting research, JAE for economics/accounting interface; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Exhibit list】tables/figures/appendices; each on a new page?
【Variable definitions】appendix present, sources/construction stated?
【Results table】clustered SEs, FE structure, magnitudes shown?
【Experiment】cell means / ANOVA / manipulation checks tabulated?
【Style】footnotes (not endnotes), blind, page budget (30/50) ...
【Next step】car-writing-style
```
