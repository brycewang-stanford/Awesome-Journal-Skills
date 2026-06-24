---
name: orgstud-methods
description: Use when choosing and justifying the research design for an Organization Studies (OS) manuscript — qualitative/ethnographic, process, historical, or quantitative — and setting the rigor bar OS reviewers expect. Designs the study; it does not run the analysis (see orgstud-data-analysis).
---

# Methods & Research Design (orgstud-methods)

## When to trigger

- You are choosing between a qualitative/process design and a quantitative one
- The design is chosen but its *rigor and transparency* are not yet defensible to OS reviewers
- A qualitative study lacks a sampling logic, immersion account, or trustworthiness safeguards
- A quantitative study leads with the estimator instead of the organizational mechanism it reveals

## Method follows the theoretical question — and OS leans qualitative

At OS, **no method is privileged in principle**, but the journal's center of gravity is **qualitative, ethnographic, process, and historical** research, and such work is genuinely first-class here — not a tolerated minority. The non-negotiable is that the design fits the question (see `orgstud-theory-development`) and is executed with craft. A sophisticated estimator cannot rescue a thin theory, and a single immersive case can carry an OS paper if the theoretical insight is deep — a different bar from venues where a clean identification design is itself treated as the contribution. OS reviewers ask, above all, *does this design let you see the organizing process you claim to theorize?*

## Branch A — Qualitative / process / ethnographic / historical

Use for *how/why* organizing unfolds: emergence, becoming, contestation, meaning, identity, institutional dynamics.

- **Theoretical (not convenience) sampling.** Cases/sites/informants chosen to illuminate the process or construct; state the logic — polar/extreme cases, theoretical replication, revelatory case, longitudinal window.
- **Access and immersion.** Specify duration, depth, and your role (participant vs. non-participant); for ethnography, time in the field; for historical work, the archive and its limits.
- **Triangulated data sources.** Interviews (count, who, when, guide), observation, internal/archival documents, secondary sources — and how they corroborate.
- **Process design.** If the contribution is a process model, build in the *temporal* leverage: real-time and/or retrospective data, event sequences, turning points (Langley's process strategies — narrative, temporal bracketing, visual mapping — are the standard idiom).
- **Trustworthiness.** Credibility, transferability, dependability, confirmability: member checks, prolonged engagement, audit trail, investigator triangulation, negative-case analysis.
- **Reflexivity.** State your standpoint and how it shaped access and interpretation — expected at a European, critically-aware journal, not optional.

## Branch B — Quantitative organization theory

Use for *whether/how much/under what conditions* across many cases — welcome at OS when it does organization-theoretic work.

- **Sample and unit of analysis** justified by the theory (organizations, fields, events, dyads, individuals nested in units).
- **Identification in service of theory.** Be explicit about the causal claim and its threat (panel FE, event-history/survival, matching, natural experiments, DiD with modern staggered-adoption caveats). At OS, identification is a means to a *theoretical* end; a flawless quasi-experiment that yields no new understanding of organizing is still rejected. Lead with the mechanism, not the estimator.
- **Measurement validity.** Operationalizations defended; multi-item reliability; common-method bias addressed if same-source.
- **Multilevel structure.** If the theory is cross-level, use appropriate models and justify aggregation.

## Either branch

- The design must let you *see the mechanism / process*, not just the endpoints.
- Pre-empt the obvious alternative explanations at the design stage, not only in robustness.
- Plan the data-to-theory link now — it feeds `orgstud-data-analysis` and `orgstud-tables-figures`.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Organization Studies is largely qualitative/theoretical; use the chain below only for its quantitative-empirical papers, and say so when a study is interpretive.

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
- [ ] Qualitative: multiple triangulated sources; trustworthiness safeguards named; reflexivity addressed
- [ ] Process work: temporal leverage built in (real-time/retrospective; turning points)
- [ ] Quantitative: identification explicit and *subordinated to* the organizational mechanism
- [ ] Quantitative: measurement validity and (if needed) multilevel structure handled
- [ ] Obvious alternative explanations are designed against, not just discussed later

## Anti-patterns

- Convenience sampling dressed up as theoretical sampling
- Qualitative work with no transparency about coding, sources, or fieldwork depth
- Treating a fancy estimator as the contribution when the question needs none
- A quantitative paper that reads as applied econometrics with organizational variables bolted on
- A design that can show *that* something happens but never *how/why* organizing produces it
- Omitting reflexivity in interpretive work at a journal that expects it

## Output format

```text
【Design】qualitative (ethnographic/process/historical) / quantitative (type)
【Why it fits】link to the theoretical question and process/mechanism
【Sampling/identification】logic + key threat addressed
【Data sources】list + triangulation / measurement plan
【Temporal leverage】how the design captures process (if applicable)
【Rigor safeguards】trustworthiness + reflexivity, or identification checks
【Next skill】orgstud-data-analysis
```
