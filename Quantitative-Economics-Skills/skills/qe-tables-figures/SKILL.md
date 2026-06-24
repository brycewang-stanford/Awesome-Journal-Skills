---
name: qe-tables-figures
description: Use when building or auditing tables and figures for a Quantitative Economics (QE) manuscript so exhibits follow QE house rules — no significance asterisks or boldface, standard errors and coverage sets shown, figures/tables placed in-text, and final files as .eps/.jpg. Shapes exhibits; it does not redo the estimation.
---

# Tables & Figures (qe-tables-figures)

## When to trigger

- Tables still mark significance with asterisks or boldface (QE forbids this)
- Exhibits are dense and the key quantity is hard to find
- Figures/tables are collected at the end instead of placed in-text
- You are preparing final files and need the right formats and notes

## QE house rules for exhibits (source map refreshed 2026-06-20)

QE applies specific presentation rules that differ from most journals:

- **No asterisks, no boldface to denote statistical significance.** Instead, report **standard errors** and **confidence / coverage sets**. Let magnitude and uncertainty speak; do not encode significance with symbols.
- **Place figures and tables in-text on the relevant page**, not gathered at the end of the manuscript.
- **Final accepted files** are preferred as **LaTeX source with `.eps` / `.jpg` figures**; the submitted PDF embeds exhibits in-text.
- The manuscript is **1.5/double-spaced, ≥12pt, ≤32 lines per page** — design exhibits to remain legible under those constraints.

## Table craft

- Lead with the estimate(s) the paper is about; put the headline quantity where the eye lands first.
- Under each estimate, show its **standard error** (and a confidence/coverage set where the inference is non-standard, e.g., weak-IV or boundary parameters).
- Self-contained notes: estimand, sample, units, clustering level, estimator, and how uncertainty is computed — so the table stands alone.
- For structural work, separate **targeted moments** (data vs. model) from **untargeted moments** used for validation; report parameter estimates with standard errors.

## Figure craft (QE is quantitatively visual)

- Event-study plots with leads/lags and confidence bands; model-fit overlays (data vs. simulated moments); counterfactual curves with uncertainty bands.
- Show uncertainty visually (bands / intervals) rather than implying it with significance stars.
- Avoid chartjunk (no 3D, minimal color); vector output for print resolution.
- Caption states what the reader should conclude, with the key number in the text.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Quantitative Economics spans structural and applied micro; the chain serves its reduced-form lane, structural estimation uses its own toolkit.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] No asterisks or boldface for significance anywhere in tables or figures
- [ ] Every estimate shows a standard error; coverage/confidence sets where inference is non-standard
- [ ] Figures and tables placed in-text on the relevant page (not at the end)
- [ ] Notes are self-contained (estimand, sample, units, estimator, inference)
- [ ] Structural: targeted vs. untargeted moments shown; parameters with SEs
- [ ] Final files prepared as `.eps` / `.jpg` for the LaTeX source at acceptance
- [ ] Exhibits legible under 12pt / 1.5-spacing / ≤32-lines constraints

## Anti-patterns

- Marking significance with `***` / boldface (QE explicitly forbids this)
- A 9-column regression table with the key estimate buried
- Collecting all figures/tables at the end of the manuscript
- Figures with no uncertainty shown, leaning on stars in a companion table
- Notes that require the body text to interpret the exhibit

## Reading an exhibit the way a QE referee does

| What the referee looks for | Pass condition at QE |
|----------------------------|----------------------|
| significance encoding | no asterisks/boldface; SE under each estimate |
| non-standard inference | coverage/confidence set shown (weak-IV, boundary) |
| structural fit | targeted vs. untargeted moments separated |
| placement | exhibit on the page that discusses it, not at the end |
| self-containment | note carries estimand, sample, units, estimator, clustering |

## Worked vignette: rebuilding a structural-fit table (illustrative)

A draft reports a 6-column table marking three coefficients with asterisks and stacking all figures after the references. The QE rebuild: a moment-fit table with two blocks — *targeted* moments (data 0.31 vs. model 0.30; data 0.18 vs. model 0.19) and *untargeted* moments used as validation (data 0.44 vs. model 0.41) — and a parameter block showing each estimate with its standard error (e.g., risk aversion 1.8, s.e. 0.3). No stars anywhere; the event-study figure moves in-text beside its discussion with a 95% band on each lead and lag. (Numbers illustrative.) The reader now sees fit, parameters, and uncertainty without decoding symbols.

## Referee pushback and the exhibit fix

- *"Significance is encoded with stars — remove them."* → Replace with standard errors and, where inference is non-standard, a coverage set.
- *"I can't tell which moments are targeted."* → Split the table into targeted and untargeted blocks; label the validation moments.
- *"The figure hides its uncertainty."* → Add confidence bands to event-study and counterfactual curves; never imply significance via a companion star table.

## Output format

```
【Significance reporting】asterisk/bold-free; SEs + coverage sets shown? [Y/N]
【Placement】figures/tables in-text on the relevant page? [Y/N]
【Headline quantity】lands first in the main table? [Y/N]
【Structural exhibits】targeted vs. untargeted moments + params w/ SEs? [Y/N or N/A]
【Final files】.eps/.jpg ready for LaTeX source? [Y/N]
【Next step】qe-writing-style
```
