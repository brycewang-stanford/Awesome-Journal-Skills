---
name: rfs-tables-figures
description: Use when main-paper exhibits are the bottleneck for a The Review of Financial Studies (RFS) manuscript — table layout, standard-error reporting, and publication-grade figures. Finalizes exhibits; does NOT decide robustness content or move material to the appendix.
---

# Tables & Figures (rfs-tables-figures)

## When to trigger

- The main table has too many columns or unlabeled specifications
- Standard errors, significance stars, or clustering are unclear or inconsistent
- A figure is a default software plot rather than a publication-grade exhibit
- A reader cannot tell from a table alone what the regression is

## What an RFS exhibit must do

Every main table or figure should be **self-contained**: a referee skimming exhibits should grasp the design, the result, and the inference without the text. RFS articles are typeset by **Oxford University Press** for the SFS, so build exhibits to OUP production specs (vector figures, clean two-column-friendly tables). One RFS-specific constraint shapes every exhibit: because RFS requires **public release of all code** as a condition of publication, each table and figure must be **regenerable by the released scripts** — a number a referee cannot reproduce from your code is a liability. The portfolio-sort and spanning exhibits in Hou, Xue, and Zhang (2015) "Digesting Anomalies" (RFS 28(3)) are a good template for decile monotonicity and long–short t-stats.

### Table conventions
- **One question per table.** A main paper typically has a handful of focused tables, not a dozen sprawling ones; overflow goes to the Internet Appendix (`rfs-internet-appendix`).
- **Self-contained caption**: state the sample, period, unit of observation, estimator, and what is being shown.
- **Coefficients with SE below in parentheses**; state the SE type (e.g., "standard errors clustered by firm") in the notes — not only stars.
- **Report significance honestly**: stars are a convenience; the SE/t-stat is the substance. State the convention in the notes.
- **Summary-statistics table**: means, SD, and key percentiles for every variable used; a correlation matrix when relevant.
- **Decimal alignment, consistent rounding, consistent variable names** across all tables.
- **Economic magnitude**, not only statistical significance — report effect sizes in interpretable units.

### Figure conventions
- Event-study / coefficient plots with **confidence bands** for DID and dynamic effects — strongly preferred over a pre/post dummy table.
- Binned scatter / RD plots for discontinuity designs.
- Label axes with units; legends self-explanatory; greyscale-legible (do not rely on color alone).
- Vector format (PDF/EPS) for print; consistent fonts and sizing.

### Reporting conventions that signal craft to finance referees
- Report N and within/adjusted R² (or pseudo-R²) for every regression column.
- State which fixed effects are absorbed in each column (a "FE" panel of yes/no rows).
- For Fama–MacBeth, report the number of cross-sections and the time-series length.
- For portfolio sorts, show monotonicity across deciles and the long–short spread with t-stat.
- Keep one canonical ordering of variables across all tables so readers can scan rows.
- Put units in the caption (returns in %, dollars in millions) — never leave a number unitful.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RFS is finance top-3 (with JF, JFE) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each main table answers one question; the rest is in the IA
- [ ] Every table caption states sample, period, unit, estimator
- [ ] SEs reported below coefficients; SE type stated in notes (clustering/adjustment)
- [ ] Economic magnitudes reported, not just significance
- [ ] Summary-statistics table present for all variables
- [ ] DID/dynamic effects shown as an event-study figure with CIs
- [ ] Figures legible in greyscale; axes labeled with units; vector format (OUP production-ready)
- [ ] Every reported number is regenerable from the code RFS requires you to release
- [ ] Variable names, rounding, and notation consistent across all exhibits

## Anti-patterns

- An 11-column main table where no one can tell what each column estimates.
- Stars with no statement of the standard-error type or clustering.
- Reporting t-stats but never the economic magnitude of the effect.
- A default Stata/R plot pasted in without axis labels or units.
- Color-only figures that become unreadable in print.
- Variable named `x1` in one table and `Leverage` in another.

## Output format

```
【Main exhibits】[table/figure list, one question each]
【SE reporting】type + clustering stated in every table note? yes/no
【Magnitude】economic effect sizes reported? yes/no
【Figures】event-study/RD plots with CIs? format?
【Moved to IA】[...]
【Next step】rfs-internet-appendix
```
