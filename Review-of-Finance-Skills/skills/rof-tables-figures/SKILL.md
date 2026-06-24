---
name: rof-tables-figures
description: Use when designing Review of Finance tables and figures under the 60-page total cap, including empirical-finance exhibits, theory figures, robustness tables, data-description tables, and replication-friendly notes.
---

# Review of Finance Tables And Figures

Use this when exhibits are too dense, under-explained, or wasting the 60-page budget. At RoF
exhibits are not free space: the hard 60-page cap explicitly counts appendices, bibliography,
figures, and tables, so every exhibit must earn its place and be self-contained for a
top-three-standard referee.

## When to trigger

- The main table has too many columns and buries the headline result.
- Figures lack confidence bands, units, or self-contained notes.
- The manuscript is near or over 60 pages and exhibits are part of why.

## Exhibit rules

- Lead with one clean headline exhibit a reader grasps in seconds; keep the main paper focused
  on exhibits that carry the finance contribution or address likely top-three-standard
  objections.
- Use table notes to document sample, period, variable construction, fixed effects,
  clustering, controls, units, and economic magnitude — a referee should read the exhibit
  without hunting through the text.
- Prefer figures where a relationship is visual: event-time cumulative returns, sorted
  portfolios, factor loadings. Show confidence bands; avoid chartjunk; use vector output
  (PDF/EPS).
- Move mechanical robustness grids to the supplementary replication package rather than padding
  in-paper exhibits, keeping the main identification logic self-contained.
- For theory papers, use figures to clarify comparative statics or equilibrium regions, not to
  decorate algebra; keep proofs compact so they do not eat the page budget.
- Respect the formatting baseline (at least 12-point font, at least 1.5 line spacing) and
  re-check that appendices, bibliography, figures, and tables still fit the 60-page cap.

## Page-budget worked example

Illustrative. A corporate-finance draft carries 14 tables and 5 figures — roughly 19
exhibit pages, nearly a third of the 60-page ceiling before a word of prose. The
RoF-shaped cut keeps in the body: summary statistics, the headline result, the
identification exhibit (an event-study figure), one mechanism table, and one robustness
table — five to seven exhibits. Everything else moves to the internet appendix behind
one-sentence pointers ("Table IA.4 repeats column 3 under alternative winsorization").
The body lands near eight exhibit pages, leaving room for the argument the referees grade.

## Exhibit calibration against the journal (hedged)

- Accepted general-interest finance papers tend toward six to ten body exhibits with a
  substantial internet appendix carrying the robustness battery; conventions differ by
  subfield, so sample recent RoF issues before fixing your own count.
- Supplementary material is hosted via OUP alongside the article and the replication
  package; confirm appendix naming and hosting mechanics against the journal's current
  author guidelines.

## Referee objections to exhibits and the conforming fix

| Objection | Fix that satisfies an RoF report |
|---|---|
| "Table 5 is uninterpretable" | split into panels; isolate the headline column; add the magnitude sentence to the note ("one s.d. of X moves Y by Z bp") |
| "The figure carries no inference" | add 95% bands and state the clustering level in the figure note |
| "Where is the robustness for claim 3?" | a visible internet-appendix pointer — robustness may leave the body but never the paper trail |
| "European and US samples are not comparable" | harmonization note: source per sample (Datastream vs. CRSP), screens applied, currency conversion, matching filters |
| "Exhibit numbers do not match the text" | regenerate all exhibits from the replication scripts (one numbered script per exhibit) before resubmitting |

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Review of Finance is the EFA flagship — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A nine-column kitchen-sink table as the main result.
- Figures with no units, no bands, or notes that require the body text to interpret.
- Letting appendix tables and the bibliography silently push the paper past 60 pages.

## Output format

```text
[Exhibit status] keep / compress / move / delete
[Finance role] <main result, identification, mechanism, robustness, or theory>
[Missing note] <sample, variables, controls, SEs, units, or data source>
[Page-budget action] <specific cut or move>
```
