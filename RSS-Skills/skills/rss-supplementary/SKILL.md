---
name: rss-supplementary
description: Use when assembling RSS (Robotics: Science and Systems) supplementary material under the separate one-week-later deadline — deciding what leaves the self-contained main PDF, cutting robot video that functions as evidence rather than promotion, anonymizing footage and archives, and packaging appendices and trial logs.
---

# RSS Supplementary

Assemble the supplement as the paper's evidence annex. RSS 2026 gave it its own
deadline (February 6, one week after the paper, AoE — verified 2026-07-08) and its
own constraint: the CFP requires the main PDF to be self-contained, so the supplement
may deepen belief but must never be *required* for it.

## The division of labor

| Content | Main PDF | Supplement |
|---|---|---|
| Claim, protocol summary, headline results, failure distribution | ✔ | |
| Full proofs / derivations | sketch | ✔ complete |
| Per-trial logs and extended tables | totals | ✔ raw |
| Robot footage | referenced | ✔ files |
| Code/data archive | availability sentence | ✔ archive |
| Anything a reviewer needs to *believe* the claim | ✔ always | never alone |

Litmus test per item: "if no reviewer opens the supplement, does the paper still
stand?" The 2026 rules make opening it discretionary, so plan for the case where
nobody does.

## Robot video as evidence, not trailer

The venue's culture reads supplementary video the way it reads tables — so cut it
like data, not like a launch video:

1. **Continuous takes for headline behaviors.** An uncut clip at stated real-time
   speed is the video equivalent of a raw log. Label any speed change on-screen; an
   unlabeled 4x cut reads as concealment once noticed.
2. **Show the failure modes.** Two or three representative failures, labeled by
   category, matched to the paper's failure table. This single choice most separates
   evidence-video from promo-video.
3. **Cover the conditions.** A clip per experimental condition beats a montage of the
   best condition; reviewers map video to the experiment matrix.
4. **No music, no title animations, no lab branding** — the last is an anonymity
   requirement, not just taste.

## Anonymization for physical media

Footage leaks identity through channels prose never has:

- Frame contents: faces, badges, lab signage, posters, distinctive robot liveries,
  window views. Crop, mask, or reshoot.
- File metadata: camera serials, GPS tags, creator fields in video containers, and
  archive paths embedding usernames — strip before packaging.
- Voice-over accents and names in ambient audio — prefer captions or replace audio.

## Archive hygiene

- One top-level README orienting a reviewer in under a minute: contents map, entry
  command, expected runtime.
- Include the trial ledger and analysis scripts (`rss-reproducibility`); exclude
  caches, checkpoints beyond the necessary, and any credential.
- Test the archive on a machine that has never seen the project; broken relative
  paths are the most common silent failure.
- Remember the ordering gift: the paper freezes first. The supplement week is for
  packaging existing evidence — footage shot after January 30 supports nothing the
  reviewers are judging.

## Video storyboard template

Draft the cut on paper before opening an editor:

```text
00:00-00:10  task + claim, one caption line (no narration needed)
00:10-01:10  headline behavior: ONE continuous take, "1x speed" on screen
01:10-01:50  one clip per experimental condition, captioned with condition ID
01:50-02:20  failure gallery: 2-3 labeled failures matching Table <n> categories
02:20-02:40  transfer/perturbation condition, uncut
02:40-end    (optional) mechanism visualization tied to a paper figure
```

Every segment maps to something in the PDF; anything that maps to nothing is
promotion and gets cut.

## What actually gets opened

| Item | Odds a reviewer opens it | Design consequence |
|---|---|---|
| Video file | High | Carry condition coverage + failures here |
| Appendix PDF | Medium | Mirror main-text section order; standalone-readable |
| Code archive README | Medium | One-minute orientation or nothing else gets read |
| Raw trial ledger | Low, but decisive when opened | Include; it settles protocol disputes |
| Checkpoints / large binaries | Very low | Ship recipes, not bulk |

## Cycle-volatile parameters

Size caps, allowed formats, and video length limits for 2026 were not publicly
surfaced (待核实); read them off the OpenReview submission form itself rather than
assuming any venue's conventions.

## Appendix craft

- Mirror the main text's section order and numbering scheme so a reviewer chasing
  "Appendix C from §4" lands without hunting.
- Open each appendix section with one sentence saying which body claim it deepens;
  orphaned appendix material is invisible under discretionary inspection.
- Restate the protocol being extended before extending it — the appendix is read
  days after the body, if at all.
- Full derivations, per-object result breakdowns, sensitivity sweeps, and extra
  qualitative figures belong here; the body keeps the sketch and the headline.
- Do not let the appendix quietly introduce new claims: anything claim-bearing
  that appears only in the supplement violates the self-containment rule from the
  reviewer's side of the table.

## Output format

```text
[Self-containment test] passes without supplement / fails: <item>
[Video cut] conditions covered <y/n> | failures shown <y/n> | speeds labeled <y/n>
[Anonymity sweep] frames / metadata / audio -> findings
[Archive check] README / entry command / clean-machine test
[Form limits] <caps from OpenReview form, or 待核实>
```
