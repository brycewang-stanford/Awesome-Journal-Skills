---
name: jcp-tables-figures
description: Use when building the exhibits for a Journal of Consumer Psychology (JCP) manuscript — condition-means tables, mediation/moderation path figures, interaction plots, and APA-formatted statistical reporting that makes the process visible. Builds the exhibits; it does not run the analysis (jcp-data-analysis).
---

# Tables & Figures (jcp-tables-figures)

## When to trigger

- Your means tables show stars but not the effect sizes/CIs a reviewer needs
- A mediation result is buried in prose instead of shown as a path diagram
- An interaction is described but there is no plot of the simple effects
- Tables/figures do not follow APA format and the copyeditor will bounce them
- Exhibits across studies are inconsistent, so the multi-study chain is hard to follow

## Exhibits at JCP must make the process legible

In a JCP paper the exhibits exist to let a reader **see the mechanism**, not just the effect. A condition-means table that shows cells without the contrast that tests the hypothesis wastes space; a mediation figure that shows the indirect path with its coefficient and CI earns its place. Build exhibits in **APA Style** (7th edition; 检索于 2026-06；以官网为准) — table titles and notes, figure captions, decimals and statistics formatted per APA — because JCP formats manuscripts to APA and non-conforming exhibits create friction at every stage.

## What each exhibit type should carry

| Exhibit | Must show | Common failure |
|---------|-----------|----------------|
| Condition means | M, SD (or SE), n per cell; the focal contrast | a sea of numbers with no highlighted comparison |
| Mediation path figure | a→b paths with coefficients, the indirect effect + bootstrap CI | only c/c′ shown; CI omitted |
| Moderation / interaction plot | the interaction with **probed simple effects** (spotlight values) | bar chart with no simple-effect annotation |
| Moderated mediation | conditional indirect effects by moderator level + index | a single mediation figure that hides the moderation |
| Multi-study summary | a study-by-study row: design, N, key result, effect size | inconsistent metrics across studies |

A path diagram for the focal study and an interaction plot for the key moderation are usually the two highest-value figures; they carry the process argument visually.

## Reporting conventions (APA + rigor era)

- Report **effect sizes and CIs** in tables, not asterisks alone; readers must judge magnitude.
- Keep **decimal places consistent** and follow APA for statistics (e.g., italic test letters, leading zeros per APA convention).
- Note **Ns before and after exclusions** in the table or its note.
- Each exhibit must be **interpretable standalone** — title, note defining abbreviations, and units.
- Do not duplicate the same result in a table and a figure; pick the form that shows the mechanism best.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCP is experimental consumer psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), and family-wise corrections matter most.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every table/figure earns its place by making the **effect or process** clearer than prose would
- [ ] Mediation shown as a path figure with coefficients and the bootstrap CI
- [ ] Interaction shown with probed simple effects (spotlight/floodlight annotated)
- [ ] Effect sizes and CIs present; not asterisk-only
- [ ] APA formatting for tables, figures, notes, and statistics
- [ ] Ns (before/after exclusions) reported; abbreviations defined in notes
- [ ] Metrics consistent across the multi-study exhibits so the chain reads cleanly

## Anti-patterns

- **Asterisk theater**: stars instead of effect sizes and CIs
- **Buried mediation**: the indirect effect described in text with no figure and no CI
- **Naked interaction**: an interaction plot with no simple-effect probing shown
- **Decorative figures**: a chart that repeats a table and adds nothing about the mechanism
- **Non-APA exhibits**: formatting that the JCP copyeditor will return
- **Inconsistent multi-study tables**: different metrics per study, hiding convergence

## Output format

```text
【Key exhibits】which table(s)/figure(s) carry the effect and the process
【Mediation figure】paths + coefficients + bootstrap CI shown? [Y/N]
【Interaction plot】simple effects probed/annotated? [Y/N]
【Reporting】effect sizes + CIs (not asterisk-only)? APA format? [Y/N]
【Multi-study table】consistent metrics across studies? [Y/N]
【Next skill】jcp-writing-style
```
