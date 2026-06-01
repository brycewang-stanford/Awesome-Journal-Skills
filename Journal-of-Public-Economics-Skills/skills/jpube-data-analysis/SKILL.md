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
