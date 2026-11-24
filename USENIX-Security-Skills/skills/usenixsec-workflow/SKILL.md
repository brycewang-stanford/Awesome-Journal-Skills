---
name: usenixsec-workflow
description: Use when planning a USENIX Security Symposium project end to end — choosing between the two annual cycles, mapping the registration-to-camera-ready calendar for a chosen cycle, sequencing artifact and ethics work early, and coordinating a team across the multi-deadline Big-Four calendar.
---

# USENIX Security Workflow

USENIX Security runs two independent submission cycles per year, so "when do we
submit?" is a real strategic choice, not a fixed date. This skill turns a target
cycle into a dated backward plan and assigns owners to the venue-specific risks.
Dates below are the USENIX Security '27 values re-read from the live '27 CFP on
2026-11-24 ('26 kept for comparison). On that date '27 Cycle 1 is in review and
**'27 Cycle 2 is the open door** (registration Jan 19, paper Jan 26, 2027, AoE) —
reconfirm against the live CFP.

## Step 1: pick the cycle

| Consideration | Favors the earlier cycle | Favors the later cycle |
|---|---|---|
| Readiness | Evaluation truly done now | Needs one more experiment done right |
| Conference lead time | Cycle-1 accepts publish ~7 months pre-symposium | Cycle-2 accepts closer to the event |
| Competing deadlines | Avoids clashing with a CCS/S&P/NDSS date | Room to route a reject to the next venue |
| Resubmission runway | None: a '27 Cycle-1 reject may not enter '27 Cycle 2* | Reject pushes to next year |

\*Per the '27 CFP: papers rejected from '27 Cycle 1 may not be submitted to '27
Cycle 2, while papers rejected from either '26 cycle may be submitted to '27 (see
`usenixsec-review-process`).

Reference calendar (verify per cycle):

| Milestone | Sec '26 C1 | Sec '26 C2 | Sec '27 C1 | Sec '27 C2 |
|---|---|---|---|---|
| Registration | Aug 19 '25 | Jan 29 '26 | Aug 18 '26 | Jan 19 '27 |
| Submission | Aug 26 '25 | Feb 5 '26 | Aug 25 '26 | Jan 26 '27 |
| Artifacts final (grace) | — | — | Aug 28 '26 | Jan 29 '27 |
| Early reject | Oct 7 '25 | Mar 17 '26 | Oct 6 '26 | Mar 9 '27 |
| Rebuttal | — | — | Nov 5–12 '26 | Apr 8–15 '27 |
| Notification | Dec 4 '25 | May 14 '26 | Dec 3 '26 | May 6 '27 |
| Shepherded approval | — | — | Dec 15 '26 | May 18 '27 |
| Finals | Jan 15 '26 | Jun 11 '26 | Jan 14 '27 | Jun 3 '27 |
| Symposium | Aug 12–14 '26 (Baltimore) | Aug 11–13 '27 (Denver) | | |

## Step 2: backward-plan from the registration date

Registration, not submission, is the first hard wall (it fixes title, authors with
ORCIDs and topics a week early). Plan backward from it:

```text
T-12 wk  Topic/venue fit locked (usenixsec-topic-selection); threat model drafted
T-10 wk  Core experiments running; artifact repo scaffolded from day one
T-8  wk  Related-work sweep of all Big-Four cycles closed since last pass
T-6  wk  Adaptive-attacker / base-rate experiments (the ones that get demanded)
T-4  wk  Full draft; Open Science appendix (mandatory) + Ethics appendix written
T-3  wk  Internal review + cold-reader pass on intro/threat model
T-2  wk  Anonymization sweep; artifact anonymous mirror live and tested
T-1  wk  REGISTRATION: freeze metadata; final polish only after this
T-0      Submit; re-download from HotCRP and read cold
```

The two moves teams most often leave too late: the **adaptive-attacker experiment**
(defenses) and the **ethics/disclosure timeline** (live-system work). Both must
start weeks before the deadline — a disclosure clock especially cannot be
compressed, since vendors set the pace.

## Step 3: assign the venue-specific risks

| Risk | Owner | Early mitigation |
|---|---|---|
| Ethics/disclosure not started | PI | Open the disclosure and IRB threads at project start |
| Artifact not reproducible | Eng lead | Build the repo alongside the code, not after the paper |
| Threat model drifts from eval | First author | Adversary-consistency review at T-3 wk |
| Anonymity leak in artifact | Eng lead | Anonymous mirror built and log-out-tested by T-2 wk |
| Missed a fresh Big-Four paper | Reader | Dated literature sweep at T-8, re-sweep at T-2 |

## Step 4: run the post-submission and post-decision phases

- **Waiting**: expect the early-reject gate first (a survivable-but-quiet signal),
  then full notification. Do not start the next paper assuming acceptance, but do
  keep the artifact repo warm — acceptance starts the Phase-1 clock immediately.
- **Rebuttal**: '27 runs a one-week rebuttal period before notification
  (Nov 5–12, 2026; Apr 8–15, 2027) — see `usenixsec-author-response`.
- **Shepherd approval**: scope the change list within 48 hours; it fits the
  ~12-day window between notification and shepherded-approval due date and no more.
- **Accept**: run camera-ready and Phase-1 artifact availability in parallel — they
  share a deadline (see `usenixsec-camera-ready`).
- **Reject**: mine the reviews, check the resubmission restriction, decide between
  the next USENIX cycle and a sibling venue with an open deadline.

## Coordinating across the Big-Four calendar

Because USENIX Security, CCS, S&P, and NDSS each run multiple deadlines, a lab can
keep a paper in motion nearly year-round — but a paper may sit under review at only
one archival venue at a time. Maintain a shared deadline board and a one-in-one-out
rule per paper; the dual-submission bar is real and enforced.

## Reverify each cycle

- All dates in the table above (re-verified for '27 on 2026-11-24; the CFP still
  governs).
- Symposium location and dates for your target year.
- Resubmission restrictions gating cycle-to-cycle and year-to-year moves.

## Output format

```text
[Cycle chosen] which cycle + why (readiness / lead time / clash / runway)
[Backward plan] dated milestones from registration wall
[Risk owners] the five venue risks assigned + early mitigations underway
[Post-decision] branch plan for accept / shepherd / reject
```
