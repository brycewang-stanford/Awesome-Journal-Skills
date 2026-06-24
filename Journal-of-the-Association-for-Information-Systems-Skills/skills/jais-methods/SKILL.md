---
name: jais-methods
description: Use when choosing and defending the research design for a Journal of the Association for Information Systems (JAIS) manuscript — a behavioral survey/experiment, an economics-of-IS identification strategy, a design-science build-and-evaluate cycle, a qualitative/interpretive study, or a review method. Matches method to the IS claim under JAIS's methodological pluralism; it designs the study and hands estimation/evaluation to jais-data-analysis.
---

# Research Design & Methods (jais-methods)

## When to trigger

- You have a theory or design propositions but no defensible way to test or evaluate them
- The method may not match the claim (e.g., a causal claim resting on a cross-sectional correlation)
- A reviewer asks "how do you know the artifact works?" or "what identifies this effect?"
- You chose a method by habit/fashion rather than because the phenomenon demands it
- You are designing a Literature Review and need a transparent, reproducible review protocol

## Pluralism is the point — but each method has its own bar

JAIS is explicitly "inclusive in… method and philosophical and research approach," so there is no mandated design. That freedom comes with a duty: **justify the method by the phenomenon and the claim**, and meet the rigor norms of that method's tradition. JAIS reviewers span paradigms, so a method chosen for convenience rather than fit is a recurring rejection. Pick the row your claim requires.

| Tradition | Typical designs | The design must establish |
|-----------|-----------------|----------------------------|
| **Behavioral** | lab/online/field experiment, multi-wave survey, panel | internal validity, construct validity, and (for surveys) *procedural* remedies for common-method bias |
| **Economics of IS** | natural experiment, DiD/event study, IV, RD, structural model | a credible identification strategy for the causal/economic effect |
| **Design science** | build-and-evaluate of an IT artifact | that the artifact is novel and useful for a real problem — utility demonstrated, not asserted |
| **Qualitative / interpretive** | case study, ethnography, grounded theory, mixed methods | trustworthiness, rich context, and a transparent path from data to constructs |
| **Literature review** | structured synthesis or theory-elaborating review | a defended scope, a reproducible search/coding protocol, and a theoretical payoff |

## Let the philosophical stance pick the criteria

JAIS is inclusive of "philosophical and research approach," which means the method must declare its epistemology so reviewers apply the right standards. Positivist work is judged on validity, reliability, and identification; interpretive work on credibility, transferability, and the authenticity of the account; critical work on the reflexivity and the emancipatory or analytic insight; design-science work on artifact utility and the generalizability of design knowledge. Stating the stance up front pre-empts the frequent mismatch where a reviewer from a different paradigm grades the paper against criteria it never claimed to meet.

## Behavioral: design out the threats before you collect

JAIS expects the measurement model to be defensible *by design*, not patched later. Build temporal/source/psychological separation against common-method bias, use validated scales (or justify new ones — but note construct *development* as the headline belongs in the Theory category), and include attention/manipulation checks. Plan to report the full measurement model and, for SEM, the correlation/covariance matrix the journal requires in an appendix.

## Behavioral: prepare the JAIS-required measurement materials now

JAIS asks SEM studies to provide a full correlation/covariance matrix plus descriptives in an appendix, and to make the (anonymized) dataset available on request to Senior Editors and reviewers. Design these into the study from the start: pre-register or pre-specify scales, keep a clean codebook, and structure data collection so the matrix and descriptives fall out automatically. Retrofitting these materials at submission — or worse, at first revision — is where otherwise sound behavioral papers stumble against JAIS's transparency rules.

## Economics of IS: anchor identification in real exogenous variation

