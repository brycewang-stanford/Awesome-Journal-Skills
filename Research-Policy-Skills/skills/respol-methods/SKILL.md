---
name: respol-methods
description: Use when working on methods for a Research Policy manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Methods (respol-methods)

## When to trigger
- The manuscript is aimed at **Research Policy (Research Policy)** and methods is the active bottleneck.
- A coauthor asks whether the draft meets the journal's innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production standard.
- The paper risks being confused with nearby venues: Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| innovation system is central | Make the innovation system assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| science policy is central | Make the science policy assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| patent evidence is central | Make the patent evidence assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| R&D organization is central | Make the R&D organization assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| technology diffusion is central | Make the technology diffusion assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## Research Policy fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: innovation system, science policy, patent evidence, R&D organization, technology diffusion.
- Sibling boundary: Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing.
- House-style aim: innovation-policy argument linking mechanisms, institutions, and technology evidence.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/research-policy
- https://www.elsevier.com/journals/research-policy/0048-7333/guide-for-authors

## Stage-specific moves

1. State the exact methods question in one sentence.
2. Identify which Research Policy audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `respol-data-analysis` if the stage passes, or back to `respol-workflow` if it does not.

## Checklist
- [ ] The Research Policy audience can see why the paper belongs in innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production.
- [ ] The draft distinguishes Research Policy from Strategic Management Journal, Management Science, Industrial.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for methods names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to Research Policy without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Research Policy
【Skill】respol-methods
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking methods
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Strategic Management Journal, Management Science
【Source status】verified URL / 待核实 / not asserted
【Next skill】respol-data-analysis
```
