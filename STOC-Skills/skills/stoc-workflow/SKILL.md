---
name: stoc-workflow
description: Use when planning a STOC (ACM Symposium on Theory of Computing) project calendar — backward planning to the early-November deadline, the STOC/FOCS alternating two-deadline year that theory groups schedule around, full-version and camera-ready milestones, and the June TheoryFest endpoint.
---

# STOC Workflow

STOC is a conference with per-edition leadership, not a journal: SIGACT appoints
a fresh program committee and chair every year (STOC 2026: PC chair Artur
Czumaj; verified 2026-07-08 via the CFP), there is no standing editor, and
publication costs ride on conference registration rather than author fees.
Anchor timeline, 2026 cycle: submissions November 4, 2025 (4:59pm EST);
notification by February 1, 2026; camera-ready and public full version March 31,
2026 (AoE); conference June 22–26, 2026, Salt Lake City, inside a five/six-day
TheoryFest program. Every date below is that cycle's snapshot — reopen
`acm-stoc.org` for the live year before acting on any of them.

## The two-beat theory year

The field's real planning unit is not one deadline but the STOC/FOCS pair:
STOC submissions close in early November for a June conference; FOCS closes in
early April for a fall conference (FOCS 2026: deadline April 1, 2026, 21:00
UTC; conference November 8–11, 2026, New York — verified 2026-07-08). The same
community, largely overlapping reviewer pools, near-identical scope. Strategic
consequences:

| Situation in late October | Sound play |
|---|---|
| Result complete, writing strong | Submit to STOC |
| Proof complete, writing weak | Submit only if the overview can be made honest in time; a rushed overview at a no-rebuttal venue is unrecoverable |
| One lemma still open | Hold for FOCS in April; five months closes lemmas |
| STOC rejection arrives Feb 1 | Two months to repair for FOCS — enough for presentation surgery, rarely enough for new mathematics |
| Result claimed by concurrent preprint | Post to arXiv immediately for priority, then decide venue calmly |

A result that misses both beats simply waits; nothing in theory culture
penalizes a strong paper for arriving one cycle later, but plenty penalizes a
broken proof for arriving on time.

## Backward plan to a November deadline

- **T−16 weeks:** the mathematical result exists in believed-complete form.
  Everything after this is verification and writing; theorem-proving scheduled
  inside the writing window is the classic failure.
- **T−12 weeks:** full proofs written out (full-version draft), not just notes.
  Writing proofs *is* verification at this venue; gaps surface only under the
  discipline of complete prose.
- **T−8 weeks:** internal verification pass — each theorem checked by a
  coauthor who did not draft its proof (`stoc-reproducibility`'s workflow).
- **T−6 weeks:** extract the extended abstract from the full version: choose
  the twelve-page story, write the technical overview (`stoc-writing-style`).
- **T−3 weeks:** hostile-read by a colleague outside the sub-area; their
  confusion map drives the final overview rewrite.
- **T−1 week:** literature re-sweep (arXiv/ECCC), objection-ledger check
  (`stoc-author-response`), anonymity sweep and HotCRP dry run
  (`stoc-submission`). If opting into a pre-submission feedback experiment
  (2026: full paper due ~3 days early), the paper must be done here.
- **T:** upload with hours to spare; the deadline is a US-Eastern wall-clock
  time, not AoE, and this catches Europeans annually.

## Between submission and decision (Nov–Feb)

- Post or refresh the arXiv/ECCC version if the cycle's double-blind rules
  permit (待核实 — check the live CFP's stance on preprints during review).
- Keep a corrections file: any bug or improvement found post-submission goes in
  it, dated. If a chair-mediated query arrives, answers come from this file; if
  acceptance arrives, it becomes the camera-ready worklist.
- Do not silently rewrite the posted preprint mid-review in ways that diverge
  from the submitted PDF; reviewers may be reading both.

## From acceptance to Salt Lake City (Feb–Jun)

1. Triage the corrections file into camera-ready fixes vs. full-version-only
   improvements (`stoc-camera-ready`).
2. Hit both March 31 deliverables: the ACM proceedings version and the public
   full version with complete proofs — the CFP treats the second as an
   expectation of acceptance, not a courtesy.
3. Prepare the TheoryFest talk: one theorem, one technique, one open problem;
   rehearse to the announced slot length. Poster/workshop add-ons follow the
   program announcement (待核实 per cycle).
4. Confirm registration and attendance obligations from the acceptance email
   (待核实; not stated in the CFP excerpts verified for this pack).

## The cycle at a glance (2026 snapshot)

```text
2025-11-01  optional LLM-feedback upload (experiment; 3 days early)
2025-11-04  STOC deadline, 4:59pm EST
2026-02-01  decisions out (at the latest)
2026-02..03 accepted: corrections triage, ACM reformat, talk draft
            rejected: repair memo -> FOCS decision point
2026-03-31  camera-ready (AoE) + full version live on arXiv/ECCC
2026-04-01  FOCS 2026 deadline, 21:00 UTC (the other beat)
2026-06-22  STOC / TheoryFest week opens, Salt Lake City
2026-11-08  FOCS 2026 conference, New York
```

Print the equivalent table for the live year from the current CFPs before
using it; both venues move their dates by days-to-weeks between cycles.

## Ownership map for multi-author teams

Name one owner each for: proof verification, the twelve-page story, the
literature sweep, anonymity/format compliance, and the full-version release.
The two that slip when shared are verification ("I thought you checked Lemma
5") and the full version ("the arXiv update can wait") — both are
reputation-priced at this venue.

## Cycle-volatility warnings

- Deadlines, the guaranteed-read window, double-blind details, and any feedback
  experiments are re-set annually in the CFP; the TheoryFest format itself
  evolves (待核实 whether future editions keep the expanded-week structure).
- FOCS mechanics are set independently by the IEEE TCMF side; never infer one
  venue's rules from the other's.

## Output format

```text
[Current stage] proving / verifying / writing / submitted / decided / camera-ready
[Beat decision] STOC <year> / FOCS <year> / hold one cycle
[Backward plan] <next two milestones with dates>
[Corrections file] empty / <n> entries pending
[Owner map] <verification, story, literature, compliance, full version>
```
