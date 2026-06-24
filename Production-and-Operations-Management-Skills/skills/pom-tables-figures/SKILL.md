---
name: pom-tables-figures
description: Use when designing the exhibits for a Production and Operations Management (POM) manuscript — result tables, comparative-statics and sensitivity plots, model schematics, empirical tables, simulation plots — and deciding what stays in the 32-page main paper vs. the online e-companion. Designs exhibits; it does not run the analysis (pom-data-analysis).
---

# Tables & Figures (pom-tables-figures)

## When to trigger

- Exhibits are cluttered, off house style, or not self-explanatory
- You are over the 32-page cap and must decide what moves to the e-companion
- A reviewer cannot follow the contribution from the table/figure sequence

## The POM exhibit budget: main paper vs. e-companion

POM's **32-page** limit *counts* tables, figures, appendices, and references (1.5 spacing, 11-pt). Treat exhibits as a scarce budget: only the displays that carry the core operational insight belong in the main paper; full proofs, large parameter grids, extended robustness, and supplementary tables go to the **unlimited online e-companion**. Number e-companion exhibits distinctly (e.g., EC.1, Table EC.2) and cross-reference them stably from the main text.

## Match the exhibit to the method track

- **Analytical/modeling:** a model schematic (decision timeline, information structure); a comparative-statics or sensitivity figure showing how the optimal policy moves with cost, lead time, or competition; a table of structural results. Lead with the *managerial* reading of the curve, not just its monotonicity.
- **Empirical OM:** a descriptive/summary table; the main results table with effect sizes and standard errors; robustness columns. Put units in decision-relevant terms (cost, fill rate, days).
- **Behavioral OM:** treatment-by-condition means with error bars; manipulation-check evidence.
- **Operations data science:** validation/performance tables plus a figure showing the **operational gain** (e.g., cost or service improvement from predict-then-optimize), not just accuracy.
- **Simulation:** plots with confidence intervals across sensitivity ranges.

## Make every exhibit decision-legible

- Title and note each exhibit with its **decision implication**, not only the statistical or mathematical object.
- State operational units explicitly.
- Ensure a Department Editor can grasp the contribution from the first one or two exhibits.
- Avoid duplicating main-paper content in appendices or the e-companion.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). POM spans analytical and empirical OM; apply the chain below to its empirical-OM papers, and note when a contribution is analytical / optimization.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Core insight exhibits in the main paper; depth in the e-companion
- [ ] Exhibits counted against the 32-page budget
- [ ] Operational units and decision implications labeled
- [ ] E-companion exhibits numbered (EC.*) and cross-referenced stably
- [ ] No duplication between main paper, appendix, and e-companion


## Exhibit pass for Production and Operations Management

Treat this skill as an executable review pass, not a prose hint. First lock the operational decision, the performance metric, and the implementable lever; then judge whether the current manuscript answers the venue's real reader: POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Exhibit】table / figure / schematic / appendix item
【Purpose】mechanism / result / robustness / implication / method detail
【Placement】main paper / e-companion (EC.*)
【Problem】readability / page budget / missing units
【Revision】specific design change
【Next step】pom-writing-style
```
