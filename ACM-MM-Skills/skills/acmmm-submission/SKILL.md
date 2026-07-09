---
name: acmmm-submission
description: Use when auditing an ACM MM (ACM Multimedia) submission for OpenReview readiness — thematic-area choice, the 6-8 page ACM sigconf budget, references-only overflow, double-blind anonymity versus the single-blind Reproducibility/Open-Source/Dataset tracks, supplementary media, dual submission, desk-reject triggers, and last-week sequencing.
---

# ACM MM Submission

Use this to run a pre-deadline audit of an ACM Multimedia paper. Reopen the current Call
for Technical Papers, the Topics of Interest page, each relevant track call, and the
OpenReview group before giving deadline-ready advice — ACM MM rewrites these each edition.

## Submission audit

- Confirm the target is the ACM MM **main conference** (or a specific track), not a
  co-located workshop, ACM MM Asia, MMSys, or ICMR.
- Choose the **thematic area** deliberately: it routes the paper to a reviewer pool, and a
  mismatched area is a quiet source of off-topic reviews.
- Apply the current **ACM `sigconf`** template with no margin, font, or spacing edits. ACM
  MM 2026 used a **6–8 page** body; references may spill onto up to two additional pages
  that contain *only* references.
- Enforce double-blind anonymity across the paper, appendix, supplement, code, media
  assets, filenames, PDF metadata, and repository links — **unless** submitting to the
  named single-blind tracks (Reproducibility, Open Source Software, Dataset), where the
  artifact's identity is expected.
- Register the abstract before the abstract deadline; the paper and the supplement have
  their own later deadlines (in 2026: abstract Mar 25, paper Apr 1, supplement Apr 8, AoE).
- Check concurrent-submission rules and prior-publication status; do not keep the same work
  under review at another archival venue when ACM MM forbids it.

## Blocking risks

- Late abstract registration or paper upload.
- Overlength body or a tampered sigconf template.
- Identity leak in the PDF, media metadata, demo watermark, or repository link (on a
  double-blind track).
- Wrong track blinding — anonymizing a Dataset/Open-Source submission, or de-anonymizing a
  main-track one.
- Non-rendering or proprietary-format supplementary media.
- Dual submission to another archival venue.

## Desk-reject and triage table

| Trigger | Severity at ACM MM | Repair window |
|---|---|---|
| Overlength body (past 8 pages) | Desk reject | None after the deadline |
| Non-references content on the overflow pages | Desk reject or chair flag | Before the deadline only |
| Author identity in a double-blind PDF/media | Desk reject | None |
| Wrong thematic area | Off-topic reviews, not a desk reject | Fixable before the paper deadline |
| Supplement that will not play for a reviewer | Lost evidence | Fixable before the supplement deadline |
| Missing OpenReview coauthor profiles | Submission blocked | Before the deadline |

## Last-week sequence for a cross-modal paper

1. Freeze the thematic-area choice and confirm the paper's claims match that area's scope.
2. Re-render every figure and media clip from scripts so body, supplement, and PDF agree.
3. Anonymize media: strip author names from filenames, EXIF/metadata, and any on-screen
   watermark, and route dataset/demo links through an anonymous mirror.
4. Confirm the OpenReview abstract matches the PDF abstract word for word.
5. Verify the body fits 8 pages with the overflow pages holding references only.

## OpenReview mechanics that trip people up

ACM MM runs on OpenReview, but the failure modes are administrative, not intellectual:

- Every coauthor needs a **complete OpenReview profile** with a real institutional history, or
  the submission is blocked or the conflict graph is wrong.
- The **abstract** is registered before the paper — a separate, earlier deadline. Missing it
  forecloses the paper deadline entirely.
- Declare **conflicts** honestly; an undeclared conflict discovered later can sink a paper.
- The **thematic area** is set at submission and is hard to change afterward; it selects your
  reviewers, so treat it as a first-class decision, not a dropdown afterthought.

## Track and blinding double-check

The most ACM MM-specific desk-reject cause is submitting to the wrong track's blinding regime.

| If you are submitting to... | Blinding | So the PDF must... |
|---|---|---|
| Main track / Brave New Ideas | Double-blind | Hide all author identity, in text, media, and links |
| Reproducibility track | Single-blind | Name the artifact and its authors as expected |
| Open Source Software Competition | Single-blind | Present the real project and repository |
| Dataset track | Single-blind | Identify the dataset and its providers |

Anonymizing a single-blind submission (or de-anonymizing a double-blind one) both signal that
the authors did not read the track call — fix it before upload, not after.

## Format anchors

- ACM MM's two-column sigconf layout compresses hard: wide multimodal figures, algorithm
  blocks, and qualitative media grids overflow the 8-page body, so budget page space as a
  design decision early, not on deadline night.
- The page counts, deadlines, and track blinding cited here describe the 2026 cycle; treat
  every number as provisional and recheck the current CFP and track calls before relying on
  it.

## Output format

```text
[ACM MM readiness] Ready / Needs fixes / Not ready
[Track + thematic area] <main/BNI/dataset/... + area>
[Blocking checks] <OpenReview/page/anonymity/media/dual-submission>
[Cross-modal evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
