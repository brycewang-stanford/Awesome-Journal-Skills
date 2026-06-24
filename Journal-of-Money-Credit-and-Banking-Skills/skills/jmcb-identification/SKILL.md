---
name: jmcb-identification
description: Use when the identification argument is the bottleneck for a Journal of Money, Credit and Banking (JMCB) manuscript — macro shock identification (SVAR, narrative, sign/high-frequency monetary surprises), parameter identification in a monetary/banking model, or a micro-banking causal design. Stress-tests the data-to-object mapping to the JMCB bar before exhibits are finalized.
---

# Identification Strategy (jmcb-identification)

## When to trigger

- A monetary-policy "shock" is just a residual from a regression, with no defense against the information effect
- An SVAR's ordering / sign restrictions are unstated or unmotivated by theory
- A bank/loan-level causal claim rests on OLS + controls, or TWFE on staggered regulation
- A banking-model parameter is "calibrated" with no statement of what in the data pins it
- You are unsure the identification clears JMCB's policy-relevant, mechanism-explicit bar

## The JMCB identification bar

JMCB referees are monetary/banking economists who judge identification by **whether the data-to-object mapping is explicit, theory-disciplined, and robust to the field's known critiques**. Because the journal spans macro and micro, "identification" means different things by engine — pick the engine and make the argument transparent, with timing and institutions on the page. The dominant failure mode JMCB punishes is a "shock" or "treatment" that is not exogenous to the thing it is supposed to move.

## Branch paths

