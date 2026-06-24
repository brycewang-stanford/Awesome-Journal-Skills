---
name: isr-data-analysis
description: Use when executing and reporting the analysis for an Information Systems Research (ISR) manuscript — identification and validity for empirical work, proof discipline and comparative statics for analytical work, and rigorous evaluation for design-science work, with overflow routed to the electronic companion. Runs and reports the analysis; it does not design the study (isr-methods) or frame the contribution (isr-contribution-framing).
---

# Analysis, Identification & Proof (isr-data-analysis)

## When to trigger

- Data are collected, or the model is built, and it is time to estimate, derive, or evaluate
- You are unsure whether your estimator matches the design, or whether a proof is complete
- Reviewers will probe identification, measurement validity, or assumption sensitivity
- A reviewer says "the analysis does not support the inference"

## Empirical genre — identification and validity first

ISR empirical reviewers expect causal claims to rest on a credible **identification strategy**, not on a fitted regression:

| Design / claim                               | Estimator / strategy                                          |
|-----------------------------------------------|---------------------------------------------------------------|
| Manipulated IT design/policy                  | Experiment: randomization checks, manipulation/attention checks |
| Quasi-experiment, staggered adoption          | DiD (modern estimators), event study, parallel-trends evidence |
| Endogenous IT investment/adoption (archival)  | IV/2SLS, RDD, matching, panel FE with cluster-robust SE        |
| Latent behavioral constructs                  | SEM/CFA (fit: CFI/TLI/RMSEA/SRMR), AVE, discriminant validity; PLS-SEM where appropriate |
| Nested data (users in teams/firms/platforms)  | Multilevel / HLM; cluster SEs to the sampling/nesting          |
| Counts, choices, durations (clicks, churn)    | Poisson/NB, logit/probit, hazard models as the DV demands      |

Address **common-method bias** by design first (separate sources/waves), then statistically (marker variable or unmeasured latent method factor — a Harman single-factor test alone is weak). Report effect sizes and practical magnitude, not only p-values.

## Analytical genre — proof discipline

For modeling papers, "analysis" means **correct, complete derivations**: state the equilibrium concept, prove existence/uniqueness where claimed, and present the **comparative statics** as the substantive results with their IS interpretation. Run robustness as **extensions** that relax key assumptions (alternative information structures, costs, timing) and show which results survive. Full proofs and lemmas belong in the **electronic companion**, with the main text carrying the intuition and the load-bearing steps.

## Design-science genre — rigorous evaluation

Demonstrate the artifact's **utility**: benchmarks against credible baselines, controlled user studies, or field deployment, with metrics tied to the stated design objectives. A demo is not an evaluation.

## Claim-to-evidence ledger

Before writing results, create a ledger that binds every contribution claim to an analysis:

| Claim type | Minimum evidence | Reviewer stress test |
| --- | --- | --- |
| Causal empirical claim | Design logic, identifying assumptions, pre-trends/placebos or randomization checks, effect magnitude | What unobserved selection or timing story would overturn the claim? |
| Construct/measurement claim | Item provenance, reliability, CFA/discriminant validity, CMB defense | Would a different construct name or common-method explanation fit the data as well? |
| Analytical claim | Proposition, proof sketch in main text, full derivation in companion, comparative statics | Which assumption drives the result, and does an extension relax it? |
| Design-science claim | Baseline comparison, objective-linked metrics, user/field evidence where relevant | Is the artifact useful beyond the demonstration case? |

If a claim lacks a row, downgrade the language before submission. ISR reviewers are receptive to careful boundaries; they are much less receptive to causal, theoretical, or design-utility claims that outrun the evidence.

## Reproducibility and the electronic companion

ISR's source-backed compliance rule is data provenance certification: authors certify rights to use data
and publish results, and any legal or corporate permissions must be obtained before submission. Regardless,
keep clean scripts/solver inputs that regenerate every exhibit, and use the electronic companion for
proofs, full measurement items, and supplementary analyses given the 32-page text / 38-page total caps.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ISR is empirical IS with strong econometric and experimental work; identification (DiD / IV) for observational claims, randomization inference for experiments.

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

- [ ] Empirical: identification strategy executed; assumptions/threats discussed
- [ ] Measurement validity (reliability, CFA fit, AVE/discriminant) reported where latent constructs used
- [ ] CMB addressed beyond a single-factor test; effect sizes reported
- [ ] Analytical: equilibrium/existence stated; comparative statics interpreted; extensions show robustness
- [ ] DSR: evaluation demonstrates utility against baselines/objectives
- [ ] Claim-to-evidence ledger completed; no claim outruns the analysis
- [ ] Proofs/measurement detail routed to the electronic companion

## Anti-patterns

- **Regression-as-causal** with no identification.
- **Single-factor CMB test** as the sole defense.
- **Algebra dump** with no economic/IS interpretation of the comparative statics.
- **Demo-not-evaluation** for a design-science artifact.
- **Results-first writing** that lists tables without saying which inference each table licenses.

## Output format

```
【Genre】empirical / analytical / design-science
【Identification or proof】[...]
【Validity / robustness】CFA fit, AVE, CMB / extensions / baselines
【Effect size or comparative statics】[...]
【Electronic companion】proofs/items/supplements routed
【Open issues for reviewers】[...]
【Next step】isr-contribution-framing
```
