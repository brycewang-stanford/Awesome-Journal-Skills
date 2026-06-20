---
name: earth-system-science-data
description: Use when targeting Earth System Science Data (ESSD) or deciding whether an earth-system dataset fits this venue. Encodes the journal's data-paper fit, the open-deposition-with-DOI requirement, quality and reuse-documentation bar, Copernicus house style, official-submission re-check, and desk-reject heuristics.
---

# Earth System Science Data (earth-system-science-data)

## Journal positioning

Earth System Science Data (ESSD) is the Copernicus / European Geosciences Union venue for
**data papers**: peer-reviewed articles whose primary product is an original, high-quality,
openly deposited dataset of lasting value to earth-system science. The defining expectation
is not a new scientific conclusion but a **reusable dataset**: the manuscript documents how
the data were produced, calibrated, quality-controlled, and how others should reuse them,
while the dataset itself lives in a FAIR public repository with its own persistent
identifier (DOI). An analysis or interpretation paper that mines data toward a hypothesis,
or a paper whose data are not openly and permanently available, is a fundamental misfit
here. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the
journal's current author guidance. Before submitting, re-check the live ESSD / Copernicus
author instructions and data policy.

## When to trigger

- The author has produced an original dataset (observations, reanalysis, compilation, model
  output) and wants to publish it as a citable data paper rather than a research article.
- A measurement campaign or long-term record needs a venue that rewards the data product
  itself, separate from any later analysis paper.
- The author is choosing between ESSD as a data paper and a domain journal (e.g.
  `water-resources-research`, `global-biogeochemical-cycles`) for an analysis paper.
- The author needs ESSD's open-deposition-with-DOI requirement and quality/reuse
  documentation bar.

## Scope & topic fit

- Original observational datasets across the earth system: atmosphere, ocean, land surface,
  cryosphere, biosphere, solid earth, and human–environment interfaces.
- Long-term monitoring records, field/campaign measurements, and instrument or station
  networks with documented provenance.
- Harmonized compilations and syntheses that merge heterogeneous sources into a single
  consistent, value-added product.
- Gridded products, reanalyses, and model output of broad reuse value, with versioning and
  uncertainty information.
- Remote-sensing and retrieval datasets with algorithm description, validation, and quality
  flags.
- Methodologically novel data-processing or quality-control workflows when the resulting
  dataset is the deliverable.

## Method & evidence bar

- The dataset must be **original and reusable**, not a re-packaging of an already-published
  product; novelty lies in the data, not in an interpretation.
- The data must be **openly deposited in a FAIR repository with a persistent DOI** before
  acceptance; a "data available on request" statement does not satisfy the journal.
- Production must be fully documented: instruments, sampling, calibration, processing chain,
  versioning, and the exact contents and format of the deposited files.
- Quality must be demonstrated with quantitative quality control, validation against
  independent references where possible, and explicit, traceable uncertainty.
- Reuse must be enabled: clear metadata, variable definitions, units, flags, file structure,
  and guidance on appropriate and inappropriate uses.
- The dataset's value and the user community it serves should be argued concretely, not
  asserted.

## Structure & house style

- Copernicus data-paper format; the manuscript and the deposited dataset are reviewed
  together — re-check current article types and structure on the live guide.
- The text must describe data generation and documentation, not advance a scientific
  hypothesis; interpretation belongs in a companion analysis paper elsewhere.
- A prominent **data availability statement** must give the repository, DOI, version, and
  license; the DOI must resolve to the actual data.
- Figures and tables should characterize the dataset (coverage maps, time–space sampling,
  validation scatter, uncertainty, flag distributions), not argue a result.
- Open-access, open-review, and open-data are the norm; the deposited files must match what
  the paper describes exactly.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Copernicus/ESSD anchors, then
  cite the current ESSD page you checked.
- Search the live site for "Earth System Science Data author guidelines" and follow the
  current Copernicus version.
- Confirm the dataset is deposited in an **approved FAIR repository with a resolving DOI,
  version, and an open license**, and that the deposited files match the manuscript.
- Re-check the data-paper structure, abstract/format expectations, and any required dataset
  metadata or repository criteria.
- Re-check open-access terms, interactive open-review procedure, competing-interests,
  funding, author-contribution, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The deliverable is a reusable dataset, not an analysis/interpretation paper.
- [ ] The data are deposited in a FAIR repository with a resolving DOI, version, and open license.
- [ ] Production, calibration, processing, and file contents are fully documented.
- [ ] Quality is shown with quantitative QC, validation, and traceable uncertainty.
- [ ] Metadata, variable definitions, units, and flags enable independent reuse.
- [ ] The deposited files exactly match what the manuscript describes.

## Common desk-reject triggers

- An analysis/interpretation paper submitted as if it were a data paper.
- A dataset that is not openly available with a resolving DOI, or is "available on request."
- Re-packaging of an already-published dataset with no original, value-added product.
- Insufficient documentation of production, quality control, or uncertainty.
- Metadata too sparse for independent reuse (missing units, flags, or variable definitions).
- A mismatch between the deposited files and the dataset described in the manuscript.

## Re-routing decision

- The dataset underpins a scientific conclusion → an analysis venue such as
  `communications-earth-and-environment` or a domain journal, with ESSD as the data citation.
- Carbon/nutrient flux data feeding a budget analysis → `global-biogeochemical-cycles`.
- Hydrologic data feeding a process/method study → `water-resources-research` / `journal-of-hydrology`.
- Climate model/reanalysis output used for a climate-science argument → `journal-of-climate`.
- Solid-earth/geochemical data interpreted as a process result → `earth-and-planetary-science-letters`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Earth System Science Data
[Data product] <what the dataset is and what community reuses it>
[Deposition] <repository + DOI + version + license status>
[Quality/documentation] <does QC + validation + metadata clear ESSD's reuse bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <data-paper structure / FAIR deposition / metadata / open-review / disclosures>
[Re-route suggestion] <if it is an analysis paper, a better-matched venue>
```
