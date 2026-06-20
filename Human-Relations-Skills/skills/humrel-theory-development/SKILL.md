---
name: humrel-theory-development
description: Use when building the theoretical engine for a Human Relations (HR) manuscript — mechanisms grounded in social theory, process vs. variance logic, constructs, and boundary conditions. Builds the argument; it does not choose methods or run analysis.
---

# Theory Development (humrel-theory-development)

## When to trigger

- You have a work-and-society puzzle (from `humrel-topic-selection`) but no theoretical machinery to explain it
- Your "theory" is a box-and-arrow diagram with labelled constructs but no *social mechanism*
- A reviewer says the theory is "thin," "post hoc," "atheoretical," or "a relabelling of the finding"
- You borrowed a fashionable construct (resilience, agility, the algorithmic) as a veneer over an under-theorized result

## The HR standard: a substantive theoretical contribution drawing on social theory

HR's gatekeeping criterion is **"a unique and substantive theoretical contribution"** to understanding work and organizations as social phenomena. Unlike a hypothesis-confirmation register, HR rewards theory that *engages social theory* — power, identity, institutions, practice, sensemaking, emotion, discourse, the labour process — and uses it to illuminate the relational dynamics of work. The deliverable is a change in how readers across organization studies, sociology, and psychology *understand* something, not a coefficient or a managerial recommendation.

## Mechanism first, grounded in a social process

A construct is not a mechanism. State the **generative social mechanism** — the relational/organizational process that produces the pattern or sequence:

- Name the **actors** and what they are doing relationally (negotiating identity, exercising or resisting power, making sense, categorizing, controlling, caring, contesting).
- Name the **social structure** in which they act (occupation, hierarchy, field, institution, network, gender/class/race order, technological regime).
- Specify the **processual or causal logic**: why does this actor, in this structure, produce this outcome or this next move?
- Specify **boundary conditions**: where does the mechanism hold, weaken, or reverse? HR readers expect scope, not universal laws.

A good test: can a reader *predict a new, non-obvious implication* for working life from your mechanism? If not, you have a label, not a theory.

## Process theory vs. variance theory — match the form to the phenomenon

- **Process theory** explains *how and why* something unfolds over time: sequences, events, becoming, contestation, feedback. Natural for ethnographic, historical, and critical HR papers.
- **Variance theory** explains *how much* an outcome co-varies with antecedents, with moderators/mediators. Natural for survey/quantitative HR papers.

HR accommodates both, but punishes a mismatch — variance framing forced onto a processual phenomenon ("control *increased* resistance") flattens exactly the relational dynamics HR exists to study. Let the form of the theory match the form of the phenomenon (this decision feeds `humrel-methods`).

## Critical and reflexive theorizing

HR's Tavistock lineage makes critical theorizing first-class: theory that problematizes power, ideology, and taken-for-granted arrangements is welcome — but it must be **generative as well as deconstructive**. A critique that only unmasks, without offering a new way to understand or a constructive reframing, reads as polemic. Pair the critical move with a positive theoretical claim that other scholars can build on.

## Inductive vs. deductive

- **Inductive/grounded:** theory is the *output*, presented after the data structure (see `humrel-data-analysis`). A grounded process model can be the *entire* HR contribution. Avoid "theory by adjective" (calling a pattern "dynamic" without specifying the process).
- **Deductive:** hypotheses must be *derived* with an explicit causal-logic paragraph each, tied to one core mechanism — not a bag of hypotheses. Moderators must be theoretically motivated, not data-mined.

## Checklist

- [ ] A named generative social mechanism (actors + structure + logic), not just constructs
- [ ] Theory engages a recognizable social-theoretical conversation, not a borrowed buzzword
- [ ] Process vs. variance form matches the phenomenon
- [ ] Boundary conditions stated (where it holds / weakens / reverses)
- [ ] Mechanism yields at least one non-obvious implication for working life
- [ ] Critical papers are generative, not only deconstructive
- [ ] Deductive: each hypothesis derived from the core mechanism; inductive: a process model planned

## Anti-patterns

- Box-and-arrow models with no mechanism ("constructs in search of a story")
- Variance framing imposed on a processual/relational phenomenon
- A fashionable construct used as a veneer over a thin finding
- Critique that only unmasks, with no constructive theoretical payoff
- "Theory by adjective"; hypotheses asserted rather than derived; a moderator zoo

## Output format

```text
【Journal】Human Relations
【Skill】humrel-theory-development
【Theory form】process / variance + why it matches the phenomenon
【Core mechanism】actors + social structure + processual/causal logic
【Social-theory anchor】the conversation it engages (power/identity/institutions/…)
【Boundary conditions】where it holds / weakens / reverses
【Non-obvious implication】the surprise for working life
【Next skill】humrel-literature-positioning
```
