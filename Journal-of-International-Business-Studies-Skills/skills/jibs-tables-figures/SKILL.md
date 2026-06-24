---
name: jibs-tables-figures
description: Use when finalizing the tables and figures for a Journal of International Business Studies (JIBS) manuscript — cross-country descriptives, correlation/result tables, measurement-invariance and CMV diagnostic exhibits, cross-level interaction plots, and country-coverage maps, all in JIBS Style Guide form and counted inside the word limit. Polishes exhibits; do not invoke until the model and contribution are settled.
---

# Exhibits in JIBS House Style (jibs-tables-figures)

## When to trigger

- Results are stable and you are building the main tables and figures
- A reviewer says an exhibit is not self-explanatory or off house style
- You need to display cross-country structure, invariance, or cross-level interactions clearly
- You must trim exhibits because JIBS counts tables/figures inside the word limit

## Remember: exhibits count toward the JIBS word limit

JIBS articles are ~10,000 words (strong/broad) or ~7,000 (narrower), and the word count is **inclusive of tables, figures, and appendices**. Every exhibit you add competes with text. Keep only exhibits that carry the cross-border argument; push full invariance and robustness output to an online appendix (which is also counted, so be disciplined).

## The exhibits a JIBS empirical paper usually needs

1. **Sample & country-coverage table.** List countries, observations per country, and key country-level descriptives so readers can judge the cross-national spread and any concentration. A country-coverage map or figure can substitute when there are many countries.
2. **Descriptives & correlation table.** Means, SDs, and a correlation matrix with reliabilities on the diagonal; flag the level (individual/firm/country) of each variable.
3. **Measurement-invariance summary.** A compact table reporting configural/metric/scalar fit (and ΔCFI/ΔRMSEA across steps), since cross-national equivalence is a first-order JIBS concern.
4. **Main results table(s).** Nested/hierarchical model columns (base → controls → main effects → interactions) for multilevel or dynamic-panel models; report SEs clustered by country, and identification diagnostics (e.g., first-stage F, Hansen/AR(2)) where endogeneity is addressed.
5. **Cross-level interaction figure.** Plot simple slopes for cross-country/cross-level moderation; label the high/low country-level moderator clearly — a self-contained figure, not a coefficient restatement.
6. **CMV / robustness diagnostic exhibit** as needed (marker-variable or latent-method results).

## JIBS Style Guide formatting

Follow the **JIBS Style Guide**: 11-point Times New Roman, double-spaced, with author-date (name, year) citations in notes. Each table/figure must be **self-contained** — a title, defined variables and units, sample size, the estimator, what the SEs cluster on, and significance conventions stated in the note. Spell out country/region groupings. Keep decimals consistent.


## Exhibit pass for Journal of International Business Studies

Use this as a second-pass capability check. First lock the cross-border mechanism, level of analysis, institutional context, and generalizability claim; then test whether the manuscript addresses international-business reviewers who expect cross-border theory, context sensitivity, and credible firm or institution evidence.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Strategic Management Journal for strategy theory, Journal of Management for broader management, International Business Review for applied IB breadth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIBS is international business — cross-country panels with confounded institutions; emphasize fixed effects, clustering, and endogeneity of location / entry choices.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```
【Country coverage】table/map present; concentration flagged? ...
【Descriptives/correlations】reliabilities on diagonal; levels marked ...
【Invariance summary】configural/metric/scalar reported ...
【Main table】nested columns; SE clustering; ID diagnostics ...
【Interaction figure】simple slopes, moderator labeled ...
【Word-budget impact】exhibits trimmed to fit inclusive limit ...
【Next step】jibs-writing-style
```

## Anti-patterns

- Exhibits that restate coefficients instead of clarifying the cross-country result.
- Correlation tables without reliabilities or without marking variable level.
- Interaction "tables" with no simple-slopes plot.
- Forgetting that tables/figures/appendices count toward the JIBS word limit.
