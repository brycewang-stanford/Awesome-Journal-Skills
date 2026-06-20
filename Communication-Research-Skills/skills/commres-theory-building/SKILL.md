---
name: commres-theory-building
description: Use when building the theoretical argument and hypotheses of a Communication Research (CR) manuscript into a testable, mechanism-level contribution. CR rewards explicit constructs, a stated communication process, and numbered hypotheses with mediation/moderation, not a bare effect. Structures the argument; it does not run analyses.
---

# Theory & Hypotheses (commres-theory-building)

At CR a result is not a contribution until it is attached to a **testable communication mechanism**.
This skill turns an idea into theory: precise constructs, an explicit process, and **numbered
hypotheses** that the design will test. CR is a hypothetico-deductive journal — a paper that documents
an effect without a tested mechanism rarely clears the bar.

## When to trigger

- The empirics are strong but the "so what / why" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "just a main effect"
- You need to state constructs, mechanisms, and predictions explicitly before collecting data
- Connecting your work to (or extending) an established communication theory

## Build the argument (theory → mechanism → hypotheses)

1. **Concept.** Define the key constructs precisely (e.g., exposure, framing, presence, perceived
   norms); distinguish each from its near neighbors so measurement is unambiguous.
2. **Mechanism.** State the communication process: who sends/receives what, through which channel,
   with what cognitive/affective/social step that produces the outcome. This is the mediator.
3. **Boundary conditions.** Name the moderators — which audiences, messages, and contexts strengthen
   or reverse the effect. CR rewards "for whom / when," not just "whether."
4. **Hypotheses.** Translate the mechanism into **explicit, numbered hypotheses** (and research
   questions where theory is thin): H1 (effect), H2 (mediation path), H3 (moderation). These become
   the tests in `commres-research-design` and `commres-data-analysis`.

## The mediation/moderation core (CR-specific)

CR is the home of **process models** — message → mediator → outcome, conditioned by moderators. State
the **causal ordering** the model assumes and how the design licenses it: a mediator measured on the
same cross-sectional wave as the outcome cannot carry a causal-process claim (defer the temporal
warrant to design). Pre-specify the indirect-effect test; do not fit a PROCESS model post hoc and
narrate it as theory.

## The theory-contribution bar at CR (calibration anchor, hedged)

A common substantive rejection is **"theory cited but not advanced."** Citing a theory is not moving
it. Calibrate where a paper sits:

| Level | What the paper does to theory | CR verdict (typical) |
|-------|-------------------------------|----------------------|
| Applies | uses an existing framing/priming/cultivation account as-is | rarely enough alone |
| Extends | adds a moderator/boundary condition to a known effect | competitive if consequential |
| Specifies | opens a mediating process a prior account left as a black box | strong fit |
| Adjudicates | pits two mechanisms and lets the data choose | high-end contribution |

The bar is the **tested theoretical move**, not the method. A heuristic, not an editorial rule.

## Reviewer-pushback patterns and the theory-level fix

| Referee comment | Underlying gap | Fix at the argument stage |
|-----------------|----------------|---------------------------|
| "Theory cited but not advanced" | applies, does not extend | name the boundary or black box the study opens |
| "Effect without a mechanism" | no mediator | state the cognitive/affective/social step and a mediation hypothesis |
| "Why doesn't this travel?" | boundary conditions absent | specify moderators where the effect holds and breaks |
| "Construct slippage" | measured thing isn't the construct | re-anchor the definition; split from neighbors; revisit the scale |
| "HARKing suspected" | hypotheses look post hoc | preregister; present theory before results, RQs where theory is thin |

## Worked micro-example: from effect to mechanism (illustrative)

A study finds gain-framed vaccine messages raise intention more than loss-framed ones — a bare effect.
Lifted to a CR argument: framing shifts **perceived response-efficacy** (mediator, H2), which raises
intention (H1); the path is stronger for **low-prior-knowledge** audiences (moderator, H3). The
constructs are defined and distinguished from "perceived threat," the indirect effect is pre-specified
with bootstrap CIs, and the moderator gives a "for whom" — a portable, tested mechanism rather than a
re-documented framing effect.

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state hypotheses before tests; preregister
- A main effect with no mediator/moderator — CR wants the process and the boundary
- Mechanisms named but never made into a testable, numbered hypothesis
- Universal claims with no boundary conditions (which audiences? which messages? which contexts?)
- A PROCESS model whose causal ordering the design cannot support

## Output format

```
【Core claim】one sentence
【Mechanism】the communication process (the mediator)
【Constructs】defined + distinguished from neighbors
【Hypotheses】H1 (effect) / H2 (mediation) / H3 (moderation) → research-design
【Boundary conditions】which audiences / messages / contexts
【Causal-ordering warrant】how the design licenses the process claim
【Next】commres-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — measurement, SEM, and mediation/PROCESS tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — CR scope and contribution expectations
