---
name: pldi-workflow
description: Use when planning a PLDI campaign across its annual clock — backward-planning from the November deadline through winter reviewing, the February response window, March notification, post-acceptance artifact evaluation, PACMPL production, and the June conference, with owners for each deliverable.
---

# PLDI Workflow

PLDI is an annual, single-deadline venue with a long tail: the paper is due in
November, but the project is not finished until the PACMPL article, the badged
Zenodo artifact, and the June talk have all shipped. Plan all three from the
start. Anchor dates below are the 2026 cycle (deadline Nov 13, 2025; response
Feb 17-21, 2026; notification Mar 5, 2026; registration opened Mar 16;
conference in Boulder Jun 15-19, 2026) — reread the current dates page before
scheduling anything, and note that PLDI 2027's calendar was unpublished as of
2026-07-08 (待核实).

PLDI has no standing editor-in-chief and charges no submission fee; leadership
rotates per edition (2026: General Chair Bor-Yuh Evan Chang, Program Chair Manu
Sridharan), the conference is funded through registration, and the PACMPL
open-access cost is handled through SIGPLAN/ACM Open arrangements at
camera-ready time (`pldi-camera-ready`), not at submission.

## Backward plan from the November deadline

| Weeks out | Milestone for a compiler/analysis paper |
|---|---|
| 12+ | Mechanism frozen; running example chosen; suite + baselines locked (`pldi-experiments`) |
| 8 | Implementation feature-complete on the suite; measurement protocol scripted (`pldi-reproducibility`) |
| 6 | Full benchmark campaign run once end-to-end; losing benchmarks diagnosed |
| 4 | Complete draft in `acmsmall`; proofs or soundness argument internally reviewed |
| 3 | Mock review by a PL colleague outside the project; ablation gaps closed |
| 2 | Final measurement run from clean scripts; claim ledger reconciled (`pldi-writing-style`) |
| 1 | Anonymity sweep, supplement assembly, HotCRP fields, dual-submission check |
| 0 | Upload with a day of slack |

## The long tail after the deadline

```text
Nov: submit; archive exact PDF + scripts + raw results
Dec-Jan: keep the artifact warm — the response window may need a rerun
Feb: response window (days, not weeks): triage -> draft -> co-author pass -> submit
Mar: decision. Accept: start AE packaging same week; camera-ready plan.
     Reject: file reviews against the claim ledger; decide POPL/OOPSLA/next PLDI.
Apr-May: artifact evaluation runs; PACMPL production; register; build the talk.
Jun: conference. Post-talk: sync the Zenodo record with the final article.
```

Two scheduling traps dominate. First, the response window is short and fixed —
a co-author on vacation in late February is a real project risk; put the window
on calendars in November. Second, artifact evaluation begins right after
notification, so the team that celebrates acceptance for two weeks starts AE
already behind (`pldi-artifact-evaluation`).

## Ownership map

Assign one named owner each for: the measurement protocol, the anonymity sweep,
the response draft, the artifact, and the camera-ready/rights workflow. The
artifact owner should not be the graduating student whose defense is in April.

## Rejection routing

A PLDI reject in March leaves useful runway: OOPSLA and ICFP deadlines, or the
next PLDI in November. Route by what the reviews attacked — soundness objections
must be fixed before any resubmission inside the same reviewer community
(`pldi-review-process`, `pldi-topic-selection`).

## Output format

```text
[Stage] design / implementation / evaluation / writing / submitted / response / decided / post-acceptance
[Next hard date] <from the live dates page; 待核实 if unpublished>
[Critical path] <three tasks gating the next stage>
[Owners] protocol / anonymity / response / artifact / camera-ready
[Long-tail risks] response-window availability, AE start, registration, talk
```
