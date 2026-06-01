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

## QE house rules for exhibits (verified 2026-06-01)

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

## Output format

```
【Significance reporting】asterisk/bold-free; SEs + coverage sets shown? [Y/N]
【Placement】figures/tables in-text on the relevant page? [Y/N]
【Headline quantity】lands first in the main table? [Y/N]
【Structural exhibits】targeted vs. untargeted moments + params w/ SEs? [Y/N or N/A]
【Final files】.eps/.jpg ready for LaTeX source? [Y/N]
【Next step】qe-writing-style
```
