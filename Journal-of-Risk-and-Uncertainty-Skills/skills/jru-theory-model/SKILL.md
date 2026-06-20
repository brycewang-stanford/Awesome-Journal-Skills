---
name: jru-theory-model
description: Use when the decision-theoretic representation is the bottleneck for a Journal of Risk and Uncertainty (JRU) manuscript — axioms, functional form, and behavioral content for choice under risk or uncertainty. Strengthens the model; it does not invent evidence or citations.
---

# Theory and Model Craft (jru-theory-model)

## When to trigger

- The paper proposes or adopts a preference representation (utility + probability weighting, an ambiguity functional) but its **axiomatic foundation** or **behavioral content** is unclear
- A functional form is asserted (CRRA + Prelec weighting, α-MEU, smooth ambiguity) without saying what it rules out
- A referee asks "what does your model predict that EU does not?" and the draft has no crisp answer
- The model is being used to interpret experimental or empirical results but its parameters are not behaviorally interpretable

## The JRU theory bar

JRU is the home of decision theory under risk and uncertainty, so a model is judged on three things at once: an **axiomatic basis** (what preference conditions characterize the representation), a **functional form** that is tractable and identifiable, and **behavioral content** (the model must forbid some observable choices — a representation that fits everything explains nothing). Theory here is rarely art-for-art's-sake; even an axiomatization is expected to connect to measurable behavior, because JRU's readership lives at the theory–experiment–empirics interface.

### Representation discipline

- **State the primitive and the domain.** Are choices over lotteries (risk, known probabilities) or acts (uncertainty, subjective/unknown probabilities)? The Ellsberg-relevant distinction governs which family is admissible.
- **Tie axioms to the functional form.** If you adopt cumulative prospect theory, the axioms are rank-dependence + sign-dependence; for α-MEU, the relevant conditions concern the set of priors and the ambiguity index. Do not present a functional form as if it fell from the sky.
- **Name the behavioral content.** State at least one choice pattern the model **predicts** and one it **forbids**. "It can match Allais and Ellsberg" is content; "it has free parameters" is not.
- **Separate the structural parameter from the nuisance.** Curvature of utility (u) vs. probability weighting (w) are often confounded in EU; a JRU model must say how they are separately interpretable.

### Common representations and what each commits you to

| Family | Commits you to | Watch for |
|--------|----------------|-----------|
| Expected utility (vNM/Savage) | Independence / sure-thing | Allais & Ellsberg violations the data will show |
| (Cumulative) prospect theory | reference point, loss aversion, w(p) | how the reference point is *fixed*, not fit ex post |
| Rank-dependent utility | rank-dependent w(p), no sign-dependence | distinguishing it from CPT empirically |
| α-MEU / maxmin | a set of priors + ambiguity index α | identifying α separately from risk attitude |
| Smooth ambiguity (KMM) | second-order belief + φ curvature | the φ vs. u separation in the data |

### From representation to testable content

A JRU model is only as valuable as the predictions it exports to the experiment or the data:

- **Derive comparative statics, not just existence.** State how the object of interest moves with a parameter (how takeup moves with ambiguity, how the certainty equivalent moves with probability weighting) — these are what the empirical sections test.
- **Map each parameter to an observable.** For every structural parameter, name the choice or moment that will pin it (this is the bridge to `jru-identification`).
- **Show the EU nesting.** State the parameter restriction under which your model collapses to expected utility; the contribution is what happens *away* from that restriction.
- **Keep the model minimal.** Add structure only where it earns a prediction; referees punish free parameters that buy fit without content.

## Checklist

- [ ] Domain stated: risk (lotteries) vs. uncertainty (acts) — and the family matches
- [ ] The functional form is tied to its characterizing axioms, not asserted
- [ ] At least one prediction the model **forbids** is named (falsifiable content)
- [ ] Utility curvature and probability weighting (or risk vs. ambiguity attitude) are separately interpretable
- [ ] The reference point / prior set is pinned down a priori, not fit after seeing choices
- [ ] Comparative statics that the experiment or data can test are derived explicitly
- [ ] Any proof of a key result is in the main text, not exiled to an appendix

## Anti-patterns

- A representation flexible enough to rationalize any choice — JRU referees test for falsifiable content
- Letting the reference point or the set of priors be a free parameter chosen to fit the data
- Conflating utility curvature with probability weighting and calling the bundle "risk aversion"
- Presenting a functional form with no axiomatic story (or an axiomatization with no behavioral implication)
- Claiming an α-MEU model "explains ambiguity aversion" without identifying α apart from u

## Risk vs. uncertainty: pick the right object

The single most consequential modeling choice is whether the primitive is **risk** (objective, known probabilities — lotteries) or **uncertainty** (subjective or unknown probabilities — acts). Getting this wrong invites a fast referee objection.

- If probabilities are given to the agent, model risk: EU, RDU, or CPT over lotteries.
- If probabilities are unknown or the source is ambiguous, model uncertainty: maxmin, α-MEU, smooth ambiguity, or variational preferences over acts.
- If the paper studies how behavior changes *as probabilities become known*, the model must span both and the Ellsberg-style distinction is itself the object of study.

State which world the agent inhabits before writing a single axiom; the admissible representations follow from it.

## Worked vignette (illustrative)

A paper models insurance under ambiguity with smooth ambiguity (KMM). A referee asks what distinguishes it from a risk-averse EU agent with a pessimistic belief. The JRU answer separates the **φ** curvature (ambiguity attitude over second-order beliefs) from **u** curvature (risk attitude), and derives a comparative static EU cannot produce: takeup falls as the *spread of second-order beliefs* widens even when the mean loss probability is held fixed. That prediction is the model's behavioral content and the bridge to the experiment in `jru-identification`.

## When the model is borrowed, not built

Most JRU empirical and experimental papers *adopt* an existing representation rather than axiomatize a new one. The craft is then about disciplined use, not invention:

- **Justify the choice of family** against the closest alternative (why CPT and not RDU; why α-MEU and not smooth ambiguity) in terms of the behavior you need it to capture.
- **Adopt the standard functional forms** (Tversky–Kahneman or Prelec weighting, CRRA/expo-power utility) and say so, so the parameters are comparable to prior estimates.
- **Do not silently modify** a published representation; if you change the reference-point rule or the prior set, flag it and show the consequence.

A borrowed model held to the same content standard — predicts something, forbids something, parameters separately interpretable — is fully publishable at JRU; an idiosyncratic variant smuggled in without justification is not.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-theory-model
【Verdict】sound / sharpen / rebuild representation
【Domain】risk (lotteries) / uncertainty (acts)
【Representation】family + characterizing axioms
【Behavioral content】one prediction it makes, one it forbids
【Parameter separation】u vs. w, or risk vs. ambiguity attitude
【Source status】verified / 待核实 / not asserted
【Next skill】jru-identification
```
