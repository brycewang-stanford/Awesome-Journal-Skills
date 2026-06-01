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

Management Science enforces a **Data and Code Disclosure Policy** (articles submitted on/after July 1, 2019). A dedicated **Data Editor (Ben Greiner**, with Milos Fisar and Ali Ozkes) **verifies** that data and code replicate **all main-manuscript results before publication**; appendix replication is welcomed but not compulsory, and verification adds **~17 days** on average. Provide a master script, version-pinned environment, README, data sources, and (where applicable) a pre-registration/project-page URL at submission (AsPredicted / AsCollected — verify the current platform).

## Anti-patterns

- A proposition with a hand-waved or incorrect proof.
- A causal claim with no credible identification, or clustering that ignores the design.
- Results that appear only with a particular control set (specification searching).
- A replication package that does not actually regenerate the reported numbers.

## Output format

```
【Lane】analytical / empirical
【Core result】proofs verified  OR  estimator + identification
【Comparative statics / inference】sign, intuition, clustered SE ...
【Robustness】relaxed assumptions / alt specs / subsamples ...
【Disclosure package】master script + README + sources: regenerates all main results? yes/no
【Next step】mgsci-contribution-framing
```
