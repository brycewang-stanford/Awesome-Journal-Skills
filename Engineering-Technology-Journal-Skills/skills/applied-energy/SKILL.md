---
name: applied-energy
description: Use when targeting Applied Energy or deciding whether a systems-level energy manuscript fits this venue. Encodes the journal's fit, the systems-scope-and-quantified-impact bar, modeling and assessment rigor, house style, the systems-vs-single-device routing, official-submission re-check, and desk-reject heuristics.
---

# Applied Energy (applied-energy)

## Journal positioning

Applied Energy (Elsevier) is a **systems-level** energy research venue: energy
conversion and integration, energy-systems modeling and optimization, decarbonization
pathways, demand and efficiency, and techno-economic and environmental assessment. Its
center of gravity is the **system, not the device** — how technologies, sectors, and
markets combine to deliver, store, or save energy, and what the quantified
energetic, economic, and environmental consequences are. The single most common misfit
is a single-material or single-component study (for example, one electrode or one
catalyst) submitted as if it were systems research; such work belongs at a materials or
device venue. A paper succeeds when its contribution is a generalizable
systems-level insight backed by transparent, validated analysis. This skill is a
**fit / venue-selection / re-framing** tool. It does not replace the journal's current
official author guidelines. Before submitting, re-check the live Applied Energy Guide
for Authors on the Elsevier site.

## When to trigger

- The author names Applied Energy for an energy-systems modeling, integration,
  decarbonization, efficiency, or techno-economic/environmental-assessment manuscript.
- A paper must be re-framed from a device/component result into a systems-level question
  with quantified energy/economic/environmental impact — or re-routed if it is in fact
  device-level.
- The author is deciding between Applied Energy's systems scope and a device venue
  (`journal-of-power-sources`) or a materials venue (`energy-storage-materials`).
- The author needs the journal's systems-scope and assessment rigor bar and
  desk-reject heuristics.

## Scope & topic fit

- Energy-systems modeling and optimization: power, heat, transport, and multi-vector
  systems; dispatch, planning, and integration of variable renewables and storage.
- Energy conversion and integration at the system/process level, including hybrid and
  sector-coupled configurations and waste-heat/energy recovery.
- Decarbonization pathways and scenario analysis: emissions, cost, and feasibility of
  transitions across technologies, sectors, or regions.
- Demand-side, efficiency, buildings, and flexibility: demand response, load modeling,
  and end-use efficiency with system-level consequences.
- Techno-economic analysis (TEA) and life-cycle/environmental assessment (LCA) of
  energy technologies and systems, with transparent assumptions.
- Data-driven and machine-learning methods for energy systems when the contribution is
  a generalizable systems insight, not a black-box fit to one dataset.

## Method & evidence bar

- The central claim is a **systems-level insight**: a result about how a system
  performs, integrates, or decarbonizes, with quantified energy, economic, and/or
  environmental outcomes — not a component performance number.
- Models must be transparent and validated/benchmarked where possible; assumptions,
  boundaries (system boundary, time horizon, spatial scope), and data sources stated.
- Techno-economic and environmental results require disclosed cost/emission factors,
  functional units, and uncertainty/sensitivity analysis; point estimates without
  sensitivity are weak.
- Generalizability and scenario robustness must be shown: results should hold or be
  characterized across cases, not depend on one favorable assumption set.
- Comparisons must use a fair baseline/counterfactual; reproducibility requires that
  data, parameters, and (where applicable) code be sufficiently described.

## Structure & house style

- Standard research-article structure (introduction, methods/model, results,
  discussion); the journal uses highlights and a graphical abstract — re-check current
  article types and requirements on the live guide.
- The introduction frames the energy-systems gap and the decision/insight at stake, not
  a component novelty; methods state the system boundary, scope, and assumptions
  explicitly.
- Figures are load-bearing: system diagrams, scenario/optimization results, cost and
  emission breakdowns, and sensitivity/uncertainty plots.
- Supporting information carries full model formulations, parameter tables, and data;
  main-text figures must support the systems claim on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Applied Energy Guide for Authors page you checked.
- Search the live site for "Applied Energy guide for authors" and follow the current
  Elsevier/Editorial Manager version.
- Re-check article types, highlights and graphical-abstract requirements, and
  length/figure expectations.
- Confirm data/code-availability expectations and assumption/parameter-reporting norms
  for TEA/LCA and modeling work.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a systems-level insight with quantified energy/economic/environmental impact, not a single-device result.
- [ ] System boundary, time horizon, spatial scope, and key assumptions are stated explicitly.
- [ ] Models are transparent and validated/benchmarked; data sources are disclosed.
- [ ] TEA/LCA results include functional units, cost/emission factors, and uncertainty/sensitivity analysis.
- [ ] Results are shown to be robust across scenarios against a fair baseline/counterfactual.
- [ ] Highlights and graphical abstract represent the systems-level advance.

## Common desk-reject triggers

- Single-material/single-device study (one electrode, one catalyst) framed as systems research.
- TEA/LCA with undisclosed assumptions, no functional unit, or no uncertainty/sensitivity analysis.
- Optimization/modeling tuned to one case with no generalizable systems insight.
- Black-box machine-learning fit to one dataset with no transferable energy-systems finding.
- Results that depend on a single favorable assumption set with no robustness check.
- Component-performance paper with system relevance asserted only in the abstract.

## Re-routing decision

- Device-level electrochemical power (cells, fuel cells, supercapacitors) → `journal-of-power-sources`.
- Electrode/electrolyte materials and mechanism → `energy-storage-materials`.
- Applied catalysis/separation process at the unit level → `chemical-engineering-journal`.
- Authoritative energy/combustion review synthesis → `progress-in-energy-and-combustion-science`.
- Highest-profile cross-cutting energy advance → `nature-energy`, `joule`, or `energy-and-environmental-science` (different selectivity/format; re-check).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Applied Energy
[Topic tags] <2–3 closest energy-systems subtopics>
[Systems insight] <the system-level claim and quantified impact in one line>
[Scope/boundary] <system boundary, horizon, and key assumptions stated?>
[Rigor] <validation + uncertainty/sensitivity + fair baseline present?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / highlights / data-code / TEA-LCA reporting / disclosures>
[Re-route suggestion] <if device/material-level or out of scope, a better-matched venue>
```
