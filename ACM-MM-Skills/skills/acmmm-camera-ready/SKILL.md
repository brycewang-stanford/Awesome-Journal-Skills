---
name: acmmm-camera-ready
description: Use when preparing the ACM MM (ACM Multimedia) camera-ready version of record — de-anonymizing safely, completing the ACM rights form and CCS concepts, meeting ACM sigconf requirements, releasing code/data/media artifacts and any earned reproducibility badge, registering, and planning the oral/poster presentation in Rio.
---

# ACM MM Camera-Ready

Use this after acceptance to turn the reviewed PDF into the ACM Digital Library version of
record. Camera-ready is a distinct piece of work with its own deadline (reported August 6 for
2026) and its own failure modes — several of them ACM-specific.

## De-anonymization pass

The reviewed paper was anonymous (main track); the camera-ready is not. Reverse the blinding
carefully:

- Add author names, affiliations, and acknowledgements/funding.
- Restore "our previous work" phrasing and the real repository/dataset URLs.
- Replace the anonymous data/code mirror with the **permanent, public** archive (DOI).
- Re-check that no *anonymous-only* placeholder text survives.

## ACM publishing requirements

| Item | What to do |
|---|---|
| ACM rights form | Complete the eRights process; paste the returned rights block and DOI into the paper |
| CCS concepts | Add ACM Computing Classification System concepts and author keywords |
| sigconf compliance | Final PDF in the current ACM `sigconf` template; pass ACM's PDF/format check |
| Reference/overflow | References may occupy the extra pages; the body stays within the accepted length |
| Metadata | Title, authors, affiliations, and abstract match the ACM submission exactly |

The exact ACM rights/OA options (including ACM Open) are settled here; confirm the current
process (待核实 each cycle).

## Artifact and badge release

```text
code:    public repo + archived DOI, LICENSE, README with run instructions
data:    dataset card, license, access path (mirror or agreement)
media:   final demo video/audio, now de-anonymized, playable in open players
badge:   if the Reproducibility track awarded a badge, include the badge and artifact link
```

Camera-ready is when the public release replaces the anonymous review artifact — do not leave
the community pointing at a dead anonymous link.

## Registration and attendance

- At least one author must register by the deadline and present; confirm the current
  registration category and any presenter requirement.
- Check visa/travel needs for **Rio de Janeiro** early — international travel is the common
  logistical failure.

## Presentation prep by tier

- **Oral:** a talk that leads with the cross-modal contribution and *plays the media* — the
  audience should see/hear the seam your paper exploits.
- **Poster:** a single readable visual with the teaser, the mechanism, and one decisive
  media example; bring a device to play a short clip.
- Prepare captioned media that works offline; conference A/V and network are unreliable.

## The ACM eRights step, in order

```text
1. Receive the ACM eRights email after acceptance; complete the rights/permissions form.
2. ACM returns the rights block + DOI + the correct conference string.
3. Paste that block verbatim into the sigconf template (do not hand-edit it).
4. Add CCS concepts and keywords; run ACM's PDF format/preflight check.
5. Upload the final PDF and source where required, matching the registered metadata.
```

Skipping or mistyping the rights block is a frequent camera-ready bounce; treat the returned
text as fixed data, not prose to reword.

## Media for the ACM Digital Library

- Supplementary video/audio can accompany the DL record; provide the **de-anonymized** final
  versions in the accepted formats, captioned and playable in open players.
- Ensure the public artifact link in the paper resolves to the permanent archive, not the old
  anonymous review mirror.
- If a badge was awarded, include the ACM badge and the artifact DOI so the DL entry carries it.

## Final camera-ready checklist

- De-anonymized fully; rights block and DOI in place; CCS concepts added.
- sigconf format check passed; metadata matches ACM record.
- Public artifact archived and linked; any badge included.
- Registration done; presentation media prepared and offline-safe.

## Output format

```text
[De-anonymization] complete / residual anonymous text: <list>
[ACM publishing] rights + CCS + sigconf done / gaps: <list>
[Artifact release] public + archived / gaps
[Registration] done / pending
[Presentation] oral/poster plan ready / to do
[Blocking items] <ordered before the camera-ready deadline>
```
