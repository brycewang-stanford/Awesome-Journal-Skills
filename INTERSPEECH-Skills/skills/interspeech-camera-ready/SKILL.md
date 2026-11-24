---
name: interspeech-camera-ready
description: Use when an INTERSPEECH paper is accepted and the camera-ready, registration, and presentation chain begins — de-anonymizing for the ISCA Archive, restoring acknowledgments on the references page, meeting the author-registration requirement for proceedings inclusion, DOI metadata, and oral/poster preparation for the conference week.
---

# INTERSPEECH Camera-Ready

Acceptance at Interspeech starts a tight administrative chain: in the 2027 (São Paulo)
cycle, notification lands 2 June and camera-ready closes **9 June 2027** — one week
(2026, Sydney: 5 June → 19 June, two weeks).
The paper then enters the **ISCA Archive** (www.isca-archive.org), the open-access
proceedings library of the International Speech Communication Association, where
every Interspeech paper since 1987's Eurospeech lineage lives with a
`10.21437/Interspeech.<year>-<number>` DOI. Work from the live acceptance email and
author pages; the steps below are the recurring shape.

## De-anonymization, done in the right order

1. Restore author names, affiliations, and emails exactly as registered in the
   submission portal (CMT in 2025–2026) —
   the metadata feeds the Archive entry and the DOI record.
2. Reinstate acknowledgments and funding on the references/acknowledgments page —
   that is the only page that may hold them, and it still may hold nothing else.
3. Convert anonymized self-citations back to first person where it reads naturally.
4. Replace anonymous demo/repository links with the permanent public ones you
   actually intend to maintain (see `interspeech-artifact-evaluation`).
5. Re-run the paper kit's PDF checker; camera-ready uploads are validated too.

## What may change vs. what may not

| Change | Status at camera-ready |
|---|---|
| Fixes promised in the rebuttal | Expected — reviewers' one leverage point |
| Typos, figure quality, reference completeness | Welcome |
| Title or author list | Restricted; usually requires chair approval |
| New experiments that alter claims | Not sanctioned — the accepted content was reviewed |
| Page count | Same 4 + 2 contract in 2027 (Long Papers 8 + 2) |

## The registration coupling

Interspeech ties proceedings inclusion to registration: **at least one author must
register (author registration) for the paper to appear in the proceedings and be
scheduled**, and an author must present it in person (2027 call). For 2026,
early-bird pricing closed 15 July and standard registration 16 August, and one full
registration covered up to four papers; the 2027 tiers were not yet published on
2026-11-24 (待核实). Budget note: Interspeech has no
article-processing charge — the ISCA Archive is open access — so registration and
travel are the real costs.

## Metadata hygiene for the Archive

- Title/abstract in the portal must match the PDF character-for-character; the
  Archive page, DOI record, and indexing are generated from the metadata.
- Check diacritics and name ordering — speech is a global community and the Archive
  preserves what you type forever.
- Keywords/index terms should use community vocabulary (the terms people search the
  Archive with), not project branding.

## Presentation planning (the part teams forget)

Accepted papers are scheduled as **oral or poster**; at Interspeech the mode is a
program-committee packing decision, not a quality verdict (Long Papers are explicitly
labelled as such in 2027). For São Paulo week (29 August – 2 September 2027):

- Oral: speech slots are short (historically ~15 minutes with questions — confirm
  the program instructions); rehearse audio playback *through the room's chain*,
  and always carry a no-audio fallback slide with spectrograms.
- Poster: print audio QR codes linking to your (now public) sample page; a speech
  poster without listenable audio wastes the medium.
- Check visa lead times for the host country immediately at acceptance — Brazil in
  2027 (Australia in 2026).

## Release checklist tied to this milestone

```text
[ ] Camera-ready PDF uploaded, checker-clean, metadata matched
[ ] Author registration completed before the early-bird cutoff
[ ] Demo page and repository made public and linked in the paper
[ ] Preprint updated/de-anonymized (no anonymity period in 2026; check the 2027 policy)
    (cite the Interspeech version with its 10.21437 DOI once assigned)
[ ] Presentation mode confirmed; audio fallback prepared
[ ] Travel/visa started; presenting author named
```

## Recurring camera-ready mistakes at this venue

- Restoring authors in the PDF but forgetting the portal metadata (or vice
  versa) — the Archive publishes the mismatch.
- Acknowledgments spilling past the references page's legal scope, or landing on
  page 4 and pushing content over the limit.
- Leaving `anonymous.4open.science`-style review links in the final PDF instead
  of the permanent repository.
- Missing the registration cutoff on the assumption that uploading the PDF was
  the whole job — the proceedings entry silently depends on a registered author.
- Citing your own paper's arXiv version in follow-ups forever because nobody
  recorded the 10.21437 DOI when it was assigned.

## The two-week sprint, scheduled

| Day (from notification) | Task |
|---|---|
| 0–2 | Read the meta-review; list promised changes; assign one owner |
| 3–6 | Apply promised fixes; de-anonymize in the order above |
| 7–9 | Fresh-eyes proofread; PDF checker; metadata cross-check |
| 10–12 | Upload; verify the portal's stored copy; register the presenting author |
| 13–14 | Buffer for the checker rejecting fonts or margins — it happens |

## Output format

```text
[Camera-ready status] not started / drafted / uploaded / confirmed
[De-anonymization] names / acks / links / self-citations — done or pending
[Registration] type, holder, deadline vs today
[Archive metadata] match check result
[Presentation] oral or poster, rehearsal state, audio fallback
[Next hard date] <date + what it gates>
```

The dates in this skill are the Interspeech 2027 chain read on the official call
(see `resources/official-source-map.md`, re-verified 2026-11-24), with 2026 kept for
comparison; registration tiers for 2027 are still to be published.
