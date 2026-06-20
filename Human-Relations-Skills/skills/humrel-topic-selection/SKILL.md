---
name: humrel-topic-selection
description: Use when deciding whether a question belongs in Human Relations (HR) and how to frame it for the journal's interdisciplinary work-and-society audience. Tests fit and sharpens the question; it does not develop the theory or invent evidence.
---

# Topic Selection (humrel-topic-selection)

## When to trigger

- You have a workplace/organizational phenomenon but are unsure it is an *HR* question rather than a sibling-journal question
- The puzzle is interesting empirically but you cannot yet say what *social-theoretical* understanding it would advance
- A coauthor asks "is this Human Relations, Organization Studies, JMS, or Work, Employment and Society?"
- The topic is timely (AI at work, platform labour, hybrid work, inequality) and you need it to be more than topical

## What makes a question an HR question

HR is the **interdisciplinary social-science journal of relationships at and around work**. Its self-description is the test: research that advances "our understanding of social relationships at and around work through theoretical development and empirical investigation." Three things travel together for a strong HR topic:

1. **The relational/social core.** The phenomenon is about people *in relation* — power, identity, meaning, conflict, control, solidarity, emotion, institutions — not a firm-level performance lever or an isolated individual trait. If the question could be answered without reference to social relations, it is probably not HR.
2. **A theoretical stake, declared early.** HR runs an editorial scoping screen and demands "a unique and substantive theoretical contribution"; "suitable data are a necessary but not sufficient feature to get to full peer review." A topic that is only descriptive or only managerial-prescriptive will not clear the screen.
3. **Interdisciplinary reach.** HR draws on sociology, psychology, organization studies, and critical theory. The best topics speak to a *conversation* readers from more than one tradition recognize.

## Sibling boundaries — where the topic should and should not go

| If the centre of gravity is… | The natural home is… | HR's distinct angle |
|------------------------------|----------------------|---------------------|
| US-style hypothesis test of an OB effect | AMJ | HR wants theory + social context, methods plural, not a moderated-mediation template |
| A debate internal to organization theory / paradigms | Organization Studies (EGOS) | HR is broader social science of work, less paradigm-internal |
| Managerial relevance / strategy / the firm | JMS | HR foregrounds the *social relation*, not managerial payoff |
| Employment, labour markets, class, work sociology | Work, Employment and Society | HR pulls the case up to *organizational/relational theory*, not labour-market description |
| A purely critical/deconstructive intervention | Organization | HR welcomes critique but rewards a constructive, generative theoretical contribution |

## How to sharpen the question

- State the phenomenon as a **puzzle or tension** ("workers say X yet do Y"), not a topic label.
- Name the **conversation** it joins and the **prior** it could unsettle (feeds `humrel-literature-positioning`).
- Identify *which* HR readers would care (organizational sociologists? critical scholars? work psychologists?) and which would desk-screen it as out of scope.
- Decide the likely archetype (ethnographic, critical, quantitative, mixed, theory) early — it sets the chain entry point in `humrel-workflow`.

## Checklist

- [ ] The question is about **social relationships at/around work**, not a firm-performance lever
- [ ] A theoretical stake is stated, not just an empirical gap or a timely topic
- [ ] The target conversation and the prior it could overturn are named
- [ ] You can say why it is HR and *not* OS / JMS / AMJ / WES / Organization
- [ ] At least one HR reader segment would find it non-obvious and important
- [ ] Process facts cited (length, review model, portal) trace to `resources/official-source-map.md` or are marked 待核实

## Anti-patterns

- A "hot topic" (AI, hybrid work) with no relational mechanism or theoretical stake
- A managerial how-to or performance-optimization question dressed as organizational research
- A descriptive case that never rises above its setting to organizational theory
- Framing so generic the journal name could be swapped without changing a word
- Treating the editorial scoping screen as a formality rather than the first real gate

## Output format

```text
【Journal】Human Relations
【Skill】humrel-topic-selection
【Verdict】fit / sharpen / reroute to sibling
【Puzzle (one sentence)】the tension, not the topic
【Relational core】how it is about relationships at/around work
【Theoretical stake】what understanding it could advance
【Sibling boundary】why HR and not OS / JMS / AMJ / WES / Organization
【Source status】verified / 待核实 / not asserted
【Next skill】humrel-theory-development
```
