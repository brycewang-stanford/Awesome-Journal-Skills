---
name: psci-study-design
description: Use when designing studies for a Psychological Science manuscript so they meet the journal's standards for power, sample-size justification, preregistration, and confound control. Strengthens the design and pre-analysis plan; it does not write code.
---

# Study Design (psci-study-design)

Psychological Science expects studies that are **adequately powered**, **transparently planned**, and
**robust to researcher degrees of freedom**. Authors must **justify sample size** (a formal power
analysis where appropriate). This skill hardens the design before data collection.

## When to trigger

- Planning a study or a multi-study package
- Writing a preregistration / pre-analysis plan or a Registered Report Stage 1
- A reviewer questioned power, design, confounds, or analytic flexibility
- Justifying sample size and stopping rules

## Design standards

1. **Sample-size justification.** Provide an explicit basis for N — a **power analysis** for the
   smallest effect of interest, a precision/AIPE rationale, or (for sequential/Bayesian designs) the
   decision rule. State the assumed effect size and where it came from.
2. **Preregister the confirmatory core.** Specify hypotheses, design, conditions, measures, exclusion
   rules, and the analysis plan in advance (OSF/AsPredicted, or a Registered Report Stage 1). This is
   what converts a claim from exploratory to confirmatory.
3. **Control researcher degrees of freedom.** Decide in advance: conditions, the full set of measures,
   exclusion criteria, covariates, and how stopping is determined. Undisclosed flexibility inflates
   false positives.
4. **Confounds and validity.** Address random assignment, manipulation/attention checks, order
   effects, demand characteristics; argue construct and external validity for the population claimed.
5. **Multi-study logic.** If using several studies, say what each adds (generalization, mechanism,
   boundary condition) — not just repetition.

## Registered Reports (strongest design path)

- Stage 1 reviews the **theory + design + analysis plan before data**; in-principle acceptance commits
  the journal regardless of outcome if you execute the plan. Ideal for confirmatory and replication
  work, and it neutralizes publication bias. For prior-collected data, use **RR with Existing Data**
  and declare provenance.

## Sample-size justification — worked example (illustrative)

For the two-study attention package, justify N *before* collecting, tied to the smallest effect of
interest (SESOI), not a round number per cell.

```
Smallest effect of interest: d = 0.30 (below this, the premise is not
            practically load-bearing for downstream clinical models).
Study 1 (between-subjects, two groups):
            target 80% power, two-sided alpha .05 → N ≈ 278; we collect 240
            and report honestly that we have ~80% power for d = 0.36, i.e.
            the design is calibrated to a slightly larger effect — stated, not hidden.
Study 2 (direct replication + moderation):
            increase to N = 300 for the interaction term; precision goal is a
            half-width ≤ 0.25 on the replication d.
Stopping rule: fixed-N; no optional stopping. (For sequential designs, state
            the decision boundary and alpha-spending in advance.)
```

State the assumed effect size *and its source* (prior meta-analytic estimate, a pilot, or a SESOI
argument). A power analysis anchored to an inflated published effect is a known failure mode here.

## Pre-data lockdown checklist

| Degree of freedom | Lock before data? | Where it lives |
|-------------------|-------------------|----------------|
| Hypotheses + direction | yes | preregistration / RR Stage 1 |
| Exact conditions and Ns | yes | preregistration |
| Full measure list (all DVs) | yes | preregistration (prevents cherry-picking) |
| Exclusion rules (attention, RT, dropout) | yes | preregistration, with expected attrition |
| Covariates / model form | yes | analysis plan |
| Stopping rule | yes | analysis plan |
| Exploratory analyses | allowed, but labeled | reported separately, post hoc |

## Design-stage reviewer pushback and the venue fix

- "50 per cell, no justification" → replace with a SESOI-anchored power or precision argument.
- "Manipulation may not have worked" → preregister and report a manipulation/attention check; if it
  fails, the confound objection lands hard at this venue.
- "Looks like flexible exclusions" → preregister exclusion rules and report the estimate with and
  without them (handoff to `psci-data-analysis`).
- "Three near-identical studies" → make each study add inference (generalization, mechanism, boundary).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Psychological Science is short-format experimental psychology with strong open-science norms; preregister, run randomization inference, and report effect sizes with family-wise corrections.

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

- "We collected 50 per cell" with no power/precision justification
- Optional stopping or undisclosed exclusion rules
- Flexible measure/condition selection revealed only after results
- Underpowered single studies chasing a surprising effect
- A multi-study paper where studies are near-duplicates with no added inference

## Output format

```
【Sample size】N + justification (power for smallest effect of interest / precision / decision rule)
【Preregistration】confirmatory core preregistered? where?
【Degrees of freedom】conditions, measures, exclusions, covariates fixed in advance? [Y/N]
【Validity】confounds / checks / population addressed
【Design path】Research Article vs Registered Report (S1)
【Next】psci-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — G*Power, `simr`, `Superpower`, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — sample-size-justification and preregistration policy
