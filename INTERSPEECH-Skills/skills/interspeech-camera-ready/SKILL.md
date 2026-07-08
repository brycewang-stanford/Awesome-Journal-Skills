---
name: interspeech-camera-ready
description: Use when an INTERSPEECH paper is accepted and the camera-ready, registration, and presentation chain begins — de-anonymizing for the ISCA Archive, restoring acknowledgments on the references page, meeting the author-registration requirement for proceedings inclusion, DOI metadata, and oral/poster preparation for the conference week.
---

# INTERSPEECH Camera-Ready

Acceptance at Interspeech starts a tight administrative chain: in the 2026 (Sydney)
cycle, notification landed 5 June and camera-ready closed **19 June** — two weeks.
The paper then enters the **ISCA Archive** (www.isca-archive.org), the open-access
proceedings library of the International Speech Communication Association, where
every Interspeech paper since 1987's Eurospeech lineage lives with a
`10.21437/Interspeech.<year>-<number>` DOI. Work from the live acceptance email and
author pages; the steps below are the recurring shape.

## De-anonymization, done in the right order

1. Restore author names, affiliations, and emails exactly as registered in CMT —
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
| Page count | Same 4+1 contract (Long Papers per their own rules) |

## The registration coupling

Interspeech ties proceedings inclusion to registration: **at least one author must
register (author registration) for the paper to appear in the proceedings and be
scheduled**. For 2026, early-bird pricing closed 15 July and standard registration
16 August. On today's calendar (2026-07-08) that makes registration, not the PDF,
the live deadline for accepted authors. Budget note: Interspeech has no
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
program-committee packing decision, not a quality verdict. For Sydney week
(27 September – 1 October 2026):

- Oral: speech slots are short (historically ~15 minutes with questions — confirm
  the program instructions); rehearse audio playback *through the room's chain*,
  and always carry a no-audio fallback slide with spectrograms.
- Poster: print audio QR codes linking to your (now public) sample page; a speech
  poster without listenable audio wastes the medium.
- Check visa lead times for the host country immediately at acceptance — Australia
  in 2026, Brazil in 2027.

## Release checklist tied to this milestone

```text
[ ] Camera-ready PDF uploaded, checker-clean, metadata matched
[ ] Author registration completed before the early-bird cutoff
[ ] Demo page and repository made public and linked in the paper
[ ] Preprint updated/de-anonymized now that the anonymity period ended
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

The dates in this skill are the verified 2026 chain (see
`resources/official-source-map.md`, checked 2026-07-08); the São Paulo 2027 cycle
will replace all of them.
