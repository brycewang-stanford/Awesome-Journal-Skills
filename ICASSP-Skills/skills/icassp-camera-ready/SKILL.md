---
name: icassp-camera-ready
description: Use when preparing an accepted ICASSP paper for IEEE Xplore publication, covering the final 4+1 PDF, IEEE PDF eXpress validation, the IEEE electronic copyright form, integrating reviewer-requested fixes without changing the accepted claim, registration and in-person presentation, and choosing open-access options for the proceedings paper.
---

# ICASSP Camera Ready

Use this after acceptance. Reopen the current ICASSP camera-ready instructions, the IEEE author
kit, PDF eXpress, the copyright-form flow, and the registration and presentation pages before
advising authors. Because ICASSP is single-blind, there is **no de-anonymization step** — the
work is mostly compliance and polishing, not identity restoration.

## Camera-ready audit

- Apply the final format. ICASSP stays at the **4+1** shape for camera-ready in recent cycles;
  confirm the current page rule rather than assuming an extra page appeared.
- Run the final PDF through **IEEE PDF eXpress** to produce an Xplore-compatible file with fonts
  embedded; the portal rejects non-conforming PDFs.
- Complete the **IEEE electronic copyright form (eCF)**; without it the paper cannot enter Xplore.
- Fold in reviewer and committee fixes **without changing the accepted contribution** beyond
  normal clarification — camera-ready is not a place to add a new claim the reviewers never saw.
- Confirm the title, author list, affiliations, and metadata exactly match what registration and
  Xplore will index.

## What changes from submission to camera-ready

| Element | Submission | Camera-ready |
|---|---|---|
| Author block | Present (single-blind) | Unchanged — verify spelling, order, affiliations |
| Acknowledgements / funding | Optional, page 5 | Add or finalize on page 5 |
| PDF validation | eXpress pass to upload | eXpress pass again on the final file |
| Copyright | Not yet | IEEE eCF signed and attached |
| Reviewer fixes | n/a | Integrated within the accepted claim |
| Data/code links | May be present | Finalize public, citable links |

## Integrating a reviewer fix (worked example)

A reviewer asked that the operating SNR range be stated in the main text rather than left to a
figure. Camera-ready move: add one sentence to the experimental section naming the range, keep
the figure, and do **not** introduce a new condition or a new number — the accepted result is the
one that was reviewed. If a committee note requested a corrected reference or a clarified
equation, apply exactly that and nothing broader.

## Registration and presentation

- ICASSP requires **in-person presentation by a registered author**; at least one author must
  register, and a no-show can jeopardize the paper's inclusion or indexing.
- Prepare both an oral and a poster fallback where the format is not yet fixed, and build slides
  or a poster that a signal-processing audience can read at a glance (one claim, the mechanism,
  the key metric).
- For any audio, image, or video demo, test playback on the venue's hardware and keep a static
  fallback that survives without network or codecs.

## Open-access and publication path

- The standard proceedings paper is published in **IEEE Xplore**; ICASSP offers an **open-access
  option** for the proceedings paper (confirm the fee and mechanics in the current kit).
- If the work followed the **OJSP-ICASSP** track instead, publication is open-access in the IEEE
  Open Journal of Signal Processing and the paper is presented but **not** in the proceedings —
  a different copyright and camera-ready flow.
- Release the code, data, and any pretrained artifacts publicly and cite them from the final
  paper; single-blind review means the repository could already carry your name.

## Final checklist

```text
[Camera-ready status] ready / needs fixes / blocked
[Final package] PDF eXpress file / IEEE eCF / metadata / public artifacts
[Format] 4+1 confirmed for this cycle
[Reviewer-change map] <concern -> exact final edit within accepted claim>
[Registration] author registered / presentation format / demo fallback
[Publication path] Xplore proceedings (+ open access?) / OJSP-ICASSP
```

## Currency note

The 4+1 camera-ready shape, PDF eXpress, and IEEE copyright flow were checked 2026-07-09 against
ICASSP 2026 renderings (see `../../resources/official-source-map.md`). Registration pricing,
copyright mechanics, and exact camera-ready dates change every cycle — confirm against the
decision email and the current author kit.
