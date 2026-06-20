---
name: ieee-transactions-on-power-systems
description: Use when targeting IEEE Transactions on Power Systems (TPWRS) or deciding whether an electric-power-systems manuscript fits this venue. Encodes the journal's fit, the methodology-plus-case-study bar, the standard-test-system expectation, the power-system-vs-power-electronics routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Power Systems (ieee-transactions-on-power-systems)

## Journal positioning

IEEE Transactions on Power Systems (TPWRS) is the leading archival venue for electric
power systems engineering: grid operation and planning, power flow and optimal power
flow, stability and dynamics, electricity markets, reliability, and the integration
of renewables, storage, and demand response at system scale. The defining expectation
is a **system-level methodological contribution validated on credible case studies** —
a new model, algorithm, or analysis whose value is shown on standard test systems or
realistic networks against meaningful baselines. Component-level device work,
power-electronics circuit design, or generic optimization with a thin power-system
wrapper are a poor fit. This skill is a **fit / venue-selection / re-framing** tool.
It does not replace the journal's current official author guidelines. Before
submitting, re-check the live IEEE Transactions on Power Systems author information
and submission system.

## When to trigger

- The author names TPWRS for a grid-operation, planning, market, or stability
  manuscript and wants a fit/framing check.
- A method must be re-framed from "we ran an optimization" into a power-system
  contribution validated on standard test systems with the right baselines.
- The author is choosing between TPWRS and `ieee-transactions-on-power-electronics`
  (converter-level) or an energy-systems venue (`applied-energy`).
- The author needs the methodology-plus-case-study bar and desk-reject heuristics
  specific to power systems.

## Scope & topic fit

- Power-system operation: economic dispatch, unit commitment, optimal power flow,
  security-constrained operation, and real-time/look-ahead scheduling.
- Planning and expansion: generation, transmission, and storage planning under
  uncertainty; reliability and resilience assessment.
- Stability and dynamics: transient, small-signal, voltage, and frequency stability;
  wide-area monitoring and control; inverter-dominated grid dynamics.
- Electricity markets and economics: market design, pricing, bidding, and the
  coupling of markets with physical operation.
- Renewable, storage, demand-response, and electric-vehicle integration; distribution
  systems, microgrids, and the transmission–distribution interface at system scale.

## Method & evidence bar

- The contribution is a **system-level method** — model, algorithm, or analysis — whose
  correctness and value are demonstrated on standard IEEE test systems or realistic
  network data, not on a toy two-bus example alone.
- Case studies must compare against meaningful baselines (existing formulations or
  solvers) and report computational performance, optimality/feasibility, and
  scalability where relevant.
- Modeling assumptions (network model, uncertainty representation, time resolution)
  must be explicit and defensible; results must be reproducible from the described
  data and parameters.
- For optimization or learning methods, the power-system formulation and constraints
  (physical, security, market) must be central — not a generic solver applied to a
  relabeled problem.
- Stability/dynamics claims require appropriate models and validation; statistical or
  data-driven results need adequate sampling and out-of-sample evaluation.

## Structure & house style

- IEEE format; TPWRS publishes full **Papers** and shorter **Letters** — match scope to
  the article type and re-check current definitions and limits on the live guide.
- The introduction motivates the power-system problem and positions against prior
  formulations; the model and assumptions are stated precisely before the method.
- Figures and tables are quantitative: single-line diagrams, convergence and
  cost/feasibility tables, time-series of operation, and scalability comparisons on
  named test systems.
- Test-system identity, data sources, and solver/parameter settings should be reported
  in enough detail to reproduce the case studies.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Transactions on Power Systems page you checked.
- Search the live site for "IEEE Transactions on Power Systems information for authors"
  and follow the current submission-system version.
- Re-check article types (Paper vs. Letter), length/overlength policy, and the IEEE
  template.
- Confirm data/code-availability expectations and any test-system/data-sharing norms
  for reproducible case studies.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a system-level method (model/algorithm/analysis), not a component or circuit-level result.
- [ ] Case studies use standard test systems or realistic network data, not a toy example alone.
- [ ] Baselines are meaningful (existing formulations/solvers), with computation, optimality/feasibility, and scalability reported.
- [ ] The power-system formulation and constraints are central, not a generic solver on a relabeled problem.
- [ ] Modeling assumptions and data/parameters are explicit and reproducible.
- [ ] Article type (Paper vs. Letter) and length fit current limits.

## Common desk-reject triggers

- A generic optimization or machine-learning method with only a thin power-system wrapper and no power-specific formulation.
- Validation on a toy example only, with no standard test system or realistic network.
- Missing or unfair baselines, or no reporting of computation/scalability for a method that claims to be practical.
- Component-level or power-electronics circuit work that belongs at the converter venue.
- Stability/market claims with inadequate models, sampling, or out-of-sample evaluation.

## Re-routing decision

- Converter/inverter/drive circuit-level contribution → `ieee-transactions-on-power-electronics`.
- Broader energy-system or techno-economic analysis → `applied-energy`.
- Control theorem about a dynamical system, not grid-specific → `ieee-transactions-on-automatic-control` / `automatica`.
- Storage-cell, battery, or materials focus → `journal-of-power-sources` / `energy-storage-materials`.
- Broad tutorial/survey of a power-systems area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Power Systems
[Topic tags] <2–3 closest power-systems subtopics>
[Method + validation] <the system-level method and the test systems it is shown on>
[Baselines + scalability] <meaningful baselines? computation/scalability reported?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / Letter
[Official items to re-check] <article type / length / data-code / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
