---
name: asq-methods
description: Use when choosing and justifying the research design for an Administrative Science Quarterly (ASQ) manuscript — qualitative (grounded-theory, ethnographic, historical) or quantitative — and setting the rigor bar. Designs the study; it does not run the analysis (see asq-data-analysis).
---

# Methods & Research Design (asq-methods)

## When to trigger

- You are deciding between a qualitative/inductive and a quantitative design
- Your design is chosen but its *rigor* and *transparency* are not yet defensible
- A qualitative study lacks theoretical sampling or trustworthiness safeguards
- A quantitative study lacks identification, or its design does not match the theory

## Principle: method follows the theoretical question

At ASQ, neither method is privileged. The journal publishes superb qualitative *and* quantitative work, and the current Editor, **Beth Bechky** (UC Davis; term began July 1, 2025), is herself an ethnographer of work and occupations — a signal that rich fieldwork is genuinely first-class here, not a tolerated minority. The ASQ guidelines say it plainly: "We do not attach greater significance to one methodological style than another, but we value data" — and it is "open to work based on qualitative or quantitative data collected from archives, the lab, or the field, as well as simulations and formal models." The guidelines also stress supporting a *diversity of methods* and ensuring the *trustworthiness* of published work (verify at journals.sagepub.com/author-instructions/asq). What is non-negotiable is that the design fits the question (see `asq-theory-development`) and is executed with rigor. A sophisticated estimator cannot rescue a thin theory, and a single immersive case can carry an ASQ paper if the insight is deep and the craft is high — a different bar from venues where a clean causal-identification design is itself treated as the contribution.

## Branch A — Qualitative / inductive design

Use for *how/why* process, emergence, meaning, identity, and contested dynamics.

Design requirements:

- **Theoretical (not convenience) sampling.** Cases/sites/informants selected to illuminate the construct or process; state the logic (polar types, theoretical replication, extreme/critical case, longitudinal).
- **Access and immersion.** Specify duration, depth, and your role (participant vs. non-participant); for ethnography, time in the field; for historical work, the archive.
- **Data sources, triangulated.** Interviews (count, who, when, semi-structured guide), observation, archival/internal documents, secondary sources — and how they corroborate.
- **Trustworthiness.** Address credibility, transferability, dependability, confirmability: member checks, prolonged engagement, audit trail, investigator triangulation, negative-case analysis.
- **Reflexivity.** Note your standpoint and how it shaped access and interpretation.

## Branch B — Quantitative design

Use for *whether/how much/under what conditions* questions across many cases.

Design requirements:

- **Sample and unit of analysis** justified relative to the theory (organizations, dyads, fields, events, individuals nested in units).
- **Identification (in service of theory).** Be explicit about the causal claim and the threat to it: panel FE, instruments, natural experiments, event-history/survival models, matching, difference-in-differences (with modern staggered-adoption caveats if relevant). At ASQ, identification is a means to a *theoretical* end, not the end itself — a flawless quasi-experiment that yields no new understanding of organizing will still be rejected. Lead with the mechanism the design illuminates, not the estimator.
- **Measurement validity.** Construct operationalization defended; multi-item measures with reliability; address common-method bias if same-source.
- **Multilevel structure.** If theory is cross-level, use appropriate models (HLM/mixed models) and justify level of aggregation.
- **Power and design adequacy** for the effects and interactions claimed.

## Either branch

- The design must let you *see the mechanism*, not just the endpoints.
- Pre-empt the obvious alternative explanations at the design stage, not only in robustness.
- Plan the data-to-theory link now (this feeds `asq-data-analysis` and `asq-tables-figures`).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ASQ wants a clean causal or well-identified observational design behind an organizational-theory contribution; reduced-form estimation fits the chain below, interpretive work does not.

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
## Checklist

- [ ] Design matches the theoretical form (process → qualitative; variance → quantitative)
- [ ] Qualitative: theoretical sampling logic stated; access/immersion specified
- [ ] Qualitative: multiple triangulated data sources; trustworthiness safeguards named
- [ ] Quantitative: identification strategy explicit; causal claims justified
- [ ] Quantitative: measurement validity and (if needed) multilevel structure addressed
- [ ] Obvious alternative explanations are designed against, not just discussed
- [ ] The design can reveal the mechanism, not only the outcome

## Anti-patterns

- Convenience sampling dressed up as theoretical sampling
- Qualitative work with no transparency about coding, sources, or fieldwork depth
- Quantitative work asserting causality from cross-sectional, same-source data
- Choosing a fancy estimator/method to signal rigor when the question doesn't need it
- A design that can show *that* something happens but never *how/why* it happens

## Output format

```
【Design】qualitative (type) / quantitative (type)
【Why it fits】link to the theoretical question
【Sampling/identification】logic + key threat addressed
【Data sources】list + triangulation/measurement plan
【Rigor safeguards】trustworthiness or identification checks
【Next step】asq-data-analysis
```
