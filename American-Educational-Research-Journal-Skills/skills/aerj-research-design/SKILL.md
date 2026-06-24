---
name: aerj-research-design
description: Use when defending the research design of an American Educational Research Journal (AERJ) manuscript — quantitative (multilevel, IRT, quasi-experimental, RCT), qualitative (case study, ethnography, interview), or mixed methods. AERJ judges each tradition on its own terms against the AERA reporting standards. Strengthens the design; it does not write code.
---

# Research Design (aerj-research-design)

AERJ accepts many methodologies but is demanding about each. The design must credibly connect the
framework (`aerj-theory-and-framework`) to evidence and meet the relevant **AERA reporting standards**.
This skill is mode-aware: name the dominant education-research lens and defend it against the strongest
alternative explanation.

## When to trigger

- Specifying sampling, measurement, identification, case selection, or an integration plan
- A reviewer questioned causal claims, generalizability, trustworthiness, or measurement validity
- Preparing a **pre-analysis plan** / preregistration for a prospective design
- Justifying how the design addresses the rival account from `aerj-literature-positioning`

## Quantitative (the field's common designs)
- **Nesting is the default.** Students in classrooms in schools — use **multilevel/HLM** models;
  specify levels, random effects, and cluster-correct inference. Report the design effect / ICC.
- **Measurement.** Tie constructs to validated instruments; report reliability and, where relevant,
  **IRT/factor** evidence. Validity is a design issue, not an afterthought.
- **Causal claims** need a credible design: RCT (with power/MDE, attrition, fidelity), or
  quasi-experimental (DID/event study with modern estimators, RD, IV, matching) — defend identifying
  assumptions, don't assert them. Map to **What Works Clearinghouse**-style expectations when claiming effects.
- **Large-scale assessment data** require plausible values and replicate/survey weights.

## Qualitative (judged on its own terms)
- **Case/site/participant selection** justified by design logic (typical, extreme, theoretical
  sampling), not convenience. Say what the case is a case *of*.
- **Trustworthiness**: prolonged engagement, triangulation, member checks, negative-case analysis,
  audit trail, researcher positionality/reflexivity.
- **Data and analysis**: how data were generated, how coding/interpretation proceeded, how themes
  were warranted by evidence (hand off to `aerj-data-analysis`).

## Mixed methods
- State the **design type** (convergent, explanatory-sequential, exploratory-sequential, embedded) and
  the **rationale** for mixing — what integration buys you that one strand cannot.
- Plan the **point and method of integration** (e.g., joint displays); avoid two papers stapled together.

## The adjudication test (AERJ-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather than
my account, the evidence would look like ___; instead it looks like ___."* If you cannot, the design
does not yet identify the contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AERJ is empirical education research — field experiments and observational school data; multilevel inference and many-outcome corrections are central.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Ignoring nesting (OLS on clustered data); clustering at the wrong level
- "Causal"/"effect" language on a descriptive or associational design
- Convenience sampling dressed up as theoretical sampling
- Mixed methods that never actually integrate
- Treating measurement validity or trustworthiness as boilerplate

## Design-credibility matrix (what each tradition must defend)

AERJ judges each methodology on its own terms, so the credibility bar differs by mode. Use this matrix
to locate the assumption a referee will press hardest.

| Mode | Core thing the design must establish | The assumption referees attack |
|------|--------------------------------------|--------------------------------|
| RCT | Power/MDE, balance, fidelity, low differential attrition | Attrition or non-compliance undoing randomization |
| Quasi-experimental | A credible counterfactual | Parallel trends / continuity at the cutoff / exclusion |
| Multilevel descriptive | Correct nesting and measurement | Cluster level mis-specified; validity unaddressed |
| Qualitative | Trustworthiness and case logic | Convenience sampling dressed as theoretical |
| Mixed | A real point and method of integration | Two strands never actually joined |

## Worked design vignette (illustrative)

An AERJ team evaluates a **peer-tutoring program** with a regression-discontinuity design on an
eligibility test score. The credibility case states the estimand (effect at the cutoff), shows a
density test with no manipulation, reports a bandwidth-robust estimate of an illustrative **0.21 SD**
on the outcome, and writes the adjudication sentence: *if selection rather than the program drove the
jump, covariates would also jump at the cutoff; instead they are smooth.* That single sentence rules
out the strongest rival. A weak version would assert "the program caused gains" with no continuity
evidence — exactly the move a methodological referee rejects.

## Referee pushback and the venue fix

- *"Causal language on an associational design."* → Either build the identification or downgrade the
  claim to description with a mechanism hypothesis.
- *"Your sampling is convenience, not theoretical."* → Justify case/site selection by design logic and
  say what the case is a case *of*.
- *"The mixed design is two papers stapled together."* → Specify the integration point and method;
  confirm method-specific expectations against the journal's current submission guidelines.

## Output format

```
【Mode】quant / qualitative / mixed
【Estimand or claim】what is being identified/shown/understood
【Key assumption(s) / trustworthiness】and how each is defended
【Rival ruled out】the adjudication sentence
【Standards】which AERA reporting standard the design meets
【Next】aerj-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — multilevel/IRT/causal packages and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AERA reporting standards + preregistration notes
