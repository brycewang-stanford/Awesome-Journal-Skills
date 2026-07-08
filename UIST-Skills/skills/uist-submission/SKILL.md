---
name: uist-submission
description: Use when performing the final pre-upload audit of a UIST paper in PCS — the abstract-then-paper deadline pair, 10-page/5-page two-column limits with desk-reject enforcement, anonymous acmart options, video-figure and supplementary uploads, the prior-work overlap rule, and deadline-week sequencing.
---

# UIST Submission

This is the audit to run in the final week before the Papers deadline. Numbers below
are the verified 2026 cycle (checked 2026-07-08 via search renderings of
`uist.acm.org/2026/`, direct fetch blocked): abstracts March 24, papers March 31,
both 11:59 pm AoE. The 2026 deadline has passed — apply this skill to a 2027
submission only after re-reading that year's Author Guide, and expect the numbers to
move.

## What PCS collects, and when

UIST runs on PCS (Precision Conference Solutions): in the submission form, choose
society "SIGCHI", conference "UIST 2026", track "UIST 2026 Papers". Two deadlines
structure the week:

1. **Abstract deadline (one week out).** Title, abstract, author list, and metadata
   must exist in PCS. This gates reviewer assignment — a placeholder abstract that
   drifts from the final paper lands you with mismatched reviewers, the least
   fixable submission error.
2. **Paper deadline.** The PDF, the video figure, and all supplementary files.
   Everything reviewed arrives now; there is no later supplement slot.

## Format gate

| Check | 2026 rule | Enforcement |
|---|---|---|
| Template | Two-column `acmart`, `\documentclass[sigconf,review,anonymous]{acmart}` | Manual + visual |
| Body length | 10 pages (standard) or 5 pages (short), excluding references and appendices | **Desk reject if exceeded** |
| Appendices | Inside the same PDF, after references; body must stand alone | Review-stage damage |
| Video figure | Optional, strongly encouraged: ≤ 3 min, 1080p/4K, MP4 H.264 | Reviewer-side (see `uist-supplementary`) |
| Anonymity | Paper, video, and supplement all purged of identity | Desk reject |

A short paper is a distinct category (smaller complete contribution), not a truncated
standard paper — do not switch categories on deadline night to dodge the page count.

## Anonymity, the UIST version

The standard is "reasonable effort," with two venue-specific twists:

- **Third-person self-citation with full references.** Do not redact your own
  citations; write about your prior work as if someone else built it.
- **Overlap attachment.** If a prior submission of yours overlaps significantly,
  upload an anonymized copy of it as supplementary material.

Sweep everything that ships: PDF text, PDF metadata, acknowledgements and grant
numbers, repository and project-page URLs, video frames (lab posters, faces,
institutional wallpaper), video audio (narrator self-identification), file names,
and archive contents.

```bash
# Mechanical pass over the actual upload set
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github|gitlab|osf\.io|acknowledg|grant' | head
ffprobe -v error -show_entries format=duration:stream=width,height,codec_name video.mp4
unzip -l supplement.zip | grep -Ei '\.git|DS_Store|/Users/|/home/' | head
```

## Deadline-week order of operations

1. **T-7d:** abstract deadline — final title/abstract in PCS, authors and conflicts
   complete, subject metadata chosen for reviewer routing.
2. **T-5d:** body frozen at the page limit; appendix absorbs the overflow.
3. **T-4d:** video locked (edits, captions, anonymization) and compressed to spec;
   verify PCS accepts the file size early, since caps were not published (待核实).
4. **T-2d:** full anonymity sweep on the merged PDF, video, and archive; run the
   mechanical checks above on the exact files to be uploaded.
5. **T-1d:** upload everything, then re-download from PCS and open cold — the
   re-downloaded copy is what reviewers see. Confirm the PCS abstract matches the
   PDF abstract word for word.
6. **T-0:** buffer only. AoE means UTC-12; convert once, write it on the wall.

## PCS form fields worth drafting early

The form is read before the PDF and configured per track; draft its contents days
ahead rather than composing in the upload session:

- **Title and abstract** — identical to the PDF, since the abstract drives
  reviewer matching from the abstract deadline onward.
- **Author list and conflicts** — complete at abstract time; adding authors later
  in the process is at minimum awkward and possibly restricted (待核实 per cycle).
- **Subject/topic descriptors** — choose for the reviewer pool you want; a
  fabrication paper tagged only "AI" gets AI reviewers.
- **Prior-submission declarations** — where the form asks about overlapping or
  previously reviewed material, answer literally; this is also where the
  anonymized overlap attachment gets referenced.
- **Track category** — standard vs short is a claim about contribution scale;
  reviewers hold you to the category you picked.

## Last-day failure modes, ranked by frequency

| Failure | Prevention |
|---|---|
| Video upload stalls or exceeds an unpublished cap | Upload media a full day early; keep a lower-bitrate export ready |
| Final LaTeX rebuild shifts the paper past the limit | Freeze the body two days out; late edits go to the appendix |
| PDF metadata carries an author name from a home template | Mechanical sweep on the exact export, every export |
| PCS abstract diverges from a last-minute PDF abstract edit | One person owns both texts; diff them at T-1d |
| A co-author's "tiny fix" reintroduces an acknowledgements block | Lock the repo after the anonymity sweep |

## Dual-track and dual-venue rules

- Papers under review elsewhere may not be under review at UIST at the same time.
- Within UIST 2026, the same work sent to both Demos and Posters is treated as a
  demo submission and rejected from Posters — pick one adjunct lane deliberately.
- A prior adjunct publication (demo/poster abstract) of the same system does not
  anonymize away: cite it in the third person and state the delta.

## Output format

```text
[Submission status] ready / blocked / at risk
[Format gate] pages <n>/<limit> · template ok? · video spec ok?
[Anonymity sweep] clean / leaks: <file: location>
[PCS state] abstract locked · uploads verified by re-download? 
[Remaining actions] <ordered, with owner and hour>
```
