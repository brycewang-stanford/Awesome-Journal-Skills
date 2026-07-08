---
name: uist-supplementary
description: Use when producing the video figure and supplementary materials for a UIST submission — treating the 3-minute video as near-mandatory evidence in a demo-culture venue, scripting it around claims, meeting the 1080p/4K H.264 spec, anonymizing frames and audio, and deciding what else ships alongside the PDF.
---

# UIST Supplementary

At most venues supplementary material is an appendix annex. At UIST the central
supplementary object is the **video figure**, and it is closer to a second
first-page than to an attachment: reviewers at a venue built on demo culture watch
it early, form their belief about whether the system is real, and read the paper
through that belief. The 2026 Author Guide calls it optional but highly encouraged;
for any paper whose contribution moves, responds, or renders, treat "optional" as
theoretical.

## The 2026 video spec (verified 2026-07-08)

| Property | Requirement |
|---|---|
| Length | At most 3 minutes |
| Resolution | 1080p (1920×1080) or 4K (3840×2160) |
| Container/codec | MP4, H.264 |
| Anonymity | Same standard as the paper — frames, audio, and filenames |
| Role | Helps reviewers evaluate the submission |

Captions/subtitles make the video robust to reviewers watching without audio and
prefigure the accessibility work required at camera-ready (see `uist-camera-ready`).

## Script the video around claims, not features

Build the shot list from the paper's contribution list — the video is the visual
twin of `uist-experiments`' claim-evidence audit:

```text
0:00-0:15  Problem in one shot: the interaction that is impossible/painful today
0:15-0:45  The artifact working, uncut, on the core capability (claim C1)
0:45-1:45  C2..Cn each demonstrated in one continuous take
1:45-2:30  Breadth: 3-4 application vignettes, a few seconds each
2:30-3:00  Envelope honesty: one edge condition, then the closing capability shot
```

Production rules that pay at review time:

- **Real time by default.** Label any speed change on screen. Nothing erodes trust
  faster than suspecting a cut hides recognition latency.
- **Uncut interaction loops** for the core claim: input and response in the same
  frame — screen-plus-hands, or picture-in-picture.
- **No staged reactions or marketing gloss**; reviewers are builders, and polish
  that outruns the paper's measurements reads as concealment.
- **Consistency audit**: every capability shown must be measured or demonstrated in
  the paper; every headline claim in the paper should be visible in the video.

## Narration and captions

The soundtrack is argument, not atmosphere:

- Narrate **what the viewer is seeing and why it is hard**, in the paper's
  vocabulary — the video and the PDF should share their key terms so reviewers
  can cross-reference without translation.
- One sentence of narration per shot; silence over a working demo is stronger
  than filler ("as you can see, the system works well" convinces no one).
- On-screen labels for condition changes ("2× speed", "different user",
  "outdoor lighting") — reviewers treat unlabeled cuts as concealment.
- Captions verbatim from narration, timed to shots; they are how the video reads
  in a quiet review session and they seed the accessibility work that
  camera-ready requires anyway.
- No music under narration, no title-card branding that could hint at a lab's
  house style.

## Editing checklist before the spec check

```text
[ ] every cut between input and response is labeled or absent
[ ] each claim shot runs uncut for at least one full interaction loop
[ ] condition labels present for speed/user/environment changes
[ ] captions complete, spell-checked, synchronized
[ ] first 20 seconds show the artifact working (reviewers may not finish)
[ ] final frame is the capability, not a logo
```

## Anonymizing moving pictures

Video leaks identity through channels PDFs do not have:

- Frames: faces, badges, lab posters, whiteboards, distinctive rooms, license
  plates through windows.
- Audio: narrators saying "at our lab in...", recognizable voices; re-record or
  synthesize narration if needed.
- Overlays and assets: watermarks, usernames in menu bars, OS accounts, project
  names in window titles.
- Metadata: camera serials and GPS in the container.

```bash
# Spec + metadata check on the exact upload file
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height video.mp4
ffmpeg -i video.mp4 -map_metadata -1 -c copy video_clean.mp4   # strip container metadata
```

## Beyond the video: what else to ship

- **Anonymized overlap copy** — required in 2026 when a prior submission of yours
  overlaps heavily (see `uist-submission`); this is a UIST-specific obligation.
- **Code, firmware, and design files** — reviewed as evidence of reality; package
  them runnable-in-five-minutes (see `uist-artifact-evaluation`).
- **Extended results** — full benchmark grids, study instruments, codebooks; but
  anything decision-critical belongs in the PDF's appendix, since supplementary
  reading is at reviewer discretion.
- **A manifest** — one README listing every file and which paper section it backs;
  unlabeled archives simply do not get opened.

## Scheduling reality

Video production consumes the same final two weeks as paper polish and cannot start
before the system is stable. Book the capture rig, the edit pass, the caption pass,
and the compression/verification pass as calendar items at feature freeze
(`uist-workflow`), and dry-run the export pipeline early — render failures at 2 am
AoE are a recurring UIST deadline story.

## Output format

```text
[Video status] scripted / shot / edited / spec-verified / anonymized
[Claim coverage] video shows <k>/<n> contribution claims; gaps: <list>
[Spec check] duration · resolution · codec · captions · metadata
[Supplement set] <files + the section each supports>
[Risk] <the single most likely late failure in the pipeline>
```
