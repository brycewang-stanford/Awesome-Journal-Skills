---
name: misq-methods
description: Use when choosing and defending the research design for a MIS Quarterly manuscript — a behavioral survey/experiment, an economics-of-IS identification strategy, a design-science build-and-evaluate cycle, or an organizational/qualitative design. Matches the method to the IS claim and the manuscript category; it designs the study and hands estimation/evaluation to misq-data-analysis.
---

# Research Design & Methods (misq-methods)

## When to trigger

- You have a theory or design propositions but no defensible way to test/evaluate them
- The method may not match the tradition or the claim (e.g., a causal claim with a correlational design)
- A reviewer asks "how do you know the artifact works?" or "what identifies this effect?"
- You need to decide what fits inside the category page limit (which counts everything)

## Match the design to the tradition and claim

MISQ spans four traditions, so there is no single mandated method. Pick the design that the claim requires.

| Tradition | Typical designs | The design must establish |
|-----------|-----------------|----------------------------|
| **Behavioral** | Lab/online experiment, field experiment, multi-wave survey, panel | Internal validity, construct validity, and (for surveys) procedural remedies for common-method bias |
| **Design science** | Build-and-evaluate of an IT artifact | That the artifact is novel and useful for a real problem — utility demonstrated, not asserted |
| **Economics of IS** | Natural experiment, DiD, IV, RD, structural model | A credible identification strategy for the causal/economic effect |
| **Organizational** | Case study, ethnography, mixed methods, longitudinal field | Trustworthiness, rich context, and a transparent path from data to constructs |

## Design science: plan the evaluation up front

A MISQ design-science paper lives or dies on **evaluation**. Following Hevner et al. (2004), decide before building how you will demonstrate utility: held-out benchmarks against credible baselines, a controlled experiment or A/B field deployment, simulation, or expert evaluation — and tie each back to the design propositions. State the problem's relevance, the artifact's novelty, and the evaluation criteria so reviewers can judge rigor *and* relevance. "We built it and it ran" is not an evaluation.

## Behavioral and economics: design out the threats early

- **Behavioral surveys:** build in *procedural* separations against common-method bias — temporal/psychological/source separation, validated scales, attention/manipulation checks — because statistical fixes alone will not convince reviewers later.
- **Economics of IS:** anchor identification in a real source of exogenous variation (a platform/policy change, staggered rollout, a breach, a system go-live). Pre-commit the comparison and the assumptions you will defend.

## Mind the page budget

Because supplementary materials are discouraged and the page limit counts text, tables, figures, references, and appendices, design a study whose evidence fits the chosen category. Scope the design to the page budget rather than planning to offload it to an online appendix.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). MISQ is empirical IS — surveys, econometric panels, experiments, and design science; the chain below serves the causal / econometric lane, while design-science artifacts use their own evaluation standards.

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

- [ ] Design matches the tradition and the strength of the claim
- [ ] Behavioral: validity threats and CMB designed out, not just measured
- [ ] Economics: a named source of exogenous variation and a defensible identification logic
- [ ] Design science: an evaluation plan tied to design propositions and credible baselines
- [ ] Qualitative: a transparent, traceable path from data to constructs
- [ ] The evidence fits the category page limit

## Anti-patterns

- A causal IS claim resting on a cross-sectional correlation.
- A design-science artifact with no comparison and no real-problem evaluation.
- Single-source, single-wave self-report with no procedural CMB remedies.
- A design that only "fits" by exporting half the evidence to discouraged supplements.

## Output format

```
【Tradition & design】experiment / survey / DiD-IV-RD / build-and-evaluate / qualitative
【Identification or evaluation】source of variation OR evaluation plan + baselines
【Validity threats handled】CMB / confounds / trustworthiness
【Fits page budget?】yes / trim
【Next step】misq-data-analysis
```
