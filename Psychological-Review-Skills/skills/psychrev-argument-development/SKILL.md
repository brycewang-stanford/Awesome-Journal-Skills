---
name: psychrev-argument-development
description: Use when deriving predictions from a Psychological Review theory and confronting them with existing data and rival models — the journal's substitute for an empirical results section. Develops the argument; it does NOT build the model (psychrev-theory-construction) or set its scope and identifiability limits (psychrev-boundary-conditions).
---

# Argument Development: Deriving & Confronting Predictions (psychrev-argument-development)

## When to trigger

- The model is built but you have not shown what it *predicts*
- You assert the theory "explains" phenomena without deriving them
- You have not compared your predictions to rival models on diagnostic cases
- A reviewer will ask "could this theory have been wrong?"

## What replaces a results section here

Psychological Review has no experiment of its own as the contribution. The work that an
empirical paper does with data, a Review paper does with **derivation and confrontation**:
you *derive* predictions from the model's assumptions, then *confront* them with already-
existing evidence and with what rival models predict. Logical and quantitative soundness is
the rigor standard, exactly as statistical inference is at empirical journals.

## The derivation discipline

1. **Derive, do not assert.** For each phenomenon in the explanandum, show how it *follows*
   from the assumptions — analytically, or by simulation that traces assumptions → behavior.
   "The model can explain X" is worthless without the derivation that it *does*.
2. **Separate signature from accommodation.** A strong prediction is a **signature** — a
   pattern the theory entails and rivals do not, ideally a *parameter-free* qualitative
   ordering or a novel pattern not used to build the model. Accommodating known data with
   fitted parameters is weaker; label it honestly as accommodation, not prediction.
3. **Make at least one risky, novel prediction.** Falsifiability is the journal's currency:
   name a pattern that, if observed, would *disconfirm* the theory, and ideally one not yet
   tested so future work can adjudicate.

## The confrontation discipline

- **Confront existing data.** Use published datasets (yours or others') to show the model
  reproduces the diagnostic phenomena. Report fit honestly: degrees of freedom, number of
  free parameters, and whether parameters were estimated or set a priori.
- **Confront rival models head-to-head.** On each diagnostic phenomenon, show what your model
  and the rival each predict, and why the data favor yours. A nested or formal model
  comparison (e.g., information criteria, parameter recovery) beats a verbal contrast.
- **Address alternative explanations.** For every prediction your model gets right, ask
  whether a simpler rival gets it right too; if so, the case is not diagnostic — find one
  that is.
- **Probe robustness.** Show the key results do not depend on a fragile parameter setting or
  an arbitrary functional form (sensitivity over a plausible range).

## Quantitative honesty (for formal models)

- State the number of free parameters and what each was fit to.
- Distinguish **fit** (reproducing data used to build the model) from **prediction**
  (data the model was not tuned on).
- Prefer **generalization** tests (fit on one set, predict another) over in-sample fit.
- Beware flexibility: a model that can fit any pattern predicts nothing — show what it *cannot* do.

## Checklist

- [ ] Each explanandum phenomenon is *derived*, not merely asserted, from the assumptions
- [ ] At least one risky, novel, falsifiable prediction is stated
- [ ] Signatures (rival-distinguishing) are separated from accommodations (fitted)
- [ ] Existing data are used to confront the model; free-parameter count is disclosed
- [ ] Head-to-head comparison with rival models on diagnostic phenomena is shown
- [ ] Alternative simpler explanations are ruled out on each diagnostic case
- [ ] Robustness to parameter/functional-form choices is demonstrated

## Anti-patterns

- "The model can explain X" with no derivation that it does
- Fitting known data and calling accommodation a prediction
- A model so flexible it could fit any result (and therefore predicts nothing)
- Verbal hand-waving where a rival has a formal, quantitative account
- Hiding the number of free parameters or which data were used to fit them
- Picking only phenomena where all theories agree (non-diagnostic)
- Introducing a brand-new experiment as the deciding evidence (data only constrain here)

## Output format

```
【Derivations】[phenomenon → how it follows from assumptions] for each
【Signatures vs. accommodations】[risky/novel predictions] | [fitted accommodations]
【Confrontation】existing data used; free-parameter count; fit vs. generalization
【Head-to-head】[diagnostic phenomenon → your prediction vs. rival's vs. data]
【Robustness】key results stable over parameter/form range: yes / fix
【Next step】psychrev-boundary-conditions (scope, identifiability, what it does NOT explain)
```
