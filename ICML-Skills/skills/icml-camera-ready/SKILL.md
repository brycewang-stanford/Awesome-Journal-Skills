---
name: icml-camera-ready
description: Use when preparing accepted ICML papers for camera-ready upload, PMLR agreement, public OpenReview record, lay summary, conflict disclosure, registration/presentation choices, format checker, and post-conference revision.
---

# ICML Camera-Ready

Use this after acceptance. ICML camera-ready work is unusually tied to public accountability because
accepted papers publish the original submission, supplementary material, reviews, meta-reviews,
rebuttal, and reviewer-author discussion along with camera-ready.

## Official items to reopen

- Current Author Instructions and camera-ready checklist.
- OpenReview camera-ready form.
- Current ICML style file and format checker.
- PMLR publication agreement and ICML release forms.
- Registration, presentation, proceedings-only, poster/oral, and post-conference revision rules.

## 2026 baseline

ICML 2026 camera-ready instructions require upload by May 28 AoE, allow a 9-page paper body, limit
the camera-ready PDF to 20MB, require appendices in the PDF, provide no camera-ready supplementary
material, ask for a lay summary, and require the format-checker code. They also introduce a
financial conflict-of-interest disclosure rule for relevant cases.

## Workflow

1. Decide whether the paper is in-person or proceedings-only and complete the required
   presentation/registration questionnaire.
2. Convert the anonymous submission into a public paper: authors, acknowledgments, funding, code,
   datasets, and repositories.
3. Incorporate reviewer/AC feedback without changing the essential accepted contribution.
4. Move all final appendices into the PDF; use public repositories for code/data instead of final
   supplementary material.
5. Enter lay summary, title, abstract, author metadata, code URL, PMLR agreement, and release forms.
6. Run the format checker and keep the successful code.
7. Plan post-conference small corrections if needed.

## Public-record exposure map

What becomes visible on OpenReview for accepted ICML papers is broader than for many venues, so plan
the deanonymization with that in mind.

| Item | Visibility after acceptance | Action |
| --- | --- | --- |
| Original anonymous submission | Public | Ensure it still reads honestly next to the final paper |
| Reviews, meta-review, rebuttal, discussion | Public | Keep rebuttal claims consistent with camera-ready edits |
| Lay summary | Public-facing | Write for a non-specialist, avoid jargon |
| Financial conflict disclosure | Required where relevant | Confirm and complete for the current cycle |

## Worked vignette: shipping the optimizer paper

The accepted optimizer paper moves all appendices into the single PDF, deanonymizes authors and
funding, links the public code repository in the OpenReview code URL field, and writes a lay summary
explaining "a faster training rule" without the convergence notation. The team runs the format
checker and keeps the passing code, then double-checks that the rebuttal's promised in-regime plot
actually appears, because both the rebuttal and the final paper are now public. Treat exact dates and
page limits as annual; the 2026 baseline above should be re-verified against the current checklist.

## Output format

```text
[Camera-ready status] Ready / Needs fixes
[Public-record risks] <original submission/supplement/reviews/rebuttal visibility issue>
[Required uploads/forms] <PMLR/release/forms/format checker/lay summary>
[Artifact release] <repo/archive/code URL/data>
[Post-conference revision plan] <none or small corrections>
```

