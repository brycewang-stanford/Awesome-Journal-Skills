---
name: jue-rebuttal
description: Use when a Journal of Urban Economics (JUE) decision letter (R&R or reject-and-resubmit) needs a response-letter strategy and a revision plan. Turns referee reports into a point-by-point response and routes the analytical work back through the pack; it does not run the new analysis itself.
---

# Rebuttal Strategy (jue-rebuttal)

## When to trigger

- A JUE R&R or major-revision letter arrived and you need a response plan
- Referees raised spatial objections (sorting, spillover, scale, spatial SEs) you must now answer with evidence
- Referees disagree with each other or with the editor and you must triage
- You are deciding which requests to satisfy, which to push back on, and which to defer
- A reject-and-resubmit invites a re-engineered design and you must scope it

## Read the editor first, then the referees

The editor's letter, not the longest referee report, sets the bar. JUE editors (检索于 2026-06；以官网为准) signal which concerns are **binding** for acceptance and which are advisory. Build the plan around the binding spatial concerns; do not exhaust effort on a referee's cosmetic asks while the editor's identification worry goes half-answered.

## Triage every comment

| Comment type | Response |
|--------------|----------|
| Binding identification/spatial concern (sorting, SUTVA, spatial SEs) | new analysis routed to `jue-identification` / `jue-robustness`; lead the response with it |
| Robustness / scale / boundary ask | run the check (`jue-robustness`); report the point estimate barely moves |
| Mechanism / equilibrium interpretation | tighten via `jue-theory-model`; locate incidence, short vs long run |
| Framing / venue / positioning | reframe via `jue-literature-positioning` / `jue-writing-style` |
| Factually mistaken referee point | disagree **respectfully with evidence**; never dismiss |
| Out-of-scope / would change the paper's question | decline politely, explain the scope, offer a smaller version |

## Response-letter craft for JUE

1. **One letter, point by point**, quoting each comment then answering immediately; mark the manuscript change (section/table/figure) for every response.
2. **Lead with the binding spatial concern.** If sorting or SUTVA was the central worry, the first response is the new design evidence — the reviewer should see it without searching.
3. **Show the estimate barely moved.** For every robustness ask, report the new check *and* that the headline magnitude is stable; instability reported honestly with a bound.
4. **Disagree with evidence, never with tone.** A wrong referee point gets a falsification or a citation, not a brush-off.
5. **Make changes visible.** Reference new exhibits by number; a diff or change-summary at the top helps the editor confirm compliance fast.
6. **Re-run the preflight.** A revision still passes through Editorial Manager; confirm the replication folder and any exemption are current (`jue-submission`).

## Deciding whether to fight or fold a spatial objection

Not every spatial objection deserves a new design; calibrate the response to what the objection actually threatens:

- **Fold (run the work)** when the objection names a real spatial confound the paper does not yet answer — sorting, SUTVA, naive SEs. These are cheap to lose and expensive to ignore; run the check and lead with it.
- **Fight (with evidence)** when the referee's premise is wrong — e.g., they assert the boundary coincides with a confounder that your covariate-smoothness panel already rules out. Quote the panel; do not concede a point the data refutes.
- **Reframe** when the objection is really about scope or venue — answer by sharpening the contribution and the equilibrium reading, not by adding analysis.
- **Decline** when satisfying the request would change the paper's question into a non-JUE paper; explain the scope and, if useful, offer a smaller companion result.

The editor reads the response for judgment as much as effort: a paper that folds on the binding spatial concern and fights only where the evidence is clearly on its side reads as credible.

## Checklist

- [ ] The editor's binding concerns are identified and answered first
- [ ] Every referee comment has a point-by-point response with a marked manuscript change
- [ ] Binding sorting/SUTVA/spatial-SE concerns answered with new evidence, led in the letter
- [ ] Robustness asks show the point estimate barely moves (or honest bound if it does)
- [ ] Disagreements are evidence-based and respectful
- [ ] New exhibits referenced by number; change summary provided
- [ ] Replication folder and any confidential-data exemption refreshed for the revision
- [ ] Revision scope held to the binding concerns, not expanded into fresh objections
- [ ] Local-estimand honesty carried into all new results (no new over-claiming)

## Anti-patterns

- Answering the loudest referee while the editor's binding concern is left thin
- Reporting that significance survived while the point estimate quietly wandered
- Dismissing a mistaken referee point instead of refuting it with evidence
- Agreeing to a scope change that turns it into a different (non-JUE) paper
- A response letter that asserts changes without pointing to the section/table/figure
- Forgetting the revision re-enters Editorial Manager and must stay replication-compliant

## Worked vignette (illustrative)

The light-rail paper's R&R has one binding editor concern — control contamination from displaced demand — and several robustness asks. The response leads with a new spillover-ring design (treated 0–800m, ring 800–1600m, control >1600m) showing the capitalization estimate holds at 4.4% and quantifying the displacement, each tied to a new map and table. The bandwidth and spatial-SE-cutoff asks follow, each showing the estimate in [4.2%, 4.6%]. A referee's claim that the boundary coincides with a highway is refuted with a covariate-smoothness panel. The letter then routes back through `jue-submission` to confirm the revision is replication-compliant.

## Pace and the revised replication folder

A field-flagship R&R is a genuine opportunity, but the clock and the standards both tighten on the second pass. Two practical disciplines: first, do not let the revision sprawl — answer what the editor flagged as binding and the referees' substantive spatial points, and resist adding scope that invites a fresh round of objections. Second, every new analysis (a spillover ring, a new scale, a placebo) changes the code and exhibits, so refresh the replication folder *as you revise*, not at the end; a revision that re-runs cleanly from raw data to the new maps is both correct and ready for the acceptance deposit. Carry the local-estimand honesty into the new results too — referees re-read for over-claiming.

## Output format

```text
【Editor's binding concerns】[...]
【Comment triage】binding-spatial: ___ | robustness: ___ | mechanism: ___ | framing: ___ | mistaken: ___ | out-of-scope: ___
【New evidence】design/robustness routed to jue-identification / jue-robustness
【Estimate stability】headline before → after: ___ → ___
【Disagreements】evidence-based, respectful? [Y/N]
【Revision compliance】replication folder + exemption refreshed? [Y/N]
【Next skill】jue-workflow (re-sequence remaining revision work) → jue-submission
```
