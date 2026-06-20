---
name: jle-theory-model
description: Use when a The Journal of Law and Economics (JLE) manuscript needs a model of the legal rule — deterrence, liability, contracting, or regulation — to interpret estimates, generate testable predictions, or carry a theory contribution in the Chicago price-theory tradition. Calibrates how much theory belongs and where; it does not design the identification (jle-identification).
---

# Theory & Model of the Legal Rule (jle-theory-model)

## When to trigger

- A referee asks "what is the economic mechanism / what model rationalizes this legal effect?"
- A reduced-form effect of a rule is credible but its economic meaning (deterrence vs. incapacitation, price vs. quality) is ambiguous
- You want a welfare statement about a legal rule, an optimal-penalty result, or a comparative static the raw estimate cannot deliver
- The paper is theoretical and you need its predictions about a legal rule to be recognizable and testable, not decorative

## The JLE theory tradition

JLE's theory is **price theory applied to legal rules** — Becker on crime (expected punishment = probability × severity), Coase on bargaining and entitlements, Calabresi/Posner on liability and least-cost avoidance, Stigler/Peltzman on regulation and capture, the litigation-selection logic of Priest–Klein. Theory earns its place when it **names the mechanism, maps a coefficient to a structural object, delivers a welfare or optimal-rule result, or generates a comparative static you then test**. JLE accepts genuinely theoretical papers, but even pure theory should speak about a *legal institution* a reader can recognize. Pick the lightest tool that does the job; do not let a model silently replace the identification an empirical design provided.

| Theory's job | Right amount of model | Where it goes |
|--------------|-----------------------|---------------|
| Name the mechanism behind a legal effect | a few equations / a deterrence or bargaining sketch | short framework before results |
| Map a reduced-form coefficient to a structural object (elasticity of crime to expected punishment) | a sufficient-statistic / first-order condition | inline derivation + appendix |
| Deliver a welfare or optimal-penalty result | a calibrated or partial-equilibrium model of the rule | a dedicated, bounded section |
| Generate sign/comparative-static predictions about a rule | a simple model of the legal game | framework section, tested in results |
| Carry a standalone theory contribution | a fully solved model of a legal institution | the body of the paper, with empirical/illustrative discipline |

## Modeling craft

1. **Make the legal rule a primitive.** The penalty schedule, the liability standard, the entitlement, the enforcement probability should be objects in the model, not afterthoughts — that is what makes it law-and-economics rather than generic theory.
2. **Comparative statics before estimates.** Derive the sign predictions about the rule first; test them after. Predictions invented post hoc read as HARKing the theory.
3. **Sufficient statistics where possible.** Express the welfare/optimal-rule object as a function of estimable elasticities (deterrence elasticity, demand response to a penalty) rather than estimating a full structural model — credibility stays in the design.
4. **Tie any structural parameter to the institution.** If you do estimate a model, each parameter should map to a data feature and a legal mechanism, validated against an untargeted moment.
5. **State scope and what the model omits** — general-equilibrium feedbacks, enforcement endogeneity, behavioral departures from rational deterrence.

## Canonical JLE modeling templates (reach for the closest)

Rather than build from scratch, most JLE theory contributions extend one of a few canonical frames. Name the one you are using; referees recognize them and will judge your extension against them.

- **Deterrence (Becker):** expected punishment = probability of apprehension × severity; offenders respond to the margin. Use for crime, enforcement, regulatory penalties, tax evasion. The comparative static you usually want: how an outcome moves with the *expected* (not nominal) penalty.
- **Liability / least-cost avoider (Calabresi–Posner):** negligence vs. strict liability allocate care between injurer and victim; the efficient rule minimizes the sum of accident and avoidance costs. Use for torts, products liability, accidents.
- **Bargaining & entitlements (Coase):** with low transaction costs the efficient outcome is invariant to the entitlement; with frictions the rule matters. Use for property, nuisance, contract remedies.
- **Regulation & capture (Stigler–Peltzman):** regulation is supplied to politically organized groups; the regulator trades off producer and consumer support. Use for entry licensing, rate regulation, occupational rules.
- **Litigation selection (Priest–Klein):** which disputes settle vs. go to trial is endogenous, so trial samples are selected. Use whenever you study court outcomes — it warns against reading trial win-rates naively.

