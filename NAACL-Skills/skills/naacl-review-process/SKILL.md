---
name: naacl-review-process
description: Use when reasoning about how a NAACL decision actually gets made — the division of labor between ACL Rolling Review (reviews, meta-review) and the NAACL program committee (commitment-stage acceptance into Main or Findings), where author leverage exists at each stage, and how the skipped-year calendar shapes committee behavior.
---

# NAACL Review Process

NAACL outsources reviewing and keeps deciding. Understanding which body owns
which judgment tells you where effort pays and where it evaporates.

## The two-stage machine

**Stage 1 — ARR (weeks 0-10 of a cycle).** Three or more reviewers score
the paper; an action editor synthesizes a meta-review. ARR produces an
assessment, not an acceptance: nothing is "in" anywhere yet. Authors see
everything and may respond mid-cycle or carry the package away.

**Stage 2 — NAACL commitment.** Authors forward the frozen package (paper,
reviews, response threads, meta-review) to NAACL through OpenReview by the
edition's commitment deadline. The chapter's senior area chairs and program
chairs then sort committed papers into Main, Findings, or reject. No new
reviews are commissioned in the normal path; the SACs reread what exists.

Consequences worth internalizing:

- Your reviews are portable. A package that misses one NAACL can commit to
  a later *ACL venue — or, since NAACL skips years, may *have* to.
- The response window is your only chance to change the text of the record;
  commitment is argument-free (aside from brief venue-specific forms some
  editions allow — verify per edition).
- Score-hunting via immediate resubmission is policed: ARR requires linking
  prior submissions with change summaries, and low meta-review scores can
  restrict quick re-entry.

## What each actor optimizes

| Actor | Reads | Optimizes for | Your lever |
|---|---|---|---|
| ARR reviewer | Your paper, 4-6 others | Defensible scores, low effort | Content pages that answer the standard doubts preemptively |
| Action editor | Reviews + response | A meta-review that survives scrutiny | Response threads that end in quotable resolutions |
| NAACL SAC | Dozens of frozen packages | A balanced program under an acceptance budget | The meta-review's final tone; venue-fit signals |
| Program chairs | SAC recommendations | Program shape: topics, tracks, theme coverage | Topic/theme alignment declared honestly |

## Main versus Findings, mechanically

Both outcomes publish in the ACL Anthology and both count as archival.
The split is a program-capacity decision made at commitment: papers judged
sound but not slotted into the main program land in Findings of NAACL.
Editions differ on what presentation Findings papers receive. Strategic
implication: soundness objections are deadly (they block both tiers), while
excitement objections often decide only *which* tier — triage your response
accordingly.

## The skipped-year effect on committee behavior

Because the chapter stands down when ACL meets in the Americas (no 2023, no
2026 edition), each NAACL arrives after a gap in which reviewed-but-uncommitted
packages accumulate. Expect commitment windows with unusually deep pools and
SACs choosing among multiple cycles' worth of papers. Practical reading: a
merely adequate package faces more competition at NAACL commitment than the
same package would at an annual venue's, and freshness of the reviews (did
the field move since?) becomes a real, if unwritten, factor.

## One package's path through the machine

A concrete trace, using the NAACL 2025 shape (October 2024 ARR cycle) as
the historical example:

1. Mid-October: anonymous PDF enters the ARR cycle on OpenReview.
2. Early November: compliance screening; desk rejections notified.
3. November: three reviews written; author response window opens after
   release.
4. Mid-December: meta-review synthesized; the package is now complete and
   frozen — this exact bundle is what every later reader sees.
5. Turn of the year: authors commit the package to NAACL 2025 (or hold it,
   or take it elsewhere; the reviews do not expire with the cycle).
6. January: SACs rank committed packages; program chairs set the
   Main/Findings/reject lines under capacity constraints.
7. Early February: final versions due for both acceptance tiers.
8. Late April: Albuquerque.

The dates move every edition; the topology — review once, decide
elsewhere, publish per tier — has been stable since NAACL adopted ARR
exclusively.

## Reading a review packet for stage 2

```text
For each review:
  score_axis   -> soundness-type or excitement-type objection?
  fixability   -> answerable from existing evidence / in-window run / no
  sac_optics   -> how does this line read to a skimming SAC?
Then: response effort = (sac_optics severity) x (fixability),
      not (how annoyed the review made you).
```

## Stage-by-stage leverage summary

1. **Before upload:** venue-preference and language/topic fields shape which
   reviewer pool and eventual SAC lane you enter.
2. **Response window:** the only writable moment; optimize the record.
3. **Commitment:** choose venue and timing — the one strategic decision that
   is entirely yours.
4. **After decision:** Main/Findings handling and, if rejected, a revise-and
   -resubmit into a later cycle with a truthful change summary.

## Output format

```text
[Stage] ARR reviewing / response / awaiting commitment / committed / decided
[Package strength] <meta-review tone + score pattern in one line>
[Objection split] soundness: <n> / excitement: <n>
[Commitment options] <NAACL edition vs sibling venues, with dates>
[Recommended play] <one action with rationale>
```
