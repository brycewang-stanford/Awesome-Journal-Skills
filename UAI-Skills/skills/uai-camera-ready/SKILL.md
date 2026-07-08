---
name: uai-camera-ready
description: Use when converting an accepted UAI paper into its PMLR proceedings version, covering de-anonymization, final formatting against the UAI template, metadata for the PMLR volume, restoring public code and data links, poster and spotlight preparation for the conference, and sequencing work back from the camera-ready deadline.
---

# UAI Camera Ready

Use this after the acceptance email. In the 2026 cycle, notification was June 1 and
camera-ready files were due July 27, ahead of the August 17–21 conference in Amsterdam —
roughly eight weeks that also contain registration, travel, and poster production. Reopen
the current camera-ready instructions on the UAI site before starting; PMLR mechanics and
page allowances are settled per cycle and were not fully published at pack-verification
time (final-version page allowance: 待核实).

## Where the paper is going

Accepted UAI papers are published as a volume of the Proceedings of Machine Learning
Research. The series is open access with no author-side publication fee; the conference
is funded by registration. Recent anchors, useful for citing prior UAI work correctly
and for knowing what your own entry will look like: UAI 2021 = PMLR v161, 2022 = v180,
2023 = v216, 2024 = v244, 2025 = v286. The 2026 volume number is assigned by PMLR
(待核实 until the volume page exists).

```bibtex
@inproceedings{deshpande24a,
  title     = {Calibrated and Conformal Propensity Scores for Causal Effect Estimation},
  author    = {Deshpande, Shachi and Kuleshov, Volodymyr},
  booktitle = {Proceedings of the Fortieth Conference on Uncertainty in Artificial Intelligence},
  series    = {Proceedings of Machine Learning Research},
  volume    = {244},
  pages     = {1083--1111},
  year      = {2024},
  publisher = {PMLR}
}
```

Use this shape (verified against the PMLR v244 metadata) as the model for your own
eventual entry and for citing UAI papers in the camera-ready bibliography.

## De-anonymization pass

Reverse every anonymity measure deliberately rather than by memory:

- Restore the author block, affiliations, and correct ordering; cross-check against the
  OpenReview author list, which feeds proceedings metadata.
- Rewrite third-person self-references back to natural phrasing where it helps clarity.
- Reinstate acknowledgements and grant numbers that the submission rules forced out.
- Replace the anonymized supplementary archive with a public, versioned repository link;
  the CFP's strong encouragement of code and data release is easiest to honor now, when
  no anonymity constraint remains.
- Re-run metadata checks in reverse: the PDF should now carry the true title and authors.

## Reconciling with the review record

- Implement every change you committed to during the author-response phase; area chairs
  occasionally check, and co-authors always remember differently.
- Fold in reviewer-requested clarifications that fit without altering claims. Camera-ready
  is for sharpening accepted content, not for smuggling in new results.
- Keep a one-page changelog mapping each commitment to the section where it landed —
  useful internally and if chairs ask.

## Production checklist

| Item | Failure it prevents |
|---|---|
| Current-cycle UAI template, final (non-anonymous) mode | Volume-wide formatting mismatch flagged by proceedings editors |
| Title/abstract identical across PDF, OpenReview, and PMLR forms | Broken indexing and citation splits |
| Every appendix referenced from the main text still resolves | Dangling "see App. D" after camera-ready edits |
| Figures regenerated from final code | Plot-vs-table divergence in the archival version |
| License and copyright forms as required this cycle | Publication held back on paperwork (exact forms: 待核实) |
| Repository tagged with a release matching the paper | "Code link rots by conference week" failure |

## Presentation obligations

For 2026 the conference stated that all accepted papers are presented in poster sessions
and spotlight presentations, physically or remotely, with selected papers receiving
longer slots. Practical consequences:

- Prepare a poster and a short spotlight talk as the default; treat a longer oral as a
  bonus you learn about later.
- The physically-or-remotely wording is UAI 2026's; whether remote presentation remains
  available, and what registration category it requires, must be reconfirmed against the
  current attendance and registration pages (fees and mandatory-registration rules:
  待核实).
- Build the poster from the paper's inference story — the model, the assumption set, the
  guarantee or diagnostic, one decisive experiment — rather than shrinking eight pages
  onto A0.

## Small print that bites in July

- European venue logistics (2026: Amsterdam) put visa timelines on the critical path
  for many authors — start the invitation-letter process the week of notification.
- August conferences collide with European institutional holidays; confirm your
  co-authors' availability for the forms-and-proofread window before assuming it.
- Poster printing on-site versus shipping is a real decision at international venues;
  decide two weeks out, not on arrival.

## Sequence from acceptance to the conference

1. Week 1: changelog from review commitments; assign owners.
2. Weeks 2–3: text edits, restored identities, regenerated figures.
3. Week 4: public repository release, tagged and linked from the paper.
4. Weeks 5–6: PMLR forms and metadata; internal proofread of the merged PDF.
5. Before the deadline: upload, then re-download and cold-read the archived file.
6. Remaining weeks: registration, visa/travel if attending in person, poster print,
   spotlight rehearsal.

## Metadata consistency sweep

PMLR entries are generated from structured metadata, so one inconsistency propagates
to Google Scholar, DBLP, and every future citation. Sweep these pairs:

- [ ] PDF title ↔ OpenReview title ↔ PMLR form title (including math in titles,
      which PMLR renders from LaTeX — check the escaped form).
- [ ] Author name spellings and diacritics ↔ each author's canonical publishing name;
      a dropped accent forks a Scholar profile.
- [ ] Author order ↔ what the group actually agreed; camera-ready is the last cheap
      moment to fix it.
- [ ] Abstract in the form ↔ abstract in the PDF after final edits.
- [ ] Repository URL in the paper ↔ the tagged release, not the moving main branch.
- [ ] BibTeX self-entry drafted for your own website ↔ the volume's eventual format
      (model it on the verified entry above).

## Output format

```text
[Camera-ready state] not started / in edits / forms pending / uploaded
[Deadline distance] <days to current official camera-ready date>
[Commitment coverage] <review promises implemented / total>
[Public artifacts] repo tagged? data linked? license chosen?
[Presentation prep] poster / spotlight / long-talk status
```
