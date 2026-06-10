---
name: iclr-camera-ready
description: Use when preparing an accepted ICLR paper for camera-ready submission, OpenReview metadata, poster instructions, slide deck, project page, video, and publication logistics. Use when de-anonymizing the final PDF, folding in promised discussion-period fixes, confirming the camera-ready page allowance for the current cycle, or assembling poster and presentation assets for ICLR's poster-heavy program.
---

# ICLR Camera Ready

Use this after an ICLR acceptance. Reopen the accepted-paper emails, current Author Guide,
OpenReview camera-ready form, poster instructions, and registration instructions; accepted-paper
logistics are volatile and can differ from submission rules.

## Camera-ready checklist

- Apply the accepted-paper template and current camera-ready page limit. In 2026, discussion and
  camera-ready versions used a 10-page main-text allowance.
- Remove anonymity where required, add acknowledgments, and verify author names/order against
  OpenReview and the conference website source of truth.
- Preserve scientific claims from the reviewed paper. Do not turn a borderline acceptance into a
  substantially different paper.
- Resolve promised clarifications from author discussion, especially limitations, failed settings,
  baseline descriptions, and reproducibility notes.
- Complete OpenReview metadata, abstract, TL;DR, subject areas, conflicts, PDF, and supplementary
  uploads exactly as requested by the current form.
- Prepare poster metadata, poster upload, slide deck, optional project page, and video recording
  according to current poster instructions.

## Publication polish

- Make code/data links stable and public only when they no longer compromise anonymity.
- Check accessibility: readable figures, alt text where requested, colorblind-safe plots, captions,
  and poster legibility.
- Archive the reviewed submission, author discussion, final PDF, supplement, code release, and
  poster assets for later citation or journal extension work.

## Promise-tracking from the public thread

Because the review thread stays online next to the published paper, any reader can check whether you
delivered what you committed to during discussion. Build the camera-ready from that thread.

| Discussion-period promise | Camera-ready action | Reader check |
| --- | --- | --- |
| "Add the compute-matched control" | Insert and reference the table | Compare thread to final PDF |
| "Clarify the failed setting" | Add a limitations paragraph naming it | Search the PDF for the setting |
| "Code will be released" | Swap anonymous link for a public repo | Click the link |
| "Fix baseline X description" | Correct it and cite the source | Read the paragraph |

## Worked vignette

A diffusion-model paper is accepted as a poster. During discussion the authors promised to release
sampling code and to soften an overclaim about out-of-distribution generalization. For camera-ready
they de-anonymize, swap the anonymous repo for a public one with a frozen release tag, scope the OOD
claim to the tested shift types, and add a TL;DR. They keep the scientific claims identical to the
reviewed version so the meta-review still matches, and reuse the strongest ablation figure on the
poster with colorblind-safe colors.

## Reviewer-pushback patterns to close out

- "Accepted claim is broader than the evidence." Narrow the wording to the reviewed scope; do not
  let acceptance license a stronger headline than the reviewers saw.
- "Figures are unreadable on the poster." Re-export at poster scale and enlarge labels before upload.

## Output format

```text
[Camera-ready state] Ready / Needs fixes / Blocked
[OpenReview items] <PDF, metadata, supplement, conflicts, author order>
[ICLR.cc items] <poster, slides, video, project page>
[Scientific-change risk] low / medium / high
[Final fixes] <ordered list before upload>
```

