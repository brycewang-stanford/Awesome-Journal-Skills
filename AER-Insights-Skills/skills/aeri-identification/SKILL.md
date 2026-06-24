---
name: aeri-identification
description: Use when the identification argument is the bottleneck for an American Economic Review: Insights (AER: Insights) short-format manuscript — causal identification in an empirical design, parameter identification in a structural model, or treatment-effect identification in an experiment. Stress-tests the strategy so it is clean enough to defend in a few pages, before exhibits are finalized.
---

# Identification — Clean Enough to Defend Short (aeri-identification)

## When to trigger

- The single headline result rests on OLS + controls, or TWFE on staggered timing
- A structural parameter is estimated but it is unclear *what in the data* identifies it
- An experiment's estimand or assumptions are not pinned down
- You are unsure the identification is clean enough to carry a *short* paper

## The AER: Insights identification bar

A short paper has **no room to rescue a weak design** with pages of robustness. The identification must be **clean, transparent, and self-contained** — the central exhibit and one or two sentences should make a non-specialist believe the headline number. Because AER: Insights papers are one insight at AER-level importance, the design is held to AER credibility but expressed with extreme economy: state the **data-to-object mapping in one sentence**, show the **single most convincing diagnostic in-text**, and move the rest to the Supplemental Appendix. AEA house style: report **standard errors / confidence sets**, not significance asterisks, and make everything reproducible for the AEA Data Editor.

## Branch paths

### Branch A: Empirical causal design (the most common AER: Insights paper)
- **DiD / event study:** with staggered adoption move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); the **single event-study figure with clean leads** is often the paper's central exhibit.
- **RDD:** density test (Cattaneo–Jansson–Ma), optimal bandwidth, covariate smoothness, bias-corrected CIs; one well-made RD plot can be the whole identification.
- **IV:** strong first stage; weak-IV-robust inference (Anderson–Rubin) if needed; defend the exclusion restriction in one tight paragraph.
- Inference clustered at the assignment level; few-cluster fixes (wild-cluster bootstrap).

### Branch B: Experiment (own data)
- Pre-registration in a recognized registry; report deviations.
- Randomization balance, attrition (Lee bounds if differential), pre-specified primary estimand, multiple-hypothesis control if more than one outcome.
- The headline is one pre-registered effect — resist reporting every arm in-text.

### Branch C: Structural / parameter identification
- **Name what identifies the key parameter** from a specific data moment, in one sentence — a short paper cannot hide behind "the likelihood."
- Report the sensitivity of the headline parameter to the moment that moves it; Monte Carlo recovery in the appendix.
- Keep the model minimal ([`aeri-theory-model`](../aeri-theory-model/SKILL.md)) — only what the single insight needs.

### Branch D: New fact / measurement
- Documented construction; show the fact is not a measurement artifact with the one most threatening alternative addressed in-text, others in the appendix.

## Choosing the single in-text diagnostic

You have **at most five exhibits total** and the identification competes with the result for that budget. Pick the **one diagnostic** that most directly defends the design (the event-study leads, the RD plot, the first-stage, the balance table) for in-text; everything else (placebo cuts, alternative bandwidths, all balance rows) goes to the appendix.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AER: Insights is a short format built around one decisive result, so the body/appendix split is even tighter — run the design cleanly the first time.

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Checklist

- [ ] Branch chosen; **data-to-object mapping stated in one sentence**
- [ ] The single most convincing diagnostic is identified for in-text placement
- [ ] Empirical: modern estimator where TWFE would bias; design diagnostic shown
- [ ] Experiment: pre-registered; primary estimand pre-specified; balance/attrition handled
- [ ] Structural: key parameter tied to an identifying moment; sensitivity reported
- [ ] Inference as SEs / confidence sets (no asterisks); clustering level correct
- [ ] The headline claim never exceeds what the identification supports

## Anti-patterns

- Relying on a wall of robustness to compensate for a weak core design (no room for it)
- TWFE on staggered treatment with no heterogeneity-bias discussion
- Reporting every experimental arm/heterogeneity split in-text instead of one estimand
- "The estimator converged" presented as identification (structural)
- Significance asterisks instead of standard errors / confidence sets

## Referee pushback mapped to the fix

- *"OLS with controls is not identification."* → Move to a design (DiD/RDD/IV/experiment) or reframe scope; one clean design beats many controls.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show flat leads in the central figure.
- *"Which moment identifies this parameter?"* → One sentence + a sensitivity number; recovery Monte Carlo in the appendix.

## Output format

```
【Branch】empirical / experiment / structural / measurement
【Data-to-object mapping】one sentence
【In-text diagnostic】<the single most convincing exhibit>
【Inference】SEs / confidence sets (no asterisks); clustering level
【To the appendix】placebos / alt bandwidths / full balance / MC recovery
【What it does NOT identify】[…]
【Next step】aeri-robustness (or aeri-theory-model if structural)
```
