---
name: eer-tables-figures
description: Use when building or revising exhibits for a European Economic Review (EER) manuscript so they report standard errors, read cleanly, and follow Elsevier economics norms. Designs tables and figures; it does not run the estimation or write the surrounding prose.
---

# Tables & Figures (eer-tables-figures)

## When to trigger

- Tables are dense, over-decorated with significance stars, or missing SEs
- Figures are cluttered, lack uncertainty bands, or are not self-explanatory
- A referee said an exhibit is "unreadable" or "buries the result"
- Preparing final editable source files for Elsevier production

## The EER exhibits bar

EER follows **Elsevier economics house style**: a paper is read through its **main tables and a few clean figures**, each **self-contained** (legible without the text). The discipline norm is to **report standard errors** (and, increasingly, confidence intervals) and to **let the magnitude carry the result** rather than a wall of asterisks. Figures and tables can be embedded for review and are supplied as **editable source files** at final stage. Aim for **fewer, sharper exhibits**: the headline result should be findable in one table and one figure.

## Table design rules

- **One headline table** carries the main result; supporting tables are secondary.
- **Report SEs** (in parentheses) under every coefficient; report N, R²/pseudo-R², and the FE/cluster structure in the notes.
- **Magnitudes legible**: scale coefficients to interpretable units; add a sentence-ready effect size.
- **Significance**: report SEs/CIs; if stars are used, do not let them *replace* the SE or the magnitude — EER norms emphasize the standard error, not the star.
- **Notes are complete**: sample, period, clustering level, estimator, and what each column varies.
- **No redundant digits**: 2–3 significant figures; align decimals.

## Figure design rules

- **Event-study plots** with leads/lags and **confidence bands** are the EER-standard causal exhibit.
- **Model-fit overlays** (data vs. model moments) for quantitative/structural work.
- **Counterfactual / policy curves** with uncertainty bands.
- **Self-contained captions**: a reader should grasp the figure from the caption alone.
- **Vector output** (`.eps`/`.pdf`) or high-resolution `.tif/.jpg`; legible fonts; colorblind-safe palettes; avoid chartjunk and 3-D effects.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). EER is a general economics field journal; the DiD/IV/RDD chain serves its applied lane.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] One headline table; the main result is findable there
- [ ] Standard errors (and/or CIs) under every estimate; N and structure in notes
- [ ] Stars (if any) do not substitute for SEs/magnitudes
- [ ] Coefficients in interpretable units with a stated effect size
- [ ] Event-study/causal figure has leads/lags + confidence bands
- [ ] Every exhibit is self-contained (caption + notes legible alone)
- [ ] Final figures supplied as editable/vector source at acceptance
- [ ] No chartjunk; colorblind-safe; 2–3 significant figures

## Anti-patterns

- A table whose only signal is the number of asterisks (no SEs, no magnitude)
- Twelve nearly-identical regression columns where two would do
- Figures with no uncertainty bands or no axis labels
- Captions that require the body text to interpret the exhibit
- Raster screenshots of tables instead of editable source
- Reporting six decimal places of false precision
- Color encodings that fail in grayscale or for colorblind readers
- An appendix figure carrying the headline result the main text never shows

## Worked vignette (illustrative)

A labor paper's first draft has a 10-column table dense with stars and no SEs. The EER revision: one headline table (4 columns: baseline, +controls, modern DiD, IV) with SEs in parentheses, clustering noted, and effect sizes spelled out ("a 1 SD increase raises wages 2.3%, s.e. 0.6"); plus one event-study figure with flat leads and a shaded 95% band. The remaining specifications move to the Supplementary material. The result is now findable in ten seconds.

## Output format

```
【Headline table】columns + what each varies; SEs present? [Y/N]
【Reporting】SEs/CIs under estimates; stars not load-bearing? [Y/N]
【Key figure】event-study / fit-overlay / counterfactual + uncertainty bands? [Y/N]
【Self-contained】captions+notes legible alone? [Y/N]
【Final files】editable/vector source ready? [Y/N]
【Next step】eer-writing-style (weave exhibits into the narrative)
```
