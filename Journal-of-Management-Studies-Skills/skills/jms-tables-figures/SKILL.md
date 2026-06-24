---
name: jms-tables-figures
description: Use when exhibits are the bottleneck for a Journal of Management Studies (JMS) manuscript — regression/SEM tables and interaction plots for quantitative work, and data-structure, representative-quotes, and process-model figures for qualitative work. Builds and audits exhibits; it does not run the analysis (jms-data-analysis) or polish prose (jms-writing-style).
---

# Tables and Figures (jms-tables-figures)

## When to trigger

- A regression table is a wall of coefficients with no story or a model figure is missing
- A qualitative paper has rich quotes but no data-structure figure tying them to constructs
- A process model is described in prose but never drawn
- Tables count against the 10,000–13,000-word budget and need pruning
- A reviewer says "I can't follow how the data became the theory" or "the table doesn't answer the question"

## The JMS exhibit bar

JMS exhibits must **make the argument legible**, in whichever idiom. Two house facts shape them: the word count is **inclusive of tables, figures, and references**, so every exhibit must earn its space; and **tables are numbered with Roman numerals, figures with Arabic numerals** (verify against current author guidance — `检索于 2026-06；以官网为准`). Quantitative and qualitative papers need different exhibit sets — match the set to the design.

## Quantitative exhibit set

- **Descriptives + correlations** (one table): means, SDs, correlations, and reliabilities on the diagonal; flag any near-collinear pairs.
- **Measurement model**: CFA loadings / AVE / CR where SEM is used — reviewers check discriminant validity here.
- **Regression / SEM results**: build models hierarchically (controls → main → interactions); report unstandardised coefficients with SEs (and standardised where helpful), N, and fit. Make the *focal* coefficient visually findable.
- **Interaction plot**: any moderation hypothesis needs a plotted interaction with simple-slope annotation — a table alone does not convey form.
- **Theoretical model figure**: boxes-and-arrows mapping one-to-one to hypotheses.

## Qualitative exhibit set (first-class at JMS)

- **Data-structure figure** (Gioia convention): first-order codes → second-order themes → aggregate dimensions, shown as a single visual so a reader sees the abstraction ladder at a glance.
- **Representative-quotes table**: each second-order theme illustrated with verbatim quotes (attributed to anonymised informants), demonstrating evidentiary depth without dumping transcripts.
- **Process / theoretical model figure**: the dynamic relationships among aggregate dimensions, with arrows that carry mechanism (and time, for process work) — not a static box diagram.
- **Case / informant table**: cases, roles, data sources, and counts (interviews, hours, documents) so the evidentiary base is auditable.

## Self-sufficiency and house style

- Every exhibit reads on its own: a title that states what it shows, defined variables/constructs, units, N, and notes.
- Place exhibits to serve the argument; avoid duplicating the same numbers in text and table.
- Prefer one well-designed figure to three crowded tables — space is scarce under the inclusive word count.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMS mixes qualitative and quantitative management research; the chain below is for the quantitative-empirical lane.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Exhibit set matches the design (quant set vs. qual set)
- [ ] Quant: descriptives+correlations with reliabilities; hierarchical models with focal coefficient findable; every moderation plotted
- [ ] Qual: data-structure figure present; representative-quotes table; process/theoretical model figure; case/informant table with counts
- [ ] Theoretical/process model figure maps one-to-one to hypotheses/propositions
- [ ] Each exhibit is self-sufficient (title, defined terms, N, notes)
- [ ] Numbering follows house style (tables Roman, figures Arabic — verify)
- [ ] Exhibits earn their space under the inclusive word count; no redundant tables

## Anti-patterns

- **Coefficient wall**: a regression table with no hierarchy and no visually findable focal effect
- **Unplotted interaction**: a moderation hypothesis shown only as a product-term coefficient
- **Quotes without structure**: rich quotes with no data-structure figure linking them to constructs
- **Prose-only model**: a process/theoretical model described but never drawn
- **Transcript dump**: pages of raw quotes instead of a curated representative-quotes table
- **Redundancy**: the same statistics in both text and table, wasting the inclusive word budget

## Output format

```text
【Idiom】quantitative / qualitative
【Quant exhibits】descriptives+correlations · measurement model · hierarchical results · interaction plot · model figure
【Qual exhibits】data-structure figure · representative-quotes table · process model figure · case/informant table
【Model figure ↔ hypotheses/propositions】one-to-one? yes/no
【Space】fits inclusive word count? redundancies removed?
【Next step】jms-writing-style
```
