---
name: aaag-data-analysis
description: Use when running and reporting the analysis for an Annals of the American Association of Geographers manuscript — spatial statistics and modeling, remote-sensing accuracy, or qualitative coding and interpretation. Sets analysis and reporting norms across the four areas; it does not choose the design.
---

# Data Analysis (aaag-data-analysis)

The Annals expects analyses that are **spatially honest** and reported with uncertainty, whatever the
area. The standard is that a competent reader in the area could follow the logic from data to claim and
see that the geography of the data was respected, not flattened.

## When to trigger

- Estimating models, running spatial statistics, classifying imagery, or coding qualitative material
- A reviewer questioned uncertainty, robustness, spatial autocorrelation, accuracy, or interpretation
- Preparing the results section and deciding what to report

## Spatial / quantitative
- **Diagnose space first.** Report spatial autocorrelation in residuals; if present, move to a spatial
  model (lag/error, GWR/MGWR, spatial regimes) and say why.
- **Uncertainty everywhere.** CIs/SEs (spatially robust where needed), not stars alone; for prediction,
  out-of-sample error from **spatial/blocked CV**.
- **Robustness.** Re-estimate across plausible **areal units and bandwidths** (MAUP/scale sensitivity);
  show the result is not a unit artifact. Report effect sizes in interpretable units.

## Remote sensing / physical
- **Accuracy with an independent sample.** Confusion matrix, overall/producer/user accuracy, kappa or
  F1; for continuous outputs, RMSE/MAE and bias; map the **spatial pattern of error**, not just a scalar.
- **Propagate uncertainty** from inputs through to the reported quantity; state the validation design.

## Qualitative / interpretive
- **Transparent analytic trail.** Coding scheme, how themes were derived, and how interpretations were
  checked (negative cases, member checks, triangulation) — credibility over counting.
- **Evidence-to-claim mapping.** Each interpretive claim is tied to identifiable (anonymized) evidence;
  avoid quote-mining that over-generalizes from one informant.

## Mixed methods
- **Show the integration.** State where the strands converge and where they conflict, and how the
  conflict was adjudicated — do not report two parallel analyses and call it mixed methods.

## Cross-cutting reporting bar

- Match every claim in the text to an exhibit or statistic; no orphan assertions.
- Report **negative / null / scale-dependent** results honestly; geography rewards scope conditions.
- Keep analysis reproducible: master script, seeds, pinned versions (see `aaag-transparency-and-data`).

## Referee pushback → Annals-specific fix

- *"Are these effects just spatial autocorrelation?"* → Show residual Moran's I before/after a spatial
  model; report the spatial-error structure, not only a global coefficient.
- *"Would the result change at a different scale/unit?"* → Provide a MAUP/bandwidth sensitivity panel
  and state the scale at which the claim holds.
- *"How accurate is the map?"* → Area-adjusted accuracy from an independent sample + a map of where
  error concentrates, not a single kappa.
- *"How do I know the qualitative reading isn't cherry-picked?"* → Coding scheme, negative cases, and an
  excerpt-to-claim table.

## Calibration anchors

- **Uncertainty is mandatory, not optional.** A coefficient or accuracy number without an interval is
  not yet a finding at this venue.
- **Scale dependence is a result, not a nuisance.** If the answer changes with the unit, say so — that
  is geographic knowledge.
- **The spatial pattern of error is itself a finding** for remote-sensing and prediction work.

## Checklist

- [ ] Spatial autocorrelation diagnosed and addressed (quant)
- [ ] Uncertainty reported (CIs/SEs; out-of-sample error via spatial CV where relevant)
- [ ] MAUP/scale or bandwidth sensitivity shown (quant)
- [ ] Accuracy via independent validation + spatial error map (RS)
- [ ] Coding scheme + evidence-to-claim trail (qual); integration shown (mixed)
- [ ] Every textual claim maps to an exhibit/statistic

## Anti-patterns

- Reporting OLS on spatial data with no autocorrelation check
- Stars-only tables with no effect sizes or CIs
- A single global accuracy number with no spatial error map
- Cherry-picked quotes standing in for an analytic trail
- "Mixed methods" that never integrate the strands

## Output format

```
【Mode】spatial-quant / remote-sensing / qualitative / mixed
【Headline result】effect/accuracy/theme + its uncertainty
【Spatial honesty】autocorrelation / MAUP / spatial-CV / spatial error map handled? [Y/N]
【Robustness】checks run and what held
【Reproducibility】master script + seeds + versions? [Y/N]
【Next】aaag-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — spatial-stats, RS, and qualitative-analysis packages
- [`../../resources/README.md`](../../resources/README.md) — shared reporting-standards background (inference, robustness)
