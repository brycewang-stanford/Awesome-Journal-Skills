---
name: epsl-figures-and-tables
description: Use when building figures and tables for an Earth and Planetary Science Letters (EPSL) manuscript. A Letter lives or dies by a few exhibits that a geochemist, seismologist, and geodynamicist can all read — maps with tectonic context, concordia/isochron plots with full error ellipses, model sections with resolution shown. It designs exhibits; it does not run the analysis.
---

# Figures & Tables (epsl-figures-and-tables)

In a letters-format paper the figures *are* the argument: with a main text near 6,500 words (re-check
the cap on the official site), EPSL papers typically carry a small number of dense, layered exhibits
plus a supplement. The venue-specific pressures are cross-disciplinary legibility — your map will be
read by someone who has never worked in that orogen — and uncertainty made visible, because the
sub-fields EPSL serves treat an error-free plot as a red flag.

## When to trigger

- Deciding which few exhibits carry the Letter and what moves to the supplement
- Drafting location maps, cross-sections, isotope plots, tomography slices, or phase diagrams
- A reviewer called an exhibit unreadable, missing context, or missing uncertainties
- Preparing figure files for Editorial Manager upload

## Principles

1. **Ration the slots.** Every main-text figure must advance the argument; reference-quality material
   (all spectra, all sections, parameter sweeps) belongs in the supplementary material.
2. **Context panel first.** Earth-science readers orient spatially: give a location/tectonic-setting
   inset with coordinates, scale, and the geodetic datum or projection named; planetary figures give
   the body, region, and data source (mission/instrument).
3. **Uncertainty is drawn, not asserted.** Error ellipses on concordia, error bars sized to the stated
   σ-level, credible envelopes on age models, damping/resolution shading on inversions.
4. **Sub-field conventions, executed exactly.** Concordia and isochron plots labeled with MSWD and n;
   stratigraphic columns with height and stage boundaries; seismic sections with depth scales and
   vertical exaggeration stated; phase diagrams with the calibration source.
5. **Color that survives review.** Perceptually uniform colormaps for continuous fields (avoid
   rainbow/jet — the geophysics community actively campaigns against it), colorblind-safe categorical
   palettes, grayscale-legible line work; vector formats for line art.
6. **Tables carry data, figures carry claims.** Full analytical tables (every analysis, every
   correction) go to the supplement and repository; the main text carries at most a compact summary
   table.

## Exhibit choices by sub-field

| Result type | The load-bearing exhibit | Non-negotiable elements |
|-------------|--------------------------|--------------------------|
| Geochronology | concordia / weighted-mean plot | ellipses at stated σ, MSWD, n-of-N, excluded grains visible |
| Isotope tracing | covariation (x–y) plot with mixing/evolution curves | endmember values sourced, 2σ bars, sample symbols by group |
| Seismic structure | depth slice + cross-section | colorbar units, resolution overlay, no rainbow |
| Geodynamic model | time-series snapshots + regime diagram | parameter values, dimensionless numbers, benchmark noted |
| Paleo-record | proxy vs age with age model envelope | tie points marked, stage boundaries labeled |
| Planetary | mapped observable + interior model | mission/instrument, datum, uncertainty band |

## Worked micro-example (illustrative — one figure carrying a slab-fluid argument)

The subduction-water Letter needs geochemistry and seismology in one exhibit (illustrative):

- **Panel a:** arc transect map with sample sites, trench, slab-depth contours, and the tomographic
  section line — the seismologist's context and the geochemist's sampling frame in one panel.
- **Panel b:** δ11B vs distance-to-trench with 2σ bars and model curves for shallow vs deep
  dehydration — the discriminating plot.
- **Panel c:** velocity cross-section (perceptually uniform colormap) with the low-velocity conduit
  and a resolution-test inset showing the feature is not smearing.

One three-panel figure replaces three single-discipline figures and makes the joint argument
inspectable at a glance — the letters-format ideal.

## Referee-pushback patterns and the venue-specific fix

- *"Ellipses/error bars missing or undefined."* → Draw them at a stated σ-level on every isotope and
  age plot; define once in the caption.
- *"I can't locate the samples."* → Add the context inset with coordinates, scale, projection.
- *"The colormap manufactures structure."* → Replace jet/rainbow with a perceptually uniform map and
  re-examine which "anomalies" survive.

## Anti-patterns

- A main text bloated with every supporting plot while the one discriminating figure is missing
- Maps without scale, coordinates, or projection; sections without depth units or exaggeration
- Age plots without MSWD, n, or the excluded analyses
- Rainbow colormaps on tomography or gridded fields
- Full 400-row analytical tables typeset in the main text instead of deposited
- Captions that name the panel but not the σ-level, model, or data source

## Output format

```
【Main exhibits】list + the claim each carries
【Context】location/setting panel with datum + scale? [Y/N]
【Uncertainty drawn】ellipses/bars/envelopes at stated σ? [Y/N]
【Conventions】sub-field norms met (MSWD, resolution overlay, ...)? [Y/N]
【Color/format】perceptually uniform + colorblind-safe + vector? [Y/N]
【Main vs supplement】split decided
【Next】epsl-reporting-and-reproducibility
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — GMT/PyGMT, GPlates, ObsPy, IsoplotR plotting
- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — how exhibits pair with a Letter's prose
