---
name: finman-tables-figures
description: Use when building or revising the exhibits of a Financial Management (FM) manuscript so the main finance result and its economic magnitude are legible at a glance and respect Wiley/finance house norms. Formats exhibits; it does not establish the result (finman-identification / finman-robustness) or write the surrounding prose.
---

# Tables & Figures (finman-tables-figures)

## When to trigger

- The main result is settled and must be made readable at a glance
- Tables are dense, over-decimaled, or bury the headline coefficient among a dozen columns
- An event-study / first-stage / portfolio-sort plot needs to carry the design visually
- You are preparing exhibits for the FMA→ScholarOne submission and want them house-style clean

## The FM exhibit bar

FM's brand is "articles that people actually read," and that taste extends to the tables. The main causal or economic estimate should be **findable in seconds**, and — because FM weighs **practical relevance** — every headline exhibit should make the **economic magnitude** legible, not just the t-statistic. Finance house style permits **significance stars but requires standard errors** in parentheses; report the **dependent-variable mean** so a reader can scale the coefficient into a managerial quantity. The journal's "less weight on trivial robustness" stance also shapes the exhibit set: do not pad the main paper with specification-sweep tables — promote the one headline table and the one identification figure, and demote the rest.

| Exhibit | What it must show | Common failure |
|---------|-------------------|----------------|
| Summary stats / Table 1 | sample, key variable means, SDs, N | no attrition or sample line |
| Main results table | headline coefficient, SE in parentheses, N, dep-var mean, controls flagged | 12 columns; magnitude not interpretable |
| Event-study figure | leads + lags, CIs, reference period, flat pre-trends | no CIs; ambiguous reference period |
| First-stage / IV table | first-stage F, exclusion logic in notes | weak first stage hidden in an appendix |
| Portfolio sort / factor table (AP) | spreads, factor-adjusted alphas, t-stats, costs | gross-only returns; no factor adjustment |
| Economic-magnitude exhibit | effect scaled to SD, dollars, or a managerial unit | only statistical significance reported |

## Exhibit craft

1. **One table for the headline.** A referee should read the main estimate, its SE, N, and dependent-variable mean without flipping pages.
2. **Standard errors always; stars optional.** SEs in parentheses are load-bearing; state the clustering level in the note; if stars are used, define them.
3. **Make the magnitude speak.** Add a one-line economic-significance statement or column — a one-SD change in X moves Y by Z percentage points / dollars — so the practical relevance FM prizes is visible.
4. **Figures carry the design.** Event-study leads and first-stage relationships persuade better as clean vector figures with CIs than as prose.
5. **Right precision and a lean set.** Two to three significant figures; keep the main paper to the exhibits that earn their place and push sweeps to the internet appendix.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Financial Management is empirical corporate finance + asset pricing; corporate-causal chain (DiD/IV/RDD) plus the factor-zoo haircut for cross-sectional pricing.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Main estimate readable in one table: coefficient, SE in parentheses, N, dep-var mean, controls flagged
- [ ] Standard errors reported everywhere; clustering level in notes; stars (if used) defined
- [ ] An economic-magnitude statement accompanies the headline result
- [ ] Identification figure present (event-study with CIs / first-stage / sorts) where relevant
- [ ] Notes make each exhibit self-contained (sample, units, clustering, controls, period)
- [ ] Precision sensible (2–3 sig figs); specification sweeps demoted to the internet appendix

## Making the magnitude speak (FM's signature exhibit move)

Because FM weights practical relevance, the single highest-return exhibit edit is making the economic size legible. Three reliable ways:

1. **A dedicated economic-significance column or panel** — alongside the coefficient, report the effect of a one-SD change in the regressor as a percentage of the dependent-variable mean.
2. **A managerial-unit translation in the note** — convert the coefficient into basis points, dollars per firm, or percentage of payout, so a CFO or investor reads the size directly.
3. **A back-of-envelope aggregate** — where credible, scale the per-firm effect to a portfolio or market total, with the assumptions stated.
A table that reports only t-statistics asks the referee to do this work; FM referees often will not, and "is this big enough to matter?" becomes the rejection.

## Anti-patterns

- A main table with 12 columns where the headline coefficient is buried
- Reporting t-stats or stars but omitting standard errors / the clustering level
- Statistical significance with no economic-magnitude translation — fails FM's relevance taste
- Over-precision (coefficients to 5 decimals) implying false accuracy
- An event-study plot with no confidence intervals or an unclear reference period
- Cramming robustness sweeps into the main paper instead of the internet appendix
- A figure that re-states a table without adding visual intuition (chartjunk that earns nothing)

## Worked vignette (illustrative)

A draft's Table 4 sweeps every control combination across 12 columns, the headline is in column 9 with only t-stats, and nothing tells a reader the size of the effect. The FM fix: promote the preferred specification to a two-panel Table 3 (Panel A baseline, Panel B full controls), each with the coefficient 3.1 (s.e. 0.9 in parentheses), N, and the dependent-variable mean 0.44; add a one-line note that a one-SD rise in the regressor implies a ~7% increase relative to the mean (illustrative); move the sweep to the internet appendix; and add Figure 1, the event-study with CIs and a marked reference period. The result is now findable, identified, and economically legible.

## Referee pushback mapped to the exhibit fix

- *"I cannot find your main estimate."* → One headline table with the coefficient, SE, N, and dep-var mean; everything else demoted.
- *"Where are the standard errors / the clustering?"* → SEs in parentheses everywhere; clustering in the self-contained note.
- *"Is the effect economically meaningful?"* → Add the economic-significance column or a managerial-unit translation.
- *"This figure adds nothing."* → Make the figure carry the identification (event-study leads, first stage), not re-plot a table.

## Wiley production notes (verify before final upload)

A few presentation details are set by the publisher rather than the field, and they save a copyediting round if handled early:

- **Figure resolution and format** must meet Wiley's print specs; export figures as vector (PDF/EPS) where possible. (Exact specs 待核实 on the author guidelines.)
- **Table layout** should survive single-column print without truncation; very wide tables get reformatted or pushed to landscape.
- **Colors** that distinguish series in a figure should also be distinguishable in grayscale, since print and many readers are monochrome.
- **Self-contained notes** are not just good craft here; they are what the copyeditor relies on to typeset the exhibit correctly.

## Output format

```
【Headline exhibit】one table carrying the main estimate? [Y/N]
【Inference shown】SEs in parentheses + clustering in notes? [Y/N]; stars defined if used
【Economic magnitude】effect scaled to a managerial/market unit? [Y/N]
【Identification figure】event-study / first-stage / sorts present with CIs? [Y/N]
【Self-contained notes】sample/units/clustering/controls/period in every note? [Y/N]
【Lean set】sweeps demoted to internet appendix? [Y/N]
【Next skill】finman-internet-appendix
```
