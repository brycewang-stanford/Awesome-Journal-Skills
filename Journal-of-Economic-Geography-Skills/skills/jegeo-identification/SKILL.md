---
name: jegeo-identification
description: Use when the inference argument is the bottleneck for a Journal of Economic Geography (JEG) manuscript — spatial causal designs, quantitative-spatial model identification, or case-based geographic inference. Stress-tests the strategy to JEG's two-community bar before exhibits are finalized.
---

# Identification Strategy (jegeo-identification)

## When to trigger

- A spatial regression rests on OLS + region fixed effects, or TWFE on staggered place-based policy
- A quantitative-spatial / NEG model is estimated but it is unclear *what in the spatial data* identifies the key elasticities
- Treatment in one region plausibly spills over to "control" regions (SUTVA across space is violated)
- A qualitative/comparative-case paper makes a causal-sounding claim with no explicit logic of inference
- You are unsure the strategy reads as credible to BOTH an economist and a geographer

## The JEG identification bar

Because JEG bridges geographical economics and human geography, "identification" means different things by branch — but in all of them the **spatial structure of the data is part of the identification problem, not a nuisance**. Two threats are nearly universal at JEG and referees expect them confronted head-on: **spatial autocorrelation** in errors (inference) and **spatial spillovers / general-equilibrium leakage** across units (SUTVA). Pick the branch and make the data-to-claim mapping explicit.

## Branch A: Spatial causal design (place-based policy, regional treatment)

- **Spatial DID / event study:** with staggered adoption move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show clean event-study leads; report a Goodman-Bacon decomposition.
- **Spillovers / SUTVA across space:** the control region is often the treated region's neighbor. Use donut/ring specifications, model spatial spillovers explicitly, or argue why leakage is bounded — do not assume independence across adjacent units.
- **Spatial RDD / border designs:** geographic discontinuities (administrative borders) are powerful but demand a continuity argument across the border and attention to what else changes at it.
- **IV with a spatial instrument:** Bartik/shift-share and geography-based instruments are common; defend exogeneity of the shares (Goldsmith-Pinkham et al.) or of the shocks, not just first-stage strength.
- **Inference:** cluster at the spatial-treatment level AND address spatial correlation across clusters with Conley spatial-HAC standard errors; report how the cutoff distance was chosen.

## Branch B: Quantitative-spatial / NEG model identification

- **Name what identifies each structural elasticity** (trade elasticity, agglomeration elasticity, migration elasticity) — tie it to specific spatial variation or moments, not "the estimator converged."
- **Calibration vs. estimation:** if elasticities are borrowed, say from where and show the counterfactual is not driven by an indefensible borrowed value; report sensitivity.
- **General-equilibrium counterfactuals:** the headline welfare/relocation number depends on the model's spatial linkages — show which parameters and which spatial structure move it.

## Branch C: Case-based / qualitative geographic inference

- Make the **logic of inference explicit**: comparative cases, process tracing, or theory-building from a critical case — and state what would have falsified the claim.
- Justify case selection on substantive spatial grounds; address generalizability rather than claiming it.

## Shift-share / Bartik instruments in a spatial setting

Shift-share instruments are pervasive in economic geography (regional exposure to national shocks via local industry mix), and JEG referees scrutinize them closely. Two defenses, two literatures:

- **Exogenous shares (Goldsmith-Pinkham–Sorkin–Swift):** identification rests on the pre-period industry shares being as-good-as-random; defend the shares' exogeneity and report the Rotemberg weights that show which industries drive the estimate.
- **Exogenous shocks (Borusyak–Hull–Jaravel):** identification rests on many quasi-random national shocks; defend the shocks and the equivalent shock-level regression.

State which justification you rely on — "we use a Bartik instrument" without naming the identifying assumption is exactly the move a JEG referee flags.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG is spatial economics — spatial dependence and sorting; emphasize identification and Conley/spatial-robust inference.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the spatial-data-to-claim mapping stated in one sentence
- [ ] Spatial autocorrelation addressed in inference (Conley SEs / appropriate clustering; cutoff justified)
- [ ] Cross-unit spillovers / SUTVA across space confronted, not assumed away
- [ ] Staggered designs use a modern estimator; pre-trends/leads shown
- [ ] Structural: each key elasticity tied to identifying spatial variation; counterfactual sensitivity shown
- [ ] Qualitative: explicit inference logic + falsification condition + case-selection justification
- [ ] The claim never exceeds what the spatial design supports

## Anti-patterns

- Default heteroskedastic SEs (or clustering on one dimension) when errors are spatially correlated
- Treating neighboring regions as clean controls while the treatment spills across the border
- TWFE on staggered place-based policy with no heterogeneity-bias discussion
- "The estimator converged" offered as structural identification of agglomeration/trade elasticities
- A qualitative paper making a causal claim with no stated logic of inference or falsifier
- Reporting significance with asterisks instead of standard errors and confidence intervals

## Worked vignette (illustrative)

A special economic zone is rolled out across regions and the paper estimates its effect on firm entry with TWFE and region-clustered SEs. Two JEG referees object: the economist says the zones were placed where growth was already accelerating (selection) and neighboring regions absorbed displaced firms (spillover inflates the gap); the geographer says "region" is the wrong scale because clusters cross administrative lines. The fix routes through all three: a Callaway–Sant'Anna estimator with clean leads (selection on trends), a ring specification isolating displacement (spillover), Conley SEs at a justified distance (spatial correlation), and a re-aggregation to commuting zones (scale). Only then is the entry effect — say a 6% rise, illustrative — credible to both readers.

## Referee pushback mapped to the identification fix

- *"Your control regions are the treated region's neighbors — spillover inflates the effect."* → Add ring/donut specs or a spatial-lag model; report the bounded effect net of displacement.
- *"Standard errors ignore that adjacent units co-move."* → Conley spatial-HAC SEs over a range of cutoffs; show residual Moran's I.
- *"The agglomeration elasticity is calibrated, not identified."* → Name the spatial variation that pins it; show the counterfactual is not driven by a borrowed value.
- *"This is a region case study calling itself causal."* → State the inference logic and the falsifier explicitly, or downgrade the causal language.
- *"The result is an artifact of the spatial unit."* → Re-estimate at another scale (the MAUP test) — partly a robustness move, but raised at identification.

## Why spatial inference is non-negotiable at JEG

Economic-geography data violate the independence assumption almost by construction: nearby places share shocks, labor markets, and institutions. A JEG referee from the economics side treats overstated inference as a fatal flaw, and one from the geography side treats "space as iid error" as conceptually naive. Confronting spatial autocorrelation and spillovers is therefore not a robustness afterthought here — it is part of whether the design identifies anything at all. Decide the spatial error structure and the spillover structure *before* you read the point estimate, so the inference is not reverse-engineered to keep significance.

## Output format

```text
【Branch】spatial-causal / quantitative-spatial-model / qualitative-case
【Spatial-data-to-claim mapping】one sentence
【Spatial autocorrelation】inference fix (Conley / clustering; cutoff)
【Spillovers / SUTVA across space】how confronted
【Identification evidence】leads+Bacon / elasticity-to-variation / inference logic
【What it does NOT identify】[...]
【Next skill】jegeo-theory-model
```
