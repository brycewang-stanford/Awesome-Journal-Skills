---
name: jebo-identification
description: Use when the design that isolates a behavioral mechanism is the bottleneck for a Journal of Economic Behavior & Organization (JEBO) manuscript — lab/field experiment, observational causal design, or simulation. Stress-tests experimental and observational identification to JEBO's behavioral-credibility bar; it does not write prose or build the deposit.
---

# Identification Strategy (jebo-identification)

## When to trigger

- A lab/field experiment's treatment, incentives, or comprehension are not pinned down
- An effect could be an **experimenter-demand effect** rather than the claimed behavioral mechanism
- An observational behavioral claim rests on OLS + controls, or TWFE on staggered timing
- A study uses deception, or runs many treatments, and the inference/ethics implications are unaddressed
- You are unsure the design isolates the *behavioral* mechanism, not a confound

## The JEBO identification bar

JEBO judges identification through a **behavioral-mechanism** lens: the design must isolate the *psychological or institutional channel* the paper claims, not merely produce a significant difference. Because JEBO treats **experimental design as a first-class identification branch** alongside observational causal designs, "identification" means different things by branch — pick the branch and make the channel transparent. Inference must match the design (clustering at the level of randomization or assignment; few-cluster corrections).

### Branch A: Lab / online experiment (the JEBO core)

- **Incentive compatibility:** payoffs must make truthful/effortful behavior the dominant strategy for the elicited object (e.g., BDM, strategy method, incentivized beliefs). State the mechanism and the stakes.
- **No-deception norm:** the experimental-economics convention is **no deception**; if you deviate, justify it and expect scrutiny — many referees treat deception as disqualifying for an incentivized study.
- **Comprehension & attention checks:** report comprehension quizzes, control questions, and how failures were handled (drop / re-instruct), so the effect is not confusion.
- **Experimenter demand:** rule out demand effects — neutral framing, between-subject where within-subject would cue the hypothesis, obfuscated objectives, or an explicit demand-treatment (e.g., Mummolo–Peterson / de Quidt-style bounds).
- **Randomization & balance:** show balance on observables; report the randomization procedure and unit.
- **Multiple treatments:** if several treatment arms, plan the comparisons and correct for multiplicity (see jebo-robustness).
- **Pre-registration:** pre-register the design and primary analysis (AEA RCT Registry / AsPredicted / OSF) and report deviations. (JEBO does not currently mandate it — 待核实 — but referees increasingly expect it.)

### Branch B: Field experiment

- ITT vs. LATE/TOT stated; randomization unit and stratification described; spillovers and SUTVA addressed.
- Attrition examined and bounded (Lee bounds if differential); compliance documented.
- Ethical clearance / consent noted; external-validity scope stated (the field setting's generality).

### Branch C: Observational behavioral empirics

- **DID / event study** with staggered adoption: move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show clean event-study leads; Goodman-Bacon decomposition.
- **IV:** strong first stage (effective F); weak-IV-robust sets (Anderson–Rubin) when needed; defend exclusion in institutions/theory + falsification.
- **RDD:** density/manipulation test (McCrary / Cattaneo–Jansson–Ma); local-linear, data-driven bandwidth, bias-corrected robust CIs.
- The behavioral interpretation must be argued, not assumed — the design identifies an estimate; the *mechanism* connecting it to a behavioral channel needs its own evidence (see jebo-theory-model).

### Branch D: Agent-based / simulation

- Document the data-generating process and behavioral rules; set and report seeds; show the result is not an artifact of grid/tuning choices (see jebo-robustness).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEBO spans behavioral/experimental and applied micro; randomization inference for experiments, DiD/IV for observational claims.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Branch chosen; the design-to-mechanism mapping stated in one sentence
- [ ] Experiment: incentive-compatible elicitation; no deception (or justified); comprehension checks reported
- [ ] Experimenter-demand effects ruled out or bounded
- [ ] Randomization unit, balance, and (for field) attrition/spillovers handled
- [ ] Observational: design-appropriate diagnostics; modern estimator where TWFE/2SLS would bias
- [ ] Inference clustered at the randomization/assignment level; few-cluster issue addressed
- [ ] The behavioral claim never exceeds what the design isolates

## Anti-patterns

- Reporting a treatment difference as a behavioral mechanism without ruling out demand effects
- Using deception in an incentivized study without justification (referees may reject outright)
- Within-subject designs that cue the hypothesis, presented as if between-subject-clean
- TWFE on staggered treatment with no heterogeneity-bias discussion
- Calling a significant coefficient "evidence of [bias]" when a non-behavioral confound survives
- Significance asterisks standing in for clustered SEs or a pre-registered primary outcome

## Worked vignette (illustrative)

A lab study claims that public visibility raises cooperation via image concerns. A referee asks whether subjects merely inferred the experimenter wanted more cooperation in the visible arm. The JEBO fix: add a demand-effect treatment (explicitly tell one cell "we expect more cooperation"), show the visibility effect (illustrative: +0.6 contributions, s.e. 0.2) is an order of magnitude larger than the pure demand response, and pre-register cooperation as the primary outcome — turning "could be demand" into a bounded, mechanism-level claim.

## Output format

```text
【Branch】lab / field / observational / simulation
【Design-to-mechanism mapping】one sentence
【Behavioral channel isolated】<image concern / loss aversion / learning / norm / ...>
【Identification evidence】[incentives+comprehension+demand-bound / balance+attrition / pre-trends+density+first-stage / DGP+seeds]
【Estimator + inference】estimator; clustering level; weak-IV/honest-DID if any
【What it does NOT identify】[...]
【Next step】jebo-theory-model
```
