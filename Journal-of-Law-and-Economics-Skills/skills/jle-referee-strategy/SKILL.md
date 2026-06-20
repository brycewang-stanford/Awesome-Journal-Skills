---
name: jle-referee-strategy
description: Use when working on referee strategy for a The Journal of Law and Economics manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Referee Strategy (jle-referee-strategy)

## When to trigger
- The manuscript is aimed at **The Journal of Law and Economics (JLE)** and referee strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions standard.
- The paper risks being confused with nearby venues: Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| legal rule variation is central | Make the legal rule variation assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| institutional doctrine is central | Make the institutional doctrine assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| contracting friction is central | Make the contracting friction assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| regulatory incidence is central | Make the regulatory incidence assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| court or statute design is central | Make the court or statute design assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JLE fit notes

- Publisher / owner context: University of Chicago Press.
- Submission route to re-check: Chicago Journals online submission.
- Signature vocabulary: legal rule variation, institutional doctrine, contracting friction, regulatory incidence, court or statute design.
- Sibling boundary: Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics.
- House-style aim: economics-first legal analysis that respects doctrine, timing, and institutional assignment.
- Official URLs currently used by the pack:
- https://www.journals.uchicago.edu/journals/jle/instruct
- https://www.journals.uchicago.edu/toc/jle/current

## Stage-specific moves

1. State the exact referee strategy question in one sentence.
2. Identify which JLE audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jle-submission` if the stage passes, or back to `jle-workflow` if it does not.

## Checklist
- [ ] The JLE audience can see why the paper belongs in law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions.
- [ ] The draft distinguishes JLE from Journal of Legal Studies, JLEO, American Law.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for referee strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JLE without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】The Journal of Law and Economics
【Skill】jle-referee-strategy
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking referee strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Legal Studies, JLEO
【Source status】verified URL / 待核实 / not asserted
【Next skill】jle-submission
```
