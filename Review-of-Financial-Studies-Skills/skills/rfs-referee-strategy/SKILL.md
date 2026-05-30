---
name: rfs-referee-strategy
description: Use when choosing suggested/opposed referees or running an objection pre-mortem before submitting a The Review of Financial Studies (RFS) manuscript. Anticipates reviewer concerns; does NOT write the rebuttal (that is rfs-rebuttal).
---

# Referee Strategy & Objection Pre-Mortem (rfs-referee-strategy)

## When to trigger

- The portal asks for suggested and opposed reviewers
- You want to anticipate the objections RFS referees will raise before they do
- A coauthor asks "who will referee this and what will they hate?"
- Preparing the cover letter's referee section

## Two jobs: referee selection and objection pre-mortem

### A. Suggesting and opposing referees
- **Suggest** referees who are active in your exact sub-field, have published the closest methods, and can evaluate both the novelty and the rigor. RFS referees are usually the authors you cite most.
- Aim for a balanced slate: not only your closest collaborators' circle, and not only theorists for an empirical paper (or vice versa).
- **Oppose** referees only with a brief, professional reason (active competing project, prior dispute, direct conflict). Do not over-exclude — editors notice and discount long oppose lists.
- Never suggest coauthors, advisors/advisees, or same-institution colleagues — these are conflicts the editor will strike.
- The editor chooses; your list is advisory. Make it easy for them to find qualified, fair referees.

### B. Objection pre-mortem (the high-value step)
Anticipate the specific objections an RFS referee will raise and address them *before* submission. Common RFS referee challenges:

| Objection                                  | Pre-empt by                                                |
|--------------------------------------------|------------------------------------------------------------|
| "This is incremental / not novel enough"   | A crisp delta in the intro (`rfs-literature-positioning`)  |
| "Endogeneity is not resolved"              | A clean shock + diagnostics (`rfs-identification`)         |
| "Results are fragile"                       | A full robustness battery (`rfs-robustness`)               |
| "You data-mined this predictor"            | Multiple-testing adjustment + OOS test                     |
| "Standard errors are wrong"                | Clustering/adjustment matched to the data                  |
| "The mechanism is asserted, not shown"     | Direct mechanism evidence / heterogeneity                  |
| "Missing a key recent paper"               | Cite and distinguish it (the close competitor)             |
| "Theory and empirics are disconnected"     | Integrate the model's prediction with the test             |

For each likely objection: write the one-paragraph answer now, and make sure the paper (or IA) already contains the evidence that answer points to.

### Reading the desk-reject vs. send-out signal
- The most common reason an RFS paper does not get sent out is a perceived novelty shortfall, not a technical flaw. Make the contribution unmissable in the abstract and first two pages.
- A second common gate is an identification threat the editor can see immediately. Surface your source of variation early so the editor does not assume it is absent.
- If two strong sub-fields could referee the paper (e.g., asset pricing and intermediation), suggest at least one from each so the editor can triangulate.

### Cover-letter referee note
- Keep it to a few sentences: name suggested referees and a one-clause reason each; name opposed referees with a brief professional reason; state there is no dual submission.

## Checklist

- [ ] Suggested referees are sub-field experts who can judge novelty AND rigor
- [ ] No conflicted names suggested (coauthors, advisors, same institution)
- [ ] Opposed list is short and professionally justified
- [ ] Top 5–8 likely objections written out with a planned response
- [ ] Each anticipated objection has supporting evidence already in the paper/IA
- [ ] The "not novel enough" risk is specifically pre-empted in the intro

## Anti-patterns

- A long opposed-referee list — signals defensiveness; editors discount it.
- Suggesting only friendly or conflicted referees.
- Ignoring the "incremental" objection because the empirics are clean.
- Discovering a fatal objection only after the reports arrive.
- Suggesting referees who cannot evaluate the method (e.g., pure theorists for a microstructure paper).

## Output format

```
【Suggested referees】[names + why each: sub-field + method fit]
【Opposed】[short, justified]
【Top objections】[objection → planned response → where evidence lives]
【Novelty defense】one-paragraph pre-empt for the "incremental" risk
【Next step】rfs-submission (finalize) → await decision → rfs-rebuttal
```
