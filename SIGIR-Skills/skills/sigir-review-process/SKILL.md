---
name: sigir-review-process
description: Use when reasoning about how SIGIR evaluates submissions — the per-track OpenReview machinery, double-blind full/short review versus single-anonymous Resources review, the PC-member nomination duty, what IR reviewers score (evaluation validity above novelty claims), the ACM Peer Review Policy layer, and how decisions land.
---

# SIGIR Review Process

SIGIR review is track-partitioned: each track (full, short, resources,
reproducibility, perspectives, industry, ...) runs its own OpenReview group with its
own reviewer pool, anonymity regime, and calendar. Advice that treats "SIGIR review"
as one process misroutes authors. This skill models the machinery and the reviewer
psychology; exact per-cycle mechanics (rebuttal windows, score scales, meta-review
forms) were not publicly verifiable for 2026 and must be read off your own
submission's OpenReview timeline (待核实).

## The machinery

| Element | What was verified for 2026 | What to confirm per cycle |
|---|---|---|
| Platform | OpenReview, per-track venue groups | Group id for your track |
| Full/short anonymity | Double-blind, fully anonymized | Preprint policy details |
| Resources anonymity | **Single-anonymous** (reviewers see authors) | — |
| Reviewer sourcing | Full-paper teams nominate one author as PC member per submission | Whether shorts/other tracks share the duty |
| Policy layer | ACM Peer Review Policy; automated compliance checks reserved | Cycle-specific screening tools |
| Decision structure | Not extractable | Rebuttal? meta-reviews? conditional accepts? |

The PC-nomination duty has a strategic edge authors miss: your nominated author will
review *other* SIGIR submissions during your own paper's review window. Nominate
someone senior enough to review credibly — chairs notice teams that nominate their
most junior author, and review quality is a community reputation signal.

## What SIGIR reviewers actually score

Across editions, IR reviewing culture weighs **evaluation validity** above almost
everything. The informal reviewer checklist, reverse-engineered from the field's own
methodology literature:

1. Is the comparison fair? (Tuned baselines, same collections, same qrels, same
   metric implementations.)
2. Are the differences real? (Paired significance tests, multiple-comparison
   handling, variance across seeds for neural systems.)
3. Is the metric-task pairing sound? (nDCG@10 for ad-hoc ranking, recall for
   first-stage retrieval, judged@k when pools are shallow.)
4. Does the mechanism explain the gain? (Ablations that isolate the claimed source.)
5. Only then: how novel is the idea, and how broadly does it matter?

The consequence: at SIGIR a modest idea with airtight evaluation routinely outscores
a bold idea with a shaky one. Papers written novelty-first, evidence-second read as
misrouted ML-venue submissions.

## Reviewer archetypes and what convinces each

- **The evaluation methodologist**: reads §Experiments first; convinced by protocol
  symmetry and correct statistics; enraged by copied baseline numbers.
- **The systems pragmatist**: asks what it costs; convinced by latency/index-size
  tables; suspicious of quality wins that ignore efficiency entirely.
- **The task veteran**: knows the collection's quirks and every prior result on it;
  convinced by correct positioning against the collection's known ceiling effects.
- **The user-focused skeptic**: asks whether the offline gain would survive contact
  with users; softened by honest scope statements about offline evaluation limits.

A submission cannot satisfy all four maximally in 9 pages; it must avoid *offending*
any of them (the four standing objections: unfair tuning, no significance testing,
metric mismatch, unexplained mechanism).

## Reading a decision packet

```text
Decision-packet triage
----------------------
1. Sort claims-about-your-paper into: factual error / evidence gap / scope dispute.
2. Factual errors -> correction with coordinates (if a channel exists; see
   sigir-author-response).
3. Evidence gaps named by >=2 reviewers -> real; plan the experiment, not the reply.
4. Scope disputes ("should have tested on X") -> decide if X is load-bearing for
   the claim as written; narrow the claim or add X, never argue taste.
5. Extract every "the authors should ..." into the next-version checklist verbatim.
```

## Reading scores like a chair

Without the cycle's exact scale (待核实), read *shapes* rather than numbers:

- **Converging middling scores** with the same named gap = a real, fixable defect;
  the packet is a work order.
- **High variance** (one champion, one detractor) = the paper's framing lets two
  archetypes read different papers; the fix is usually §1, not §5.
- **Uniform low confidence** = the submission landed outside the track's reviewer
  pool; re-read `sigir-topic-selection` before blaming reviewers.
- **A long, detailed negative review** is the most valuable object in the packet —
  it is the only reviewer who fully engaged; answer it with matching precision.

## Confidentiality and conduct

- Submissions are confidential under the ACM Peer Review Policy: reviewers must not
  share, reuse, or feed submissions to external services; authors likewise must not
  publicize reviewer text out of context.
- Attempting to identify reviewers, or contacting suspected reviewers about a live
  submission, is a conduct violation with career-scale downside in a community this
  small — every senior IR researcher reviews for SIGIR eventually.
- Suspected review misconduct (plagiarized review, LLM-generated boilerplate,
  conflict violations) goes to the track chairs through official channels only.

## After the decision

- **Accept**: conditional items (if any) become the first camera-ready tasks; see
  `sigir-camera-ready`.
- **Reject**: the packet is a specification for the next venue; the SIGIR-family
  calendar (next SIGIR, SIGIR-AP, ECIR, CIKM, WSDM) means a well-revised paper waits
  months, not a year — see `sigir-workflow` for the routing calendar.

## Output format

```text
[Track machinery] group id / anonymity regime / nomination duty satisfied
[Standing-objection audit] tuning-fairness / significance / metric-match / mechanism: pass-risk each
[Archetype exposure] which reviewer archetype the paper most risks offending
[Packet triage] factual errors <n> / evidence gaps <n> / scope disputes <n>
[Confidentiality flags] none / <issue to raise with chairs>
[Next move] respond / revise-for-<venue> / camera-ready
```
