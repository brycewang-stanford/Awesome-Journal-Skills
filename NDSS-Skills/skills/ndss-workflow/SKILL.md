---
name: ndss-workflow
description: Use when planning an NDSS submission calendar — choosing between the summer and fall cycles, backward-planning from the AoE deadline through early-reject, rebuttal, notification, camera-ready, and the Seoul symposium, and placing NDSS honestly inside the security big-four retargeting year.
---

# NDSS Workflow

One symposium, two entrances. NDSS 2027 accepts papers through a summer cycle and a fall
cycle, each a complete two-round review pipeline, both feeding the same week in Seoul
(22-26 March 2027). Plan against the cycle you can actually win, not the one that arrives
first.

## The 2027 skeleton (re-verified 2026-11-24 on the live CFP; always recheck)

| Milestone | Summer cycle | Fall cycle |
| --- | --- | --- |
| Paper deadline (AoE / UTC-12) | May 6, 2026 — passed | August 19, 2026 — passed |
| Round-1 reviews / early-reject notification | June 18, 2026 | Round 1 Sept 18 - Oct 13, 2026 |
| Rebuttal | July 15-17, 2026 | November 19-21, 2026 |
| Interactive discussion | July 15-22, 2026 | November 19-26, 2026 |
| Author notification | July 29, 2026 | December 2, 2026 |
| Minor Revision approved by shepherd | August 19, 2026 | January 5, 2027 |
| Major Revision resubmission | August 31, 2026 | January 5, 2027 |
| Major Revision notification | September 16, 2026 | January 25, 2027 |
| Camera-ready | September 30, 2026 | February 7, 2027 |
| Symposium (Seoul) | March 22-26, 2027 | March 22-26, 2027 |

As of 2026-11-24 both NDSS 2027 cycles are closed and the fall cycle is at final
notification; **NDSS 2028 has no published call**, so the next NDSS deadline (by the 2027
pattern, a summer cycle around May 2027) is not yet a date. Registration for Seoul opened in
October 2026 (Internet Society announcement) — for many teams the 2027 edition also means
visas and long-haul travel budgets that San Diego never required. Start that paperwork at
acceptance, not at camera-ready.

## Backward plan from a cycle deadline (D)

```text
D        paper deadline (AoE)          ── freeze everything
D-1 wk   full-draft freeze             ── format, anonymity, ethics-section, AI-disclosure passes only
D-2 wk   internal red-team read        ── someone plays the Round-1 reviewer
D-3 wk   evaluation freeze             ── last new experiment; start writing results
D-5 wk   disclosure clock check        ── vendor notifications sent early enough that
                                          "we disclosed" is true at submission time
D-6 wk   go/no-go                      ── fit test done, adversary model written,
                                          headline experiment already running
```

The item teams misplace is the **disclosure clock**: responsible disclosure has latency
measured in weeks, and the CFP expects reporting (or a concrete plan) for high-impact
vulnerabilities. A finding made nine days before the deadline forces an uncomfortable choice; a finding made
six weeks before the deadline does not.

## Choosing the cycle

- Enter the **earliest cycle whose backward plan closes** with the evaluation *done*, not
  projected. A thin submission is worse than a late one here, because a reject may not be
  resubmitted to the same edition at all, and a summer reject may not reappear with major
  overlap in that edition's fall cycle.
- The rebuttal window is short and fixed (2027: July 15-17 summer, November 19-21 fall).
  Check coauthor availability during those exact days before committing.
- A **Major Revision** outcome converts the calendar: you get reviewer-specified revision
  tasks and a resubmission window (2027: about one month — August 31, 2026 for summer,
  January 5, 2027 for fall). Budget the
  post-notification month as working time, not celebration time.

## The big-four year, seen from the NDSS seat

The four flagship deadlines interleave, and NDSS's late-summer fall deadline sits where
papers rejected from the S&P and CCS spring/summer cycles and the USENIX Security year
naturally land. Two honest rules for riding this calendar:

1. **Retargeting without revision is re-rejection.** Reviewer pools overlap heavily across
   the big four; a resubmission that ignores its previous reviews often meets the same
   people. Fold in the fixes, and re-frame for NDSS's networked-adversary lens rather than
   doing a logo swap.
2. **NDSS is a venue, not a fallback tier.** Its acceptance bar is a peer of the other
   three; a paper that was thin at S&P is thin here too. What legitimately changes is *fit*
   — protocol, web, DNS, and distributed-infrastructure work often reads better to an NDSS
   PC than it did wherever it bounced.

## Running the year

- Track each paper as a state machine: `drafting → submitted → round-2 | early-reject →
  rebuttal → accept | minor-rev | major-rev | reject`, with an owner and a next-action per
  state. The review-process skill details what each state means.
- On **early reject** (with Round-1 reviews in hand): route to the next venue on the
  routing table in `ndss-topic-selection`, after folding in the reviews. The same-edition
  door is closed; the 2028 door is not.
- On **accept / minor revision**: fork immediately into camera-ready (2027: September 30,
  2026 for summer, February 7, 2027 for fall) and the artifact-evaluation opt-in, which comes
  first (see `ndss-artifact-evaluation`), plus logistics
  (registration, visas, who presents).
- Keep the per-author six-submission cap visible on the group's board each cycle; it binds
  collaborations with many shared authors sooner than people expect.

## Output format

```text
[Cycle chosen] summer / fall / next edition — one-line justification
[Backward plan] table of dated freezes ending at the AoE deadline
[Disclosure clock] green / yellow / red + earliest safe submission date
[Rebuttal window] coauthors confirmed available? yes/no
[Post-decision branches] accept / minor / major / reject → owner + next action each
[Logistics] Seoul registration, visa lead time, presenter
```