### Branch A: Macro shock identification (SVAR / narrative / external instruments)
- **High-frequency monetary surprises:** identify off tight windows around FOMC/ECB announcements (Kuttner; Gürkaynak–Sack–Swanson factors; Gertler–Karadi external instrument). **Defend against the information effect** (Nakamura–Steinsson; Jarociński–Karadi sign decomposition or poor-man's sign restrictions) — a surprise that moves rates *and* raises growth forecasts is not a clean policy shock.
- **SVAR ordering / sign restrictions:** motivate every restriction from theory or institutions; report sensitivity to the ordering and to the restriction set; for set-identified models report the full identified set, not a single draw.
- **Narrative shocks** (Romer–Romer style): document the construction, the information set, and orthogonalization to forecasts.
- **IRF inference:** report bands that match the method (e.g., bias-corrected/bootstrap for VARs; lag-robust / HAR for local projections); state the local-projection vs. VAR choice and why.

### Branch B: Structural monetary / banking model identification
- **Name what identifies each parameter** — tie it to a moment or institutional fact, not "the estimator converged." For a banking-friction model, say which data feature (loan spreads, deposit betas, capital ratios) disciplines the friction.
- **Targeted vs. untargeted moments:** report fit to targeted moments and validate on untargeted ones.
- **Policy-invariance:** argue the parameters survive the counterfactual you run (Lucas critique) — central to JMCB's policy use.
- Report estimation regularity (objective, multi-start, Monte Carlo recovery) when estimated rather than calibrated.

### Branch C: Micro-banking causal design (bank / loan / firm panel)
- **Staggered policy/regulation:** move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show clean event-study leads; Goodman-Bacon decomposition.
- **Khwaja–Mian style:** absorb credit demand with firm×time (or industry×region×time) fixed effects to isolate bank-driven credit supply — the workhorse banking identification; state explicitly that you net out demand.
- **IV / Bartik credit-supply shifters:** strong first stage (effective F); defend exclusion; for shift-share defend share or shock exogeneity.
- **Inference:** cluster at the treatment-assignment level (often bank and time, two-way); address few-cluster issues (wild-cluster bootstrap); Driscoll–Kraay if cross-sectional dependence is a concern.

## Referee pushback mapped to the identification fix

- *"Your monetary-policy shock is contaminated by the information effect."* → Decompose the surprise into pure-policy and information components (Jarociński–Karadi sign restrictions, or orthogonalize to Greenbook/Blue-Chip forecast revisions); show the IRF is robust to the cleaned shock.
- *"The SVAR result is an artifact of your recursive ordering."* → Report the headline IRF under alternative orderings and a theory-motivated sign-restriction scheme; for set-identified models show the full identified set.
- *"You measure credit demand, not supply."* → Absorb demand with firm×time (or industry×region×time) fixed effects, à la Khwaja–Mian; report the within-firm cross-bank coefficient.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"Your calibrated parameters won't survive the counterfactual."* → Argue policy-invariance (Lucas critique); show the parameters are not functions of the policy you change.
- *"Standard errors are understated."* → Two-way cluster (bank and time) or wild-cluster bootstrap with few clusters; Driscoll–Kraay for cross-sectional dependence.

## Matching identification to the JMCB policy use

A JMCB identification argument is not complete until it connects to the policy question. A clean shock that identifies an IRF still needs the reader to see *which policy lever* the response speaks to; a clean bank-supply coefficient still needs the reader to see *what it implies for transmission or regulation*. State the estimand in policy-relevant units (a transmission elasticity, a pass-through, a welfare number) so the identification serves the contribution rather than standing alone as a methodological exercise.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMCB is monetary/banking — macro time series + bank panels; local projections for the macro lane, DiD/IV for the bank lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Engine chosen (macro shock / structural / micro-banking); data-to-object mapping in one sentence
- [ ] Macro: surprise defended against the information effect; IRF bands match the method
- [ ] Structural: each parameter tied to identifying moments/facts; policy-invariance argued for the counterfactual
- [ ] Micro: credit demand absorbed (firm×time) where the claim is credit *supply*; modern estimator where TWFE would bias
- [ ] Inference matched to design; clustering level stated; few-cluster handled
- [ ] The claim never exceeds what the identification supports

## Anti-patterns

- A "monetary policy shock" that is a raw regression residual with no information-effect defense
- SVAR sign/ordering restrictions presented as innocuous when they drive the headline IRF
- Reading a bank-lending response as credit *supply* without absorbing credit *demand*
- TWFE on staggered bank regulation with no heterogeneity-bias discussion
- "Calibrated to the literature" standing in for an identification argument in a model paper
- One-way clustering on a bank×time panel where shocks are correlated across banks within a period

## A note on local projections vs. VARs

JMCB publishes both, and referees will ask why you chose one. Local projections are flexible and robust to misspecification of the dynamics but can be imprecise at long horizons; VARs are efficient but impose the full system. State the trade-off you made: if the IRF shape is the contribution, a referee may want the LP for transparency *and* a VAR for efficiency as a cross-check. When the two disagree materially, that disagreement is informative and should be reported, not buried.

## Worked vignette (illustrative)

A paper claims monetary tightening cuts lending most at low-capital banks. The first draft uses the FOMC-day change in the 2-year yield as the shock and bank-level OLS. A JMCB referee raises two objections: the surprise is contaminated by the information effect, and the lending response could be demand, not supply. The fix: purge the surprise of the forecast-revision component (Jarociński–Karadi), and re-estimate with firm×quarter fixed effects so identification comes from within-firm variation across banks of different capital. The capital-interaction settles at −0.6pp per 25bp for the lowest-capital quartile (s.e. 0.2, illustrative), now defensible as supply.

## State what you do NOT identify

The fastest way to lose a JMCB referee is to claim more than the design supports. A within-firm bank-supply coefficient identifies the *supply* margin, not the general-equilibrium effect on aggregate credit (firms may substitute to other banks). A high-frequency surprise identifies the *announcement-window* response, not the full effect of a sustained policy stance. A local-at-cutoff or LATE estimate is not the population effect. Name the boundary explicitly in the paper — a referee who sees you already know the limit is far more likely to accept the contribution than one who has to point it out.

## Output format

```text
【Engine】macro-shock / structural / micro-banking
【Data-to-object mapping】one sentence
【Identification evidence】[HF-surprise + info-effect defense / moments + invariance / firm×time + first-stage]
【Estimation/inference】method + bands/SEs + clustering level + few-cluster fix
【What it does NOT identify】[...]
【Next skill】jmcb-empirical-design
```
