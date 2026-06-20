---
name: amann-review-process
description: Use when working on review process for a Academy of Management Annals manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Review Process (amann-review-process)

## When to trigger
- The manuscript is aimed at **Academy of Management Annals (Annals)** and review process is the active bottleneck.
- A coauthor asks whether the draft meets the journal's commissioned and high-level reviews that synthesize management and organization research standard.
- The paper risks being confused with nearby venues: Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| integrative review is central | Make the integrative review assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| theory synthesis is central | Make the theory synthesis assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| agenda setting is central | Make the agenda setting assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| management field map is central | Make the management field map assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| conceptual reconciliation is central | Make the conceptual reconciliation assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## Annals fit notes

- Publisher / owner context: Academy of Management / Taylor & Francis.
- Submission route to re-check: Academy of Management submission.
- Signature vocabulary: integrative review, theory synthesis, agenda setting, management field map, conceptual reconciliation.
- Sibling boundary: Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets.
- House-style aim: field-defining synthesis that reorganizes theory rather than merely cataloging papers.
- Official URLs currently used by the pack:
- https://journals.aom.org/journal/annals
- https://aom.org/research/publishing-with-aom/author-resources

## Stage-specific moves

1. State the exact review process question in one sentence.
2. Identify which Annals audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `amann-revision` if the stage passes, or back to `amann-workflow` if it does not.

## Checklist
- [ ] The Annals audience can see why the paper belongs in commissioned and high-level reviews that synthesize management and organization research.
- [ ] The draft distinguishes Annals from Academy of Management Review, Journal of Management, Journal of Management Studies.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for review process names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] The review explains inclusion/exclusion logic and how competing schools are balanced.
- [ ] The synthesis produces an agenda, taxonomy, or framework rather than a bibliography.

## Anti-patterns
- Submitting a paper that is merely adjacent to Annals without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Academy of Management Annals
【Skill】amann-review-process
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking review process
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Academy of Management Review, Journal of Management
【Source status】verified URL / 待核实 / not asserted
【Next skill】amann-revision
```
