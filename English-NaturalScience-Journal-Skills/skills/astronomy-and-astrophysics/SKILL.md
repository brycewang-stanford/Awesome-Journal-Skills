---
name: astronomy-and-astrophysics
description: Use when targeting Astronomy & Astrophysics (A&A) or deciding whether an astronomy manuscript fits this European flagship published by EDP Sciences. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Astronomy & Astrophysics (astronomy-and-astrophysics)

## Journal positioning

A&A is published by EDP Sciences on behalf of a consortium of mostly European countries and is the European flagship journal covering all of astronomy and astrophysics. Its defining character is comprehensive scope paired with high observational and methodological rigor: A&A publishes the full range of the field — stellar physics, the interstellar medium, galaxies, cosmology, the Sun and heliosphere, planets and exoplanets, and instrumentation — and is especially strong on observational surveys, data-rich analyses, and instrument/method papers. It maintains a dedicated Letters section for urgent, significant short results alongside full-length research articles. A&A rewards careful, reproducible analysis with complete description of data reduction, calibration, and uncertainties; it is a working journal of record for the community, not a venue that prioritizes headline novelty over completeness. Readership is the international astronomy community, with a strong European base. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the A&A/EDP Sciences site.

## When to trigger

- The author names A&A as the target venue for a complete astronomy or astrophysics research article or a Letter.
- A manuscript is an observational survey, instrumentation/method paper, or data-driven astrophysical analysis and the author is choosing between A&A, The Astrophysical Journal, The Astronomical Journal, and MNRAS.
- A short, time-critical but significant result needs the A&A Letters section.
- The author needs A&A's data-reduction-documentation norms, language-editing expectations, and section conventions, plus desk-reject criteria, before submission.

## Scope & topic fit

- Stellar physics: stellar structure and evolution, atmospheres, spectroscopy, asteroseismology, variable and binary stars, and stellar populations.
- Interstellar medium and star formation: molecular clouds, dust, astrochemistry, protostars, and feedback processes.
- Galaxies and cosmology: galaxy formation and evolution, AGN, large-scale structure, the high-redshift universe, and cosmological parameter analyses.
- The Sun, heliosphere, and solar-stellar connection: solar physics, magnetism, and space weather drivers.
- Planetary systems and exoplanets: detection, characterization, atmospheres, dynamics, and solar-system bodies.
- Instrumentation, numerical methods, catalogs, and data-reduction techniques that enable the above — A&A explicitly welcomes instrument and method papers.

## Method & evidence bar

- Data reduction, calibration, and analysis must be documented completely enough to reproduce; this is a central A&A referee expectation.
- Uncertainties must be propagated and reported rigorously; statistical methods must be appropriate and justified, with systematics discussed explicitly.
- Observational claims must account for selection effects, completeness, and instrumental systematics; survey papers must define samples precisely.
- Numerical and modeling results must specify codes, parameters, and convergence sufficiently for reproduction.
- New results should be placed against existing measurements and theoretical expectations, with quantitative comparison rather than qualitative assertion.
- Data products, catalogs, and code should be made available (e.g., via the CDS/VizieR for tables, or a public repository); A&A has long-standing data-archiving links with the CDS.

## Structure & house style

- A&A uses the `aa` LaTeX class (EDP Sciences `aa.cls`); manuscripts follow standard structure (Introduction, Observations/Data, Methods/Analysis, Results, Discussion, Conclusions) with appendices for technical detail.
- Full-length articles have no strict hard length cap but should be appropriately concise; Letters are short, with their own length limit and a fast-track significance bar.
- Clear, correct scientific English is expected; A&A provides language-editing services and may require editing where needed.
- Tables intended for the community should be submitted in machine-readable form and are archived at the CDS; large tables go to the CDS rather than the body text.
- Figures must be quantitatively clear with labeled axes and uncertainties; color and multi-panel figures are standard.
- References follow the A&A/EDP style; the abstract is structured into Context, Aims, Methods, and Results.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Astronomy & Astrophysics author guidelines" / "A&A instructions for authors" and follow the current EDP Sciences version.
- Re-check the `aa.cls` LaTeX class and current formatting, the structured-abstract requirement, and Letters length limits.
- Re-check CDS/VizieR table-submission and data-archiving requirements; confirm accepted repositories for data and code.
- Re-check language-editing, open-access/charge options, competing-interests, and AI-use disclosure; confirm preprint (arXiv) policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the astronomical result of this paper and how it advances the field.
- [ ] Data reduction, calibration, and uncertainties are documented completely enough to reproduce the analysis.
- [ ] Selection effects, completeness, and systematics are addressed; samples and methods are precisely defined.
- [ ] The manuscript uses the `aa.cls` class with a structured (Context/Aims/Methods/Results) abstract.
- [ ] Machine-readable tables are prepared for the CDS; data and code availability is arranged.
- [ ] The paper is positioned against recent A&A / ApJ / MNRAS measurements and models on this question.

## Common desk-reject triggers

- An analysis with incompletely described data reduction, missing uncertainties, or unaddressed systematics.
- A survey or catalog paper with an ill-defined sample, ignored selection effects, or no completeness assessment.
- A result presented without quantitative comparison to existing measurements or theory.
- A Letter that does not meet the urgency-and-significance bar or exceeds the Letters length limit.
- Manuscript English so unclear that the scientific content cannot be assessed, with no use of available language editing.

## Re-routing decision

- AAS-style framing or a US-community readership better matched to the ApJ family: `the-astrophysical-journal`.
- Observationally broad survey, catalog, solar-system, or exoplanet data paper emphasizing the data product: `the-astronomical-journal`.
- RAS-community framing, theory-heavy or simulation-driven astrophysics suited to the RAS journals: `monthly-notices-of-the-royal-astronomical-society`.
- High-impact, broad-audience astronomy result for a Nature-family venue: `nature-astronomy`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Astronomy & Astrophysics (A&A)
[Topic tags] <2–3 closest topics>
[Method/evidence] <is the data reduction, uncertainty treatment, and systematics handling complete and reproducible, with quantitative comparison to prior work?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <aa.cls & structured abstract / Letters length / CDS table archiving / data-code / language editing / arXiv policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
