---
name: jeem-identification
description: Use when working on identification strategy for a Journal of Environmental Economics and Management manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Identification Strategy (jeem-identification)

## When to trigger
- The manuscript is aimed at **Journal of Environmental Economics and Management (JEEM)** and identification strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management standard.
- The paper risks being confused with nearby venues: Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| environmental externality is central | Make the environmental externality assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| regulatory design is central | Make the regulatory design assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| valuation evidence is central | Make the valuation evidence assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| climate adaptation is central | Make the climate adaptation assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| resource management is central | Make the resource management assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JEEM fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: environmental externality, regulatory design, valuation evidence, climate adaptation, resource management.
- Sibling boundary: Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change.
- House-style aim: economic identification linked to environmental mechanisms and policy welfare.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-environmental-economics-and-management
- https://www.elsevier.com/journals/journal-of-environmental-economics-and-management/0095-0696/guide-for-authors

## Stage-specific moves

1. State the exact identification strategy question in one sentence.
2. Identify which JEEM audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jeem-theory-model` if the stage passes, or back to `jeem-workflow` if it does not.

## Checklist
- [ ] The JEEM audience can see why the paper belongs in environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management.
- [ ] The draft distinguishes JEEM from Review of Environmental Economics, Policy, AEJ Economic Policy.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for identification strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JEEM without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-identification
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking identification strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Review of Environmental Economics, Policy
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-theory-model
```
