---
name: pom-rebuttal
description: Use when drafting the revision and point-by-point response after a Production and Operations Management (POM) revise-and-resubmit — addressing the Department Editor and referees, splitting changes between the main paper and the e-companion, and respecting the 32-page cap. Drafts the response after revisions; it does not interpret the decision letter (pom-review-process).
---

# R&R Response & Rebuttal (pom-rebuttal)

## When to trigger

- You received a POM R&R and have planned (or made) the revision
- You must reconcile conflicting referee demands for the Department Editor
- A later-round decision asks you to defend or further revise prior changes

> Write the response letter **after** revising the manuscript, not before. Resubmit through ScholarOne (mc.manuscriptcentral.com/poms) to the **same Department Editor** where possible, and keep the revised main document within the **32-page** cap — push heavy new material into the unlimited online **e-companion**.

## Response-document structure

1. **Opening letter to the Department Editor.** Thank the editor and referees; summarize the most important changes in 2–4 sentences; state explicitly how you addressed the editor's stated priorities, including any practice-relevance concern. Note where referees conflicted and how you resolved it.
2. **Per-referee sections.** Restate every comment (verbatim or faithfully numbered), then respond.
3. **Point-by-point format** for each comment:
   - **Comment** (quoted/numbered)
   - **Response** (what you changed and the OM reasoning)
   - **Location** (main-paper section/table/figure **and** e-companion item)
   - **Implication** (how the change strengthens the theory and/or practice contribution)

## Responding to POM's signature demands

- **"Sharpen the operations mechanism / contribution."** Strengthen the mechanism and the managerial lever; show what the OM field now learns and what a manager does differently — do not merely add citations (see `pom-theory-development`, `pom-contribution-framing`).
- **"Practice relevance is unclear."** This is a real gate at POM. Translate results into operational magnitude (cost, fill rate, wait time) and an actionable decision; add evidence, not rhetoric.
- **"Strengthen the method."** For analytical work, add a proof, relax an assumption, or extend the numerical study (full derivations → e-companion). For empirical work, add identification or robustness; for data science, demonstrate operational value.
- **"Add analysis/study."** Often decisive — but watch the 32-page budget; new material typically lives in the e-companion so the main body stays within limit.

## Tone and tactics

- Be respectful and substantive; referees are colleagues investing in the paper.
- Concede gracefully where they are right; make the change.
- Disagree with evidence, not assertion; if you decline a request, give an OM reason and an alternative analysis where possible.
- Address every point — silent omissions read as evasion.
- Surface referee conflicts to the Department Editor and state your chosen resolution.
- Do not reframe a barred resubmission as a normal revision — only an explicit invitation reopens POM.

## Worked micro-example: weak vs. strong response

Referee comment: *"The base-stock result appears to hinge on full backordering; under lost sales the structure could collapse."*

- **Weak response:** "We thank the referee for this observation. Backordering is a standard assumption in the inventory literature (citations)." — This concedes nothing, tests nothing, and will read to the Department Editor as evasion of a legitimate modeling concern.
- **Strong response:** "We agree the demand-fulfillment regime deserves scrutiny. We re-derived the ordering policy under lost sales (new e-companion section EC.4): the base-stock structure survives, the optimal level rises modestly across our calibrated instances, and the managerial ranking — dual sourcing dominates expediting — is unchanged. Revised Section 5.2 and Table 3 report the comparison; full proofs remain in EC.4." — New analysis, quantified operational consequence, exact main-paper and e-companion locations.

## What POM referees probe, by method track

- **Analytical:** every load-bearing assumption defended in operational terms (why stationary demand, why exponential service times), and tractability choices priced — a numerical study showing what relaxing them changes.
- **Empirical:** identification threats named and countered — endogenous inventory or capacity choices, demand censoring in sales records — plus robustness of any structural estimates to alternative specifications and samples.
- **Behavioral:** incentive compatibility of the experimental design and an argued bridge from the lab decision to real ordering or scheduling behavior.
- **Data science:** operational value demonstrated beyond predictive accuracy — a decision that improves, not merely a metric that rises.

## Checklist

- [ ] Manuscript actually revised before the letter was written
- [ ] Editor's priorities (incl. practice relevance) addressed first and explicitly
- [ ] Every referee comment restated and answered; none skipped
- [ ] Each response names main-paper **and** e-companion locations
- [ ] Mechanism/practice and method demands met with real changes, not citations only
- [ ] Revised main document still within 32 pages
- [ ] Referee conflicts surfaced and resolved for the editor

## Output format

```
【Decision round】1st R&R / 2nd round / ...
【Editor priorities addressed】1... 2... 3...
【Per-referee coverage】R1: x/x, R2: x/x, R3: x/x — all answered? yes/no
【Major changes】mechanism/practice: ... method/data: ... new analysis: ...
【Declined requests + justification】[...]
【Page/e-companion status】main pages within 32? new material → e-companion
【Next step】resubmit via ScholarOne; on next decision → pom-review-process
```
