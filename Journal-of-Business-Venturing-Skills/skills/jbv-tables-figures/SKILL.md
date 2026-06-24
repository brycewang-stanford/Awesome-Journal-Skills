---
name: jbv-tables-figures
description: Use when building or cleaning the exhibits for a Journal of Business Venturing (JBV) manuscript — venture descriptive/correlation tables, survival curves, interaction plots, process models, and qualitative data structures in Elsevier house style. Late-stage polish; do not invoke while the entrepreneurial mechanism or identification is still unsettled (use jbv-theory-development / jbv-data-analysis first).
---

# Tables & Figures (jbv-tables-figures)

## When to trigger

- Tables/figures are cluttered, redundant, or not self-explanatory
- You need the standard exhibit set for an entrepreneurship empirical paper
- A reviewer says an exhibit is "not interpretable" or "off house style"
- You are presenting survival, interaction, or qualitative-process results

## JBV exhibit conventions

JBV publishes via Elsevier/ScienceDirect, so prepare figures for both print and online, with self-contained captions and references that can be reconciled to the journal's numbered style. Each exhibit must stand alone: a reader should grasp it without the text.

## The standard exhibit set (match to your design)

- **Table 1 — Descriptives & correlations**: venture-level means, SDs, and correlations; note the sampling frame (e.g., Crunchbase/PSED) and the time window. Flag survivorship in the note if the sample conditions on survival.
- **Table 2+ — Main models**: nested model columns; report coefficients with SEs, the SE-clustering level (cohort/region/industry), and fit. For **survival models** report hazard ratios with a clear baseline and the risk set; for **selection models** show both the selection and outcome equations.
- **Interaction plots**: when you theorize moderation by an entrepreneurial condition (uncertainty, resource scarcity, ecosystem support), plot simple slopes with a clear region of significance — do not leave the interaction to a coefficient alone.
- **Survival/Kaplan-Meier curves**: for time-to-IPO/exit/failure, show curves by key group with at-risk counts.
- **Process model / framework figure**: a boxes-and-arrows model of the entrepreneurial mechanism (opportunity → action → outcome) — earns its place only if it adds beyond the text.
- **Qualitative data structure**: for inductive work, a Gioia-style figure (first-order codes → second-order themes → aggregate dimensions) plus a power-quote table.

## Quality bar

- Every table note defines abbreviations, significance stars, SE type, and N (and venture-level vs. event-level units).
- Figures are legible in grayscale; lines/markers distinguishable without color.
- No exhibit duplicates the text; no number in a table contradicts the prose.
- Units and scales are stated (e.g., USD funding, log employees, months-to-exit).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBV studies founders and ventures where selection / survivorship threatens every claim; lead with identification and selection-correction tooling.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Descriptives/correlation table with frame, window, and survivorship note
- [ ] Main-model table reports SEs, clustering level, fit; HRs/selection eqs if used
- [ ] Interaction plotted with simple slopes + significance region
- [ ] Survival curves with at-risk counts where time-to-event is the outcome
- [ ] Process model or framework figure earns its place (adds beyond text)
- [ ] Qualitative data structure + power quotes for inductive work
- [ ] Self-contained captions; grayscale-legible; no text duplication

## Anti-patterns

- **Coefficient-only moderation** with no simple-slope plot.
- **Mega-table** dumping every model and control with no narrative.
- **Color-only figures** that collapse in print.
- **Decorative framework figure** that merely restates the abstract.


## Exhibit pass for Journal of Business Venturing

Treat this skill as an executable review pass, not a prose hint. First lock the entrepreneurial mechanism, level of analysis, evidence design, and boundary conditions for ventures; then judge whether the current manuscript answers the venue's real reader: entrepreneurship reviewers who ask whether the paper advances venture formation, opportunity, founder, or ecosystem theory.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Entrepreneurship Theory and Practice for broader entrepreneurship, Strategic Entrepreneurship Journal for strategy interface, AMJ for general management; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Exhibit list】T1 descriptives; T2.. models; F1 interaction; F2 survival; F3 model ...
【Survival/selection reporting】HRs / two equations shown? ...
【Moderation】simple-slope plot present? ...
【Qual】Gioia data structure + quotes? ...
【House-style fixes】captions, grayscale, units ...
【Next step】jbv-writing-style
```
