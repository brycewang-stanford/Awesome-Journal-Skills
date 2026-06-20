---
name: ecopol-writing-style
description: Use when an Economic Policy (EP) manuscript's prose reads like a technical report instead of accessible policy writing. Rewrites for the EP dual audience — non-technical main text, rigor in the appendix; it does not invent evidence or citations.
---

# Writing Style (ecopol-writing-style)

## When to trigger

- The introduction opens with the econometric specification instead of the policy question
- A policymaker would stop reading at the third paragraph because of jargon or notation
- The main text is dense with equations a policy reader cannot follow
- The abstract states what you did, not what a policymaker should now think
- The paper has rigor but not the accessible voice EP is known for

## EP's defining house style: accessible main text, rigorous appendix

This is the most distinctive EP craft skill, because EP's whole identity is **rigorous analysis written accessibly for economists and policymakers together**. The discipline is a *split*: the **main text is non-technical and policy-first**; the **technical machinery — proofs, full estimators, derivations — lives in the appendix**. A reader from a finance ministry should be able to read the main text start to finish and come away with the policy conclusion and the reasoning; an economist should be able to verify everything in the appendix. Write the main text as if explaining to a smart non-specialist, not dumbing down — making the logic legible without notation.

This is a late-stage skill: do not rewrite the intro before identification, the model, and the headline number have settled.

## The EP intro structure (write it in this order)

1. **The policy question and why it is live now** — name the decision a policymaker faces.
2. **What we find — the magnitude, in plain units** — the headline number a non-economist can repeat.
3. **Why it is credible — one plain sentence on the identification**, no notation.
4. **What it implies for policy** — the recommendation or the shift in the debate.
5. **Then** the academic positioning and the road map.

Notice rigor comes *after* the policy payoff, not before. This inverts the typical economics intro.

## Sentence- and section-level moves

- **Verbs over nouns, prose over notation.** "Firms above the threshold cut hiring by 8%" beats "the estimated coefficient on the treatment indicator is −0.08 (s.e. 0.02)."
- **Define every term a policymaker might not know** on first use, in one clause.
- **Move equations to the appendix** unless an equation *is* the clearest way to state a policy relationship; even then, gloss it in words.
- **The abstract is a policy abstract:** question → finding (magnitude) → implication. Confirm the exact abstract length in the live guidelines (待核实).
- **Anticipate the two discussants in the writing:** address the academic's likely concern in a footnote/appendix pointer and the policy reader's "so what" in the text.
- **Avoid hedging fog.** Policymakers need a clear bottom line with its caveats stated, not a paragraph of qualifications that obscures the conclusion.

## Checklist

- [ ] Intro opens with the policy question, not the specification
- [ ] Headline finding stated as a magnitude in plain units within the first page
- [ ] Identification explained in one notation-free sentence in the main text
- [ ] Policy implication stated explicitly, with caveats but a clear bottom line
- [ ] Equations/proofs/full estimators relegated to the technical appendix
- [ ] Jargon defined on first use; a non-economist could follow the main text
- [ ] Abstract is question → magnitude → implication (length per guidelines — 待核实)

## Anti-patterns

- An introduction that leads with the model or the regression equation
- A main text so notation-heavy that the policy discussant cannot read it without the appendix
- An abstract that lists methods instead of stating the policy takeaway
- Hedging so heavy the reader cannot tell what you actually conclude
- "Dumbing down" by removing the rigor instead of moving it to the appendix — EP wants both
- Copying an AEJ:EP-style technical intro and pasting a policy sentence on the end

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-writing-style
【Intro order】policy Q → magnitude → plain identification → implication? Y/N
【Main text legible to non-economist】Y/N
【Notation in main text】minimal / needs moving to appendix
【Abstract】question → magnitude → implication (length 待核实)
【Bottom line】one clear policy sentence present? Y/N
【Next skill】ecopol-replication-package
```
