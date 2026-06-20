---
name: jais-rebuttal
description: Use when working on rebuttal strategy for a Journal of the Association for Information Systems manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Rebuttal Strategy (jais-rebuttal)

## When to trigger
- The manuscript is aimed at **Journal of the Association for Information Systems (JAIS)** and rebuttal strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship standard.
- The paper risks being confused with nearby venues: MIS Quarterly, Information Systems Research, JMIS, and Management Science.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| sociotechnical system is central | Make the sociotechnical system assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| IS theory is central | Make the IS theory assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| digital innovation is central | Make the digital innovation assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| methodological pluralism is central | Make the methodological pluralism assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| cumulative contribution is central | Make the cumulative contribution assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JAIS fit notes

- Publisher / owner context: Association for Information Systems.
- Submission route to re-check: AIS eLibrary / journal submission.
- Signature vocabulary: sociotechnical system, IS theory, digital innovation, methodological pluralism, cumulative contribution.
- Sibling boundary: MIS Quarterly, Information Systems Research, JMIS, and Management Science.
- House-style aim: theory-forward IS research with method fit and clear community contribution.
- Official URLs currently used by the pack:
- https://aisel.aisnet.org/jais/
- https://aisel.aisnet.org/jais/policies.html

## Stage-specific moves

1. State the exact rebuttal strategy question in one sentence.
2. Identify which JAIS audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jais-rebuttal` if the stage passes, or back to `jais-workflow` if it does not.

## Checklist
- [ ] The JAIS audience can see why the paper belongs in information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship.
- [ ] The draft distinguishes JAIS from MIS Quarterly, Information Systems Research, JMIS.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for rebuttal strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to JAIS without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of the Association for Information Systems
【Skill】jais-rebuttal
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking rebuttal strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not MIS Quarterly, Information Systems Research
【Source status】verified URL / 待核实 / not asserted
【Next skill】jais-rebuttal
```
