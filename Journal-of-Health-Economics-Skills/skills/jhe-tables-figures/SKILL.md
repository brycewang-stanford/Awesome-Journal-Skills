---
name: jhe-tables-figures
description: Use when building or revising the exhibits of a Journal of Health Economics (JHE) manuscript so the health-policy result is legible at a glance and the institutional/identification logic is visible. Formats exhibits; it does not establish the result (jhe-identification / jhe-robustness) or write prose.
---

# Tables and Figures (jhe-tables-figures)

## When to trigger

- The main result is settled and must be readable at a glance to a health economist
- Tables are dense, over-decimaled, or bury the headline policy effect
- An event-study / RD / first-stage plot needs to carry the identification visually
- The descriptive picture of the health setting (utilization, spending distribution, coverage) is missing or buried

## The JHE exhibit bar

At JHE the **main health-policy estimate should be findable in seconds**, and the exhibits should let a health economist judge both the *magnitude* and the *institutional plausibility* of the result. Elsevier/JHE house style permits significance stars, but **standard errors in parentheses are the load-bearing object** and clustering must be stated. Two exhibit duties are specific to this journal: (1) a **descriptive/institutional exhibit** that shows the health setting — the coverage gap, the spending distribution (it is skewed — show it), the policy timeline — so readers trust the variation; and (2) the **identification figure** (event-study leads, RD continuity, first stage) that makes the design visible before the table.

| Exhibit | What it must show | Common failure |
|---------|-------------------|----------------|
| Main results table | headline effect, SE in parentheses, N, clustering, dependent-var mean | too many columns; SEs missing; over-precision |
| Descriptive/institutional table | sample, coverage/utilization baseline, policy timing | generic summary stats with no health-system detail |
| Spending-distribution figure | skew, zero mass, where the effect sits in the distribution | mean-only reporting that hides the skew |
| Event-study figure | leads + lags, CIs, reference period, flat pre-trends | no CIs; ambiguous reference period |
| RD figure | binned scatter + local-linear fit, bandwidth, density panel | overfit global polynomial; no density |
| Heterogeneity exhibit | effects by clinically/policy-relevant subgroup with MHT | a starred subgroup fishing wall |

## Exhibit craft

1. **One table for the headline.** The preferred specification — effect, SE in parentheses, N, dependent-var mean, clustering level — should be readable without flipping pages; demote the controls sweep to the online appendix.
2. **Show the distribution, not just the mean.** Health spending and utilization are right-skewed and zero-heavy; a distribution figure or quantile effects tell the policy story a mean hides.
3. **Make the setting legible.** A descriptive exhibit naming the program, eligibility, and timing earns referee trust that the variation is what you say it is.
4. **Figures carry identification.** Event-study leads, RD continuity, and the first stage are more convincing as clean vector figures than as prose.
5. **Right precision and self-contained notes.** Two to three significant figures; each note states sample, units, clustering, controls, outcome definition, and (if used) what a star means.
6. **Name the outcome in plain terms.** "Any inpatient admission (0/1)" beats an opaque variable label; a health-policy reader should know exactly what was measured from the exhibit alone.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHE is health economics — insurance/program reforms and selection; foreground DiD/IV/RDD and selection corrections.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline effect readable in one table: coefficient, SE in parentheses, N, dep-var mean, clustering stated
- [ ] A descriptive/institutional exhibit makes the health setting and policy timing concrete
- [ ] Skewed/zero-inflated outcomes shown as a distribution, not only a mean
- [ ] Identification figure present (event-study with CIs / RD with density / first stage)
- [ ] Heterogeneity reported by policy-relevant subgroup with MHT, not subgroup fishing
- [ ] Notes self-contained (sample, units, clustering, outcome definition, controls)
- [ ] Figures clean vector output; precision 2–3 sig figs; no redundant exhibits
- [ ] Outcome variables named in plain terms; magnitudes shown against a base rate

## Anti-patterns

- A summary-statistics table with no health-system detail, so the variation looks generic
- A 12-column results table where the policy effect is buried in column 9
- Reporting stars or t-stats but omitting standard errors / clustering level
- Mean-only reporting that hides the skew and zero mass in spending/utilization
- An event-study with no confidence intervals or an unclear reference period
- An RD figure with a high-order global polynomial manufacturing a jump
- A heterogeneity wall of starred subgroups with no MHT and no clinical/policy logic
- An exhibit whose magnitude has no base rate, so the reader cannot judge whether it is large

## Referee pushback mapped to the exhibit fix

- *"I cannot find your main estimate."* → One headline table with the effect, SE, N, clustering, and dep-var mean; the controls sweep demoted to the appendix.
- *"Where are the standard errors and what is the clustering?"* → SEs in parentheses everywhere; clustering level (usually state) and any star meaning stated in the self-contained note.
- *"Your mean effect hides what happened in the tail."* → Add a distribution or quantile-effect figure; health spending lives in the right tail, and the mean can understate or mask the policy story.
- *"This RD jump looks like a polynomial artifact."* → Replace the global high-order fit with a local-linear binned scatter plus a density panel.
- *"I cannot tell whether your variation is credible."* → Add the descriptive/institutional exhibit: eligibility, payment rule, and policy timing, so the design is plausible before the table.

## Worked vignette (illustrative)

A coverage paper's Table 4 sweeps every control combination across 12 columns; the headline take-up effect hides in column 9 with only t-stats. The JHE fix: promote the preferred specification to a two-panel Table 2 (Panel A: effect 4.1pp, s.e. 1.0 in parentheses, N, dep-var mean, clustered on state; Panel B: with full controls), move the sweep to the online appendix, and add Figure 1 — the event-study with CIs and a marked reference period. Add Figure 2 showing the spending distribution shift, since the mean effect understates the policy story in the right tail. The result and its design are now legible in seconds.

## Magnitudes a health-policy reader can act on

A JHE exhibit is persuasive when the reader can translate the number into a policy statement. Always give the **base rate** alongside the effect (a 4.1pp coverage gain reads differently against a 62% baseline than a 20% one), report **dollar magnitudes** for spending in current units, and reserve **QALY/mortality** language for effects you actually estimated. For heterogeneity, organize by the subgroup a regulator cares about (income band, age-eligibility, chronic-condition status), not by whatever split happens to be significant. The exhibit should let a policymaker read off "who was affected and by how much" without the prose.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-tables-figures
【Headline exhibit】one table carrying the policy effect? [Y/N]
【Inference shown】SEs in parentheses + clustering level in notes? [Y/N]; stars defined if used
【Setting exhibit】descriptive/institutional + distribution shown? [Y/N]
【Identification figure】event-study / RD / first stage with CIs? [Y/N]
【Heterogeneity】policy-relevant subgroups with MHT? [Y/N]
【Next skill】jhe-writing-style
```

## Handoff boundary

This skill makes a settled result legible; it does not establish the result (`jhe-identification` / `jhe-robustness`) or write the surrounding argument (`jhe-writing-style`). Do not polish exhibits while the estimate is still moving — that is wasted effort and it tempts presentation choices that flatter an unstable number. When the headline and identification figures are clean and self-contained, hand off to `jhe-writing-style`.
