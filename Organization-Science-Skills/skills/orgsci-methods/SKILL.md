---
name: orgsci-methods
description: Use when choosing and defending the research design for an Organization Science manuscript — matching one of the journal's eclectic methods (qualitative/inductive, quantitative/archival, experimental, computational/simulation, formal-analytical) to the question and level of analysis, and justifying design without requiring causal identification.
---

# Research Design & Methods (orgsci-methods)

## When to trigger

- You are choosing a method, or a reviewer says the method does not fit the question
- A reviewer demands causal identification you cannot obtain
- Your level of analysis and your data source do not line up
- You are mixing methods and need to justify the combination

## Match the method to the question — the journal is pluralistic

Organization Science is **methodologically eclectic**: it publishes qualitative and inductive fieldwork, quantitative and archival studies, experiments, computational/simulation models, and formal-analytical theory, and it does not privilege one. The design must **fit the theoretical contribution and the level of analysis**, not signal methodological fashion.

| Theoretical goal / data structure | Design that fits |
|-----------------------------------|------------------|
| Build a new process or construct from the field | Inductive qualitative (grounded theory, ethnography, comparative cases) |
| Test a cross-level mechanism in nested data | Multilevel / HLM with explicit composition or contextual logic |
| Trace organizational founding/failure over time | Event-history / survival; panel |
| Isolate a behavioral mechanism | Lab or field experiment, vignette/conjoint |
| Explore adaptation, learning, search dynamics | Agent-based / NK simulation or formal model |
| Characterize an interfirm or intra-org structure | Network analysis (ERGM, centrality, brokerage) |

## Causal inference is valued but not required

A defining stance: causal inference is valued but **"not necessary and often impossible"** at this venue. Do **not** abandon a strong organizational question because clean identification is unavailable. Instead, support inference with **research design, theoretical logic, institutional/field knowledge, and mechanism evidence** — triangulation, process tracing, placebo and falsification logic, and ruling out alternative explanations. This distinguishes Organization Science from identification-first, economics-leaning venues: a transparent design with a credible mechanism beats a thin paper with a clever instrument.

## Design quality that reviewers check

- **Fit:** the method can actually deliver the theoretical claim and operates at the right level.
- **Transparency:** sampling, case selection, coding scheme, manipulation, model assumptions, or parameter ranges are fully specified.
- **Trustworthiness (qualitative):** purposive sampling rationale, saturation, audit trail, member checks where relevant.
- **Replicability:** enough detail and references that others could reproduce the study; appendices carry the design detail.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Org Science spans field studies, experiments, and computational/qualitative work; the chain below is for its empirical/causal lane — simulation and qualitative work are outside it.

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

- Reaching for an instrument or quasi-experiment the setting cannot support, when mechanism evidence would serve better.
- Aggregating individual data to organizational claims with no composition justification.
- A simulation with no empirical anchor or unjustified parameter ranges.
- Method chosen to look rigorous rather than to test the theory.


## Methods pass for Organization Science

Use this as a second-pass capability check. First lock a level map, a mechanism paragraph, and the cover-letter contribution statement; then test whether the manuscript addresses interdisciplinary organization reviewers who ask whether the mechanism travels across levels of analysis.

- **Primary move:** Name assumptions, diagnostics, robustness, falsification, and failure modes; do not accept a method section that hides the decisive validity threat.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against AMJ for empirical management framing, ASQ for organization-theory depth, Management Science for formal/quantitative operations; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Submission-ready gate:** before final advice, re-open `resources/official-source-map.md` for upload-week rules and name the one live-check item that could change the recommendation.

## Output format

```
【Design】qualitative-inductive / multilevel / panel-EH / experiment / simulation / formal
【Level fit】matches the theoretical claim's level? cross-level logic stated?
【Inference strategy】design + logic + institutional knowledge + mechanism (not identification-only)
【Transparency/trustworthiness plan】sampling, coding, assumptions, audit trail
【Next step】orgsci-data-analysis
```
