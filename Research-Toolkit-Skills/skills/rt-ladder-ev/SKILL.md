---
name: rt-ladder-ev
description: Use when choosing between submission sequences rather than between single venues — "should I try the top journal first, or start one rung down?", or when a tenure/job-market clock makes time-to-print the binding constraint. Costs a resubmission ladder in months and in probability of ever placing, using each venue's own turnaround and desk-reject figures. Follows rt-journal-match, which produces the ladder this one prices.
---

# Ladder Expected Value (rt-ladder-ev)

`rt-journal-match` returns a shortlist and an order. This answers the question that
order implies but never states: **what does that sequence cost?**

Authors compare venues one at a time — *is JF worth a shot?* — and the answer is almost
always yes in isolation. The cost only appears in the sequence. Trying two long shots
before a realistic venue is not a slightly worse plan than skipping them; on typical
finance turnarounds it is nine extra months for perhaps three extra points of placement
probability. Nothing else in this repository made that trade visible, so it was decided
by optimism.

## When to trigger

- Two candidate submission orders and no principled way to choose.
- A clock: job market, tenure case, grant report, a co-author's graduation.
- A paper that has already been rejected twice and needs the remaining ladder costed.
- Someone asks "is it worth trying X first?" — that is a sequence question.

## What it needs

The [`paper-profile.yml`](../../../shared-resources/journal-selection/paper-profile.md)
(for `ambition`, `constraints.clock`, `history`) plus, **for each rung**, three numbers:

| Input | Where it comes from |
|---|---|
| months to first decision | the venue's `resources/official-source-map.md` — live-checked, never from memory |
| desk-reject / acceptance rate | same source map, same rule |
| `p_accept` for **this** paper | your judgement, conditioned on the paper — see below |

**`p_accept` is not the published acceptance rate.** A venue's 6% is computed over a
submission pool that includes everything sent to it. A clean design with a
general-interest result is not a random draw from that pool, and neither is a thin one.
Start from the published rate, then move it with the venue's own
`*-topic-selection` fit judgement and `rt-desk-reject-risk` output, and say which way you
moved it and why.

## What it does

```bash
python3 tools/ladder_ev.py \
    --rung "Journal of Finance:0.05:4.5" \
    --rung "Review of Financial Studies:0.08:5.0" \
    --rung "JFQA:0.20:3.5" \
    --rung "Journal of Banking and Finance:0.35:2.5"
```

Walks the ladder top-down carrying the probability the paper is still unplaced, and
returns: time until the ladder resolves, time to print conditional on placing, the
probability of placing at all, and — the number that changes minds — the probability of
running the ladder out and having nowhere left to go.

Then run the alternative sequence and compare. The comparison is the deliverable, not
either number on its own.

## Hard rules

1. **Turnaround and acceptance figures come from the source map, read at the time of
   use.** They are volatile; this skill stores none of them.
2. **Report the band, not the point.** `p_accept` is a judgement, so the tool prints a
   ±40% sensitivity band by default. **If two ladders' bands overlap, say they are
   indistinguishable** — do not rank them anyway on the third decimal place.
3. **A ladder with no floor is not a plan.** If the probability of exhausting the ladder
   exceeds ~25%, the shortlist is missing a credible home; go back to
   `rt-journal-match` for a safe rung rather than reporting a number.
4. **Never present the output as a forecast.** It is arithmetic over stated assumptions.
   State the assumptions next to the answer.

## Output format

```
【Ladder A】V1 → V2 → V3   resolves in N months · places P% · exhausts E%
【Ladder B】V2 → V3        resolves in N months · places P% · exhausts E%
【Difference】what B buys or costs vs A, in months and in placement probability
【Sensitivity】whether the difference survives the ±40% band
【Assumptions】each p_accept, and why it differs from the published rate
【Recommendation】which sequence, and the one fact that would change it
```

## Anti-patterns

- Using published acceptance rates as `p_accept` — that is the pool's number, not the
  paper's.
- Costing a ladder whose rungs were never checked for fit; a fast rung that will desk-
  reject the paper on scope is not a rung. Run `rt-journal-match` first.
- Optimising time-to-print alone. A worse-placed paper can cost more career-years than
  the months it saved — `ambition` in the profile is what balances that, and it belongs
  in the write-up.
- Reporting one decimal place of expected months as though it were measured.

---
*Follows [`rt-journal-match`](../rt-journal-match/SKILL.md) (which builds the ladder) and
[`rt-venue-reframe`](../rt-venue-reframe/SKILL.md) (which prices the rewrite each rung
needs). Method: [`journal-match.md`](../../../shared-resources/journal-selection/journal-match.md)
step 6.*
