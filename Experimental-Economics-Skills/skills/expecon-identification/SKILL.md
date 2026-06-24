---
name: expecon-identification
description: Use when the credibility of an Experimental Economics (ExpEcon) manuscript rests on experimental control — incentive compatibility, randomization, the no-deception gate, and clean treatment contrasts. Stress-tests design-based identification before exhibits are finalized; it does not draft prose.
---

# Experimental Control & Identification (expecon-identification)

## When to trigger

- A referee questions whether the treatment effect is causal or an artifact of an uncontrolled difference
- Payoffs may not be **incentive compatible** — subjects could earn more by misreporting, or stakes are hypothetical/trivial
- Any procedure risks tripping the **ESA no-deception norm** (false feedback, fake co-players, rigged draws, undisclosed payoff manipulation)
- Randomization, session structure, or the order of treatments could confound the comparison

## Identification at ExpEcon = control + a clean contrast

In observational economics, identification is an argument about why selection does not bias the estimate. In the lab, **you manufacture identification by design**: randomization plus tight control means the *only* systematic difference across conditions is the manipulated dimension. The job here is to verify that claim holds, on four fronts.

### 1. The two gates (binary; check first)

- **No deception (hard gate).** Experimental Economics only considers studies that **do not deceive participants** (检索于 2026-06；以官网为准). This is the single most common cause of an ExpEcon desk reject. Deception includes: false information about other participants or their choices, fabricated feedback, rigged "random" draws, misrepresenting payoffs or the true purpose in a payoff-relevant way, and confederates posing as subjects. **Acceptable** practices that are *not* deception: withholding (not misstating) information, abstract/neutral framing, the strategy method, and not naming the hypothesis. If a design needs deception to work, it cannot be saved by disclosure — redesign it.
- **Salient real incentives.** Choices must be **incentivized with real consequences**. Verify the payment mechanism is **incentive compatible**: BDM/random-lottery for valuations and risk, strategy-method payoffs that match the decision being elicited, one-randomly-paid-round to avoid wealth/hedging effects, and truthful-reporting mechanisms where beliefs are elicited (e.g., a proper scoring rule, ideally binarized/BSR to be robust to risk preferences). State the ECU→money conversion and the realized average payment.

### 2. Randomization & control

- Random assignment **to treatment**, and document the unit (individual, group, session). Report balance on observables and on a comprehension measure.
- Hold everything else fixed: identical instructions except the manipulated clause, same interface, same matching protocol, same subject pool and recruitment (e.g., ORSEE/hroot), same physical/online conditions.
- Beware **session-level confounds**: if a treatment was run in different sessions/cohorts than the control, session is confounded with treatment — randomize within session or run treatments interleaved.

### 3. Comprehension, order, and learning

- **Comprehension checks** before play; report pass rates and pre-specify how failures are handled (exclude vs. retain). A treatment difference driven by differential comprehension is not the mechanism.
- **Order/learning effects:** if within-subject, counterbalance order and test for order effects; if between-subject, justify the loss of power against the gain in clean identification.

### 4. The estimand and inference unit

- State the **estimand** in one sentence: the average treatment effect of [manipulation] on [primary outcome], for [population]. Distinguish it from any structural parameter.
- The independent unit is usually the **session or matching group, not the individual decision** (decisions within a group are not independent). Inference must respect this — see `expecon-robustness`.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Experimental Economics is lab/field experiments; randomization inference, `romano_wolf` for many treatments/outcomes, and power are decisive — observational tools secondary.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] **No deception** confirmed against the ESA definition; if borderline, the borderline practice is named and defended as non-deceptive
- [ ] Payment mechanism is **incentive compatible** for every elicited object; ECU→money rate and realized payments reported
- [ ] Random assignment documented; balance + comprehension reported; treatment not confounded with session/cohort
- [ ] Comprehension-check handling pre-specified; order/learning addressed
- [ ] Estimand stated in one sentence; primary outcome and comparison pre-registered
- [ ] Independent unit of inference identified (session/matching group)

## Anti-patterns

- Any deception, however mild, presented as harmless — this is the classic ExpEcon desk reject
- Hypothetical or token stakes treated as "incentivized"
- A non-incentive-compatible belief elicitation (e.g., flat-payment guesses) read as truthful beliefs
- Treatment run in separate sessions from control, so session and treatment are confounded
- Reporting per-decision n as if decisions were independent observations
- Calling a comprehension-driven gap "the behavioral effect"

## Worked vignette (illustrative)

A trust-game variant gives second movers feedback on first movers' transfers. To boost a treatment, the authors consider *inflating* the displayed transfer. That is **deception** — desk-reject territory. The fix preserves identification without lying: run a strategy-method condition where second movers respond to *every* possible transfer, so the contrast is built from truthful, fully-incentivized responses and no feedback needs to be faked. Power is then justified at the matching-group level (e.g., 18 groups/arm for 80% power on a 1-token gap, illustrative).

## Referee pushback mapped to the fix

- *"Is this deception?"* → Name the procedure, classify it against the ESA definition (withholding/abstract framing/strategy method = OK; false feedback/fake co-players/rigged draws = not OK), and quote the instructions.
- *"The belief elicitation isn't incentivized."* → Switch to a proper/binarized scoring rule and report it; flat-payment beliefs are not data.
- *"Treatment is confounded with session."* → Show treatments were interleaved or randomized within session, or re-run; do not hand-wave.
- *"The effect is just confusion."* → Report comprehension pass rates by treatment and re-run excluding failers; show the gap persists.
- *"What is the estimand?"* → State the ATE in one sentence and the population it speaks to; separate it from any structural parameter.

## Quick incentive-compatibility reference

| Object elicited | Incentive-compatible mechanism |
|-----------------|-------------------------------|
| Valuation / WTP | BDM, or second-price/random-price |
| Risk preference | one-randomly-paid lottery menu (e.g., Holt–Laury), paid for real |
| Beliefs | proper scoring rule, ideally binarized (BSR) to be risk-robust |
| Strategy across states | strategy method, with payoff for the realized contingency |
| Repeated-game earnings | one-randomly-selected-round payment to avoid wealth/hedging |

If an elicited object is *not* on an incentive-compatible footing, the data for that object are suggestive at best — fix it before claiming it identifies anything.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-identification
【Verdict】pass / revise / reroute
【No-deception gate】clear / borderline-defended / FAILS
【Incentive compatibility】mechanism per elicited object + ECU→money + realized pay
【Randomization & control】unit, balance, session-confound check
【Comprehension / order】pass rates + handling; counterbalancing
【Estimand】ATE of [X] on [Y] for [pop]; inference unit = session/group
【Next skill】expecon-robustness
```