Name the source of variation — a platform/policy change, a staggered rollout, a breach, a system go-live — and pre-commit the comparison and the assumptions you will defend. With staggered timing, plan a modern estimator (Callaway–Sant'Anna, Sun–Abraham) rather than naive TWFE, and the event-study and placebo evidence you will show. JAIS publishes econometric IS work, but the identification must be transparent enough for an SE to interrogate.

## Design science: plan the evaluation up front

A JAIS design-science paper lives or dies on **evaluation tied to design principles**. Decide before building how you will demonstrate utility: held-out benchmarks against credible baselines, a controlled experiment or A/B field deployment, simulation, or expert evaluation — and connect each back to a design proposition. "We built it and it ran" is not an evaluation.

## Design science: anchor in a recognized DSR tradition

A JAIS design-science paper should make its design-research logic legible: state the relevant problem, the kernel/justificatory theory behind the design choices, the generalizable design principles, and the evaluation that will test them. The artifact is the vehicle; the prescriptive, reusable design knowledge is the contribution — which is also why JAIS routes such work through its theory-forward lens rather than treating "we built a working system" as sufficient.

## Qualitative/interpretive: make philosophical stance explicit

JAIS welcomes interpretive and critical work, so state your paradigm (positivist, interpretive, critical, design) and let it govern the criteria you invite reviewers to apply. Build a traceable chain from raw data to constructs and an audit trail; trustworthiness, not p-values, is the currency.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAIS spans empirical and design-science IS; apply the chain below to its causal / econometric papers and note when work is design-science or conceptual.

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

- [ ] Design matches the tradition and the strength of the claim, and the choice is justified by the phenomenon
- [ ] Behavioral: validity threats and CMB designed out, not just measured; measurement model planned
- [ ] Economics: a named source of exogenous variation and a modern, defensible identification logic
- [ ] Design science: an evaluation plan tied to design propositions and credible baselines
- [ ] Qualitative: philosophical stance stated; a transparent path from data to constructs
- [ ] Review: scope, reproducible protocol, and theoretical payoff specified
- [ ] Data/code can be made available on request to SEs/reviewers (anonymized) per JAIS policy

## Justify the method to a cross-paradigm panel

Because JAIS's reviewer pool spans paradigms, the method section must do explicit justification work that a single-paradigm journal can leave implicit. State *why this design answers this question* in a sentence a reviewer from another tradition would accept, then meet that tradition's own rigor norms. A positivist reviewer reading an interpretive paper, or an interpretive reviewer reading an experiment, should both be able to see that the method is the right tool — not merely a competently executed default. Pluralism cuts both ways: it widens what is publishable and raises the burden of fit justification.

## Worked vignette: matching method to claim (illustrative)

A team asks whether a firm's adoption of a generative-AI service desk *causes* faster ticket resolution. If the claim is causal, a multi-wave survey of agent perceptions will not earn it — a reviewer will ask "what identifies the effect?" The fitting design names exogenous variation (a staggered rollout across regions), pre-commits a modern staggered-DID estimator and the event-study/placebo evidence, and clusters at the rollout unit. But if the team's real question is *how* agents renegotiate their professional identity around the AI, the causal design answers the wrong question; a qualitative, interpretive design with a stated paradigm and a traceable data-to-construct chain is the rigorous choice. Same setting, different claim, different method — and JAIS will publish either when the fit is argued.

## Anti-patterns

- A causal IS claim resting on a cross-sectional correlation.
- A design-science artifact with no comparison and no real-problem evaluation.
- Single-source, single-wave self-report with no procedural CMB remedies.
- Naive TWFE on staggered treatment with no heterogeneity-bias discussion.
- A qualitative study with no stated paradigm, so reviewers apply mismatched criteria.

## Output format

```text
【Tradition & design】experiment / survey / DiD-IV-RD / build-and-evaluate / qualitative / review
【Identification or evaluation】source of variation OR evaluation plan + baselines OR review protocol
【Validity threats handled】CMB / confounds / trustworthiness
【Paradigm (if interpretive/critical)】stated
【Data availability】can be shared on request (anonymized): yes
【Source status】verified URL / 待核实
【Next skill】jais-data-analysis
```
