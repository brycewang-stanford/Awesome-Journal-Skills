---
name: rt-submission-readiness
description: Use right before submitting — run a venue-parameterized go/no-go scorecard on the author's own manuscript (fit, identification, robustness, exhibits, exposition, venue mechanics, data/code, pre-empted objections). Returns PASS/FLAG/FAIL per dimension, the blocking gaps, and the desk-reject risk. Reads the venue bar from the target pack + source-map.
---

# Submission-Readiness Self-Check (rt-submission-readiness)

The mechanical/structural go/no-go that catches avoidable desk rejects before you hit
submit. Full rubric:
[`shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md).
It is the outward-facing analogue of the repo's internal `tools/quality_scorecard.py`.

## When to trigger

- The draft is "done" and the author is about to submit to a named venue.
- Before paying a submission fee / starting the portal.

## What it does

Reads the target pack's skills + `resources/official-source-map.md`, inspects the actual
manuscript (cite §/table for every flag), and scores nine dimensions PASS / FLAG / FAIL:

1. Fit & general interest · 2. Contribution clarity · 3. Identification / method ·
4. Robustness & inference · 5. Exhibits self-contained · 6. Exposition (magnitude up front)
· 7. Venue mechanics (page limit / anonymization / fee / cover letter) · 8. Data & code /
reproducibility · 9. Pre-empted referee objections.

**Go/no-go:** any FAIL on Fit, Identification, or Venue-mechanics is a no-go (the classic
desk-reject triggers).

## Hard rules

1. **Read the manuscript; cite locations** — no status without a §/table/page reference.
2. **Venue facts live from the source-map**, never from memory.
3. **No false green** — unverifiable dimension → `UNKNOWN`, not PASS.
4. **Map every FAIL/FLAG to the owning skill** (and its execution bridge) so the author
   knows exactly where to fix it.

## Output format

```
【Venue】… (bar: pack skills + source-map, read live)
【Scorecard】1 Fit … PASS/FLAG/FAIL — note (§ cited) · … (dims 2–9)
【Go / No-go】GO / NO-GO — deciding dimension(s)
【Blocking gaps (FAIL)】ranked; each with the fix + owning skill
【Will-be-pushed (FLAG)】referee-anticipation list
【Desk-reject risk】low / medium / high — why
```

Next: if readiness passes, `rt-simulated-referee` for the substantive adversarial review.
