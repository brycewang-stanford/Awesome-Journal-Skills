# SkillOpt behavioral judge rubric (0–100)

The judge scores **an answer produced by a rollout agent** to a held-out
researcher query, against that query's **ground-truth fact sheet**. The judge sees
the answer and the ground truth, but **not** the skill text and **not** which skill
version produced the answer.

This rubric deliberately rewards none of the things the static scorecard already
covers (length, headers, presence of a checklist). It rewards exactly one thing:
**did this answer correctly and usefully serve the researcher?**

## Dimensions

### 1. Factual correctness — 35 pts
Every checkable claim matches the ground-truth fact sheet.
- Start at 35. Subtract **12 for each wrong fact** stated as true (e.g. naming the
  wrong submission portal, an out-of-band word limit, the wrong Bluebook edition).
- Subtract 4 for each claim that is true but materially imprecise.
- A confidently-stated wrong fact is the worst failure mode; do not floor gently.

### 2. Actionable specificity — 25 pts
The answer gives the concrete number / step / threshold the researcher can act on,
not a pointer to "go check the page" when the fact is in fact stable and verified.
- Full marks: states the operative numbers and the exact next action.
- Heavy penalty: deflects a *stable, verifiable* fact to "confirm on the official
  page" (false humility that strands the user).
- Distinguish from §5: deflecting a genuinely *volatile* fact is correct, not a
  specificity failure.

### 3. Need coverage — 20 pts
Does the answer address what this query actually requires — including problems the
researcher did **not** know to ask about?
- Full marks: surfaces the latent issue (e.g., an over-length manuscript, a missing
  anonymization step) even when the user's question did not name it.
- Penalty: answers the literal question while letting the user walk into a
  rejection the skill should have caught.

### 4. Venue specificity — 10 pts
The answer is true of **this venue**, not generic journal or generic law-review
boilerplate. Full marks reflect facts that would be wrong at a peer venue.

### 5. Calibrated hedging — 10 pts
Flags genuinely volatile items (current intake volume, exact open dates, fees) for
live confirmation, **without** hedging stable verified facts into mush.
- Full marks: confident on the stable, explicitly live-check on the volatile.
- Penalty both ways: hedging the stable (see §2) **and** stating a volatile,
  turnover-prone detail as a fixed fact.

## Output contract

The judge returns strict JSON:

```json
{
  "scores": {"factual": 0, "specificity": 0, "coverage": 0, "venue": 0, "hedging": 0},
  "total": 0,
  "wrong_facts": ["..."],
  "missed_needs": ["..."],
  "strengths": ["..."],
  "one_line_verdict": "..."
}
```

`total` must equal the sum of the five dimensions (max 100). `wrong_facts` and
`missed_needs` are the reflection signal the optimizer turns into bounded edits.
