---
name: mgsci-data-analysis
description: Use when executing and reporting the analysis for a Management Science (INFORMS) manuscript — proving and numerically verifying analytical results, or estimating and validating empirical models (identification, robustness, inference) to the standard of the relevant Department, and preparing a Data-and-Code-Disclosure-ready replication package. It executes; it does not design the study (mgsci-methods) or frame the contribution (mgsci-contribution-framing).
---

# Analysis & Verification (mgsci-data-analysis)

## When to trigger

- Results are ready to be derived/estimated and reported
- You are unsure whether the analysis actually supports the claim
- Reviewers will probe proof correctness, identification, or robustness
- You must assemble the replication package the Data Editor will verify

Because Management Science is **bimethodological**, "analysis" means proving/computing results in the analytical lane or estimating/validating in the empirical lane. Both are held to their Department's rigor bar.

## Analytical lane — prove, then illustrate

- **Proofs first.** Every proposition/theorem needs a correct, checkable proof (main text or appendix). Reviewers verify the algebra and the logic.
- **Comparative statics** carry the managerial insight — report how the optimal policy/equilibrium moves with each primitive, with sign and intuition.
- **Numerical illustration.** Where closed forms run out, provide computational examples; report parameter ranges and confirm the qualitative result is not knife-edge.
- **Robustness of the model.** Show the insight survives relaxed assumptions / alternative timing / heterogeneity.
- **Reproducible numerics.** Code/notebooks must regenerate every figure and computed example.

## Empirical lane — identify, estimate, stress-test

| Data structure / claim                       | Estimator                                                 |
|----------------------------------------------|-----------------------------------------------------------|
| Causal effect, observational                 | DiD / IV / RDD / event study; cluster-robust SE           |
| Causal effect, controlled                    | Experiment: randomization + manipulation/attention checks |
| Panel with unit heterogeneity                | Fixed/random effects; clustered SE                        |
| Mechanism / structural primitives            | Structural estimation tied to the model                   |
| Count / limited dependent variable           | Poisson/NB, logit/probit, Tobit as fits                   |

- **Identification before estimation.** Name the variation and the threats it rules out; defend exclusion/parallel-trends/continuity as the design requires.
- **Inference.** Cluster standard errors to the sampling/treatment structure; report robustness to alternative specifications, samples, and measures.
- **Behavioral/experimental.** Report manipulation checks, power, and pre-registered vs exploratory analyses distinctly.

## Data and Code Disclosure (mandatory, verified)

Management Science enforces a **Code and Data Disclosure Policy** (effective June 1, 2019; revised April 20, 2026). Authors must create an **AsCollected project page** and provide its URL during submission. Accepted papers with numerical or computational work must provide data, programs, and details sufficient to permit replication before production, or an approved alternative disclosure plan for proprietary/sensitive data. Provide a master script, version-pinned environment, README, data sources, and a clear disclosure plan from the start.

## Execution bridge (StatsPAI / Stata MCP)

Run the analysis, audit it, and keep the scripts — the same scripts satisfy the
AsCollected disclosure above. Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- Fit with `as_handle=true`, then `audit_result(result_id)` to get the missing-checks
  checklist with the exact `suggest_function` for each.
- **Sensitivity:** `honest_did_from_result` (DiD), `oster_delta` / `sensemakr` (OVB).
- **Many outcomes:** `romano_wolf` / `benjamini_hochberg` for the family-wise haircut.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Every reported estimate traces to a tool call; preserve the master script + pinned
environment so the run *is* the replication package. If StatsPAI/Stata are not
connected, adapt the vendored `resources/code/` skeleton and flag any unverified number.

## Anti-patterns

- A proposition with a hand-waved or incorrect proof.
- A causal claim with no credible identification, or clustering that ignores the design.
- Results that appear only with a particular control set (specification searching).
- A replication package that does not actually regenerate the reported numbers.


## Two-lane evidence bar at Management Science

The journal runs analytical and empirical work through different reviewer pools, and the evidence bar differs by lane:

| Element | Analytical lane | Empirical lane |
|---|---|---|
| Core claim | Theorem/proposition with a complete, checkable proof | Causal estimate with credible identification |
| Inference | Comparative statics with signed intuition | Standard errors clustered at the design level |
| Robustness | Relax key assumptions; show what breaks | Alternative specs, subsamples, placebo where available |
| Reproducibility | Self-contained proofs in the appendix | Master script + README that regenerates every reported number |

A frequent desk-to-reviewer failure is mixing lanes: an empirical paper that leans on an un-validated structural assumption, or an analytical paper whose "numerical illustration" silently does the real work. Name the lane, then clear that lane's bar before any prose or submission recommendation.

## Evidence pass for Management Science

Run this as a concrete capability pass. First lock the decision problem, formal or empirical engine, managerial lever, and generality claim; then test whether the manuscript addresses OR/MS reviewers who expect a generalizable decision model, credible empirical leverage, or algorithmic insight with managerial consequence.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Operations Research for method-first optimization, Marketing Science for marketing models, Organization Science for organization-theory mechanisms; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Lane】analytical / empirical
【Core result】proofs verified  OR  estimator + identification
【Comparative statics / inference】sign, intuition, clustered SE ...
【Robustness】relaxed assumptions / alt specs / subsamples ...
【Disclosure package】master script + README + sources: regenerates all main results? yes/no
【Next step】mgsci-contribution-framing
```
