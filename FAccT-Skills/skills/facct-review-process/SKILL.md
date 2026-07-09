---
name: facct-review-process
description: Use when reasoning about how an ACM FAccT submission is evaluated — mutually-anonymous review by a mixed CS+law+social-science pool matched via author-selected focus areas, Area Chairs, the short factual-correction rebuttal, the new Accept/Revise/Reject decision with a revise-and-resubmit round, and how FAccT's interdisciplinary process differs from a pure-ML conference's single-shot rebuttal.
---

# FAccT Review Process

Model the pipeline before interpreting any single review. FAccT's process has two features that
surprise authors arriving from a pure-ML venue: the reviewer pool is **interdisciplinary** (a
computer scientist, a lawyer, and a social scientist may all be assigned), and — new for the 2026
edition — the decision set is **Accept / Revise / Reject**, where **Revise** is a genuine
revise-and-resubmit round, not a soft reject. Your paper is matched to reviewers and **Area Chairs**
by the **focus areas** you selected at registration, so those choices shape who reads you as much as
your title does.

## Process model

- Submission and review run on **OpenReview** (new for 2026) with **mutual anonymity**: authors and
  reviewers are hidden from each other.
- Papers are matched to reviewers and **Area Chairs** by **disciplinary focus area**, so an
  interdisciplinary paper is typically read by people from more than one field — a strength and a
  risk (each expects their lane's rigor).
- Reviewers weigh **relevance** to the conference and the chosen area, and **quality and clarity** —
  correctness, depth of exposition (how well you contextualize approach, methodology, perspective,
  and domain), and an honest evaluation of **both strengths and limitations**.
- After preliminary reviews, a **short rebuttal** window lets authors correct **factual errors and
  misunderstandings** and signpost minor edits — it is not for re-arguing substantive disagreement.
- **Area Chairs** synthesize reviews into a recommendation: **Accept**, **Revise**, or **Reject**.
  **Revise** papers address AC-prioritized concerns by the revision deadline and are **re-reviewed**
  before a final decision.
- Accepted papers are **archival ACM proceedings** (or non-archival by author choice) and are
  **presented in person**.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and rigor hold; minor polish only | Camera-ready; do not reopen scope |
| Revise | Repairable gaps: a missing disaggregation, an under-argued harm, a construct concern, a thin cross-lane engagement | Treat as an R&R: address each AC-prioritized concern, evidenced, by the deadline |
| Reject | Structural: not FAccT-shaped, harm claim unsupported, one-discipline paper misrouted | Reframe or reroute (NeurIPS/ICML/CHI/AIES/law), do not lightly resubmit unchanged |

The strategic reading: write the initial submission so that whatever is weakest is **fixable inside
the revision window** (an analysis you can add, a limitation you can bound, a construct you can
validate) rather than **structural** (a study design or a venue-fit problem you cannot repair in
weeks). The 2026 process is built to reward repairable papers.

## The interdisciplinary reviewer reality

Expect readers from different fields, matched by your focus areas. A fairness-methods reviewer
checks your metrics, baselines, and disaggregation; a legal reviewer checks whether you use the
doctrine correctly; a qualitative reviewer checks your coding, reflexivity, and treatment of
participants. The common failure is a paper strong for one and naive to another — so **answer each
reviewer on the axis they raised**, and do not dismiss a cross-lane objection as "not my field": at
FAccT it is precisely the point.

## Where author leverage actually exists

```text
[Before submission]  focus-area selection -> which disciplines review you   (largest lever)
[Rebuttal]           factual corrections and misreadings only; not a debate
[Revise round]       the strongest lever: address each AC-prioritized concern with concrete changes,
                     re-read before the final decision
[After reject]       no appeal; reroute to a sibling venue or the CRAFT track, or resubmit next cycle
```

A rebuttal moves borderline papers when it fixes a factual misreading a reviewer built an objection
on; it does not move papers when it argues taste. In the Revise round, an **unaddressed
AC-prioritized concern** — neither fixed nor explicitly and reasonably declined — is what turns the
re-review against you.

## Reading a review packet

Weight reviews before answering. A review that engages your subgroup tables, your codebook, or the
specific doctrine was read closely and will be read closely again — that reviewer is your likely
advocate if the revision holds. A review from an adjacent discipline that raises a framing or harm
concern is not noise; it is the interdisciplinary check the venue exists for, and the Area Chair
will weight it.

## Misreadings to avoid

- **Treating Revise as a guaranteed accept** — the re-review is real; budget the short window like a
  deadline.
- **Treating the rebuttal as the revision** — the rebuttal is for factual corrections; substantive
  fixes belong in the Revise round.
- **Dismissing the out-of-field reviewer** — the mixed panel is the design, not an accident.
- **Projecting a pure-ML process** — FAccT is not single-shot accept/reject; and the Revise round,
  OpenReview, and rebuttal specifics are 2026-new, so re-confirm them each cycle.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / revise / final / accepted
[Decision category] accept / revise / reject, with the criterion driving it
[Criterion map] each review point -> relevance | correctness | depth | strengths-and-limits | discipline
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / arguing taste in rebuttal / ignoring the out-of-field reviewer
```
