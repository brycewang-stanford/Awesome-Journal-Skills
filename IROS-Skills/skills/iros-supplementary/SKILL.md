---
name: iros-supplementary
description: Use when preparing the IROS video attachment as evidence — the 60-second/10 MB limit, its own deadline, storyboarding uncut real trials and labeled failures, showing playback speed honestly, anonymizing footage under the double-anonymous cycle, and compensating for the fact that IROS provides no supplementary PDF.
---

# IROS Supplementary

At IROS the "supplement" is essentially **one short video**, not an appendix. There is no supplementary
PDF, so the video is the only extra channel — and IROS caps it tighter than its siblings. Treat it as a
piece of evidence a reviewer watches *before* reading, not as a highlight reel.

## The video envelope (2026 anchor — reverify)

- **Length:** up to 60 seconds. This is half of ICRA's window; a video cut for ICRA must be re-edited,
  not merely re-uploaded.
- **Size:** up to 10 MB. Encode for clarity within the cap rather than shipping a soft 60 MB export.
- **Format:** mpg / mpeg / mp4.
- **Deadline:** its own date (2026: March 5), a few days after the paper — plan for it separately.

## What earns its 60 seconds

- **Uncut real trials.** One or two continuous takes of the system doing the task on the real robot beats
  a montage of cuts that hides the seams.
- **At least one labeled failure.** Showing a failure and naming it builds more trust than an unbroken
  string of successes, which reviewers read as cherry-picked.
- **Honest playback speed.** Caption any speed-up ("4x") on screen; silent time compression is a
  credibility leak.
- **Legible conditions.** A caption stating the platform, the task, and that trials are representative
  orients the viewer in the first seconds.

## Storyboard for a 60-second cut

| Seconds | Content | Purpose |
|---|---|---|
| 0-8 | Title card: task, platform, "representative trials"; no author/lab identity | Orient without leaking identity |
| 8-35 | One or two uncut successful trials at honest speed | Show the system actually runs |
| 35-50 | One labeled failure with its cause on screen | Prove honesty; preempt skepticism |
| 50-60 | A condition sweep or second environment, if it fits | Show it is not one lucky setting |

## Anonymizing footage (2026 double-anonymous cycle)

- Crop or blur institute banners, door signs, logo'd safety vests, and building-specific scenery.
- Strip identifying audio (a named voice, a lab intercom) — mute or replace with captions.
- Check file metadata and the filename for author or organization strings before upload.
- Remove any on-screen URL that carries a lab organization name.

## Compensating for the missing PDF supplement

Because there is no appendix, decision-critical material cannot live "in the supplement." The metric
definition, the trial protocol, and the key ablation must be in the paper body. Use the video to *show*
behavior, not to *carry* an argument the body omits — a reviewer who mutes the video should still be able
to evaluate the contribution.

```text
Pre-upload video check:
  duration <= 60 s ?      size <= 10 MB ?      format mp4/mpg/mpeg ?
  uncut real trial shown ?   >=1 labeled failure ?   speed captioned ?
  no lab identity in frames, audio, filename, or metadata ?
  plays on a machine without lab codecs ?
```

## Output format

```text
[Video status] Ready / Needs fixes / Not ready
[Envelope] <s>s / <MB>MB / format / deadline ok?
[Evidence quality] uncut trials? failure shown? speed honest?
[Anonymity] frames/audio/metadata/filename checked?
[Body dependency] what argument must move from video into the paper body?
```
