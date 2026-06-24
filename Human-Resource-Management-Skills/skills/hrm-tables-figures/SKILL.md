---
name: hrm-tables-figures
description: Use when exhibits are the bottleneck for a Human Resource Management (Wiley "HRM") manuscript — the descriptives/correlation table, the model build-up, interaction and simple-slope plots, the theoretical-model figure, and (for qualitative work) the data-structure figure. Builds reader-ready exhibits; it does not run the analysis (hrm-data-analysis).
---

# Tables & Figures (hrm-tables-figures)

## When to trigger

- The correlation table is missing means, SDs, reliabilities, or has inconsistent decimals
- A significant interaction is reported in text but never plotted
- The regression/HLM tables dump every coefficient with no model build-up logic
- The theoretical model in the intro does not match the hypotheses being tested
- A qualitative paper has rich quotes but no data-structure figure

## The exhibits HRM expects (and the conventions referees enforce)

HRM follows management/applied-psychology table norms (APA-aligned house style). The standard set:

| Exhibit | Must contain |
|---------|--------------|
| **Table 1 — descriptives & correlations** | Means, SDs, full correlation matrix, **scale reliabilities (α) on the diagonal**; significance noted; level-appropriate (within/between if multilevel) |
| **Table 2+ — regression / HLM / SEM** | Nested **model build-up** (controls → main effects → interactions); unstandardized and/or standardized coefficients with SEs; model fit (R², ΔR², pseudo-R², CFI/RMSEA for SEM); df and N at each level |
| **Interaction plot** | Simple slopes at ±1 SD, axes labeled in construct units, the moderator legend clear, region of significance where relevant |
| **Theoretical-model figure** | Boxes and arrows mapping **one-to-one** to the numbered hypotheses |
| **Mediation figure** | Path coefficients on the diagram; indirect effect + bootstrap CI reported |
| **Qualitative data-structure figure** | First-order codes → second-order themes → aggregate dimensions (Gioia-style) |

## Make exhibits carry the argument, not just the numbers

- **The correlation table is the credibility table.** Reviewers read it first; reliabilities below ~.70, a correlation near 1.0 between "distinct" constructs (discriminant-validity red flag), or a mean at a scale ceiling all undermine the paper before the hypotheses are tested.
- **Build models, don't dump them.** A nested progression shows the incremental variance the focal effect explains over controls — that ΔR²/Δ-2LL is the contribution made visible.
- **Always plot a supported interaction.** A coefficient is not interpretable as "the effect strengthens"; the plot is. Label axes in real construct units, not z-scores, so an HR reader can see the practical magnitude.
- **The model figure is a contract.** Every arrow must be a hypothesis and every hypothesis an arrow; mismatches read as sloppiness or HARKing.
- **Translate magnitude for practice.** Where possible, annotate the practically meaningful difference (e.g., the predicted productivity gap between low- and high-HPWS units) so the exhibit serves HRM's practice mandate.

## Formatting discipline

- Self-contained titles and notes: a reader should understand each exhibit without the text (N, level, what significance markers mean, abbreviations defined).
- Consistent decimals (typically two) and consistent variable names across all tables and the text.
- Report **effect sizes and CIs**, not only stars; do not let asterisks substitute for interpretation.
- Place exhibits per Wiley/ScholarOne submission conventions; keep figures legible in greyscale.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). HRM is empirical HR — multilevel survey data, field experiments, and panels; multilevel inference and many-outcome corrections matter most.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Table 1 has M, SD, correlations, and reliabilities on the diagonal
- [ ] Regression/HLM/SEM tables show a nested model build-up with fit and ΔR²/Δfit
- [ ] Every supported interaction is plotted with labeled, construct-unit axes
- [ ] The theoretical-model figure maps one-to-one to the hypotheses
- [ ] Mediation diagrams show paths and indirect-effect bootstrap CIs
- [ ] Qualitative papers include a first-order → themes → dimensions data structure
- [ ] Titles/notes are self-contained; decimals and variable names consistent
- [ ] Effect sizes / CIs reported; practitioner magnitude annotated where possible

## Anti-patterns

- **Missing reliabilities**: a correlation table with no α on the diagonal
- **Coefficient dump**: one mega-table with no model build-up
- **Unplotted interaction**: a claimed moderation never shown graphically
- **Figure–hypothesis mismatch**: arrows that don't correspond to numbered hypotheses
- **Star-only reporting**: asterisks instead of effect sizes and CIs
- **Z-score axes**: interaction plots no HR reader can map to practice
- **Orphan exhibits**: tables that cannot be read without the surrounding text

## Output format

```text
【Journal】Human Resource Management (Wiley "HRM")
【Skill】hrm-tables-figures
【Table 1】M/SD/correlations/reliabilities present? [Y/N]
【Model tables】nested build-up + fit + ΔR²/Δfit? [Y/N]
【Interactions】all supported ones plotted, construct-unit axes? [Y/N]
【Model figure】one-to-one with hypotheses? [Y/N]
【Mediation/qual】path CIs / data-structure figure present? [Y/N]
【Magnitude】practitioner-meaningful annotation added? [Y/N]
【Next skill】hrm-writing-style
```
