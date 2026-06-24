---
name: finman-identification
description: Use when the causal or economic credibility of a Financial Management (FM) result is the bottleneck — endogenous corporate policy choices, staggered-event designs, weak instruments, or a "correlation dressed as a channel." Stress-tests the identification to FM's applied-finance bar before exhibits are finalized.
---

# Identification Strategy (finman-identification)

## When to trigger

- The headline claim rests on a regression of an outcome on an endogenous corporate-policy choice plus controls
- A difference-in-differences exploits a regulation or shock with **staggered** adoption and uses plain TWFE
- An instrument is invoked but the exclusion restriction and first-stage strength are not defended
- You are asserting a *channel* or *mechanism* where the design only supports a correlation

## The FM identification bar

FM is an applied-finance journal that prizes **practical relevance**, but practical relevance does not buy a pass on identification — the editors list **rigor** alongside relevance among the five criteria. The realistic standard is **credible, well-defended causal or economic identification appropriate to corporate-finance data**, not the absolute frontier bar of JF/JFE/RFS. What FM referees reward: a clearly named source of exogenous variation, a design matched to it, and an honest statement of what is and is not identified — paired with an economically meaningful magnitude. What they punish: endogeneity hand-waved away with firm fixed effects, a "shock" that is anticipated or confounded, and a mechanism claim the design cannot reach.

## Branch paths

### Branch A: Corporate-finance event / regulation designs (DiD, event study)
- With **staggered** adoption, move beyond TWFE — use Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille; report a Goodman-Bacon decomposition to show what TWFE was averaging.
- Show a clean **event study with pre-period leads** flat around zero; FM referees read the pre-trend plot before the table.
- Defend that the shock is **unanticipated and not bundled** with a confounding policy; address anticipation/reversal.
- Cluster inference at the level of treatment assignment (firm, state, industry); flag few-cluster problems.

### Branch B: Endogenous corporate-policy choices (capital structure, payout, governance, M&A)
- Treat the policy as a **choice**, not an exogenous regressor; name the omitted variable / reverse-causality story explicitly and show how the design breaks it.
- Where an IV is used, defend the **exclusion restriction in institutional and economic terms**, report first-stage strength, and use weak-IV-robust inference (Anderson–Rubin) when F is modest.
- Matching / entropy balancing must show covariate balance and acknowledge selection on unobservables (Oster-style sensitivity is persuasive and cheap).

### Branch C: Asset pricing / return predictability
- Identification here is about **separating signal from data-snooping**: control for known factors, address multiple testing, and show the result survives reasonable transaction costs and out-of-sample.
- Distinguish a risk explanation from a mispricing one explicitly rather than leaving the channel ambiguous.

### Branch D: Mechanism / channel claims
- A correlation between treatment and outcome is not a channel. To claim a mechanism, show the **intermediate variable moves** and that shutting it down attenuates the effect (mediation, heterogeneity by mechanism intensity).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Financial Management is empirical corporate finance + asset pricing; corporate-causal chain (DiD/IV/RDD) plus the factor-zoo haircut for cross-sectional pricing.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The source of exogenous (or quasi-exogenous) variation is named in one sentence
- [ ] Staggered designs use a modern estimator; event-study leads shown and flat
- [ ] Endogenous policy choices have the OVB/reverse-causality story named and addressed
- [ ] IVs defend exclusion in economic/institutional terms; weak-IV inference where F is modest
- [ ] Inference clustered at the assignment level; few-cluster issues flagged
- [ ] Channel claims backed by intermediate-variable evidence, not just the reduced form
- [ ] The economic magnitude is stated and plausible — not just statistical significance

## Anti-patterns

- "We include firm and year fixed effects" presented as if it solved endogeneity
- Plain TWFE on staggered treatment with no heterogeneity-robust check or Bacon decomposition
- An instrument whose exclusion restriction is asserted, never argued institutionally
- Calling a reduced-form correlation a "channel" with no intermediate-variable evidence
- Significance-chasing a tiny coefficient while the economic magnitude is trivial — FM cares about the magnitude

## Worked vignette (illustrative)

A paper regresses firm investment on board independence and calls independence a "monitoring channel." A referee notes independent boards are chosen, not assigned. The FM fix: exploit a staggered listing-rule change that forced independence on some firms, re-estimate with Sun–Abraham, show flat pre-trend leads, and demonstrate that the investment response concentrates where the monitoring slack was largest (the mechanism). Then state the magnitude — say a 2.1pp change in investment (s.e. 0.7, illustrative) — so the result is both identified and economically legible to a manager.

## Referee pushback mapped to the identification fix

- *"Firm and year fixed effects don't solve endogeneity here."* → Name the specific OVB/reverse-causality story and bring a design (quasi-shock, IV, or matching) that breaks it; add an Oster bound for unobservables.
- *"Staggered TWFE is biased in this setting."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"Your instrument is not plausibly excluded."* → Defend exclusion institutionally, report first-stage F, and use Anderson–Rubin inference if F is modest.
- *"This is a correlation, not the channel you claim."* → Show the intermediate variable moves and that attenuating it kills the effect.
- *"Significant, but is it economically large?"* → State the magnitude scaled to a managerial unit; FM weights economic size, not stars.

## A note on FM's identification taste vs. the top-3

FM does not demand the absolute frontier identification bar of JF/JFE/RFS, where a single contested assumption can sink a paper. It demands a **credible, honestly-bounded** design with the threats named and the leading one defused — paired with relevance. Over-engineering identification at the cost of a legible economic story is a *mis-read* of the journal; under-defending it and leaning on relevance is the more common, and fatal, error.

## The minimum credible-design package by branch

When time is short, these are the non-negotiable elements a referee will look for first:

- **Event/regulation DiD:** a flat pre-trend event-study plot + a heterogeneity-robust estimator + clustering at assignment level.
- **Endogenous policy:** the named OVB/reverse-causality story + one design element that breaks it (IV, quasi-shock, or matching) + an Oster sensitivity bound.
- **Asset pricing:** factor controls + a multiple-testing acknowledgment + net-of-cost evidence + a risk-vs-mispricing statement.
- **Mechanism:** intermediate-variable evidence + heterogeneity along mechanism intensity.
A paper missing its branch's minimum package will draw a credibility report no matter how relevant the question.

## Output format

```
【Branch】event/regulation DiD / endogenous policy / asset pricing / mechanism
【Exogenous variation】one sentence
【Design + estimator】[modern DiD / IV / matching / factor controls]
【Identification evidence】[pre-trends / first-stage / balance / mediation]
【Inference】clustering level; weak-IV handling if any
【Economic magnitude】stated and plausible? [Y/N]
【What it does NOT identify】[...]
【Next skill】finman-empirical-design
```
