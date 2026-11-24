---
name: chi-supplementary
description: Use when assembling supplementary materials for an ACM CHI submission — the video figure with mandatory closed captions, appendices, study instruments, code and data archives — all due with the paper on the single September deadline, anonymized end to end, plus the camera-ready video preview.
---

# CHI Supplementary Materials

CHI collects the paper, the video figure, and every supplementary file **together on
the one submission deadline** (September 10, 2026 for CHI 2027, per chi2027.acm.org,
re-read 2026-11-24). There is no later supplement slot, so supplement production is
deadline-week work that must be scheduled like writing. Everything uploaded is part
of the anonymous review record; everything accepted ships to the ACM Digital Library
beside the paper, permanently.

## What goes where

| Material | Phase | Governing rule |
|---|---|---|
| Video figure (no hard limit at submission; ≤ 5 min recommended, 5 min max at publication-ready) | With submission | Anonymized; closed captions required |
| Appendices (instruments, extra tables, prompts) | With submission | Reviewed at reviewer discretion; paper must stand alone |
| Code / data archive | With submission | All non-video material as **one .zip with a README**; de-identified, anonymous, no `.git` history |
| Consent/IRB templates | With submission | Templated versions only — these files name institutions by design |
| Video preview (~30 s pitch) | Camera-ready (publication-ready deadline) | Accepted papers only; captioned; goes to DL and program |
| Final supplements | Publication-ready deadline | De-anonymized, captioned, archival quality |

The self-containment rule cuts across all of it: reviewers must be able to judge the
contribution from the PDF alone. Supplements deepen; they never carry a load-bearing
result.

## The video figure

SIGCHI's video guide (sigchi.org/resources/guides-for-authors/videos/) sets the
expectations this pack verifies: video figures illustrate key aspects of the work,
run up to about five minutes, are archived in the DL, and **every video needs a
closed-caption file** (SRT, SBV, or VTT). The CHI 2027 call sets no duration limit
for submission video figures but recommends staying within 5 minutes; the
publication-ready instructions cap the final video figure at 5 minutes. Craft rules that survive review:

- Show the interaction, not slides. Thirty seconds of real use beats two minutes of
  bullet points read aloud.
- Leave titles on screen long enough to read (the guide suggests up to ~10 seconds
  for video figures).
- Anonymize the audio track too: no narrator saying the lab's name, no institutional
  logos on walls or screens, no identifiable bystanders, and consent for every
  visible participant — including for eventual public archiving, not just review.
- Write the caption transcript yourself (or correct an auto-transcript line by
  line); auto-captions mangle technical vocabulary exactly where precision matters.
- Audio-describe or narrate what matters visually: the captions plus narration
  should let a listener who cannot see the screen follow the contribution.

```bash
# Video figure QA before PCS upload
ffprobe -v error -show_entries format=duration,size -of default=nw=1 videofigure.mp4
ffmpeg -i videofigure.mp4 -i videofigure.srt -c copy -c:s mov_text captioned.mp4
ffprobe -v error -select_streams s -show_entries stream=codec_name captioned.mp4  # captions present?
# Archive hygiene for the code/data supplement
zip -r supplement.zip supplement/ -x '*.git*' '*.DS_Store' '*node_modules*'
unzip -l supplement.zip | grep -Ei 'consent|irb|\.env|id_rsa|\.key' && echo "PURGE THESE"
```

## Anonymization has more surface area here than in the paper

The PDF gets proofread; supplements leak. Recurring channels, all desk-reject grade
(`chi-submission`): PDF/Office metadata inside appendix files, `.git` histories with
author emails, notebook outputs showing home-directory paths with usernames, OSF or
GitHub links registered to named accounts (use the platforms' anonymous-view
mechanisms), app-store links for the studied prototype, and consent forms with
letterhead. Sweep the exact files being uploaded, not the working copies.

## Structure the archive for a tired reviewer

One `README` at the root, mapping files to paper sections; instruments in one
folder; data dictionary beside the data; a one-command entry point for any code
(`chi-reproducibility` holds the transparency ladder). A reviewer gives the archive
five minutes — spend your effort on the first five minutes.

## The video preview (after acceptance)

The ~30-second preview is optional but disproportionately valuable: it plays on
YouTube and beside the DL record, and is how conference attendees choose sessions.
One idea, one strong visual, captioned, titles readable in ~4 seconds per the guide.
Produce it in February against the publication-ready deadline (2027-02-18), when the
camera-ready is stable — not in deadline-week September (`chi-camera-ready`).

## Cycle-volatile items

File-size caps and accepted formats for PCS uploads were not stated on the CHI 2027
call or publication-ready pages at the 2026-11-24 check (待核实). The CHI 2027 call
does fix the packaging: non-video supplements go in a single .zip with a README
describing the materials, and non-anonymized supplements desk-reject the whole
submission. Read the live "Guide to Submitting a Video" page for the cycle before
finalizing the package.

## Output format

```text
[Package] video figure ✓/✗ (captions ✓/✗) · appendix ✓/✗ · code/data ✓/✗ · README ✓/✗
[Self-containment] paper stands without supplements: yes/no
[Anonymity sweep] metadata · git history · links · audio track · footage consent — clean?
[Consent coverage] archival publication consent for all visible participants: yes/no
[Deferred to camera-ready] video preview · de-anonymized archives
[Blocking issue] <what stops upload today>
```
