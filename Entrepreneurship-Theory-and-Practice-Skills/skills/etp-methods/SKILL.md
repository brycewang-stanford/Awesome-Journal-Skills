---
name: etp-methods
description: Use when designing or defending the research design for an Entrepreneurship Theory and Practice (ETP) manuscript — matching a method to an entrepreneurial question and handling the selection, survivorship, and process-observation problems unique to new ventures. Designs the study; it does not estimate it (etp-data-analysis) or frame the contribution (etp-contribution-framing).
---

# Methods & Research Design (etp-methods)

## When to trigger

- You are choosing a design and unsure it can observe the entrepreneurial process you theorize
- A reviewer flags selection into entrepreneurship, survivorship bias, or an undocumented sampling frame
- The design is cross-sectional but the theory is a venturing *process*
- You are weighing inductive qualitative work, experiments, archival venture panels, or mixed methods
- Construct validity for an entrepreneurial measure (alertness, effectuation, SEW, passion) is in doubt

## ETP is method-plural but theory-first

ETP publishes strong **quantitative, qualitative, and mixed-methods** work; it has no single preferred method. The constant is that the design must let you **build or test entrepreneurship theory** and that it confronts the inference problems that are *endemic to studying new ventures*. Choose the design that can actually observe the mechanism, then design against the entrepreneurship-specific threats below — these are the things ETP referees reflexively probe.

| Entrepreneurial question / claim | Fitting design |
|----------------------------------|----------------|
| How ventures/opportunities emerge; sensemaking; identity work | Inductive qualitative (Gioia, process), longitudinal cases |
| Founder decision logic / cognition under uncertainty | Experiments, conjoint / policy-capturing, verbal protocols |
| Antecedents/consequences across many ventures | Archival venture panels (Crunchbase, PitchBook, GEM, PSED/KFS, registries) |
| Founding, exit, IPO, failure, time-to-event | Survival / event-history models |
| Financing signals (VC, angels, crowdfunding) | Field/natural experiments; panels with funding events |
| Family-firm behavior (SEW) | Survey + archival; sometimes dyadic/family data |
| Theory-building plus generalization | Mixed methods (qual to build, quant to test) |

## The four threats ETP referees reflexively probe

- **Selection into entrepreneurship.** Founders self-select; comparing them to non-founders, or treating "who became an entrepreneur" as random, invites a Heckman/Roy or design-based response. Ignoring selection is a near-automatic flag.
- **Survivorship.** New-venture samples lose failed ventures fast; a sample of survivors silently conditions on success and biases any "what makes ventures succeed" claim. Push the frame upstream to nascent/registry panels (PSED-style) that capture pre-founding and failed ventures.
- **Process observability and temporal precedence.** To claim antecedents or a process, the design must order constructs in time — longitudinal waves, pre/post a shock, staged measurement. A single cross-section cannot carry a venturing-process claim.
- **Construct validity for entrepreneurial constructs.** Effectuation, alertness, passion, SEW, and entrepreneurial orientation are contested measures; cite the validated scale, report reliability, and show discriminant validity from the generic relabel (e.g., effectuation ≠ improvisation; SEW ≠ ownership concentration).

## Qualitative rigor at ETP

For inductive work, ETP expects a visible **trustworthiness** apparatus: a clear data structure (1st-order codes → 2nd-order themes → aggregate dimensions), an audit trail, representative quotations tied to informants, and a process model as the output. Sampling logic (theoretical, not convenience) and saturation should be argued. A rich story without this scaffolding reads as journalism to a methods-attentive ETP reviewer.

## Checklist

- [ ] The design can actually observe/test the theorized entrepreneurial mechanism
- [ ] Selection into founding is modeled or addressed by design
- [ ] Survivorship/attrition handled in the sampling frame, not patched statistically later
- [ ] Temporal precedence supports any antecedent/process claim
- [ ] Entrepreneurial constructs use validated scales with reliability + discriminant validity
- [ ] Qualitative: data structure, audit trail, theoretical sampling, quotations, process model
- [ ] Sample frame, coverage, and construction documented (especially for novel datasets)

## Anti-patterns

- **Survivor-only sample** treated as representative of venture creation
- **Cross-sectional self-report** used to claim a dynamic entrepreneurial process
- **Selection ignored** — founders compared to non-founders as if assignment were random
- **Construct relabeling** — a generic measure renamed as an entrepreneurial one
- **Convenience startup sample** with an undocumented frame
- **Thin qual** — vivid quotes, no data structure or audit trail

## Output format

```text
【Journal】Entrepreneurship Theory and Practice
【Question→design fit】design + why it observes the entrepreneurial mechanism
【Selection】founding-choice strategy (model / design-based / N/A + why)
【Survivorship/attrition】sampling-frame handling
【Temporal precedence】how constructs are ordered in time
【Construct validity】scale + reliability + discriminant evidence
【Qual rigor】data structure / audit trail / saturation (if applicable)
【Next skill】etp-data-analysis
```
