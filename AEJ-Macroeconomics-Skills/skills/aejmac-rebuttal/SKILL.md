---
name: aejmac-rebuttal
description: Use when an American Economic Journal: Macroeconomics (AEJ: Macro) decision letter has arrived (R&R or reject-with-comments) and you need a response-letter strategy and revision plan. Plans the rebuttal and revision; it does not run new identification, model, or robustness work itself (route to those skills).
---

# Rebuttal & Response Letter (aejmac-rebuttal)

## When to trigger

- An R&R from the editor/coeditor and referees has arrived
- A reject-with-comments where a re-submission (here or elsewhere) is being weighed
- Referee reports conflict with each other and you must reconcile them
- You need to convert a pile of macro objections into a tractable revision plan

## The AEJ: Macro rebuttal posture

AEJ: Macro review is **single-blind** and editor/coeditor-managed; the coeditor's letter is the **binding instruction set** — when a referee and the coeditor disagree, follow the coeditor. The response must show that the **broad-interest macro contribution survived** the scrutiny and that the identified-empirical and/or quantitative-model objections are answered with **new exhibits, not new prose alone**. Macro referees reward a response that re-runs the decisive check and reports the (possibly changed) number honestly.

## Building the response

### Step 1 — Triage every comment
- Build a table: comment → required action → owning skill → main-text vs. appendix → status.
- Tag each as **(a) do and show**, **(b) do and report even if it weakens the result**, or **(c) reasoned pushback**. Most should be (a)/(b); reserve (c) for the few you can win on the merits.

### Step 2 — Map comments to the macro skills
- Identification objections → `aejmac-identification` (re-do the SVAR/LP/narrative defense).
- "Artifact of the sample/spec" → `aejmac-robustness` (sample splits, method cross-check).
- Calibration / counterfactual / Lucas-critique → `aejmac-theory-model`.
- "Not broad enough" / contribution unclear → `aejmac-literature-positioning` / `aejmac-writing-style`.
- Reproducibility → `aejmac-replication-package`.

### Step 3 — Write the letter
- **Open with a short summary** of the main changes and the headline (state if the number moved).
- **One comment, one response block**: restate the comment, state what you did, point to the exact new table/figure/section, quote the changed text.
- **Be honest about movement**: if a robustness check changed the estimate, report the new value and explain why the conclusion still holds (or how it is now appropriately qualified).
- **Push back sparingly and with evidence**, never with attitude; concede gracefully where the referee is right.

### Step 4 — Reconcile conflicts
- When referees conflict, say so explicitly, explain your choice, and tie it to the coeditor's guidance.

## Checklist

- [ ] Every comment in a triage table with action, owning skill, location, status
- [ ] The coeditor's letter treated as binding; conflicts reconciled to it
- [ ] Each empirical/model objection answered with a **new exhibit**, not prose alone
- [ ] Honest reporting where a check moved the headline number
- [ ] Response letter is point-by-point, with exact pointers and quoted changed text
- [ ] Pushback is rare, evidenced, and courteous
- [ ] Reproducibility comments resolved against the openICPSR package

## Anti-patterns

- Answering an identification or robustness objection with words instead of a re-run and a new exhibit
- Hiding that a robustness check changed the estimate
- Treating a referee as adversary; defensiveness in tone
- Ignoring the coeditor's priorities to satisfy a referee's tangent
- A response letter that does not point to exact tables/sections
- Promising changes in the letter that are not actually in the revised manuscript

## Worked vignette: the number moved (illustrative)

A referee says the monetary-policy output response is a pre-Volcker artifact. You re-estimate post-1984 (`aejmac-robustness`) and the peak response falls from -0.8% to -0.6% (90% bands overlapping). The strong response block: "We agree the early sample could drive the result. Re-estimating on 1984–2019 (new Table A4, Figure A3), the peak output response is -0.6% (90% band [-1.0, -0.2]), within the band of the full-sample estimate; the qualitative conclusion is unchanged and the magnitude is now reported for the modern monetary regime. We have revised the abstract and Section 4 accordingly." Honest, exhibit-backed, conclusion preserved and appropriately scoped.

## Output format

```
【Decision type】R&R / reject-with-comments
【Triage table built】comment → action → owning skill → location → status? [Y/N]
【Coeditor letter treated as binding】conflicts reconciled to it? [Y/N]
【New exhibits for empirical/model objections】listed? [Y/N]
【Honest number movement reported】? [Y/N / NA]
【Letter style】point-by-point with exact pointers? [Y/N]
【Next step】revise manuscript; re-run aejmac-submission preflight before resubmitting
```
