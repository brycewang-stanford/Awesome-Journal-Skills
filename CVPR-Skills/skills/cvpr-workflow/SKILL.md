---
name: cvpr-workflow
description: Use when planning a CVPR submission campaign end to end, covering the November abstract/paper/supplement deadline chain, coauthor reviewer-duty scheduling, the January rebuttal sprint, February decisions, camera-ready and June conference logistics, and the resubmission ladder across ICCV, ECCV, and the next CVPR.
---

# CVPR Workflow

CVPR is an annual machine with one intake: for CVPR 2027, paper registration November
10, 2026, papers November 16, supplements November 23, rebuttal January 25 – February 1,
2027, decisions February 25, conference June 20–24, 2027 in Seattle (the 2026 cycle ran
November 6 / 13 / 20, 2025 to a June 3–7 Denver meeting). This skill turns that spine into a
project plan with owners, because CVPR deadline weeks are lost to coordination
failures more often than to science failures.

## Campaign calendar (CVPR 2027 dates, re-verified 2026-11-24)

| When | Milestone | Owner discipline |
|---|---|---|
| T–10 weeks (early Sep) | Freeze scope: claims, benchmarks, baselines | PI + first author sign one paragraph |
| T–8 weeks | Experiment matrix running; recipe ledger live | Every table row has a config |
| T–6 weeks | First full draft; flip-test the figures | Co-authors annotate, don't rewrite |
| T–4 weeks (early Oct) | OpenReview profiles audited for every author | One named owner; new coauthors close the list |
| T–1 week (Nov 10, 2026) | **Paper registered; profiles + enrollment complete; quotas checked** | Desk-reject exposure if missed; author list frozen |
| Nov 16, 2026 | **Paper (with LLM Usage Statement) submitted** | Freeze 24h early; upload before the panic hour |
| Nov 23, 2026 | **Supplement uploaded** | Videos/code packaged per `cvpr-supplementary` |
| Dec 14, 2026 – Jan 8, 2027 | Coauthors deliver their assigned reviews | Late reviews endanger *your* paper |
| Jan 25 – Feb 1, 2027 | Reviews land; one-page rebuttal | Pre-book this week; nobody travels |
| Jan 25 – Feb 5, 2027 | Reviewer responses and AC–reviewer discussion | Resist mailing the AC |
| Feb 25, 2027 | Decisions (Main or Findings Track) | Both branches pre-planned |
| Spring (待核实) | Camera-ready + dataset release due | See `cvpr-camera-ready` |
| Jun 20–24, 2027 | Conference (workshops 20–21, main 22–24) | Poster/talk/travel logistics |

## The two windows people fail to defend

**Deadline fortnight (early November).** The supplement trailing the paper by a week
tempts teams to leave packaging "for week two" — then week two evaporates into video
rendering and code scrubbing. Rule: the supplement plan (what goes in, who builds it)
is written *before* the paper deadline; week two only executes it.

**Rebuttal week (late January).** Seven days, one page, all reviewers at once. Assign
roles when reviews drop, not after a day of group grief:

```yaml
# rebuttal-roles.yaml — filled within 12 hours of review release
reader:        # summarizes all reviews neutrally, one page, no rebuttals yet
runner:        # owns the 1-2 small requested experiments; hard stop at day 5
writer:        # owns the single page; everyone else feeds bullets
adjudicator:   # PI decides which objections get space, which get one line
deadline:      # internal freeze 24h before OpenReview close
```

## Reviewer duty as a planned workload

Submitting enrolls qualifying authors into a 25k-reviewer pool, and undelivered or
irresponsible reviews — including uploading a submission to an external LLM — can
desk-reject every paper the offender authored (verified 2026 and 2027 policy). Treat December–January reviewing as a scheduled deliverable: at
submission time, list which coauthors are likely reviewers, block their calendar for
review weeks, and have the group's senior authors sanity-check first-time reviewers'
drafts against the official reviewer guidelines.

## Multi-paper coordination

Most labs submit several papers into the same November wall, which multiplies the
process risks nonlinearly:

- **Shared coauthors, shared exposure**: one person's undelivered January review
  endangers every paper they touch; the duty ledger must be lab-level, not
  paper-level.
- **Conflict hygiene**: OpenReview conflicts must be complete across all submissions;
  a stale institution on one profile pollutes assignments for the whole batch.
- **Compute contention**: rebuttal-week reserve GPU allocations collide when three
  papers each promised "small requested experiments"; pre-negotiate priority order.
- **Internal review**: schedule lab-mates' cross-reads at T–10, not T–2 — at T–2
  everyone is defending their own draft.

## The resubmission ladder

At a 25.42% acceptance rate, the rational plan covers rejection before it happens. The
CV calendar offers a clean ladder — CVPR (Nov) → ICCV (spring deadline, odd years) /
ECCV (spring deadline, even years) → WACV/3DV or back to CVPR. Rules for climbing:

- Bank the reviews: fix every factual objection before the next deadline; reviewer
  pools overlap across CVF venues and repeat objections read badly (triage method in
  `cvpr-review-process`).
- Mind the dual-submission windows: the CVPR attestation covers Nov 16, 2026 – Feb 22,
  2027 for CVPR 2027 (Nov 13 – Feb 20 in 2026); the next venue's window must not overlap
  a paper still under CVPR review.
- Re-check freshness: three months of arXiv can obsolete a comparison table; budget a
  baseline-refresh pass, not just an edit pass.

## Deadline fortnight, day by day

The last two weeks compress badly when run ad hoc. A schedule that has survived
contact with real teams:

- **T–14 to T–10**: results freeze for the main table. New numbers after this go to
  the supplement or the rebuttal, not the body.
- **T–10 to T–7**: full-draft pass; run the figure flip test with an outsider; final
  baseline-freshness check against the leaderboard.
- **T–7 (abstract day)**: register the abstract, verify every profile renders as
  complete when logged out of the authors' accounts, lock the author list.
- **T–6 to T–3**: claim-calibration pass (`cvpr-writing-style`), bibliography venue
  verification (`cvpr-related-work`), LLM Usage Statement drafted and checked for
  anonymity.
- **T–2**: full mechanical sweep from `cvpr-submission`; internal freeze.
- **T–1**: upload; re-download; cold read. Nobody edits after upload day.
- **T to T+7 (supplement week)**: execute — do not design — the supplement plan;
  identity-scan code and videos; upload at T+5, not T+7, to survive a failed render.

## Cycle-status note

As of 2026-11-24, the CVPR 2027 call (Seattle, June 20–24, 2027) is published and its
submission window has closed; the dates above are CVPR 2027's. No later edition is
announced — for the next cycle, reopen cvpr.thecvf.com the moment your team commits,
because the deadline chain and requirements (the 2026 Compute Reporting Form, the 2027
LLM Usage Statement and quotas) change between editions.

## Output format

```text
[Campaign stage] scoping / building / deadline-fortnight / in-review / rebuttal / decided
[Calendar] next 3 milestones with dates and owners
[Duty ledger] reviewing coauthors + calendar blocked: yes/no
[Risk register] top 3 (missed-profile, supplement drift, rebuttal roles, …)
[Plan B] next venue + its verified deadline
[Cycle check] current-year pages reopened on: <date>
```
