---
name: jais-contribution-framing
description: Use when sharpening the theoretical contribution of a Journal of the Association for Information Systems (JAIS) manuscript — stating what the paper adds to IS knowledge, matching the contribution claim to the chosen category, and making it legible to a pluralistic, theory-forward reviewer pool. Frames and tests the contribution; it does not build the theory (jais-theory-development) or run the analysis (jais-data-analysis).
---

# Contribution Framing (jais-contribution-framing)

## When to trigger

- Results exist but the "so what for IS theory" is thin, implicit, or generic
- A Senior Editor or reviewer says "the contribution is unclear" or "this is incremental"
- The contribution you claim does not match the category you submitted to
- You can describe what you *did* but not what the field now *knows* that it did not
- You are unsure whether the contribution is theoretical, methodological, or empirical — and JAIS prizes the first two explicitly

## What "contribution" means at JAIS

JAIS exists to publish "innovative, interesting and rigorously developed conceptual and empirical contributions" and to "encourage theory based multi- or inter-disciplinary research." Two things follow. First, **theory and method are contributions in their own right** here — more than at most siblings, a paper whose payoff is a new theory, framework, or methodological advance is welcome on its own terms. Second, "interesting" is doing real work in that sentence: JAIS rewards a contribution that is generative and a little surprising, not a confirmatory increment to a settled question. State the contribution as *what the field now knows or can do that it could not before*.

## Match the contribution claim to the category

The category you chose sets the kind of contribution reviewers expect. A mismatch reads as confused framing.

| Category | The contribution claim should be… |
|----------|-----------------------------------|
| **Theory** | a new construct, a novel framework, or a generative integration — the theory *is* the payoff |
| **Research Article** | a theory-grounded empirical/design result; *not* primarily "we built a new construct" (that belongs in Theory) |
| **Literature Review** | new research directions, or theory developed/elaborated through synthesis |
| **Research Perspectives** | a reframing that changes how the field sees an assumption or practice |
| **Foundational Research** | the first disciplined account of a novel digital phenomenon, with new or pre-theoretical insight |
| **Policy and Impact** | a credible translation from IS research to policy |

## "Interesting" is a JAIS criterion, not a flourish

The about-page phrase "innovative, interesting and rigorously developed" is doing evaluative work. JAIS rewards contributions that challenge an assumption the field holds, surface a counterintuitive mechanism, or reframe a settled debate — not contributions that merely confirm an expected effect with cleaner data. When you frame the contribution, test it against this bar: *which prior belief does this unsettle?* A paper that answers "none, but our estimate is more precise" is rigorous but not interesting, and at JAIS that is a reason for rejection, not a minor revision. Pair the surprise with the rigor; one without the other does not clear the bar.

## Frame it in one auditable sentence

Write: *"Before this paper, IS scholars [believed / could not / lacked X]; this paper shows [Y], which changes [Z]."* Then check that every section earns its place against that sentence. The abstract and introduction should let a reviewer from a *different* tradition grasp the contribution without your sub-field's shorthand — pluralism means your reader may not share your priors.

A useful stress test: hand the one-sentence contribution to a colleague in another IS tradition and ask them to restate what is new. If they can only restate what you *did* (the method, the data), the contribution is still framed as activity; if they can restate what the field now *knows*, it is framed as a contribution. JAIS's pluralistic reviewer pool effectively runs this test for you — better to pass it before submission than to learn the answer in the decision letter.

## Name the type of theoretical contribution

Reviewers respond better when you say *what kind* of theoretical move you are making, because it tells them which yardstick to apply. The common JAIS-relevant types: introducing a **new construct**; building a **new framework or model** relating constructs; offering a **novel integration** that reconciles two theories; identifying a **boundary condition** that bounds an accepted claim; surfacing a **new mechanism** behind a known relationship; or, in the Foundational category, a **pre-theoretical insight** about a phenomenon too new to model. State the type in the introduction so the contribution is not left for the reviewer to reverse-engineer.

## Separate the theoretical from the empirical and managerial

JAIS reviewers will not accept a strong finding as a substitute for a theoretical contribution. State the theoretical advance first, then the empirical evidence that supports it, then (briefly) implications for practice. A paper with rich data but no theoretical payoff is a desk-reject; a paper with a sharp theory and honest, scoped evidence can succeed.

## Checklist

- [ ] The contribution is stated as a change in what the field knows or can do, in one sentence
- [ ] The contribution kind (theoretical / methodological / empirical) is explicit
- [ ] The claim matches the chosen JAIS category's expectation
- [ ] A reviewer from a different IS tradition could grasp it without insider shorthand
- [ ] The contribution is "interesting/generative," not a confirmatory increment
- [ ] The theoretical advance is not silently replaced by a strong empirical finding
- [ ] Boundary conditions keep the claim from over-reaching the evidence

## Referee pushback mapped to the framing fix

- *"The contribution is incremental."* → Re-state it as a change in what the field knows ("before this paper… ; this paper shows…"), and show the prior belief it overturns or the gap it closes — not a marginal effect-size update.
- *"This reads as a strong finding without a theoretical contribution."* → Lead with the theoretical advance; demote the empirical result to evidence *for* it. JAIS will not accept data in place of theory.
- *"Why is this a Research Article and not a Theory paper?"* → If the real novelty is a construct or framework, re-categorize; if it is the empirical test of an existing theory, say so and keep the construct claims modest.
- *"I can't tell what's new for my sub-field."* → Add a sentence translating the contribution into terms a reviewer from another IS tradition would value.

## Worked vignette (illustrative)

A paper reports that a platform's switch to algorithmic matching raised transaction completion by a measured amount. Framed as activity — "we analyzed 2.3M transactions before and after a matching-algorithm change" — it reads as a strong finding with no theory, a likely JAIS desk-reject. Reframed for JAIS: "Before this paper, IS theory treated platform matching as a search-cost reduction; this paper shows it also reshapes *who trusts whom*, introducing an algorithmic-trust channel that the search-cost account cannot explain — which changes how we theorize platform governance." The number now serves a theoretical advance, and the contribution is legible to behavioral, economic, and design-science reviewers alike. If the algorithmic-trust channel is the whole payoff, the paper may belong in the Theory category instead.

## Anti-patterns

- A contribution stated as activity ("we conducted a survey of…") rather than as new knowledge.
- Claiming a theory contribution in a Research Article whose real novelty is a new construct (route to Theory).
- An "incremental confirmation" framing in a journal that prizes interesting, generative work.
- Letting managerial implications stand in for a theoretical contribution.
- A contribution legible only to one sub-tradition while the reviewer pool spans five.

## Output format

```text
【Journal】Journal of the Association for Information Systems (JAIS)
【Contribution sentence】before this paper… ; this paper shows… ; which changes…
【Contribution kind】theoretical / methodological / empirical
【Category match】claim fits Theory / Research Article / Review / Perspectives / Foundational / Policy
【Cross-tradition legibility】graspable without insider shorthand: yes/fix
【Boundary conditions】claim scoped to evidence: yes/fix
【Next skill】jais-tables-figures
```
