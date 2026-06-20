---
name: journal-of-climate
description: Use when targeting Journal of Climate or deciding whether a climate-dynamics or climate-variability manuscript fits this venue. Encodes the journal's fit, the large-scale-climate-science bar, model-evaluation and statistical-rigor expectations, AMS house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Climate (journal-of-climate)

## Journal positioning

Journal of Climate is the American Meteorological Society's journal for research on the
large-scale climate of the atmosphere, ocean, land, and cryosphere. Its defining
expectation is a **contribution to climate science**: an advance in understanding
climate dynamics, variability, change, predictability, or diagnostics at regional-to-global
scale, supported by rigorous analysis. A local weather case study, a short-range forecast
verification, or an impacts paper that applies climate data without contributing to climate
understanding is a poor fit, however careful. This skill is a **fit / venue-selection /
re-framing** tool. It does not replace the journal's current author guidance. Before
submitting, re-check the live Journal of Climate / AMS author instructions.

## When to trigger

- The author names Journal of Climate and wants a fit/framing check for a climate-dynamics
  or climate-variability paper.
- A regional analysis or model run must be re-framed into a large-scale climate-science
  contribution rather than a local case study.
- The author is choosing between Journal of Climate, a dynamics-focused AMS sibling, and a
  broader earth-science venue.
- The author needs the journal's model-evaluation and statistical-significance expectations.

## Scope & topic fit

- Large-scale atmospheric and oceanic circulation and their role in climate.
- Climate variability and modes (ENSO, NAO, monsoons, decadal variability) and their
  mechanisms and teleconnections.
- Climate change detection, attribution, and projection using observations and models.
- Climate modeling and model evaluation: process representation, biases, ensembles, and
  model intercomparison.
- Climate diagnostics, reanalyses, and the energy/water/carbon budgets of the climate
  system.
- Land–atmosphere and ocean–atmosphere coupling, cryosphere–climate interactions, and
  climate predictability on seasonal-to-decadal scales.

## Method & evidence bar

- The contribution must advance **climate understanding**, not merely report that a model or
  region behaved a certain way.
- Statistical claims require appropriate significance testing that accounts for
  autocorrelation, finite ensemble size, and multiplicity; effect sizes and confidence
  intervals should be reported, not just p-values.
- Model-based results must be evaluated against observations or reanalysis, with biases and
  internal variability explicitly addressed (single realizations are rarely sufficient).
- Mechanistic claims need diagnostic evidence linking the proposed dynamics to the observed
  signal, not correlation alone.
- Datasets, reanalyses, and model output should be identified by version and source so the
  analysis is reproducible; AMS expects clear data-availability statements.
- Trend and attribution work must separate forced response from internal variability with a
  defensible framework.

## Structure & house style

- AMS article format; re-check current article types and length expectations on the live
  guide.
- The introduction must state the climate-science question and gap, not just describe a
  dataset or region.
- Figures should be quantitative and diagnostic (maps, time series with significance,
  composite/regression analyses); they must support the mechanistic argument.
- Methods must specify datasets, model configurations, ensemble sizes, and statistical
  procedures precisely enough to reproduce; AMS requires a data-availability statement.
- Terminology and metrics should follow established climate-science conventions so results
  are comparable across studies.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the AMS anchors, then cite the
  current Journal of Climate page you checked.
- Search the live site for "Journal of Climate author guidelines" and follow the current
  AMS version.
- Re-check article types, abstract/format expectations, and length/figure expectations.
- Confirm the AMS data-availability and code/software policy: identify datasets, model
  output, and reanalyses with sources and persistent identifiers where possible.
- Re-check competing-interests, funding, author-contribution, AI-use disclosure, and
  open-access/page-charge terms.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The paper advances climate understanding, not a single local weather or impacts case.
- [ ] Statistical significance accounts for autocorrelation, ensemble size, and multiplicity.
- [ ] Model results are evaluated against observations/reanalysis with biases and internal variability addressed.
- [ ] Mechanistic claims are backed by diagnostic evidence, not correlation alone.
- [ ] Forced response is separated from internal variability in any trend/attribution claim.
- [ ] Datasets, model configurations, and an AMS data-availability statement are specified.

## Common desk-reject triggers

- A local weather event or short-range forecast study with no large-scale climate contribution.
- An impacts/applications paper that uses climate data but adds nothing to climate science.
- Trends or significance reported without accounting for autocorrelation or multiple testing.
- Model results presented without observational evaluation or any treatment of internal variability.
- Mechanistic claims resting on correlation with no diagnostic support.
- Missing data/model-version provenance or a non-compliant data-availability statement.

## Re-routing decision

- Flagship climate-change significance for a broad audience → `nature-climate-change`.
- Broad earth/environment open-access framing → `communications-earth-and-environment`.
- Short, high-immediacy geophysical result → `geophysical-research-letters`.
- Hydrologic-cycle or water-resources focus dominant → `water-resources-research` / `journal-of-hydrology`.
- Carbon/nutrient biogeochemical budgets dominant → `global-biogeochemical-cycles`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Climate
[Topic tags] <2–3 closest climate-science topics>
[Climate-science contribution] <the advance in dynamics/variability/change/predictability>
[Method/evidence] <does model evaluation + statistical rigor clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / data-availability / statistical conventions / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
