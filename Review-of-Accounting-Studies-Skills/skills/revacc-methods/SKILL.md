---
name: revacc-methods
description: Use when research design and identification are the bottleneck for a Review of Accounting Studies (RAST) manuscript — choosing the setting, shock, and design that credibly identify an accounting effect, or fixing the primitives and solution concept of an analytical model. Designs the study; it does not run the estimation and robustness (revacc-data-analysis) or frame the contribution (revacc-contribution-framing).
---

# Research Design & Identification (revacc-methods)

## When to trigger

- Your treatment (a disclosure, a standard adoption, an audit/tax regime) may be endogenous
- Adoption is staggered across firms/years and you need a defensible DiD
- You have an association and a referee will ask "is this causal or just correlation?"
- You are designing an experiment to isolate a channel archival data cannot separate
- You are building an analytical model and must fix primitives, timing, and the equilibrium concept

## Identification for archival accounting at RAST

Accounting treatments — disclosure choices, conservatism, auditor selection, tax positions, standard adoption — are rarely random, so RAST referees expect a **credible identification strategy**, not kitchen-sink controls. Pick the design that breaks the endogeneity for *your* accounting setting.

| Identification threat / setting | Design |
|---------------------------------|--------|
| Regulation / standard adoption with a clean date (e.g., a reporting mandate) | Difference-in-differences; event study around the adoption date |
| Staggered adoption across firms/states/countries | Staggered DiD with modern estimators (avoid naive TWFE bias) |
| Endogenous accounting/auditor/tax choice | Instrumental variables / 2SLS with a defensible exclusion |
| A threshold rule (covenant, index inclusion, size or regulatory cutoff) | Regression discontinuity |
| Selection on observables | Matching (PSM/entropy) as a complement, not the main claim |
| A plausibly exogenous shock to the information environment | Natural experiment; pre-trends shown |
| Information content of an accounting signal | Short-window event study with a clean benchmark and confound check |

State the **estimating equation**, the **unit and level**, the **fixed effects** (firm, year, industry-year), and the **identifying variation** explicitly. The design section must make a skeptic believe the variation is as-good-as-random conditional on controls. RAST's first-round-decision culture means a weak design is more likely to draw a reject than a "fix it in revision."

## Measurement design is part of identification

For contested accounting constructs (discretionary accruals, earnings quality, disclosure indices, audit quality, information asymmetry), the **proxy choice is a design decision**. Pre-commit a primary measure with precedent and plan the alternative proxies you will use to show the result is not proxy-driven (carried out in `revacc-data-analysis`). A clean design on a fragile proxy still fails.

## If the lane is analytical

- Fix the **information structure, players, timing, and payoffs** before solving; state the equilibrium concept (PBE, sequential, etc.).
- Show the model is the **minimal** structure that generates the accounting result; defend each assumption as load-bearing.
- Plan the comparative statics that become testable or normative accounting implications.

## If the lane is experimental

- Manipulate the focal accounting construct with realistic stimuli and a fit-for-purpose pool (investors, auditors, managers); IRB documentation is expected.
- Pre-register where feasible; include manipulation and attention checks; power the design for the **interaction**, not just the main effect.

## Design hygiene

- Show **parallel pre-trends** for any DiD and report dynamic (event-time) effects.
- Defend the **exclusion restriction** for any IV in words — relevance alone is not enough.
- Pre-commit the main specification; relegate alternatives to robustness.
- Plan the data provenance trail now (Compustat/CRSP/I/B/E/S/audit-data vintages and screens).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAST is empirical accounting; emphasize identification of disclosure / governance effects and the multiple-testing haircut for mined associations.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The identifying variation (shock/setting/threshold) is named and defended
- [ ] Estimating equation, unit, level, fixed effects, and clustering plan are stated
- [ ] DiD shows pre-trends and dynamic effects; staggered designs use a modern estimator
- [ ] IV exclusion restriction is argued, not asserted; matching is a complement, not the claim
- [ ] Primary construct proxy pre-committed; alternative proxies planned
- [ ] Analytical models fix primitives/timing and the solution concept before solving
- [ ] Experiments have IRB, realistic stimuli, manipulation/attention checks, adequate power

## Anti-patterns

- **Kitchen-sink controls** standing in for identification ("we control for everything").
- **TWFE on staggered adoption** without addressing heterogeneous-treatment-effect bias.
- **IV by convenience:** an instrument correlated with the outcome directly.
- **Matching as causal proof** when selection is on unobservables.
- **Proxy fragility:** a single contested construct measure with no alternative planned.
- **Non-minimal model:** primitives a referee can strip without losing the result.

## Output format

```text
【Lane】archival / analytical / experimental
【Setting & identifying variation】...
【Design】DiD / staggered-DiD / IV / RDD / event study / experiment / model
【Spec】equation; unit/level; fixed effects; clustering plan
【Construct】primary proxy + alternatives planned
【Identification defense】pre-trends / exclusion / discontinuity / randomization ...
【Data provenance】sources + vintages + screens noted
【Next skill】revacc-data-analysis
```
