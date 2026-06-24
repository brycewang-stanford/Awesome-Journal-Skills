---
name: jf-tables-figures
description: Use when finalizing tables and figures for a The Journal of Finance (JF) manuscript for the AFA flagship. Enforces accessible, self-contained, general-interest exhibits with Roman-numeral tables, economic-magnitude reporting, and matching Internet Appendix numbering; it does not decide which results to run.
---

# Tables & Figures (jf-tables-figures)

## When to trigger

- Tables/figures are drafted but notes, units, or formatting are inconsistent
- A reader cannot interpret an exhibit without hunting through the text
- You are aligning main-text exhibits with Internet Appendix exhibits

## JF norm: self-contained, accessible exhibits

JF is general-interest and prizes accessibility. Each exhibit must be **self-contained**: a reader from another subfield should understand it from its caption and notes alone. Because the manuscript faces a **60-page limit** (≥1.5 spacing, 12-pt font), keep only **decisive** exhibits in the body and send the rest to the **Internet Appendix** (bundled at the end of the same PDF, labeled `IA.*`, not counted against 60 pages; see `jf-internet-appendix`).

## Exhibit standards

- **Numbering**: JF uses Roman numerals for tables (Table I, II, …) and Arabic for figures (Figure 1, 2, …); the Internet Appendix mirrors this as `IA.I`, `IA.1`. Keep the schemes consistent.
- **Notes state the inference**: sample, period, units, and the **standard-error/clustering convention** belong in every table note.
- **Economic units**: report magnitudes in interpretable units (bps, % of market cap, Sharpe gain), consistent with JF's general-interest voice.
- **No orphan exhibits**: every table/figure (body or IA) is referenced from the text.

## Checklist

- [ ] Each exhibit interpretable from caption + notes alone
- [ ] Table notes state sample, period, units, and SE/clustering
- [ ] Magnitudes in economic units, not just stars/t-stats
- [ ] JF numbering scheme (Table I…, Figure 1…) and matching `IA.*` in the appendix
- [ ] Only decisive exhibits in the body; rest in the Internet Appendix
- [ ] Body stays within 60 pages

## What a JF exhibit must carry (calibration anchors)

JF exhibits answer to a general-interest reader, so the table itself, not the surrounding prose, must deliver the economics. Useful calibration anchors for the flagship, hedged where conventions vary by subfield:

| Exhibit element            | JF expectation (illustrative anchor)                                  |
|----------------------------|------------------------------------------------------------------------|
| Body exhibit count         | Typically a lean set of decisive tables/figures; the exhaustive grid lives in the Internet Appendix |
| Magnitude column           | A column or note giving the effect in bps, % of market cap, or Sharpe gain — not stars alone |
| Inference convention       | Every table note names the SE estimator and clustering dimension(s)    |
| Numbering                  | Roman tables (I, II, …), Arabic figures (1, 2, …), IA mirrors as `IA.*` |
| Self-containment           | Caption + notes let an out-of-subfield AFA reader interpret the exhibit |

Exact body-exhibit counts are not a fixed rule; confirm against the journal's current author guidelines and recent issues, but the cultural signal at JF is "few, decisive, self-explaining in the body; everything else online."

## Worked vignette — formatting a momentum horse-race table

*Illustrative numbers.* A corporate-finance reader picks up a Table II reporting a long-short anomaly. The raw spread is 0.62% per month. The amateur version prints only coefficients and three stars. The JF-grade version, by contrast:

- Labels the row in **economic units** — "long–short return, % per month" — and adds a note: "55 bps after Fama–French five-factor + momentum adjustment (illustrative), annualized Sharpe gain ≈ 0.4."
- States inference in the note: "Newey–West (12 lags) t-statistics in parentheses; sample 1972–2023 (illustrative); NYSE breakpoints, value-weighted."
- Sends the equal-weighted, alternative-breakpoint, and decile-by-decile versions to the **Internet Appendix** as `IA.II`, `IA.III`, cited from the text.

The reader now understands the magnitude, the inference, and where to find more — without leaving the page. That self-containment is the JF house standard.

### Referee-pushback patterns and the JF-specific fix
| Pushback on an exhibit                              | JF-specific fix                                              |
|-----------------------------------------------------|-------------------------------------------------------------|
| "I can't tell what 0.62 means economically"         | Add a magnitude note (bps/month, Sharpe gain, % market cap) |
| "Which standard errors are these?"                  | Name the estimator and clustering in every table note       |
| "Table III and IA.3 use different definitions"      | Reconcile; keep one variable definition across body and IA  |
| "The body has fifteen tables"                       | Move all but the decisive ones to the Internet Appendix     |

## Execution bridge (StatsPAI / Stata MCP)

Generate the exhibit from the fitted result, don't transcribe numbers by hand (the
most common source of body-vs-IA inconsistency). Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Regression tables:** `etable` (multi-model columns) or `did_summary_to_latex` /
  `did_summary_to_markdown` straight from the `result_id` — one variable definition,
  one set of numbers, body and Internet Appendix in sync by construction.
- **Event-study / coefficient figures:** `plot_from_result`, `enhanced_event_study_plot`,
  `event_study_table` — emit the figure with axis units and the SE/clustering note baked in.
- **Every exhibit note** must name the estimator and clustering (pull it from the
  result's diagnostics) and state the **economic magnitude** in interpretable units —
  the JF self-containment standard, now machine-generated rather than retyped.

For a full chain producing JF-ready tables/figures from a fitted DiD result, see
[`resources/worked-examples/02-execution-walkthrough.md`](../../resources/worked-examples/02-execution-walkthrough.md).
If StatsPAI/Stata are not connected, format from the vendored `resources/code/` outputs.

## Anti-patterns

- A table whose meaning is unclear without three paragraphs of text
- Significance stars with no economic magnitude
- Missing SE/clustering convention in the note
- Body crowded with exhibits that belong in the Internet Appendix, breaching the 60-page limit
- Inconsistent numbering between body and appendix
- A figure with no axis units or a caption that assumes subfield-specific notation

## Output format

```
【All exhibits self-contained?】yes / no
【Notes state SE/clustering + units?】yes / no
【Magnitudes in economic units?】yes / no
【JF numbering consistent (Table I.. / IA.*)?】yes / no
【Decisive-only in body, ≤60 pp?】yes / no
【Next step】jf-writing-style
```
