---
name: jfi-tables-figures
description: Use when designing the exhibits for a Journal of Financial Intermediation (JFI) paper — banking-literate tables and figures with explicit sample construction, institution definitions, event timing, fixed-effect progressions that display demand absorption, and self-contained notes. It designs exhibits; it does not run the estimation.
---

# Tables & Figures (jfi-tables-figures)

## When to trigger

- Building or revising the table/figure set for a JFI submission
- A referee found the exhibits hard to read or under-documented

## What JFI exhibits must do

JFI exhibits are read by **banking and intermediation specialists**, so they must be self-contained and
institution-aware:

- **Summary / sample table first:** the bank/loan/firm universe, the data source (Call Reports, DealScan,
  HMDA, etc.), every filter, and units — readers must reconstruct the sample from the notes alone.
- **Define institutions and variables in the notes:** what counts as a "bank," how credit/balance-sheet
  quantities are measured, the treatment and its timing.
- **Main result table:** the headline specification with the FE structure visible, standard errors and the
  clustering level stated, and the mechanism estimate foregrounded.
- **Event-study / dynamics figure:** for DID designs, a pre-trend-and-effect plot is often the single most
  persuasive exhibit; show confidence bands and the reference period.
- **Robustness exhibits:** alternative samples, windows, and specifications, compactly tabulated.
- **Theory papers:** a clean figure of the mechanism or comparative statics, with parameters in the note.

## House conventions

Number exhibits and call them out in order; **numbered manuscript sections** (1, 1.1) host them. Notes
should name the estimator, sample, clustering, and significance markers. There is no fixed exhibit count,
but optional Highlights are capped at 3-5 bullets of 85 characters each.

## Worked exhibit plan: a capital-shock transmission paper (illustrative)

| # | Exhibit | The job it does for a JFI referee |
|---|---|---|
| T1 | Sample construction: register universe → multi-bank firms | Lets the reader reconstruct the sample and see what firm×time FE costs |
| T2 | Bank and firm summaries by exposure | Balance: treated and control banks comparable pre-shock |
| T3 | Main: loan growth on the shock; columns no FE → firm FE → firm×time FE | The supply channel, with demand absorption visible across columns |
| F1 | Event study around the rule change | Pre-trends plus dynamics — often the single decisive exhibit |
| T4 | Mechanism heterogeneity: relationship intensity, bank capital | Shows the intermediation channel, not generic credit tightening |
| T5 | Compact robustness grid, one row per named threat | The battery without appendix sprawl |
| F2 | Real effects: firm outcomes by exposure | The consequence panel that earns the policy sentence |

The fixed-effect **column progression in T3** is a JFI-native convention: the coefficient's movement
across columns is itself evidence on sorting and demand, so interpret it in the text. If T4's
heterogeneity is the contribution's heart, consider promoting it ahead of the robustness grid — exhibit
order should mirror the argument, not the order the regressions were run.

## Exhibit-count calibration (hedged)

Accepted empirical papers in this literature typically run on the order of six to nine main-text exhibits
with further robustness in an online appendix; theory papers often carry two to four comparative-statics
figures. These are reading-based calibrations — no cap is stated; confirm formatting specifics against
the journal's current author guidelines.

## Exhibit-level referee pushback, and fixes

- "I cannot tell which sample column 4 uses" → put N, sample, and FE rows in **every** column.
- "The event study has no reference period marked" → label the omitted period and shade the announcement.
- "The heterogeneity split shows no test" → report the interaction p-value, not two stars side by side.
- "The comparative-statics figure hides the friction" → for theory papers, plot the outcome against the
  friction parameter itself (monitoring cost, equity-issuance cost), with the no-friction benchmark as a
  dashed reference line, so the figure literally shows what intermediation adds.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A results table a reader cannot map to a sample or a clustering choice
- Star-soup with no economic-magnitude discussion
- A DID paper with no event-study/pre-trend figure
- Figures whose axes, units, or parameters are undefined

## Output format

```
【Sample table】source + filters + units documented? [Y/N]
【Main table】FE structure + clustering visible? [Y/N]
【Dynamics figure】event-study/comparative-statics present? [Y/N]
【Notes】self-contained (estimator, sample, SE)? [Y/N]
【Next skill】jfi-writing-style
```
