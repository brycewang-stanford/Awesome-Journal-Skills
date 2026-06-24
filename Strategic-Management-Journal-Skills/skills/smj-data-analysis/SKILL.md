---
name: smj-data-analysis
description: Use when estimating models and defeating endogeneity for a Strategic Management Journal (SMJ) manuscript — the single highest bar at SMJ. Executes and stress-tests the identification design from smj-methods; it does not design the study or build exhibits.
---

# Data Analysis & Endogeneity (smj-data-analysis)

## When to trigger

- You have a performance regression with no endogeneity / reverse-causality treatment
- DID, IV, matching, or a selection model is chosen but not yet stress-tested
- Reviewers will ask "how do you know this is causal and not selection?"
- You need to plan the mechanism test and the robustness battery

## The SMJ endogeneity mandate

Performance regressions with **unaddressed endogeneity or reverse causality are the #1 SMJ rejection reason.** Treat causal identification as a first-class part of the paper, not a footnote. The reviewer's mental model: *firms that make this strategic choice are different in ways that also affect performance.* You must close that door explicitly.

SMJ codifies this in Bettis, Gambardella, Helfat & Mitchell (2014), "Quantitative empirical analysis in strategic management," *SMJ* 35(7): 949–953: acknowledge endogeneity, make a good-faith effort to address it, and avoid **data snooping / p-hacking**. Report **economic magnitudes**, not just stars. SMJ will publish well-designed studies that report **null results** — so do not suppress a theory-relevant null.

## Threat → tool map

| Threat                                   | Primary tools                                              |
|------------------------------------------|------------------------------------------------------------|
| Self-selection into the strategic choice | IV, Heckman selection, PSM/CEM + DID, Rosenbaum bounds     |
| Reverse causality / simultaneity         | Exogenous shock + DID, lagged + Granger-style tests, IV    |
| Unobserved time-invariant heterogeneity  | Firm fixed effects (caveat: cannot fix time-varying confounds) |
| Omitted environmental confound           | Industry-year FE, region FE, controls, falsification tests |
| Measurement error in X                   | IV, multiple indicators, sensitivity analysis              |

Pick from the threat named in `smj-methods`; usually you will combine FE with one identification tool.

## Design-specific execution

### DID / natural experiment
- Test and **show** parallel pre-trends (event-study plot, not just a claim).
- If treatment timing is staggered, address heterogeneous-treatment-effect bias (Goodman-Bacon decomposition; Callaway–Sant'Anna or Sun–Abraham estimators) rather than naive two-way FE.
- Run placebo tests (fake treatment dates; unaffected units) and report effect dynamics.

### Instrumental variables
- Report the first-stage F (weak-instrument concern below conventional thresholds → use weak-IV-robust inference).
- Make the **exclusion** argument in prose: why the instrument affects performance *only* through the strategic choice. Reviewers reject IVs whose exclusion is implausible.
- Report the reduced form and over-identification tests where applicable.

### Matching (PSM / CEM) + DID
- Report covariate balance before/after; show common support.
- Matching handles selection on *observables only*; combine with DID and acknowledge residual selection on unobservables (bounds).

### Heckman selection
- Justify the exclusion restriction in the selection equation (a variable affecting selection but not the outcome). A Heckman with no valid exclusion restriction is identified only off functional form — reviewers know this.

## Mechanism & robustness

- **Mechanism test:** if you theorized a mediator, test it (prefer evidence beyond a Baron–Kenny mediation regression — e.g., moderation-of-process, subsample variation in the mechanism).
- **Magnitude, not just stars:** interpret the key effect in economic terms (e.g., "a 1 SD increase in X → a Y% change in performance"); SMJ cares about meaningful effects.
- **Robustness battery (report, do not bury):** alternative DVs; alternative samples (drop dominant industries/years); alternative estimators; clustering choices; prior performance; survivorship. Where feasible, show sensitivity to the identifying assumption (partial-identification / bounding).
- **Inference:** cluster standard errors at the level of treatment assignment (often firm); justify the choice.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SMJ is strategy — firm-level panels where strategic choices are endogenous; foreground IV / DiD identification and the endogeneity-of-strategy objection.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The identifying threat is stated and the matching tool is deployed
- [ ] Reverse causality is addressed by design, not by lags alone
- [ ] Firm (and industry-year) fixed effects included where appropriate
- [ ] DID: parallel-trends evidence shown; staggered-timing bias addressed; placebos run
- [ ] IV: first-stage strength reported; exclusion argued in prose; reduced form shown
- [ ] Matching: balance + common support reported; unobservable selection acknowledged
- [ ] Heckman: valid exclusion restriction, not functional-form identification
- [ ] Mechanism tested, not just asserted
- [ ] Robustness across DV, sample, estimator, and clustering reported
- [ ] Standard errors clustered at the assignment level

## Anti-patterns

- Cross-sectional correlations interpreted causally — an instant credibility loss at SMJ
- "We include fixed effects" treated as a complete endogeneity defense (FE miss time-varying confounds)
- IV with an exclusion restriction no reviewer would believe
- Heckman or PSM run mechanically with no defensible exclusion / balance
- Ignoring that firms self-select into the very strategic choice being studied
- Staggered DID with naive two-way FE and no heterogeneity correction
- A wall of robustness tables that never confronts the central threat
- Specification hunting until p < 0.05 (data snooping); reporting stars with no economic magnitude; suppressing a theory-relevant null — all discouraged by SMJ

## Output format

```
【Identifying threat】selection | reverse causality | unobserved heterogeneity | omitted confound
【Estimator】FE + [IV | DID | matching | Heckman | ...]
【Identification evidence】[parallel trends / first-stage F / balance / exclusion argument]
【Placebo / falsification】[done?]
【Mechanism test】[what + result]
【Robustness】[DV alt, sample alt, estimator alt, clustering]
【Residual threat acknowledged】...
【Economic magnitude reported】yes / add
【Nulls reported honestly (no p-hacking)】yes
【Next step】smj-contribution-framing
```

## Templates & resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Stata/R/Python packages (reghdfe, ivreghdfe, csdid/did, psmatch2, rdrobust) and strategy data sources
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ p-hacking / null-results / endogeneity policy and the Bettis et al. (2014) editorial
