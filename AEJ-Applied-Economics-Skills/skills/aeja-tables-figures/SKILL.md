---
name: aeja-tables-figures
description: Use when building or revising the exhibits of an American Economic Journal: Applied Economics (AEJ: Applied) manuscript so the main causal result is legible in one table or figure and respects AEA house presentation norms. Formats exhibits; it does not establish the result (aeja-identification / aeja-robustness) or write the surrounding prose.
---

# Tables & Figures (aeja-tables-figures)

## When to trigger

- The main result is settled and must be made readable at a glance
- Tables are dense, over-decimaled, or bury the headline coefficient
- An event-study / RD / first-stage plot needs to carry the identification visually
- You are preparing exhibits for submission and want them AEA-house-style compliant

## The AEJ: Applied exhibit bar

At AEJ: Applied the **main causal estimate should be findable in seconds** and every exhibit should earn its place. AEA house style permits **significance stars but expects standard errors** in parentheses, clear notes that make each exhibit self-contained, and clean figures over chartjunk. Lead with the design's signature visual — the event-study plot, the RD scatter, or the balance table — because at this journal the *picture of the identification* is half the persuasion.

| Exhibit | What it must show | Common failure |
|---------|-------------------|----------------|
| Main results table | headline coefficient, SE in parentheses, N, controls indicated, dependent-var mean | too many columns; no SEs; over-precision |
| Balance table (RCT) | baseline means by arm, differences, joint test | missing joint test; no attrition row |
| Event-study figure | leads + lags, CIs, reference period, flat pre-trends visible | no CIs; ambiguous reference period |
| RD figure | binned scatter + fitted lines, bandwidth, density | overfit polynomial; no density panel |
| First-stage / IV table | first-stage F, exclusion logic in notes | weak first stage hidden |
| Robustness exhibit | point-estimate stability across checks | a starred wall with no map |

## Exhibit craft

1. **One table for the headline.** Table 1 (or 2) should let a referee read the main causal estimate, its SE, and N without flipping pages.
2. **Standard errors always, stars optional.** AEA permits stars, but SEs in parentheses are the load-bearing object; report the dependent-variable mean so magnitudes are interpretable.
3. **Self-contained notes.** Each exhibit's note states sample, units, clustering level, controls, and what an asterisk (if used) means — a referee should not need the text to read the table.
4. **Figures carry identification.** Event-study leads, RD continuity, and balance are more convincing as figures than as prose; make them publication-clean (vector output, readable fonts, CIs shown).
5. **Right precision.** Two to three significant figures; do not report coefficients to five decimals.

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

- [ ] Main causal estimate readable in one table: coefficient, SE in parentheses, N, dep-var mean, controls flagged
- [ ] Standard errors reported everywhere; clustering level stated in notes; stars (if used) defined
- [ ] Identification figure present (event-study with CIs / RD with density / balance with joint test)
- [ ] Notes make every exhibit self-contained (sample, units, clustering, controls)
- [ ] Figures are clean vector output, legible, no chartjunk, consistent scales
- [ ] Precision sensible (2–3 sig figs); no redundant exhibits

## Anti-patterns

- A main results table with 12 columns where the headline coefficient is hard to find
- Reporting stars or t-stats but omitting standard errors / clustering level
- Over-precision (coefficients to 5 decimals) implying false accuracy
- An event-study plot with no confidence intervals or unclear reference period
- An RD figure with a high-order global polynomial that manufactures a jump
- Exhibit notes that force the reader back to the text to interpret the table

## Worked vignette (illustrative)

A draft's Table 4 has 12 columns sweeping every control combination, and the headline coefficient is buried
in column 9 with only t-statistics shown. The AEJ: Applied fix: promote the preferred specification to a
two-panel Table 2 — Panel A the main estimate (coefficient 3.1, s.e. 0.9 in parentheses, N, dependent-var
mean 0.44), Panel B the same with the full controls — and move the sweep to the online appendix. Add Figure 1,
the event-study with confidence intervals and a clearly marked reference period, so the identification is
visible before the reader reaches the table. The result is now findable in seconds.

## Referee pushback mapped to the exhibit fix

- *"I cannot find your main estimate."* → One headline table with the coefficient, SE, N, and dep-var mean;
  everything else demoted to the appendix.
- *"Where are the standard errors / what is the clustering?"* → SEs in parentheses everywhere; clustering
  level and (if used) star meaning stated in the self-contained note.
- *"This RD jump looks like an artifact of the polynomial."* → Replace the global high-order fit with a
  local-linear binned scatter plus a density panel.

## Output format

```
【Headline exhibit】one table/figure carrying the main estimate? [Y/N]
【Inference shown】SEs in parentheses + clustering level in notes? [Y/N]; stars defined if used
【Identification figure】event-study / RD / balance present with CIs? [Y/N]
【Self-contained notes】sample/units/clustering/controls in every note? [Y/N]
【Figure quality】vector, legible, no chartjunk? [Y/N]
【Next step】aeja-writing-style
```
