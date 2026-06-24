---
name: jpsp-tables-figures
description: Use when building tables and figures for a Journal of Personality and Social Psychology (JPSP) manuscript in APA 7th edition style — embedded in the text, self-contained, and covering a multi-study package including the internal meta-analysis forest plot. Guides exhibit design; it does not generate data.
---

# Tables & Figures — APA 7th (jpsp-tables-figures)

JPSP exhibits do heavy lifting because the paper spans **many studies**: readers navigate the package
through your tables and figures. JPSP asks authors to **embed tables and figures in the manuscript
text**, and information in tables **does not count toward the word limit** — so well-built exhibits
both communicate and free up words for the (capped) introduction and discussion.

## When to trigger

- Building or revising tables and figures
- Summarizing results across multiple studies
- Producing the internal meta-analysis forest plot
- Formatting exhibits to the APA Publication Manual (7th edition)

## What strong JPSP exhibits do

1. **Self-contained.** Each table/figure is readable without the text: full title, variable
   definitions, N, units, error bars defined, and notes explaining abbreviations and significance.
2. **Carry the multi-study story.** A **cross-study summary table** (effect sizes + CIs per study)
   and a **forest plot** for the internal meta-analysis let reviewers see convergence at a glance.
3. **Show effects, not just stars.** Plot estimates with **confidence intervals**; for repeated
   measures use within-subject CIs; show distributions (e.g., raincloud) where they matter.
4. **APA 7th formatting.** APA table structure (no vertical rules), figure captions and notes, proper
   statistical notation; SEM path diagrams labeled with standardized coefficients where used.
5. **Embedded, not appended.** Place each exhibit near its first mention in the text per JPSP rule;
   keep supplemental-only exhibits in the online supplement with a table of contents.
6. **Accessible.** Colorblind-safe palettes; legible in grayscale; vector output for print.

## Exhibit checklist

- [ ] Every exhibit self-contained (title, N, units, error bars, notes)
- [ ] Cross-study summary table of effect sizes + CIs
- [ ] Forest plot for the internal meta-analysis
- [ ] Effect sizes with uncertainty shown, not stars alone
- [ ] APA 7th table/figure formatting and notation
- [ ] Tables/figures embedded in text; supplements have a table of contents
- [ ] Colorblind-safe and grayscale-legible

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPSP is predominantly experimental social/personality psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), power, and family-wise corrections are decisive.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A separate, near-identical table per study with no integrative summary
- Stars-only tables; error bars whose meaning (SE vs CI vs SD) is undefined
- Figures unreadable in grayscale or to colorblind readers
- Exhibits dumped at the end instead of embedded near first mention
- Tables that duplicate the text instead of compressing it

## The two exhibits every JPSP package needs

Because the paper spans studies, two integrative exhibits do disproportionate work and reviewers look for them by name:

| Exhibit | What it must show | Reviewer flag if missing |
|---------|-------------------|---------------------------|
| Cross-study summary table | One row per study: N, design, key effect size, **95% CI** | "I cannot see the package converge" |
| Internal meta-analysis forest plot | Per-study effects + pooled random-effects estimate + I² | "Where is the integrative analysis?" |

*Illustrative forest-plot row set* (invented): S1 d = 0.34 [0.10, 0.58]; S2 d = 0.21 [−0.02, 0.44]; S3 d = 0.40 [0.16, 0.64]; pooled d = 0.31 [0.18, 0.45]. Plotting these together — each CI as a horizontal bar, the diamond as the pooled estimate — lets a reviewer see S2's wide interval is low power, not disconfirmation. A stars-only table hides exactly that.


## Exhibit pass for Journal of Personality and Social Psychology

Treat this skill as an executable review pass, not a prose hint. First lock the construct validity, study sequence, power/robustness plan, and boundary conditions; then judge whether the current manuscript answers the venue's real reader: psychology reviewers who need a theoretical construct, validated measurement, and cumulative-study logic.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Psychological Science for shorter general-interest findings, Personality and Social Psychology Bulletin for field scope, Journal of Experimental Social Psychology for experiment-centered claims; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Per-study exhibits】list (design-appropriate)
【Cross-study summary】effect-size table present? [Y/N]
【Meta-analysis figure】forest plot present? [Y/N]
【APA 7th formatting】tables/figures + notation compliant? [Y/N]
【Embedded + accessible】in-text + colorblind/grayscale-safe? [Y/N]
【Next】jpsp-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — papaja/apaTables, ggplot2, metafor forest plots, SEM path diagrams
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — embedded-exhibits rule and word-count treatment
