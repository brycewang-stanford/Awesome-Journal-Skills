---
name: mksc-rebuttal
description: Use when drafting the revision and response letter after a Marketing Science revise-and-resubmit — structuring point-by-point responses to the Senior/Associate Editor and reviewers across a multi-round process, especially on assumptions, identification, counterfactuals, computation, and replication. Drafts the response after revising; it does not interpret the decision (mksc-review-process).
---

# R&R Response & Rebuttal (mksc-rebuttal)

## When to trigger

- You received an MKSC R&R and have planned the revision (via `mksc-review-process`)
- You have actually made (or scoped) the manuscript and code changes and need to write the response
- You must reconcile conflicting reviewer demands for the AE
- A later-round decision asks you to defend or extend prior changes

> Write the response **after** revising the manuscript and re-running the analysis — it documents changes, not promises. The process is developmental and typically multi-round; resubmit the revised manuscript, response document, and updated replication materials through ScholarOne (mc.manuscriptcentral.com/mksc), keeping the same handling team where possible and the manuscript blinded.

## Response-document structure

1. **Opening letter to the Senior/Associate Editor.** Thank the team; summarize the most important changes in 2–4 sentences; explicitly address the AE's prioritized concerns. Note where reviewers conflicted and how you resolved it. (The cover letter/response is seen by the Editor/AE; keep the manuscript anonymized.)
2. **Per-reviewer sections.** Restate every comment (numbered/faithfully), then respond.
3. **Point-by-point format**: **Comment** → **Response** (what you did and the modeling/econometric reasoning) → **Location** (section/table). Quote new manuscript text where helpful.

## Responding to MKSC's signature demands

- **"Identification is not credible."** Add the explicit identification argument, stronger/alternative instruments, a sensitivity-of-estimates analysis, or a Monte Carlo recovering known parameters — and explain why it resolves the concern (see `mksc-data-analysis`).
- **"The model is too restrictive / an assumption drives the result."** Relax the assumption and re-estimate, or show the result is robust to it; report the new comparative static/counterfactual.
- **"The counterfactual is not valid."** Re-solve allowing firms to re-optimize, report magnitudes with uncertainty, and bound the scope of validity.
- **"Computation / multiple equilibria."** Report solver settings, convergence, multiple starting values, and how multiplicity is handled.
- **"Replication."** Update the data-and-code package; confirm the master script reproduces every revised table/figure/counterfactual.
- **Adding analysis vs. length.** Heavy new derivations or robustness usually live in the **online appendix**; for a **Frontiers** paper, the 6,000-word total cap still binds, so move detail online.

## Before/after: answering the signature "identification" objection

The modal MKSC first-round comment is some form of "I am not convinced the model identifies the effect." Compare responses:

- **Weak (citation-padding, will draw a second round):** "We thank the reviewer. We have added references to prior structural work establishing that this class of models is identified (Section 3)."
- **Strong (re-analysis, closes the point):** "We agree the argument was implicit. We now (i) state the exclusion restriction explicitly — cost shifter Z shifts supply but not demand conditional on our controls (Section 3.2); (ii) add a Monte Carlo that recovers the known parameters from simulated data within 3% (Appendix C.1); and (iii) report a sensitivity analysis showing the counterfactual moves less than 5% as we perturb the restriction (Table C4). Together these address the concern that [assumption] drove the estimate."

The strong version does real work — an explicit restriction, a recovery experiment, and a sensitivity bound — and tells the AE exactly where each lives.

## Reconciling conflicting reviewers for the AE

When reviewers pull in opposite directions (R1: "the model is too stylized"; R2: "the model is over-parameterized"), do not silently satisfy one. State the trade-off to the AE, choose a resolution, and justify it: e.g., "We keep the parsimonious specification R2 favored and add R1's richer variant as a robustness check in Appendix D, showing the main counterfactual is unchanged." Surfacing the conflict with a defended choice reads as judgment; picking a side silently reads as evasion.

## Tone and tactics

- Be respectful and substantive; concede gracefully and make the change.
- Disagree with evidence (an alternative estimation, a robustness result), not assertion.
- Address every point; silent omissions read as evasion.
- Surface reviewer conflicts to the AE with your chosen resolution.

## Checklist

- [ ] Manuscript and code actually revised before the letter was written
- [ ] AE's prioritized concerns addressed first and explicitly
- [ ] Every reviewer comment restated and answered, with locations
- [ ] Identification / assumption / counterfactual demands met with real re-analysis
- [ ] Computation and replication-package updates documented
- [ ] Declined requests justified with evidence and an alternative test
- [ ] Manuscript stays blinded; length/Frontiers cap respected

## Anti-patterns

- Writing the response before re-running the analysis.
- Answering "deepen identification" by adding citations instead of re-estimating.
- A counterfactual left unchanged when firm re-optimization was the objection.
- Skipping an inconvenient comment or de-blinding the manuscript.

## Output format

```
【Round】1st R&R / 2nd / ...
【AE priorities addressed】1... 2... 3...
【Per-reviewer coverage】R1 x/x, R2 x/x, R3 x/x — all answered?
【Major changes】model/identification: ... counterfactual: ... computation: ...
【Replication】updated package reproduces revised exhibits?
【Declined + justification】...
【Status】drafted / final → resubmit via ScholarOne
【Next step】on next decision → mksc-review-process
```
