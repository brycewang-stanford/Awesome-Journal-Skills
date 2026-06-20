---
name: expecon-replication-package
description: Use when working on replication package for a Experimental Economics manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Replication Package (expecon-replication-package)

## When to trigger
- The manuscript is aimed at **Experimental Economics (Experimental Economics)** and replication package is the active bottleneck.
- A coauthor asks whether the draft meets the journal's laboratory, field, online, and artefactual experiments in economics standard.
- The paper risks being confused with nearby venues: JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| experimental protocol is central | Make the experimental protocol assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| incentive compatibility is central | Make the incentive compatibility assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| pre-analysis plan is central | Make the pre-analysis plan assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| treatment contrast is central | Make the treatment contrast assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| subject-pool design is central | Make the subject-pool design assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## Experimental Economics fit notes

- Publisher / owner context: Springer for the Economic Science Association.
- Submission route to re-check: Springer Nature submission.
- Signature vocabulary: experimental protocol, incentive compatibility, pre-analysis plan, treatment contrast, subject-pool design.
- Sibling boundary: JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty.
- House-style aim: protocol-transparent experimental economics with credible incentives and robust inference.
- Official URLs currently used by the pack:
- https://link.springer.com/journal/10683
- https://www.springer.com/journal/10683/submission-guidelines

## Stage-specific moves

1. State the exact replication package question in one sentence.
2. Identify which Experimental Economics audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `expecon-referee-strategy` if the stage passes, or back to `expecon-workflow` if it does not.

## Checklist
- [ ] The Experimental Economics audience can see why the paper belongs in laboratory, field, online, and artefactual experiments in economics.
- [ ] The draft distinguishes Experimental Economics from JEBO, Games, Economic Behavior.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for replication package names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to Experimental Economics without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Experimental Economics
【Skill】expecon-replication-package
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking replication package
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not JEBO, Games
【Source status】verified URL / 待核实 / not asserted
【Next skill】expecon-referee-strategy
```
