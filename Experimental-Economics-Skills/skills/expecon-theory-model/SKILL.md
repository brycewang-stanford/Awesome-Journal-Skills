---
name: expecon-theory-model
description: Use when turning the behavioral or game-theoretic argument behind an Experimental Economics (ExpEcon) manuscript into pre-specified, testable predictions. Develops the hypotheses tested; it does not run estimation or invent citations.
---

# Theory and Hypotheses (expecon-theory-model)

## When to trigger

- The design exists but the paper never states *which model predicts what* in each treatment
- Competing accounts (selfishness, inequity aversion, reciprocity, social image, level-k, QRE, confusion) all rationalize the same data and you cannot tell them apart
- A referee asks for "the theoretical prediction" and the draft only has informal intuition
- You need the equilibrium/point predictions that your pre-analysis plan will commit to *before* data collection

## Theory here is a hypothesis generator, not the headline

At a method-defined journal, the model earns its place by **producing the predictions your treatments adjudicate**. You do not need a new theorem (that is GEB). You need a transparent map: *given this game and these parameters, model A predicts X in treatment T1 and Y in T2; model B predicts the reverse.* Build that map in four steps.

1. **State the game precisely.** Players, action sets, information, payoffs in **experimental currency units (ECU) and their money conversion**, matching protocol, and horizon. This is the object subjects actually face — write it as they experience it.
2. **Derive the benchmark prediction.** The standard-preferences / Nash / subgame-perfect point (or set). Make it numeric where possible: "the self-interested prediction is a contribution of 0; the social optimum is 20."
3. **Layer the behavioral alternatives.** For each rival account, derive its *distinct* prediction under your parameters — and crucially **how it differs across treatments**. Reciprocity and inequity aversion may agree in T1 but diverge in T2; that divergence is your test.
4. **Pre-specify the directional hypotheses.** Convert each model's prediction into a signed, treatment-indexed hypothesis (H1: contributions higher under T2 than T1) that the PAP will lock. Distinguish **point predictions** (testable against a constant) from **comparative-statics predictions** (testable across treatments) — the latter are usually more robust to noise and confusion.

## Making predictions discriminating

- **Calibrate parameters so models separate.** A common design failure is choosing payoffs where every model predicts the same behavior. Tune the stakes/ratios so the predicted treatment effects of rival models have *opposite signs or different magnitudes*.
- **Handle noise explicitly.** If subjects err, a sharp point prediction may fail mechanically. Either use a structural error model (logit/QRE) you fit, or rely on the *comparative* prediction, which survives symmetric noise.
- **Separate the prediction from confusion.** A treatment difference can reflect the mechanism *or* differential comprehension. Design the contrast so a confusion account predicts no difference (or the wrong sign), then back it with comprehension data (see `expecon-identification`).
- **Keep structural estimation honest.** If you estimate a behavioral parameter (e.g., an inequity-aversion coefficient), it belongs to `expecon-robustness`/`expecon-identification` for identification; here, just state which moments would identify it.

## Equilibrium concept and what it buys you

State which solution concept your benchmark uses, because the experiment will test the behavioral *departure* from it. Nash or subgame-perfect equilibrium gives a sharp point to reject; QRE (quantal response) builds in noise and is often the more honest benchmark for interior behavior; level-k or cognitive-hierarchy is the right benchmark when iterated reasoning is the phenomenon (beauty contests, guessing games). The choice is not cosmetic: a "deviation from Nash" can be fully explained by QRE noise, so if your contribution is that subjects depart *systematically* from the rational benchmark, anchor on QRE and show the residual the noise model cannot absorb. Name the concept, justify it in one sentence, and tie each treatment's prediction to it.

## Worked vignette (illustrative)

A gift-exchange labor experiment wants to test whether reciprocity, not just selfish play, drives effort. Standard preferences predict minimum effort regardless of wage (the benchmark, numeric: e = 1). A reciprocity model predicts effort rising in the wage; inequity aversion *also* predicts a wage–effort link but flattens once payoffs equalize. The two diverge at **high wages**: reciprocity keeps climbing, inequity aversion plateaus. So the design adds a high-wage treatment precisely where the predictions split, and pre-specifies H1 (effort increases in wage) and H2 (the high-wage marginal increase is positive under reciprocity, ≈0 under inequity aversion). Now a single contrast adjudicates.

