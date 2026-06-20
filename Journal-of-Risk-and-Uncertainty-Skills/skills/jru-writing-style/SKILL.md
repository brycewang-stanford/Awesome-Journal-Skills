---
name: jru-writing-style
description: Use when working on writing style for a Journal of Risk and Uncertainty manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Writing Style (jru-writing-style)

## When to trigger
- The manuscript is aimed at **Journal of Risk and Uncertainty (JRU)** and writing style is the active bottleneck.
- A coauthor asks whether the draft meets the journal's risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions standard.
- The paper risks being confused with nearby venues: Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| risk preference is central | Make the risk preference assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| uncertainty attitude is central | Make the uncertainty attitude assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| prospect-theory test is central | Make the prospect-theory test assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| insurance behavior is central | Make the insurance behavior assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| experimental elicitation is central | Make the experimental elicitation assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JRU fit notes

- Publisher / owner context: Springer.
- Submission route to re-check: Springer Nature submission.
- Signature vocabulary: risk preference, uncertainty attitude, prospect-theory test, insurance behavior, experimental elicitation.
- Sibling boundary: Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science.
- House-style aim: decision-theoretic clarity with careful measurement of risk and uncertainty.
- Official URLs currently used by the pack:
- https://link.springer.com/journal/11166
- https://www.springer.com/journal/11166/submission-guidelines

## Stage-specific moves

1. State the exact writing style question in one sentence.
2. Identify which JRU audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jru-replication-package` if the stage passes, or back to `jru-workflow` if it does not.

## Checklist
- [ ] The JRU audience can see why the paper belongs in risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions.
- [ ] The draft distinguishes JRU from Experimental Economics, Journal of Economic Behavior, Organization.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for writing style names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JRU without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-writing-style
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking writing style
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Experimental Economics, Journal of Economic Behavior
【Source status】verified URL / 待核实 / not asserted
【Next skill】jru-replication-package
```
