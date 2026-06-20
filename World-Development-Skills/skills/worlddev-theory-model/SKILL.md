---
name: worlddev-theory-model
description: Use when working on theory and model craft for a World Development manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Theory and Model Craft (worlddev-theory-model)

## When to trigger
- The manuscript is aimed at **World Development (World Development)** and theory and model craft is the active bottleneck.
- A coauthor asks whether the draft meets the journal's development studies and development economics across poverty, institutions, sustainability, and policy implementation standard.
- The paper risks being confused with nearby venues: Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| development intervention is central | Make the development intervention assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| local institution is central | Make the local institution assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| poverty mechanism is central | Make the poverty mechanism assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| implementation constraint is central | Make the implementation constraint assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| global-south relevance is central | Make the global-south relevance assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## World Development fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: development intervention, local institution, poverty mechanism, implementation constraint, global-south relevance.
- Sibling boundary: Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives.
- House-style aim: development evidence that connects identification to implementation, equity, and institutions.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/world-development
- https://www.elsevier.com/journals/world-development/0305-750X/guide-for-authors

## Stage-specific moves

1. State the exact theory and model craft question in one sentence.
2. Identify which World Development audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `worlddev-robustness` if the stage passes, or back to `worlddev-workflow` if it does not.

## Checklist
- [ ] The World Development audience can see why the paper belongs in development studies and development economics across poverty, institutions, sustainability, and policy implementation.
- [ ] The draft distinguishes World Development from Journal of Development Economics, World Bank Economic Review, Economic Development.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for theory and model craft names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to World Development without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】World Development
【Skill】worlddev-theory-model
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking theory and model craft
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Development Economics, World Bank Economic Review
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-robustness
```
