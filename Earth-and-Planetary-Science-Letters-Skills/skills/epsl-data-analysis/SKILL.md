---
name: epsl-data-analysis
description: Use when reducing and reporting data for an Earth and Planetary Science Letters (EPSL) manuscript — full analytical-uncertainty budgets for isotope and geochronology data, defensible statistics (MSWD, weighted means, Bayesian age models), and inversion/model diagnostics. It guides reduction and reporting norms; it does not fabricate results.
---

# Data Analysis (epsl-data-analysis)

EPSL's methods-transparency culture is strictest exactly where the journal is strongest: isotope
geochemistry and geochronology. Reviewers expect every headline number to arrive with its complete
error budget — internal precision, external reproducibility, standard and blank corrections, and
systematic terms like decay-constant uncertainty — and they expect model results to arrive with their
resolution limits. Design choices live in `epsl-study-design`; deposition and supplements in
`epsl-reporting-and-reproducibility`.

## When to trigger

- Reducing isotope, geochronologic, elemental, or geophysical data to reportable results
- Deciding which uncertainty terms to propagate and how to quote them
- Computing weighted means, isochrons, concordia intercepts, or Bayesian age–depth models
- A reviewer asked for the error budget, the MSWD, or a resolution test

## Reporting norms EPSL expects

1. **State the full uncertainty ladder.** Quote internal (within-run) precision, external
   reproducibility from repeat standards/replicates, and — when comparing across methods or to other
   studies — systematic terms (decay constants, tracer calibration, spectrometer bias). Say which
   ladder rung each quoted ±X σ includes, and whether σ means 1σ, 2σ, or 95% CI.
2. **Anchor to community values.** Name the reference materials with the values used, the
   normalization scheme (e.g., what δ is measured against), and the decay constants adopted, with
   citations — so the numbers remain comparable when calibrations shift.
3. **Statistics that match geochemical data.** Weighted means with MSWD reported and *interpreted*
   (MSWD ≫ 1 means scatter beyond analytical error — say why); isochrons with the regression model
   named; mixtures and outliers handled by a stated rule, not silent deletion.
4. **Age models with honest priors.** Bayesian age–depth or eruption-tempo models report priors,
   convergence, and sensitivity to them; deposit the model input/config.
5. **Inversions come with diagnostics.** Resolution/recovery tests, misfit and trade-off curves, and
   an explicit statement of what the data cannot see; never present a smoothed model as if it were data.
6. **Blanks and detection.** Report total procedural blanks and their variability; state how
   blank-sensitive results (small samples, young ages, low abundances) respond to the blank range.

## Uncertainty-reporting table reviewers work down

| Element | What to report | If omitted, the reviewer assumes |
|---------|----------------|----------------------------------|
| σ-level and type | 1σ/2σ/95% CI; internal vs external | numbers are not comparable |
| Reference materials | measured vs accepted values, per session | accuracy unverified |
| Blanks | magnitude + variability + correction | small samples untrustworthy |
| Decay constants / tracer | which values, cited | ages not portable across studies |
| MSWD / goodness of fit | value + interpretation | scatter hidden in the mean |
| Model resolution | recovery tests, trade-offs | structure may be artifact |

## Worked micro-example (illustrative — a weighted-mean age that survives review)

Twelve single-zircon U-Pb analyses from one ash bed (illustrative numbers):

- Ten young analyses give a weighted mean of 66.021 ± 0.024 Ma (2σ, analytical only), MSWD = 1.3 —
  scatter consistent with analytical error, so a single population is defensible.
- Two older grains are excluded as inherited *by a pre-stated criterion* (resolvably older than the
  main cluster), and shown in the figure anyway.
- Reported as: "66.021 ± 0.024/0.031/0.075 Ma (2σ: analytical / +tracer / +decay constants), MSWD 1.3,
  n = 10/12" — the three-tier bracket lets a reader compare against Ar-Ar or astrochronologic ages
  without emailing the authors.

The habit that prevents most queries: every mean is accompanied by its MSWD, its n-of-N, and a plot
showing the excluded analyses.

## Referee-pushback patterns and the venue-specific fix

- *"Uncertainties are quoted but not defined."* → State σ-level, and split analytical vs systematic
  terms wherever the result is compared to external ages or data.
- *"MSWD indicates overdispersion."* → Do not just widen errors; identify the geological or analytical
  source of scatter and let the interpretation absorb it.
- *"The anomaly is at the edge of resolution."* → Show the recovery test at that node; soften or drop
  claims the test cannot support.

## Anti-patterns

- A headline age or rate with a bare ± and no statement of what it includes
- Standards measured but never reported against accepted values
- Outlier analyses removed without a stated rule or a visible plot
- MSWD omitted, or quoted without interpretation
- Tomographic/model features discussed where resolution tests show smearing
- Comparing your ages to literature ages without harmonizing decay constants

## Output format

```
【Headline number】value ± (σ-level; analytical/+systematic) + units + n
【Traceability】standards vs accepted values; blanks; constants cited
【Statistics】weighted mean/isochron/Bayesian model + MSWD/diagnostics
【Exclusions】rule stated + shown in figures? [Y/N]
【Model diagnostics】resolution/sensitivity reported? [Y/N or N/A]
【Next】epsl-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — IsoplotR, ET_Redux, iolite, ObsPy, inversion codes
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — methods-transparency and data expectations
