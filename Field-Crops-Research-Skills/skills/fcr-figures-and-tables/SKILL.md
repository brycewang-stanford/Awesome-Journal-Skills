---
name: fcr-figures-and-tables
description: Use when building tables and figures for a Field Crops Research (FCR) manuscript so exhibits are self-contained, quantitatively complete, and agronomically informative — yield and response curves, AMMI/GGE biplots, observed-vs-simulated plots, and weather-vs-phenology series. FCR exhibits must show units, error (SED/LSD), and sample structure. Designs exhibits; it does not run the analysis.
---

# Figures & Tables (fcr-figures-and-tables)

Exhibits are where an agronomy reviewer checks whether the result is real and general. At FCR every
exhibit must be **self-contained** and **quantitatively complete**: units, sample/replication, and a
measure of **error or variability** (SE, **SED, or LSD**) belong on the exhibit itself.

## When to trigger

- Designing the main results table/figure or a key descriptive exhibit
- Deciding what belongs in the article vs. supplementary material
- A reviewer found an exhibit unclear, mislabeled, or missing error/units
- Presenting G×E, response curves, or model evaluation

## Principles

1. **Self-contained.** A reader should understand each exhibit from its caption, axis/column labels,
   and footnote alone. State the **crop, cultivar(s), environments (sites×seasons), N/replication,
   units (SI)**, and what the value is (mean? adjusted mean?).
2. **Show the error.** Yield and treatment means need **SED or LSD** (with α and df) or error bars
   defined in the caption — never bare means. For curves, show fitted line + CI and the data.
3. **Right exhibit for the question.** Use a **response curve** for quantitative factors (N, water,
   density); an **AMMI/GGE biplot** or Finlay–Wilkinson plot for G×E; **observed-vs-simulated with the
   1:1 line** for model evaluation; **time series vs. thermal time/phenology** with weather overlays
   for development.
4. **Accessible.** Colourblind-safe palettes; legible in **grayscale**; no chartjunk, no 3D, no
   needless colour. Vector output (PDF/EPS) for print.
5. **Reproducible & consistent.** Numbers match the analysis script and the deposited data; table and
   figure values are internally consistent and consistent with the text.

## Agronomy-specific exhibits

- Yield-gap / boundary-line plots; nitrogen- and water-response curves with fitted models.
- AMMI biplots, GGE biplots, Finlay–Wilkinson stability regressions for multi-environment data.
- Weather (rainfall, temperature, radiation) shown **against crop phenology** (sowing, anthesis, maturity).
- Maps where spatial/regional variation is the point; observed-vs-simulated panels for modelling.

## Anti-patterns

- Means with no SED/LSD, error bars, or units
- Mean-separation letters on a quantitative dose where a response curve is appropriate
- Tables that need the prose to be intelligible (not self-contained)
- Colour-only encoding that fails in grayscale or for colourblind readers
- Exhibit values that don't match the analysis output or the data deposit

## Output format

```
【Main exhibit】what it shows + why this exhibit type
【Self-contained?】caption + labels + crop/cultivar + envs + N + units present? [Y/N]
【Error shown?】SED / LSD / CI with α stated? [Y/N]
【Accessible?】grayscale-legible + colourblind-safe? [Y/N]
【Article vs supplement】split decided
【Reproducible?】matches analysis output + data deposit? [Y/N]
【Next】fcr-reporting-and-data-policy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting and G×E-biplot tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reporting expectations (units, weather vs. phenology)
