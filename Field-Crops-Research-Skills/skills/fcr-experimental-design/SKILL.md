---
name: fcr-experimental-design
description: Use when designing or defending the field-experiment or modelling design of a Field Crops Research (FCR) manuscript — multi-environment trials, randomization and replication, blocking and split-plot layouts, genotype-by-environment (G×E) structure, and crop-model calibration/validation. FCR expects field experiments to span at least two seasons and/or multiple environments. Strengthens the design; it does not write code.
---

# Experimental Design (fcr-experimental-design)

FCR is demanding about **field-experimental rigour**. The design must credibly connect the agronomic
question to evidence that generalises across environments. The single most important FCR-specific rule:
field experiments should, unless exceptional circumstances apply, span **at least two seasons and/or
multiple locations/environments**. Design for that from the start.

## When to trigger

- Planning a multi-environment trial (MET) or a season×site×treatment layout
- A reviewer questioned randomization, replication, blocking, or G×E inference
- Deciding how to characterise environments (soil, weather, phenology)
- Designing a crop-modelling study (calibration/validation, scenario design)

## Field-experiment design essentials

- **Multi-environment by design.** Plan ≥ 2 seasons and/or multiple sites; define what an
  "environment" is (site×year, managed water/N regime). State why the set spans the target population
  of environments.
- **Randomization & replication.** Use a proper randomized design (RCBD, **resolvable
  incomplete-block / alpha-lattice**, split-plot for factor hierarchies, strip-plot, augmented for many
  genotypes). State replication per environment and the randomization procedure — not "plots were
  arranged."
- **Blocking & spatial control.** Block against known field gradients; plan for **spatial analysis**
  (e.g., row/column or P-spline) where fields are large or heterogeneous.
- **Plot management detail.** Plot size, borders/guard rows, sowing density, dates, and the management
  applied — enough to reproduce the experiment.
- **Environment characterisation.** Record **soil and weather** and present weather **in relation to
  crop phenology**; this is what lets readers interpret G×E.

## Genotype/treatment × environment (G×E)

- Decide up front how G×E will be modelled: factorial structure, which effects are **fixed vs.
  random**, and how environments enter (random sample vs. fixed targets).
- Plan stability/adaptation analyses (Finlay–Wilkinson regression, **AMMI**, **GGE biplot**) where
  ranking across environments is the question.

## Crop-modelling design

- State the model and **version**, the **cultivar coefficients**, and the **calibration vs.
  validation** split (independent data, not the same trials).
- Justify the scenario/factor design and the environments simulated; report what the model **adds**
  beyond the field data (extrapolation, yield-gap decomposition, generalisation).

## The generalisation test (FCR-specific)

For your design, write one sentence: *"These environments represent ___, so the result is expected to
hold for ___ (and not for ___)."* If you cannot, the design does not yet support a general,
FCR-worthy claim — add environments or scope the claim.

## Design-choice decision table (match layout to the question)

FCR referees expect the layout to follow from the agronomic question and the field's structure, with a
named design and stated randomization. Pick — and justify — before committing plots.

| Situation | Design FCR expects | Note |
|-----------|--------------------|------|
| One factor, field gradient | RCBD, blocks across the gradient | name blocks, give replication |
| Many genotypes, few reps | Resolvable incomplete block / **alpha-lattice** | recover inter-block information |
| Factor hierarchy (irrigation × N) | Split-plot (water = whole-plot) | report whole-plot + sub-plot error |
| Large/heterogeneous field | RCBD/lattice **+ spatial model** (row–column, P-spline) | pre-plan the spatial term |
| Genotype ranking across environments | MET, environments a random sample | enables AMMI/GGE, stability inference |

## Sizing anchors (illustrative, hedged)

No universal minimum exists, but FCR's ≥2-seasons/-environments expectation points to norms worth
calibrating against — as *illustrative anchors* (confirm against your own variance): MET genotype
trials often run **≥6–8 site-years** before stability inference is credible; replication is commonly
**3–4 blocks** per environment; a response curve wants **≥4–5 levels**.

## Worked design vignette (illustrative)

*Illustrative; the logic is the lesson.* A team wants to claim a new wheat cultivar yields more under
reduced N. A weak design — **1 site, 1 season, cultivar unreplicated** — cannot separate cultivar from
field position and yields no G×E information. The FCR-grade redesign: **2 seasons × 4 sites (8
environments)** on a soil-N gradient, **split-plot** (N as whole-plot, cultivar as sub-plot), **4 blocks
per environment**, **5 N levels** for a response curve, and a **row–column spatial term** — making the
cultivar × N × environment surface identifiable and testable across environments.

## Anti-patterns

- One site, one season presented as sufficient (fails the multi-environment expectation)
- "Randomized" asserted with no design named, no replication count, no layout
- Treating a controlled-environment study as the main evidence (out of scope — see `fcr-topic-selection`)
- Ignoring spatial heterogeneity in large fields; pseudoreplication (sub-samples treated as reps)
- Calibrating and validating a model on the same data

## Output format

```
【Design】RCBD / alpha-lattice / split-plot / MET / modelling
【Environments】#seasons × #sites; what they represent
【Randomization & replication】procedure + reps per environment
【G×E plan】fixed/random structure; stability analysis if relevant
【Environment characterisation】soil + weather vs. phenology recorded? [Y/N]
【Generalisation sentence】represents ___ → holds for ___
【Next】fcr-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design packages (agricolae, FielDHub) and crop models (APSIM, DSSAT, STICS)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — the ≥2-seasons/-environments rule and reproducibility expectations
