---
name: emnlp-camera-ready
description: Use when converting an accepted EMNLP paper — Main or Findings — into its ACL Anthology camera-ready form: de-anonymization, integrating response-phase commitments, Limitations and checklist-appendix handling, Anthology metadata hygiene, artifact link restoration, and Budapest presentation and registration logistics.
---

# EMNLP Camera Ready

Use this after the acceptance email. For EMNLP 2026 the notification landed August 20 and
camera-ready was due September 20, for a hybrid conference in Budapest October 24-29.
Main-conference and Findings papers both produce Anthology camera-readies on the same
clock; what differs is the presentation package. Reopen the acceptance email and the
current camera-ready instructions before acting — the conference, not ARR, owns this
phase.

## The three-way merge

A camera-ready is a merge of (a) the reviewed PDF, (b) the edits you promised during the
response window, and (c) the de-anonymization diff. Do them in that order and keep the
promises auditable:

1. Start from the exact submitted source, not a lab-internal draft that kept evolving.
2. Apply every edit committed in the response, and only contribution-preserving edits
   beyond that — SACs accepted a specific paper, not a direction.
3. Restore identity last: author block, acknowledgements, funding, and the real
   repository links that replaced anonymized placeholders.

```bash
# Keep the promise trail honest: diff reviewed vs camera-ready source
latexdiff submitted/main.tex camera/main.tex > promise-audit.tex
grep -n "TODO\|anonymous\|anon\.4open\|XXXX" camera/*.tex   # leftover anonymization
grep -rn "github.com\|huggingface.co" camera/*.tex          # links now real and public?
```

## Page arithmetic after acceptance

Recent ACL-family practice grants accepted papers an extra content page to absorb
reviewer-requested material — **verify the 2026 allowance in the official instructions
before using it** (unconfirmed at 2026-07-08). Spend any extra space in value order:
response-phase commitments first, then the error-analysis or scope clarifications
reviewers wanted, and only then new polish. The Limitations section remains mandatory
and uncounted; EMNLP 2025 additionally shipped the completed Responsible NLP checklist
as a paper appendix — check whether 2026 repeats this and budget the pages.

## Anthology metadata is forever

The ACL Anthology entry is generated from what you submit, and errors there outlive any
typo in the PDF:

| Field | Failure that actually happens | Prevention |
|---|---|---|
| Author names | Diacritics dropped, name order flipped | Each coauthor confirms their own rendered name |
| Title casing | Anthology BibTeX propagates a miscased title | Match title field to the PDF exactly |
| Abstract | Form abstract is the pre-response version | Paste from the final PDF, not from OpenReview |
| PDF fonts | Non-embedded fonts break Anthology rendering | Embed all fonts; validate the final PDF |

The Anthology is open access with no author fee; there is no APC anywhere in this
pipeline — budget goes to registration and travel instead.

## Artifact restoration

Acceptance dissolves the anonymity constraint, so the artifact story flips from hiding
identity to maximizing findability:

- Move code and data from anonymized archives to permanent public homes; add licenses,
  model cards or data statements, and the exact configs behind each table.
- Make the repository README point at the paper (Anthology link once live, arXiv
  meanwhile) and state which commit reproduces the camera-ready numbers.
- If the paper promised data release "upon acceptance," this is the moment that promise
  becomes checkable — and NLP readers do check.

## Findings-specific handling

A Findings camera-ready is a full peer-reviewed publication in its own Anthology volume
(`20XX.findings-emnlp`), on the same deadline. Presentation options for Findings papers
have varied by edition and were unconfirmed for 2026 at check time — ask the program
chairs rather than assuming a poster exists or does not. Cite your own paper as
"Findings of the Association for Computational Linguistics: EMNLP 2026" — miscrediting
it to the main proceedings is a small dishonesty reviewers of your *next* paper will
notice.

## Presentation and logistics (hybrid, verify specifics)

- EMNLP 2026 is hybrid; the exact in-person versus virtual presentation obligations and
  registration tiers were 待核实 at check time — confirm which registration category
  the accepted paper requires and by when.
- Poster and talk formats, session assignment, and video or slide upload deadlines
  arrive by email between camera-ready and the conference; nominate one author to own
  that inbox.
- Budapest in late October: visa lead times for many passports exceed the
  notification-to-conference gap — the visa-chairs contact exists for exactly this, and
  early outreach beats airport improvisation.

## Camera-ready week, ordered

1. Rebuild from the submitted source and apply the promise list (response commitments
   first) with the diff audit running.
2. Verify the 2026 page allowance and checklist-appendix requirement in the official
   instructions — both were unconfirmed at pack-check time and both change layout.
3. De-anonymize: author block, acknowledgements, funding, real links; then rerun the
   leftover-anonymization grep, because "anon.4open.science" surviving into the
   Anthology is a permanent embarrassment.
4. Each coauthor confirms their own name rendering and affiliation; the submitting
   author confirms title and abstract fields against the final PDF.
5. Publish the artifact repository, pin the reproducing commit, and test every link in
   the PDF from a logged-out browser.
6. Upload early enough to survive one round of publication-chair bounce-back (font
   embedding and metadata complaints are routine).

## After Budapest

Two post-conference tasks close the loop cleanly: update the arXiv version (if one
exists) to the camera-ready content with the Anthology citation on page one, so the
version the field actually downloads credits the venue; and record the paper's final
BibTeX from the Anthology itself rather than hand-writing it — Anthology BibTeX is the
canonical form your citers will use, and your own reference lists should match it.

## Output format

```text
[Camera-ready state] merge pending / promises applied / metadata verified / uploaded
[Promise audit] <response commitment -> edit location>
[Anthology metadata] <names / title / abstract / fonts checked>
[Artifacts] <repo public, licensed, commit-pinned: yes/no per artifact>
[Logistics] <registration, presentation format, visa owner>
```
