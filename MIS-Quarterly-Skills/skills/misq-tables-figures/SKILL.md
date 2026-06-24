---
name: misq-tables-figures
description: Use when designing the exhibits for a MIS Quarterly manuscript — measurement/correlation and structural-model tables for behavioral IS, regression and robustness tables for economics-of-IS, artifact architecture and evaluation exhibits for design science, and a Gioia-style data structure for qualitative work — all sized to fit MISQ's page limit, which counts tables and figures. Late-stage polish; do not run before the contribution and evaluation are settled.
---

# Tables & Figures (misq-tables-figures)

## When to trigger

- Exhibits are cluttered, off-style, or not self-explanatory
- Tables and figures are eating the page budget (the limit counts them)
- A reviewer cannot reconstruct your model, identification, or artifact from the exhibits
- You are at the polish stage with a settled contribution

## Every exhibit costs page budget

Unlike journals that exclude exhibits from the limit, MISQ page limits **count text, tables, figures, references, and appendices together**, and supplementary materials are discouraged. So each exhibit must earn its space: consolidate, remove decorative figures, and keep only what carries the argument. Plan the exhibit set against the category budget (e.g., 50 pp for a Research Article).

## Choose exhibits by tradition

| Tradition | Core exhibits |
|-----------|---------------|
| **Behavioral** | Construct correlation table (reliabilities on the diagonal), measurement-model table (loadings, AVE, CR), structural-model figure with path coefficients, simple-slopes plot for moderation |
| **Economics of IS** | Descriptives/balance table, main regression table, robustness table, an event-study/parallel-trends figure |
| **Design science** | Artifact architecture/process figure, design-principles-to-requirements table, evaluation table (artifact vs. baselines), ablation table |
| **Organizational / qualitative** | Gioia-style data structure (first-order codes → second-order themes → aggregate dimensions), a process model figure, a table of representative quotations |

## Make each exhibit self-contained

A reviewer should understand a table or figure without hunting through the text: complete titles, defined variables/constructs, units, sample size, and notes for estimator, SE clustering, and significance. For design-science evaluation tables, name the baselines and the metric. Follow the MISQ Style Guide for table/figure presentation and APA 7th conventions.

## Figures that carry the contribution

- A clean structural/path model or theoretical-model figure for behavioral/organizational papers.
- An event-study/coefficient plot for economics-of-IS identification.
- An architecture or build-and-evaluate cycle diagram for design science.
Avoid 3-D effects, chartjunk, and figures that merely restate a table.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). MISQ is empirical IS — surveys, econometric panels, experiments, and design science; the chain below serves the causal / econometric lane, while design-science artifacts use their own evaluation standards.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Exhibit set fits the category page budget (tables/figures count)
- [ ] Each table/figure is self-explanatory with full notes
- [ ] Behavioral: correlation/measurement tables and a structural-model figure included
- [ ] Economics: main + robustness tables and an identification figure
- [ ] Design science: architecture figure, design-principles table, evaluation/ablation tables
- [ ] Qualitative: a Gioia-style data structure exhibit
- [ ] APA 7 / MISQ Style Guide formatting

## Anti-patterns

- Padding the manuscript with figures that restate tables — wasting scarce page budget.
- Tables with undefined variables or missing SE/clustering notes.
- A design-science evaluation table with no baseline column.
- Beautifying exhibits before the model, identification, or evaluation is final.


## Exhibit pass for MIS Quarterly

Use this as a second-pass capability check. First lock the IS phenomenon, artifact/platform, theory mechanism, design or empirical warrant, and managerial implication; then test whether the manuscript addresses information-systems reviewers who expect strong IS theory, digital artifact or platform grounding, and evidence with organizational consequence.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Information Systems Research for quantitative IS, Journal of Management Information Systems for applied systems, Management Science for broader OR/MS; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Exhibit set】tables + figures, by tradition
【Page-budget impact】fits / trim N exhibits
【Self-contained?】notes/baselines/units present
【Style】APA 7 / MISQ Style Guide compliant
【Next step】misq-writing-style
```
