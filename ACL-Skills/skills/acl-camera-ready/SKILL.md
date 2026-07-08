---
name: acl-camera-ready
description: Use when preparing an accepted ACL main-conference or Findings paper for camera-ready, covering the extra content page, de-anonymization and acknowledgements, AI-assistance disclosure, keeping the Limitations section, ACL Anthology metadata and CC BY 4.0 publication, meta-review-driven edits, and presentation-mode logistics.
---

# ACL Camera Ready

Use this after ACL (or Findings of ACL) acceptance. Camera-ready quality
controls how the paper looks forever in the ACL Anthology, which is the
permanent open-access record. For ACL 2026 the camera-ready deadline was
April 19, 2026 — confirm the current edition's date in the acceptance email
before planning anything.

## The extra page and what it is for

- Accepted \*ACL papers traditionally receive one additional content page:
  long papers up to 9 pages, short papers up to 5. The page exists to address
  reviewer and meta-review comments, not to smuggle in a new contribution.
- Spend it in priority order: fixes the meta-review asked for, clarifications
  reviewers requested, then de-anonymization overhead (author block,
  acknowledgements) which consumes real space.
- References remain unlimited; the Limitations section remains **mandatory**
  in the camera-ready and still sits outside the page count.

## De-anonymization pass

- Restore authors, affiliations, and acknowledgements; convert third-person
  self-citations ("Smith showed") back to natural first person where clearer.
- Replace anonymous supplement links with the permanent public repository,
  dataset page, or model card; test every URL logged out.
- Add the funding and AI-assistance acknowledgements: ACL policy requires
  generative-AI use beyond polishing to be disclosed, with details in the
  Acknowledgements matching your Responsible NLP checklist answers.

## Anthology-facing metadata

| Item | Why it matters at ACL | Common error |
|---|---|---|
| Title/abstract in the form | Becomes the Anthology landing page | Unicode or LaTeX macros pasted raw |
| Author names + order | Permanent citation record, BibTeX for everyone | Name spelled differently than prior papers |
| PDF fonts embedded | Anthology archival requirement | Missing Type-1/TrueType embedding from figures |
| License acceptance | Anthology publishes under CC BY 4.0 (post-2016 policy) | Assuming you can restrict reuse later |
| Video/poster uploads | Linked from the Anthology page when provided | Skipped, losing visibility |

Publication in the Anthology is open access with no author fee; ACL's cost
model is conference registration, not APCs.

## Integrating reviewer-mandated changes

Work from the meta-review, not memory:

1. Extract every "should," "must," and "the authors agreed to" from the
   meta-review and discussion thread into a checklist.
2. Map each to an edit: new sentence, moved table, scoped claim, added
   citation. The accepted contribution must not silently grow — a stronger
   claim than reviewers evaluated is an integrity problem, not a bonus.
3. Keep section and table numbering stable where possible so the review
   record still points at the right objects.
4. Re-run the checklist consistency pass: if you promised error bars or a
   contamination note in discussion, the camera-ready must contain it.

## Main conference vs Findings logistics

- Findings papers are full peer-reviewed publications in the Anthology but are
  typically not part of the main oral program; presentation options (Findings
  poster sessions, workshop presentation slots, videos) vary per edition —
  check the current conference's Findings instructions rather than assuming.
- Registration and presentation expectations differ by track and edition; ACL
  2026 ran as a hybrid conference in San Diego (July 2-7, 2026). Verify the
  current attendance requirement before booking or skipping travel.

## Camera-ready week runbook

```text
Day 1: meta-review edit checklist; claim-scope audit
Day 2: de-anonymize; acknowledgements incl. funding + AI disclosure
Day 3: public artifact links live; README + license on the repo
Day 4: rebuild with final style; font embedding + page-count check
Day 5: metadata form; abstract matches PDF; submit and archive everything
```

## Common camera-ready rejections and rework requests

- Unembedded fonts from matplotlib or Inkscape figures — regenerate with
  embedding forced rather than patching the PDF.
- Title case mismatch between the form and the PDF, or LaTeX math left in
  the plain-text abstract field.
- Author list drift: an author added or reordered after review needs chair
  approval, not a silent metadata edit.
- Limitations section deleted "for space" — it is still required and still
  free; removing it can bounce the paper at publication checks.
- Non-resolving artifact URLs: the Anthology page will outlive your lab
  server; prefer archived, versioned hosting for the link of record.

## If the paper landed in Findings

- The Anthology volume is "Findings of the Association for Computational
  Linguistics: ACL <year>" — cite and list it that way; miscrediting your
  own venue tier propagates into others' bibliographies.
- Camera-ready mechanics are the same as main-conference papers, extra page
  included; deadlines are usually shared — confirm in the decision letter.
- Ask early which presentation options the edition offers Findings papers
  (poster session, affiliated workshop slot, video); slots can require
  separate sign-up shortly after notification.

## Presentation assets riding the same deadline window

- Poster/slide templates, video-upload requirements, and session-format
  details arrive with or shortly after camera-ready instructions; the
  video deadline is often earlier than authors expect.
- Registration typically must be completed by a named author before the
  paper is scheduled — check the decision email for the binding rule.
- Book the error budget: font, metadata, and form rejections bounce back
  days later, so submitting on the deadline hour forfeits the retry.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Meta-review edits] <requested change -> edit made>
[Extra-page budget] <what the added space was spent on>
[De-anonymization + disclosure] <authors/acks/AI-use/links status>
[Anthology package] <PDF/metadata/license/artifact links>
```
