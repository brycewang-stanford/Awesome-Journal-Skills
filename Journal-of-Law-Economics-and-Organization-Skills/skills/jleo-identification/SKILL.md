---
name: jleo-identification
description: Use when working on identification strategy for a Journal of Law, Economics, and Organization manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Identification Strategy (jleo-identification)

## When to trigger
- The manuscript is aimed at **Journal of Law, Economics, and Organization (JLEO)** and identification strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design standard.
- The paper risks being confused with nearby venues: Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| organizational governance is central | Make the organizational governance assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| contracting institution is central | Make the contracting institution assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| legal-economic mechanism is central | Make the legal-economic mechanism assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| agency problem is central | Make the agency problem assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| institutional design is central | Make the institutional design assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JLEO fit notes

- Publisher / owner context: Oxford University Press.
- Submission route to re-check: OUP submission.
- Signature vocabulary: organizational governance, contracting institution, legal-economic mechanism, agency problem, institutional design.
- Sibling boundary: Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review.
- House-style aim: institutional-economics argument that integrates legal rules, governance, and organizational mechanisms.
- Official URLs currently used by the pack:
- https://academic.oup.com/jleo
- https://academic.oup.com/jleo/pages/General_Instructions

## Stage-specific moves

1. State the exact identification strategy question in one sentence.
2. Identify which JLEO audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jleo-theory-model` if the stage passes, or back to `jleo-workflow` if it does not.

## Checklist
- [ ] The JLEO audience can see why the paper belongs in law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design.
- [ ] The draft distinguishes JLEO from Journal of Law, Economics, Journal of Legal Studies.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for identification strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JLEO without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Law, Economics, and Organization
【Skill】jleo-identification
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking identification strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Law, Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jleo-theory-model
```
