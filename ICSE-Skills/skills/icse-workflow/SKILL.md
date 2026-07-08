---
name: icse-workflow
description: Use when planning an ICSE research-track campaign end to end, covering the single-cycle calendar from the June abstract deadline through September response, October decisions, the November revision sprint, artifact evaluation, camera-ready, and the April conference, plus rerouting timelines after rejection.
---

# ICSE Workflow

An ICSE campaign is a ten-month pipeline with one entrance. The 2027 cycle
(checked 2026-07-08 against the official dates pages) runs a **single
submission cycle** — a change from the two-cycle 2025/2026 model — so a missed
June deadline costs a full year, and the calendar below is the whole game.

## The 2027-cycle master calendar

| Date (all AoE where applicable) | Milestone | Your workstream |
|---|---|---|
| Jun 23, 2026 | Abstract (mandatory) | Real title + abstract frozen |
| Jun 30, 2026 | Full paper deadline | 10+2 IEEE PDF, artifact link live |
| Jul–Aug 2026 | Reviews written | Prepare response infrastructure; rest |
| Sep 2026 | Author response window | Criterion-mapped replies (`icse-author-response`) |
| Oct 20, 2026 | Decisions: Accept / Major Revision / Reject | Branch: celebrate / sprint / reroute |
| Nov 17, 2026 | Major Revision due | Four-week revision sprint |
| Dec 18, 2026 | Final MR decisions | Terminal for the cycle |
| Early 2027 (待核实) | Artifact evaluation window | Badge submission (`icse-artifact-evaluation`) |
| 待核实 | Camera-ready due | +1 page allowance, IEEE production |
| Apr 25 – May 1, 2027 | ICSE in Dublin (core Apr 28–30) | Talk, artifact, networking plan |

Artifact-evaluation and camera-ready dates for 2027 were not posted at check
time; the 2026 edition ran artifact registration/submission in early January,
which is the planning anchor until real dates appear.

## Working backward from June 30

A credible empirical-SE paper cannot be compressed into deadline month, because
its long poles — subject recruitment, benchmark construction, multi-week tool
runs, qualitative coding with a second rater — do not parallelize late. Plan
backward:

```text
Jun 30  freeze: PDF + anonymized replication package
Jun 16  full internal mock review against the four criteria
Jun 02  results complete; threats-to-validity written from real limitations
May 05  evaluation running at scale; paper skeleton has real numbers
Apr 07  study design locked (RQs, baselines, metrics, subjects); pilot done
Mar 2026 and earlier: idea vetted with icse-topic-selection; related work swept
```

The two dates authors most often plan around wrongly: the **abstract deadline
is mandatory** (June 23 — a week before the paper, not a formality), and the
**response window is September**, which lands in teaching-start season for most
groups — reserve the days now.

## Role assignments that prevent deadline-week chaos

- **Evidence owner** — benchmarks, baselines, statistics; owns Jun 2 freeze.
- **Artifact owner** — replication package, anonymization, availability
  statement; owns the link that goes in the paper.
- **Prose owner** — the 10-page budget, the threats section, the criterion
  self-audit.
- **Process owner** — HotCRP fields, conflicts, abstract registration,
  calendar of every date above in the group calendar with AoE conversions.

One person can hold two hats; no hat may be unheld.

## Branch plans after October 20

- **Accept:** artifact-evaluation submission (badges are opt-in and
  post-acceptance), camera-ready with the extra page, Dublin logistics.
- **Major Revision:** the November sprint is pre-planned *before* October —
  which experiments could be extended, which machines are free in November.
  Groups that first think about feasibility on notification day lose a week
  of the four.
- **Reject:** reroute within weeks, not months. FSE and ASE deadlines
  typically land in spring/summer, ISSTA in autumn/winter; TSE/TOSEM/EMSE take
  extended versions year-round, and a journal acceptance can return to the
  ICSE stage via journal-first (2027 window: papers accepted Oct 11, 2025 –
  Oct 10, 2026 at TSE/TOSEM/EMSE). Check each venue's live dates — sibling
  calendars move annually.

## Cadence between milestones

The calendar above names endpoints; groups that hit them run a steady
between-milestone cadence: a weekly claims-vs-evidence review from April
(which headline claim is still unevidenced, who unblocks it), a biweekly
package build so the artifact never diverges more than two weeks from the
paper, and a standing "deadline minus 14" rehearsal where the current draft
is mock-reviewed against the four criteria by someone outside the author
list. The mock review is the cheapest Major-Revision insurance available:
it finds the missing-baseline and boilerplate-threats objections while
there is still a month to fix them rather than four weeks in November.

## Cycle-volatility warnings

- The single-cycle structure itself is the newest variable: 2025/2026 ran two
  cycles, 2027 runs one. Verify the cycle count *first* each year, because it
  changes every downstream date and the rerouting math.
- Response format, artifact deadlines, camera-ready dates, and registration
  rules were all unposted for 2027 at check time — 待核实 before promising
  them to coauthors.
- Do not let old two-cycle advice ("resubmit to cycle 2") leak into planning;
  that lane does not exist in 2027.

## Output format

```text
[Cycle position] months to next ICSE deadline; feasible? yes/no
[Backward plan] dated milestones from today to freeze
[Owners] evidence / artifact / prose / process
[Branch readiness] MR sprint pre-plan? reroute venue + date named?
[Calendar risks] deadlines colliding with teaching/travel; AoE conversions done
```
