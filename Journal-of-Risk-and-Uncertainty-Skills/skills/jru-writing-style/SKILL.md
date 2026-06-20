---
name: jru-writing-style
description: Use when the prose of a Journal of Risk and Uncertainty (JRU) manuscript must convey a decision model and its measurement with precision. Sharpens abstract, intro, and exposition for a risk/uncertainty audience; it does not invent evidence or citations.
---

# Writing Style (jru-writing-style)

## When to trigger

- The abstract says "we study risk preferences" without naming the primitive, the method, or the headline number
- The introduction motivates with a policy anecdote but never states the decision-theoretic claim
- Notation drifts: the same symbol means utility in one section and value in another, or w(p) is never formally introduced
- The paper reads as either pure theory or pure empirics when JRU readers expect the bridge between them

## The JRU voice

JRU prose is **precise about the decision model and honest about measurement**. The reader is a risk-and-uncertainty specialist who wants, fast: which primitive the paper moves, how it was elicited or estimated, and how big and how precise the effect is. The house register is technical but not ornamental — the model earns its symbols, and every claim is calibrated to what the identification supports.

### Abstract (treat each sentence as load-bearing)

1. The primitive and the question ("How does ambiguity attitude shape insurance takeup?").
2. The method in a phrase (incentive-compatible elicitation; hedonic-wage estimation; an axiomatization).
3. The headline result as a *number with a direction* (a magnitude, not "significant").
4. The decision-theoretic interpretation — what it implies for EU vs. its alternatives.
Keep within the journal's abstract limit (待核实 — verify exact word cap on the official guidelines).

### Introduction

- Open on the **decision-theoretic puzzle**, not a news hook. The motivating tension should be a gap in how we represent or measure a risk primitive.
- State the contribution as a property of a primitive in the first page (mirror `jru-literature-positioning`).
- Preview the identification in one or two sentences — JRU readers want to know *what pins the parameter* before the results.
- Tell the reader what the paper does **not** claim; over-claiming is the fastest route to a skeptical referee.

### Exposition

- Introduce the representation formally before interpreting it; define u, w(p), the prior set, the reference point once and use them consistently.
- Report effects as **magnitudes with precision**, in interpretable units (a VSL in dollars, an elasticity, a λ).
- Keep the experiment's incentive structure and the estimand visible in the main text, not buried in a procedures appendix.

### Calibrating claims to the evidence

JRU's referees are quick to flag prose that runs ahead of the identification. A few habits keep the register honest:

- **Match the verb to the design.** Write "is associated with" for a correlation, "raises" only where the identification supports causation, "is consistent with" when a model fits but is not uniquely identified.
- **Quantify, then interpret.** Lead with the number and its precision; follow with the decision-theoretic reading. Avoid an interpretation the confidence interval cannot bear.
- **Name the scope of the claim.** A lab estimate of loss aversion is a statement about the elicited population and stakes, not a universal constant — say so.
- **Reserve "robust" for the robustness section.** Do not assert robustness in the intro before the checks in `jru-robustness` are reported.

### Section-by-section register

- *Model section:* terse and formal — definitions, then results, then one paragraph of interpretation.
- *Design / data section:* concrete — the mechanism, the stakes, the estimand, the sample, in plain sequence.
- *Results section:* numbers with precision first, decision-theoretic meaning second.
- *Discussion:* the boundary of the claim and what it implies for EU vs. its alternatives, without re-litigating the introduction.

## Checklist

- [ ] The abstract names the primitive, the method, a signed magnitude, and the EU-vs-alternatives interpretation
- [ ] The intro opens on a decision-theoretic puzzle and states the contribution within the first page
- [ ] The identification is previewed before the results
- [ ] Notation for u, w(p), priors, and reference point is defined once and used consistently
- [ ] Effects are reported as magnitudes in interpretable units, with precision
- [ ] The paper explicitly states what it does not claim
- [ ] Abstract/length conform to the journal limits (verify exact caps; mark 待核实 if unconfirmed)

## Anti-patterns

- An abstract that says "significant effects" without a number or a direction
- A policy-anecdote opening that never reaches the decision model
- Symbol drift (u vs. v, w(p) introduced only in a footnote)
- Hiding the incentive mechanism or estimand in an appendix while the intro makes strong claims
- Prose that over-states generality beyond what the elicitation/estimation supports

## Worked vignette (illustrative)

A draft abstract reads: "We run an experiment on decision-making and find significant behavioral effects." The JRU rewrite: "We elicit ambiguity attitudes with an incentive-compatible matching-probabilities task (N illustrative) and estimate an α-MEU model. Ambiguity aversion (α illustrative 0.62) raises the willingness to pay for an unambiguous prospect by [magnitude], a wedge expected utility cannot generate. The result implies insurance demand responds to *ambiguity*, not just to risk." Same study — but the primitive, method, magnitude, and theoretical stakes are all visible.

## Terminology a JRU reader expects you to use precisely

Sloppy vocabulary signals a non-specialist. Use these distinctions exactly:

- **Risk** (known probabilities) vs. **uncertainty / ambiguity** (unknown probabilities) — never interchangeable.
- **Risk aversion** (utility curvature) vs. **probability weighting** (distortion of p) vs. **loss aversion** (asymmetry around a reference point) — three different things, not synonyms for "cautious."
- **Value** v(·) (prospect-theory carrier of utility over gains/losses) vs. **utility** u(·) (EU carrier over final wealth) — keep the symbols distinct.
- **Certainty equivalent**, **risk premium**, **willingness to pay** — defined precisely, not used loosely.

A paper that uses these terms cleanly reads as written by an insider; one that blurs them invites the referee to doubt the rest.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-writing-style
【Verdict】lands / tighten / rebuild abstract
【Abstract has】primitive + method + signed magnitude + EU-vs-alt interpretation [Y/N]
【Intro】decision-theoretic puzzle + contribution on page 1 [Y/N]
【Notation】consistent u / w(p) / priors / reference point [Y/N]
【Limits】abstract/length within journal caps (待核实) [Y/N]
【Next skill】jru-replication-package
```
