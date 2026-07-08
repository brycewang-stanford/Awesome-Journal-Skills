---
name: focs-submission
description: Use when running the final pre-upload audit of a FOCS (IEEE Symposium on Foundations of Computer Science) submission — the April HotCRP deadline clock, the abstract-references-plus-ten-pages attention rule, the 11-point single-column format floor, PDF security restrictions, double-blind checks, and SIGACT publication-policy compliance.
---

# FOCS Submission

Anchor cycle: FOCS 2026 (67th edition), submissions due Wednesday, April 1,
2026, 5:00 PM EDT — a US-Eastern wall clock equal to 21:00 UTC, not an
anywhere-on-earth deadline — via `focs26.hotcrp.com` (CFP checked 2026-07-08;
that deadline has passed, so this audit now serves the next cycle: reopen the
live CFP before trusting any number here).

## What the 2026 CFP actually required

| Requirement | 2026 wording (verify per cycle) |
|---|---|
| Length | No bound; full version encouraged as the submission |
| Attention rule | Abstract + references + first **ten pages** guaranteed; the rest at the committee's discretion |
| Typography | 11-point or larger font, single column, single-spaced with ample spacing, ≥1-inch margins, letter-size paper |
| File | PDF **without security restrictions on copying or printing** |
| Anonymity | Double-blind: no names/affiliations/emails, third-person self-references, acknowledgements omitted |
| Publication policy | SIGACT rules: nothing published or scheduled before the conference month elsewhere; no simultaneous proceedings/journal submission |
| Exceptions | Prior appearance in a venue with significantly different format/content/audience: contact the program chair **before** submitting |

Note the guaranteed-read set: FOCS names the *references* as always-read
material alongside the ten pages. Your bibliography is a reviewed object —
stale, sloppy, or misattributed citations are visible even to the laziest
reading (see `focs-related-work`).

## Mechanical pre-flight

Run these on the exact PDF you will upload, not on a draft:

```bash
# Page geometry and count of the guaranteed window
pdfinfo submission.pdf | grep -E 'Pages|Page size'   # letter = 612 x 792 pts

# FOCS-specific: the CFP forbids copy/print security restrictions
qpdf --show-encryption submission.pdf                # want: "File is not encrypted"

# Identity leakage in embedded metadata
exiftool submission.pdf | grep -iE 'author|creator|company'

# Self-reference sweep in the source
grep -rn --include='*.tex' -iE '\b(we|our) (recent|previous|earlier|prior)\b|acknowledg|thank' .
```

The encryption check is easy to fail accidentally: some institutional PDF
tooling and some print-to-PDF drivers stamp permission flags by default, and
a restricted PDF violates the letter of the CFP.

## Deadline-week sequence

1. **T-7 days — content freeze.** No new theorems. Anything proved this week
   goes to the arXiv version later, not into the submission.
2. **T-5 days — window audit.** Confirm every result is stated by page ten and
   the technical overview reflects the proofs as they now exist.
3. **T-3 days — first upload.** HotCRP allows re-uploads until the deadline;
   an early upload converts a hard cliff into a soft one. Fill conflicts,
   topics, and co-author records now — PC conflict data affects assignment
   quality directly.
4. **T-1 day — blind and format pass** using the commands above, on the
   compiled final PDF.
5. **Deadline day — clock arithmetic.** 5 PM EDT is late evening in Europe and
   early morning in Asia; compute your local equivalent once, write it down,
   and stop trusting mental arithmetic under stress.

## HotCRP metadata is part of the submission

Theory authors treat the web form as an afterthought; the committee's
machinery does not. Three fields shape your paper's fate before anyone reads
a word:

- **Topics.** Assignment starts from your topic selections. Choosing only
  your micro-area starves the paper of breadth readers; choosing everything
  looks unserious. Pick the two or three areas whose reviewers you would
  actually want in the room.
- **Conflicts.** Declare advisors, recent co-authors, and current-institution
  colleagues per the form's definitions. Under-declared conflicts discovered
  later can void a review cycle; over-declared conflicts (tagging everyone
  senior in the area) can be read as reviewer-shopping.
- **Author records.** Complete them accurately even though the PDF is blind —
  the system uses them for conflict resolution, and errors are painful to
  repair after decisions.

## Policy traps specific to this venue

- **The IEEE/SIGACT seam.** FOCS is an IEEE Computer Society (TCMF) event that
  enforces ACM SIGACT's publication policy. Authors who read only IEEE's
  generic submission rules miss the simultaneous-submission bar entirely.
- **arXiv is safe, proceedings are not.** Posting the full version to arXiv or
  ECCC before submitting is normal community practice and does not violate the
  prior-publication rule; a workshop with *published proceedings* does.
- **The invited-journal overlap.** If a journal version of a companion result
  is already in press with overlapping material, disclose to the chair before
  the deadline rather than hoping the overlap goes unnoticed.

## Readiness verdict

```text
[FOCS submission audit]
Window     : all theorems stated by p.10           PASS/FAIL
Format     : 11pt+/single-column/1in/letter        PASS/FAIL
PDF        : unencrypted, metadata clean           PASS/FAIL
Blind      : third-person self-refs, no acks       PASS/FAIL
Policy     : no simultaneous/prior publication     PASS/FAIL
HotCRP     : conflicts, topics, authors complete   PASS/FAIL
Verdict    : UPLOAD / FIX(ordered list) / CONSULT CHAIR
```

Any FAIL in the first three rows is fixable in hours; a policy FAIL is not
fixable at all after upload — resolve those with the program chair first.
