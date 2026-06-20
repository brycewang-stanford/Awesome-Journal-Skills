---
name: jhe-tables-figures
description: Use when working on tables and figures for a Journal of Health Economics manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Tables and Figures (jhe-tables-figures)

## When to trigger
- The manuscript is aimed at **Journal of Health Economics (JHE)** and tables and figures is the active bottleneck.
- A coauthor asks whether the draft meets the journal's health economics, insurance, provider incentives, medical technology, health policy, and health behavior standard.
- The paper risks being confused with nearby venues: American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| provider incentives is central | Make the provider incentives assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| insurance design is central | Make the insurance design assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| patient selection is central | Make the patient selection assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| clinical-policy margin is central | Make the clinical-policy margin assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| health-data privacy is central | Make the health-data privacy assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JHE fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: provider incentives, insurance design, patient selection, clinical-policy margin, health-data privacy.
- Sibling boundary: American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy.
- House-style aim: policy-relevant causal evidence with institutional health-system detail.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-health-economics
- https://www.elsevier.com/journals/journal-of-health-economics/0167-6296/guide-for-authors

## Stage-specific moves

1. State the exact tables and figures question in one sentence.
2. Identify which JHE audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jhe-writing-style` if the stage passes, or back to `jhe-workflow` if it does not.

## Checklist
- [ ] The JHE audience can see why the paper belongs in health economics, insurance, provider incentives, medical technology, health policy, and health behavior.
- [ ] The draft distinguishes JHE from American Journal of Health Economics, Journal of Public Economics, Health Economics.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for tables and figures names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to JHE without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-tables-figures
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking tables and figures
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not American Journal of Health Economics, Journal of Public Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jhe-writing-style
```
