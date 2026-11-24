---
name: siggraph-workflow
description: Use to plan a SIGGRAPH or SIGGRAPH Asia Technical Papers campaign backward from the deadline, covering the two annual cycles, the form-then-upload two-step submission, the rebuttal window, the Technical Papers Committee decision, conditional-accept second-stage revision, TOG camera-ready, and the in-person presentation.
---

# SIGGRAPH Workflow

SIGGRAPH runs on **two cycles a year** and a compressed single-round calendar with a journal-grade
tail. Planning backward from the right deadline — and knowing which of the two conferences you are
targeting — is the highest-leverage move. Dates below are the SIGGRAPH 2026 / SIGGRAPH Asia 2026
snapshots plus the SIGGRAPH 2027 deadlines posted as of 2026-11-24 (full 2027 call still pending),
from `resources/official-source-map.md`; reopen the live Important Dates page for your cycle first.

## The two cycles

| Cycle | Deadline (approx.) | Conference | Latest instance |
|---|---|---|---|
| SIGGRAPH (North America) | ~January | Summer | SIGGRAPH 2026, Los Angeles, 19-23 Jul 2026 (met): form 15 Jan, paper 22 Jan, upload 23 Jan 2026 (22:00 UTC). **Next: SIGGRAPH 2027, Anaheim, 8-12 Aug 2027** — form & conflicts 21 Jan, paper 28 Jan, upload 29 Jan 2027 (22:00 UTC; full call pending) |
| SIGGRAPH Asia | ~May | December | SIGGRAPH Asia 2026, Kuala Lumpur, 1-4 Dec 2026: form 5 May, paper 12 May, upload 13 May 2026 (23:59 AoE). Next: SIGGRAPH Asia 2027, Tokyo, 30 Nov-3 Dec 2027 (no call yet) |
| TOG direct | rolling | (no conference talk) | ScholarOne, outside the conference cycle — less common |

A rejected paper is typically revised against the reviews and resubmitted to the *next* cycle, so
the two deadlines form a natural half-year rhythm. Pick the cycle whose deadline your results can
credibly meet — a rushed submission to the nearer deadline usually loses to a finished one at the
next.

## Backward plan from the upload deadline

```text
T+1d    Upload deadline: files matching MD5 checksums; every co-author's conflicts entered
T-0     Paper deadline: PDF (or MD5) + supplemental video + representative image on Linklings
T-1wk   Submission form locks title/abstract/topics/ALL co-authors (earlier hard deadline)
T-2wk+  Anonymity-policy embargo starts: no project page, PR or social posts (arXiv allowed)
T-2wk   Freeze results; render the final results video; clear rights on every frame/figure
T-4wk   Final comparisons + timings on stated hardware; ablations complete
T-8wk   Draft complete in acmart (>=2.16); teaser figure locked; internal reviews
T-12wk+ Method + implementation stable; baselines reproduced; scene set assembled
```

The two immovable graphics-specific costs are the **results video** (allow real production time)
and **faithful baseline comparisons** (allow time to build and run others' code). Neither
compresses well in the last week.

## After submission

```text
Reviews released -> you see the full set
Rebuttal window (~6 weeks post-deadline): <=1000 words, text only, anonymous, address factual errors
Technical Papers Committee meeting: conditional accept / reject + track (Journal vs Conference)
[If conditional] make every required change -> second-stage committee verification
Camera-ready: TOG metadata, rights/DOI, final video, permanent code archive
Presentation: at least one author presents in person at the conference
```

## Milestone checklist

- [ ] Cycle chosen (SIGGRAPH vs SIGGRAPH Asia) and its exact UTC cutoffs confirmed on the live page.
- [ ] Track intent chosen (dual-track vs Journal-only) — see `siggraph-submission`.
- [ ] Baselines reproduced and running before the writing freeze.
- [ ] Results video scoped and scheduled as a real production task.
- [ ] Submission form completed (authors locked) before its earlier deadline.
- [ ] Rebuttal plan ready the moment reviews land — see `siggraph-author-response`.
- [ ] Conditional-accept change list tracked to the second-stage review.
- [ ] Camera-ready TOG apparatus and permanent archive prepared — see `siggraph-camera-ready`.
- [ ] Presenter and travel confirmed for in-person presentation.

## Reverify each cycle

- Both conferences' exact dates and UTC cutoffs, and whether the year runs the usual two editions.
- The rebuttal window and length, the acmart revision, and the Conference-track page budget.
- The anonymity policy and its embargo window (2026: double-blind, embargo from two weeks before the deadline).

## Output format

```text
[Target cycle] SIGGRAPH 20XX (Jan) / SIGGRAPH Asia 20XX (May) / TOG-direct
[Countdown] weeks to form deadline / upload deadline
[Critical path] video production + baseline comparisons on track? yes/no
[Post-submission] rebuttal plan / conditional-accept list / camera-ready readiness
[Blockers] <ordered, dated to the UTC cutoff>
```
