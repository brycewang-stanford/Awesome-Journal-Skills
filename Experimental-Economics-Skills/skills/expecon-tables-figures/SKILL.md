---
name: expecon-tables-figures
description: Use when an Experimental Economics (ExpEcon) manuscript's exhibits must make the treatment contrast and its uncertainty visible at a glance. Builds design-carrying tables and figures; it does not run analysis or draft prose.
---

# Tables and Figures (expecon-tables-figures)

## When to trigger

- A reader cannot see the treatment effect from your main figure without reading the text
- Tables report regression coefficients but never show the raw treatment means and their spread
- Time/round dynamics (learning, convergence, decay) are hidden inside aggregate numbers
- Error bars, units, or the inference level on a plot are ambiguous or wrong

## The treatment-comparison figure is the paper's spine

At a method-defined journal, the central exhibit is almost always a **comparison across treatments**, and a referee should grasp the result from it alone. Design it to do three jobs.

1. **Show the contrast directly.** Plot the primary outcome by treatment — bars or dot-and-CI for means, but **prefer showing the distribution** (box/violin, or a CDF when distributions differ in shape, not just level). A CDF often reveals that a "no mean effect" masks a shift in the tails.
2. **Show uncertainty at the right level.** Error bars / CIs must reflect the **independent unit** (session/matching-group), not per-decision noise. State the level in the note. Mismatched error bars are an instant credibility hit at this journal.
3. **Show dynamics when the game is repeated.** A round-by-round line plot per treatment reveals learning, convergence to equilibrium, and end-game effects that an average conceals. Mark the period averaging window you use for tests.

## House conventions experimentalists expect

- **Raw behavior before models.** Lead with a figure of actual choices (e.g., contribution distributions), then a table of treatment means with group-level SEs, then regressions for adjustment/heterogeneity. Do not open with a regression table.
- **Report effect sizes, not just stars.** Give the treatment difference in **outcome units and as a fraction of the control mean / endowment** (e.g., "+3.2 tokens, 16% of endowment"), with a CI. Significance asterisks alone are weak evidence here; many ExpEcon papers report exact p-values and CIs.
- **A summary/design table.** Include a treatments table (conditions × what is manipulated × n sessions/groups/subjects) so a referee can audit the design and balance at a glance.
- **Self-contained notes.** Each exhibit names the outcome, the unit of observation, the inference level, the test used, n at each level, and the period window. A figure a referee must decode from the body is a figure that loses trust.
- **Color/encoding discipline.** Keep treatment colors consistent across every figure; ensure grayscale legibility; label axes in the subjects' units (ECU) with the money conversion noted once.

## Exhibit-by-exhibit plan for a typical paper

A clean ExpEcon results section usually runs a small, fixed set of exhibits — build them in this order:

| # | Exhibit | What it must show |
|---|---------|-------------------|
| 1 | Treatments/design table | conditions × manipulated dimension × n (sessions / groups / subjects) |
| 2 | Primary outcome by treatment | distribution (box/violin or CDF) + mean with group-level CI |
| 3 | Round-by-round dynamics (if repeated) | per-treatment trajectory; averaging window for tests marked |
| 4 | Primary test table | effect size in units + share of endowment + CI + exact p, at the right unit |
| 5 | Heterogeneity / mechanism | regression with covariates, clustered at session/group |
| 6 | Robustness panel | exclusions, learning halves, order, permutation test |

Resist the urge to add a seventh table of exploratory contrasts to the main text; push it to the appendix and label it exploratory.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Experimental Economics is lab/field experiments; randomization inference, `romano_wolf` for many treatments/outcomes, and power are decisive — observational tools secondary.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] One main figure shows the primary treatment contrast and is interpretable on its own
- [ ] Distributions (not just means) shown where shape matters; CDF used when relevant
- [ ] Error bars / CIs reflect the session/matching-group unit; the level is stated in the note
- [ ] Repeated games include a round-by-round dynamics plot with the averaging window marked
- [ ] Effect sizes reported in outcome units and as a share of endowment/control, with CIs
- [ ] A treatments/design table lists conditions, manipulation, and n at each level
- [ ] Every exhibit note is self-contained (outcome, unit, level, test, n, window)
- [ ] Exploratory contrasts are confined to the appendix and labeled

## Common scale and encoding traps

- **Truncated y-axes** that magnify a trivial treatment gap — start contribution/effort axes at the meaningful floor (often 0 or the endowment min), not at a level chosen to dramatize.
- **Pooling rounds silently** — if you average over rounds for a bar, the reader cannot see decay; pair it with the dynamics plot and state the window.
- **Inconsistent treatment colors** across figures, forcing the reader to re-learn the legend each time.
- **Over-plotted scatter** of individual decisions — bin, jitter, or show the density instead.
- **CIs that imply more precision than the design has** — at the matching-group unit, intervals are usually wider than per-decision intervals; show the honest ones.

Each of these is a small thing a referee notices instantly and reads as carelessness about the inference unit, which is the trait this journal least forgives.

## Anti-patterns

- A bar of means with no distribution, hiding that treatment shifts tails not the center
- Error bars computed on per-decision data when the unit is the group — overstated precision
- Opening with a dense regression table before the reader has seen the raw treatment behavior
- Stars-only reporting with no effect size, CI, or share-of-endowment context
- A repeated-game result with no dynamics plot, so learning/end-game effects are invisible
- Exhibit notes that omit the inference level or the rounds used for the test

## Worked vignette (illustrative)

A risk-elicitation paper reports only mean "number of safe choices" by treatment, with t-test stars — and finds nothing. Rebuilding as a **CDF of safe choices** reveals the treatment shifts the *upper tail* (more extreme risk-aversion) while the mean is flat. The new main figure shows the two CDFs diverging above the 7th choice; the test moves to a Kolmogorov–Smirnov / distributional comparison at the session level, and the effect is reported as "the 80th percentile rises by 1.5 safe choices (illustrative)." The story was in the distribution the mean hid.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-tables-figures
【Verdict】clear / rebuild
【Main contrast figure】outcome by treatment; distribution shown? CDF?
【Uncertainty】CI at session/group unit, stated in note? [Y/N]
【Dynamics】round-by-round plot for repeated game? window marked?
【Effect size】in units + share of endowment + CI
【Design table】conditions × manipulation × n present? [Y/N]
【Exploratory】confined to appendix and labeled? [Y/N]
【Next skill】expecon-writing-style
```
