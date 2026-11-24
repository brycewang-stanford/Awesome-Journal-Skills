---
name: rof-submission
description: Use when running a Review of Finance submission preflight for Editorial Express, regular versus Fast-Track fee choice, 60-page cap, 150-word abstract, double-blind anonymity, Chicago references, cover-letter disclosure, and code-sharing exceptions.
---

# Review of Finance Submission

Use this before uploading through Editorial Express (`editorialexpress.com/rof`). RoF is the
official journal of the European Finance Association (EFA), published by Oxford University
Press. Re-verify volatile figures on the official pages before paying or submitting.

## Preflight

- Choose the track and verify the current fee and tiered refund schedule (re-verified
  2026-11-24 on revfin.org; re-verify before paying). Regular submission is EUR 350 (EUR 300
  for EFA members); Fast-Track first submission is EUR 900 (resubmission EUR 500) and targets
  an editorial decision within 14 days of the later of editor assignment and confirmed payment.
  Since 1 November 2026 a desk rejection is either *with comment* (no refund) or *without
  comment* (RoF keeps EUR 100 and refunds the rest): regular EUR 250 / EUR 200 for members,
  Fast-Track EUR 800 (Fast-Track resubmission EUR 400). Slow-decision refunds: regular EUR 175
  / EUR 150 (members) if a decision takes over 120 days; Fast-Track EUR 550 (decision > 14
  days) or EUR 725 (decision > 120 days).
- Disclose any AI-tool use in the cover letter and acknowledge it in the manuscript (RoF LLM
  policy, updated 30 October 2026); papers whose methods use LLM/agent outputs must also report
  the model name, version, and access dates. Never leave hidden text or embedded instructions
  in the PDF — that is rejection without refund plus a one-year submission suspension.
- Confirm the manuscript stays within the hard 60-page total cap, including appendices,
  bibliography, figures, and tables.
- Keep the abstract within 150 words (count it).
- Confirm formatting: at least 12-point font, at least 1.5 line spacing, 1-inch side and
  1.5-inch top/bottom margins, submitted as a PDF with the first page numbered page 1.
- Remove author-identifying references, acknowledgements, grants, repository links, and file
  metadata for double-blind review.
- Check Chicago-style citations and references.
- Prepare cover-letter disclosures: confirm the paper is not under simultaneous review
  elsewhere and disclose any prior RoF rejection — either omission triggers desk rejection
  and a two-year submission ban. Request any code-sharing exception here, at initial
  submission, since it cannot be added later.
- Stage code/data materials and the Data Availability Statement.

See `templates/cover_letter.md` and `templates/checklist.md` for skeletons.

## Track-choice arithmetic — worked example

Illustrative, using the published schedule (re-verify before paying). An EFA member
submits regular at EUR 300; a desk rejection without comment refunds EUR 200, so being
screened out costs EUR 100 (a desk rejection with comment refunds nothing). Fast-Track costs EUR 900 against a 14-day target — the premium buys several
months of expected calendar on a finished paper. Worth paying when a rival team is
circulating the same natural experiment or a deadline (tenure file, job market) needs the
decision; wasted when gate-level problems — page cap, soft identification, missing
disclosures — make a desk screen the likely outcome.

## Desk-risk grid

| Check | Pass condition | Where it fails silently |
|---|---|---|
| Page count | <=60 total incl. appendices, bibliography, exhibits | appendix tables added after the last count |
| Abstract | <=150 words with the finding stated | counting keywords or JEL line by mistake |
| Anonymity | no names, grants, repos; metadata scrubbed | acknowledgement footnote surviving from the working-paper version |
| Disclosure | prior-RoF-rejection and no-parallel-submission statements present | omission triggers desk rejection plus the two-year ban |
| AI use | any AI-tool use disclosed in the cover letter and acknowledged in the manuscript; no hidden text | LLM-generated data or prompts used in the method but not reported with model/version/dates |
| Code policy | proprietary-data exception requested in this cover letter | exception deferred to later (the policy expects it at initial submission) |
| Format | 12-pt minimum, 1.5 spacing, required margins, PDF starting at page 1 | LaTeX class silently compiling at 11-pt |

## Final-hour sequence

1. Recount pages with the final bibliography and appendices compiled in.
2. Regenerate the PDF, strip author metadata, and open it on a clean machine to confirm.
3. Re-read the cover letter for the two disclosure sentences and any code-sharing
   exception paragraph.
4. Confirm the Editorial Express account, the fee route (member vs. non-member, regular
   vs. Fast-Track), and payment details.
5. Archive the exact submitted PDF and a hash of the replication package so the eventual
   R&R diff is auditable.

## Upload manifest

- Anonymized manuscript PDF: the only file referees see — title page without names,
  first page numbered 1, internet-appendix material clearly separated if included.
- Cover letter to the editor: disclosures (including any AI-tool use), any code-sharing exception, optional context
  on closely related own work (kept non-identifying in the manuscript itself).
- Supplementary files where applicable: internet appendix and any pre-staged replication
  material, packaged for OUP hosting rather than an external archive link (which would
  break anonymity anyway).
- Fee payment confirmation on the chosen track; for Fast-Track the 14-day clock runs from
  valid payment, so pay and upload the same day. Confirm the exact upload slots on
  Editorial Express and the journal's current author guidelines — interfaces change.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue rof-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Route] regular / Fast-Track
[Blocking checks] <fee/page/abstract/anonymity/style/disclosure/code>
[Highest desk risk] <one issue>
[Fix order] <ordered list>
```
