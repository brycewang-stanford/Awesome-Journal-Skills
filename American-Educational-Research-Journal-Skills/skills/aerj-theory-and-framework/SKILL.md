---
name: aerj-theory-and-framework
description: Use when building the conceptual or theoretical framework for an American Educational Research Journal (AERJ) manuscript. AERJ expects a clear framework that frames the question, guides the design and analysis, and elevates a result into a contribution to understanding. Strengthens the framework; it does not invent theory.
---

# Theory & Conceptual Framework (aerj-theory-and-framework)

AERJ rewards work that is **theoretically grounded** — a framework that frames the question, justifies
the design, and gives the findings meaning for the field. A strong result without a frame reads as a
report, not a contribution. The frame can be a formal theory, a conceptual model, or an interpretive
lens, depending on your methodological tradition and dominant education-research lens.

## When to trigger

- Articulating the conceptual / theoretical framework section
- A reviewer said the paper is "under-theorized" or "atheoretical"
- Connecting constructs to measures (quant) or to coding/interpretation (qual)
- Stating the propositions, hypotheses, or guiding questions the study tests or explores

## How to build the framework

1. **Name the frame and its provenance.** Whose theory or which conceptual tradition (learning theory,
   organizational theory, sociocultural, critical/equity frameworks, development, etc.)? Cite its
   strongest statement, not a textbook gloss.
2. **Make it do work.** The framework should generate the questions/propositions, motivate the design
   choices, and shape what counts as evidence — not sit decoratively in section 2.
3. **Define constructs operationally.** For quantitative work, tie each construct to a measure/indicator
   (hand off to `aerj-data-analysis`). For qualitative work, tie constructs to what you will look for and
   how you will interpret it.
4. **State the contribution to understanding.** Are you extending, testing, complicating, or
   integrating a framework? Be explicit; AERJ values conceptual advance.
5. **Attend to equity and context.** Where relevant, the frame should make explicit assumptions about
   who, where, and under what conditions the claim holds.

## The framework-does-work test

For each major design or analysis choice, write: *"We do this **because** the framework implies ___."*
If a choice has no such line, either the choice or the framework is underspecified.

## Anti-patterns

- A "theory" section that never reappears in design, analysis, or discussion
- Borrowing a framework as decoration while the analysis runs on intuition
- Hypotheses with no derivation from the frame; or qual coding with no conceptual anchor
- Over-claiming a grand theory from a single bounded study
- Ignoring context/equity assumptions the framework actually carries

## Framework expectations by tradition (AERJ referees)

AERJ rewards conceptual advance, but what a "framework doing work" looks like differs by method and
dominant education-research lens. Calibrate yours against the row that fits your study.

| Tradition / lens | Frame should generate | Under-theorized tell a referee flags |
|---------------------|-----------------------|--------------------------------------|
| Quantitative, teaching/learning lens | Hypotheses and construct-to-measure links | Hypotheses with no derivation from the frame |
| Quantitative, policy/institutional lens | Mechanisms the policy/organizational design tests | A frame cited once, then never revisited |
| Qualitative | Sensitizing concepts guiding what to look for | "Lens" named but coding runs on intuition |
| Mixed | Why integration is theoretically motivated | Two strands with two unrelated frames |

## Worked framework vignette (illustrative)

An integrated-AERJ study of a **school-funding equalization reform** invokes an organizational-resource
framework. To make it do work, the authors derive that equalization should compress *between-school*
variance in instructional spending more than *within-school* variance — a testable implication. Their
multilevel design then reports an illustrative drop in between-school spending variance from **0.30 to
0.18** after the reform. Because the framework generated that specific prediction, the result reads as
a conceptual advance about how institutions absorb funding shocks, not a descriptive spending tally.
Each design choice carries a "we do this *because* the framework implies ___" line.

## Referee pushback and the venue fix

- *"The paper is atheoretical / under-theorized."* → Show the frame generating the questions and
  shaping what counts as evidence, not sitting decoratively in section 2.
- *"You over-claim a grand theory."* → Scope the contribution to extend/test/complicate, and state the
  conditions under which the claim holds.
- *"Constructs aren't operationalized."* → Tie each construct to a measure (quant) or to an observable
  (qual); confirm framing expectations against the journal's current submission guidelines.

## Output format

```
【Framework】name + provenance (key citation)
【Constructs】defined + linked to measures (quant) or to interpretation (qual)
【Propositions/Questions】derived from the frame
【Contribution】extend / test / complicate / integrate
【Does-work check】each design choice tied to the frame? [Y/N]
【Next】aerj-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — measurement/SEM and qualitative coding tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AERJ scope and reporting-standards expectations
