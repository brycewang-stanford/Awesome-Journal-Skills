---
name: naacl-submission
description: Use when a paper aimed at NAACL is about to be uploaded to an ACL Rolling Review cycle — verifying that the chosen cycle can still reach the next NAACL edition, that the PDF passes ARR's format and anonymization gates, and that every declaration on the OpenReview form survives a desk-reject audit.
---

# NAACL Submission

NAACL has no submission portal of its own. What you upload goes to an ACL
Rolling Review (ARR) cycle on OpenReview; NAACL enters the picture weeks later,
when you commit the finished review package to the conference. This skill
audits the upload with that split in mind. The single most NAACL-specific
check comes first, because it is the one authors from other venues never
think to make.

## Check zero: does this cycle reach a NAACL at all?

NAACL is not annual. The chapter historically stands down in years when the
main ACL meeting is hosted in the Americas — there was no NAACL 2023 and no
NAACL 2026 (ACL 2026 ran in San Diego, July 2-7, 2026). As of 2026-07-08 the
next edition is NAACL 2027, whose dates, venue, and feeding ARR cycles were
still unannounced (待核实 via https://2027.naacl.org/ and
https://aclrollingreview.org/dates). Before polishing anything:

```text
1. Open aclrollingreview.org/dates → does any listed cycle name NAACL?
2. If yes  → that cycle's submission date is your real deadline.
3. If no   → your reviewed paper can still wait in ARR and commit later,
             or commit to a sibling venue (EMNLP/EACL/AACL) instead.
4. Record the answer with a date — this table changes without notice.
```

Historical anchor: NAACL 2025 (Albuquerque, April 29 - May 4, 2025) drew on
the ARR October 2024 cycle — ARR upload October 15, 2024; reviews and
meta-reviews back December 12, 2024; final versions for Main and Findings due
February 8, 2025; all deadlines 11:59 PM UTC-12. Treat those numbers as shape,
not schedule.

## The gates ARR applies before any human reads the science

| Gate | Passing condition | Cost of failure |
|---|---|---|
| Length | Long ≤ 8 content pages, short ≤ 4; references and the Limitations section sit outside the count | Rejected without review |
| Template | Current *ACL style files, unaltered geometry | Treated as a length violation |
| Limitations | A real Limitations section after the conclusion | Explicit desk-reject ground |
| Anonymity | No names, affiliations, thank-yous, or de-anonymizing links anywhere in PDF or supplements | Rejected without review |
| Checklist | Responsible NLP checklist filed and consistent with the PDF | Desk reject for misleading answers |
| Resubmission link | Prior ARR ID plus a change summary if this work was reviewed before | Desk reject if omitted |

Two subtleties worth spelling out for NAACL-bound work specifically. First,
papers on Indigenous or low-resource languages of the Americas often carry
community acknowledgements and data-partnership credits — those must come out
of the reviewed version and return only at camera-ready. Second, a preprint
is allowed at any time under current ARR policy, but the form asks you to
declare it; an inaccurate declaration is itself a desk-reject ground, and
truthfully declaring "no preprint" buys borderline-case priority you forfeit
by posting one mid-cycle.

## Form fields that quietly decide your fate

- **Preferred venue.** When a cycle feeds more than one conference, the form
  asks where you intend to commit. Naming NAACL here routes your paper toward
  the chapter's area-chair pool; it is a signal, not a contract.
- **Reviewing obligations.** ARR expects author-side reviewing or nomination;
  ignoring the field can block the submission outright.
- **Languages studied.** Fill it precisely — a NAACL commitment later puts
  your paper before a community that reads "Spanish, Quechua, English" as
  substantive information, not metadata.

## Supplements at upload time

- Software and data go in as archives (`.zip`/`.tgz`) through the OpenReview
  fields, not as links to personal cloud storage that can log visitors.
- Reviewers promise to judge the paper from its content pages alone, so a
  supplement may deepen evidence but must never complete an argument.
- Name files blandly (`code.zip`, `data_card.pdf`); a lab-convention filename
  is an anonymity leak the sweep below should catch.

## Worked micro-case

A team studying code-switched Spanish-English dialogue plans to submit in
July 2026 "for NAACL." The calendar check shows no cycle currently names
NAACL 2027. Their real options: enter the next open cycle now and let the
reviewed package wait for a NAACL commitment window (reviews stay valid
across cycles), target EMNLP/AACL via the May cycle instead, or hold for the
cycle NAACL 2027 eventually announces. The audit's job is to force that
decision explicitly rather than let a vague "submit to NAACL" drift into a
missed conference entirely.

## Ordered pre-upload pass

1. Reconfirm the live cycle calendar and the NAACL question above.
2. Rebuild the PDF from the untouched current style files.
3. Run an anonymization sweep over text, footnotes, metadata, and every
   linked artifact; check supplement archives file by file.
4. Reconcile each checklist answer against the section it points to.
5. If resubmitting, write the change summary a skeptical AC would accept.
6. Upload early enough to fix a rejected PDF before the AoE cutoff.

## Mechanical sweeps before the AoE cutoff

- `pdfinfo main.pdf` — creator/author metadata fields must be empty or
  generic; LaTeX toolchains leak usernames here.
- Search the PDF text for your institution's name, grant numbers, and the
  string fragments of every author's homepage.
- Open each supplement archive on a machine that has never touched the
  project; hidden OS files and absolute paths surface immediately.
- Recompute the content-page count *after* the last figure move; page 8.05
  is page 9 to a compliance script.
- Remember the clock: 11:59 PM UTC-12 is later than every timezone in the
  Americas, which breeds complacency — OpenReview load spikes at the hour
  are the real risk, not the math.

## Output format

```text
[Cycle sanity] <cycle name -> feeds NAACL? yes/no/unverified>
[Gate results] length / template / limitations / anonymity / checklist / resubmission
[Declaration risks] <preprint, venue preference, reviewing obligation>
[Blocking fixes] <ordered, with owner>
[Upload verdict] go / hold / re-plan cycle
```
