---
name: ndss-author-response
description: Use when writing an NDSS rebuttal and working the interactive discussion phase — triaging Round-2 reviews under a short window, answering adaptive-attack and ethics objections with pointable evidence, and negotiating toward Accept or a well-scoped Minor/Major Revision.
---

# NDSS Author Response

Reaching the rebuttal at NDSS already means something: the early reject did not take you,
and the paper is in Round 2 with reviewers who will *talk back* — the 2027 process pairs
the written response with an interactive discussion phase (fall window: October 8-10,
2026). Plan for a conversation, not a single volley.

## Triage first (day one of the window)

Sort every review point into four buckets before writing a sentence:

| Bucket | Test | Response strategy |
| --- | --- | --- |
| Misreading | The paper already answers it | Quote section/figure; ask implicitly "what would make this clearer?" |
| Real gap, small | Answerable with existing data or a quick run | Present the number now; offer the camera-ready edit |
| Real gap, large | Needs new experiments/implementation | Do not fake it — scope it as revision work; this is Major-Revision fuel, used well |
| Judgment call | Reviewer weighs the contribution differently | One respectful paragraph on why the framing holds; then stop |

Answer *every* reviewer, but spend the word budget where the decision is live: the
skeptical-but-engaged review, not the enthusiast or the write-off.

## Rules of engagement

- **Point, don't reargue.** "Table 3, row 4 reports the adaptive variant: success drops to
  X% at cost Y" beats three paragraphs of prose. Every claim in the response should have a
  coordinate in the paper or a concrete new number.
- **New results are allowed to be small.** A single clarifying experiment run during the
  window, honestly labeled, moves discussions; a promised future experiment moves nothing.
- **Concede precisely.** "Correct — our measurement cannot distinguish A from B; we will
  weaken §5.2's claim accordingly" earns trust that the contested points then spend.
- **Stay anonymous and in-channel.** The response lives in HotCRP, double-blind rules
  still apply, and no external links that could fingerprint the authors.

## The objections this venue actually raises

**"An adaptive attacker bypasses this."** The highest-frequency defense-paper objection.
If the paper evaluated adaptation (`ndss-experiments`), point to it. If the reviewer's
specific strategy is genuinely new: analyze it in the response — capability check against
the threat model, then either an argument or a quick measurement. Never answer with "out
of scope" unless the threat model *already* excluded that capability in the submitted PDF.

**"The ethics handling is insufficient."** Respond with facts and dates, not reassurance:
disclosure sent ⟨date⟩, vendor acknowledged ⟨date⟩, scan rate-capped at ⟨rate⟩ with opt-out
honored, data handling per §Ethics. If the process moved since submission (a patch shipped,
an advisory published), say so — it is among the few post-deadline facts reviewers welcome.

**"Prevalence is overstated."** Restate the population definition and validation, give the
error directions, and if the reviewer is right that the sampled frame limits the claim,
propose the exact weakened sentence for the camera-ready.

**"Delta over [X] is thin."** Answer at the mechanism level (layer, precondition,
adversary), in two sentences, with a citation coordinate. Novelty debates are lost by
volume and won by specificity.

## Working the interactive discussion

The discussion phase rewards responsiveness: short turnaround, direct answers, no
repetition of the written response. If a reviewer proposes a compromise reading ("the
claim holds for provider-side deployments only"), engage with it seriously — discussions
often converge on the Minor/Major Revision boundary, and a well-received author who
scopes revisions crisply lands on the better side of it.

## Skeleton

```text
Thank-you line (one, no flattery).

COMMON THREADS (if ≥2 reviewers share an objection)
  T1: <objection> → answer once, pointable evidence, camera-ready commitment.

REVIEWER A
  A1 (misreading): see §4.1 ¶2 and Fig. 5; we will foreground this in §1.
  A2 (small gap): ran the suggested configuration — result R; added to Tab. 2.
REVIEWER B
  B1 (adaptive strategy S): S requires on-path capability; threat model §2
    excludes it — but under S' (off-path variant) success is X% (new run).
  ...

REVISION OFFER (one block, scoped)
  We commit to: [list]. We will not: [list, with one-line reasons].
```

## Failure modes

Rebuttals that rewrite the paper's argument from scratch; word budgets burned on the
strongest review; sarcasm at a misreading (misreadings are data — see
`ndss-review-process`); promising in the response what the revision cannot deliver, which
converts a winnable Major Revision into a failed one at re-review.

## Output format

```text
[Bucket map] each review point → misreading / small gap / large gap / judgment
[Live decision] which reviewer(s) the response must move, and with what
[New evidence] runs completed inside the window + where they land in the paper
[Revision offer] committed items vs declined items with reasons
[Discussion posture] open questions expected; owner for fast replies
```
