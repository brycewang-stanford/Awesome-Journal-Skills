---
name: jmis-rebuttal
description: Use when working on rebuttal strategy for a Journal of Management Information Systems manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Rebuttal Strategy (jmis-rebuttal)

## When to trigger
- The manuscript is aimed at **Journal of Management Information Systems (JMIS)** and rebuttal strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology standard.
- The paper risks being confused with nearby venues: MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| digital platform is central | Make the digital platform assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| IT governance is central | Make the IT governance assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| analytics adoption is central | Make the analytics adoption assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| information systems theory is central | Make the information systems theory assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| organizational technology is central | Make the organizational technology assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JMIS fit notes

- Publisher / owner context: Taylor & Francis.
- Submission route to re-check: Taylor & Francis submission.
- Signature vocabulary: digital platform, IT governance, analytics adoption, information systems theory, organizational technology.
- Sibling boundary: MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science.
- House-style aim: IS scholarship that connects technology mechanisms to organizational and managerial outcomes.
- Official URLs currently used by the pack:
- https://www.tandfonline.com/journals/mmis20
- https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=mmis20

## Stage-specific moves

1. State the exact rebuttal strategy question in one sentence.
2. Identify which JMIS audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jmis-rebuttal` if the stage passes, or back to `jmis-workflow` if it does not.

## Checklist
- [ ] The JMIS audience can see why the paper belongs in information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology.
- [ ] The draft distinguishes JMIS from MIS Quarterly, Information Systems Research, Journal of the AIS.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for rebuttal strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to JMIS without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Management Information Systems
【Skill】jmis-rebuttal
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking rebuttal strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not MIS Quarterly, Information Systems Research
【Source status】verified URL / 待核实 / not asserted
【Next skill】jmis-rebuttal
```
