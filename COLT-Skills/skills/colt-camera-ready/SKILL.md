---
name: colt-camera-ready
description: Use when converting an accepted COLT (Conference on Learning Theory) paper into its PMLR proceedings version, covering de-anonymization, acknowledgements and funding restoration, appendix consolidation into the archival PDF, PMLR volume metadata and BibTeX hygiene, rebuttal-promised edits, and presentation logistics.
---

# COLT Camera Ready

Use this after a COLT acceptance. COLT proceedings are published electronically in the
Proceedings of Machine Learning Research (PMLR) — verified against the COLT 2026 CFP
and PMLR volume pages on 2026-07-08. The camera-ready instructions arrive with the
acceptance notification; they, not this file, control exact dates and forms.

## Recent volume anchors (verified 2026-07-08)

| Edition | PMLR volume | Location | Volume editors |
|---|---|---|---|
| COLT 2024 (37th) | v247 | Edmonton, Canada | Shipra Agrawal, Aaron Roth |
| COLT 2025 (38th) | v291 | Lyon, France | Nika Haghtalab, Ankur Moitra |
| COLT 2026 (39th) | announced with acceptance (待核实) | San Diego, USA | current program chairs |

Volume editors are the program chairs of that edition; the pairing rotates every year.
The COLT 2026 volume number and camera-ready deadline were not yet published at the
access date — take both from your acceptance email.

## De-anonymization pass

- Remove the template's `anon` option so the author block renders; verify the running
  head and PDF metadata now carry real names.
- Restore acknowledgements, funding lines, and any statements the anonymous version cut.
  These lines add length — recheck where the body boundary falls if the current
  instructions still enforce a body limit at camera-ready (待核实 per cycle).
- Rewrite defensive third-person self-citations ("the authors of [12] showed") back
  into honest first person where it reads better.
- Swap anonymized or omitted repository links for stable public URLs, and test each
  from a logged-out browser.

## Consolidating the archival PDF

At COLT the appendix ships inside the same archival PDF, so the proceedings version is
the *complete* record — there is no separately hosted supplement to lean on later.

- Fold every rebuttal-promised edit into the text now: theorem statements that must
  carry an explicit constant, assumptions promoted from appendix to body, corrected
  displays. Keep a private ledger mapping each reviewer request to the diff that
  answers it, because chairs occasionally spot-check.
- Do not renumber theorems, lemmas, or assumptions relative to the reviewed version
  unless forced; the review record and any citing preprints refer to the old numbers.
- Reconcile the arXiv version: theory readers will diff arXiv against PMLR, so either
  update arXiv to match or note the differences in the arXiv comments field.
- Run a final pass on cross-references — `\ref` breakage introduced by de-anonymization
  edits is the most common camera-ready defect in proof-heavy papers.

## PMLR metadata and citation hygiene

Title, author order, and abstract you enter in the proceedings forms become the
citable record. The PMLR page for your paper generates the canonical citation; make
your own BibTeX consistent with it:

```bibtex
@inproceedings{yourkey2026tight,
  title     = {Tight Rates for a Learning Problem},
  author    = {Lastname, First and Coauthor, Second},
  booktitle = {Proceedings of the 39th Annual Conference on Learning Theory},
  series    = {Proceedings of Machine Learning Research},
  volume    = {TBD},   % assigned volume number, e.g. v291 was COLT 2025
  pages     = {1--30}, % assigned by the volume
  year      = {2026},
  publisher = {PMLR}
}
```

- Check every accent and math symbol in the title as it will render on the PMLR page.
- Author order must match the submission unless the chairs approved a change.
- PMLR is open access with no author-side publication fee; COLT's cost model is
  conference registration, not an APC.

## Presentation and registration obligations

- Expect that an accepted COLT paper must be presented at the conference by an author;
  the exact registration requirement, talk versus poster format, and any remote
  option for the 2026 edition were not verifiable at the access date (待核实) — the
  acceptance email and the registration page at learningtheory.org control.
- COLT is single-track: your talk or poster is seen by the whole community, so slide
  preparation deserves more lead time than at parallel-session venues.
- Budget for registration early; COLT 2026 ran June 29 to July 3 in San Diego, and
  conference-hotel capacity at smaller venues fills quickly.

## Preparing the talk alongside the PDF

Camera-ready season doubles as talk season, and at a single-track venue the talk is
part of the paper's public record:

- Build the talk from the informal theorem statements and the technique paragraph,
  not from the formal setup — the room already speaks the field's vocabulary but has
  not seen your notation.
- One slide of "what was known" with exact prior rates mirrors the paper's
  known-vs-new ledger and is the single highest-value slide at COLT.
- Rehearse the proof-idea slide until it survives without the appendix: the aim is
  that a listener could set a student to re-derive the result.
- If the edition uses posters for some papers, the poster's spine is the same three
  objects: model, theorem, technique — resist the empirical-venue urge to fill space
  with plots you do not have.
- Announce the open questions from the paper's discussion section; COLT audiences
  treat posed problems as gifts, and follow-up work cites the talk's source paper.

## Common camera-ready defects at COLT

| Defect | Why it happens | Catch it by |
|---|---|---|
| Body overflow after author block returns | Anonymous version used the freed lines | Recompiling with authors before editing anything |
| Theorem numbering drift vs. reviewed version | Appendix restructuring | Diffing the numbered-statement list |
| arXiv/PMLR content divergence | Only one copy updated | A scheduled same-day update of both |
| Broken `\ref` after merging rebuttal edits | Labels deleted with old text | `grep`-style check for "??" in the compiled log |
| Metadata mismatch (title case, accents) | Forms filled from memory | Copy-pasting from the final PDF |

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Reviewer-promise ledger] <request -> diff location>
[De-anonymization checks] <author block / acknowledgements / links / metadata>
[Numbering stability] preserved / documented changes
[Logistics] <forms, registration, presentation owner>
```
