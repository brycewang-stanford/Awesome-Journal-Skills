---
name: joap-study-design
description: Use when designing studies and measurement for a Journal of Applied Psychology (JAP) manuscript so they meet the journal's high bar on construct validity, causal inference, common-method variance, nested/multilevel data, and sample-size justification. Strengthens the design and measurement plan; it does not write code.
---

# Study Design & Measurement (joap-study-design)

JAP holds measurement and design to an exacting standard. The recurring killers are **common-method
variance (CMV)**, **weak causal warrants** (cross-sectional single-source data), **unmodeled nesting**,
and **construct validity** gaps. This skill hardens the design *before* data collection, where most of
these problems can actually be solved.

## When to trigger

- Planning a study, a multi-study package, or a measurement strategy
- Writing a preregistration / pre-analysis plan
- A reviewer questioned CMV, causal inference, measurement, nesting, or power
- Justifying sample size at the relevant level of analysis

## Design standards

1. **Construct validity first.** Use validated measures; report reliability and, where the construct is
   new or contested, provide validity evidence (CFA, convergent/discriminant, measurement invariance
   across groups/time). A weak measure dooms an otherwise good design.
2. **Earn the causal claim.** Cross-sectional single-source correlation rarely suffices. Strengthen
   with **temporal separation** (multi-wave), **multiple sources** (self + supervisor + objective),
   **experimental or quasi-experimental** legs, or a **field experiment**.
3. **Design against CMV.** Build in procedural remedies (temporal/source/measurement separation,
   protected anonymity) *and* plan statistical checks; declare the strategy up front. Post hoc
   Harman's single-factor test alone is treated as insufficient at JAP.
4. **Model the nesting.** If employees are nested in teams/units/firms, justify N at each level, report
   ICC(1)/ICC(2) and r_wg for aggregated constructs, and use multilevel models — do not ignore
   dependence or aggregate away the structure without justification.
5. **Justify sample size at the right level.** Power for the *effect that carries the claim* (e.g., the
   cross-level interaction or indirect effect), not just the total N; for multilevel designs, the L2
   sample size usually constrains power.

## Common-method variance — the JAP design playbook

| Remedy | Type | Note |
|--------|------|------|
| Temporal separation (multi-wave) | procedural | predictor and outcome at different waves |
| Source separation (self + other/objective) | procedural | the strongest single defense |
| Measurement/context separation | procedural | different scales/formats for predictor vs outcome |
| Protected anonymity, balanced items | procedural | reduces consistency and acquiescence bias |
| Marker variable / CFA marker technique | statistical | plan a theoretically unrelated marker in advance |
| ULMC (unmeasured latent method construct) | statistical | report alongside, not instead of, procedural remedies |

## Sample-size justification — worked example (illustrative)

For the servant-leadership package, justify N at the level the hypotheses live, before collecting.

```
Multilevel field study (2-2-2 / 2-1-2 mediation):
  Constraint: 74 teams (L2) drives power for the team-level indirect effect.
  Power target: 80% for the indirect effect (Monte Carlo power for multilevel
                mediation), assuming a path ≈ .25, b path ≈ .30, ICC(1) ≈ .15.
  Result: target ≥ 70 teams, ~8 members each → ~560–620; we collect 612 in 74.
Lab experiment (causal leg):
  Between-subjects, two conditions; power for the interaction (H3 boundary),
  N ≈ 240 at 80%, alpha .05; fixed-N, no optional stopping.
Aggregation: report ICC(1), ICC(2), r_wg(j) to justify team-level aggregation
            of psychological safety; preregister exclusion rules.
```

## Pre-data lockdown checklist

| Degree of freedom | Lock before data? | Where it lives |
|-------------------|-------------------|----------------|
| Hypotheses + direction + level | yes | preregistration |
| Measures (all scales, all items) | yes | preregistration (prevents scale cherry-picking) |
| CMV remedies (procedural + planned statistical) | yes | design + preregistration |
| Aggregation rules (ICC/r_wg thresholds) | yes | analysis plan |
| Exclusion rules (careless responding, attrition) | yes | preregistration |
| Covariates / model form | yes | analysis plan |
| Exploratory analyses | allowed, labeled | reported separately, post hoc |

## Design-stage reviewer pushback and the venue fix

- "Cross-sectional, same-source — common method bias" → add temporal/source separation or an
  experimental leg; declare procedural remedies, not just a Harman's test.
- "You ignored nesting" → model multilevel structure; report ICC(1)/ICC(2)/r_wg; justify aggregation.
- "Measure validity unclear" → report reliability, CFA fit, and invariance; cite scale provenance.
- "Underpowered for the cross-level effect" → repower at the constraining level; report the Monte Carlo
  power analysis (handoff to `joap-data-analysis`).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAP is organizational psychology — multilevel survey/field data and experiments; cluster at the right level and apply mediation/moderation discipline.

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

- Cross-sectional single-source self-report as the sole evidentiary base
- CMV addressed only by a post hoc Harman's single-factor test
- Nested data analyzed as if independent, or aggregated without ICC/r_wg justification
- New or modified measures with no validity evidence
- Sample size justified by total N while the carrying effect lives at L2

## Output format

```
【Construct validity】reliability + CFA/invariance evidence? [Y/N]
【Causal warrant】temporal / multi-source / experimental leg present? [Y/N]
【CMV】procedural remedies + planned statistical check declared? [Y/N]
【Nesting】levels, ICC/r_wg, multilevel model justified? [Y/N/NA]
【Sample size】powered for the carrying effect at the right level? [Y/N]
【Next】joap-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Mplus/`lavaan`/`lme4`, Monte Carlo power, CMV-marker and invariance tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — measurement, design, and reporting expectations
