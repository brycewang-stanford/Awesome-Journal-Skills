---
name: jmgmt-contribution-framing
description: Use when working on contribution framing for a Journal of Management manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Contribution Framing (jmgmt-contribution-framing)

## When to trigger
- The manuscript is aimed at **Journal of Management (JOMgmt)** and contribution framing is the active bottleneck.
- A coauthor asks whether the draft meets the journal's management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods standard.
- The paper risks being confused with nearby venues: Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| management theory contribution is central | Make the management theory contribution assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| multi-study design is central | Make the multi-study design assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| construct validity is central | Make the construct validity assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| organizational mechanism is central | Make the organizational mechanism assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| boundary conditions is central | Make the boundary conditions assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JOMgmt fit notes

- Publisher / owner context: SAGE for the Southern Management Association.
- Submission route to re-check: SAGE / ScholarOne submission.
- Signature vocabulary: management theory contribution, multi-study design, construct validity, organizational mechanism, boundary conditions.
- Sibling boundary: Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies.
- House-style aim: theory-driven management research with clean construct logic and robust empirical design.
- Official URLs currently used by the pack:
- https://journals.sagepub.com/home/jom
- https://journals.sagepub.com/author-instructions/JOM

## Stage-specific moves

1. State the exact contribution framing question in one sentence.
2. Identify which JOMgmt audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jmgmt-tables-figures` if the stage passes, or back to `jmgmt-workflow` if it does not.

## Checklist
- [ ] The JOMgmt audience can see why the paper belongs in management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods.
- [ ] The draft distinguishes JOMgmt from Academy of Management Journal, Strategic Management Journal, Organization Science.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for contribution framing names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to JOMgmt without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Management
【Skill】jmgmt-contribution-framing
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking contribution framing
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Academy of Management Journal, Strategic Management Journal
【Source status】verified URL / 待核实 / not asserted
【Next skill】jmgmt-tables-figures
```
