---
name: cogpsych-theory-and-hypotheses
description: Use when stating the theory, formalizing the model, and deriving predictions for a Cognitive Psychology (Elsevier) manuscript. The journal rewards a formal/computational account whose parameters mean something and whose predictions discriminate it from rivals. Structures the theory and the model that the experiments test; it does not fit the model or run analyses.
---

# Theory, Models & Hypotheses (cogpsych-theory-and-hypotheses)

Cognitive Psychology rewards a **formal account of a cognitive process** — a computational or
mathematical model whose parameters have interpretable meaning and whose predictions can be **fit to
data and compared against rival models**. The cardinal move here is to turn a verbal theory into a
model that makes the experiments *discriminating*, and to separate predicted (confirmatory) from
discovered (exploratory) results.

## When to trigger

- Specifying the theory and the formal/computational model that the experiments will test
- Deriving the predictions that **separate** your account from rival models
- Co-designing the model with the experiments (iterate with `cogpsych-study-design`)
- A reviewer said the work is "atheoretical," "the model is just a curve fit," or "your data don't
  distinguish the accounts"

## Build the theory-and-model

1. **State the cognitive theory.** What mechanism or representation explains the phenomenon, and why —
   in words, before equations. Name the rival accounts you intend to adjudicate.
2. **Formalize it.** Write the model: its representations, processes, free parameters, and what each
   parameter *means* psychologically. A model whose parameters lack interpretation is a red flag here.
3. **Name the rival model(s).** Specify the competing account(s) in the **same formal language** so the
   comparison is fair (nested or matched-flexibility where possible).
4. **Derive discriminating predictions.** Identify the data pattern that the models predict
   *differently* — that qualitative or quantitative signature is what your experiments must produce.
5. **Mark prediction status.** Separate **confirmatory** (pre-committed/preregistered) predictions from
   **exploratory** model exploration done after seeing data; do not present a post hoc fit as predicted.
6. **State what would disconfirm the model.** Which data pattern, or which parameter estimate, would
   count against your account — this is what makes the model a theory, not a fitting exercise.

## Avoiding the "just a curve fit" objection

- A model that fits anything explains nothing. Show the model is **falsifiable** (some data it cannot
  produce) and **identifiable** (its parameters can be recovered — handoff to `cogpsych-data-analysis`).
- Prefer **qualitative signatures** that one model predicts and the other forbids over a small numerical
  edge in fit; reviewers trust a crossed prediction more than a smaller AIC.

## Worked micro-example — theory to discriminating prediction (illustrative)

A recognition-memory program adjudicating two models, written so prediction status is legible.

```
Theory:  Recognition reflects a single continuous memory-strength signal;
         the unequal-variance signal-detection (UVSD) model formalizes it.
Rival:   A dual-process account adds a threshold recollection process (DPSD).
Formalization:
         UVSD parameters: d', sigma(old). DPSD parameters: R (recollection),
         d' (familiarity). Both fit the same confidence-ROC data.
Discriminating prediction (confirmatory, preregistered, Exps 1-3):
         The z-ROC slope is < 1 and *linear* under UVSD; DPSD predicts a
         characteristic U-shaped/curved z-ROC. The shape, not the fit index,
         separates them.
Exploratory: any post hoc parameter that improves DPSD fit is reported as
         exploratory, not as a prediction.
Disconfirming: a reliably curved z-ROC across experiments counts against UVSD,
         stated up front.
```

## Theory-stage reviewer pushback and the venue fix

| Reviewer pushback | Cognitive Psychology fix |
|-------------------|--------------------------|
| "Atheoretical / mechanism unclear" | state the mechanism in words, then give the formal model before the experiments |
| "The model is just a curve fit" | show a falsifiable, identifiable model with a *crossed* qualitative prediction, not only a fit edge |
| "Your data can't distinguish the accounts" | design the discriminating signature into the experiments; formalize both rivals in the same language |
| "Parameters are uninterpretable" | give each free parameter a psychological meaning and a recovery check |
| "This looks post hoc" | mark confirmatory vs. exploratory; pre-commit the model comparison where feasible |

## Theory calibration anchors

- The contribution is the **model-as-theory**, not the experiments alone; experiments earn their place
  by discriminating models, and the model earns its place by being falsifiable and identifiable.
- A crossed qualitative prediction (one model predicts a pattern the other forbids) is worth more than a
  marginal fit advantage; lead with it.
- Pre-commit the model space and the comparison criteria before fitting where you can; deciding the
  winning model after seeing the fits is the modeling form of HARKing.
- Match model flexibility when comparing — a more flexible model that fits better may simply be
  overfitting; this is why parameter recovery and model recovery matter (`cogpsych-data-analysis`).

## Anti-patterns

- A verbal theory with no formal model where the phenomenon is plainly formalizable
- A model with uninterpretable parameters or that cannot fail to fit
- Comparing models of unequal flexibility without acknowledging it
- Presenting a post hoc model selection as a predicted result
- No statement of which data or parameter estimate would disconfirm the account

## Output format

```
【Theory】the mechanism/representation, briefly
【Model】formalization: parameters + their psychological meaning
【Rival(s)】competing account(s) in matched formal language
【Discriminating prediction】the signature that separates the models
【Status】confirmatory (pre-committed) vs exploratory
【Disconfirming evidence】what would count against the model
【Next】cogpsych-literature-positioning
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — modeling frameworks, model-recovery and preregistration tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope and modeling emphasis
