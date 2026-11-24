---
name: icse-workflow
description: Use when planning an ICSE research-track campaign end to end, covering the single-cycle calendar from the June abstract deadline through September response, October decisions, the November revision sprint, artifact evaluation, camera-ready, and the spring conference, plus rerouting timelines after rejection.
---

# ICSE Workflow

An ICSE campaign is a ten-month pipeline with one entrance. The ICSE 2028
cycle (call re-checked 2026-11-24) runs a **single submission cycle**, as
ICSE 2027 did after the two-cycle 2025/2026 model, so a missed deadline costs
a full year, and the calendar below is the whole game.

## The 2028-cycle master calendar

| Date (all AoE where applicable) | Milestone | Your workstream |
|---|---|---|
| Jun 24, 2027 | Abstract (mandatory); reciprocal reviewer nominated | Real title + abstract frozen |
| Jul 1, 2027 | Full paper deadline | 10+2 ACM `sigconf` PDF, artifact link live |
| Jul–Sep 2027 | Reviews written; all-negative papers rejected early | Prepare response infrastructure |
| Sep 24–26, 2027 | Author response window (3 days) | Criterion-mapped replies (`icse-author-response`) |
| Oct 21, 2027 | Decisions: Accept / Major Revision / Reject | Branch: celebrate / sprint / reroute |
| Nov 18, 2027 | Major Revision due | Four-week revision sprint |
| Nov 25, 2027 | Camera-ready of directly accepted papers | +1 page allowance, ACM production |
| Dec 19, 2027 | Final MR decisions | Terminal for the cycle |
| Early 2028 (待核实) | Artifact evaluation window | Badge submission (`icse-artifact-evaluation`) |
| Jan 26, 2028 | Camera-ready of accepted MR papers | +1 page allowance, ACM production |
| Apr 29 – May 7, 2028 | ICSE in Waikoloa, Hawaii (main conference May 3–5) | Talk, artifact, networking plan |

Artifact-evaluation dates for 2028 are not posted yet; ICSE 2027 ran artifact
registration on January 22 and submission on January 29, 2027, which is the
planning anchor until real dates appear.

## Working backward from July 1

A credible empirical-SE paper cannot be compressed into deadline month, because
its long poles — subject recruitment, benchmark construction, multi-week tool
runs, qualitative coding with a second rater — do not parallelize late. Plan
backward:

```text
Jul 01  freeze: PDF + anonymized replication package
Jun 17  full internal mock review against the five criteria
Jun 03  results complete; threats-to-validity written from real limitations
May 06  evaluation running at scale; paper skeleton has real numbers
Apr 08  study design locked (RQs, baselines, metrics, subjects); pilot done
Mar 2027 and earlier: idea vetted with icse-topic-selection; related work swept
```

The two dates authors most often plan around wrongly: the **abstract deadline
is mandatory** (June 24 — a week before the paper, not a formality), and the
**response window is three days in late September** (24–26 in 2027), which lands in teaching-start season for most
groups — reserve the days now.

## Role assignments that prevent deadline-week chaos

- **Evidence owner** — benchmarks, baselines, statistics; owns Jun 3 freeze.
- **Artifact owner** — replication package, anonymization, availability
  statement; owns the link that goes in the paper.
- **Prose owner** — the 10-page budget, the threats section, the criterion
  self-audit.
- **Process owner** — HotCRP fields, conflicts, abstract registration, the
  reciprocal-reviewer nomination,
  calendar of every date above in the group calendar with AoE conversions.

One person can hold two hats; no hat may be unheld.

## Branch plans after October 21

- **Accept:** artifact-evaluation submission (badges are opt-in and
  post-acceptance), camera-ready with the extra page (due November 25, 2027
  for direct accepts), Hawaii logistics.
- **Major Revision:** the November sprint is pre-planned *before* October —
  which experiments could be extended, which machines are free in November.
  Groups that first think about feasibility on notification day lose a week
  of the four.
- **Reject:** reroute within weeks, not months. FSE and ASE deadlines
  typically land in spring/summer, ISSTA in autumn/winter; TSE/TOSEM/EMSE take
  extended versions year-round, and a journal acceptance can return to the
  ICSE stage via journal-first (2027 window, the latest published: papers
  accepted Oct 11, 2025 – Oct 10, 2026 at TSE/TOSEM/EMSE; the 2028 window is
  not posted yet). Check each venue's live dates — sibling
  calendars move annually.

## Cadence between milestones

The calendar above names endpoints; groups that hit them run a steady
between-milestone cadence: a weekly claims-vs-evidence review from April
(which headline claim is still unevidenced, who unblocks it), a biweekly
package build so the artifact never diverges more than two weeks from the
paper, and a standing "deadline minus 14" rehearsal where the current draft
is mock-reviewed against the five criteria by someone outside the author
list. The mock review is the cheapest Major-Revision insurance available:
it finds the missing-baseline and boilerplate-threats objections while
there is still a month to fix them rather than four weeks in November.

## Cycle-volatility warnings

- The cycle structure is volatile: 2025/2026 ran two cycles, 2027 and 2028
  run one. Verify the cycle count *first* each year, because it changes every
  downstream date and the rerouting math. The template also flipped (ACM in
  2026, IEEE in 2027, ACM in 2028).
- Response-format caps, artifact deadlines, the HotCRP URL, and registration
  rules were unposted for 2028 at check time (2026-11-24) — 待核实 before
  promising them to coauthors.
- Early rejection (new in 2028) means some papers never reach the response
  window; do not plan the September week as guaranteed.
- Do not let old two-cycle advice ("resubmit to cycle 2") leak into planning;
  that lane does not exist in 2028.

## Output format

```text
[Cycle position] months to next ICSE deadline; feasible? yes/no
[Backward plan] dated milestones from today to freeze
[Owners] evidence / artifact / prose / process
[Branch readiness] MR sprint pre-plan? reroute venue + date named?
[Calendar risks] deadlines colliding with teaching/travel; AoE conversions done
```
