---
name: orgstud-tables-figures
description: Use when building the exhibits for an Organization Studies (OS) manuscript — data structures, process-model figures, evidence tables, and (for quantitative work) results tables. Designs exhibits that make the inference auditable; it does not run the analysis (see orgstud-data-analysis).
---

# Tables & Figures (orgstud-tables-figures)

## When to trigger

- Your qualitative paper has quotes scattered in prose but no data structure or evidence table
- Your process paper narrates events but has no process-model figure
- A reviewer cannot trace how your data became your constructs from the exhibits alone
- Quantitative tables are dense, asterisk-driven, or do not answer the theoretical question

## Exhibits carry the auditability of the inference

At OS, the exhibits are where reviewers **verify the data-to-theory inference**, not where decoration goes. For qualitative and process work especially, a few well-built exhibits do more than pages of prose: they let a skeptical reader see the analytic ladder at a glance. The exhibit set is part of the rigor argument, not an afterthought.

## The core qualitative/process exhibits

- **Data structure figure (Gioia-style).** First-order codes (informant terms) → second-order themes (researcher constructs) → aggregate dimensions. This is the single most expected exhibit in inductive OS papers; it makes the abstraction from data to theory visible in one image.
- **Data-to-theory / evidence table.** Rows = constructs or themes; columns = representative raw evidence (quotes, document excerpts), the code, and the construct. This is where "proof quotes" live, freeing the body for a few "power quotes."
- **Process-model figure.** Phases/stages with **explicit transition arrows and labels** — what triggers each move and what each phase accomplishes. A process model with unlabeled arrows is a common reviewer complaint; the figure must encode the mechanism, not just sequence boxes.
- **Case/site comparison table.** For multi-case designs (Eisenhardt idiom), a table contrasting cases on the dimensions that drive the theory.
- **Informant/data-source table.** Who, how many, when, role — establishing the empirical base.

## Quantitative exhibits

- **Descriptives + correlations** with clear units; **main results** in interpretable form.
- **Report effect magnitudes** and confidence intervals, interpreted in organizational terms — not significance stars as the headline.
- **Robustness** in a compact appendix table keyed to the specific theoretical threat each check addresses.
- Multilevel/interaction effects plotted (marginal-effects/interaction figures) rather than left to coefficients.

## Craft standards either way

- **Every exhibit answers a question** stated in its title/caption; if you cannot say what question it answers, cut it.
- **Self-contained.** Notes define abbreviations, units, sources, N; the reader should not need the body to parse the exhibit.
- **The figure encodes the argument.** A process figure should let a reader reconstruct the theory; a data structure should let them reconstruct the coding.
- **SAGE production.** Figures legible in greyscale and at print size; follow SAGE OS artwork specs at acceptance (检索于 2026-06；以官网为准).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Organization Studies is largely qualitative/theoretical; use the chain below only for its quantitative-empirical papers, and say so when a study is interpretive.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Inductive paper has a data structure figure (first-order → second-order → dimensions)
- [ ] A data-to-theory / evidence table makes the inference auditable; proof quotes live here
- [ ] Process paper has a process-model figure with *labeled* transitions, not bare boxes
- [ ] Informant/data-source table establishes the empirical base
- [ ] Quantitative: magnitudes/CIs interpreted; robustness keyed to theoretical threats
- [ ] Every exhibit answers a stated question and is self-contained (notes, units, N)
- [ ] Figures legible in greyscale / at print size per SAGE specs

## Anti-patterns

- An inductive OS paper with no data structure figure — reviewers expect it
- A process figure of unlabeled boxes and arrows that encodes sequence but not mechanism
- Quotes scattered in prose with no evidence table to corroborate them
- Significance asterisks presented as the result instead of interpreted magnitudes
- Exhibits the body must explain because their captions/notes are incomplete
- Decorative figures that answer no question (cut them)

## Worked vignette: rescuing a flat process figure (illustrative)

A process paper submitted a figure of four boxes — "Onset → Escalation → Resolution → Stabilization" — joined by plain arrows. A reviewer wrote: "This is a timeline, not a process model; I cannot see the mechanism." The fix was not a prettier figure but a more *theoretical* one: each arrow was labeled with the **trigger** that drives the transition (e.g., "a breach makes the prior frame untenable") and each phase annotated with **what it accomplishes that the prior could not** (e.g., "Escalation surfaces the latent logic conflict"). The redrawn figure now encodes the generative logic, so a reader can reconstruct the theory from the image alone — which is exactly what an OS process exhibit must do.

## Output format

```text
【Exhibit set】data structure / evidence table / process model / case table / results
【Auditability】can a reader trace data → constructs from exhibits alone? (Y/N)
【Process figure】transitions labeled with triggers + what each phase does? (Y/N/NA)
【Quant】magnitudes + CIs interpreted; robustness keyed to threats? (Y/N/NA)
【Self-containment】captions/notes complete (units, N, sources)? (Y/N)
【Next skill】orgstud-writing-style
```
