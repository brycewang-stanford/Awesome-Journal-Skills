---
name: aejmac-tables-figures
description: Use when building or revising exhibits for an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript — impulse-response figures, fan charts, model-fit overlays, and regression/moment tables — to AEA house standards and macro conventions. Formatting and clarity; it does not generate the underlying estimates.
---

# Tables & Figures (aejmac-tables-figures)

## When to trigger

- IRF figures lack confidence bands, units, or a clear horizon axis
- Tables are dense, mislabeled, or report coefficients without the macro quantity of interest
- A model-fit comparison (data vs. simulated moments) is asserted in text but not shown
- Exhibits do not stand alone — the reader needs the body text to decode them

## The AEJ: Macro exhibits bar

AEJ: Macro follows **AEA house style** (applied by the AEA at copyediting; the submitted PDF need not pre-conform, but clean exhibits speed review). Macro adds its own conventions: the **impulse-response function** is the workhorse figure, and the **headline quantity** (multiplier, peak response, welfare cost, share of variance) must be readable off the exhibit. Every exhibit should be **self-contained**: title, axis labels with units and horizon, sample, and the inference object (bands / SE) in the note.

## Figure conventions (macro-specific)

- **IRFs**: plot the response with a **shaded confidence band** (state the level, e.g., 68% and/or 90%); label the horizon axis in the natural unit (quarters/months/years); mark zero; if sign-restricted, show the **identified set / median-target**, not a spurious point.
- **Fan charts / forecast bands**: show the full predictive distribution where the claim is about uncertainty.
- **Model-fit overlays**: plot **data vs. model** (targeted and untargeted moments) on the same axes; this is the credibility figure for quantitative work.
- **Counterfactual figures**: baseline vs. counterfactual paths with uncertainty carried through.
- **Variance decompositions / contribution plots**: stacked or grouped, with a clear legend.
- Vector output (`.eps`/`.pdf`) preferred for final files; keep colors legible in grayscale; no chartjunk.

## Table conventions

- Report the **economic quantity**, not just raw coefficients — e.g., the multiplier, the elasticity, the implied share — with its SE/band.
- AEA tables conventionally use **significance stars**; AEJ: Macro accepts them, but the **standard error / band must be present** and must carry the inference (do not let stars substitute for a reported SE). Note significance levels in the table note.
- One decisive number per row; align decimals; units in the column header or note.
- Targeted-vs-untargeted-moment tables: clearly flag which moments were matched.
- Notes carry: sample, frequency, estimator, inference (HAC/cluster), and what an asterisk means.

## Main text vs. online appendix

- Main text: the **decisive** IRFs, the headline table, the model-fit figure. AEJ: Macro articles run ~40 pages including exhibits (检索于 2026-06；以官网为准), so exhibits compete for space.
- Online appendix: full robustness IRFs, additional moments, alternative specifications, derivations.

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
## Checklist

- [ ] Every IRF has a confidence band with its level stated, a labeled horizon axis, and a zero line
- [ ] Sign-restricted responses shown as a set/median-target, not a fake point estimate
- [ ] Model-fit figure (data vs. model, targeted + untargeted) present for quantitative papers
- [ ] Tables report the macro quantity with its SE/band; notes give sample/estimator/inference
- [ ] Significance stars (if used) accompany, not replace, reported SEs
- [ ] Each exhibit is self-contained (decodable without the body text)
- [ ] Decisive exhibits in main text; the rest in the online appendix; figures vector + grayscale-legible

## Anti-patterns

- IRFs with no confidence bands, or bands whose level is never stated
- Sign-restricted IRFs drawn as a single line, hiding set-identification
- Tables of raw VAR coefficients with no impulse responses or implied quantity
- Stars reported but standard errors omitted
- A model "matches the data" claimed in prose with no overlay figure
- Exhibits readable only with a magnifying glass after the AEA's two-column typesetting

## Output format

```
【Exhibit inventory】IRFs / fan charts / model-fit / counterfactual / tables
【IRF compliance】bands+level / horizon axis / zero line / set-vs-point? [Y/N]
【Quantity legibility】headline number readable off each exhibit? [Y/N]
【Table compliance】SE/band present; notes complete; stars don't replace SEs? [Y/N]
【Main vs. appendix split】decisive in text, rest in online appendix? [Y/N]
【Next step】aejmac-writing-style
```
