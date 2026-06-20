---
name: revacc-topic-selection
description: Use when working on topic selection for a Review of Accounting Studies manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Topic Selection (revacc-topic-selection)

## When to trigger
- The manuscript is aimed at **Review of Accounting Studies (RAST)** and topic selection is the active bottleneck.
- A coauthor asks whether the draft meets the journal's analytical, empirical, and experimental accounting research with strong economics foundations standard.
- The paper risks being confused with nearby venues: The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| accounting disclosure is central | Make the accounting disclosure assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| audit quality is central | Make the audit quality assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| capital-market accounting is central | Make the capital-market accounting assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| tax and reporting is central | Make the tax and reporting assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| earnings information is central | Make the earnings information assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## RAST fit notes

- Publisher / owner context: Springer.
- Submission route to re-check: Springer Nature submission.
- Signature vocabulary: accounting disclosure, audit quality, capital-market accounting, tax and reporting, earnings information.
- Sibling boundary: The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research.
- House-style aim: accounting research that links institutional reporting detail to credible economic mechanisms.
- Official URLs currently used by the pack:
- https://link.springer.com/journal/11142
- https://www.springer.com/journal/11142/submission-guidelines

## Stage-specific moves

1. State the exact topic selection question in one sentence.
2. Identify which RAST audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `revacc-theory-development` if the stage passes, or back to `revacc-workflow` if it does not.

## Checklist
- [ ] The RAST audience can see why the paper belongs in analytical, empirical, and experimental accounting research with strong economics foundations.
- [ ] The draft distinguishes RAST from The Accounting Review, Journal of Accounting Research, Journal of Accounting.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for topic selection names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to RAST without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Review of Accounting Studies
【Skill】revacc-topic-selection
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking topic selection
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not The Accounting Review, Journal of Accounting Research
【Source status】verified URL / 待核实 / not asserted
【Next skill】revacc-theory-development
```
