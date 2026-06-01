---
name: rje-data-analysis
description: Use when executing and stress-testing the empirical analysis for a RAND Journal of Economics (RJE) industrial-organization manuscript — estimating structural demand/supply, entry, auction, or reduced-form models, then running the robustness, counterfactual, and inference checks IO referees expect. Analysis discipline, not study design.
---

# Data Analysis & Robustness (rje-data-analysis)

## When to trigger

- Estimates are in hand and you need the robustness suite IO referees demand
- A structural counterfactual needs validation before it goes in the article
- You must report inference correctly for market-level / clustered data

## Analysis norms at the IO flagship

RJE referees apply **industrial-organization empirical norms**. Whether the work is structural or reduced-form, the analysis must show the estimates are **credible, well-behaved, and economically sensible**, and that **counterfactuals are disciplined** by the model.

### Structural work
- **Estimation diagnostics:** report objective-function value, convergence, and sensitivity to **starting values** (non-convex objectives); use multiple starts and report them.
- **Economic sanity:** elasticities, markups, and marginal costs in plausible ranges; own-price elasticities negative and large enough for positive markups.
- **Identification-in-practice:** show which moments move which parameters (sensitivity / informativeness of moments).
- **Counterfactuals:** state maintained assumptions (e.g., fixed product set, conduct unchanged), report them as ranges/bounds, and validate against any out-of-sample episode (a known merger, entry, or price change).

### Reduced-form work
- **Modern DID** where timing is staggered (Callaway–Sant'Anna / Sun–Abraham), with event-study leads and a Goodman-Bacon decomposition.
- **Weak-IV-robust inference** where instruments are weak; report the first-stage F.
- **Placebo / falsification** on markets or periods that should not respond.

### Inference (both)
- Cluster at the level of treatment/market variation; with few clusters use **wild-cluster bootstrap**.
- Set and report **seeds** for simulation, bootstrap, and randomization.

## Robustness suite to stage

- Alternative demand specification / functional form (structural) or alternative controls and sample (reduced-form)
- Alternative instruments and conduct assumptions
- Subsample and alternative market-definition checks
- Sensitivity of the headline **counterfactual / welfare** number to key assumptions

## Page-cap discipline

RJE's caps are hard (main text **<=40 pp**, total **<=50 pp**). Put the core estimates and one or two decisive robustness exhibits in the main text; **move the full robustness battery to the appendix** (within the <=10-page appendix+references budget), not into discouraged supporting information.

## Anti-patterns

- A single structural run with no starting-value or specification sensitivity
- Counterfactuals reported as point estimates with no assumption bounds
- TWFE on staggered policy timing presented as the headline
- Default robust SEs when variation is at the market level

## Output format

```
【Estimator】structural (demand/conduct/entry/auction) / reduced-form
【Economic sanity】elasticities/markups plausible? [Y/N]
【Robustness done】[specifications, instruments, conduct, subsamples]
【Counterfactual】assumptions stated + bounded? [Y/N]
【Inference】clustering / weak-IV / seeds set? [Y/N]
【Page budget】main robustness in appendix? [Y/N]
【Next step】rje-tables-figures
```
