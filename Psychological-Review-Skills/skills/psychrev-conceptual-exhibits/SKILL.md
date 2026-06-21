---
name: psychrev-conceptual-exhibits
description: Use when designing the figures of a Psychological Review manuscript — model/architecture diagrams and simulation-of-model-behavior plots (NOT experiments). Builds the exhibits; it does NOT derive the predictions they display (psychrev-argument-development) or set the model's scope (psychrev-boundary-conditions).
---

# Conceptual Exhibits: Model Diagrams & Simulation Figures (psychrev-conceptual-exhibits)

## When to trigger

- The theory is built and derived; now it must be shown
- Your figure is boxes-and-arrows with no specified dynamics
- You have a model but no plot of what it *does*
- A reviewer will ask "show me the model's behavior, not just its architecture"

## The two figure types Psychological Review actually uses

Figures here carry **theoretical** work. They are almost never plots of an experiment you ran
(you ran none). There are two legitimate kinds:

1. **Model / architecture diagrams** — the structure of the theory: components, representations,
   information flow, feedback. Every box is a defined construct or module; every arrow is a
   specified process or relationship from the theory, not decoration.
2. **Simulation-of-model-behavior figures** — the model's *output*: predicted curves, surfaces,
   phase portraits, parameter sweeps, fits to existing data. This is the figure that does the
   persuasive work — it shows the model produces (or fails to produce) the diagnostic phenomena.

A third, supporting kind: **model-vs-data** and **model-vs-rival** overlays, where the model's
prediction is plotted against published data points or against a rival model's prediction.

## Design rules for model diagrams

- Every box maps to a named assumption/construct/module in the text; every arrow to a specified
  process. If a reader cannot read the diagram off the model description, it is decoration.
- Distinguish **core** structure from **implementational** detail visually (e.g., shading), so
  reviewers see what is load-bearing.
- Keep the level of analysis consistent within a diagram (do not mix computational and
  implementational components without saying so).
- Label representations and processes with the same terms used in the equations/algorithm.

## Design rules for simulation figures

- Plot the **diagnostic** behaviors — the patterns that distinguish your theory from rivals.
- State, in the caption, the **parameters used** and whether they were fit or set a priori; a
  simulation figure with undisclosed parameters is unreviewable.
- Show **parameter sweeps** where the qualitative pattern is the prediction (the pattern should
  be robust across the plotted range, per `psychrev-boundary-conditions`).
- Overlay **existing data** when confronting the model with evidence; cite the data source.
- When comparing to a rival, plot both predictions on the same axes; do not compare across panels
  with different scales.
- Mark which curves are **predictions** (model not tuned on them) vs. **fits** (tuned).

## Caption discipline (APA)

A Psychological Review caption is self-contained: what the panel shows, the model and
parameters that produced it, the data source if overlaid, and what theoretical point it makes.
Numbering and labels must match the text exactly; reference every figure in the prose.

## Checklist

- [ ] Every model-diagram box is a defined construct/module; every arrow a specified process
- [ ] Core structure is visually distinguished from implementational detail
- [ ] At least one simulation figure shows the model's diagnostic behavior
- [ ] Simulation captions disclose parameters and whether they were fit or set a priori
- [ ] Predictions (untuned) are visually distinguished from fits (tuned)
- [ ] Model-vs-data and model-vs-rival overlays share axes and cite data sources
- [ ] Figures meet APA resolution/format specs; numbering and labels match the text

## Anti-patterns

- A box-and-arrow diagram that cannot be read off the model description (decoration)
- Presenting the architecture but never the behavior the architecture produces
- Simulation figures with undisclosed or cherry-picked parameters
- Comparing model and rival across panels with mismatched axes/scales
- Plotting a fit and implying it is a prediction
- A figure of an experiment — there is no experiment; data appear only to constrain the model

## Output format

```
【Figure list】[Fig 1: diagram | Fig 2..n: simulation/behavior | overlays vs. data/rival]
【Diagram check】boxes=constructs, arrows=processes, core vs. impl. distinguished: yes / fix
【Behavior figures】diagnostic patterns shown; parameters disclosed (fit vs. a priori): yes / fix
【Predictions vs. fits】visually marked: yes / fix
【Captions】self-contained, APA, matched to text: yes / fix
【Next step】psychrev-contribution-framing → psychrev-writing-style
```