## Referee pushback mapped to the fix

- *"Your 'theory' has no testable prediction."* → Derive the benchmark point numerically and the rival predictions per treatment; state signed hypotheses.
- *"All your models predict the same thing here."* → Re-calibrate payoffs so rival predictions diverge across treatments; show the divergence.
- *"The point prediction is rejected, but that's just noise."* → Lead with the comparative-statics prediction or fit a QRE/logit error model.
- *"This is a theory paper, not an experiment."* → Drop any claim to a new theorem; frame the model strictly as the hypothesis generator the design tests.

## When the "theory" is a measurement model

Not every ExpEcon paper has a game-theoretic model; some test a **decision-theoretic or measurement** claim (risk attitudes, time preferences, ambiguity, belief updating). The same discipline applies: state the functional form whose parameter you elicit (e.g., CRRA utility, (quasi-)hyperbolic discounting), the **prediction each rival specification makes across treatments**, and the moments that identify the parameter. A treatment that shifts elicited present bias only under one discounting model, and not under another, is your discriminating test. Make that explicit rather than reporting a parameter as if its model were uncontested.

## Checklist

- [ ] The game is written as subjects face it: actions, info, ECU payoffs + conversion, matching, horizon
- [ ] The standard-preferences benchmark is derived and stated numerically
- [ ] Each rival behavioral model has a *distinct* prediction, and the treatments are chosen so predictions diverge
- [ ] Hypotheses are signed, treatment-indexed, and match the pre-analysis plan
- [ ] Point vs. comparative-statics predictions are distinguished
- [ ] A confusion account is shown to predict a different pattern than the mechanism

## How much formalism is enough

The flagship rewards predictions, not page count of algebra. A half-page derivation that yields a sharp, signed, treatment-indexed prediction is worth more than a five-page model whose comparative statics the experiment never tests. If a proof is needed, it goes in an appendix; the main text carries only the predictions the design adjudicates. If your model implies a prediction you did *not* build a treatment to test, either add the treatment or cut the prediction — unused theory invites the "this is a theory paper" objection without earning the credit.

## Translating predictions into the pre-analysis plan

The PAP is where these predictions become commitments, so write them in testable form *now*. For each hypothesis, specify: the **outcome variable** (and how it is constructed from raw choices), the **comparison** (which treatments, which direction), the **test** and the **unit** (session/matching-group), and the **decision rule** (what result confirms vs. rejects). Distinguish the single **primary** confirmatory test from secondary ones. A prediction you cannot phrase as "outcome Y is higher in treatment T than C, tested by [test] at the group level, p<α" is not yet operational — sharpen it here before it reaches `expecon-robustness`, where an unspecified prediction becomes an uncorrected fishing expedition.

## Anti-patterns

- "Theory" that is informal intuition with no derived prediction to test
- Parameter choices where all candidate models predict the same outcome (an undiscriminating design)
- A sharp point prediction with no account of decision noise, then declared "rejected"
- Importing a full new theorem the experiment cannot test — that paper belongs at GEB
- Hypotheses written after seeing the data and presented as pre-specified

## Handoff to the design

The deliverable of this stage is a small table the rest of the pack consumes: for each treatment, the prediction of every candidate model, with the cells where they diverge highlighted. `expecon-identification` uses it to confirm the contrast that produces the divergence is clean; `expecon-robustness` uses the *primary* signed hypothesis to set the powered comparison; `expecon-tables-figures` plots the predicted vs. observed pattern. If you cannot fill that table — if some treatment has no distinct prediction from any model — that treatment is not yet earning its place and should be cut or re-specified before any data are collected.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-theory-model
【Verdict】pass / sharpen / reroute
【Game】players / actions / info / ECU payoffs + conversion / matching / horizon
【Benchmark prediction】standard-preferences point (numeric)
【Rival predictions】model → treatment-indexed prediction (where they diverge)
【Pre-specified hypotheses】H1, H2… (signed, treatment-indexed)
【Confusion check】how the design separates mechanism from comprehension
【Next skill】expecon-identification
```
