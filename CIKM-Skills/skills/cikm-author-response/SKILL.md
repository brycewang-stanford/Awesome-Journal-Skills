---
name: cikm-author-response
description: Use when preparing author-side communication around CIKM reviews — drafting for a response window if the cycle offers one (unconfirmed for 2026), writing camera-ready revision notes that answer reviewer concerns, handling post-decision chair correspondence, and converting rejection reviews into a resubmission brief.
---

# CIKM Author Response

CIKM's response mechanics are genuinely cycle-dependent: no official statement
confirming or denying a 2026 rebuttal phase could be retrieved (source map,
2026-07-08, 待核实). This skill therefore covers all four author-side writing
situations around CIKM reviews, with the no-window case treated as the default —
because when there is no rebuttal, the reply to reviewers gets written anyway, just
in different documents.

## Situation map

| Situation | The document you actually write | Governing constraint |
|---|---|---|
| A response window opens | Anonymous reply inside EasyChair | Announced word/format rules; anonymity persists |
| No window, paper accepted | Camera-ready revision note | Address concerns without exceeding accepted scope |
| No window, paper rejected | Resubmission brief for the next venue | Honest triage, no venue-blaming |
| Factual process error | Confidential note to PC chairs | Facts only; never argue merit this way |

## If a window opens: the tri-lane reply

CIKM reviews arrive from up to three community lanes (`cikm-review-process`), so a
good reply is organized by reviewer, not by theme — each lane's reviewer should find
their own objection answered in their own vocabulary:

1. Lead each reviewer block with the concern that most threatens *their* score, not
   the one easiest to rebut.
2. Answer from submitted material — section, table, appendix, or the artifact the
   paper already cites. New results pasted into a reply carry no weight a reviewer
   is obliged to credit and can violate window rules; check the announcement.
3. Concede real limits in one sentence and scope them ("holds for static graphs;
   streaming is future work") — the blended pool punishes evasion harder than
   limitation, because at least one reviewer is expert enough to see through it.
4. Preserve anonymity end to end: no names, no identifying URLs, no "as our earlier
   system at [company]" slips. The double-blind regime does not lapse at review.

## Micro-example: the mining-lane scalability objection

> Reviewer: "Complexity analysis suggests quadratic blow-up on dense graphs; the
> experiments avoid this regime."

Reply skeleton: (a) confirm the reading is correct for worst-case density; (b) point
to the submitted Table/appendix entry showing observed scaling on the densest tested
graph; (c) state the density regime of the target application and that the claim is
scoped to it; (d) offer a one-sentence camera-ready scope clarification. Four moves,
no new experiments, no evasion.

## No window, accepted: the revision note

The August 7 → August 20 camera-ready sprint (2026 dates) is where reviewer concerns
get answered in practice. Build a concern → edit ledger: every substantive review
point maps to a camera-ready change, a scoped-limitation sentence, or a reasoned
no-change. Keep the ledger; if the proceedings process or a chair asks what changed,
the answer is ready, and `cikm-camera-ready` consumes it directly.

## No window, rejected: the resubmission brief

Write it within a week, while context is fresh:

- Sort review points into: fix-with-evidence, fix-with-writing, disagree-with-reason.
- Tag each point by reviewer lane — lane-clustered objections identify which
  community the paper failed, which drives the `cikm-workflow` fallback choice.
- Draft the one paragraph a future reviewer at the next venue would need to see
  changed. If that paragraph cannot be written, the problem is the contribution,
  not the venue.

## Tone calibration for a three-community room

CIKM's communities have different argument cultures — IR discussion leans
protocol-precise, mining leans delta-and-numbers, KM/database leans
systems-pragmatic — but one register works for all three: technical, specific,
and unwounded. Practical rules:

- Quote the reviewer's actual words before answering them; paraphrase invites
  "that is not what I said."
- Numbers over adjectives: "Table 3 row 4 shows 2.9 points at k=10" persuades
  every lane; "we respectfully believe the improvement is substantial" persuades
  none.
- Never grade the reviewer ("the reviewer misunderstands...") — write "the
  submission states this compactly in §4.2; we will make it explicit" and let the
  evidence do the accusing.
- Budget by leverage: one blocking objection answered completely beats five minor
  points each answered at 20%.

## Verify-before-writing checklist

Response mechanics are exactly the kind of fact this venue changes per cycle, so
before drafting anything reviewer-facing:

```text
[ ] Reopen the current cycle's author instructions / notification email:
    does a response channel exist at all this year?
[ ] If yes: word/character limit, format, deadline (AoE?), and whether
    new results or links are permitted or barred
[ ] Anonymity rules during the window (assume double-blind persists)
[ ] Who may submit: contact author only, or any author?
[ ] For chair notes: the stated contact route on the host site, not a
    guessed email address
```

Every item comes from the current host site or EasyChair instance — the 2026
source map deliberately records the rebuttal question as unresolved (待核实), and
this checklist is how it gets resolved for whatever cycle is live.

## The one-page ceiling

Whatever the channel — window reply, camera-ready note, or chair correspondence —
hold to roughly a page of substance per audience. Beyond that length, the reader
is skimming, and a skimmed concession does as much damage as an unmade one. If
the honest response needs three pages, the paper had three pages of problems;
choose the one whose resolution changes the decision and spend the page there.

## Output format

```text
[Situation] response-window / camera-ready note / resubmission brief / chair note
[Per-reviewer leads] <R1/R2/R3: the concern each block opens with>
[Evidence anchors] <submitted section/table/artifact per concern>
[Concessions] <scoped limits admitted, in one line each>
[Deliverable deadline] <window close / Aug-20-style camera-ready gate / next venue gate>
```
