---
name: jhr-rebuttal
description: Use when a Journal of Human Resources (JHR) revise-and-resubmit arrives and you must plan the response letter — answering referees and the handling editor, satisfying the reconciliation and sensitivity demands, and confirming no fee applies to invited revisions. Strategy and structure; it does not write your results.
---

# R&R Rebuttal Strategy (jhr-rebuttal)

## When to trigger

- A JHR R&R or conditional-acceptance letter arrived
- You need to structure point-by-point responses to referees and the editor
- Referees asked you to reconcile with prior estimates or add sensitivity tests
- You are unsure how much weight to give the handling editor vs. the referees

## JHR-specific framing

- **No fee for invited revisions** — the $175 charge is initial-submission only, so resubmit cleanly without budgeting again.
- **Single-anonymous review:** referees know who you are; keep the tone collegial and specific, and avoid defensive or status-based appeals.
- **The reconciliation requirement carries into revision.** If referees ask why your estimates differ from prior published work, the expected response is **comparative estimation** (re-run under the prior spec/sample) plus **sensitivity tests** — not prose alone. JHR explicitly may require this.
- The **handling editor (coeditor/associate editor)** synthesizes the reports; when referees conflict, anchor your plan to the editor's letter and say so.

## Response-letter structure

1. **Cover note to the editor** — summarize the 3-5 most substantive changes; state how you handled any conflicting referee requests.
2. **Per-referee blocks** — quote each comment, then respond. Use one of: *Done* (point to the new table/figure/section), *Done differently* (justify), or *Respectfully push back* (rare, evidence-based).
3. **A reconciliation appendix** — a side-by-side of your estimate vs. the prior literature's, with the bridge explained (sample, spec, period, population).
4. **A change-log** — every manuscript change keyed to a comment, with new page/exhibit numbers.

## Checklist

- [ ] Every referee point addressed explicitly (none silently dropped)
- [ ] Reconciliation with prior published estimates shown numerically, not asserted
- [ ] Requested sensitivity/comparative tests added and cross-referenced
- [ ] Editor's synthesis used to resolve conflicting referee asks
- [ ] Revision still within the 40-page limit; new material pushed to the Online Appendix
- [ ] Disclosure statement and data-archive footnote updated if anything changed
- [ ] Tone collegial (single-anonymous — they know you)

## Anti-patterns

- Answering prose with prose when a number/comparison was requested
- Silently dropping an inconvenient referee point
- Letting the revision balloon past the page limit
- Picking a fight with one referee instead of letting the editor's letter arbitrate
- Forgetting to refresh the data-availability footnote after adding analyses

## Common referee pushback at JHR and the expected fix

| Referee objection | Weak response | JHR-calibrated response |
|---|---|---|
| "Pre-trends look noisy / TWFE biased with staggered timing" | Cite a methods paper and assert robustness | Re-estimate with a heterogeneity-robust estimator, show the new event study, add a pre-trend sensitivity bound |
| "Why does your estimate differ from [prior paper]?" | A paragraph of contextual speculation | Comparative estimation: prior spec on your sample, your spec on the prior window, bridge table cited |
| "Clustering seems wrong" | Footnote defending current choice | Re-cluster at the assignment level, add wild bootstrap if clusters are few, report both |
| "Effect could be sorting at the cutoff" | Verbal institutional argument only | Density test, covariate continuity, donut estimate in a new appendix exhibit |
| "Results are a LATE; policy claim is broader" | Soften one sentence | Characterize compliers, re-scope the policy paragraph, flag what does not travel |

## Worked response excerpt

```text
Comment R2.3: The staggered rollout makes the TWFE estimates hard to interpret.

Response: Done. We now report Callaway-Sant'Anna group-time ATTs as the
preferred estimates (new Table 3) and move TWFE to Appendix Table A7 for
comparison. The event study (new Figure 2) shows pre-period coefficients near
zero; a pre-trend sensitivity exercise (Appendix Table A8) indicates the
headline effect survives violations up to twice the largest pre-period
estimate. Pages 14-16 are rewritten around the new estimates.
```

Every response of this type names the new exhibit, the new pages, and the
result of the check — referees at this venue reward verifiable specificity.

## Triage order for a multi-referee letter

1. Editor's letter first: extract the must-do list and any arbitration of
   conflicts.
2. Empirical asks next (reconciliation, estimators, inference) — these gate
   acceptance.
3. Framing and exposition asks last; they often resolve themselves once the
   new tables exist.

## Output format

```
【Decision】R&R / conditional accept
【Referee map】R1/R2/R3 asks → response type each
【Reconciliation】prior-vs-ours table added? [Y/N]
【Sensitivity】new tests + cross-refs? [Y/N]
【Length】still <=40pp; overflow in appendix? [Y/N]
【Next step】resubmit via msubmit.net (no fee)
```
