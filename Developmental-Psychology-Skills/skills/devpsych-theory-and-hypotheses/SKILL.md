---
name: devpsych-theory-and-hypotheses
description: Use when stating the developmental theory and age-graded hypotheses for a Developmental Psychology (APA) manuscript. The journal rewards hypotheses that are explicitly about change (age effects, within-person trajectories, mechanisms) and a clean confirmatory/exploratory split under JARS. Structures the argument; it does not run analyses.
---

# Developmental Theory & Hypotheses (devpsych-theory-and-hypotheses)

Developmental Psychology rewards a **theory of change** and **age-graded, directional hypotheses**.
Because the journal asks for a credible developmental claim and applies **JARS** reporting, the cardinal
rule is: **state the developmental mechanism and the predicted form of change before the data**, and
label exploratory analyses as exploratory.

## When to trigger

- Writing the theoretical framing and hypotheses
- Preparing a preregistration / pre-analysis plan for a developmental study
- Reconciling what you predicted about change with what the trajectories show
- A reviewer flagged the work as "atheoretical," "not developmental," "post hoc," or "HARKed"

## Build the developmental argument

1. **State the mechanism of change.** What developmental process (maturation, learning, transactional
   parent–child dynamics, scaffolding, cumulative risk) predicts the effect, and *why it changes with age*.
2. **Specify the form of the developmental hypothesis.** Be explicit about which of these you predict:
   an **age main effect**, an **age × condition interaction**, a **growth-curve shape** (slope sign,
   acceleration), a **within-person change**, or a **moderated trajectory**.
3. **Derive directional predictions.** Give a sign and, where possible, a magnitude/effect-size
   expectation — not "age will be related to X."
4. **Mark hypothesis status.** Separate **confirmatory** (preregistered, predicted) from **exploratory**
   (generated after seeing data) analyses, clearly, per JARS.
5. **State what would disconfirm the developmental account** — e.g., a flat trajectory, a reversed age
   slope, or invariance failure that means the construct is not the same across ages.

## Age-graded hypothesis forms (name yours)

| Hypothesis form | What it claims | Typical test |
|-----------------|----------------|--------------|
| Age main effect | level differs by age | age as predictor (cross-sectional or wave) |
| Age × condition | manipulation effect differs by age | interaction term |
| Growth shape | within-person slope/curvature | latent growth / multilevel |
| Sensitive period | effect concentrated in an age window | nonlinear / spline age terms |
| Transactional | child→parent and parent→child over time | cross-lagged / RI-CLPM |

## Worked micro-example — theory to hypothesis status (illustrative)

A longitudinal effortful-control package, written so the developmental claim and status are legible.

```
Mechanism: Sensitive, contingent parenting scaffolds the maturation of
           effortful control; the scaffolding payoff grows across early childhood.
H1 (confirmatory, preregistered): Effortful control shows positive
           within-person growth from age 4 to 8 (latent slope > 0).
H2 (confirmatory): Maternal scaffolding at wave 1 predicts a steeper slope
           (scaffolding × time interaction, directional).
H3 (exploratory): Bidirectional child→parent effects across waves
           (RI-CLPM) — labeled exploratory; preregister for a future sample.
Disconfirming: a flat/negative latent slope, or measurement non-invariance
           across ages (the construct is not the same thing being "grown").
```

## Avoiding HARKing in developmental work

- Do not present an unexpected age interaction or a trajectory shape you discovered post hoc as if it had
  been predicted. If you found it after seeing the data, **say so** and frame it for confirmation.
- Constraints on generality matter here: name the **ages, populations, and cohort/era** to which the
  developmental claim is meant to apply, rather than implying it holds at every age and place.

## Theory-stage reviewer pushback and the venue fix

| Reviewer pushback | Developmental Psychology fix |
|-------------------|------------------------------|
| "Atheoretical / mechanism unclear" | state the developmental mechanism and *why it changes with age* in one or two sentences |
| "This is not developmental" | recast the hypothesis as change (slope/interaction/within-person), not a single-age correlation |
| "Looks HARKed" | show the preregistration; relabel post hoc trajectory shapes exploratory |
| "Claim outruns the design" | scale H1 to what the ages/waves can support; add a constraints-on-generality clause |

## Anti-patterns

- Hypotheses about a relationship "in children/older adults" with no change component
- Non-directional "age will be associated with X" predictions
- Blurring confirmatory and exploratory analyses (JARS expects the split)
- Ignoring that an effect could be cohort, not age, and theorizing as if it were maturation
- No statement of what trajectory or interaction would disconfirm the account

## Output format

```
【Mechanism of change】the developmental process, briefly
【Developmental hypothesis form】age effect / age×condition / growth shape / within-person / moderated
【Hypotheses】directional, testable (H1, H2, …)
【Status】confirmatory (preregistered) vs exploratory
【Disconfirming evidence】trajectory/interaction/invariance result that counts against it
【Next】devpsych-literature-positioning
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration templates and developmental-theory references
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS reporting standards and scope
