---
name: ijoc-literature-positioning
description: Use when working on literature positioning for a INFORMS Journal on Computing manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Literature Positioning (ijoc-literature-positioning)

## When to trigger
- The manuscript is aimed at **INFORMS Journal on Computing (IJOC)** and literature positioning is the active bottleneck.
- A coauthor asks whether the draft meets the journal's operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems standard.
- The paper risks being confused with nearby venues: Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| algorithmic contribution is central | Make the algorithmic contribution assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| computational experiment is central | Make the computational experiment assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| optimization benchmark is central | Make the optimization benchmark assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| reproducible code is central | Make the reproducible code assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| decision analytics is central | Make the decision analytics assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## IJOC fit notes

- Publisher / owner context: INFORMS.
- Submission route to re-check: INFORMS / ScholarOne submission.
- Signature vocabulary: algorithmic contribution, computational experiment, optimization benchmark, reproducible code, decision analytics.
- Sibling boundary: Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues.
- House-style aim: computational OR contribution with transparent algorithms, benchmarks, and reproducibility.
- Official URLs currently used by the pack:
- https://pubsonline.informs.org/journal/ijoc
- https://pubsonline.informs.org/page/ijoc/submission-guidelines

## Stage-specific moves

1. State the exact literature positioning question in one sentence.
2. Identify which IJOC audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `ijoc-methods` if the stage passes, or back to `ijoc-workflow` if it does not.

## Checklist
- [ ] The IJOC audience can see why the paper belongs in operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems.
- [ ] The draft distinguishes IJOC from Operations Research, Management Science, Manufacturing & Service Operations Management.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for literature positioning names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to IJOC without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-literature-positioning
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking literature positioning
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Operations Research, Management Science
【Source status】verified URL / 待核实 / not asserted
【Next skill】ijoc-methods
```
