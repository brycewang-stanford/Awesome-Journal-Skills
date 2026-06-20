---
name: jebo-referee-strategy
description: Use when working on referee strategy for a Journal of Economic Behavior and Organization manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Referee Strategy (jebo-referee-strategy)

## When to trigger
- The manuscript is aimed at **Journal of Economic Behavior and Organization (JEBO)** and referee strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings standard.
- The paper risks being confused with nearby venues: Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| behavioral mechanism is central | Make the behavioral mechanism assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| institutional setting is central | Make the institutional setting assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| laboratory evidence is central | Make the laboratory evidence assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| field-experiment design is central | Make the field-experiment design assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| organizational incentives is central | Make the organizational incentives assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JEBO fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: behavioral mechanism, institutional setting, laboratory evidence, field-experiment design, organizational incentives.
- Sibling boundary: Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics.
- House-style aim: mechanism-forward behavioral evidence with transparent experimental or institutional design.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-economic-behavior-and-organization
- https://www.elsevier.com/journals/journal-of-economic-behavior-and-organization/0167-2681/guide-for-authors

## Stage-specific moves

1. State the exact referee strategy question in one sentence.
2. Identify which JEBO audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jebo-submission` if the stage passes, or back to `jebo-workflow` if it does not.

## Checklist
- [ ] The JEBO audience can see why the paper belongs in behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings.
- [ ] The draft distinguishes JEBO from Experimental Economics, Games, Economic Behavior.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for referee strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JEBO without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Economic Behavior and Organization
【Skill】jebo-referee-strategy
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking referee strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Experimental Economics, Games
【Source status】verified URL / 待核实 / not asserted
【Next skill】jebo-submission
```
