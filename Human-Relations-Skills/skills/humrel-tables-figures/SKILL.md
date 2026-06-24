---
name: humrel-tables-figures
description: Use when building and auditing the exhibits for a Human Relations (HR) manuscript — qualitative data-structure and evidence tables, process models, and quantitative tables/figures. Improves the exhibits; it does not change the analysis or theory.
---

# Tables & Figures (humrel-tables-figures)

## When to trigger

- Your exhibits exist but a reader cannot trace the inference from data to theory
- A qualitative paper has quotes scattered in prose but no data-structure or evidence table
- A process study has no figure showing the temporal/phase structure
- Quantitative tables are dense, asterisk-driven, or report numbers without interpretation
- You are checking exhibits for anonymization before a double-anonymous submission

## Exhibits must make the argument visible

At HR, exhibits are part of the *theoretical* apparatus, not an appendix of proof. The job differs by tradition, but the test is constant: each exhibit should let a reader *see the inference* that the prose claims.

## Qualitative & critical exhibits

- **Data-structure figure (the spine of a qualitative paper).** Show first-order codes → second-order themes → aggregate dimensions (Gioia) or the equivalent. This is often the single most scrutinized exhibit; build it from `humrel-data-analysis`.
- **Evidence / data-to-theory table.** Representative quotations mapped to constructs, so the data-to-theory link is auditable. Quotes here are *proof quotes*; reserve a few vivid *power quotes* for the body.
- **Process / phase model.** For process theory, a figure showing the sequence, events, and feedback over time — the visual argument of how the phenomenon unfolds.
- **Informant / site table.** Roles, counts, durations — establishing the evidentiary base without revealing identifying detail (anonymize site and organization names).

## Quantitative exhibits

- **Descriptives + correlations** with reliabilities on the diagonal where applicable.
- **Main models** in a clean regression table; **report standard errors / confidence intervals**, and do not let significance asterisks *be* the result — interpret magnitudes in the text.
- **Interactions plotted**, not left as raw coefficients; show simple slopes for moderation.
- **Multilevel results** labelled by level; variance components reported where theory is cross-level.

## House-style and submission constraints

- **SAGE Harvard (author-date)** governs in-text references and notes within exhibits (检索于 2026-06；以官网为准).
- The **13,000-word total cap** includes everything; bloated tables and a long appendix compete with the main text for that budget — every exhibit must earn its space.
- **Anonymize all exhibits** for double-anonymous review: no organization names, no identifying figures, no author-revealing acknowledgements in notes.
- Figures should be legible in greyscale and at the journal's column width.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Human Relations blends critical/qualitative and quantitative work; apply the chain below to its survey / experimental quantitative papers.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Qual: a data-structure figure shows codes → themes → dimensions
- [ ] Qual: an evidence table maps quotations to constructs (auditable inference)
- [ ] Process papers: a phase/temporal model figure is present
- [ ] Quant: SEs/CIs reported; magnitudes interpreted in text, not via asterisks alone
- [ ] Interactions are plotted; multilevel results labelled by level
- [ ] Every exhibit earns its place against the 13k word budget
- [ ] All exhibits anonymized (no site/organization/author tells)
- [ ] References within exhibits follow SAGE Harvard

## Anti-patterns

- A qualitative paper with no data-structure or evidence table (inference invisible)
- Quote-dumping in tables with no mapping to constructs
- Tables where significance asterisks substitute for substantive interpretation
- Process claims with no figure showing the temporal structure
- Exhibits that reveal the field site or author institution
- An appendix so large it crowds out the main argument under the word cap

## Output format

```text
【Journal】Human Relations
【Skill】humrel-tables-figures
【Qual exhibits】data structure / evidence table / process model status
【Quant exhibits】SEs-CIs reported; magnitudes interpreted (yes/no)
【Inference visible】can a reader trace data → theory? (yes/no)
【Anonymization】exhibits clean of site/author tells (yes/no)
【Budget】exhibits justified against 13k cap (yes/no)
【Next skill】humrel-writing-style
```
