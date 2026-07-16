---
name: epsl-literature-positioning
description: Use when positioning an Earth and Planetary Science Letters (EPSL) manuscript against prior work. EPSL's readership spans geochemistry, geophysics, geodynamics, geochronology and planetary science, so the knowledge gap must be framed across sub-fields and against the frontier, not inside one method community. It frames the gap and citations; it does not fabricate references.
---

# Literature Positioning (epsl-literature-positioning)

An EPSL paper is typically refereed by specialists from *different* sub-fields — a geochemist and a
geodynamicist, or a seismologist and a mineral physicist. Positioning that only cites your own method
community reads as parochial to the other reviewer, and positioning that ignores what the adjacent
community already established reads as naive. This skill builds the cross-disciplinary gap statement
that survives both.

## When to trigger

- Writing the introduction's "what is known / what is missing" arc
- A reviewer wrote "the authors seem unaware of the geophysical (or geochemical) constraints"
- Checking whether the claimed gap is already closed in an adjacent literature
- Preparing an invited Frontiers Paper that must map an entire frontier

## How to position for EPSL

1. **State the gap as a competing-hypothesis problem.** "Models A and B predict opposite signs for
   [observable]; existing data cannot distinguish them" beats "few studies have examined region X."
2. **Triangulate across observables.** Show what isotopes, seismology, experiments, and dynamical
   models each say about the process — and precisely where they disagree. EPSL papers often live at
   these intersections.
3. **Cite the frontier, including EPSL's own record.** The journal has carried many of the defining
   papers in mantle geochemistry, geochronology, and geodynamics since 1966; reviewers notice when the
   canonical constraint (often an EPSL paper) is missing.
4. **Date-stamp the constraints.** Decay constants, reference frames, and velocity models get revised;
   position against the *current* values, and say which calibration you adopt.
5. **Differentiate quantitatively.** "Our 2σ precision of ±0.15‰ (illustrative) resolves the ~0.3‰
   difference the debate turns on" is a positioning sentence, not a methods sentence.

## Which literatures the paired reviewers expect you to engage

| If your contribution is... | You must also engage... | Reviewer who flags the omission |
|----------------------------|--------------------------|----------------------------------|
| An isotopic tracer of a mantle/crust process | the dynamical models the tracer tests | the geodynamicist |
| A tomographic or seismic-structure result | the mineral-physics and petrology constraints on interpretation | the experimentalist |
| A geochronology-based rate | the stratigraphic/astrochronologic framework it must fit | the stratigrapher |
| A planetary-interior claim | mission data (gravity, seismic, magnetic) and cosmochemistry | the planetary scientist |
| A paleomagnetic or rock-record result | the geochronology anchoring the record | the geochronologist |

## Worked micro-example (illustrative — positioning a water-in-the-mantle paper)

Suppose the paper reports electrical-conductivity anomalies interpreted as hydrated transition-zone
mantle. Weak positioning cites only the magnetotelluric literature and claims "the transition zone's
water content is debated." The EPSL-grade version (illustrative):

- **Known:** mineral-physics experiments allow wadsleyite to store weight-percent-level water; some
  seismic discontinuity studies and inclusion finds support local hydration.
- **Disagreement:** conductivity-based and seismic-based water estimates for the same region differ
  by an order of magnitude, and lab calibrations disagree on the conductivity–water law.
- **This paper closes it by:** jointly inverting conductivity and discontinuity topography under both
  calibrations, showing only a hydrated layer under one plate is consistent with all datasets.

The lift comes from placing the paper at the intersection of three literatures and naming the
calibration choice on which the debate has actually turned.

## Referee-pushback patterns and the venue-specific fix

- *"The gap is regional, not conceptual."* → Restate what unresolved process question the region
  merely *samples*; cite the global debate the result feeds.
- *"Ignores the adjacent constraint."* → Add the geophysics/geochemistry/experimental leg you skipped;
  EPSL's paired-reviewer model makes this omission expensive.
- *"Positioning rests on superseded values."* → Update to current decay constants / reference models
  and state the choice explicitly.

## Anti-patterns

- An introduction that tours one region's history instead of a process debate
- Citing only your method community when the claim crosses into another's territory
- "Poorly understood" or "controversial" with no named hypotheses in tension
- Missing the canonical EPSL constraint every referee in the sub-field knows by author and year
- A "first ever" claim that a five-minute scan of GCA, JGR, or Nature Geoscience would defeat

## Output format

```
【Known】2–3 lines, spanning the relevant observables
【In tension】the hypotheses/datasets that disagree, with names
【Gap】the discriminating measurement or model nobody has made
【This paper closes it by】the quantitative advance
【Literatures engaged】geochem / geophys / geochron / experiments / planetary (which apply)
【Next】epsl-study-design
```

## Supplementary resources

- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — how landmark EPSL papers framed their gaps
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference databases (GEOROC, EarthChem, IRIS) for scanning the constraint landscape
