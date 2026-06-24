---
name: jmgmt-tables-figures
description: Use when exhibits are the bottleneck for a Journal of Management (JOM) manuscript — the means/SD/correlation table, CFA/SEM and HLM result tables, the theoretical-model figure, interaction plots, and meta-analytic forest/funnel plots, all in APA style and under the 50-page guillotine. Builds exhibits; it does not run the analysis (jmgmt-data-analysis).
---

# Tables & Figures (jmgmt-tables-figures)

## When to trigger

- The descriptive/correlation table is missing, mislabeled, or inconsistent with the text
- A SEM/HLM table is dense and a reviewer cannot find the focal effect
- An interaction is claimed but never plotted
- A meta-analysis lacks a forest plot or a publication-bias funnel
- Exhibits are eating into the **50-page (inclusive)** budget and need to be tightened

## The exhibits a JOM paper is expected to carry

JOM follows **APA (7th)** style, and reviewers (many of them methodologists) expect a conventional, scannable exhibit set:

1. **Table 1 — Means, SDs, reliabilities, and correlations.** Variables in a sensible order; reliabilities (α/ω) on the diagonal; significance shown but always paired with the values; full Ns and a clear note. This is the most-read table; errors here cost credibility.
2. **Measurement-model table (CFA).** Standardized loadings, CR/ω, AVE, and a discriminant-validity panel (AVE vs. squared correlations or HTMT).
3. **Hypothesis-test table (SEM/HLM/regression).** Steps/models in columns; the *focal* coefficients visually findable; effect sizes (ΔR²/f²) and CIs reported, not just stars.
4. **Theoretical-model figure.** Boxes and arrows mapping **one-to-one** to the hypotheses, with hypothesis labels (H1, H2…) on the paths — it should be readable without the text.
5. **Interaction plot(s).** Simple slopes at ±1 SD with axes labeled in construct terms; a region-of-significance band where useful.
6. **(Meta-analysis) forest plot + funnel/PET-PEESE plot** and a moderator table reporting k, N, corrected effects, CIs, and credibility intervals.

## House-style and significance conventions

- APA significance notation is permitted (* p<.05, ** p<.01, *** p<.001), but **always report the coefficient/effect size and ideally a CI** — stars alone are not evidence of magnitude, and JOM methods reviewers say so.
- Each table is self-contained: full variable names (no undefined abbreviations), Ns, the estimator, and what the cells are (b, β, OR, r).
- Figures must be legible in grayscale and at print size; do not encode meaning in color alone.

## Working under the 50-page guillotine

Because the **50-page limit counts tables and figures** (检索于 2026-06；以官网为准), every exhibit competes with text. Tactics: merge the descriptives and correlations into one Table 1; move secondary robustness tables and the full CFA item list to the **online supplement**; keep only exhibits that carry a hypothesis test or the model itself in the main paper. Cut any table the text fully narrates.

## Reading exhibits the way a JOM methods reviewer does

A methodologically literate reviewer scans the exhibits *before* the prose to sanity-check the claims. They will: (a) confirm the diagonal of Table 1 carries reliabilities and that no inter-construct correlation is so high it threatens discriminant validity; (b) check that the squared focal correlation is consistent with the structural coefficient (a large path with a near-zero correlation is a red flag); (c) verify the hypothesis table's degrees of freedom and N match the sample described in methods; and (d) confirm every interaction in the hypothesis table also appears as a plot. Build exhibits anticipating exactly this scan, so the numbers cross-validate each other.

## Meta-analysis exhibits specifically

For a JOM meta-analysis the exhibits *are* the evidence. The moderator table should report, per moderator level: **k, total N, the artifact-corrected mean effect, its 95% CI, the 80% credibility interval, and a heterogeneity statistic (I² or Q)**. A forest plot orders effects so the reader sees the spread; a funnel plot (with trim-and-fill or PET-PEESE overlay) shows the bias picture. Tie each moderator row back to the competing theory it tests, so the table reads as a theory adjudication rather than a coefficient list.

## The theoretical-model figure as the paper's spine

In a JOM empirical paper the model figure is the single most consulted exhibit: reviewers use it to check that the hypotheses, the methods, and the results all line up. Draw it so the antecedent, mechanism (mediator), moderator, and outcome are each a labeled box; put the hypothesis number on each path; and show the moderator entering on the path it is theorized to qualify, not floating beside it. If a path in the figure has no corresponding hypothesis, or a hypothesis has no path, a reviewer will read it as sloppiness about the theory. Keep control variables out of the figure.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Management covers empirical management broadly (including meta-analysis); the chain below serves primary causal / panel work.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Table 1 has means, SDs, reliabilities on the diagonal, correlations, Ns, and a clean note
- [ ] CFA table reports loadings, CR/ω, AVE, and discriminant validity
- [ ] Hypothesis table makes focal effects findable; effect sizes/CIs present, not stars alone
- [ ] Theoretical-model figure maps one-to-one to hypotheses, labeled H1…Hk
- [ ] Every claimed interaction has a simple-slopes plot
- [ ] (Meta) forest + funnel/bias plot + moderator table present
- [ ] APA 7th formatting; exhibits legible in grayscale; no color-only encoding
- [ ] Exhibit set fits the 50-page budget; secondary tables in the supplement

## Anti-patterns

- **A correlation table that disagrees with the text** (different Ns, signs, or values)
- **Reliabilities missing** from the diagonal of Table 1
- **Stars without magnitudes** — a hypothesis table of asterisks and no effect sizes
- **A model figure that does not match the hypotheses** (extra/missing paths)
- **An interaction asserted but never plotted**
- **Color-dependent figures** that vanish in grayscale
- **Exhibit bloat** that pushes the paper over 50 pages instead of using the supplement

## Output format

```
【Table 1】means/SD/reliabilities(diag)/correlations/N + note? [Y/N]
【CFA table】loadings/CR-ω/AVE/discriminant? [Y/N]
【Hypothesis table】focal effects findable; effect sizes + CIs? [Y/N]
【Model figure】one-to-one with H1…Hk, labeled? [Y/N]
【Interaction plots】every interaction plotted? [Y/N]
【Meta exhibits】forest + funnel + moderator table? [Y/N/NA]
【APA + grayscale + 50pp budget】compliant? [Y/N]
【Next step】jmgmt-writing-style
```
