---
name: jue-tables-figures
description: Use when working on tables and figures for a Journal of Urban Economics manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Tables and Figures (jue-tables-figures)

## When to trigger
- The manuscript is aimed at **Journal of Urban Economics (JUE)** and tables and figures is the active bottleneck.
- A coauthor asks whether the draft meets the journal's urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting standard.
- The paper risks being confused with nearby venues: Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| spatial equilibrium is central | Make the spatial equilibrium assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| housing supply is central | Make the housing supply assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| commuting margin is central | Make the commuting margin assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| local public goods is central | Make the local public goods assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| neighborhood sorting is central | Make the neighborhood sorting assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JUE fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: spatial equilibrium, housing supply, commuting margin, local public goods, neighborhood sorting.
- Sibling boundary: Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied.
- House-style aim: spatially grounded evidence with clear maps, mechanisms, and equilibrium caveats.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-urban-economics
- https://www.elsevier.com/journals/journal-of-urban-economics/0094-1190/guide-for-authors

## Stage-specific moves

1. State the exact tables and figures question in one sentence.
2. Identify which JUE audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jue-writing-style` if the stage passes, or back to `jue-workflow` if it does not.

## Checklist
- [ ] The JUE audience can see why the paper belongs in urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting.
- [ ] The draft distinguishes JUE from Journal of Public Economics, Journal of Economic Geography, Regional Science.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for tables and figures names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JUE without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Urban Economics
【Skill】jue-tables-figures
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking tables and figures
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Public Economics, Journal of Economic Geography
【Source status】verified URL / 待核实 / not asserted
【Next skill】jue-writing-style
```
