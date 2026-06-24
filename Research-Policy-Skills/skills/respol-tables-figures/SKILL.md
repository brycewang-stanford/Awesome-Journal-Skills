---
name: respol-tables-figures
description: Use when exhibits are the bottleneck for a Research Policy (RP) manuscript — designing tables and figures (regression tables, patent/bibliometric maps, event-study plots, case data structures) that carry the innovation mechanism for an interdisciplinary readership. Builds exhibits; it does not run the analysis (respol-data-analysis) or write prose (respol-writing-style).
---

# Tables and Figures (respol-tables-figures)

## When to trigger

- The key result is buried in a wall-of-coefficients table no reader can parse
- A bibliometric/patent map or network is decorative — pretty but uninterpretable
- An event-study or dose-response plot is missing where the design demands one
- A qualitative paper has no data-structure table linking evidence to constructs
- A referee says exhibits "don't answer the question" or descriptive stats are missing/opaque

## The Research Policy exhibits bar

RP exhibits serve an **interdisciplinary** readership, so they must be self-explanatory to an economist, a management scholar, and a policymaker alike. Each exhibit should answer one question and visibly support the contribution; the headline result deserves a focused exhibit, not a dump of every specification. Innovation data also carry specific exhibit conventions: descriptive statistics that reveal the **skew and zeros** typical of patent/citation data, transparent variable definitions, and maps/networks that are *interpreted*, not merely displayed.

## Designing the core exhibits

### Regression / estimation tables
- Lead with a table that isolates the headline innovation effect; relegate the full specification grid to robustness.
- Report coefficients with standard errors and the relevant model statistics; state the estimator, sample, fixed effects, and clustering in the notes so the table stands alone.
- For count models, report incidence-rate ratios or marginal effects where they aid interpretation — a raw NB coefficient is opaque to many RP readers.
- Provide a descriptive-statistics and correlation table that shows the distribution (means, SDs, and the share of zeros for count variables).

### Patent / bibliometric exhibits
- Co-occurrence/citation networks and technology maps must have an interpretive payoff: annotate clusters, state the layout algorithm and the tie definition, and tell the reader what to see.
- Time-series of patenting/diffusion should mark policy dates or structural breaks relevant to the claim.

### Causal-design plots
- Event-study plots with leads/lags and confidence bands for DID; first-stage and reduced-form plots for IV; RD plots with binned means and the fitted discontinuity.

### Qualitative exhibits
- A data-structure table (1st-order codes → 2nd-order themes → aggregate dimensions) and a representative-quotes table that ties evidence to each construct.

## General craft

- Every exhibit has a number, a self-contained title, complete notes (source, sample, units), and is referenced and *interpreted* in the text.
- Units and variable definitions are explicit; do not assume the reader knows your patent indicator.
- Figures should be legible in greyscale and at print size; avoid chartjunk and uninterpreted color.
- Place exhibits to follow the argument's logic; the appendix holds robustness, not load-bearing results.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Research Policy is innovation studies — patent/firm panels with selection; foreground identification and the selection objection.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] A focused exhibit isolates the headline innovation effect
- [ ] Descriptive stats reveal skew/zeros in patent/citation variables
- [ ] Count-model results are reported in interpretable units (IRR / marginal effects) where helpful
- [ ] Patent/bibliometric maps are annotated and interpreted, not decorative
- [ ] Design-required plots (event study / first stage / RD) are present
- [ ] Qualitative data-structure and quotes tables link evidence to constructs
- [ ] Each exhibit stands alone (title + notes: source, sample, estimator, clustering)
- [ ] Every exhibit is interpreted in the text, not just cited

## Anti-patterns

- A single mega-table where the headline result is one column among twenty
- A network/map shown without telling the reader what to conclude from it
- Raw negative-binomial coefficients with no interpretive translation
- Descriptive tables that hide the zero-inflation of innovation counts
- Color-dependent figures that fail in greyscale
- A qualitative paper with quotes scattered in prose but no data-structure table

## Output format

```text
【Journal】Research Policy
【Skill】respol-tables-figures
【Headline exhibit】what it isolates and how it supports the contribution
【Descriptives】skew/zeros of innovation variables shown? [Y/N]
【Interpretation】count units / map annotation / design plots present? [Y/N]
【Stand-alone notes】source, sample, estimator, clustering in each note? [Y/N]
【Qualitative】data-structure + quotes table? [Y/N / NA]
【Verdict】pass / revise / reroute
【Next skill】respol-writing-style
```
