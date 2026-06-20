---
name: aiche-journal
description: Use when targeting AIChE Journal or deciding whether a chemical-engineering manuscript fits this venue. Encodes the journal's fit, the fundamental-and-generalizable contribution bar, modeling-plus-experiment rigor, house style, the fundamentals-vs-applied routing, official-submission re-check, and desk-reject heuristics.
---

# AIChE Journal (aiche-journal)

## Journal positioning

AIChE Journal is the flagship archival journal of the American Institute of Chemical
Engineers, publishing **fundamental, generalizable chemical-engineering science**:
transport phenomena, thermodynamics, reaction engineering and kinetics, separations,
interfacial and colloidal phenomena, and process systems engineering. Its center of
gravity is the principle, not the product — a paper earns space when it advances the
understanding of a chemical-engineering phenomenon in a way that transfers beyond the
specific system studied. Application case studies that optimize one process, or
materials papers where the chemical-engineering science is incidental, are a weak fit
and read better at a more applied venue. This skill is a **fit / venue-selection /
re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live AIChE Journal author guidelines on
the Wiley site.

## When to trigger

- The author names AIChE Journal for a transport, thermodynamics, reaction-engineering,
  separations, or process-systems manuscript and wants a fit/framing check.
- A paper must be re-framed from "we built/optimized this process" into a generalizable
  chemical-engineering principle with predictive reach.
- The author is choosing between AIChE Journal's fundamentals bar and the more applied
  `chemical-engineering-journal`.
- The author needs AIChE Journal's modeling-and-experiment rigor bar and desk-reject
  heuristics.

## Scope & topic fit

- Transport phenomena: momentum/heat/mass transfer, multiphase flow, mixing, and
  interfacial transport with new theory, correlation, or mechanism.
- Thermodynamics and molecular engineering: equations of state, phase equilibria,
  electrolyte and complex-fluid thermodynamics, and predictive property modeling.
- Reaction engineering and kinetics: reactor design and analysis, catalytic kinetics,
  multiscale reaction–transport coupling, and intensified reactors.
- Separations: distillation, absorption, extraction, adsorption, and membrane
  separations where the advance is in mechanism, modeling, or generalizable design.
- Interfacial, colloidal, and particle science; population-balance and complex-fluid
  behavior tied to chemical-engineering phenomena.
- Process systems engineering: modeling, optimization, control, and design at the
  systems level when the methodological contribution generalizes.

## Method & evidence bar

- The central claim is a **fundamental, transferable result** — a model, mechanism, or
  scaling — validated against experiment or rigorous simulation, not a tuned outcome
  for a single feedstock or unit.
- Models must be physically grounded, with stated assumptions, dimensional consistency,
  and validation against independent data; a fitted correlation with no mechanistic
  basis is usually insufficient.
- Experimental work must report conditions, uncertainties, and reproducibility in
  enough detail to reproduce the measurement and the regime of validity.
- Generality is demonstrated, not asserted: show that the result holds across a
  parameter range, dimensionless regime, or system class — not at one operating point.
- Compare to the correct prior models/correlations and state precisely what is new
  (wider regime, fewer assumptions, better predictive accuracy).

## Structure & house style

- Standard research-article structure (introduction, theory/methods, results,
  discussion); AIChE Journal publishes full archival articles and shorter formats —
  re-check current article types on the live guide.
- The introduction frames the chemical-engineering-science gap and the phenomenon
  being explained, not the application target; the discussion makes the
  generality/validity argument explicit.
- Equations and dimensionless groups are load-bearing; define all symbols, give a
  nomenclature section per house style, and keep notation consistent.
- Figures pair model predictions with experimental/simulation data and show error
  bars and regimes of validity; supporting information carries extended derivations
  and full datasets.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Wiley anchors, then cite the
  current AIChE Journal author-guidelines page you checked.
- Search the live site for "AIChE Journal author guidelines" and follow the current
  Wiley/submission-system version.
- Re-check article types, length/figure expectations, and the nomenclature/SI-units
  formatting conventions.
- Confirm data-availability, supporting-information, and any code/model-sharing
  expectations.
- Re-check ORCID, competing-interests, funding, author-contribution (CRediT), and
  AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a fundamental, generalizable chemical-engineering result — not a one-process optimization.
- [ ] Models are physically grounded with stated assumptions and validated against independent data.
- [ ] Generality is demonstrated across a parameter range / dimensionless regime, not at one operating point.
- [ ] Experimental conditions, uncertainties, and reproducibility are fully reported.
- [ ] Novelty is pinned to specific prior models/correlations (wider regime / fewer assumptions / better accuracy).
- [ ] Nomenclature, units, and notation follow house style and are internally consistent.

## Common desk-reject triggers

- Single-process optimization or case study with no transferable chemical-engineering principle.
- Empirical correlation fitted to one dataset with no mechanistic basis or validation regime.
- Materials-synthesis paper where the chemical-engineering science is incidental to the material.
- Simulation-only study with no experimental anchor or testable prediction.
- Application-domain framing (a specific product/plant) where the science does not generalize.
- Scope mismatch: a pure chemistry, pure materials, or pure controls paper using CE only as a label.

## Re-routing decision

- Applied/materials-heavy chemical engineering with environmental/energy emphasis → `chemical-engineering-journal`.
- Membrane materials and transport as the core → `journal-of-membrane-science`.
- Systems-level energy conversion / techno-economic scope → `applied-energy`.
- Combustion or energy review synthesis → `progress-in-energy-and-combustion-science`.
- Catalysis as a chemistry/mechanism advance over CE design → `nature-catalysis`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] AIChE Journal
[Topic tags] <2–3 closest CE subtopics>
[Fundamental claim] <the generalizable transport/thermo/reaction/separation principle in one line>
[Method/evidence] <does model + experiment clear the fundamentals + validation bar?>
[Generality] <range/regime over which the result is shown to hold>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / nomenclature / data policy / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
