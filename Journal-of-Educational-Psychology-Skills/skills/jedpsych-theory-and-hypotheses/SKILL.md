---
name: jedpsych-theory-and-hypotheses
description: Use when stating the learning/motivation theory and hypotheses for a Journal of Educational Psychology manuscript. JEP expects a clear psychological mechanism, directional hypotheses tied to that theory, and an honest separation of confirmatory (ideally preregistered) from exploratory analyses. Structures the argument; it does not run analyses.
---

# Theory & Hypotheses (jedpsych-theory-and-hypotheses)

The Journal of Educational Psychology rewards a **clear psychological mechanism** for an educational
phenomenon and **honest hypothesis status**. Because JEP is a research journal in *educational
psychology*, the theory must explain learning, motivation, engagement, or achievement — not merely
report that an intervention worked. The cardinal rule mirrors the credibility era: **state theory and
confirmatory hypotheses before the data**, and label exploratory results as exploratory.

## When to trigger

- Writing the theoretical framing and hypotheses
- Preparing a preregistration / pre-analysis plan for a field trial or longitudinal study
- Reconciling what theory predicted with what you found
- A reviewer flagged the work as "atheoretical," "post hoc," "HARKed," or "just an evaluation"

## Build the argument

1. **Name the learning mechanism.** What cognitive, motivational, or self-regulatory process predicts
   the effect, and why it should operate in this educational setting. JEP wants the *psychology* of why
   the instruction, condition, or trajectory changes learning.
2. **Derive directional hypotheses.** Translate the theory into specific, testable predictions (direction
   and, where possible, an educationally meaningful magnitude — not just "an effect").
3. **Mark hypothesis status.** Separate **confirmatory** (predicted in advance, ideally preregistered)
   from **exploratory** (generated after seeing data) analyses, clearly, in the text. Preregistration is
   encouraged at JEP; report whether and where you preregistered.
4. **Specify what would disconfirm.** Say which results would count against the mechanism; this is what
   makes a test credible at a post-credibility-revolution venue.
5. **Tie theory to nesting where relevant.** If the mechanism operates at the classroom or school level
   (e.g., a climate or instruction effect), say so — it dictates the design (see `jedpsych-study-design`).

## Avoiding HARKing and the "it worked" trap

- Do not present an exploratory finding as if it were predicted; if you discovered it post hoc, say so and
  frame it as a hypothesis for future confirmation.
- Do not let "the program raised scores" stand in for theory. JEP asks *why* — through which learning or
  motivational process — so a result without a mechanism reads as evaluation, not educational psychology.

## Worked micro-example — theory to hypothesis status (illustrative)

A reading-comprehension strategy-instruction field trial, written so hypothesis status is legible.

```
Theory:  Explicit strategy instruction builds metacognitive monitoring,
         which lets readers allocate effort to comprehension breakdowns,
         improving inference on novel texts.
H1 (confirmatory, preregistered):
         Strategy-instruction classrooms outperform business-as-usual on a
         transfer comprehension task (directional; classroom-level effect).
H2 (confirmatory, preregistered): The effect is mediated by gains in a
         metacognitive-monitoring measure (mechanism test).
H3 (exploratory): Larger gains for initially low-comprehension students
         (aptitude-treatment interaction; flagged for future confirmation).
Disconfirming: a near-zero classroom-level effect, or no monitoring gain,
         counts against the metacognitive account — stated up front.
```

## Constraints-on-generality (a venue expectation)

Name the boundary of the claim rather than implying universal scope across grades, subjects, and
contexts. Confirm current wording against the journal's submission guidelines, but include the substance:

```
Constraints on generality: We expect H1 to hold for upper-elementary
readers in general-education classrooms with the studied text genre. We do
not claim it generalizes to early decoding, to multilingual learners
without adaptation, or to fully online instruction without further test.
```

## Theory-stage reviewer pushback and the venue fix

| Reviewer pushback | JEP fix |
|-------------------|---------|
| "Atheoretical — reads as program evaluation" | state the learning/motivation mechanism and a mediation test, not just outcome means |
| "This looks HARKed" | show the preregistration / analysis plan timestamp; relabel post hoc analyses exploratory |
| "Mechanism untested" | add the mediator measure and a preregistered mediation hypothesis |
| "Claims outrun the sample" | scope hypotheses to the grades/subjects/settings studied; add a constraints clause |
| "Non-directional hypothesis" | commit to a sign and an educationally meaningful magnitude |

## Theory calibration anchors

- The mechanism sentence is what separates educational *psychology* from evaluation: one crisp claim about
  the cognitive or motivational process, then a derived, directional prediction and a way to test it.
- The honesty rule is temporal: anything specified *before* data is confirmatory; anything generated
  *after* seeing data is exploratory, full stop — and JEP's Transparency and Openness regime makes the
  distinction visible to editors and reviewers.
- Stating what would *disconfirm* the mechanism is what converts a story into a test; an unfalsifiable
  framing reads as a red flag.
- When the mechanism lives at the classroom/school level, the hypotheses must be stated at that level, or
  the design and analysis will not match the claim.

## Anti-patterns

- "The intervention worked" with no psychological mechanism (evaluation, not educational psychology)
- Theory written to fit the result after the fact (HARKing)
- Vague, non-directional "we expect a relationship" hypotheses
- No statement of what would disconfirm the theory
- A mechanism stated at the individual level for a classroom-level treatment

## Output format

```
【Mechanism】the learning/motivation process, briefly
【Hypotheses】directional, testable (H1, H2, …), with a mediation/mechanism test
【Status】which are confirmatory (preregistered?) vs exploratory
【Disconfirming evidence】what would count against the mechanism
【Level】individual vs classroom/school — matched to the claim
【Next】jedpsych-literature-positioning
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration templates and analysis-plan tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and JARS reporting standards
