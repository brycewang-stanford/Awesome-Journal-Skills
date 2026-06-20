---
name: ier-literature-positioning
description: Use when working on literature positioning for a International Economic Review manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Literature Positioning (ier-literature-positioning)

## When to trigger
- The manuscript is aimed at **International Economic Review (IER)** and literature positioning is the active bottleneck.
- A coauthor asks whether the draft meets the journal's general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach standard.
- The paper risks being confused with nearby venues: QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| general-equilibrium discipline is central | Make the general-equilibrium discipline assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| structural clarity is central | Make the structural clarity assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| international readership is central | Make the international readership assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| theory-empirics balance is central | Make the theory-empirics balance assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| concise identification is central | Make the concise identification assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## IER fit notes

- Publisher / owner context: Wiley for the Economics Department of the University of Pennsylvania and the Osaka University Institute of Social and Economic Research.
- Submission route to re-check: Wiley / ScholarOne-style online submission.
- Signature vocabulary: general-equilibrium discipline, structural clarity, international readership, theory-empirics balance, concise identification.
- Sibling boundary: QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review.
- House-style aim: formal economics argument with enough intuition for a broad journal audience.
- Official URLs currently used by the pack:
- https://onlinelibrary.wiley.com/journal/14682354
- https://onlinelibrary.wiley.com/page/journal/14682354/homepage/forauthors.html

## Stage-specific moves

1. State the exact literature positioning question in one sentence.
2. Identify which IER audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `ier-identification` if the stage passes, or back to `ier-workflow` if it does not.

## Checklist
- [ ] The IER audience can see why the paper belongs in general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach.
- [ ] The draft distinguishes IER from QJE, JPE, REStud.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for literature positioning names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to IER without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-literature-positioning
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking literature positioning
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not QJE, JPE
【Source status】verified URL / 待核实 / not asserted
【Next skill】ier-identification
```
