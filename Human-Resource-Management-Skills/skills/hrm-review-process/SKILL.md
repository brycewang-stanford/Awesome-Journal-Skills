---
name: hrm-review-process
description: Use when working on review process for a Human Resource Management manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Review Process (hrm-review-process)

## When to trigger
- The manuscript is aimed at **Human Resource Management (HRM)** and review process is the active bottleneck.
- A coauthor asks whether the draft meets the journal's human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy standard.
- The paper risks being confused with nearby venues: Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| HR system is central | Make the HR system assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| talent architecture is central | Make the talent architecture assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| employment relation is central | Make the employment relation assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| workforce analytics is central | Make the workforce analytics assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| strategic HR is central | Make the strategic HR assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## HRM fit notes

- Publisher / owner context: Wiley.
- Submission route to re-check: Wiley online submission.
- Signature vocabulary: HR system, talent architecture, employment relation, workforce analytics, strategic HR.
- Sibling boundary: Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal.
- House-style aim: HR scholarship that connects people practices to organizational mechanisms and outcomes.
- Official URLs currently used by the pack:
- https://onlinelibrary.wiley.com/journal/1099050x
- https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html

## Stage-specific moves

1. State the exact review process question in one sentence.
2. Identify which HRM audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `hrm-rebuttal` if the stage passes, or back to `hrm-workflow` if it does not.

## Checklist
- [ ] The HRM audience can see why the paper belongs in human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy.
- [ ] The draft distinguishes HRM from Personnel Psychology, Journal of Management, Human Relations.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for review process names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to HRM without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Human Resource Management
【Skill】hrm-review-process
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking review process
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Personnel Psychology, Journal of Management
【Source status】verified URL / 待核实 / not asserted
【Next skill】hrm-rebuttal
```
