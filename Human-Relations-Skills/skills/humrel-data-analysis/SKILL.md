---
name: humrel-data-analysis
description: Use when working on data analysis for a Human Relations manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Data Analysis (humrel-data-analysis)

## When to trigger
- The manuscript is aimed at **Human Relations (Human Relations)** and data analysis is the active bottleneck.
- A coauthor asks whether the draft meets the journal's work, employment, organizations, social relations, power, identity, and critical management standard.
- The paper risks being confused with nearby venues: Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| workplace relation is central | Make the workplace relation assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| power and identity is central | Make the power and identity assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| employment institution is central | Make the employment institution assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| qualitative insight is central | Make the qualitative insight assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| social theory is central | Make the social theory assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## Human Relations fit notes

- Publisher / owner context: SAGE for the Tavistock Institute.
- Submission route to re-check: SAGE / ScholarOne submission.
- Signature vocabulary: workplace relation, power and identity, employment institution, qualitative insight, social theory.
- Sibling boundary: Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society.
- House-style aim: socially grounded organization research that links theory, context, and lived work.
- Official URLs currently used by the pack:
- https://journals.sagepub.com/home/hum
- https://journals.sagepub.com/author-instructions/HUM

## Stage-specific moves

1. State the exact data analysis question in one sentence.
2. Identify which Human Relations audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `humrel-contribution-framing` if the stage passes, or back to `humrel-workflow` if it does not.

## Checklist
- [ ] The Human Relations audience can see why the paper belongs in work, employment, organizations, social relations, power, identity, and critical management.
- [ ] The draft distinguishes Human Relations from Organization Studies, Journal of Management Studies, Administrative Science Quarterly.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for data analysis names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to Human Relations without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Human Relations
【Skill】humrel-data-analysis
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking data analysis
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Organization Studies, Journal of Management Studies
【Source status】verified URL / 待核实 / not asserted
【Next skill】humrel-contribution-framing
```
