---
name: jpsp-rebuttal
description: Use when responding to a Journal of Personality and Social Psychology (JPSP) decision — revise-and-resubmit or accept-with-revision — across a section editor and multiple masked reviewers, deciding when a concern needs new analyses, an internal-meta-analysis update, or new studies. Guides response strategy; it does not fabricate results or write the paper.
---

# Rebuttal & Response Letter (jpsp-rebuttal)

A JPSP decision comes from **one section's editor** synthesizing **masked reviewers**. The section's
framing matters: in IRGP terms, the editor has judged your **central** limitations (must-fix for
interpretability) versus **peripheral** ones, and whether central issues are fixable with **existing**
vs. **new** data. Your response letter must show you understood that distinction and addressed the
central limitations first.

## When to trigger

- An R&R or accept-with-revision decision arrives
- Planning the revision and the point-by-point response
- A reviewer asks for a new study, new analyses, or an updated internal meta-analysis
- Reconciling conflicting reviewer requests under the editor's framing

## Response strategy

1. **Lead with the editor's synthesis.** The editor's letter tells you which concerns are decisive.
   Address **central limitations** first and unmistakably.
2. **Point-by-point, verbatim.** Quote each reviewer comment, then respond; show manuscript changes
   with page/line references and quoted new text.
3. **Existing vs. new data.** If a central limitation is addressable with **existing** studies/data
   (re-analysis, a study currently in the supplement, an added robustness check or updated internal
   meta-analysis), do that. If it truly needs **new** studies, recognize that a rejected paper
   resubmitted with new data is treated as a **new** submission (per IRGP) — decide accordingly.
4. **Disagree respectfully, with evidence.** You may push back on a request that would weaken the
   paper — explain why, cite evidence, and offer an alternative (e.g., a supplementary analysis).
5. **Reconcile conflicts.** When reviewers disagree, surface it and let the editor's framing arbitrate;
   do not silently satisfy one reviewer and ignore another.
6. **Keep transparency current.** Update preregistration/exploratory labeling, JARS reporting, and the
   trusted-repository deposit to reflect new analyses or studies (`jpsp-open-science-and-transparency`).
7. **Respect the caps on the revision.** Added theory/analysis must still fit the section's
   intro+discussion word cap and study limit — push detail to exhibits and the supplement.

## Anti-patterns

- A defensive letter that argues away central limitations instead of fixing them
- Answering peripheral nitpicks thoroughly while sidestepping the decisive concern
- Adding studies that blow the section's study cap into the main text (use the supplement)
- Silently changing results without updating the internal meta-analysis or transparency statements
- Claiming you "addressed" a comment without pointing to the actual change

## Triage map: which concern needs which response

In IRGP terms the editor has already sorted concerns into central vs. peripheral and existing-data vs. new-data. Mirror that sort in your reply so the editor sees you understood the decision.

| Reviewer concern | Likely tier | Response that fits JPSP |
|------------------|-------------|--------------------------|
| "Key study is underpowered" | central, **existing data** | Re-analyze with smallest-effect framing; pool into the **internal meta-analysis**; report the updated CI |
| "Effect could be a confound" | central, **existing or new** | A focused alternative-explanation analysis; add one targeted study only if no existing data isolates it |
| "Theory not advanced beyond demonstration" | central, **conceptual** | Sharpen the contribution and diagnostic hypotheses; a new study rarely fixes a thin idea |
| "Add a fourth manipulation check" | peripheral | Do it briefly or justify; do not let it crowd out the central fix |

A central limitation needing **new** studies means a rejected paper resubmitted later is treated as a **new** submission (IRGP guidance; confirm per section).

## Worked micro-example: a two-reviewer R&R reply

*Illustrative — invented decision to show the structure, not a real letter.*

Editor's synthesis: "innovative idea, but S2's null is a central concern." R1 wants a new study; R2 calls the mediation over-claimed.

- **Open with the central point.** "We agree S2's interpretability was the decisive issue."
- **Existing-data fix first.** Pooling S1–S3 gives random-effects d = 0.31, 95% CI [0.18, 0.45] (illustrative); S2's wide CI [−0.02, 0.44] reflected lower power, now stated at p. 14.
- **Disagree respectfully.** On R2's point we soften causal language to "consistent with" and add a sensitivity analysis, not a new mediation study the design cannot support.
- **Surface the conflict.** R1 asked for a study R2 did not; we offer the pooled re-analysis and defer.

## Output format

```
【Decision】accept-with-revision / R&R (section: ASC/IRGP/PPID)
【Editor's central concerns】listed first
【Per concern】central vs peripheral · existing-data fix vs new study · what changed (page/line)
【Internal meta-analysis】updated if results changed? [Y/N]
【Transparency】prereg/JARS/repository updated? [Y/N]
【Caps respected】revision still within word + study limits? [Y/N]
【Tone】point-by-point, evidence-based, conflicts surfaced for the editor
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — re-analysis, metafor (updated meta-analysis), repository tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — IRGP decision categories and central/peripheral framing
