---
name: aerj-research-design
description: Use when defending the research design of an American Educational Research Journal (AERJ) manuscript — quantitative (multilevel, IRT, quasi-experimental, RCT), qualitative (case study, ethnography, interview), or mixed methods. AERJ judges each tradition on its own terms against the AERA reporting standards. Strengthens the design; it does not write code.
---

# Research Design (aerj-research-design)

AERJ accepts many methodologies but is demanding about each. The design must credibly connect the
framework (`aerj-theory-and-framework`) to evidence and meet the relevant **AERA reporting standards**.
This skill is mode-aware: pick the section that matches your work and defend it against the strongest
alternative explanation.

## When to trigger

- Specifying sampling, measurement, identification, case selection, or an integration plan
- A reviewer questioned causal claims, generalizability, trustworthiness, or measurement validity
- Preparing a **pre-analysis plan** / preregistration for a prospective design
- Justifying how the design addresses the rival account from `aerj-literature-positioning`

## Quantitative (the field's common designs)
- **Nesting is the default.** Students in classrooms in schools — use **multilevel/HLM** models;
  specify levels, random effects, and cluster-correct inference. Report the design effect / ICC.
- **Measurement.** Tie constructs to validated instruments; report reliability and, where relevant,
  **IRT/factor** evidence. Validity is a design issue, not an afterthought.
- **Causal claims** need a credible design: RCT (with power/MDE, attrition, fidelity), or
  quasi-experimental (DID/event study with modern estimators, RD, IV, matching) — defend identifying
  assumptions, don't assert them. Map to **What Works Clearinghouse**-style expectations when claiming effects.
- **Large-scale assessment data** require plausible values and replicate/survey weights.

## Qualitative (judged on its own terms)
- **Case/site/participant selection** justified by design logic (typical, extreme, theoretical
  sampling), not convenience. Say what the case is a case *of*.
- **Trustworthiness**: prolonged engagement, triangulation, member checks, negative-case analysis,
  audit trail, researcher positionality/reflexivity.
- **Data and analysis**: how data were generated, how coding/interpretation proceeded, how themes
  were warranted by evidence (hand off to `aerj-data-analysis`).

## Mixed methods
- State the **design type** (convergent, explanatory-sequential, exploratory-sequential, embedded) and
  the **rationale** for mixing — what integration buys you that one strand cannot.
- Plan the **point and method of integration** (e.g., joint displays); avoid two papers stapled together.

## The adjudication test (AERJ-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather than
my account, the evidence would look like ___; instead it looks like ___."* If you cannot, the design
does not yet identify the contribution.

## Anti-patterns

- Ignoring nesting (OLS on clustered data); clustering at the wrong level
- "Causal"/"effect" language on a descriptive or associational design
- Convenience sampling dressed up as theoretical sampling
- Mixed methods that never actually integrate
- Treating measurement validity or trustworthiness as boilerplate

## Output format

```
【Mode】quant / qualitative / mixed
【Estimand or claim】what is being identified/shown/understood
【Key assumption(s) / trustworthiness】and how each is defended
【Rival ruled out】the adjudication sentence
【Standards】which AERA reporting standard the design meets
【Next】aerj-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — multilevel/IRT/causal packages and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AERA reporting standards + preregistration notes
