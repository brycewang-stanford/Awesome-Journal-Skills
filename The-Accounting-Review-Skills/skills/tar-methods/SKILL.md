---
name: tar-methods
description: Use when the research design and identification strategy are the bottleneck for a The Accounting Review (TAR) manuscript — choosing the setting, shock, and design that credibly identify an accounting effect, or structuring an analytical model or experiment. Designs the study; it does not run the estimation and robustness (tar-data-analysis) or frame the contribution (tar-contribution-framing).
---

# Research Design & Identification (tar-methods)

## When to trigger

- Your treatment (a disclosure, a standard adoption, an audit/tax regime) may be endogenous
- Adoption is staggered across firms/years and you need a defensible DiD
- You have an association and a reviewer will ask "is this causal or just correlation?"
- You are designing an experiment to isolate a channel archival data cannot separate
- You are building an analytical model and need to fix primitives and solution concept

## TAR is method-agnostic but identification-obsessed

TAR's stated policy is open to all rigorous methods; the bar is the contribution. In the dominant
**large-sample archival** lane, "rigorous" almost always means a **credible identification
strategy**, because accounting treatments (disclosure choices, conservatism, auditor selection, tax
positions) are rarely randomly assigned. Pick the design that breaks the endogeneity for *your*
accounting setting.

## Identification toolkit for archival accounting

| Identification threat / setting                          | Design                                                        |
|----------------------------------------------------------|--------------------------------------------------------------|
| Regulation / standard adoption with a clean date         | Difference-in-differences; event study around the date       |
| Staggered adoption across firms/states/countries         | Staggered DiD with modern estimators (avoid the TWFE bias)   |
| Endogenous accounting/auditor/tax choice                 | Instrumental variables / 2SLS with a defensible exclusion    |
| A threshold rule (covenant, index inclusion, size cutoff)| Regression discontinuity                                     |
| Selection on observables                                 | Matching (PSM/entropy) as a complement, not the main claim   |
| A plausibly exogenous shock to information environment    | Natural experiment; pre-trends shown                         |

State the **estimating equation**, the **unit and level**, the **fixed effects** (firm, year,
industry-year), and the **identifying variation** explicitly. The design section should make a
skeptic believe the variation is as-good-as-random conditional on controls.

## If the lane is experimental

- Manipulate the focal accounting construct; use realistic stimuli and an appropriate participant
  pool (investors, auditors, managers) — IRB documentation is required and reviewers expect it.
- Pre-register where feasible; include manipulation and attention checks; power the design for the
  interaction, not just the main effect.

## If the lane is analytical

- Fix the information structure, players, and payoffs before solving; state the equilibrium concept.
- Show the model is the *minimal* structure that generates the accounting result.

## Design hygiene

- Show **parallel pre-trends** for any DiD; report dynamic (event-time) effects.
- Defend the **exclusion restriction** for any IV — relevance is not enough.
- Pre-commit the main specification; relegate alternatives to robustness (see `tar-data-analysis`).
- Plan the **data-authenticity** trail now: the processing code for the sample is part of submission.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). TAR is archival accounting — DiD around regulation / standard changes, IV, and earnings-based designs; the corporate-causal chain fits directly.

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
- [ ] Estimating equation, unit, level, and fixed effects are stated
- [ ] DiD designs show pre-trends and dynamic effects; staggered designs use a modern estimator
- [ ] IV exclusion restriction is argued, not asserted; matching is a complement, not the claim
- [ ] Experiments have IRB, realistic stimuli, manipulation/attention checks, and adequate power
- [ ] Analytical models fix primitives and the solution concept before solving

## Anti-patterns

- **Kitchen-sink controls** standing in for identification ("we control for everything").
- **TWFE on staggered adoption** without addressing heterogeneous-treatment-effect bias.
- **IV by convenience**: an instrument that fails exclusion (correlated with the outcome directly).
- **Matching as causal proof** when selection is on unobservables.
- **An experiment with no IRB** or with a participant pool unfit for the construct.

## Output format

```
【Lane】archival / experiment / analytical
【Setting & identifying variation】...
【Design】DiD / staggered-DiD / IV / RDD / event study / experiment / model
【Spec】equation; unit/level; fixed effects; clustering plan
【Identification defense】pre-trends / exclusion / discontinuity / randomization ...
【Data-authenticity plan】processing code + data description ready? yes/no
【Next step】tar-data-analysis
```
