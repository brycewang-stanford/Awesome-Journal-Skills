---
name: jpam-tables-figures
description: Use when building tables and figures for a Journal of Policy Analysis and Management (JPAM) manuscript — self-contained, decision-legible exhibits that show the policy effect, its uncertainty, the design's validity, and cost-benefit / distributional results. Designs exhibits; it does not run the estimation.
---

# Tables & Figures (jpam-tables-figures)

JPAM exhibits serve a mixed audience — economists, political scientists, public-management scholars, and
practitioners — so they must be **self-contained and decision-legible**: a policymaker should grasp the
main result, its uncertainty, and who it affects without reading the methods section. Lead with the
exhibit that shows the policy effect and its credibility, not a wall of coefficients.

## When to trigger

- Designing the main results table/figure and the design-validity exhibits
- A reviewer found tables unreadable, or the key result hard to locate
- Presenting cost-benefit or distributional results visually
- Preparing exhibits for the (double-blind) submission

## What the exhibit set should contain

1. **The headline effect, clearly.** A main results table or a coefficient/effect figure in policy-
   relevant units, with confidence intervals — not just significance stars.
2. **Design-validity exhibits.** The evidence that the identification holds: an **event-study /
   pre-trends** plot for DiD, an **RD plot** with binned means and the fitted discontinuity, a balance
   table for an RCT, a synthetic-control fit plot. These often persuade reviewers more than the point
   estimate.
3. **Heterogeneity / mechanism.** A figure showing effects by the theory-driven subgroups.
4. **Cost-benefit / distributional.** Where central, an exhibit that shows the benefit-cost result and
   its sensitivity, or the distribution of gains and costs across groups.

## Craft standards

- **Self-contained captions:** define the sample, the estimator, the units, the inference (what the
  error bars/SEs are and the clustering), and the time window — readable without the text.
- **Confidence intervals over stars** in figures; report SEs and the clustering level in tables.
- **Policy-relevant units** on axes and in cells (dollars, percentage points, per-recipient).
- **Accessible design:** colorblind-safe palettes, legible in grayscale, vector output for print.
- **Honest scaling:** do not truncate axes to exaggerate an effect; show the zero line where relevant.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPAM is policy analysis — program evaluation is the core; DiD/IV/RDD and the policy-relevant magnitude are decisive.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Main effect in policy-relevant units with CIs, locatable at a glance
- [ ] A design-validity exhibit (event-study / RD plot / balance / SC fit) included
- [ ] Heterogeneity exhibit matches the pre-specified subgroups
- [ ] Cost-benefit / distributional result shown where it is central
- [ ] Captions self-contained: sample, estimator, units, inference, window
- [ ] Colorblind-safe, grayscale-legible, vector format
- [ ] Every exhibit number/value matches the deposited replication output

## Anti-patterns

- A dense regression table with stars and no confidence intervals or units
- Hiding the parallel-trends / RD-validity evidence in an appendix the reviewer must hunt for
- Captions that require the methods section to interpret
- Truncated or rescaled axes that overstate the effect
- A cost-benefit conclusion in prose only, with no exhibit or sensitivity shown
- Exhibits whose numbers drift from the replication package

## Calibration anchors (hedged)

- For a DiD or RD paper, the **design-validity figure often does more persuasive work than the point
  estimate** — a clean pre-trends or RD plot pre-empts the cross-disciplinary referee's first objection.
- A mixed APPAM audience reads exhibits before prose; if the headline effect and its uncertainty are not
  legible from the figure alone, the paper feels harder than it is.
- Confidence intervals communicate policy precision better than stars — a wide CI is itself information a
  decision-maker needs.

## Worked micro-example (illustrative)

For a staggered-adoption DiD, the strong exhibit set is: (1) an **event-study figure** with confidence
bands showing flat pre-trends and the post-policy effect; (2) a **main table** reporting the
heterogeneity-robust estimate in dollars with the clustering level named; (3) a **subgroup figure** for
the pre-specified populations; and (4) a **benefit-cost panel** with sensitivity bars. A reviewer can
verify the identification, read the magnitude, and see the policy bottom line without leaving the
figures. (Illustrative.)

## Output format

```
【Headline exhibit】main effect + CI in policy units
【Design-validity exhibit】event-study / RD / balance / SC fit
【Heterogeneity / mechanism】subgroup figure
【Cost-benefit / distribution】exhibit + sensitivity (if central)
【Accessibility】colorblind-safe, grayscale, vector? [Y/N]
【Next】jpam-writing-style
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — event-study and RD plotting templates
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — figure tooling (coefplot, ggplot2, marginaleffects)
