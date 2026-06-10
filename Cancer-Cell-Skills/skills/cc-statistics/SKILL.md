---
name: cc-statistics
description: Use when defining n, choosing statistical tests, correcting for multiple comparisons, and reporting error bars for a Cancer Cell (Cell Press) manuscript. Focuses on biological statistics and avoiding pseudo-replication; it does not design experiments or build figures.
---

# Biological Statistics (cc-statistics)

## When to trigger

- `n` is ambiguous, or you suspect pseudo-replication
- Unsure which test fits the data and design
- Many comparisons without multiplicity correction
- Error bars / variability are unlabeled in figures or legends

## Defining `n` (the core issue)

- `n` = number of **independent biological replicates** (separate mice, independent cultures/passages, distinct patients).
- Technical replicates (duplicate wells, repeat reads) describe measurement precision and **do not** count toward `n`.
- State `n` for **every** panel in the legend, with what one unit is ("n = 5 mice per group", "n = 3 independent experiments").
- Pooling cells from many wells of one experiment and calling it n=many is **pseudo-replication** — a classic Cancer Cell reviewer catch.

## Choosing the test

| Design | Typical test |
|--------|--------------|
| Two groups, continuous, ~normal | Unpaired t-test (Welch if unequal variance) |
| Two paired conditions | Paired t-test |
| Two groups, non-normal / small n | Mann-Whitney U |
| >2 groups, one factor | One-way ANOVA + post-hoc (Tukey/Dunnett) |
| Two factors (e.g., genotype × treatment) | Two-way ANOVA + correction |
| Tumor growth over time | Mixed-effects / repeated-measures ANOVA (not many t-tests per timepoint) |
| Survival / time-to-event | Kaplan-Meier + log-rank; Cox for covariates |
| Categorical / proportions | Fisher's exact / chi-square |
| Correlation | Pearson (normal) / Spearman (ranked) |
| High-dimensional omics | Model-based (DESeq2/edgeR/limma) with FDR |

Check assumptions (normality, equal variance) and report how. Prefer non-parametric or Welch corrections for small/uneven bench-scale data.

## Multiple comparisons

- Few planned comparisons → Tukey / Dunnett / Holm / Bonferroni.
- Genome-wide / omics → control the **false discovery rate** (Benjamini-Hochberg); report adjusted p / q-values.
- Do not run many pairwise t-tests across groups or timepoints without correction.

## Error bars and reporting

- Define **what every error bar is**: SD, SEM, or 95% CI — in the legend.
- Show data points (dot plots / superplots) rather than bar-only charts when `n` is small.
- Report exact p-values (not just asterisks) where feasible, plus the test and `n`.
- Distinguish biological-replicate variability from technical noise in plots.
- For survival, give hazard ratios with CIs, not p-value alone.

## Checklist

- [ ] `n` defined per panel as biological replicates; one unit specified
- [ ] No pseudo-replication (technical reps not counted as `n`)
- [ ] Test choice matches design; assumptions checked
- [ ] Repeated/longitudinal data analyzed with appropriate model, not serial t-tests
- [ ] Multiple comparisons corrected; FDR for omics
- [ ] Error bars defined (SD/SEM/CI) in every legend
- [ ] Exact p-values, test name, and `n` reported
- [ ] Data points shown for small-n comparisons
- [ ] Statistical software + versions stated (in STAR Methods)

## Anti-patterns

- "n=3" meaning three technical wells of one experiment
- SEM used to make tiny error bars without saying so
- Bar charts hiding 2–3 underlying points
- Multiple t-tests across timepoints/groups, uncorrected
- Asterisks with no test, no `n`, no exact p
- Treating omics features as independent without FDR control


## Statistics pass for Cancer Cell

Use this as a second-pass capability check. First lock the cancer context, mechanism, model system, validation chain, and translational boundary; then test whether the manuscript addresses cancer-biology reviewers who expect mechanistic oncology, translational relevance, and strong multi-modal validation.

- **Primary move:** Check estimand, denominator, uncertainty, multiplicity, missing data, sensitivity, and reporting standard before interpreting any result.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Cell for broader biology, Nature Cancer for oncology breadth, Clinical Cancer Research for clinical translation; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【n definition】biological unit = ...; per-panel n stated? Y/N
【Pseudo-replication risk】none / fix: [...]
【Tests】per analysis: ...
【Multiplicity】correction used: ...
【Error bars】SD/SEM/CI defined in legends? Y/N
【Reporting gaps】exact p / data points / software version
【Next step】cc-figures-tables
```
