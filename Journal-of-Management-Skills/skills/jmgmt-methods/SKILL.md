---
name: jmgmt-methods
description: Use when research design and measurement are the bottleneck for a Journal of Management (JOM) manuscript — matching design to the theoretical claim, construct validity, common-method bias, endogeneity, multilevel structure, and (for meta-analyses) coding/artifact corrections. Designs the study; it does not run the estimation (jmgmt-data-analysis).
---

# Research Design & Methods (jmgmt-methods)

## When to trigger

- The design may not match the theory's level, timing, or causal claim
- Data are single-source, single-wave, self-reported (common-method bias risk)
- The theory is causal but the design is cross-sectional/correlational
- Constructs lack established, validated measures
- A meta-analysis needs a defensible coding protocol and artifact-correction plan
- A reviewer says "the design cannot test this hypothesis" or "endogeneity is unaddressed"

## Match the design to the claim

JOM welcomes **all empirical methods** — survey, experiment, archival panel, multilevel field study, qualitative, and meta-analysis — and judges on *fit and rigor*, not a preferred method. JOM's **research-methods identity** (it explicitly covers research methods and runs methods-focused reviews) means design choices are scrutinized closely.

| Theoretical claim | Design that earns it |
|-------------------|----------------------|
| Causal effect of a manipulable cause | Experiment (lab/online/field), or natural experiment |
| Process unfolding over time | Multi-wave panel; longitudinal/lagged design |
| Firm/strategy outcome from archival cause | Panel archival with fixed effects + an endogeneity strategy |
| Cross-level mechanism (team→individual) | Multilevel/nested data analyzed with HLM, not OLS |
| Synthesis across a literature | Meta-analysis with a pre-registered coding protocol |

A two-study design (field study for generalizability + experiment for the causal mechanism) is a recognized JOM strength — it buys internal and external validity at once.

## Designing against the threats JOM referees punish

- **Common-method bias (CMB)**: separate the sources of predictor and outcome; separate them temporally across waves; use objective/archival outcomes where possible. **Procedural remedies beat statistical fixes** (the Podsakoff et al. guidance is the field reference). Plan this *before* collecting data; a Harman single-factor test alone will not satisfy a JOM reviewer.
- **Endogeneity (archival/macro)**: anticipate omitted variables, reverse causality, and selection. Specify an identification strategy — instrument, natural experiment, panel fixed effects, difference-in-differences, Heckman/2SLS, propensity matching — and state the assumptions each requires.
- **Measurement / construct validity**: use validated multi-item scales; pilot new measures; plan a confirmatory factor analysis (CFA) with fit indices and a discriminant-validity test (AVE vs. shared variance, or the HTMT ratio). State the level at which each construct is measured.
- **Multilevel discipline**: if data are nested, justify aggregation with ICC(1), ICC(2), and r_wg; model the nesting (random effects/HLM). Theorizing at the team level but running OLS on disaggregated individuals is a standard rejection trigger.
- **Sampling & power**: justify the frame, response rate, and statistical power — *especially for interactions*, which JOM reviewers know are underpowered when authors present null moderation as a "boundary condition."

## Meta-analysis design

- Pre-specify inclusion/exclusion criteria and a transparent search; report a PRISMA-style flow.
- Double-code a subset; report inter-coder agreement.
- Choose the artifact-correction model (Hunter–Schmidt psychometric meta-analysis vs. Hedges–Olkin random-effects) and justify it; correct for sampling error and, where defensible, measurement unreliability and range restriction.
- Plan moderator/meta-regression analyses that map to *competing theories*, plus publication-bias diagnostics.

## Referee pushback mapped to the design fix

- *"This is single-source, single-wave — common-method bias is unaddressed."* → Add temporal/source separation or an objective outcome; a Harman test alone will not close it.
- *"Your archival regressor is endogenous."* → Specify and defend an identification strategy (IV/NE/FE/DiD/matching) and report first-stage strength.
- *"The new scale's discriminant validity is unestablished."* → Report a CFA with AVE vs. shared variance or an HTMT ratio, plus an alternative-model comparison.
- *"You theorize at the team level but test individuals."* → Justify aggregation (ICC, r_wg) and model the nesting, or re-pitch the theory at the individual level.
- *"The interaction is underpowered."* → Report power for the interaction specifically; if it is a true null, theorize the boundary rather than presenting an underpowered null as a finding.

## Designing a multi-study program

JOM rewards study programs that *triangulate* rather than merely accumulate. A canonical pairing is a field study (external validity, real outcomes) plus an experiment (causal mechanism, manipulation of the antecedent). Decide what each study is *for* — generalizability, causal identification, or mechanism evidence — and make sure together they license the central claim. A second study that merely re-runs the first in a new sample adds length without adding inferential leverage, and the 50-page limit punishes it.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Management covers empirical management broadly (including meta-analysis); the chain below serves primary causal / panel work.

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

- [ ] Design can actually test each hypothesis (causal claims have causal leverage)
- [ ] CMB addressed by procedural design (separate sources/time), not just a post-hoc test
- [ ] Endogeneity strategy specified for archival/observational causal claims
- [ ] Validated measures; new scales piloted; CFA + discriminant validity planned
- [ ] Levels aligned across theory/measurement/analysis; aggregation (ICC, r_wg) justified
- [ ] Sampling frame, response rate, and power (incl. interactions) justified
- [ ] (Meta) coding protocol, inter-coder agreement, artifact-correction model, bias diagnostics

## Anti-patterns

- **Cross-sectional causal claims**: "X causes Y" from one-wave correlational data
- **CMB as afterthought**: a Harman single-factor test instead of designed separation
- **Ignored endogeneity**: an archival "effect" with an obviously endogenous regressor and no strategy
- **Mismatched levels**: theorizing at the team level, testing individuals via OLS
- **Home-grown scales** with no reliability or discriminant-validity evidence
- **Underpowered interactions** presented as null "boundary conditions"
- **Vote-counting meta-analysis** with no artifact corrections or bias checks

## Output format

```
【Design】experiment / panel-archival / multilevel survey / qualitative / meta-analysis
【Hypothesis-design fit】each H testable? notes ...
【CMB plan】procedural remedies ...
【Endogeneity strategy】instrument / NE / FE / DiD / matching ...
【Measures】validated? new (piloted)? CFA + discriminant?
【Levels】theory / measurement / analysis aligned? aggregation (ICC, r_wg) ...
【Power & sampling】frame, N, power for interactions ...
【Meta only】coding / agreement / artifact model / bias checks ...
【Next step】jmgmt-data-analysis
```
