---
name: webconf-workflow
description: Use when planning a team's calendar around the Web Conference (WWW) annual cycle — the autumn abstract/paper deadlines, the holiday-week rebuttal, January decisions, the short-paper and Web4Good fallback windows inside the same edition, venue-volatility contingencies, and rerouting after rejection.
---

# Web Conference Workflow

The Web Conference runs one research-tracks cycle per year, anchored in early
autumn, with the conference the following spring or summer. The 2026 edition adds
two planning lessons no other pack in this collection teaches as vividly: the same
edition offered **later submission windows into the same proceedings** (short
papers, Web4Good), and the conference itself **moved by ten weeks mid-cycle**
(April 13-17 → June 29 - July 3, 2026), so travel and money plans need slack.

## The 2026 cycle as a planning template

| Milestone | 2026 edition date | Offset from abstract |
|---|---|---|
| Abstract (research/industry) | Sep 30, 2025 | 0 |
| Full paper | Oct 7, 2025 | +1 week |
| Short papers abstract / paper | Nov 10 / Nov 17, 2025 | +6 / +7 weeks |
| Web4Good abstract / paper | Nov 23 / Nov 30, 2025 | +8 / +9 weeks |
| Rebuttal window | Nov 24 - Dec 1, 2025 | +8 weeks |
| Notification | Jan 13, 2026 | +15 weeks |
| Camera-ready | Jan 25, 2026 | +17 weeks |
| Author registration (post-postponement) | Mar 30, 2026 | +26 weeks |
| Conference | Jun 29 - Jul 3, 2026 | +39 weeks |

Every date above is a 2026 anchor for *shape*, not a prediction: pull the current
edition's important-dates page before committing the team.

## Backward planning from the abstract deadline

```text
T-12w  Claim set frozen; datasets acquired; ethics/ToS posture settled
        (data-access negotiations are the long pole for web papers)
T-8w   Experiment matrix running (webconf-experiments); baselines reproduced
T-6w   First full draft; web-native framing test (webconf-writing-style)
T-4w   Internal review by someone from the track's *other* discipline
T-2w   Freeze authors + track; sweep co-author EasyChair profiles;
        count per-author submissions against the cap of 7
T-1w   Page-zone audit, anonymity sweep (webconf-submission)
T+0    Abstract registered -- author list now immutable
T+1w   Paper in, with hours of margin (deadlines are strict, AoE)
```

Two locks distinguish this venue's timeline: the **author-list freeze at T+0** and
the **track choice**, both irreversible a week before the paper itself is due.

## The intra-edition fallback tree

A miss or a weak draft at the research deadline is not a lost year here:

1. **Short papers** (+6 weeks; 4 pages including references; main proceedings) —
   right when the core idea is sound but the full evidence program isn't.
   Compressing an 8-page draft to 4 is a rewrite, not a trim; decide by T+2w.
2. **Web4Good** (+8 weeks; main proceedings) — right when the work's center is
   societal benefit; it is a distinct scope, not a consolation lane.
3. **Workshops / companion venues** (per-workshop deadlines, companion
   proceedings) — visibility and feedback without burning the idea's archival slot.
4. **Hold for the next edition** — WWW 2027 is announced for Dublin, Ireland, so
   the next cycle's deadlines will land in roughly the same autumn window.

Each fallback has different proceedings placement and prestige; choose by what the
paper needs (archival main-proceedings status vs. fast feedback), not by sunk cost.

## Capacity planning quirks

- The rebuttal week (late November in 2026's cycle) collided with a major US
  holiday; name the responding author *at submission time* and check their
  November calendar.
- Notification-to-camera-ready was twelve days; pre-draft the de-anonymized
  version and the artifact deposit during the December quiet period
  (`webconf-camera-ready`).
- Budget approvals for registration + travel should start at notification, not at
  the registration deadline — and the 2026 postponement shows dates can move after
  booking, so prefer refundable fares and watch official channels, not rumor.

## Portfolio planning under the cap

Groups submitting several papers per cycle hit constraints individuals never see.
The 7-per-author cap binds on senior authors first: an advisor on nine drafts must
drop off two *before* abstracts are registered, which is an authorship-integrity
decision, not a bookkeeping one — being removed to dodge the cap while continuing
to contribute violates the spirit of both the cap and the authorship policy.
Rebuttal week is the second portfolio bottleneck: five papers times a one-week
window means five simultaneous response drafts; assign one owning author per
paper in September and let the PI review rather than write. Track collisions are
the third: two similar papers from one group in one track invite the panel to
compare them against each other — differentiate their framings deliberately or
route one to a different track or venue.

## After rejection

Route by the review packet's agreement structure (`webconf-review-process`): a
converged evidence objection means running the missing experiments and returning
next edition; a fit objection means the sibling circuit — WSDM (autumn deadline,
web mining methods), CIKM (spring, broad IR/KM), SIGIR (winter, retrieval), KDD
(winter/summer dual-cycle, mining) — inherits the paper with modest reframing.
Never resubmit unchanged into an overlapping reviewer pool; panels remember.

## Cycle-shape volatility to plan around

Three shape changes the series has actually made, which a multi-year plan should
treat as live possibilities rather than history:

- **Conference month moves.** Recent editions ran in late April/early May
  (Singapore 2024, Sydney 2025) while 2026 landed in late June/early July after
  its postponement — the *submission* window has stayed autumn-anchored, so plan
  research capacity around September-October and treat the conference date as the
  flexible end.
- **Platform switches** (OpenReview 2024-25 → EasyChair research tracks 2026)
  change co-author onboarding costs; budget a week for profile wrangling whenever
  a new edition's call names a different system.
- **Special-track churn** (Web4Good appeared for 2026) means the fallback tree
  must be rebuilt from the current edition's calls page each year, not reused.

## Output format

```text
[Cycle position] T<±n>w relative to current-edition abstract deadline
[Locks ahead] author freeze / track choice / cap count -- dates
[Fallback decision] research full / short / Web4Good / workshop / next edition
[Capacity flags] rebuttal-week owner, camera-ready pre-work, travel slack
[Next actions] <this week's moves, with owning author>
```
