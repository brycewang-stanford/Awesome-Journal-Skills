---
name: ier-theory-model
description: Use when the model is the contribution for an International Economic Review (IER) manuscript and its assumptions, results, or comparative statics are not yet tight. Stress-tests load-bearing assumptions, generality, and the proof to IER's theory/structural bar; it does not write the proofs.
---

# Theory and Model Craft (ier-theory-model)

## When to trigger

- The model "works" numerically but you cannot say which assumption is doing the work
- Existence/uniqueness of equilibrium is asserted rather than proved, or relies on a knife-edge condition
- A referee suspects the headline result is an artifact of a functional-form or parametric choice
- The comparative statics are stated but the *sign* of a key derivative is not signed cleanly
- You are unsure the model is general enough — does the result survive perturbing the convenient assumption?

## Why theory is central at IER

IER tilts theory/structural, and for theory and structural papers the model **is** the contribution — so the bar is not "is the model plausible" but "is the result **tight and general**." A tight result names exactly which assumptions are load-bearing and shows the conclusion is not an accident of a convenient functional form. This is the difference an IER referee looks for between a paper that teaches a general lesson and one that re-derives a known fact under new notation.

### What makes a result "tight" at IER

| Dimension | The tight version | The loose version a referee punishes |
|-----------|-------------------|--------------------------------------|
| Load-bearing assumptions | Each key assumption is flagged, and you show what breaks without it | A long assumption block where the reader can't tell which one drives the result |
| Existence / uniqueness | Proved (or a clean sufficient condition given), with the economic content of the condition explained | "Under standard conditions, an equilibrium exists" with no condition stated |
| Generality | Result holds for a class (general preferences/technology) or you say precisely where it fails | Result shown only for log/CES/quadratic with no claim about robustness |
| Comparative statics | Signs derived analytically; the mechanism (which force dominates) is named | Numerical comparative statics with no analytical sign and no intuition |
| Mechanism | One paragraph of intuition that a non-specialist can follow precedes the algebra | The math stands alone; the reader must reverse-engineer the economics |

### The discipline sequence for an IER model

1. **Write the assumptions as a ranked list**, not a block — order them by how much the result depends on each. The top one or two are your load-bearing assumptions; the rest are for tractability.
2. **For each load-bearing assumption, run the perturbation test**: relax it slightly and report whether the result survives, weakens, or flips. If it flips, that is the paper's real boundary — state it as a result, not a limitation buried in a footnote.
3. **Prove (or cleanly bound) existence and uniqueness**, and translate the condition into economics. A condition like "the demand elasticity exceeds 1" must be explained, not just stated.
4. **Sign the comparative statics analytically** wherever possible; where a sign is ambiguous, decompose it into competing forces and say which dominates and when. This is the comparative-statics craft IER readers expect.
5. **Lead each formal result with intuition.** The model serves a general audience; the proof goes to the appendix (see `ier-replication-package` for the proof-appendix contract), the economics stays in the text.
6. For structural/quantitative work, hand the parameter-identification question to `ier-identification` — "what in the data pins this parameter" is a different question from "is the model tight."

### Worked vignette: making a uniqueness claim tight (illustrative)

A general-equilibrium model with externalities asserts "an equilibrium exists and is unique." A referee flags this as the soft spot — multiplicity would undermine the comparative statics the paper builds on. The loose draft cites "standard fixed-point arguments." The tight IER version states a sufficient condition (say, the externality elasticity is below a threshold), proves uniqueness under it, and then explains the economics: below the threshold the feedback from the externality does not overpower the price mechanism, so the equilibrium map is a contraction. Now the condition is not a technicality — it is the economic boundary of the result, and the comparative statics are safe inside it. If the referee asks "what if the elasticity is above the threshold?", the paper already answers: multiplicity, and the paper says so as a result, not a caveat.

### Why theory craft is judged harder at IER than at applied venues

At an applied journal a model is often a framing device for the empirics, and a referee tolerates a convenient functional form. At IER, when the model *is* the contribution, the same functional-form shortcut is a rejection risk: the referee asks whether the result is a property of the economics or an artifact of the algebra. The perturbation test and the analytical comparative static are how you demonstrate it is the economics — they are not optional polish but the core evidence that the result is real and general.

### The "is it new or is it notation?" gate

The single most common theory-paper rejection at a rigor journal is "this re-derives a known result in new notation." Pre-empt it by stating, in one sentence near the start, what is *new* relative to the closest existing result — a weaker assumption, a sharper conclusion, a previously-unproven case, or a reversal. If you cannot complete the sentence "unlike [closest paper], we show that ___," the contribution may be presentational rather than substantive, and you should revisit `ier-literature-positioning` before investing in the proofs. A genuinely new result usually has a *boundary* the old result lacked — the regime where the conclusion changes — and naming that boundary is the cleanest proof of novelty.

### Generality without overreach

IER rewards generality, but a referee equally punishes a generality claim the proof does not support. The honest move is to prove the result for the broadest class you actually can, then state precisely where it stops. "The result holds for any preferences in class P; outside P, Example 3 shows it can fail" is stronger than a vague "we expect this generalizes." The failure example is not a weakness — it delineates the result and shows you understand its limits, which is exactly the rigor an IER board reads for.

## Checklist

- [ ] Assumptions are ranked; the one or two load-bearing ones are explicitly flagged
- [ ] Each load-bearing assumption has a perturbation test (survive / weaken / flip stated)
- [ ] Existence and uniqueness are proved or given a clean, economically interpreted sufficient condition
- [ ] Comparative statics are signed analytically, or the competing forces are decomposed
- [ ] Every formal result is preceded by a paragraph of mechanism intuition
- [ ] Generality is claimed for a class, or the failure boundary is stated as a result
- [ ] Proofs are appendix-ready and self-contained (handoff to ier-replication-package)

## Anti-patterns

- An undifferentiated assumption block where no reader can identify the load-bearing one
- "An equilibrium exists under standard conditions" with no condition and no economic content
- Headline result shown only under CES/log/quadratic, presented as if general
- Numerical comparative statics substituting for an analytical sign and a named mechanism
- Burying the result's true boundary (where the assumption flips it) in a limitations footnote
- A proof in the body that crowds out the intuition a broad audience needs

## Referee pushback mapped to the theory fix

- *"This re-derives a known result."* → State the one-sentence novelty ("unlike [X], we show ___"); name the boundary/regime where your conclusion differs from the incumbent.
- *"The result is knife-edge."* → Run the perturbation test; prove the result for a class, and state precisely where it fails as a result, not a caveat.
- *"Existence/uniqueness is hand-waved."* → Give a clean sufficient condition, prove it, and explain its economic content.
- *"The comparative static is just numerical."* → Sign the derivative analytically, or decompose the competing forces and say which dominates and when.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-theory-model
【Result (one line)】the theorem/proposition that is the contribution
【Load-bearing assumptions】the 1–2 the result actually rests on
【Perturbation test】what happens when each is relaxed (survive/weaken/flip)
【Existence/uniqueness】proved? condition? economic meaning of the condition
【Comparative statics】which derivatives signed; which forces decomposed
【Mechanism intuition】one-paragraph plain-English mechanism present? [Y/N]
【Verdict】tight / needs-work / not-yet-general
【Next skill】ier-identification (structural) or ier-robustness
```
