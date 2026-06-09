---
name: geophysical-research-letters
description: Use when targeting Geophysical Research Letters (GRL) or deciding whether an Earth or space science manuscript fits this high-impact short-format venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Geophysical Research Letters (geophysical-research-letters)

## Journal positioning

Geophysical Research Letters is an American Geophysical Union (AGU) journal published by Wiley, and it is the union's flagship venue for short, high-impact reports spanning the full breadth of the Earth and space sciences — atmosphere, ocean, solid earth, hydrology, cryosphere, biogeosciences, and space physics. Its defining character is the combination of brevity and significance: GRL exists to communicate a single important, broadly interesting finding rapidly, not to provide the comprehensive treatment that a full-length journal allows. The journal rewards work that is novel, immediately consequential, and of interest beyond a narrow subdiscipline — a result that changes how a community interprets a process or that resolves a question of wide significance. Readership is the entire AGU community across geoscience and space science. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the GRL/AGU/Wiley site.

## When to trigger

- The author names GRL as the target venue for a short, high-impact Earth or space science finding.
- A manuscript reports a single significant, broadly interesting result, and the author is choosing between GRL and a full-length JGR section or Nature Geoscience.
- A paper has a clear, consequential finding that does not need the length of a full-length article and would lose impact if padded.
- The author needs GRL's strict length and significance bar, plus desk-reject criteria, before submission.

## Scope & topic fit

- Atmospheric science: dynamics, composition, convection, climate variability, extreme-event mechanisms — when a single result has broad significance.
- Oceanography and cryosphere: circulation change, sea-level processes, ice-sheet and sea-ice dynamics, ocean heat content, where a finding reframes understanding.
- Solid earth and geodesy: seismology, tectonics, volcanology, gravity and deformation, where a result is novel and consequential.
- Hydrology and biogeosciences: terrestrial water cycle, land-atmosphere coupling, carbon and nutrient cycling — when the finding is general and timely.
- Space physics and aeronomy: magnetosphere, ionosphere, solar-terrestrial coupling, planetary space environments.
- Methodological or observational advances that immediately enable a significant new geophysical inference across a community.

## Method & evidence bar

- The significance must be identifiable in one or two sentences; a paper whose central finding is incremental or narrowly technical is misfit for GRL.
- The result must be rigorously supported within the short format: appropriate uncertainty quantification, error bars and confidence intervals, and sensitivity to key assumptions.
- Observational claims need clear data provenance, calibration, and treatment of instrument or sampling biases.
- Modeling claims need adequate description of configuration, validation against observations where possible, and honest treatment of model limitations.
- Data and code must be deposited in an AGU-compliant FAIR repository (Zenodo, PANGAEA, community archives) with persistent identifiers; availability statements are mandatory.
- Statistical significance of geophysical trends or differences must be established against appropriate null models and autocorrelation.

## Structure & house style

- GRL enforces a strict length limit — a low word count, a hard cap on figures plus tables, and a limited reference count; re-check current limits on the live site.
- The main text is a single continuous argument: a concise introduction stating the gap and significance, methods kept tight, results, and a focused discussion — no exhaustive literature review.
- Supporting Information carries extended methods, additional figures, and supplementary analyses; the main text must stand alone scientifically.
- Figures must be efficient and publication-quality; each must carry a key result, and the figure cap must be respected.
- The abstract is unstructured, short, and must convey the finding and its significance to a broad geoscience reader.
- A plain-language summary is required and must communicate the significance to non-specialists.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Geophysical Research Letters submission guidelines" and follow the current AGU/Wiley version.
- Re-check the strict word limit, the figure-plus-table cap, and the reference limit; confirm current Supporting Information conventions.
- Re-check AGU's data and software availability policy; confirm accepted FAIR repositories and that an availability statement is included.
- Re-check the plain-language summary requirement, competing-interests, funding, and AI-use disclosure; confirm preprint policy (ESSOAr/EarthArXiv posting is generally compatible).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the single significant finding and why it matters across the geoscience community.
- [ ] The paper fits within the current word, figure, and reference limits without cutting substance; if not, a full-length journal is more appropriate.
- [ ] Methods are tight in the main text and fully documented in Supporting Information; analyses are reproducible.
- [ ] Uncertainty, error bars, and significance against appropriate nulls are reported for the central claim.
- [ ] Data and code are deposited in an AGU-compliant FAIR repository; availability statement and persistent identifiers are ready.
- [ ] A plain-language summary communicates the significance to non-specialists.

## Common desk-reject triggers

- An incremental result, a regional case study, or a technical refinement without broad geophysical significance.
- A paper that exceeds the word, figure, or reference limit, or whose scope requires the length of a full-length article.
- A modeling or observational study lacking uncertainty quantification, validation, or treatment of biases.
- A descriptive dataset or instrument report without a significant scientific inference.
- A missing or non-compliant data/software availability statement, or a missing plain-language summary.

## Re-routing decision

- A complete, comprehensive treatment needing full-length space: the relevant section of `journal-of-geophysical-research` (Atmospheres, Oceans, Solid Earth, Space Physics, etc.).
- A higher-impact, broader-reach result with cross-disciplinary significance: `nature-geoscience`.
- An authoritative invited review rather than primary research: `reviews-of-geophysics`.
- A water-resources or hydrology finding better matched to a water-focused venue: `nature-water` or `water-research`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Geophysical Research Letters
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there a single significant, broadly interesting finding, and is it rigorously defended with uncertainty within the short format?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <word/figure/reference limit / SI conventions / data-software FAIR deposition / plain-language summary / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