## Checklist

- [ ] Theory's job named (mechanism / mapping / welfare-or-optimal-rule / comparative statics / standalone)
- [ ] The legal rule (penalty, standard, entitlement, enforcement) is a primitive in the model
- [ ] Lightest adequate tool chosen; for empirical papers, the model does not upstage the design
- [ ] If a sufficient statistic: the estimable elasticities and validity assumptions stated
- [ ] If structural: each parameter tied to a data feature and a legal mechanism; untargeted-moment validation
- [ ] Comparative statics / sign predictions derived *before* they are tested
- [ ] Welfare/optimal-rule numbers carry uncertainty and a stated scope (what is omitted)

## Anti-patterns

- A "model" that adds notation but no testable prediction about the legal rule
- Comparative statics produced after seeing the results (HARKing the theory)
- Letting model assumptions quietly substitute for the identification the empirical design should provide
- A welfare or optimal-penalty number with no uncertainty and no statement of omissions
- Generic mechanism-design theory with no recognizable legal institution (drifts toward a theory journal)

## Worked vignette (illustrative)

A clean RD shows a sentence-enhancement threshold cuts re-offending by 5pp (s.e. 1.4). The number is credible but the policy question is whether harsher sentences deter or merely incapacitate. Instead of a full dynamic crime model, the paper uses a Becker-style framework: the deterrence channel predicts a drop in *new* offenses by those still at liberty near the margin, while incapacitation predicts a drop only during custody. A sufficient-statistic argument expresses the marginal deterrence value as the offense elasticity to expected punishment (estimated from the RD) times the social cost per offense (calibrated). The framework yields a testable split the paper then confirms in the timing of effects — the JLE ideal of theory that names and tests a legal mechanism.

## How much theory is too much for an empirical JLE paper

JLE publishes both empirical and theoretical work, so the dial is wider than at an empirical-only journal — but for an *empirical* submission the model should still stay in its lane:

- **Too little:** a reduced-form effect with no framework, leaving the referee to ask "deterrence or incapacitation? price or quality?" with no way to tell.
- **Right:** a compact framework that issues a sign or comparative-static prediction the data then adjudicate, plus (if needed) a sufficient-statistic mapping to a welfare or optimal-rule number.
- **Too much:** a fully solved structural model whose assumptions, not the legal variation, now carry the identification — at which point reviewers ask why the empirical design was needed at all.

For a *theoretical* submission the calculus inverts: the model is the contribution, but it must still concern a recognizable legal institution and yield results an empiricist could in principle confront with data.

## Referee pushback mapped to the theory fix

- *"What is the mechanism behind this legal effect?"* → Add a short framework (deterrence / liability / bargaining) with a sign prediction you then test — not more notation.
- *"This number is not policy-relevant without a welfare statement."* → Express the optimal-rule object as a sufficient statistic of estimable elasticities; state the validity assumptions.
- *"Your model just assumes the result."* → Make the legal rule a primitive, tie each parameter to a data feature and a mechanism, and validate against an untargeted moment.

## Output format

```
【Theory's job】mechanism / coefficient-to-structural mapping / welfare-or-optimal-rule / comparative statics / standalone
【Legal rule as primitive】penalty / standard / entitlement / enforcement: ___
【Tool chosen】framework / sufficient statistic / small structural model / fully solved model
【Key relation】estimand = f(estimable elasticities / parameters): ___
【Predictions derived before testing】[Y/N]
【Validity + what it omits】[...]
【Next step】jle-robustness
```
