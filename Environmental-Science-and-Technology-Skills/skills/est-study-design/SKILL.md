---
name: est-study-design
description: Use when designing experiments, sampling campaigns, or modeling studies for Environmental Science & Technology (ES&T) so the design survives expert review — environmental relevance, controls, replication, mass/energy balances, and a QA/QC plan built in from the start. It guides design decisions; it does not run the study.
---

# Study Design (est-study-design)

ES&T reviewers are demanding about whether a design can actually support its environmental claim.
The failure modes are predictable: unrealistic conditions, missing controls, no replication, an
unclosed mass balance, or QA/QC bolted on after the fact. Design to pre-empt them. Execution and
reporting of results live in `est-data-analysis`.

## When to trigger

- Planning a lab/mesocosm/field study, sampling campaign, or modeling experiment
- Choosing concentrations, matrices, controls, replicates, and endpoints
- Setting up the QA/QC and mass/energy-balance plan before generating data
- A reviewer questioned environmental relevance, controls, or replication

## Design principles ES&T expects

1. **Environmental relevance.** Use concentrations, matrices, pH/ionic strength, light, temperature,
   and timescales representative of the target system — not only idealized lab spikes. Justify any
   accelerated/exaggerated conditions.
2. **Controls that isolate the mechanism.** Include the controls that rule out abiotic loss,
   sorption, volatilization, photolysis, blanks, and matrix effects — whatever could mimic your effect.
3. **Replication & randomization.** Biological/experimental replicates (not just technical);
   randomize/rotate where position or batch could confound; power your design for the effect size.
4. **Mass / energy balance.** Where the design implies one, plan to account for inputs, products,
   sorbed/volatilized fractions, and losses — unexplained gaps are a top rejection reason.
5. **QA/QC by design.** Pre-plan blanks (method/field), spikes/recoveries, CRMs, LOD/LOQ,
   calibration, surrogate/internal standards, and duplicates (see `est-data-analysis`).
6. **Dose–response / kinetics.** For toxicity or reaction studies, design enough points to fit
   curves/rate constants, not just a single dose or time point.
7. **Models.** State assumptions, domain, boundary/initial conditions, calibration vs validation data,
   and sensitivity/uncertainty analysis up front.

## Anti-patterns

- Lab spikes orders of magnitude above environmental levels presented as relevant
- No abiotic/sorption/photolysis control to isolate the claimed process
- n = 1 or technical replicates passed off as independent replication
- A transformation/treatment study with no attempt at a mass balance
- QA/QC improvised after data collection; no blanks or recoveries planned
- A model with undisclosed assumptions and no validation or sensitivity analysis

## Output format

```
【Design】lab / mesocosm / field / modeling + endpoints
【Environmental relevance】conditions match target system? [Y/N + justification]
【Controls】which confounders ruled out
【Replication/power】n, randomization, effect size
【Mass/energy balance】planned? how closed?
【QA/QC plan】blanks / spikes / CRM / LOD-LOQ / calibration
【Next】est-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — instruments, fate/transport models, QA/QC backbone
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ES&T scope and rigor expectations
