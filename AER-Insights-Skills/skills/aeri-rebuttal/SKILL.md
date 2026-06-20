---
name: aeri-rebuttal
description: Use when responding to an American Economic Review: Insights (AER: Insights) conditional-accept decision — addressing the editor's letter within the short window, usually without a second referee round. Drafts a concise, decisive response and revision plan; it does not redo the analysis (see aeri-robustness / aeri-identification).
---

# Conditional-Accept Response (aeri-rebuttal)

## When to trigger

- A **conditional accept** letter arrived from AER: Insights
- You must return a revised short paper within the conditional window (~8 weeks)
- The letter lists changes the editor expects, and you need a tight response
- You received a **reject** and are deciding what to do (see end of this skill)

## What an AER: Insights conditional accept means (检索于 2026-06；以官网为准)

AER: Insights does **not** issue traditional revise-and-resubmit decisions. A **conditional accept** means the editor **expects to publish** the paper subject to the changes in the decision letter; authors typically get about **8 weeks** to return the revision, which is **normally not sent back to referees**. The conditions are meant to be **achievable without substantial uncertainty** — this is finishing, not relitigating. So the response is short, complete, and non-defensive: do what the letter asks, document it crisply, and do not reopen settled issues.

## How to respond

1. **Treat the letter as a punch list.** Map every requested change to a concrete edit; nothing is "optional."
2. **Comply, don't argue.** Since there is no referee round to win, push back only where a request is genuinely infeasible or would be wrong — and then offer an alternative that satisfies the underlying concern.
3. **Keep the response letter short.** One numbered item per request: the request, what you did, where in the paper (section/exhibit/line). Editors of a short journal reward concision.
4. **Protect the caps.** Edits must keep the paper **within 7,000 − 200×(#exhibits) words and ≤5 exhibits** — added text or an added exhibit can re-breach the gate. Move new material to the Supplemental Appendix ([`aeri-robustness`](../aeri-robustness/SKILL.md)).
5. **Finalize the replication package.** A conditional accept means the AEA Data Editor check is imminent; have the deposit ready ([`aeri-replication-package`](../aeri-replication-package/SKILL.md)).
6. **Keep the single insight intact.** Do not let requested additions turn the short paper into a sprawling one.

## Response-letter structure

```
Dear Editor [name],
Thank you for the conditional acceptance. We have addressed each point below.

1. [Editor request, quoted/paraphrased]
   Response: [what we did], now in [Section/Exhibit/Appendix].
2. ...
We confirm the manuscript remains within the word and exhibit limits, and the
replication package is prepared for the AEA Data Editor.
```

## Checklist

- [ ] Every item in the decision letter mapped to a concrete edit
- [ ] Response letter is **concise**, point-by-point, non-defensive
- [ ] Any pushback is rare, justified, and offers an alternative
- [ ] Revised paper still **within word + exhibit caps**; new material to the appendix
- [ ] The **single insight** is unchanged; no scope creep
- [ ] Replication package finalized for the **AEA Data Editor** check
- [ ] Returned within the conditional window (~8 weeks)

## Anti-patterns

- Arguing with the editor as if this were a multi-round R&R
- Adding text/exhibits that re-breach the word or exhibit cap
- A long, defensive response letter for a short paper
- Letting requested additions sprawl the paper beyond its single insight
- Leaving the data/code deposit until after the response is sent

## If it was a REJECT instead

There is no path to relitigate a reject at AER: Insights. Reframe quickly: the short paper is often a strong fit for an **AEJ** field journal, or can be expanded into a fuller **AER**-style paper if the idea supports more. Route back to [`aeri-topic-selection`](../aeri-topic-selection/SKILL.md) to decide which.

## Output format

```
【Decision】conditional accept / reject
【Punch list】each request → edit → location
【Caps after revision】words = __ (≤ 7000 − 200×__?), exhibits __/5
【Insight intact】single idea unchanged? [Y/N]
【Data editor】replication package ready? [Y/N]
【If reject】next venue (AEJ / expand to AER) → aeri-topic-selection
【Next step】submit revision within ~8-week window
```
