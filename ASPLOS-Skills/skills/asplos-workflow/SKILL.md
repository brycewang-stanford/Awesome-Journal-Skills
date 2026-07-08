---
name: asplos-workflow
description: Use when planning an ASPLOS campaign across the two-deadline cycle — sequencing evidence building, the September 9, 2026 submission gate, author-response windows, the December 21 notification, Major Revision resubmission six weeks later, artifact evaluation, and the April 2027 conference in Crete, with owners per risk.
---

# ASPLOS Workflow

An ASPLOS campaign is a pipeline with two entry gates per edition and a revision
side-channel, not a single deadline sprint. All dates below are the verified 2027
cycle (CFP and conference site, checked 2026-07-08); reopen the official pages before
committing a team to any of them.

## The 2027 cycle as a calendar

| Gate | April cycle | September cycle |
|---|---|---|
| Full-paper deadline (11:59 PM AoE) | April 15, 2026 — **passed** | **September 9, 2026 — the live gate** |
| Author response | July 6-9, 2026 — **open this week** (as of 2026-07-08) | December 1-4, 2026 |
| Notification | July 27, 2026 | December 21, 2026 |
| Major Revision due | camera-ready deadline, 6 weeks after notification | camera-ready deadline, 6 weeks after notification |
| Conference | April 11-15, 2027, Heraklion, Crete, Greece | same |

There is no separate abstract deadline in 2027, and no mid-year third round — the
edition moved from three deadlines to two. Missing September means waiting for the
next edition's first gate.

## Working backward from September 9, 2026

A credible countdown for a systems paper with hardware-dependent evidence:

```text
T-10 weeks (by ~Jul 1)   Freeze the claim list; run asplos-topic-selection;
                         choose evidence instruments (silicon / FPGA / simulator).
T-8 weeks                Evaluation infrastructure done: baselines building,
                         workloads chosen, simulator configs pinned.
T-6 weeks                First full results sweep; kill or descope claims the
                         data will not carry. Start the two-page draft NOW —
                         it is the part rapid review actually reads.
T-4 weeks                Full draft; internal red-team against the rapid-review
                         question set; ablations running.
T-2 weeks                Freeze experiments. Citation-format pass (full names,
                         no "et al.", DOIs). Anonymity sweep.
T-1 week                 HotCRP entry created; PDF uploaded; co-author sign-off.
T-0  Sep 9, 11:59 PM AoE HotCRP status shows *complete*, not draft.
```

## Role assignments that prevent known failures

- **Two-page owner** — one author owns pages 1-2 as a standalone artifact and
  rehearses them against `asplos-writing-style`; rapid review reads nothing else.
- **Evidence-integrity owner** — keeps the experiment matrix (claims × platforms ×
  baselines) current so the rebuttal window never requires new runs under pressure.
- **Compliance owner** — template, 11-page geometry, citation full-name rule, GenAI
  disclosure, HotCRP fields; format violations risk rejection without review.
- **Response owner** — reserves the response window dates (Dec 1-4 for the September
  cycle) on every author's calendar at submission time, not after reviews arrive.

## Branch planning at notification (December 21, 2026)

1. **Accept** → switch to `asplos-camera-ready` immediately; camera-ready lands
   ~6 weeks out, and artifact evaluation (`asplos-artifact-evaluation`) runs in
   parallel with its own appendix and deadlines (2027 AE calendar 待核实).
2. **Major Revision** → treat as a funded contract, not a consolation: the revision
   is due at the camera-ready deadline and *counts as a submission*; scope revision
   work to exactly what the decision letter requires, tracked in a change log that
   will become the resubmission note.
3. **Reject at rapid review** → the diagnosis is almost always positioning: the
   first two pages did not establish the intersection or the evidence. Fix framing
   before considering a new venue.
4. **Reject after full review** → mine the reviews for the evidence matrix, then
   re-run `asplos-topic-selection`; some full-review rejects are strong ISCA, SOSP,
   or PLDI papers mis-aimed at the intersection.

## Cross-edition cautions

- The two-deadline structure is itself new for 2027; do not assume it for 2028.
- ASPLOS logistics genuinely change year to year — the 2025 edition (30th, Rotterdam)
  ran jointly with EuroSys; 2026 (31st) was standalone in Pittsburgh; 2027 is in
  Crete. Travel, visa, and registration planning must restart per edition (fees and
  attendance rules for 2027: 待核实).
- Program leadership rotates every edition; there is no standing editorial memory to
  appeal to. A policy answer from a previous year's chairs is expired.

## Hardware lead times are schedule items

Systems evidence has procurement physics that a paper calendar must absorb:

- Cluster or testbed reservations for the T-8 to T-2 sweep window book out weeks
  ahead; reserve at claim-freeze time, not first-results time.
- FPGA synthesis iterations and simulator calibration runs are days-long serial
  steps — one redesign late in the countdown costs a week, not an evening.
- Access to pre-production parts (new memory devices, engineering samples) often
  comes with NDA review of the paper text; start that review before T-4 or it
  becomes the critical path.

## Between notification and Crete

An accepted September-cycle paper has a compressed post-decision runway:
camera-ready and any Major Revision work land ~6 weeks after December 21 —
squarely across the holiday break, which the six-week plan must acknowledge —
followed by artifact evaluation, then travel logistics for an April conference
in Greece (visa timelines for some team members exceed the gap; start at
notification). Presentation format, registration requirements, and speaker
obligations for 2027 were 待核实 at pack-check time: read the acceptance email
before assigning the talk.

## Pipelining across gates

Teams running multiple projects should treat the two gates as a pipeline: a
paper that misses the September evidence bar can target the next edition's first
gate with its evaluation matrix already built, while the response and revision
windows of a September submission land in December-February — plan author
bandwidth so a Major Revision does not collide with the next project's deadline
sprint. One person cannot own the revision of paper A and pages 1-2 of paper B
in the same six weeks.

## Output format

```text
[Cycle chosen] September 2026 / next edition (reason)
[Countdown health] on-track items · at-risk items with dates
[Owners] two-page / evidence / compliance / response — names attached?
[Branch plans] accept · major-revision · rapid-reject · full-reject, one line each
[Calendar holds] Dec 1-4 response window + 6-week revision block reserved? Y/N
[Facts to re-verify] <official pages to reopen before relying on this plan>
```
