---
name: jmr-methods
description: Use when matching the research design to the claim for a Journal of Marketing Research (JMR) manuscript — experimental design (lab and field), causal identification (IV/DiD/RDD/matching), or structural/analytical estimation. Adapts to JMR's dominant genres and to its journal-level rigor and replication expectations. It designs; jmr-data-analysis executes and reports.
---

# Research Design & Identification (jmr-methods)

## When to trigger

- The design may not actually support the causal, behavioral, or structural claim
- You must choose between a lab experiment, a field experiment, and observational identification
- A structural model needs an identification and estimation plan
- Reviewers will probe confounds, internal/external validity, or "what identifies this?"

## Match design to the claim by genre

### Behavioral (lab and field experiments)
- **Manipulation**: a clean operationalization of the cause, with manipulation and attention checks; pretests to validate stimuli.
- **Design**: random assignment; factorial designs for interactions; **process-by-moderation** or measured-vs-manipulated mediation to test the mechanism (not just the effect).
- **Field experiments**: a randomized intervention with a real marketing outcome (purchase, click, retention) strengthens external validity; pre-register where feasible.
- **Power**: a priori power analysis sized for the **interaction**, not just the main effect; plan multiple studies (lab establishes mechanism; field shows it in market).

### Modeling / econometric (observational and structural)
- **Causal identification**: choose the strategy the variation supports — IV/2SLS, difference-in-differences (modern estimators for staggered adoption), regression discontinuity, matching, or control-function approaches — and defend the exclusion/parallel-trends/continuity assumptions.
- **Structural estimation**: random-coefficient (BLP-style) demand, dynamic/discrete-choice, or hierarchical-Bayes models; state what data variation identifies each parameter and the estimator (GMM/MLE/MCMC).
- **Data**: scanner/panel (NielsenIQ-IRI), clickstream, platform logs, or field-collaboration data; document sample construction and selection.

## Journal-level expectations that shape design

- The eventual report must carry **exact p-values (three digits), standard errors, and effect sizes** — design and power your studies so these are meaningful, not borderline.
- Plan the **Web Appendix** from the start: full stimuli, additional studies, estimation details, and robustness go there ('W'-prefixed), keeping the print paper within **50 pages**.
- Plan **replication**: per AMA transparency policy you must be able to share code, instruments/stimuli, and materials, and provide data/materials before final acceptance — build clean, documented pipelines now.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMR mixes experiments, structural models, and quasi-experiments; the chain below serves the experimental and reduced-form lanes, while structural demand estimation uses its own toolkit.

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
## Anti-patterns

- A single-cell or confounded manipulation that cannot isolate the cause.
- Claiming causality from cross-sectional correlation with no identification strategy.
- A structural model with an unstated or hand-waved identification argument.
- Underpowered interaction tests; optional-stopping / unreported flexibility.
- Designing studies that cannot meet the exact-statistics or replication mandates.


## Methods pass for Journal of Marketing Research

Run this as a concrete capability pass. First lock the marketing construct, data or study design, inference threat, and managerial or consumer implication; then test whether the manuscript addresses marketing reviewers who expect measurement, experiments, consumer behavior, or empirical strategy to answer a marketing question.

- **Primary move:** Name the estimand or objective, assumptions, diagnostics, robustness checks, and failure modes before accepting the method as venue-ready.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Marketing Science for quantitative modeling, Journal of Marketing for strategic managerial contribution, Journal of Consumer Research for consumer-theory depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric
[Claim] causal / structural / descriptive
[Design] experiment(lab/field) / IV-DiD-RDD-matching / structural
[Identification] assumption + the variation that identifies it
[Power & studies] sized for interaction? lab+field plan?
[Web Appendix / replication] planned
[Next skill] jmr-data-analysis
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
