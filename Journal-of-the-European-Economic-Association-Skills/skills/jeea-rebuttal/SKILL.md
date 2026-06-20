---
name: jeea-rebuttal
description: Use when an R&R or decision letter arrives for a Journal of the European Economic Association (JEEA) manuscript and a response-letter strategy and revision plan are needed. Plans and drafts the response; it does not produce new estimates or rewrite the paper.
---

# Rebuttal & Response Letter (jeea-rebuttal)

## When to trigger

- A JEEA decision letter arrived (R&R, major/minor revision, or reject-and-resubmit)
- You need to triage referee + co-editor comments into a revision plan
- You are drafting the point-by-point response and are unsure how to prioritize
- Referees disagree with each other, or with the co-editor

## The JEEA revision reality (source map refreshed 2026-06-20)

JEEA review is **single-blind** and **co-editor-led**: the co-editor's letter is the **controlling document** — it tells you which referee points are binding and which are optional. Resubmission also requires the **submitting author to be a current EEA member**. Empirical revisions must keep the **replication package current** because the **Data Editor verifies it before formal acceptance**. The editorial team works to a **fast timeline**, so a focused, complete revision is rewarded over a sprawling one. Address the **general-interest contribution** the co-editor cares about first; subfield minutiae second.

## Response-letter strategy

- **Read the co-editor's letter as the priority map.** Do exactly what it flags as essential; treat referee points it downgrades as lower priority (but still answer them).
- **Point-by-point, quote-then-respond.** Reproduce each comment, then state precisely what you changed and where (section, table, page), or why you respectfully did not.
- **Concede gracefully, push back with evidence.** Where a referee is right, fix it and say so. Where you disagree, disagree with an analysis or a citation, never with attitude (single-blind: they know who you are).
- **Resolve referee conflicts via the co-editor.** When referees contradict each other, follow the co-editor's steer and say you did.
- **Show, don't assert.** New robustness or a generalized proposition belongs in the paper and is pointed to from the letter, not merely promised.
- **Keep the replication package in sync** with every new exhibit (`jeea-replication-package`).

## Revision plan structure

1. **Co-editor's essential requests** — addressed first, completely.
2. **Major referee points** — identification, model generality, robustness, contribution.
3. **Minor points** — exposition, citations, exhibits.
4. **Conflicts** — how you resolved contradictory requests (citing the co-editor).
5. **Replication** — what changed in the package.

## Checklist

- [ ] Co-editor letter parsed; essential vs. optional points separated
- [ ] Every referee comment answered point-by-point (quote → response → location)
- [ ] Changes are in the paper and pointed to, not just promised
- [ ] Disagreements backed by analysis/citation, professional in tone
- [ ] Referee conflicts resolved via the co-editor's guidance
- [ ] Replication package updated for new exhibits; EEA membership current for resubmission
- [ ] Revision is focused (matches the fast-timeline norm), not sprawling

## Response-letter anatomy (per comment)

For each referee point, use the same three-move structure so the editor can verify your revision quickly:

1. **Quote** the comment verbatim (or faithfully paraphrased), numbered to match the referee.
2. **Respond** with exactly what changed and **where** — "We now estimate with Callaway–Sant'Anna (Table 3, Section 4.2, p. 14)" — or a respectful, evidence-backed reason for not changing.
3. **Point** to the specific new exhibit/passage so the editor need not hunt.

Open the letter with a short summary of the **major changes**, framed against the **co-editor's essential requests**, before the point-by-point.

## Worked vignette (illustrative)

Referee 1 wants a structural model; Referee 2 calls the existing model "overbuilt." The co-editor's letter says the empirical contribution is the draw and the model should stay light. The rebuttal follows the co-editor: it trims the model (citing Referee 2), explains to Referee 1 that a fuller structural treatment is a separate paper the editor agreed was out of scope, and points to the leaner model section. The contradiction is resolved by deferring to the controlling document, stated explicitly and politely.

## Anti-patterns

- Treating all comments as equal weight instead of following the co-editor's priority map
- Promising changes in the letter that are not actually in the revised paper
- Defensive or dismissive tone toward a referee (single-blind — they know you)
- Ignoring a contradiction between referees instead of resolving it via the co-editor
- Letting the replication package fall out of sync with new results
- Forgetting EEA membership is required again to resubmit
- A response letter that argues without pointing to the changed text

## Output format

```
【Co-editor essentials】[the binding requests]
【Major points】[referee → change → location]
【Minor points】[handled]
【Conflicts】[how resolved via co-editor]
【Replication】[package updated for new exhibits? Y/N]
【Membership】[submitting author EEA member for resubmission? Y/N]
【Next step】resubmit via the EEA portal
```
