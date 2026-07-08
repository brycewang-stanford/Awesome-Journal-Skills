---
name: icra-supplementary
description: Use when planning ICRA supplementary material, which in this venue means primarily the video attachment — 180 seconds, 20 MB, submitted in fixed PaperPlaza windows — plus external code links; covers storyboarding, showing failures, anonymization of footage, and what may never live only outside the 6+2-page PDF.
---

# ICRA Supplementary

At most ML conferences "supplementary" means an unlimited appendix PDF. ICRA has
no such thing: the 2026-cycle rules cap the reviewed document at 6 content pages
plus 2 reference-only pages, with no appendix upload. What ICRA has instead is
the **video attachment** — a robotics-native evidence format with hard specs
(≤ 180 seconds, ≤ 20 MB, mpeg/mp4/mpg in 2026) and its own submission windows.
This skill treats the video as the serious scientific artifact it is.

## The self-containment rule

Because reviewers are not obligated to open anything beyond the PDF, and because
there is no appendix:

- Every load-bearing definition, equation, protocol detail, and result **must be
  in the 6 pages**. The video may demonstrate; it must never be the only place a
  claim is supported.
- External links (project page, code) are pointers to *optional corroboration*.
  Under the double-anonymous policy they must also be anonymized or omitted.
- The test: delete the video and all links mentally — does the paper still prove
  its claims? If no, restructure the body, not the supplement.

## What the video is for

Robotics reviewers watch the attachment early, often before reading past the
abstract. It answers questions text cannot:

| Reviewer question | Video answer |
|---|---|
| Is this real hardware or renders? | continuous, uncut executions |
| Is the demo cherry-picked? | multiple trials, varied conditions, a counter on screen |
| How fast is it really? | wall-clock timestamps, explicit "1× speed" labels |
| What does failure look like? | one or two failure clips with a caption naming the cause |
| Is a human secretly helping? | wide shots showing the full workspace and no puppeteer |

## Storyboard for 180 seconds

```text
0:00-0:10  title card: paper title only (no authors — double-anonymous)
0:10-0:30  task + platform in one wide continuous shot
0:30-1:30  core capability: 3-5 uncut executions, varied instances,
           on-screen labels: condition, trial number, 1× speed
1:30-2:10  the money comparison: baseline vs method, same task instance,
           side by side if possible
2:10-2:35  a failure case, honestly labeled with the taxonomy category
           from the paper's failure table
2:35-3:00  generalization montage (may be sped up — label "4×"),
           closing card pointing to the paper, nothing else
```

Rules the storyboard encodes: label every speed change (silent speed-ups are
treated as deception when caught); prefer uncut takes over montage for the core
claim; synchronize the video's trial conditions with the paper's tables so a
reviewer can cross-reference; show failure deliberately — it converts the video
from advertisement into evidence.

## Meeting 20 MB without looking like 2005

180 seconds under 20 MB means roughly 900 kbps total — tight but workable:

- Encode H.264 (in an mp4 container per the allowed formats), 720p, high-profile
  two-pass; drop the audio track entirely (narration goes into captions, which
  also survive muted review viewing and avoid voice de-anonymization issues).
- Avoid 60 fps; robotics motion reads fine at 24-30 fps and halves bitrate.
- Static title cards and captions compress to nearly nothing; noisy handheld
  footage does not — use a tripod, lock exposure.
- Verify the final file on the actual spec: duration ≤ 180 s, size ≤ 20 MB,
  extension among the allowed three, plays in a stock player.

## Anonymization of footage

Video leaks identity faster than text (2026-cycle double-anonymous rules):

- Sweep frames for lab posters, door signs, safety-vest logos, license plates,
  reflections in glass, and named equipment tags; blur or reshoot.
- No voice-over (voiceprints identify); no bystanders' faces without masking.
- Strip container metadata (`ffmpeg -map_metadata -1` on the final pass) — the
  encoder tag can carry a username.

## Project pages and external links

A public project page is standard robotics practice *after* acceptance but a
liability during double-anonymous review:

- If the page already exists (earlier arXiv release), do not link it from the
  submission; reviewers finding it on their own is tolerated, you leading them
  there is a violation pattern.
- An anonymized mirror (no lab name in domain or footer) may be linked if the
  cycle's rules permit external material at all — reread the current CFP.
- Plan the public page for acceptance week: paper, final video, artifact link,
  BibTeX with the IEEE Xplore DOI (`icra-camera-ready` stages this flip).

## Windows and logistics

In the 2026 cycle videos were accepted only during two windows (Aug 5-Sep 9 and
Sep 17-22, 2025, 23:59 Pacific) — note the second window closes *after* the paper
deadline, a grace period for editing but not for shooting. Bank raw footage
throughout the experimental campaign (`icra-reproducibility` ties clips to trial
logs); deadline-week shooting produces both worse videos and worse anonymity
discipline. Verify the current year's windows and specs on the year-site before
scheduling the edit.

## Pre-upload checklist

1. Paper passes the self-containment test with video deleted.
2. Storyboard beats present: uncut core, labeled speeds, comparison, failure.
3. Trial conditions on screen match table conditions in the paper.
4. Spec check: ≤ 180 s, ≤ 20 MB, allowed container, plays everywhere.
5. Anonymity sweep of frames, captions, metadata complete.
6. Upload inside the posted window; confirmation archived.

## Output format

```text
[Self-containment] pass / fail — claims living only in video: <list>
[Storyboard audit] uncut-core / speed-labels / comparison / failure: y/n each
[Spec] <s> s, <MB> MB, <container> — compliant: y/n
[Anonymity] frame sweep, captions, metadata: clean / leaks: <list>
[Window] target window <dates> — footage ready by: <date>
[Cross-reference] video trials ↔ paper tables consistent: y/n
```
