---
name: advmat-methods
description: Use when deciding what characterization and experimental detail an Advanced Materials manuscript must show to prove its structure–property claim, and what belongs in the Experimental Section and Supporting Information. Partitions and stress-tests methods; does not design figures or run analysis.
---

# Advanced Materials Methods & Characterization (advmat-methods)

## When to trigger

- Your structure or phase assignment rests on a single technique
- A reviewer of a prior draft asked "how do you know it is this phase / this mechanism?"
- The device metric has no benchmarking against comparable state-of-the-art systems
- The Experimental Section sprawls, or you cannot tell what belongs in the body vs. the SI
- Reproducibility is thin: batch-to-batch spread, synthesis provenance, or statistics are missing

## The multi-technique principle

An Adv. Mater. claim about a material must be **triangulated by complementary techniques**, not asserted from one. A single XRD pattern or one TEM image is rarely enough; referees expect the structure–composition–property picture to close from several independent angles.

A practical characterization matrix (adapt to your material class):

| Claim you are making            | Do not rely on one technique — triangulate with                          |
|---------------------------------|--------------------------------------------------------------------------|
| Crystal structure / phase       | XRD (+ Rietveld) **and** electron diffraction (SAED) / HRTEM lattice     |
| Morphology / size / architecture| SEM **and** TEM (+ statistics over many particles, not one hero image)   |
| Composition / oxidation state   | XPS **and** EDS/EELS mapping **and** ICP-MS/AES for bulk stoichiometry    |
| Local bonding / defects         | Raman / FTIR / XAS (XANES/EXAFS), NMR where applicable                    |
| Optoelectronic property         | UV-vis / PL / TAS + the transport or device measurement it predicts      |
| Electrochemical performance     | CV + galvanostatic cycling + rate/stability data + post-mortem analysis   |

State uncertainties and sample counts. "n = 3 devices, mean ± s.d." beats a single best cell.

## Benchmarking is not optional

Adv. Mater. device claims live or die on **fair comparison to the state of the art**. Put the comparison in the paper, on equal footing:

- Compare against the best *reported* systems for the same function, under comparable conditions — cite them.
- Report the metric with its measurement protocol (scan rate, illumination, active area, humidity) so it is comparable.
- If you claim a record, show a benchmark table or plot (e.g. an efficiency-vs-stability or Ragone-style comparison) rather than a bare number.

## Body vs. Experimental Section vs. Supporting Information

| Detail type                                   | Main text / Experimental Section   | Supporting Information            |
|-----------------------------------------------|------------------------------------|-----------------------------------|
| Core synthesis route + key parameters          | Experimental Section (reproducible)| full optimization sweeps          |
| The decisive characterization proving the claim| main-text figure                   | extended datasets, more samples   |
| Device fabrication + measurement protocol      | Experimental Section               | full protocols, control devices   |
| Benchmarking vs. state of the art              | main text                          | full comparison table + refs      |
| Statistics on the headline metric              | main text (n, mean ± s.d.)         | per-sample data, histograms       |
| Instrument models / settings                   | Experimental Section (concise)     | exhaustive parameters             |

The Experimental Section must let a competent group **reproduce** the material. Detail that is essential-but-bulky (full recipes, calibration, secondary controls) goes to the SI and is cited inline.

## Rigor without bulk

- Pre-empt the leading alternative explanation for your structure/property claim **in the body**, briefly, and point to the SI for the exhaustive checks.
- Report purity/phase fraction, not just "phase-pure" as an adjective.
- Give data-availability and, where relevant, computational details (see `resources/external_tools.md` for the DFT/simulation stack).

## Checklist

- [ ] Every structural/compositional claim is supported by ≥2 complementary techniques
- [ ] Morphology/size claims carry statistics, not a single hero image
- [ ] The headline metric is benchmarked against cited state-of-the-art systems, fairly
- [ ] Device metrics report the full measurement protocol (area, conditions, scan rate)
- [ ] The headline number carries a sample count and spread (n, mean ± s.d.)
- [ ] The Experimental Section is reproducible; bulky detail is in the SI and cited
- [ ] The leading alternative explanation is named and addressed

## Anti-patterns

- A single-technique structure claim ("XRD confirms the phase") with no corroboration
- One flattering TEM/SEM image standing in for a distribution
- A record metric with no benchmarking and no measurement conditions
- Reporting one best device and hiding batch-to-batch variability
- An Experimental Section too vague to reproduce, or so long it belongs in the SI
- "Data available on request" instead of a concrete availability statement

## Output format

```
【Central material claim】...
【Triangulation】technique 1 / technique 2 / technique 3 — sufficient?  yes / add: ...
【Morphology statistics】present?  yes / fix
【Benchmarking vs. SOTA】in main text, fair, cited?  yes / fix
【Metric statistics】n + spread stated?  yes / fix
【Reproducibility】Experimental Section reproducible?  yes / fix
【Next】advmat-figures (characterization figure) or advmat-supplementary (SI partition)
```

> Data-availability, reproducibility, and characterization-reporting expectations evolve — verify current Wiley Advanced Materials policy on the official author page.
