---
name: arecon-evidence-standards
description: Use when working on evidence standards for a Annual Review of Economics manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Evidence Standards (arecon-evidence-standards)

## When to trigger
- The manuscript is aimed at **Annual Review of Economics (AREcon)** and evidence standards is the active bottleneck.
- A coauthor asks whether the draft meets the journal's commissioned review articles synthesizing major areas of economics for specialists and adjacent economists standard.
- The paper risks being confused with nearby venues: Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| field synthesis is central | Make the field synthesis assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| research frontier is central | Make the research frontier assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| conceptual map is central | Make the conceptual map assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| evidence stocktake is central | Make the evidence stocktake assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| future agenda is central | Make the future agenda assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## AREcon fit notes

- Publisher / owner context: Annual Reviews.
- Submission route to re-check: Annual Reviews editorial process.
- Signature vocabulary: field synthesis, research frontier, conceptual map, evidence stocktake, future agenda.
- Sibling boundary: Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals.
- House-style aim: agenda-setting synthesis that clarifies what the field knows, disputes, and should do next.
- Official URLs currently used by the pack:
- https://www.annualreviews.org/journal/economics
- https://www.annualreviews.org/page/authors/general-information

## Stage-specific moves

1. State the exact evidence standards question in one sentence.
2. Identify which AREcon audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `arecon-tables-figures` if the stage passes, or back to `arecon-workflow` if it does not.

## Checklist
- [ ] The AREcon audience can see why the paper belongs in commissioned review articles synthesizing major areas of economics for specialists and adjacent economists.
- [ ] The draft distinguishes AREcon from Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for evidence standards names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] The review explains inclusion/exclusion logic and how competing schools are balanced.
- [ ] The synthesis produces an agenda, taxonomy, or framework rather than a bibliography.

## Anti-patterns
- Submitting a paper that is merely adjacent to AREcon without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Annual Review of Economics
【Skill】arecon-evidence-standards
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking evidence standards
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Economic Literature, Journal of Economic Perspectives
【Source status】verified URL / 待核实 / not asserted
【Next skill】arecon-tables-figures
```
