---
name: jpube-data-analysis
description: Use when handling the empirical analysis for a Journal of Public Economics (JPubE) manuscript — administrative tax/transfer/health/register data, elasticity and bunching estimation, sufficient-statistics and MVPF calculations, heterogeneity, and robustness. Executes the analysis plan; for the causal design itself use jpube-identification-strategy.
---

# Data Analysis (jpube-data-analysis)

## When to trigger

- You are estimating a behavioral elasticity, take-up rate, or moral-hazard parameter
- The analysis uses administrative or register microdata with disclosure constraints
- You need to map estimates into welfare (DWL, MVPF, sufficient statistics)
- Robustness, heterogeneity, or measurement concerns are unresolved

## What JPubE analysis looks like

Public economics at JPubE is typically built on **large administrative or register data** — tax records (IRS/SOI), social-insurance files (UI/DI/SSA), health-program data (Medicaid/CMS), or whole-population European registers — because credible policy elasticities need population-scale variation around kinks, notches, and reform dates. The analysis should convert clean identification into a **policy-relevant quantity**, not stop at a coefficient.

## Analysis norms

- **Estimate the policy parameter directly.** Recover the taxable-income / labor-supply elasticity, the take-up or crowd-out rate, or the insurance-vs.-moral-hazard wedge that the welfare argument needs.
- **Sufficient statistics & MVPF.** Where you claim a welfare verdict, show the mapping from estimated responses to the formula explicitly, state the primitives held fixed, and propagate standard errors (delta method or bootstrap) into the welfare object.
- **Respect disclosure and licensing.** Restricted tax/health/register data require formal access and output clearance; document cell-size suppression and the access path, and supply programs even when microdata cannot be shared.
- **Measurement honesty.** Top-coding, income definitions, real-vs.-nominal, and program-rule coding drive public-finance results; document each choice.
- **Heterogeneity that matters for policy.** By income, eligibility margin, or jurisdiction — heterogeneity is the input to optimal nonlinear policy, not a fishing expedition.
- **Robustness.** Bin width and excluded region (bunching), bandwidth (RD/RKD), estimator choice (staggered DID), functional form, and sensitivity of the welfare conclusion to key elasticities.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPubE is public economics — tax/transfer/program designs; DiD/IV/RDD and bunching are central, magnitudes in policy units.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The estimated object is the parameter the welfare claim needs
- [ ] Sufficient-statistics / MVPF mapping shown with primitives stated and SEs propagated
- [ ] Data access, licensing, and disclosure (cell suppression) documented
- [ ] Income / program-rule / top-coding definitions stated and tested
- [ ] Heterogeneity tied to a policy margin, not data-mined
- [ ] Robustness covers the design-specific tuning parameters
- [ ] The welfare conclusion's sensitivity to key elasticities is reported

## Anti-patterns

- Reporting a regression coefficient and never converting it to a welfare quantity
- An MVPF / sufficient-statistic number with no standard error or sensitivity analysis
- Ignoring disclosure rules when describing restricted administrative data
- Subgroup splits with no multiple-testing discipline presented as "heterogeneity"


## Worked example: from elasticity to a welfare number (illustrative)

A DI-reform evaluation recovers a labor-supply response to a benefit cut, then builds the MVPF: the mechanical fiscal saving is the denominator; the behavioral fiscal externality (induced earnings → recovered taxes, minus crowd-out) adjusts the numerator, giving **MVPF ≈ 0.8** (illustrative). The skill's norms then bind: state the primitives held fixed (no GE wage response, fixed program rules); propagate the elasticity's SE through the MVPF by the delta method, reporting a CI on the welfare object; and show how MVPF moves if the key elasticity sits at the high or low end of the literature. The welfare statistic with its uncertainty — not the bare elasticity — is the deliverable.

## Calibration table: estimate → welfare object

| Estimated object | Welfare mapping | Watch for |
|------------------|-----------------|-----------|
| Taxable-income elasticity | Marginal DWL / optimal top rate | Mean reversion, income shifting |
| Take-up / benefit response | MVPF numerator + denominator | Crowd-out onto other programs |

## Evidence pass for Journal of Public Economics

Treat this skill as an executable review pass, not a prose hint. First lock the policy instrument, affected margin, identification design, and welfare or incidence interpretation; then judge whether the current manuscript answers the venue's real reader: public economists who ask whether policy design, fiscal incidence, or welfare interpretation is credible.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JDE for development policy, JIE for cross-border policy, AEJ Economic Policy for broad policy readership; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Data】source + restricted? + disclosure handled? [Y/N]
【Policy parameter】elasticity / take-up / crowd-out / moral-hazard wedge
【Welfare mapping】DWL / MVPF / sufficient stat — SEs propagated? [Y/N]
【Measurement choices】[income def, top-coding, rule coding, ...]
【Heterogeneity】policy margin: [...]
【Robustness done】[bin/bandwidth/estimator/sensitivity, ...]
【Next step】jpube-tables-figures
```
