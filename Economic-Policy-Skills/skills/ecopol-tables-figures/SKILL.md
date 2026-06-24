---
name: ecopol-tables-figures
description: Use when an Economic Policy (EP) manuscript's exhibits are too technical for a policy reader or do not carry the policy message. Redesigns tables and figures for the EP dual audience; it does not invent evidence or citations.
---

# Tables and Figures (ecopol-tables-figures)

## When to trigger

- A minister or central-bank reader could not extract the policy takeaway from your main exhibit
- Tables are dense regression dumps with every coefficient and three sets of stars
- The key magnitude is buried in a coefficient cell rather than shown as a headline effect
- Figures lack the context (units, baseline, policy threshold) a non-economist needs
- You are choosing which exhibits go in the accessible main text vs. the technical appendix

## EP exhibits serve two readers — design for the harder one

EP is read by economists **and** policymakers, and presented to two discussants. The main-text exhibits must be legible to the policy reader; the regression machinery belongs in the appendix. The governing principle: **lead with figures that show the policy effect, demote dense tables to the appendix.** A good EP figure answers the policy question by itself — an event-study plot of the reform's effect over time, a map of treated regions, a bar of the welfare/cost decomposition — with a caption a non-specialist can read standalone.

Note on house style: EP applies its template and copyediting at the commissioning/production stage, and authors receive style guidance on commissioning (检索于 2026-06；以官网为准). All figures should carry **alternative text (alt text)** for accessibility (检索于 2026-06；以官网为准). Confirm exact figure-format and table-style rules in the live author guidelines.

## Main-text vs. appendix split

| Exhibit | Where it belongs |
|---------|------------------|
| Headline policy effect (event study, treatment effect over time) | main-text figure |
| Magnitude in policy-meaningful units (€, jobs, % of GDP) | main-text figure/table |
| Welfare / fiscal-cost decomposition | main-text figure |
| Full regression table with all controls and specifications | appendix |
| Robustness grid across specifications | compact summary in main text; full grid in appendix |
| Balance / first-stage / density diagnostics | appendix |

## Craft moves for the policy reader

- **Translate units.** Show effects as €, jobs, percentage-points of GDP, or per-capita — not just a standardized coefficient. The policymaker thinks in outcomes, not z-scores.
- **Put the baseline in the figure.** An effect of "−0.08" is meaningless without "relative to a baseline of 0.40." Annotate it.
- **One message per figure.** If a figure makes two points, split it. Caption states the single takeaway.
- **Drop significance asterisks from the headline story.** Show the point estimate and a visible confidence interval; let the policy reader see precision directly rather than decoding stars.
- **Mark the policy object on the plot** — the reform date, the eligibility threshold, the counterfactual path — so the design is visible.
- **Tables: only the coefficients that matter** in the main text; full controls in the appendix.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Economic Policy is policy-facing applied economics; foreground a credible design and a policy-relevant magnitude.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] At least one main-text figure that conveys the policy effect standalone
- [ ] Effects shown in policy-meaningful units, with the baseline annotated
- [ ] Confidence intervals visible; headline message not asterisk-dependent
- [ ] Policy object (reform date / threshold / counterfactual) marked on relevant figures
- [ ] Dense regression tables and diagnostics moved to the appendix
- [ ] Each figure has a standalone, non-technical caption (and alt text per accessibility policy — 待核实 on exact spec)
- [ ] One message per exhibit; no two-point figures

## Anti-patterns

- A main-text table of 20 coefficients × 6 columns that no policymaker will read
- Reporting effects only as standardized/log coefficients with no real-world units
- Three tiers of significance stars carrying the headline instead of a shown CI
- Figures with no baseline, no units, and no marked policy event
- Leaving the single most policy-relevant exhibit in the appendix while the main text shows diagnostics

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-tables-figures
【Headline figure】does it convey the policy effect standalone? Y/N
【Units】effect expressed in € / jobs / %GDP / per-capita?
【Baseline + policy object】annotated on figure? Y/N
【Precision】CI shown (not asterisk-driven)? Y/N
【Main-text vs appendix】what moved to appendix
【Accessibility】alt text / format per guidelines (待核实 exact spec)
【Next skill】ecopol-writing-style
```
