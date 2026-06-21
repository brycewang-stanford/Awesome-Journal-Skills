---
name: cps-rebuttal
description: Use when responding to a Comparative Political Studies (CPS) revise-and-resubmit decision — structuring the response letter to multiple anonymous reviewers and the editor. Plans the revision and response; it does not fabricate results or relitigate the decision.
---

# Rebuttal & R&R Response (cps-rebuttal)

An R&R is a contract: address **every** point from each reviewer and the editor, show what changed, and
point to where. CPS reviewers are comparativists; they care most about comparative leverage, the rival
explanations, measurement across cases, and inference. Treat the letter as a navigable document the
editor can verify against the revised manuscript.

## When to trigger

- A decision letter arrives with reviewer reports (R&R, or major/minor revisions)
- Planning the revision and the point-by-point response
- Reviewers disagree with each other and you must reconcile their demands
- A reviewer asks for analyses that would change the paper's identification or scope

## Response-letter structure

1. **Opening synthesis.** Thank the editor/reviewers; state the 3–4 biggest changes in a short paragraph
   so the editor sees the shape of the revision immediately.
2. **Point-by-point.** Reproduce each comment verbatim, then **Response** (what you did) and **Location**
   (section/table/page). Number them (R1.1, R1.2, …) for easy cross-reference.
3. **Show, don't assert.** Quote new text, name the new exhibit, give the new estimate — don't just say
   "we have addressed this."
4. **Handle disagreement.** Where reviewers conflict, state the trade-off and your principled choice;
   ask the editor to adjudicate if needed. Where you decline a change, give a reasoned, evidence-based
   defense — politely, without relitigating the decision.

## CPS-specific revision priorities

- **Comparative leverage / travel.** If a reviewer doubts the comparison or generalization, strengthen
  the design argument or the scope conditions (`cps-research-design`, `cps-theory-building`) — do not
  just add caveats.
- **Rival explanations.** New robustness or case evidence that adjudicates the rival the reviewer raised;
  state the adjudication sentence explicitly.
- **Measurement across cases.** If asked, show robustness to alternative codings (V-Dem/Polity/etc.) and
  defend comparability.
- **Inference.** Add few-cluster corrections, randomization inference, or multiple-testing adjustments if
  challenged; report honest CIs.
- **Transparency.** Update the replication package and data availability statement to match every new
  result (`cps-transparency-and-data`).

## Reviewer coalition map

Before writing the response, classify comments by reviewer role rather than by report order:

| Reviewer concern | Typical request | Revision move |
|------------------|-----------------|---------------|
| Theory/comparative contribution | Clarify what travels beyond the cases | Rewrite the contribution paragraph and scope conditions |
| Design/identification | Explain comparison, timing, or assignment | Add design schematic, placebo, or rival-specific test |
| Measurement | Defend cross-national coding or construct validity | Add alternative coding, measurement appendix, or limitation |
| Area expertise | Fix case history, regional literature, or institutional detail | Add precise citations and qualify overgeneralization |
| Transparency | Make data/code/evidence auditable | Update Dataverse package, README, appendix, and data statement |

Use the map to reconcile conflicts. If one reviewer wants broader theory and another wants narrower case
precision, the response should say how the revision sharpens the scope condition rather than simply
expanding both sections.

## Checklist

- [ ] Every reviewer and editor point has a numbered Response + Location
- [ ] Opening synthesis lists the major changes up front
- [ ] New text/exhibits/estimates quoted, not merely described
- [ ] Reviewer disagreements reconciled with a stated, principled choice
- [ ] Declined requests answered with evidence, not defensiveness
- [ ] Comparative leverage / rival / measurement / inference concerns addressed substantively
- [ ] Replication package and data availability statement updated to match the revision
- [ ] Revised manuscript still within the word limit and anonymized

## Anti-patterns

- Cosmetic edits dressed up as substantive responses ("we have clarified this")
- Ignoring or merging away a reviewer's point without acknowledgment
- Defensive or dismissive tone; relitigating the decision instead of answering it
- Adding caveats where the reviewer asked for design/identification work
- New results in the letter that the deposited code no longer reproduces
- Letting the revision creep over the word limit or re-introduce identifying info

## Output format

```
【Decision】R&R / major / minor
【Major changes】the 3–4 headline revisions
【Reviewer coalition map】theory / design / measurement / area / transparency concerns classified
【Point-by-point】R1.1 … with Response + Location each
【Disagreements】how conflicting reviews were reconciled
【Declined】any requests declined + the evidence-based reason
【Transparency】package + data availability statement updated? [Y/N]
【Then】resubmit via SAGE Track (cps-submission for the preflight)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — CPS review model and decision categories
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — benchmark the revised framing against verified CPS papers
