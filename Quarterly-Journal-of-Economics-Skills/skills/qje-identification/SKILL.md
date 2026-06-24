---
name: qje-identification
description: Use when the causal identification strategy is the bottleneck for a Quarterly Journal of Economics (QJE) manuscript — RCT, staggered DID, IV, RDD, event study. Stress-tests the design to the QJE general-interest bar before tables are drafted.
---

# Causal Identification (qje-identification)

## When to trigger

- The empirical core is OLS + controls with an undefended causal claim
- A DID uses two-way fixed effects (TWFE) on staggered timing without modern estimators
- An IV's first stage is weak or the exclusion restriction is unargued
- An RDD lacks a McCrary density test or bandwidth-robustness
- You are unsure your design clears the QJE causal bar

## The QJE identification bar

QJE rewards **credible identification serving a big question**, not technique for its own sake. Editorial reality shapes the bar: five Harvard-based Editors (Barro, Katz, Nunn, Shleifer, Stantcheva as of 2024) desk-screen in roughly two weeks, so the identifying variation must be legible and convincing on a first read. QJE's own canon mixes clean experiments and quasi-experiments with reduced-form ambition — e.g., Chetty, Hendren, Kline & Saez, "Where is the Land of Opportunity?" (QJE 2014), and Chetty et al. on Project STAR kindergarten effects (QJE 2011). The credibility ranking editors and referees implicitly apply (strong → weaker):

1. **RCT / field experiment** with pre-registration and balance
2. **Sharp/fuzzy RDD** at a clean policy threshold
3. **DID / event study** off a credibly exogenous policy shock (with modern estimators)
4. **IV** with a strong first stage and a defended exclusion restriction
5. **Matching / selection-on-observables** — acceptable only as a complement, rarely as the spine

Note the QJE-specific twist: a *novel, hard-to-assemble dataset answering a first-order question* can carry a paper even when the design is reduced-form, because the journal prizes the question and the lesson (Akerlof's "Market for 'Lemons'", QJE 1970, is the patron saint of idea-first papers). It will not save a narrow within-field estimate.

## Branch paths

### Branch A: DID / event study

- Staggered adoption? You **must** move beyond TWFE. Use Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille; report a Goodman-Bacon decomposition to expose "forbidden" comparisons.
- Pre-trends: show a clean event-study plot with leads; pre-period coefficients near zero.
- Inference: cluster at the level of treatment assignment; consider wild-cluster bootstrap with few clusters.
- Placebo / permutation tests on treatment timing and on outcomes that should not move.

### Branch B: IV

- First-stage F should be strong; with weak instruments use Anderson–Rubin or other weak-IV-robust confidence sets, not just t-stats.
- Exclusion restriction argued in **three registers**: economic theory, institutional detail, and falsification (effect absent where the channel is absent).
- Report the reduced form and the OLS alongside IV; discuss the LATE/compliers interpretation.
- Defend the instrument's own exogeneity — not just relevance.

### Branch C: RDD

- McCrary / Cattaneo–Jansson–Ma density test for manipulation at the cutoff.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus at least three bandwidth-robustness checks; report bias-corrected CIs.
- Covariate smoothness / balance at the threshold; placebo cutoffs.
- For fuzzy RDD, report the first stage in the discontinuity.

### Branch D: RCT / field experiment

- Pre-registration / pre-analysis plan referenced; report deviations.
- Randomization balance table; attrition analysis (Lee bounds if differential).
- Multiple-hypothesis adjustment across outcomes/subgroups.
- External validity discussed: what does the experimental population teach beyond itself?

### Branch E: novel descriptive / measurement paper

- Is the data genuinely new and hard to assemble? (At QJE this is a real path, but only with first-order facts.)
- Are the new facts disciplined against measurement error and alternative explanations?
- Is there a clear conceptual lesson the facts deliver to all of economics, not one subfield?

## Execution bridge (StatsPAI / Stata MCP)

A QJE identification claim should be **estimated and audited**, not just argued. Full
map: [`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md). QJE applied-micro instantiation:

1. `detect_design` → `recommend` → fit with `as_handle=true`, then `audit_result` to
   enumerate the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` (never bare TWFE); show the
   `bacon_decomposition` weight you are correcting; `honest_did_from_result`
   (Rambachan–Roth) because the pre-trend test is low-power (Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity`/`mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` to state how strong a confounder must be.

Report the **economic magnitude** the QJE body expects; route the full diagnostic
battery to the appendix, and keep every number reproducible for `qje-replication-package`.
If StatsPAI/Stata are not connected, adapt the vendored `resources/code/` skeleton and
flag any unverified number. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).

## Checklist

- [ ] Identifying variation named in one sentence and defended as exogenous
- [ ] Design-appropriate diagnostics done (pre-trends / density / first-stage / balance)
- [ ] Modern estimator used where TWFE would be biased (staggered DID)
- [ ] Inference matched to assignment level; few-cluster issues addressed
- [ ] Placebo / permutation / falsification tests reported
- [ ] LATE / external-validity interpretation stated explicitly
- [ ] The claim never exceeds what the design supports

## Anti-patterns

- TWFE on staggered treatment with no discussion of heterogeneity bias
- IV that is "exogenous shock × lagged endogenous variable" with no exclusion argument
- "We argue treatment is as good as random" with no falsification evidence
- RDD reporting one bandwidth and hiding sensitivity
- A clean local design oversold as a global structural parameter with no broad lesson

## Output format

```
【Design】RCT / RDD / DID / IV / descriptive / other
【Identifying variation】one sentence
【Diagnostics done】[pre-trends, density, first-stage F, balance, ...]
【Diagnostics missing】[...]
【Inference】clustering level + few-cluster handling
【Interpretation】LATE / ATT / external validity note
【Next step】qje-theory-model
```
