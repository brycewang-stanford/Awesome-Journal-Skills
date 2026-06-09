---
name: the-astronomical-journal
description: Use when targeting The Astronomical Journal (AJ) or deciding whether an observational astronomy manuscript fits this AAS/IOP venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Astronomical Journal (the-astronomical-journal)

## Journal positioning

AJ is published by IOP Publishing on behalf of the American Astronomical Society (AAS) and is, with The Astrophysical Journal (ApJ), one of the two AAS research journals. Its defining character is an observational and data-centric scope that is broader on the empirical side than its sister ApJ: AJ is the natural home for surveys, catalogs, instrumentation and observing-technique papers, solar-system studies, and exoplanet detection and characterization — work where the measurement, the data product, and the methodology are the primary contribution. Where ApJ leans toward astrophysical interpretation and theory, AJ leans toward the observations and the data themselves, though the two overlap substantially. AJ rewards careful, well-calibrated measurements with complete documentation of methods and uncertainties, and shares the AAS journals' strong norms on machine-readable data tables and open data. Readership is the international astronomy community via the AAS journals. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AAS/AJ site.

## When to trigger

- The author names AJ as the target venue for an observational, survey, catalog, instrumentation, solar-system, or exoplanet paper.
- A manuscript's primary contribution is a measurement, data product, or technique rather than astrophysical theory, and the author is choosing between AJ, The Astrophysical Journal, and Astronomy & Astrophysics.
- A paper delivers a catalog, survey data release, or observing/reduction methodology that the community will use.
- The author needs AJ's machine-readable-table norms, AASTeX conventions, and observational framing, plus desk-reject criteria, before submission.

## Scope & topic fit

- Surveys and catalogs: photometric and spectroscopic surveys, source catalogs, data releases, and value-added catalogs.
- Solar-system science: small bodies, asteroids and comets, planetary moons, dynamics, occultations, and observational characterization.
- Exoplanets: detection (transit, radial velocity, microlensing, direct imaging), confirmation and validation, system characterization, and ephemerides.
- Instrumentation and observing techniques: telescope/instrument performance, pipelines, reduction and calibration methods, and astrometric/photometric techniques.
- Stellar and galactic observational astronomy: astrometry, photometry, kinematics, and survey-based population studies where the data are the contribution.
- Time-domain and multi-messenger observational follow-up, light curves, and discovery/characterization reports.

## Method & evidence bar

- Measurements must be well-calibrated with completely documented reduction and analysis; uncertainties (statistical and systematic) must be propagated and reported.
- Surveys and catalogs must define samples precisely, characterize completeness and selection effects, and validate against existing data.
- Detection and confirmation claims (e.g., exoplanets, solar-system bodies) must state significance, false-positive assessment, and follow-up clearly.
- Instrument and technique papers must quantify performance with reproducible tests and comparison to prior methods.
- Numerical and modeling components must specify codes, parameters, and convergence sufficiently for reproduction.
- Data products and machine-readable tables must accompany the paper per AAS open-data norms; large tables are published as machine-readable tables and/or deposited in recognized archives.

## Structure & house style

- AJ uses the AAS AASTeX LaTeX class (`aastex`); manuscripts follow standard structure (Introduction, Observations/Data, Methods/Reduction, Results, Discussion, Conclusions) with appendices for technical material.
- There is no rigid hard length limit, but papers should be appropriately concise; the AAS publishes a single combined article type rather than a separate Letters format.
- Data tables intended for community use must be supplied as machine-readable tables in AASTeX format; figures should be quantitatively clear with labeled axes and uncertainties.
- Open-data and software-citation norms apply: cite software and data with DOIs, and deposit data in archives such as Zenodo or mission/survey archives.
- References follow the AAS/AASTeX style with full bibliographic data and ADS/DOI links where available.
- Abstracts are unstructured and should state the data/measurement, the method, and the result concisely.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The Astronomical Journal author guidelines" / "AAS journals instructions for authors" and follow the current AAS/IOP version.
- Re-check the AASTeX class and current formatting, machine-readable-table requirements, and figure/data conventions.
- Re-check the open-access / article-charge (publication-fee) terms and the AAS data and software policies.
- Re-check competing-interests, funding, and AI-use disclosure; confirm preprint (arXiv) policy and software/data DOI-citation requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the measurement, data product, or technique this paper contributes and who will use it.
- [ ] Reduction, calibration, and uncertainties are documented completely enough to reproduce the result.
- [ ] Samples, completeness, selection effects, and (for detections) significance and false-positive assessment are addressed.
- [ ] The manuscript uses AASTeX with machine-readable tables for community-use data.
- [ ] Data and software are deposited and cited with DOIs per AAS open-data norms.
- [ ] The paper is positioned against recent AJ / ApJ / A&A observations and data products on this question.

## Common desk-reject triggers

- A paper whose primary contribution is astrophysical theory or interpretation with only secondary observational content (better suited to ApJ).
- A survey or catalog with an ill-defined sample, missing completeness/selection analysis, or no machine-readable tables.
- A detection or confirmation claim without significance, false-positive, or systematics assessment.
- An analysis with incompletely documented reduction or unpropagated uncertainties.
- A data-only deposit with no analysis, validation, or methodological contribution.

## Re-routing decision

- The core contribution is astrophysical theory, modeling, or interpretation rather than the data themselves: `the-astrophysical-journal`.
- European-flagship framing or a paper better matched to EDP Sciences norms and the A&A Letters section: `astronomy-and-astrophysics`.
- RAS-community, theory- or simulation-heavy astrophysics: `monthly-notices-of-the-royal-astronomical-society`.
- High-impact, broad-audience astronomy result for a Nature-family venue: `nature-astronomy`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Astronomical Journal (AJ)
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the measurement/data product well-calibrated, fully documented, and reproducible, with completeness, systematics, and significance addressed?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <AASTeX & machine-readable tables / publication fee / data-software DOIs / disclosure / arXiv policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
