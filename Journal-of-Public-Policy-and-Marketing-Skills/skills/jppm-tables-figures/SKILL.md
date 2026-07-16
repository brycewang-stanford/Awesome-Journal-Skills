---
name: jppm-tables-figures
description: Use when building exhibits for a Journal of Public Policy & Marketing (JPP&M) manuscript — event-study and DiD displays, condition-contrast tables, subgroup forest plots, and stimuli exhibits that a policy reader can act on. Builds the exhibits; it does not produce the estimates (jppm-data-analysis).
---

# Tables & Figures (jppm-tables-figures)

## When to trigger

- Tables report coefficients an academic can parse but a policy reader cannot
- The evaluation has no event-study figure showing pre-trends and dynamics
- Subgroup results for vulnerable populations are scattered across prose
- The tested label/warning/disclosure stimuli are described but never shown
- The 50-page all-inclusive cap forces you to choose which exhibits survive

## Exhibits for a dual audience

JPP&M exhibits are read by two audiences at once: methods-literate reviewers who will interrogate the identification, and policy-oriented readers (including practitioners on the editorial board) who need the decision-relevant magnitude at a glance. Every exhibit should therefore carry **two layers**: the estimation detail (specification, SEs, clustering, N) in the table body and notes, and a **decision-unit translation** — percentage points, dollars, calories, share of consumers — in the headline row, figure annotation, or note. Because the 50-page limit *includes* tables and figures at every review stage, each exhibit must displace prose, not duplicate it; move the long battery to a web appendix.

## The high-value JPP&M exhibits

| Exhibit | What it must carry | Typical failure |
|---------|--------------------|-----------------|
| Stimuli figure | the actual tested labels/disclosures side by side, at realistic scale | describing formats in prose a regulator would need to see |
| Event-study figure | pre-period placebos + dynamic effects, CI band, policy date marked | showing only the post-period average |
| DiD table | group-time ATT, estimator named, cluster level, pre-trend sensitivity row | plain TWFE with stars and no diagnostics |
| RDD figure | binned outcomes + fit on both sides, bandwidth noted; density plot nearby | a fitted line with no raw data visible |
| Condition-contrast table | means/effects per policy option with the pairwise contrast the decision needs | omnibus F with no decision-mapped contrasts |
| Subgroup forest plot | pre-specified vulnerable-group effects with corrected CIs on one axis | significant splits in text, the rest invisible |
| Policy-translation table | effect × exposed population = market magnitude, with assumptions listed | leaving the rescaling to the reader |

A stimuli figure is uniquely load-bearing at this journal: agencies regulate formats, so reviewers want to see exactly what was tested and whether it is mandatable.

## House conventions (AMA journals)

- Follow the **AMA journals style** shared across JM/JMR/JPP&M: numbered tables and figures, descriptive titles, notes defining every abbreviation, references and tables may be single-spaced while text is double-spaced (per the AMA submission guidelines — re-check current specifics on ama.org before formatting).
- Report **effect sizes and confidence intervals**; stars alone do not survive review.
- State the **estimator, clustering level, and fixed effects** in each table's note so the exhibit stands alone.
- Keep **Ns visible** (per cell / per group-time), including before/after exclusions.
- Figures must survive **grayscale print** and small reproduction — policy briefs will screenshot them.

## Economy under the 50-page cap

- Budget exhibits first: typically 1 stimuli figure, 1 identification figure, 2–3 core tables, 1 subgroup display in the body; everything else to the web appendix.
- Merge robustness variants into a single compact multi-column table rather than serial near-duplicates.
- Never present the same estimate as both table and figure; pick the form the decision reader needs.

## Checklist

- [ ] Each body exhibit carries both estimation detail and a decision-unit translation
- [ ] Stimuli shown as tested, at realistic scale
- [ ] Event-study / RDD figures display pre-trends or raw discontinuity, not just fits
- [ ] Estimator, clustering, FEs, and Ns named in every table note
- [ ] Subgroup effects displayed as a single corrected family (forest plot or panel)
- [ ] Effect sizes + CIs everywhere; no stars-only columns
- [ ] Body exhibits fit the 50-page all-inclusive budget; battery moved to web appendix

## Anti-patterns

- **Coefficient wall**: a 12-column regression table with no translated magnitude anywhere
- **Invisible stimuli**: regulating formats the reader never gets to see
- **Post-only plots**: dynamics figures that start at the policy date
- **Star tables**: significance markers standing in for effect sizes and CIs
- **Subgroup scatter**: heterogeneity sprinkled through prose instead of one comparable display
- **Cap blindness**: ten body exhibits that force the text out of the 50-page envelope

## Output format

```text
【Exhibit budget】body tables/figures list vs. web-appendix list (within 50-page cap)
【Stimuli figure】tested formats shown at scale? [Y/N]
【Identification display】event-study / RDD / placebo figure with pre-period evidence? [Y/N]
【Decision-unit layer】each body exhibit translated for the policy reader? [Y/N]
【Notes discipline】estimator, clustering, Ns, abbreviations in every note? [Y/N]
【Next skill】jppm-writing-style
```
