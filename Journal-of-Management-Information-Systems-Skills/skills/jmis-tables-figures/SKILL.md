---
name: jmis-tables-figures
description: Use when the exhibits are the bottleneck for a Journal of Management Information Systems (JMIS) manuscript — regression/SEM tables, platform/value figures, measurement-model exhibits, or artifact-evaluation charts that must carry the argument inside the 50-page budget. Finalizes exhibits and labeling; it does not run the analysis (jmis-data-analysis) or polish prose (jmis-writing-style).
---

# Tables and Figures (jmis-tables-figures)

## When to trigger

- A reader cannot get the headline result from the tables/figures without the text
- Exhibits are dense, mislabeled, or report estimates without economic magnitude
- The exhibit count is pushing the manuscript over the **50-page** ceiling
- Survey papers lack the measurement-model exhibits reviewers expect (reliability/validity, loadings, HTMT)

## Make each exhibit answer one question

A JMIS exhibit should be readable on its own: a self-contained title, defined variables and units, the sample and period, and a note stating the estimator, clustering, and what the stars/SEs mean. The reader should be able to state the finding from the table alone. Order exhibits to track the argument — descriptive/measurement first, main result next, mechanism and robustness after.

## Report magnitudes, not just significance

JMIS values managerial relevance, so a coefficient table that shows only significance underdelivers. Report **economic magnitude** — marginal effects, elasticities, dollar value, or lift — alongside (or instead of) raw coefficients, and put the number that matters in the table the reader will actually look at. Report standard errors (and the clustering level) clearly; a figure with confidence intervals often communicates an effect better than a wall of asterisks.

## Exhibits by evidence type

| Evidence type | Exhibits reviewers expect |
|---------------|----------------------------|
| **IT-value / platform econometrics** | Descriptives + balance; main DiD/IV table; an **event-study figure with leads** for parallel-trends; robustness table; magnitude in interpretable units |
| **Behavioral survey (SEM/PLS)** | Measurement model (loadings, CR, AVE), discriminant validity (HTMT / Fornell-Larcker), structural-path diagram with coefficients and significance |
| **Experiment** | Cell means with CIs, manipulation-check results, treatment-effect figure, mediation/moderation exhibit |
| **Design-science / ML** | Benchmark table vs. credible baselines with uncertainty; ablation; a figure tying performance to the managerial decision |
| **Analytical model** | Comparative-static figures showing how the key outcome moves with the parameter that carries the insight |

## Respect the page budget and the appendix boundary

The complete manuscript is capped at **≤50 pages** (12pt, double-spaced), so exhibits compete with text for space. Keep in the body the exhibits that establish the contribution; move secondary robustness, full measurement batteries, and large parameter tables to the online appendix — but never let a load-bearing result live only in the appendix. Figures should be legible in grayscale and not rely on color alone. (检索于 2026-06；以官网为准.)

## Worked example: turning a coefficient table into a JMIS exhibit (illustrative)

A draft Table 3 reports `redesign × post = −0.062 (0.018)***` and nothing else. A JMIS reader cannot tell what that means. The fixed exhibit keeps the coefficient but adds a column translating it to the managerial scale (−6.2 pp seller retention; ≈N exits/quarter at the observed base), states the estimator and the clustering level in the note, and is paired with an **event-study figure** whose flat pre-period leads visibly support parallel trends. The reader now gets identification *and* magnitude from the exhibits without leaving for the prose — which is exactly what a method-literate, management-minded JMIS referee scans for first.

## Sequence the exhibits to track the argument

Order is part of the argument: (1) descriptives/balance establish the sample and comparability; (2) the main effect table/figure delivers the headline with magnitude; (3) the mechanism exhibit shows *why* (mediation, heterogeneity, the channel); (4) robustness shows the threat-by-threat survival. A reader should be able to reconstruct the paper's logic from the exhibit sequence alone. Resist the temptation to front-load a dramatic figure before the reader can interpret it.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMIS is empirical IS — survey-based SEM and econometric panels; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every exhibit is self-contained (title, variables, units, sample, period, note)
- [ ] The headline finding is readable from the main exhibits without the prose
- [ ] Economic magnitude (not just significance) is reported for the key effect
- [ ] SEs and clustering level are stated; CIs used where they communicate better
- [ ] Survey papers include measurement-model and discriminant-validity exhibits
- [ ] Empirical papers include an event-study/leads figure where parallel trends matter
- [ ] Body holds the contribution-establishing exhibits; appendix holds only support; ≤50pp respected
- [ ] Exhibits numbered consecutively, captioned by content, and called out in order
- [ ] No exhibit de-anonymizes the author or proprietary data source in the blind file

## Number and reference exhibits for JMIS's house style

JMIS uses **numbered bracketed citations [n]** with an alphabetized reference list, so any in-text reference to a source *inside* a table note should use the same numbered form, not author-date. Number tables and figures consecutively, give each a caption that names what it shows (not just "Regression results"), and make sure every exhibit is called out in the text in order. Because the manuscript is double-anonymized, scrub identifying content from figures too — institution logos, internal dashboard screenshots, or proprietary platform names that reveal the author or data source belong out of the blind file or suitably masked. (检索于 2026-06；以官网为准.)

## Anti-patterns

- A coefficient table with stars but no magnitude or interpretation
- Exhibits the reader cannot parse without hunting through the text
- A load-bearing result relegated to the online appendix
- A staggered-DID paper with no event-study/leads figure
- A survey paper missing discriminant-validity evidence
- Color-only figures that fail in grayscale
- A "kitchen-sink" main table with no marked preferred specification
- Author-date references in a table note when JMIS uses numbered brackets
- Figures or screenshots that de-anonymize the author or proprietary data source in a blind file

## Common exhibit defects JMIS referees flag

- **A "kitchen-sink" main table** with twenty controls and no marked specification — highlight the preferred column and relegate the rest.
- **Stars without a scale** — a reader cannot tell whether `0.06***` is large; always pair significance with an interpretable magnitude.
- **A staggered-DID paper with only a single pooled coefficient** — show the dynamic event-study so pre-trends and the post-treatment path are visible.
- **A survey paper whose constructs overlap** — without an HTMT/Fornell-Larcker exhibit, reviewers assume discriminant validity fails.
- **Figures that die in print** — JMIS appears in print, so a color-coded figure that becomes unreadable in grayscale will draw a production comment; encode with line style or labels too.
- **Notes that omit the estimator or clustering** — the reader must be able to reconstruct what produced the numbers from the note alone.

## Output format

```text
【Headline exhibit】reads alone? magnitude shown? [Y/N]
【Diagnostics shown】event-study/leads | measurement model + HTMT | benchmarks + uncertainty
【Inference labeling】SEs + clustering stated; CIs where clearer [Y/N]
【Body vs. appendix】contribution exhibits in body; ≤50pp respected [Y/N]
【Next step】jmis-writing-style
```
