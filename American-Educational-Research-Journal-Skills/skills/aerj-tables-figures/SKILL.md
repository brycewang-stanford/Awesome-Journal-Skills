---
name: aerj-tables-figures
description: Use when building tables and figures for an American Educational Research Journal (AERJ) manuscript. Exhibits must be self-contained, accessible, and formatted to APA 7th edition, and they must be anonymized for masked review. Improves exhibits; it does not generate data.
---

# Tables & Figures (aerj-tables-figures)

In AERJ, a reader should grasp each exhibit **without hunting through the text**, and every exhibit must
follow **APA 7th-edition** table/figure conventions. Because review is **masked**, exhibits must carry
no identifying clues (institution names, data-source giveaways in titles).

## When to trigger

- Designing tables/figures or revising them after analysis
- A reviewer found an exhibit unreadable, mislabeled, or non-APA
- Preparing exhibits for a masked submission (no identifying content)
- Deciding what belongs in the body vs an appendix

## Principles

1. **Self-contained.** Title states what the exhibit shows; notes define every abbreviation, the
   sample/N, the units, and significance/probability conventions. A reader should not need the text.
2. **APA 7th-edition format.** Table number + italic title; horizontal rules only (no vertical rules);
   figure number + title; a general note, then specific notes, then probability notes.
3. **Report estimates with uncertainty.** Coefficients with SEs/CIs; for multilevel models, label
   levels and random effects; mark the estimand, not just stars.
4. **Figures earn their place.** Use a figure when it shows something a table cannot (trajectories,
   interactions, distributions, RD/event-study, joint displays for mixed methods). Otherwise use a table.
5. **Accessibility.** Colorblind-safe palettes; legible in grayscale; readable at print size; vector
   output for line art.
6. **Qualitative exhibits.** Coding trees, thematic maps, and evidence tables (theme → exemplar
   quotation) are legitimate exhibits — anonymize participants and sites.
7. **Match the package.** Exhibit numbers/values must match the analysis output and the deposited
   materials (see `aerj-transparency-and-data-policy`).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AERJ is empirical education research — field experiments and observational school data; multilevel inference and many-outcome corrections are central.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Tables readable only with the surrounding paragraph
- Vertical rules, inconsistent decimals, undefined abbreviations (non-APA)
- Stars without effect sizes or intervals; no N or units
- Rainbow palettes that fail in grayscale or for colorblind readers
- Identifying clues in titles/notes that break masking
- Exhibit values that drift from the replication package

## What AERJ exhibit referees check

Reviewers across AERJ's policy/institutional, teaching/learning, development, and cross-cutting lenses
read exhibits before they read prose, so an unreadable exhibit damages the paper
before the argument is even heard. Use this as a pre-submission exhibit triage.

| Exhibit type | What an AERJ referee expects to see | Desk-screen / first-round red flag |
|--------------|-------------------------------------|------------------------------------|
| Multilevel results table | Level-1 and level-2 coefficients separated, random-effect variances, ICC, N at each level | One undifferentiated column that hides the nesting |
| Growth-model table | Intercept/slope means, variance components, time coding stated | Trajectories implied but no variance components reported |
| Quasi-experimental figure | Event-study or RD plot with bandwidth, pre-trend, confidence band | A bare bar chart of means with no uncertainty |
| Qualitative evidence table | Theme → operational definition → exemplar excerpt → source (anonymized) | A wall of quotations with no analytic column |
| Mixed-methods joint display | Quant result and qual finding side by side with a meta-inference column | Two stacked exhibits that never meet |

## Worked exhibit vignette (illustrative)

Take an AERJ study of a middle-school **reading-comprehension intervention** in 40 schools.
The core table reports a treatment coefficient of **0.18 SD** (95% CI [0.04, 0.32]), a school-level
ICC of **0.14**, and **N = 3,200** students in **40** schools (all numbers illustrative). A strong
AERJ exhibit puts the estimate, the interval, the ICC, and both N levels in one self-contained note;
a weak one prints "b = 0.18, p < .05" and forces the reader into the methods section to learn the
sample is clustered. The companion joint display pairs that 0.18 SD estimate with the qualitative
finding that teachers in higher-gain schools re-allocated time to discussion — the meta-inference
column is what earns the figure its place.

## Referee pushback and the venue fix

- *"I cannot tell which estimates are between- vs within-school."* → Split the table by level and
  label random effects; report the ICC explicitly.
- *"The figure is unreadable in the printed (grayscale) issue."* → Move from color-coded lines to
  distinguishable markers/linetypes; SAGE print remains a constraint.
- *"This exhibit could identify the district."* → Strip site-revealing titles and notes; masked
  review requires anonymized exhibits, not just an anonymized text body.

## Output format

```
【Exhibit】table / figure — one-line purpose
【Self-contained?】title + notes define N, units, abbreviations, significance [Y/N]
【APA 7th format】[Y/N]
【Uncertainty shown】SE/CI + estimand labeled [Y/N]
【Accessible】colorblind-safe + grayscale-legible [Y/N]
【Masked】no identifying clues [Y/N]
【Next】aerj-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting/exhibit tooling and APA table helpers
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APA style and masked-review requirements
