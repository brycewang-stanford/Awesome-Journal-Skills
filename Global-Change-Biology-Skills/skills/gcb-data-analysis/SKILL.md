---
name: gcb-data-analysis
description: Use when executing and reporting the analysis for a Global Change Biology (GCB) manuscript — mixed/hierarchical models, time-series and spatial analysis, meta-analysis, and model evaluation with honest uncertainty. GCB reviewers and data archiving demand reproducible, well-quantified inference. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (gcb-data-analysis)

GCB reviewers are quantitatively sophisticated, and because **data and code are archived publicly with
a DOI** (see `gcb-reporting-and-data-policy`), the analysis must be reproducible by a third party.
Analyze as if both are true — because they are. This skill covers execution and reporting norms; design
decisions live in `gcb-study-design`.

## When to trigger

- Running main and supporting analyses; building the results
- Choosing the right model for nested/repeated/spatial ecological data
- Synthesizing effect sizes for a meta-analysis or evaluating a process model
- Making the analysis reproducible before deposit

## Analysis norms GCB expects

1. **Respect the data structure.** Use mixed / hierarchical models (`lme4`, `glmmTMB`, `brms`, `INLA`)
   for nested, repeated-measures, and spatially/temporally autocorrelated data; do not ignore random
   effects or autocorrelation.
2. **Report uncertainty honestly.** Effect sizes with confidence/credible intervals, not just p-values
   or stars; state the magnitude and its ecological/biogeochemical meaning.
3. **Quantify, propagate, and partition uncertainty.** For models, separate **parameter, structural,
   and scenario** uncertainty; prefer **ensembles**; show measurement error where it matters.
4. **Meta-analysis discipline.** Appropriate effect size (log response ratio, Hedges' g), random/mixed
   effects, heterogeneity (I^2, tau^2), moderators pre-specified, and a publication-bias check.
5. **Evaluate models against observations.** Report skill metrics and where the model fails, not only
   where it succeeds.
6. **Right inference for the unit.** Match the analysis to the experimental/sampling unit; avoid
   pseudoreplication carrying through from design.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from raw/constructed data.
- **Set and report seeds** for any stochastic step (bootstrap, MCMC, simulation, model ensembles).
- Pin software/package versions (`renv.lock`, `conda`/`requirements.txt`, model version + forcing).
- Keep manuscript table/figure numbers matched to script outputs — they will be archived together.

## Matching the method to the global-change question

GCB referees expect the analysis to fit the data-generating process. Use this as a routing table from
question shape to the inferential machinery a quantitatively literate reviewer will look for.

| Question shape | Expected machinery | What a reviewer checks |
|----------------|--------------------|------------------------|
| Effect of a manipulated driver across randomized plots | Mixed model with plot/block random effects | Random structure matches the design; no pseudoreplication |
| Trend in a flux time series | Autocorrelation-aware regression / state-space | Residual autocorrelation modelled, not ignored |
| Spatial pattern across a gradient | Spatial random field (INLA/`spaMM`) | Spatial dependence handled; CRS and area stated |
| Synthesis across many studies | Random/mixed-effects meta-analysis | Effect-size choice, I^2/tau^2, bias check |
| Future projection from a process model | Multi-model ensemble | Structural + parameter + scenario spread shown |

## Worked micro-example (illustrative)

A warming-experiment meta-analysis pools log response ratios (lnRR) of aboveground biomass from 64
studies. A defensible GCB workflow: fit a random-effects model, report the pooled lnRR back-transformed
to a percentage with its interval, and quantify heterogeneity. Illustrative output — pooled lnRR 0.12,
i.e. a +13% biomass response (95% CI 6–20%), I^2 = 71% with tau^2 = 0.04, and a moderator showing the
effect halves in water-limited sites. The funnel plot and trim-and-fill leave the sign unchanged. The
71% heterogeneity is the result, not noise: it motivates the moisture moderator. All numbers illustrative.

## Referee pushback patterns and the GCB-appropriate fix

- "Pseudoreplication: chamber treated as replicate" → move the treatment effect to a random-effect or
  split-plot structure at the true unit of inference.
- "Heterogeneity ignored in the synthesis" → report I^2/tau^2 and pre-specified moderators, not a single
  pooled mean.
- "Projection has no uncertainty band" → run an ensemble and partition parameter, structural, and
  scenario spread rather than reporting one trajectory.
- "Skill claimed but never tested out-of-sample" → report validation against held-out observations and
  the conditions where the model fails.

## Anti-patterns

- Treating nested/repeated/spatial data as independent observations
- Stars-only results with no effect sizes, intervals, or ecological magnitude
- A single model run reported as if it had no structural or scenario uncertainty
- A meta-analysis with no heterogeneity or publication-bias assessment
- Code that cannot reproduce the printed tables/figures ("works on my machine")

## Output format

```
【Main estimate】effect size + interval + ecological/biogeochemical meaning
【Data structure】random effects / autocorrelation handled? [Y/N]
【Uncertainty】measurement + parameter + structural + scenario partitioned?
【Model evaluation / heterogeneity】skill metrics or I^2 reported?
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】gcb-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — mixed-model, meta-analysis, spatial, and modelling packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data/code archiving policy
