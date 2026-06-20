---
name: en-engtech-journal-workflow
description: Use when deciding which English engineering / technology journal skill to invoke next, comparing fit across the 40-journal engineering roadmap, or routing a manuscript before venue-specific re-framing. Routes by engineering sub-discipline, contribution type (theory vs. method vs. system vs. device), and validation shape (proof / simulation / bench experiment / field deployment).
---

# Engineering & technology journal workflow (en-engtech-journal-workflow)

## Purpose

This is the routing skill for the engineering bundle. It does not replace a
single-journal profile; it first classifies the manuscript by **engineering
sub-discipline, contribution type, and validation shape**, then routes into the
matching per-journal skill for fit and re-framing. It is a sibling to
`en-natsci-journal-workflow` (natural science) and `en-journal-workflow`
(econ/finance/management).

## Ask four things first

1. **Sub-discipline:** electrical/EECS, control, communications/information theory,
   signal processing, power/energy systems, robotics, photonics/optics, electronics
   devices, biomedical engineering, mechanics/solids, fluids, manufacturing,
   aerospace, chemical/process engineering, energy conversion/storage, materials
   engineering, or civil/transportation?
2. **Contribution type:** a theorem/bound, a new algorithm/method, a system or
   architecture, a device/material with measured performance, a tutorial/survey, or
   a design methodology?
3. **Validation shape:** mathematical proof, numerical simulation, controlled bench
   experiment, hardware prototype, pilot/field deployment, or standardized
   materials/mechanical testing?
4. **Audience breadth:** the whole field (Proceedings of the IEEE, a Nature
   Portfolio engineering title), a sub-discipline community (an IEEE Transactions,
   Automatica, JFM, Acta Materialia), or a specialty niche?

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| Authoritative tutorial / scanning-the-field review (EE/CS) | `proceedings-of-the-ieee` |
| Control theory, stability, optimal/robust/adaptive control | `ieee-transactions-on-automatic-control` / `automatica` |
| Coding, capacity, information-theoretic bound | `ieee-transactions-on-information-theory` |
| Estimation, detection, sampling, array/statistical signal processing | `ieee-transactions-on-signal-processing` |
| Communication systems, protocols, networks | `ieee-transactions-on-communications` / `ieee-transactions-on-wireless-communications` / `ieee-journal-on-selected-areas-in-communications` |
| Power electronics / converters / drives | `ieee-transactions-on-power-electronics` / `ieee-transactions-on-industrial-electronics` |
| Power grid, electricity markets, system operation | `ieee-transactions-on-power-systems` |
| Antennas, propagation, electromagnetics | `ieee-transactions-on-antennas-and-propagation` |
| Robot design, planning, control, manipulation | `ieee-transactions-on-robotics` / `the-international-journal-of-robotics-research` |
| Medical imaging reconstruction / analysis | `ieee-transactions-on-medical-imaging` |
| Biomedical devices, signals, instrumentation | `ieee-transactions-on-biomedical-engineering` / `nature-biomedical-engineering` |
| Photonics device / optical method, broad + high impact | `optica` / `light-science-and-applications` |
| Authoritative photonics review | `laser-and-photonics-reviews` |
| New electronic device / circuit concept, broad significance | `nature-electronics` |
| Implantable / regenerative / drug-delivery materials | `biomaterials` |
| Structural alloys / processing–microstructure | `acta-materialia` |
| Solid mechanics, fracture, constitutive theory | `journal-of-the-mechanics-and-physics-of-solids` / `international-journal-of-plasticity` |
| Fundamental fluid mechanics | `journal-of-fluid-mechanics` |
| Machining, forming, precision manufacturing | `international-journal-of-machine-tools-and-manufacture` |
| Additive manufacturing process–structure–property | `additive-manufacturing` |
| Composite materials / structures | `composites-part-b-engineering` |
| Aerospace systems review | `progress-in-aerospace-sciences` |
| Chemical/process engineering fundamentals | `aiche-journal` / `chemical-engineering-journal` |
| Combustion / energy-conversion fundamentals review | `progress-in-energy-and-combustion-science` |
| Membranes / separations | `journal-of-membrane-science` |
| Systems-level energy analysis, integration, decarbonization | `applied-energy` |
| Batteries / fuel cells / electrochemical power | `journal-of-power-sources` / `energy-storage-materials` |
| Authoritative materials review | `progress-in-materials-science` |
| Transportation/network methodology, theory | `transportation-research-part-b-methodological` |
| Concrete / cementitious materials science | `cement-and-concrete-research` |

## Sibling-journal disambiguation

| Confusable targets | Decision rule |
|---|---|
| `ieee-transactions-on-automatic-control` vs `automatica` | Both are top control venues; TAC leans toward rigorous theory and shorter technical notes, Automatica toward methodological breadth — route by the form of the main result and re-check current scopes. |
| `ieee-transactions-on-robotics` vs `the-international-journal-of-robotics-research` | T-RO favors complete, validated robotics contributions; IJRR favors longer, conceptually framed archival work — route by contribution length and framing. |
| `optica` vs `light-science-and-applications` | Both are high-impact photonics; decide whether the advance is best framed for the Optica/OSA optics community or the Nature Portfolio breadth audience. |
| Nature-Portfolio engineering (`nature-electronics`/`nature-biomedical-engineering`) vs IEEE Transactions | Nature titles need field-changing significance and broad framing; a complete, rigorous specialty result routes to the matching IEEE Transactions. |
| `acta-materialia` vs the materials/energy titles in the natural-science bundle (`advanced-materials`, `nature-materials`) | Route structural/processing metallurgy to Acta Materialia; conceptual functional-materials advances to the Nature/Advanced family. |
| `applied-energy` vs `journal-of-power-sources`/`energy-storage-materials` | Systems-level energy integration → Applied Energy; device-level electrochemical power/storage → the power-source/storage titles. |

## Decision rules

- **Name the engineering contribution.** "We built/measured X" is not a contribution
  unless it advances a method, a bound, a design principle, or a performance frontier
  with a reproducible margin over the right baseline.
- **Baseline and benchmark discipline.** Performance claims need comparison to the
  current state of the art under stated, reproducible conditions — not to a strawman.
- **Theory vs. system.** A theorem/bound, a method with guarantees, and a deployed
  system are different products; pick the reviewer community that evaluates the main
  claim.
- **Survey/tutorial venues are mostly invited or scoped** (Proceedings of the IEEE,
  Progress in Materials Science / Aerospace Sciences / Energy and Combustion
  Science) — do not route an unsolicited primary-data paper there without checking
  scope.
- **Reproducibility/data/code** expectations are now standard in engineering — a
  results paper without enough to reproduce the key claim is a common reject.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Biggest current gap] contribution-clarity / baseline / validation / reproducibility / formatting / official requirements
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
