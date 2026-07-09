---
name: itcs-author-response
description: Use to operate under the reality that ITCS has no rebuttal or author-response phase — pre-empting reviewer objections inside the submission, then handling the post-decision situation (camera-ready window on accept, or rerouting and reusing the reviews on reject) since there is no revise-and-resubmit.
---

# ITCS Author Response

The defining fact of this skill: **ITCS has no rebuttal and no author-response phase.** Following
theory-conference norms, the program committee forms its reviews and reaches accept/reject
**without any input from you** in between (see
[`itcs-review-process`](../itcs-review-process/SKILL.md)). There is also **no Major Revision** and
no revise-and-resubmit. So "author response" at ITCS is not a rebuttal-writing task — it is
(1) doing the rebuttal's *work* inside the submission, before the deadline, and (2) handling the
situation after the decision lands. Both are covered here.

## Part 1 — The rebuttal you write in advance (in the paper)

At a rebuttal venue you would hold arguments in reserve to answer reviewers. At ITCS there is no
reserve turn, so every such argument must be *in the submitted PDF*. Pre-empt the three objections
an ITCS PC reliably raises:

- **"Is the model trivial or all-powerful?"** Answer with an **anchoring result** in the
  introduction — a separation or surprising possibility showing the model is neither empty nor
  everything (see [`itcs-writing-style`](../itcs-writing-style/SKILL.md)).
- **"Is this actually new?"** Answer with a **delta-first related-work** paragraph naming the
  closest prior model and what it did *not* ask; search the ITCS/ICS back-catalog hardest, since
  that is where "already asked" hides (see [`itcs-related-work`](../itcs-related-work/SKILL.md)).
- **"Why should the community care?"** Answer with a concrete **payoff** — a connection, a
  reframing, an application sketch — on the first page.

Also disarm the objections you *can* foresee about your own paper:

- **State scope and limitations yourself.** A candidly owned gap is a strength at ITCS; the same
  gap discovered by a reviewer, with no rebuttal to contextualize it, is a weakness.
- **Prove the load-bearing lemma in full**, in the PDF's appendix — a reviewer who gets stuck on a
  deferred proof cannot ask you to clarify (see
  [`itcs-reproducibility`](../itcs-reproducibility/SKILL.md)).
- **Add a "why not the obvious approach" remark** where a reviewer might think your problem is
  easy; this is the single most common unspoken objection to a new-model paper.

## Part 2 — After the decision

### On accept

- Move to [`itcs-camera-ready`](../itcs-camera-ready/SKILL.md): switch to `lipics-v2021`,
  de-anonymize, complete LIPIcs metadata, hit the production deadline.
- **Reviews may still contain requests or corrections** even without a rebuttal round. Fold
  reasonable fixes into the camera-ready — a corrected claim, a missing citation, a clarified
  definition — using the extra latitude the (unlimited) LIPIcs length allows.
- Register a presenter; consider a **Graduating Bits** talk if a coauthor is near graduation.

### On reject

There is **no resubmission to a later ITCS round this year** (single annual cycle), so the move is
to *use* the reviews, not to answer them:

- **Mine the reviews for the real objection.** Since they were written without expecting a reply,
  they tend to be candid. Identify whether the paper was judged *not novel enough* (a framing
  problem) or *not correct/complete* (a proof problem) — the fix differs sharply.
- **Reroute by the diagnosis.** If reviewers admired the depth but not the novelty, a depth venue
  (STOC/FOCS/SODA) may fit; if they doubted the novelty of the *question*, rethink the framing
  before resubmitting anywhere (see [`itcs-topic-selection`](../itcs-topic-selection/SKILL.md)).
- **Fix proof gaps before the next submission**, and update the arXiv/ECCC/ePrint full version so
  the durable record is correct.
- **Do not email the PC to argue the decision.** There is no appeal-by-rebuttal culture; a polite
  clarifying question to the chairs is the ceiling, and rarely changes an outcome.

## What "author response" is NOT at ITCS

| Not this | Because |
|---|---|
| A rebuttal document answering reviewers | There is no author-response phase |
| A point-by-point response letter | There is no Major Revision / R&R round |
| A second submission to a later round | ITCS runs one annual cycle |
| An appeal to overturn a reject | No appeal-by-rebuttal culture; reroute instead |

## Output format

```text
[ITCS response mode] pre-submission pre-emption / post-accept / post-reject
[Pre-emption] anchoring result? novelty delta? payoff? scope owned? load-bearing proof in PDF? (yes/no each)
[Post-accept] camera-ready fixes folded in? presenter registered? Graduating Bits considered?
[Post-reject] objection diagnosed (novelty vs correctness)? reroute target? full version corrected?
[Next action] <single clearest step>
```
