---
name: jole-tables-figures
description: Use when designing tables and figures for a Journal of Labor Economics (JOLE) manuscript under the journal's word economy — each full-page table or figure counts as 500 words toward the ~20,000-word limit. Makes exhibits earn their space; it does not run the analysis.
---

# Tables & Figures (jole-tables-figures)

## When to trigger

- The main table has many columns and the paper is getting long
- You are unsure whether a result should be a table, a figure, or appendix-only
- Exhibits are pushing the manuscript toward or past the word limit
- Notes under tables/figures are not self-contained

## JOLE's exhibit economy (this is the distinctive constraint)

JOLE does **not normally publish articles exceeding 20,000 words, and it counts a full-page table or figure as 500 words** toward that total. That rule changes how you design exhibits: **every full page of tables/figures costs you 500 words of text.** A paper with ten full-page exhibits has spent 5,000 words before a single sentence. So the discipline is:

- **Promote only the headline exhibits to the body.** The 1–3 results that carry the paper become main tables/figures; everything else goes to the online appendix.
- **Consolidate.** Combine related specifications into one well-organized table rather than several; a tight panel beats five thin ones.
- **Prefer a figure when it carries the result more efficiently** (event-study plots, RDD discontinuity plots, binscatters, wage-profile and decomposition charts) — but remember a full-page figure still costs 500 words, so it must replace, not duplicate, text.
- **Self-contained notes.** Each exhibit's note states the sample, the estimator, the SE clustering, and the units, so a referee can read it without hunting through the text.

## Designing the main exhibits

1. **Lead exhibit = the result.** The single table or figure a labor referee should remember (e.g., the main treatment effect with its event-study, or the decomposition).
2. **Units and magnitudes visible.** Report effects in interpretable labor units (percent, percentage points, log points, dollars) with CIs.
3. **No chartjunk.** No 3D, minimal color, confidence bands shown; vector output (PDF/EPS) for print.
4. **Numbering and call-outs in order.** Every exhibit is referenced in the text in sequence.
5. **Budget the pages.** Tally how many full pages of exhibits you have and convert at 500 words/page; trim against the ~20,000-word cap.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JOLE is labor economics — the home of clean identification; DiD/IV/RDD and selection corrections are the binding constraint.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Only 1–3 headline exhibits in the body; the rest in the online appendix
- [ ] Full-page exhibits counted at **500 words each** against the ~20,000-word cap
- [ ] Related specifications consolidated, not scattered across many small tables
- [ ] Figures used where they carry the result more efficiently than prose
- [ ] Effects in interpretable labor units with confidence intervals
- [ ] Self-contained notes: sample, estimator, SE clustering, units
- [ ] Vector output; no chartjunk; exhibits numbered and called out in order

## Anti-patterns

- A 12-column kitchen-sink main table that eats the word budget
- Many thin tables where one consolidated panel would do
- A full-page figure that merely restates a paragraph (it still costs 500 words)
- Notes that force the referee back into the text to learn the sample or SEs
- Forgetting that exhibits count toward the length cap and overrunning it
- Effects reported as bare coefficients with no interpretable units

## Output format

```
【Headline exhibits】[1–3] in body, rest to appendix? [Y/N]
【Page budget】full pages of exhibits × 500 words = ___ ; within cap? [Y/N]
【Consolidation】related specs combined? [Y/N]
【Figure vs. table】each result in the more efficient form? [Y/N]
【Notes】self-contained (sample/estimator/SE/units)? [Y/N]
【Next step】jole-writing-style
```
