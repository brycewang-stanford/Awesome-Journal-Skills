---
name: restat-rebuttal
description: Use when a The Review of Economics and Statistics (REStat) decision letter (R&R or reject-and-resubmit) has arrived and the manuscript needs a response-to-referees letter and a revision plan. Drafts the response strategy; it does not run new analysis (route that to the analysis skills).
---

# Rebuttal & Response Letter (restat-rebuttal)

## When to trigger

- A REStat R&R (or a reject with encouragement) arrived and you must respond
- You need to triage referee comments into changes, pushbacks, and concessions
- The response letter needs structure before you write a word of revision
- Referees disagree with each other and you must navigate conflicting demands

## The REStat rebuttal mindset

A REStat revision is judged on whether you **took the identification and measurement concerns seriously and resolved them with evidence**, not rhetoric. The editor is an applied economist arbitrating between referees; your letter must make their job easy: **every comment quoted, addressed, and pointed to the exact change** (page/table/figure). Treat the toughest **identification / measurement** objection as the centerpiece — that is what gets papers rejected at REStat, and resolving it convincingly is what gets them accepted. Concede gracefully where the referee is right; push back **with evidence, never tone** where they are wrong.

## Response-letter structure

1. **Opening:** thank the editor and referees; summarize the 2–4 substantive changes in a short paragraph the editor can skim.
2. **Point-by-point:** for each comment — **quote it**, give your response, name the **specific change** (new Table X, revised §Y, new appendix exhibit Z).
3. **Group related comments** so the same fix is not re-explained; cross-reference.
4. **Disagreements:** state them respectfully, back them with an exhibit or citation, and offer a middle option (e.g., add the alternative as a robustness check even if you keep the main spec).
5. **Conflicting referees:** surface the conflict explicitly for the editor and explain the path you chose.

## Triage table

| Comment type | Response |
|--------------|----------|
| Right and easy | Do it; point to the change |
| Right and hard (new identification/measurement check) | Do it — this is the centerpiece; route to `restat-identification` / `restat-robustness` |
| Based on a misreading | Clarify the text so the misreading cannot recur; thank them for flagging the ambiguity |
| Wrong but defensible request | Add as robustness (appendix), keep the main result, explain why |
| Out of scope / would be a different paper | Decline politely; bound the scope in the text; cite where future work could go |

## Checklist

- [ ] Every referee/editor comment is quoted and individually addressed
- [ ] Each response names the specific change (page / table / figure / section)
- [ ] The hardest identification/measurement objection is resolved with new evidence, not argument
- [ ] Disagreements are evidence-backed and respectful; a middle option offered where possible
- [ ] Conflicting referee demands are surfaced for the editor with a reasoned choice
- [ ] New analyses re-run through the replication package (`restat-replication-package`) so numbers stay consistent
- [ ] Summary of major changes leads the letter for the editor's skim

## Anti-patterns

- A response letter that argues the referee is wrong without adding any evidence
- Vague "we have revised accordingly" with no pointer to the actual change
- Addressing easy comments thoroughly and dodging the hard identification one
- Letting tone turn defensive or dismissive — the editor reads it
- New results that do not reconcile with the deposited code (breaks reproducibility)
- Silently picking one referee over another without flagging the conflict to the editor

## Worked vignette: resolving the centerpiece objection (illustrative)

Referee 2 writes: "I am not convinced the parallel-trends assumption holds; the treated states look
different pre-period." This is the centerpiece — the objection that, unanswered, rejects the paper. A weak
reply asserts that pre-trends "look fine." A REStat reply does three things: (1) adds an **event-study figure**
with pre-period leads and a flat, tightly-estimated pre-trend; (2) reports **Rambachan–Roth honest bounds**
showing the effect survives plausible pre-trend violations; (3) points to the exact new exhibit ("new Figure 3,
§4.2"). The letter opens by summarizing this as the lead change so the editor sees the hardest concern
resolved with evidence first. Easy comments are then dispatched briefly, each with a pointer to the change.

## Output format

```
【Decision】R&R / reject-with-encouragement / minor revision
【Major changes summary】[2–4 bullet paragraph for the editor]
【Centerpiece objection】[the hardest identification/measurement concern] → [evidence-based fix]
【Point-by-point coverage】every comment quoted + change named? [Y/N]
【Disagreements】[comment → evidence-backed pushback + middle option]
【Referee conflicts】[surfaced for editor + chosen path]
【Consistency】new numbers re-run through Dataverse package? [Y/N]
【Next step】revise via the relevant analysis skills → restat-submission (resubmit)
```
