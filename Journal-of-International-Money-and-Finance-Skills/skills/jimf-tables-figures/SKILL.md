---
name: jimf-tables-figures
description: Use when building or revising the exhibits of a Journal of International Money and Finance (JIMF) manuscript so the international result is legible and respects Elsevier/finance presentation norms. Formats exhibits; it does not establish the result (jimf-identification / jimf-robustness) or write the prose.
---

# Tables & Figures (jimf-tables-figures)

## When to trigger

- The main result is settled and must be readable at a glance
- A cross-country panel table is wide and dense; the headline coefficient is hard to find
- An event-study / impulse-response / local-projection plot must carry the identification visually
- Country-level heterogeneity (AE vs. EM, by region) needs a map, scatter, or panel of plots
- You are preparing exhibits for an Elsevier submission and want them house-style clean

## The JIMF exhibit bar

JIMF is an empirical finance/macro journal, so the **headline international effect should be findable in seconds** and the *picture of the identification* should appear before the reader reaches the table. Finance house style (unlike the Econometric Society journals) **permits significance stars but requires standard errors** in parentheses and self-contained notes. The distinctive JIMF exhibits are the cross-country panel regression table, the high-frequency event-study / impulse-response figure, and the country-heterogeneity display.

| Exhibit | What it must show | Common failure |
|---------|-------------------|----------------|
| Main panel-regression table | headline coefficient, SE in parentheses, FE indicated (country/time), N, R², dep-var | 12 columns; FE structure unclear; no dep-var mean |
| Event-study / surprise figure | response over the window, CIs, the announcement at t=0, pre-window flat | no CIs; ambiguous window; overlapping events |
| Impulse response / local projection | horizon on x-axis, CI bands, units stated (bp, %) | no bands; units unstated; truncated horizon |
| Country heterogeneity | by-country or by-region coefficients (forest plot / map / scatter vs. exposure) | a pooled coefficient hiding huge dispersion |
| Pass-through table | pass-through by horizon and by invoicing/currency margin | aggregate-only; horizon collapsed |
| Robustness display | point-estimate stability across checks (coefficient plot / spec curve) | a starred wall with no through-line |

## Exhibit craft for international finance

1. **One table for the headline.** The preferred specification should let a referee read the coefficient, its SE, the fixed-effect structure (country / time / two-way), N, and the dependent-variable mean without flipping pages. Demote the control sweep to the appendix.
2. **Make the fixed effects and clustering legible.** In a cross-country panel the FE structure *is* the identification; show "Country FE: Yes / Time FE: Yes" rows and state the clustering level in the note.
3. **Figures carry the identification.** Event-study windows, impulse responses, and pre-trend leads persuade more as figures with CI bands than as prose; mark t=0 and the window; state units (basis points vs. percent).
4. **Show heterogeneity, don't hide it.** When AE and EM differ, a forest plot of country/region coefficients or a scatter against ex-ante exposure is worth more than a pooled number.
5. **Right precision and units.** Two to three significant figures; state whether the exchange-rate effect is per 1% or per 1 s.d., per 25bp surprise, etc.
6. **Self-contained notes.** Sample, country set, period, frequency, FE, clustering, and star meaning all in the note.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIMF is international macro-finance; cross-country panels + asset pricing — identification plus factor/Newey-West inference.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline coefficient readable in one table: estimate, SE in parentheses, FE rows, N, dep-var mean
- [ ] Fixed-effect structure and clustering level stated explicitly (the identification, made visible)
- [ ] Identification figure present (event-study / IRF / local projection) with CI bands and a marked t=0/window
- [ ] Country/region heterogeneity displayed where it exists (forest plot / scatter vs. exposure / map)
- [ ] Units and the per-unit scaling stated (per 1%, per 1 s.d., per 25bp)
- [ ] Stars (if used) defined; SEs reported everywhere; precision 2–3 sig figs
- [ ] The underlying estimate is settled (identification + robustness) before the exhibit is polished
- [ ] Control sweep demoted to the appendix; the body carries only the preferred specification
- [ ] Event-study / IRF figures follow the canonical form (marked t=0, CI bands, normalized shock)
- [ ] Dollar vs. exchange-rate effect distinguishable from the exhibits (USD and NEER shown where relevant)
- [ ] Every exhibit note is self-contained (sample, period, frequency, FE, clustering)

## Anti-patterns

- A main panel table with a dozen columns where the headline coefficient is buried mid-table
- An event-study or impulse-response figure with no confidence bands or an unmarked event date
- A single pooled coefficient when the country dispersion is the actual story
- Reporting t-stats or stars but omitting standard errors or the clustering level
- Failing to state the FE structure, so a reader cannot tell within-country from cross-country variation
- Exhibit notes that send the reader back to the text to learn the country set or the period

## Where exhibits end and the result begins

This skill formats and arranges; it does not establish the estimate. If the headline coefficient is still moving, fix that in `jimf-identification` and `jimf-robustness` before polishing the exhibit — a beautifully typeset table of an unstable number is wasted effort. The right sequence is: settle identification, stabilize the estimate across robustness checks, then promote the preferred specification to the headline table and build the identification figure around it. Exhibits are the last empirical step before writing, not a substitute for the analysis.

## Worked vignette (illustrative)

A draft's Table 5 sweeps every control combination across 14 columns, and the spillover coefficient sits in column 11 with only t-stats. The JIMF fix: promote the preferred specification to a two-panel Table 2 — Panel A the baseline (coefficient 0.42, s.e. 0.13 in parentheses, Country FE Yes, Time FE Yes, N, two-way clustered), Panel B with openness interaction — and move the sweep to the online appendix. Add Figure 1, the local-projection impulse response of EM bond spreads to the cleaned US surprise with 90% bands over a 20-day horizon, and Figure 2, a forest plot of the by-country coefficients against capital-account openness. The international effect is now visible before the table.

## Figure conventions JIMF readers expect

Several JIMF exhibits have near-canonical forms; matching them signals fluency. A **high-frequency event study** plots the cumulative response across a tight window with the announcement at t=0 and CI bands, and states whether the window is intraday or daily. A **local-projection impulse response** puts horizon on the x-axis, the response (in stated units) on the y-axis, and shaded confidence bands, with the shock normalized (per 25bp, per 1 s.d.). A **country-heterogeneity forest plot** shows each country/region coefficient with its CI, ordered by an interpretable covariate (openness, EM vs. AE), so dispersion and its correlate are visible at once. A **pass-through table** reports the cumulative coefficient at several horizons, ideally split by invoicing-currency margin. Use these forms unless you have a reason not to.

## Referee pushback mapped to the exhibit fix

- *"I cannot find your main international effect."* → One headline table with the coefficient, SE, FE rows, N, and dep-var mean; the control sweep demoted to the appendix.
- *"Your event-study window/event is ambiguous."* → Mark t=0, state the window length and frequency, and add CI bands.
- *"A pooled coefficient hides huge country dispersion."* → Add a forest plot of by-country estimates against the relevant exposure covariate.
- *"Is this a dollar effect or an exchange-rate effect?"* → Report the result in both USD and NEER columns so the reader can see which.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-tables-figures
【Headline exhibit】one table carrying the estimate + FE rows + SE? [Y/N]
【FE / clustering visible】country/time FE rows + clustering in note? [Y/N]
【Identification figure】event-study / IRF / LP with CI bands + marked t=0? [Y/N]
【Heterogeneity shown】forest plot / scatter vs. exposure / map? [Y/N]
【Units / scaling】per 1% / 1 s.d. / 25bp stated? [Y/N]
【Next skill】jimf-internet-appendix
```
