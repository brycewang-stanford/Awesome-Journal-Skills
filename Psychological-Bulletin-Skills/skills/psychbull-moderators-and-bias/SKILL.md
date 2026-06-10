---
name: psychbull-moderators-and-bias
description: Use when explaining heterogeneity and probing robustness in a Psychological Bulletin meta-analysis — moderator/subgroup analysis, meta-regression, and publication-bias diagnostics (funnel, Egger, trim-and-fill, PET-PEESE, p-curve, selection models) plus sensitivity analyses. Extends the core model; estimation lives in psychbull-meta-analysis-methods.
---

# Moderators & Publication Bias (psychbull-moderators-and-bias)

Once a pooled effect and its heterogeneity exist, two questions decide the paper's credibility: **what
explains the variation** (moderators), and **is the effect an artifact of selective reporting**
(publication bias). Psychological Bulletin reviewers scrutinize both, and **MARS** requires reporting
bias assessment. This skill extends the core model in `psychbull-meta-analysis-methods`.

## When to trigger

- Testing pre-specified moderators / meta-regression to explain heterogeneity
- Running publication-bias diagnostics
- A reviewer asks for sensitivity / robustness analyses
- Reconciling conflicting signals across bias tests

## Moderators & meta-regression

- **Pre-specify** moderators in the protocol; treat unplanned ones as **exploratory** and label them.
- Use **mixed-effects meta-regression** (categorical subgroups and continuous moderators); report the
  moderator coefficient, its CI, **residual heterogeneity**, and **R² analog** (variance explained).
- Beware **ecological/aggregation** bias (study-level moderators ≠ individual-level), **multiple
  testing** across many moderators, and **confounded** moderators; interpret cautiously.

## Publication-bias diagnostics (run several, not one)

1. **Funnel plot** (with contour enhancement) — visual asymmetry; not proof on its own.
2. **Egger's regression** / rank tests — small-study effects, with the usual caveats under high
   heterogeneity.
3. **Trim-and-fill** — imputes "missing" studies; treat as sensitivity, not truth.
4. **PET-PEESE** — regression-based bias-adjusted estimate.
5. **p-curve / p-uniform** — evidential value and right-skew vs. p-hacking signatures.
6. **Three-parameter selection models** (`weightr`) — model the selection process directly.

No single test is decisive; **converging evidence** across methods is the standard, and all are weak
under strong heterogeneity — say so.

## Sensitivity & robustness

- **Leave-one-out** and influence/outlier diagnostics; refit without high-leverage studies.
- Sensitivity to **effect-size metric**, **model** (RVE vs. multilevel), and **inclusion borderline**.
- Subset by **study quality / risk of bias**; published vs. grey literature.

## Anti-patterns

- Mining dozens of moderators and theorizing the one that hits (HARKing); no multiple-testing caution
- A single bias test reported as if it settled the question
- Trim-and-fill or PET-PEESE reported as the "true" effect rather than a sensitivity bound
- Ignoring that bias diagnostics behave poorly under high heterogeneity
- Subgroup claims from tiny k (few studies per cell)

## What Psychological Bulletin referees demand here

The APA's flagship review journal treats moderator and bias work as the place where a competent
meta-analysis either earns trust or collapses. Referees at this venue apply a recognizable bar:

| Referee expectation | Pass | Desk-reject / major-revision trigger |
|---------------------|------|--------------------------------------|
| Moderators pre-registered | Listed in protocol, confirmatory vs. exploratory labeled | Moderators appear only in Results, none in the protocol — read as fishing |
| Multiple bias diagnostics | Funnel + Egger + selection model + PET-PEESE converge | One funnel plot, eyeballed, called "no evidence of bias" |
| Bias caveats under heterogeneity | States that diagnostics weaken when I² is high | Egger taken at face value with I² = 75% |
| Subgroup k disclosed | k per cell reported; thin cells flagged | A moderator "effect" rests on a cell of k = 3 |
| Sensitivity breadth | Leave-one-out + metric + model + quality subsets | A single estimate, no robustness at all |

## Worked vignette — bias and moderators on an intervention synthesis

*Illustrative numbers only — not real data.* A random-effects synthesis of a self-affirmation
intervention pools k = 42 effects, g = 0.34, 95% CI [0.24, 0.44], I² = 68%, τ² = 0.041. The
moderator/bias pass under this skill's rules:

- **Pre-specified moderator** (delivery format, 3 levels): mixed-effects meta-regression gives an
  R²-analog of 0.22; residual I² drops to 51%. Confirmatory, so it carries theoretical weight.
- **Exploratory moderator** (publication year): tested but labeled exploratory; the slope is null and
  reported as such, not spun.
- **Bias diagnostics run together**: funnel asymmetry is visible; Egger p = 0.03; trim-and-fill adds 6
  imputed studies and shifts g to 0.27 (a sensitivity bound, not "the truth"); a three-parameter
  selection model lands g ≈ 0.25; PET-PEESE gives 0.21. Convergence says the effect is real but likely
  inflated, so the abstract reports the range, not the rosy 0.34.
- **Sensitivity**: leave-one-out moves g within [0.31, 0.36]; restricting to low-risk-of-bias studies
  (k = 19) gives 0.29. The bottom line is hedged accordingly.

## Referee pushback → venue-specific fix

- *"Your moderators look post-hoc."* → Cite the protocol; relabel any unplanned moderator as
  exploratory.
- *"A single funnel plot is not a bias analysis."* → Add Egger, a selection model, and PET-PEESE; report
  convergence and the heterogeneity caveat.
- *"Subgroup claim rests on too few studies."* → Disclose k per cell; down-weight thin-cell claims.

## Output format

```
【Moderators】pre-specified vs exploratory; meta-regression coef + CI + R²
【Residual heterogeneity】after moderators
【Bias diagnostics】funnel / Egger / trim-fill / PET-PEESE / p-curve / selection — converge? 
【Sensitivity】leave-one-out, metric, model, quality subsets
【Bottom line】is the effect robust? [statement]
【Next】psychbull-theory-integration
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `metafor`, `dmetar` (PET-PEESE), `weightr`, `puniform`, p-curve
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MARS bias-assessment reporting
