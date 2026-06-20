---
name: jue-theory-model
description: Use when a Journal of Urban Economics (JUE) manuscript needs a spatial model to interpret its mechanism — a spatial-equilibrium frame, a sorting model, or a quantitative spatial model (QSM) for counterfactuals. Builds the theory that disciplines the empirics; it does not establish the identification (jue-identification) or run robustness (jue-robustness).
---

# Spatial Theory & Model Craft (jue-theory-model)

## When to trigger

- A reduced-form spatial result needs a mechanism that interprets the magnitude
- A referee asks "what does this estimate mean in equilibrium, once agents re-sort?"
- The paper wants **counterfactuals** (a policy, an infrastructure change) that require a quantitative spatial model
- The empirical object (a density-wage elasticity, a capitalization rate) maps to a structural parameter you have not named
- You are choosing how much model the paper needs: a one-equation Rosen–Roback wedge or a full QSM

## How much model does a JUE paper need?

JUE is empirically led, but referees expect theory to **discipline interpretation**, not decorate it. Match the model to the claim:

| The claim is... | The model you need | Pitfalls |
|-----------------|--------------------|----------|
| "this amenity/disamenity is valued at X" | Rosen–Roback capitalization, wages + rents jointly | using only prices ignores the wage margin and the worker indifference condition |
| "agglomeration raises productivity by Y" | sharing/matching/learning micro-foundation; sorting vs spillover decomposition | attributing sorting of high types to true agglomeration |
| "policy/infrastructure changes welfare by Z" | quantitative spatial model with mobility, trade/commuting, housing | counterfactual not invariant to the policy; ignored general-equilibrium reallocation |
| "households sort on local public goods" | Tiebout / discrete-choice sorting model | treating sorting as exogenous; no equilibrium in prices |
| "market access drives outcomes" | gravity/market-access (Donaldson–Hornbeck, ARSW) | endogenous network; access measured without the structural weight |

## Spatial-equilibrium discipline

1. **Respect the indifference/zero-profit conditions.** In a Rosen–Roback world a local change that looks like a pure benefit is partly capitalized into rents and partly offset by wage adjustment. A JUE referee will ask where the incidence falls — land, labor, or firms.
2. **Close the model where agents move.** If your empirical comparison holds location fixed but theory says agents re-sort, the reduced form is a short-run object; say so and bound the long-run.
3. **For a QSM, tie every parameter to data.** State which moment or reduced-form estimate identifies each elasticity (migration, commuting, housing supply, agglomeration). Report sensitivity of counterfactuals to the parameters that are least well identified.
4. **Argue invariance for counterfactuals.** The estimated elasticities must be policy-invariant enough for the experiment you run (a spatial Lucas critique).
5. **Use theory to sign and bound, not to over-claim.** The most persuasive JUE theory section delivers a comparative static the data then confirms.

## Checklist

- [ ] The model is matched to the claim (capitalization / agglomeration / QSM / sorting / market access)
- [ ] Spatial-equilibrium conditions (indifference, zero-profit, market clearing) are respected
- [ ] Incidence is located: who bears the change — land, labor, or firms
- [ ] Short-run (location fixed) vs long-run (re-sorting) is distinguished
- [ ] QSM: each structural parameter is tied to an identifying moment/estimate; counterfactual sensitivity reported
- [ ] Counterfactual parameters argued policy-invariant
- [ ] Open-city vs closed-economy assumption stated and defended for the geographic scale
- [ ] The model is load-bearing (removing it makes an estimate uninterpretable), not decorative
- [ ] Theory yields a comparative static the empirics actually test

## Anti-patterns

- A reduced-form result with no mechanism, leaving the magnitude uninterpretable
- Reading a capitalization estimate from prices alone, ignoring the wage and the worker indifference margin
- Attributing the density-wage elasticity to agglomeration when it is sorting of high-productivity workers
- A QSM whose counterfactual rests on parameters never tied to data, or whose elasticities are not policy-invariant
- Decorative theory: a model that does not change how any estimate is read
- Ignoring general-equilibrium reallocation, so a local gain is reported as a national welfare gain

## Referee pushback mapped to the theory fix

- *"What does this mean once households re-sort?"* → Embed the estimate in a spatial-equilibrium model; report the short-run (location fixed) vs long-run (re-sorting) effect and where incidence lands.
- *"Is this agglomeration or sorting of high types?"* → Add the sharing/matching/learning micro-foundation and a decomposition that separates true spillovers from compositional sorting.
- *"Your counterfactual parameters are not policy-invariant."* → Argue invariance explicitly (spatial Lucas critique); show the elasticities are primitives, not functions of the policy.
- *"The model is decorative."* → Derive a comparative static the data then tests; if the model changes no estimate's interpretation, cut it.

## Calibrate vs estimate

JUE accepts both calibrated and estimated spatial models, but the referee asks the same question: *what disciplines the parameters?* For a calibrated QSM, cite the external estimates each elasticity comes from and report counterfactual sensitivity to the least-credible one. For an estimated model, name the moment or reduced-form variation that identifies each parameter (this hands off to `jue-identification`). Either way, the counterfactual's credibility is only as strong as the weakest-identified elasticity — surface it rather than hiding it in an appendix.

## Open vs closed city, and why it matters here

A recurring JUE referee question is whether your setting is an **open city** (migration equalizes utility, so local shocks capitalize into land and dissipate in welfare terms) or a **closed economy** (population fixed, effects fall on prices and quantities differently). The choice changes the sign and incidence of your comparative statics: in an open-city model a local amenity gain is fully capitalized into rents with no utility change, whereas in a closed model it raises resident welfare. State which assumption you make and defend it for your geographic scale — a single metro is more open than a national system. Getting this wrong is a common interpretation error referees flag.

## Worked vignette (illustrative)

A paper estimates that a zoning relaxation raised housing units in treated tracts. Reduced form alone cannot say whether welfare rose, because households re-sort and rents adjust elsewhere. The JUE theory move: embed the estimate in a small spatial-equilibrium model with mobility and housing supply, calibrate the supply elasticity to the reduced-form response and the migration elasticity to prior estimates, and report the welfare counterfactual with sensitivity to the migration elasticity (the least-identified parameter). The model shows the local rent decline is partly undone by in-migration — a comparative static the data then supports.

## Where the model lives in the paper

JUE referees punish theory that is either missing or overgrown. A reduced-form paper usually needs only a compact framework — a few equations stating the indifference/zero-profit conditions and the comparative static the data tests — placed before the empirics so the estimate has meaning when it arrives. A structural paper carries a fuller model but should still front-load the intuition and relegate derivations to an appendix. The test in both cases: remove the model and ask whether any estimate changes meaning. If nothing changes, the model is decoration; if the magnitude becomes uninterpretable, the model is load-bearing and belongs in the main text.

## Output format

```text
【Claim type】capitalization / agglomeration / QSM-counterfactual / sorting / market-access
【Model chosen】one line — and why this much model
【Equilibrium conditions】indifference / zero-profit / clearing respected? [Y/N]
【Incidence】land / labor / firms
【Run vs long-run】short-run (fixed location) vs long-run (re-sorting)
【QSM params → data】each elasticity tied to a moment; sensitivity reported?
【Comparative static tested】[...]
【Next skill】jue-robustness
```
