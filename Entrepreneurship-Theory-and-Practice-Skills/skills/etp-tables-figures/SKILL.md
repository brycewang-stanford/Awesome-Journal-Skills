---
name: etp-tables-figures
description: Use when building the exhibits for an Entrepreneurship Theory and Practice (ETP) manuscript — results tables, the theoretical/mechanism model figure, and (for qualitative work) the Gioia data structure, in APA style.
Builds exhibits; it does not run the analysis (etp-data-analysis) or write the prose (etp-writing-style).
---

# Tables & Figures (etp-tables-figures)

## When to trigger

- Your results tables are dense walls of coefficients a reviewer cannot read
- The paper has no figure that shows the *theoretical model* / mechanism
- A qualitative paper lacks a data-structure figure (1st-order → 2nd-order → dimensions)
- Tables use significance asterisks as the headline and omit effect sizes / CIs
- Exhibits are not APA-formatted or appear at the end rather than near their callout

## What ETP exhibits must do

At ETP, exhibits carry two loads: the **empirical** (do the numbers support the claim?) and the **theoretical** (can a reader *see* the mechanism?).
The journal's strong-theory identity means a **conceptual/mechanism figure is expected** in most papers — a diagram of the hypothesized chain (antecedents → entrepreneurial mechanism → outcomes, with moderators/mediators) — and for inductive work a **Gioia data structure** is essentially mandatory.
Format to **APA**: descriptive titles, defined abbreviations, notes that make the table self-contained.

## The exhibit suite by paper type

| Paper type | Expected core exhibits |
|------------|------------------------|
| Deductive quantitative | Theoretical model figure; descriptives + correlations; main regression table; interaction/moderation plots |
| Survival / event-history | Theoretical figure; Kaplan–Meier curves; hazard table with hazard ratios + CIs |
| SEM | Theoretical model figure; measurement model (loadings, AVE, CR); structural model with standardized paths |
| Inductive / qualitative | Gioia data structure; process model figure; quotation table linked to informants |
| Mixed methods | Data structure (qual phase) + regression/SEM (quant phase) + an integrating figure |

## Make results tables earn their space

- **Lead with magnitude, not stars.** Report coefficients with standard errors and, where possible, confidence intervals; give effect sizes (hazard ratios, marginal effects, standardized betas).
  Significance asterisks may appear by APA convention, but they cannot be the story.
- **One question per table.** A reader should know what claim each table tests from its title.
- **Show the moderation, don't just tabulate it.** An interaction is best read as a simple-slopes plot; a table of products rarely communicates the contingency.
- **Correlation tables**: include means, SDs, and reliabilities on the diagonal for self-report constructs.

## The mechanism figure is a contribution, not decoration

A clean theoretical model figure does triple duty: it states the hypotheses visually, signals the entrepreneurial mechanism (so a reviewer cannot mistake it for a generic-org model), and gives the reader a map for the results.
Label the constructs with your *entrepreneurial* names (e.g., "affordable-loss reasoning," "socioemotional wealth"), not generic placeholders, and make moderators/mediators visually distinct.

## Qualitative exhibits

The Gioia data structure is the trust contract for inductive ETP work: it shows the inductive chain from informant terms to theoretical dimensions.
Pair it with a process-model figure (the dynamic "movie" of the static data structure) and a quotation table that ties evidence to dimensions and informants.
Thin or absent data structures are a fast credibility loss.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ETP is entrepreneurship, where selection and survival bias are pervasive — foreground identification and selection corrections.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] A theoretical/mechanism figure is present and labeled with entrepreneurial constructs
- [ ] Inductive papers include a Gioia data structure and a process model
- [ ] Results tables lead with magnitude (effect sizes, CIs), not asterisks alone
- [ ] Interactions/moderations shown as plots, not just product terms
- [ ] Correlation table reports means, SDs, and reliabilities
- [ ] Every exhibit is self-contained (APA title + notes) and called out near its placement
- [ ] No exhibit carries a claim the main text fails to make

## Anti-patterns

- **No mechanism figure** in a theory-forward paper
- **Asterisk-as-headline** tables with no effect sizes or CIs
- **Generic-construct labels** that let a reviewer recast the model as non-entrepreneurial
- **Interaction-as-table** with no simple-slopes plot
- **Decorative figures** that repeat the text without adding interpretive value
- **Thin/absent Gioia structure** in an inductive submission

## Worked vignette (illustrative)

A quantitative effectuation paper submits four dense regression tables, asterisks marking significance, and no figure.
An ETP-ready exhibit suite reorganizes this.
Add a **theoretical model figure** first: boxes labeled with the entrepreneurial constructs (affordable-loss reasoning → venture survival), market uncertainty drawn as a moderator on the path — so a reviewer immediately sees the mechanism is effectual, not generic risk-taking.
Collapse the four tables into one descriptives-plus-correlations table (means, SDs, reliabilities on the diagonal) and one main results table that *leads with hazard ratios and confidence intervals*, with asterisks demoted to a footnote per APA.
Replace the buried interaction term with a **simple-slopes plot**: two survival curves, high vs. low uncertainty, making the contingency legible at a glance.
The result is fewer exhibits doing more work, each self-contained, and the mechanism visible to a reviewer in the first figure rather than reconstructed from a coefficient table.

## Output format

```text
【Journal】Entrepreneurship Theory and Practice
【Mechanism figure】present? entrepreneurial labels? Y/N
【Core exhibit suite】list matched to paper type
【Results table】leads with magnitude (effect size + CI)? Y/N
【Moderation】shown as simple-slopes plot? Y/N
【Qual exhibits】Gioia data structure + process model? (if applicable)
【APA + self-contained】titles/notes/abbrevs defined? Y/N
【Next skill】etp-writing-style
```
