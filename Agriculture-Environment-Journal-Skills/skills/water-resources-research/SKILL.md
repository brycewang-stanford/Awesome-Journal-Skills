---
name: water-resources-research
description: Use when targeting Water Resources Research (WRR) or deciding whether a hydrology / water-science manuscript fits this venue. Encodes the journal's fit, the quantitative water-science contribution bar, data-and-code deposition expectations, AGU house style, official-submission re-check, and desk-reject heuristics.
---

# Water Resources Research (water-resources-research)

## Journal positioning

Water Resources Research (WRR) is the American Geophysical Union's flagship journal for
the science of water — the physical, chemical, biological, and socio-hydrological
processes governing water resources, and the methods used to observe, model, and manage
them. The defining expectation is a **quantitative, generalizable advance in water
science**: a new process understanding, method, theory, or analysis that transfers beyond
one basin. An applied case study that reports model results for a single catchment with no
methodological or conceptual contribution is a weak fit. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current author
guidance. Before submitting, re-check the live WRR/AGU author instructions and data policy.

## When to trigger

- The author names WRR and wants a fit/framing check for a hydrology or water-science paper.
- A basin-specific modeling or monitoring study must be re-framed into a transferable
  methodological or process contribution.
- The author is choosing between WRR, `journal-of-hydrology`, and a broader earth-science
  venue.
- The author needs WRR's quantitative-contribution bar and AGU data-deposition expectations.

## Scope & topic fit

- Surface-water and groundwater hydrology: catchment processes, streamflow, recharge,
  vadose-zone and subsurface flow and transport.
- Hydrologic modeling, data assimilation, uncertainty quantification, and predictability.
- Hydroclimatology, snow/ice hydrology, and land–atmosphere water exchange.
- Water quality, contaminant transport, and ecohydrology when mechanistically framed.
- Socio-hydrology, water-resources systems, and human–water interactions with rigorous
  quantitative analysis.
- Hydrologic measurement, sensing, and experimental methods that advance observation.

## Method & evidence bar

- The contribution must be **quantitative and transferable**: a method, theory, or process
  insight whose value is not confined to one site.
- Models must be evaluated against data with appropriate skill metrics, benchmarks, and
  uncertainty quantification; parameter identifiability and equifinality should be addressed.
- Observational studies need defensible sampling/monitoring design, error characterization,
  and reproducible processing.
- Claims of improvement require comparison to a credible baseline (an established model or
  method), not a strawman.
- Data and code underpinning the results should be deposited in a FAIR community repository
  per AGU policy.

## Structure & house style

- AGU article format; WRR publishes research articles, technical reports/notes, and
  commentaries — re-check current article types and length expectations on the live guide.
- The introduction must state the water-science gap and the transferable contribution, not
  just describe a study area.
- Figures should be quantitative and load-bearing (hydrographs, maps with uncertainty,
  skill/benchmark comparisons); a key-points summary is part of the AGU format.
- Methods and data/code availability statements must let a reader reproduce the central
  result; AGU expects open data/software with persistent identifiers.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the AGU anchors, then cite the
  current WRR page you checked.
- Search the live site for "Water Resources Research author guidelines" and follow the
  current AGU/Wiley version.
- Re-check article types, key-points and abstract format, and length expectations.
- Confirm the **AGU data and software availability policy**: deposit data/code in an
  approved repository and cite it with a DOI.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure, and
  open-access terms.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The contribution is a transferable method/theory/process insight, not a single-basin case study.
- [ ] Models are benchmarked against data with skill metrics and uncertainty quantification.
- [ ] Observational design, error characterization, and processing are reproducible.
- [ ] Improvement is shown against a credible baseline, not a strawman.
- [ ] Data and code are deposited in a FAIR repository with persistent identifiers.
- [ ] Key points and AGU formatting/availability statements are prepared.

## Common desk-reject triggers

- Single-catchment model application with no methodological or conceptual advance.
- Model results presented without benchmarking, skill metrics, or uncertainty quantification.
- Observational study with weak sampling design or no error characterization.
- Missing or non-compliant data/code deposition where AGU policy requires it.
- Scope mismatch: a pure water-engineering design, water-policy essay, or chemistry paper with
  no water-science contribution.

## Re-routing decision

- Broader process/observational/applied hydrology → `journal-of-hydrology`.
- Carbon/nutrient biogeochemical cycling focus → `global-biogeochemical-cycles`.
- Climate-dynamics framing dominant → `journal-of-climate`.
- Land–atmosphere flux / agro-meteorology → `agricultural-and-forest-meteorology`.
- New documented hydrologic dataset as the product → `earth-system-science-data`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Water Resources Research
[Topic tags] <2–3 closest water-science topics>
[Transferable contribution] <the method/theory/process insight beyond one basin>
[Method/evidence] <does benchmarking + uncertainty + data deposition clear WRR's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / key points / AGU data-software policy / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
