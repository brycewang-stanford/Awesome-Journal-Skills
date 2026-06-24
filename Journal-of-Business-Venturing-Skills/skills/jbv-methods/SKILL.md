---
name: jbv-methods
description: Use when designing or defending the research design for a Journal of Business Venturing (JBV) manuscript — matching a methodologically pluralistic but theory-first approach (venture panels, experiments, qualitative process work, mixed methods) to an entrepreneurial question, and handling selection, survival, and novel-dataset issues. Designs the study; it does not estimate it (jbv-data-analysis) or frame the contribution (jbv-contribution-framing).
---

# Methods & Research Design (jbv-methods)

## When to trigger

- You are choosing a design and unsure which fits a venture-creation question
- The design may not let you observe the entrepreneurial process you theorize
- A reviewer flags selection into entrepreneurship, survivorship bias, or sample novelty
- You are weighing qualitative process work, experiments, archival venture panels, or mixed methods

## JBV is methodologically pluralistic — but theory-first

JBV prizes a clear, substantive **theoretical contribution to entrepreneurship** over any single method. Well-executed qualitative, conceptual, quantitative, and mixed-method studies are equally welcomed; the unifying demand is that the work advance theory about the entrepreneurial phenomenon, not merely apply a method. Choose the design that can actually test or build your theory:

| Entrepreneurial question / claim                         | Fitting design                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------|
| Process of how ventures emerge / sensemaking             | Inductive qualitative (Gioia, process), longitudinal case studies |
| Entrepreneurial judgment / cognition under uncertainty   | Experiments, conjoint/policy-capturing, vignettes (Prolific/lab)  |
| Antecedents/consequences across many ventures            | Archival venture panels (Crunchbase, PitchBook, GEM, KFS, PSED)   |
| Founding choice, exit, IPO, failure                      | Survival/event-history; selection models                          |
| Financing signals (VC, crowdfunding)                     | Field/natural experiments, panel with funding events              |
| Theory-building plus generalization                      | Mixed methods (qual to build, quant to test)                      |

## Design issues specific to the entrepreneurial setting

- **Selection into entrepreneurship**: founders self-select; model the choice (Heckman/Roy) or use design-based identification rather than ignoring it.
- **Survivorship**: new-venture samples lose failed ventures fast; a sample of survivors silently conditions on success. Design to observe pre-founding and failed ventures (PSED-style nascent panels, registry data).
- **Novel datasets**: JBV values new entrepreneurship data; document construction, coverage, and the sampling frame transparently — novelty is an asset only if the frame is defensible.
- **Temporal precedence**: to claim antecedents/mechanisms, the design must order them in time (longitudinal, pre/post a shock, staged measurement).

## Co-submission of method artifacts

The Editorial Manager workflow lets you attach a **MethodsX** article (detailed protocol) or **Data in Brief** descriptor on the "Attach files" page — useful for novel measures, hand-coded datasets, or experimental protocols.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBV studies founders and ventures where selection / survivorship threatens every claim; lead with identification and selection-correction tooling.

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

- [ ] Design can actually observe/test the theorized entrepreneurial mechanism
- [ ] Selection into founding addressed (modeled or design-based)
- [ ] Survivorship/attrition handled in the sampling frame, not just statistically later
- [ ] Novel dataset's construction, coverage, and frame documented
- [ ] Temporal precedence supports the antecedent/mechanism claim
- [ ] Qual studies: trustworthiness plan (data structure, audit trail, quotations)
- [ ] Considered MethodsX / Data in Brief co-submission for protocols/data

## Design referee-pushback patterns and the JBV-specific fix

| Pushback at the design stage                              | JBV-specific fix                                                                    |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------|
| "Cross-sectional, yet you theorize a venturing *process*."| Re-design with staged measurement or a pre/post shock; a single wave cannot carry a process claim.|
| "The construct is general-management ability relabeled."  | Anchor the manipulation/measure to a venture primitive and show discriminant validity from it.|
| "Your sample is whoever survived to be observed."         | Push the frame upstream to nascent/registry data capturing pre-founding and failed ventures.|
| "A novel hand-coded dataset — why trust the frame?"       | Document construction, inter-coder reliability, and coverage; consider a MethodsX/Data in Brief co-submission.|

## Worked micro-example (illustrative)

A hypothetical JBV study claims *perceived environmental uncertainty* causes founders to evaluate ambiguous opportunities more favorably. Design reasoning:

- **Why an experiment**: the claim is causal and about entrepreneurial *judgment*, so a vignette experiment (240 founders, illustrative) manipulates uncertainty while holding the opportunity fixed — isolating the targeted cognition.
- **Construct guard**: the vignette describes a *new-venture* opportunity under Knightian uncertainty, not a generic managerial decision, so a referee cannot recast it as ordinary risk-taking.
- **Triangulation**: pair it with an archival panel where a plausibly exogenous uncertainty shock shifts real founding/financing — answering "lab artificiality" by design.
- **Temporal precedence**: in the archival arm, measure uncertainty *before* the founding outcome so the antecedent claim is ordered in time.

## Calibration anchors (hedged)

- JBV is method-pluralist: a deep inductive study and a clean field experiment clear the *same* bar if both advance entrepreneurship theory. The dividing line is **theory payoff**, not method prestige.
- The desk-reject-adjacent failure is the **survivor-only, single-wave, generic-construct** combination; design against all three up front.
- Artifact options (MethodsX, Data in Brief) can change; **confirm against the journal's current author guidelines**.

## Anti-patterns

- **Method-led, theory-light** — a clean identification with no entrepreneurship-theory payoff.
- **Survivor-only sample** treated as representative of venture creation.
- **Cross-sectional self-report** used to claim a dynamic entrepreneurial process.
- **Convenience startup sample** with an undocumented frame.

## Output format

```
【Question→design fit】design chosen + why it fits the entrepreneurial claim ...
【Selection】founding-choice strategy ...
【Survivorship/attrition】sampling-frame handling ...
【Data novelty】construction + coverage + frame ...
【Temporal precedence】how ordered in time ...
【Artifacts】MethodsX / Data in Brief? ...
【Next step】jbv-data-analysis
```
