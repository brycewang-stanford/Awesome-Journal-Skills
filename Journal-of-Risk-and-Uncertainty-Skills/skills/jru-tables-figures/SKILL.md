---
name: jru-tables-figures
description: Use when exhibits for a Journal of Risk and Uncertainty (JRU) manuscript must make choice patterns and risk-parameter estimates legible. Improves tables and figures for a risk/uncertainty audience; it does not invent evidence or citations.
---

# Tables and Figures (jru-tables-figures)

## When to trigger

- Choice data are buried in a wall of cells when a figure could show the *pattern* (the fourfold pattern, an Allais reversal, an Ellsberg gap)
- A structural table lists parameters with no sense of which moment or task identifies them
- A probability-weighting function or value function is described in prose instead of plotted
- Standard errors, confidence intervals, or the estimation method behind each parameter are missing or inconsistent

## What JRU exhibits must do

JRU audiences read for **decision-theoretic content**: they want to see the shape of the weighting function, the location of the reference point, the size of the ambiguity premium, and how precisely each parameter is pinned down. The exhibit's job is to make the *behavioral pattern* and the *parameter estimate* immediately legible, with honest uncertainty.

### Figures — the workhorses of this field

- **Plot the estimated functions, not just their parameters.** A Prelec or Tversky–Kahneman w(p) and a reference-dependent value function are far more informative drawn than tabulated; overlay the EU benchmark (the 45° line for w(p)) so the deviation is visible.
- **Show the choice pattern directly** where it is the point: certainty-equivalent curves, switching-point distributions in a price list, the fourfold pattern of risk attitudes, the Ellsberg matching-probability gap.
- **Confidence bands, not just point curves** — show estimation uncertainty around the fitted function.
- For experiments, a **CONSORT-style flow** (recruited → completed → analyzed) and a balance summary belong up front.

### Tables — discipline

- Each structural parameter row should make clear **what identifies it** (which task/moment) and report a standard error or CI and the estimation method.
- Report **standard errors / confidence intervals** as the primary inferential object; do not let asterisks substitute for showing precision and magnitude.
- Separate **structural parameters** (curvature, weighting, ambiguity index, λ) from **nuisance / control** estimates so the reader's eye lands on the primitives.
- Units and stakes stated (lab currency vs. real money, per-period vs. lifetime) so a VSL or premium is interpretable.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JRU spans decision experiments and applied risk; randomization inference for experiments, DiD/IV for observational claims.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The probability-weighting / value function (or ambiguity premium) is **plotted**, with the EU benchmark overlaid
- [ ] Confidence bands accompany any fitted function or key estimate
- [ ] Each structural parameter shows its identifying task/moment, an SE/CI, and the estimation method
- [ ] The headline behavioral pattern (fourfold / Allais / Ellsberg) is shown, not just described
- [ ] Experiment exhibits include sample flow and balance
- [ ] Magnitudes are interpretable: stakes, units, and currency stated
- [ ] Precision is shown via SE/CI rather than asterisks alone

## Reading the exhibit as a referee would

Before finalizing, look at each exhibit cold and ask the questions a JRU referee asks:

- Can I see the **deviation from EU** without reading the text? (If the w(p) plot has no 45° line, no.)
- Can I tell **how precise** each estimate is? (If only stars, no.)
- Can I tell **what identifies** each parameter? (If the table has no identifying-task column, no.)
- Can I convert the magnitude to something **interpretable** — dollars, an elasticity, a probability? (If units are "points," no.)

An exhibit that fails any of these sends the referee back to the prose to reconstruct what the figure should have shown — friction that costs goodwill in review.

## Anti-patterns

- A table of CPT parameters with no plot of the resulting curves
- Reporting risk/ambiguity parameters with significance stars but no standard errors or magnitude
- Mixing structural primitives and control coefficients in one undifferentiated column
- A figure of w(p) with no EU 45° reference, so the reader cannot judge the deviation
- Lab results in unspecified "points" that cannot be mapped to money or to a real-stakes claim

## The exhibit each archetype needs

| Paper archetype | The one exhibit that carries it |
|-----------------|-------------------------------|
| CPT / RDU estimation | plotted w(p) and value function with confidence bands vs. the EU benchmark |
| Ambiguity (α-MEU / smooth) | the ambiguity premium (or matching-probability gap) by treatment, with CIs |
| Risk-attitude elicitation | distribution of switching points / certainty equivalents, not just a mean |
| VSL / hedonic-wage | the wage–risk gradient with its CI, and the estimate against the meta-analytic range |
| Insurance demand | takeup vs. price/loss with the demand curve and elasticity annotated |

## Caption and note discipline

- The note states the **estimation method**, the **inference** (clustering / bootstrap), and the **sample** so the table is self-contained.
- Define every symbol used in the table (α, λ, γ, δ) in the note or a shared notation box; do not assume the reader carries the model in their head.
- If a parameter is reported in lab currency, give the conversion to money in the note so the magnitude is interpretable.

## Worked vignette (illustrative)

A paper estimates cumulative prospect theory and reports α (utility curvature), λ (loss aversion), and the Prelec γ, δ in a dense table. The JRU revision adds one figure: the fitted w(p) with a confidence band against the 45° EU line, showing the characteristic inverse-S, and a second panel with the value function showing the kink at the reference point. The table is then trimmed to the structural primitives with SEs and a column naming the task that identifies each — controls move to the appendix, and the note states the MSM objective, subject-level clustering, and the currency conversion.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-tables-figures
【Verdict】clear / redraw / re-tabulate
【Key function plotted】w(p) / value function / ambiguity premium [Y/N]
【Benchmark overlaid】EU 45° / risk-neutral [Y/N]
【Precision shown】SE/CI not stars [Y/N]
【Identifying task per parameter】[Y/N]
【Source status】verified / 待核实 / not asserted
【Next skill】jru-writing-style
```
