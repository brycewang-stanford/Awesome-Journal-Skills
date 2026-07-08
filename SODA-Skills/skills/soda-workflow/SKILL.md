---
name: soda-workflow
description: Use when planning a SODA (ACM-SIAM Symposium on Discrete Algorithms) campaign end to end — backward-planning to the July AoE deadline, SODA's seat in the theory calendar between STOC and FOCS deadlines, the September rebuttal and October decision, satellite deadlines (ALENEX, SOSA), and the January conference.
---

# SODA Workflow

The 2027 anchor calendar, checked 2026-07-08 (SIAM SODA27/ALENEX27/SOSA27 pages
via search renderings; `siam.org` blocked direct fetches): papers due **July 9,
2026 (AoE)** on `soda27.hotcrp.com`; reviews to authors by September 1; responses
due September 4; decisions October 2026; conference **January 24-27, 2027,
Philadelphia**, co-located with ALENEX (papers due July 20, 2026) and SOSA
(papers due August 6, 2026). SODA appoints a new PC every cycle under joint
SIAM/ACM SIGACT sponsorship — every date here is a 2027-cycle snapshot, void for
any other year until re-checked.

## SODA's seat in the theory year

Theory groups plan around three rotating deadlines, and SODA's is the summer one:

| Beat | Deadline season | Conference season | 2026-27 anchors |
|---|---|---|---|
| SODA | early-mid July | January | July 9, 2026 → January 24-27, 2027 |
| STOC | early November | June | pattern; 2027 dates 待核实 |
| FOCS | early April | October-November | pattern; 2027 dates 待核实 |

Sitting in SODA's seat, the planning consequences are:

- A result finished in **spring** has a natural July home at SODA; pushing to
  the November STOC deadline buys four months you may not need and delays the
  talk by five.
- A **SODA rejection lands in October** — about a month before STOC's deadline.
  That is enough time for presentation surgery and review-driven repairs, not
  for new mathematics. Decide within a week of the decision.
- A result that misses July 9 waits four months (STOC), nine months (FOCS), or
  twelve (next SODA). Theory culture never punishes a year's delay; it always
  punishes a broken lemma. When in doubt, wait.
- January is also **ITCS** season: a conceptual paper rejected from SODA often
  fits ITCS's early-September deadline pattern (2027 dates: 待核实).

## Backward plan to July 9

| Checkpoint | State of the project |
|---|---|
| T-12 weeks (mid-April) | Result proved to the group's satisfaction; claims ledger opened (`soda-reproducibility`) |
| T-8 weeks (mid-May) | Full proofs written as prose — writing is the verification |
| T-6 weeks (late May) | Blind proof-check pass: each proof verified by a non-author of that proof |
| T-4 weeks (June) | Front matter built: title-page abstract, overview, prior-bound table (`soda-writing-style`); final arXiv sweep for concurrent work |
| T-2 weeks | Format and anonymity audit (`soda-submission`); HotCRP record created; conflicts entered |
| T-1 week | Full-document read by the least-involved coauthor; freeze |
| July 9, AoE | Upload confirmed by re-downloading the stored PDF |

The classic failure is proving through June: theorem-finishing scheduled inside
the writing window converts both into deadline-night work.

## If the deadline is this week

This pack's anchor deadline (July 9, 2026) sits in early July — so a reader in
the first week of July 2026 is not planning, but triaging. Honest triage:

| State of the paper today | Verdict |
|---|---|
| Proofs complete, front matter rough | Submit: polish the abstract and overview first, in that order — they carry triage review |
| One proof "almost works" | Do not submit the claim. Either weaken the theorem to what is proved, or hold the paper for STOC |
| Complete but nobody re-checked the proofs | Submit only with a same-week blind check of the main theorem; a withdrawn SODA paper costs less than a refuted one |
| Result strong, writing chaotic | Submit if the first ten pages can be made honest by Thursday; the back matter is verified, not enjoyed |
| Waiting on an experiment | Cut it; experiments are optional evidence at SODA (`soda-experiments`) and never worth a missed AoE cutoff |

The one thing not to do in deadline week: broaden claims to justify the rush.
Reviewers arrive in August with time you did not have.

## The quiet phases and their jobs

- **July-August (refereeing):** do not idle. Maintain the claims ledger, pre-draft
  the two predictable rebuttal paragraphs, post/refresh the arXiv version, and
  decide whether an ALENEX (July 20) or SOSA (August 6) companion is real.
- **September 1-4 (rebuttal):** the three-day sprint; all-hands availability
  arranged in advance (`soda-author-response`).
- **September-October (PC deliberation):** silence is structural, not
  informative. Prepare both branches: camera-ready plan and re-route plan.
- **October-January (accepted branch):** condensation, SIAM forms, arXiv sync,
  talk build (`soda-camera-ready`); registration logistics for Philadelphia.

## Owner discipline for a group submission

Every deadline on this page needs exactly one named owner, decided in June:

- **Deadline owner** — watches the SIAM page for changes, does the final
  upload, holds the HotCRP credentials, converts AoE to local time correctly.
- **Ledger owner** — maintains the claims ledger from `soda-reproducibility`
  through submission and into rebuttal week.
- **Rebuttal owner** — pre-books the September 1-4 window across all coauthor
  calendars in July, when calendars are still empty.
- **Satellite owner** — if an ALENEX or SOSA companion exists, it gets its own
  three owners; shared ownership across sibling submissions is how one deadline
  eats another.

## Multi-paper and satellite choreography

```text
Decision tree for a group with theory + implementation results in June 2026:
1. Theory result stands alone?            -> SODA by July 9
2. Implementation contribution disjoint?  -> ALENEX by July 20 (AE follows)
3. Simplification of a known result?      -> SOSA by August 6
4. Same claims in two of the above?       -> pick one; overlap risks both
Each paper needs its own contribution sentence that mentions no sibling.
```

One calendar per paper, one owner per deadline. Shared-author papers at SODA and
a satellite also share the January trip — one registration decision, one talk
rehearsal block, and no scheduling collision (satellites run January 24-26,
inside the SODA window).

## Output format

```text
[Cycle verdict] Submit July 9 / hold for STOC / re-route
[Backward plan] <checkpoint dates with owners, from today>
[Quiet-phase tasks] <ledger, rebuttal prep, arXiv, satellite decisions>
[Contingency] <October rejection branch: repair-for-STOC or wait>
[Satellite calendar] <ALENEX/SOSA/ITCS deadlines in play, if any>
```
