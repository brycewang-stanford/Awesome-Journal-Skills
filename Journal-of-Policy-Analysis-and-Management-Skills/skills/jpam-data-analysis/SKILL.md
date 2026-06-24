---
name: jpam-data-analysis
description: Use when running and reporting the estimation for a Journal of Policy Analysis and Management (JPAM) manuscript — program-evaluation estimates plus the cost-benefit and distributional analysis JPAM expects, with robustness, heterogeneity, and honest uncertainty. Guides analysis norms; it does not replace the identification design.
---

# Data Analysis: Estimation, Cost-Benefit & Distribution (jpam-data-analysis)

JPAM analysis has two layers most field-journal papers skip: beyond the **causal estimate**, reviewers
expect attention to **cost-benefit** and **distributional** consequences — *who gains, who pays, and is
it worth it?* The estimate answers "does the policy work"; the cost-benefit and distributional work
answers "should we do it, and for whom." Both must be reported honestly, with uncertainty carried
through.

## When to trigger

- Producing the main estimates and the robustness/heterogeneity suite
- Adding (or being asked to add) cost-benefit or distributional analysis
- A reviewer questioned standard errors, robustness, or the policy-relevance of the magnitude
- Translating an effect size into a decision-relevant quantity (per-dollar, per-recipient, MVPF)

## Estimation norms

- **Report effects in policy-relevant units** — percentage points, dollars, per-recipient, per-dollar-
  spent — not just standardized coefficients.
- **Robustness as a coherent suite**, not a coefficient dump: alternative specifications, samples,
  bandwidths/estimators, and a placebo where the design allows. Show the result is not knife-edge.
- **Theory-driven heterogeneity** (from `jpam-theory-building`), pre-specified where possible; report
  which subgroup tests are primary and adjust for multiplicity.
- **Honest uncertainty** — confidence intervals, not just stars; discuss precision when a null is
  policy-relevant ("we can rule out effects larger than X").

## Cost-benefit & distributional analysis (JPAM premium)

- **Cost-benefit:** monetize benefits and costs on a common basis, state the discount rate and the
  perspective (government budget vs. society), and run sensitivity to key assumptions. Where suitable,
  report the **Marginal Value of Public Funds (MVPF)** or benefit-cost ratio.
- **Distributional:** show *who* gains and *who* bears the cost (by income, race, region, recipient vs.
  taxpayer). A positive average effect with regressive incidence is a different policy story — say so.
- **Fiscal externalities:** account for downstream budget effects (e.g., reduced transfers, increased
  tax revenue) where the literature does.
- **Carry uncertainty through** to the cost-benefit conclusion — do not present a point ratio as if the
  estimate were certain.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPAM is policy analysis — program evaluation is the core; DiD/IV/RDD and the policy-relevant magnitude are decisive.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Effects reported in policy-relevant units, not only standardized
- [ ] Robustness suite addresses the design's specific vulnerabilities
- [ ] Heterogeneity tied to the theory of change; multiple-testing handled
- [ ] Confidence intervals reported; informative nulls discussed
- [ ] Cost-benefit with stated perspective, discount rate, and sensitivity (MVPF / BCR where apt)
- [ ] Distributional incidence shown — who gains, who pays
- [ ] Fiscal externalities considered where relevant
- [ ] Every number in the text matches the deposited replication output

## Anti-patterns

- Reporting only standardized effects a policymaker cannot act on
- A robustness "kitchen sink" that never states which checks address which threat
- Cost-benefit with a hidden discount rate or perspective, and no sensitivity analysis
- A flattering average effect that hides regressive distribution
- Presenting a benefit-cost ratio as certain when the underlying estimate has a wide CI
- Post hoc subgroup hunting presented as confirmatory

## Calibration anchors (hedged)

- The cost-benefit and distributional layers are what most distinguish a JPAM analysis from a field-
  economics paper — budget time for them, do not bolt them on at the end.
- An MVPF or benefit-cost ratio is only as credible as the estimate it rests on; report its sensitivity
  to the effect-size CI and to the discount rate, not a single point.
- A precisely estimated null can be a publishable JPAM result if it rules out a policy-relevant effect
  — frame it as "we can rule out effects larger than X," not "no effect."

## Worked micro-example (illustrative)

An evaluation finds a job-training program raises quarterly earnings by \$420 (95% CI \$120–\$720). The
JPAM analysis does not stop there: it converts this to a **benefit-cost ratio** (lifetime earnings gain
vs. per-participant cost) under a stated discount rate, runs **sensitivity** across the CI and discount
rate, shows the gain is **concentrated among longer-tenured entrants** (theory-driven heterogeneity), and
notes the program is **net-positive to the government budget** only above a take-up threshold. The policy
story is the package, not the \$420. (Numbers illustrative.)

## Output format

```
【Main estimate】effect in policy-relevant units (+ CI)
【Robustness】checks mapped to specific threats
【Heterogeneity】theory-driven subgroups + multiplicity handling
【Cost-benefit】perspective, discount rate, MVPF/BCR, sensitivity
【Distribution】who gains / who pays
【Next】jpam-tables-figures
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — estimation + robustness skeletons (Stata + Python)
- [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md) — inference + reporting table stakes
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — cost-benefit / MVPF tooling and policy data sources
