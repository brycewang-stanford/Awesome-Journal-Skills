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

## Design-weakness diagnostic

GCB reviewers probe whether the design can bear the weight of the global-change claim. Use this to
locate the soft spot before a referee does and to choose the strengthening move.

| Design soft spot | Reviewer phrasing | Strengthening move |
|------------------|-------------------|--------------------|
| Treatment confounded with unit | "Pseudoreplication" | Replicate at the inference level; state the unit |
| Dose far above realistic change | "Unrealistic forcing" | Add a realism gap statement or a dose gradient |
| Space-for-time as causal | "Gradient is not an experiment" | Add covariates or a confounder model |
| Single model run | "No structural uncertainty" | Move to an ensemble; partition uncertainty |
| Unstated search protocol | "Synthesis not reproducible" | Pre-register a PRISMA-style protocol |

## Worked micro-example (illustrative)

A team plans an open-top-chamber warming experiment to test a soil-respiration feedback. A weak design
warms one large chamber and samples it 30 times, then treats those as 30 replicates — pseudoreplication
a GCB referee will flag immediately. The strengthened design uses six warmed and six control plots
(illustrative n), warming each by an ecologically realistic +2 C rather than +6 C, and pre-commits to a
mixed model with plot as the random unit. Power analysis (illustrative) suggests this detects a 15%
efflux change. The realism gap and the scaling limit to ecosystem level are stated up front. Numbers
illustrative.

## Referee pushback patterns and the design fix

- "Correlative gradient presented as mechanistic" → pair the gradient with a manipulation or a
  process-model test of the mechanism.
- "Cannot scale this plot result to the biome" → design the sampling or modelling to carry scaling
  uncertainty, and bound rather than assert the larger claim.
- "Controls inadequate" → specify ambient, pre-treatment, or counterfactual baselines matched to the
  driver.

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
