---
name: jleo-rebuttal
description: Use when a Journal of Law, Economics, and Organization (JLEO) decision letter has arrived and you need a response-letter strategy — triaging an institutional-economist referee's report into a credible revision and point-by-point reply. Plans the rebuttal; it does not redo the analysis (route back to the relevant jleo-* skill).
---

# Rebuttal Strategy (jleo-rebuttal)

## When to trigger

- A JLEO R&R or major-revision letter arrived and you must plan the response before editing
- Two referees pull in opposite directions (one wants more theory, one more empirics) and you must reconcile
- A referee challenges the institutional mechanism or the identification of a *chosen* governance/institution
- The editor's letter signals which concerns are decisive and which are optional
- You need a point-by-point response that an institutional-economics referee will read as responsive, not evasive

## Reading a JLEO decision letter

JLEO editors and referees come from the institutional and organizational economics communities, and their reports tend to probe the **mechanism** and the **credibility of a chosen institutional object** harder than the marginal estimate. Before drafting, decode the letter:

1. **Find the editor's weighting.** The editor's cover note usually signals which referee points are binding. Solve those first; treat the rest as secondary unless cheap.
2. **Separate the conceptual from the technical.** Institutional referees raise two kinds of point: "your mechanism is not what you claim / your contribution is smaller than stated" (conceptual — may require reframing or new tests) and "this robustness/inference is missing" (technical — usually a table). Triage accordingly.
3. **Identify the deal-breakers.** A challenge to the identification of a self-selected governance form, or to the validity of a hand-coded institutional measure, is usually a deal-breaker that needs real work, not rhetoric.

## Building the response

| Referee point type | Response strategy |
|--------------------|-------------------|
| "Mechanism is mislabeled / contribution oversold" | Reframe honestly; add a test that pins the mechanism, or scope the claim down — do not just reassert |
| "Governance/institution is endogenous" | New identification work (IV / shock / selection bound), then report it; route to jleo-identification |
| "Institutional measure is invalid" | Validate with an alternative measure; document coding; route to jleo-replication-package |
| "Model adds nothing" | Add a comparative static the intuition lacked, or cut the model to its working core |
| "Alternative mechanism" | Add a discriminating test; concede partial if the rival is genuinely live |
| "Missing robustness / inference" | Run it, add the table, point to it; route to jleo-robustness |
| Referees conflict | Let the editor's signal break the tie; explain the choice respectfully to both |

## Drafting discipline

- **Point-by-point, quote then respond.** Reproduce each comment, then state what you changed and where (page/table). Institutional referees check that you actually moved the paper.
- **Lead each reply with the action, not the argument.** "We have added X (Table 3)" before "we believe the original was adequate."
- **Concede where right; defend with evidence where not.** A defended point needs a new exhibit or a citation, not just rhetoric. Never claim a change you did not make.
- **Keep the institutional framing consistent.** If you reframe the mechanism for one referee, propagate it through the abstract, intro, and the other referee's reply so the paper reads coherently.
- **Summarize the major changes up front** in a cover letter to the editor, mapped to the binding concerns.

## Checklist

- [ ] The editor's binding concerns are identified and solved first
- [ ] Every referee point has a quote-then-respond entry that names the change and its location
- [ ] Deal-breakers (endogeneity, measure validity, mechanism) got real work, not rhetoric
- [ ] Conflicting referees reconciled with reference to the editor's signal
- [ ] No claimed change is unsupported by an actual edit/exhibit
- [ ] The reframed institutional mechanism (if any) is consistent across the whole paper

## Anti-patterns

- Reasserting the mechanism a referee challenged without new evidence or a scope-down
- Answering an endogeneity objection with prose where a new design or a bound is needed
- A response that argues with the referee instead of moving the paper
- Claiming a change ("we now address selection") that the manuscript does not actually contain
- Reframing for one referee while leaving the abstract/intro contradicting the new framing

## Worked vignette (illustrative)

Referee 1 says the make-or-buy effect is selection, not governance; Referee 2 says the model is decorative; the editor flags Referee 1 as decisive. The plan: route to jleo-identification for a specificity-shock design that breaks the selection (the decisive fix), then trim the model to the single comparative static the data test (answering Referee 2 cheaply). The response letter leads with the new identification, maps it to the editor's binding concern, and shows the slimmed model now earns its place.

## Output format

```text
【Decision】R&R / major / minor; editor's binding concerns: ___
【Referee points triaged】conceptual vs. technical; deal-breakers: ___
【Action per point】quote → change → location (page/table)
【New work needed】route to jleo-identification / jleo-robustness / jleo-replication-package
【Referee conflict resolution】per editor's signal: ___
【Consistency】reframed mechanism propagated to abstract/intro? [Y/N]
【Next step】revise, then re-run jleo-submission preflight before resubmitting
```
