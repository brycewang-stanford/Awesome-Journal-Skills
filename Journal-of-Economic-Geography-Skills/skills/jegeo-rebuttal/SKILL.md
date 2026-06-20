---
name: jegeo-rebuttal
description: Use when working on rebuttal strategy for a Journal of Economic Geography manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Rebuttal Strategy (jegeo-rebuttal)

## When to trigger
- The manuscript is aimed at **Journal of Economic Geography (JEG)** and rebuttal strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy standard.
- The paper risks being confused with nearby venues: Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| spatial clustering is central | Make the spatial clustering assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| regional divergence is central | Make the regional divergence assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| place-based policy is central | Make the place-based policy assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| network geography is central | Make the network geography assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| innovation ecosystem is central | Make the innovation ecosystem assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JEG fit notes

- Publisher / owner context: Oxford University Press.
- Submission route to re-check: OUP / ScholarOne submission.
- Signature vocabulary: spatial clustering, regional divergence, place-based policy, network geography, innovation ecosystem.
- Sibling boundary: Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics.
- House-style aim: spatial economic argument that combines maps, mechanisms, and regional theory.
- Official URLs currently used by the pack:
- https://academic.oup.com/joeg
- https://academic.oup.com/joeg/pages/General_Instructions

## Stage-specific moves

1. State the exact rebuttal strategy question in one sentence.
2. Identify which JEG audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jegeo-rebuttal` if the stage passes, or back to `jegeo-workflow` if it does not.

## Checklist
- [ ] The JEG audience can see why the paper belongs in economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy.
- [ ] The draft distinguishes JEG from Journal of Urban Economics, Regional Studies, Economic Geography.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for rebuttal strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JEG without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-rebuttal
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking rebuttal strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Urban Economics, Regional Studies
【Source status】verified URL / 待核实 / not asserted
【Next skill】jegeo-rebuttal
```
