---
name: jebo-theory-model
description: Use when a Journal of Economic Behavior & Organization (JEBO) manuscript needs a behavioral or bounded-rationality model to organize, predict, or interpret its evidence. Right-sizes theory in a pluralist journal — from a sharp testable prediction to a standalone behavioral model or agent-based simulation; it does not design the identification or build the package.
---

# Behavioral Theory & Model (jebo-theory-model)

## When to trigger

- A referee asks "what model rationalizes this behavior / what is the mechanism?"
- The treatment effect is credible but its behavioral *meaning* is ambiguous
- You have a behavioral model but it generates no prediction the experiment could falsify
- You are building an agent-based or evolutionary model and must justify its discipline
- You are tempted to lead with a heavy structural model and need to right-size it for JEBO

## The JEBO theory dial

JEBO is pluralist: theory can be the **lead** (a behavioral/bounded-rationality model is itself the contribution) or the **support** (a model that yields the prediction an experiment tests, or interprets a reduced-form estimate). What JEBO does not reward is theory that adds notation without a **testable behavioral prediction** or a sharper interpretation. Pick the lightest tool that does the job — and whatever the weight, the model's *behavioral primitives* (preferences, beliefs, heuristics, learning rules) must be explicit and defensible, not assumed for convenience.

| Theory's job | Right amount of model | Where it goes |
|--------------|-----------------------|---------------|
| Name the mechanism / give intuition | a few equations or a conceptual frame | short section before results |
| Generate a sharp prediction to test | a small behavioral model with comparative statics | framework section; tested in results |
| Map a reduced-form estimate to a behavioral parameter | sufficient-statistic / structural-behavioral link | inline derivation + appendix |
| Lead the paper (theory is the contribution) | a full behavioral model, with at least one testable implication | main body, with a discipline section |
| Explore emergent organizational/market behavior | agent-based / evolutionary model | main body + robustness sweeps |

### Making the prediction sharp (the usual JEBO sweet spot)

A behavioral model earns its place when it predicts something a *rational benchmark does not* — a sign, an ordering of treatments, a moderator. State the comparative static **before** the results ("the model predicts cooperation rises with γ only when monitoring is salient") so the test is a real test, not a post-hoc fit. A model whose every parameterization confirms the data predicts nothing.

### Behavioral primitives, not free parameters

Whether a social-preference utility (e.g., inequity aversion, reciprocity, reference dependence) or a learning rule (reinforcement, EWA, level-k / cognitive hierarchy), tie each behavioral primitive to something the design measures or the literature constrains. A "behavioral" parameter chosen only to fit the data is decoration.

### Agent-based / evolutionary discipline

Simulation is welcome at JEBO, but referees demand discipline: justify behavioral rules from evidence, calibrate to known moments, report parameter sweeps (handled in jebo-robustness), and distinguish robust emergent regularities from knife-edge artifacts.

## Checklist

- [ ] Theory's job named (mechanism / prediction / mapping / lead / emergent behavior)
- [ ] Lightest adequate tool chosen; weight matches the journal slot
- [ ] At least one comparative static / sign prediction stated *before* it is tested
- [ ] Behavioral primitives (preferences/beliefs/learning rules) tied to data or literature, not free
- [ ] If structural-behavioral: each parameter linked to a data feature; untargeted-moment check
- [ ] If agent-based: rules justified, calibration stated, sweeps planned
- [ ] Predictions/magnitudes carry scope and uncertainty

## Anti-patterns

- A "model" section that adds notation but yields no testable behavioral prediction
- Comparative statics derived *after* seeing the results (HARKing the theory)
- A social-preference or learning parameter chosen purely to fit, with no independent discipline
- Leading a thin empirical paper with a heavy structural model (reads as a different journal)
- An agent-based model whose headline result is a knife-edge of untested tuning choices
- Calling a reduced-form effect "loss aversion" with no model linking the estimate to that primitive

## Worked vignette (illustrative)

A within-firm field study finds output falls after a pay-cut more than it rises after an equal raise. The raw asymmetry is suggestive but ambiguous. The JEBO move: a reference-dependent effort model with the prior wage as the reference point predicts exactly this asymmetry and a *kink* at the reference wage. The paper states the kink prediction before testing, then shows effort drops ~2× as steeply below the reference as it rises above (illustrative) — turning a correlation into a mechanism-level result a reference-free model cannot produce.

## Output format

```text
【Theory's job】mechanism / prediction / mapping / lead / emergent
【Tool chosen】frame / small behavioral model / structural-behavioral / agent-based
【Behavioral primitives】<preferences / beliefs / learning rule> — disciplined by ___
【Sharp prediction (pre-stated)】<sign / ordering / moderator>
【Magnitude or interpretation delivered】[number + scope], or "prediction only"
【Next step】jebo-robustness
```
