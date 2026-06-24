---
name: respol-data-analysis
description: Use when executing and stress-testing the empirical analysis for a Research Policy (RP) manuscript — building bibliometric/patent variables, running estimation or qualitative coding, and assembling robustness that an innovation-studies referee will accept. Executes the analysis; it does not choose the design (respol-methods) or present exhibits (respol-tables-figures).
---

# Data Analysis (respol-data-analysis)

## When to trigger

- Patent/bibliometric variables are built but the construction steps are not documented or reproducible
- Headline results exist but robustness to alternative measures and specifications is thin
- A count outcome (patents, citations) is run with OLS instead of an appropriate count model
- Qualitative coding lacks a transparent coding scheme or inter-coder reliability
- A referee says results are "not robust," "driven by outliers/one sector," or "the data are a black box"

## The Research Policy analysis bar

RP referees know innovation data intimately and distrust opaque pipelines. The two things they probe hardest are **how the variables were built** (especially patent/bibliometric ones) and **whether the finding survives the obvious alternatives**. Counts and skewed distributions are the norm in innovation data, so estimators must respect that; and because most RP indicators are noisy proxies, robustness is not optional decoration — it is how you show the innovation claim, not the measure's artifacts, drives the result.

## Building and modeling innovation data

### Variable construction (document everything)
- For patents/citations: record office, family definition, matching algorithm to firms/regions/inventors, name-disambiguation method, and truncation window. A referee should be able to rebuild the variable from the description plus the deposited code.
- For composite indicators (originality, generality, technological proximity): state the formula and the classification scheme (IPC/CPC) and version used.
- Flag and justify any sample restrictions (years, sectors, minimum patent counts) — selection on the dependent variable is a common RP rejection cause.

### Estimation that fits innovation outcomes
- Patent/citation **counts**: Poisson/negative binomial (or fixed-effects Poisson / PPML) rather than logging-plus-OLS, which mishandles zeros and Jensen's inequality. Address over-dispersion and excess zeros explicitly.
- Skewed continuous outcomes: justify transformation and report level results.
- Panels: choose FE vs. RE on substantive grounds (Hausman is a guide, not a verdict) and cluster at the level of treatment/assignment; address few-cluster inference where relevant.
- Causal designs: report the diagnostics the design demands (pre-trends/event study for DID, first stage and weak-IV-robust inference for IV, density and bandwidth robustness for RDD).

### Qualitative analysis
- Make the coding scheme explicit; report how codes became constructs; report inter-coder agreement where multiple coders; show a data-structure/evidence table linking quotes to constructs.

### Robustness that persuades RP
- Alternative measures of the key innovation construct (e.g., patent count vs. citation-weighted vs. family size).
- Alternative specifications, samples (drop dominant sector/period), and estimators.
- A direct test that the result is not an artifact of the indicator's known bias (e.g., truncation, propensity to patent).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Research Policy is innovation studies — patent/firm panels with selection; foreground identification and the selection objection.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every patent/bibliometric variable is documented well enough to rebuild from the text + code
- [ ] Count outcomes use count models, not log-OLS hacks; zeros and over-dispersion handled
- [ ] Panel FE/RE and clustering choices are justified substantively
- [ ] Causal designs report their required diagnostics
- [ ] Qualitative coding scheme and reliability are transparent
- [ ] Robustness varies the key innovation measure, not just controls
- [ ] At least one check targets the indicator's known bias directly
- [ ] A reproducibility package (data sources + code) is assembled or planned

## Anti-patterns

- A patent-variable "black box" no referee could reconstruct
- Logging patent counts and running OLS instead of a count model
- Robustness that only adds controls and never varies the innovation measure
- Selecting the sample on the outcome (only patenting firms) without addressing it
- Qualitative findings with no visible coding scheme or evidence table
- Reporting only the specification that "works"

## Output format

```text
【Journal】Research Policy
【Skill】respol-data-analysis
【Variable build】patent/bibliometric construction documented? [Y/N]
【Estimator】count/panel/causal choice + why it fits the outcome
【Diagnostics】design-required checks reported
【Robustness】alternative measures + specs + bias-targeted check
【Reproducibility】data sources + code package status
【Verdict】pass / revise / reroute
【Next skill】respol-contribution-framing
```
