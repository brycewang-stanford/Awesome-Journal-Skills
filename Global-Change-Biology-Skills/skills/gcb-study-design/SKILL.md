---
name: gcb-study-design
description: Use when designing the study behind a Global Change Biology (GCB) manuscript — manipulative experiments, observational/gradient studies, or process modelling of biological responses to global change. GCB reviewers probe scale, replication, realism, and causal inference. Guides design choices; it does not collect or simulate data.
---

# Study Design (gcb-study-design)

GCB reviewers are experts in **ecology, biogeochemistry, and ecosystem/Earth-system modelling**. They
will probe whether the design can actually support a **driver → biological-response** claim at the
stated scale. This skill covers design choices and their tradeoffs; analysis lives in
`gcb-data-analysis`.

## When to trigger

- Designing a warming / eCO2 / drought / N-addition experiment or a gradient/observational study
- Setting up a process-model or species-distribution-model experiment (Technical Advance or analysis)
- Justifying scale, replication, controls, and the realism of the manipulation
- A reviewer questioned confounding, pseudoreplication, or extrapolation

## Design families and what GCB expects

1. **Manipulative experiments** (OTC/infrared warming, FACE/eCO2, rainfall manipulation, N addition,
   reciprocal transplants). Report **dose, duration, replication, and the realism gap** versus real-world
   change; avoid **pseudoreplication** (treatment confounded with plot/chamber).
2. **Observational / gradient & long-term studies** (space-for-time, latitudinal/elevational gradients,
   LTER/NEON time series). State **confounders** and the limits of **space-for-time substitution**; use
   design or covariates to address them.
3. **Process / ecosystem & distribution models** (DGVMs, soil-C, crop, SDM/niche). Document **version,
   forcing, spin-up, parameterization, and evaluation against observations**; prefer **ensembles** and
   report **structural vs parameter vs scenario uncertainty**.
4. **Evidence synthesis / meta-analysis.** Pre-specify the **search protocol** (PRISMA-style), inclusion
   criteria, effect size, and heterogeneity/publication-bias plan.

## Cross-cutting design principles

- **Match scale to claim.** Plot-scale results do not automatically scale to ecosystem or biome.
- **Replicate at the level of inference**, and state the experimental unit explicitly.
- **Define controls and baselines** appropriate to the driver (ambient, pre-treatment, counterfactual run).
- **Plan for uncertainty** up front, not as an afterthought.

## Anti-patterns

- Pseudoreplication: a single warmed plot/chamber treated as many independent replicates
- Over-extrapolating a short, high-dose manipulation to gradual real-world change
- Space-for-time substitution presented as if it were a controlled experiment
- A model run with no evaluation against observations and no uncertainty
- A meta-analysis with no pre-specified protocol or bias assessment

## Output format

```
【Design family】experiment / gradient-observational / model / synthesis
【Driver & response】manipulated/measured at what scale
【Replication & unit】level of inference; pseudoreplication ruled out? [Y/N]
【Realism / confounding】dose-duration realism or confounder plan
【Uncertainty plan】measurement + model + scenario
【Next】gcb-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — experimental, observational, and modelling toolchains
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — GCB scope (molecular-to-biome, aquatic/terrestrial)
