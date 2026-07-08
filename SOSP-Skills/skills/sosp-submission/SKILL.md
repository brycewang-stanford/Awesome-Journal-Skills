---
name: sosp-submission
description: Use when auditing a SOSP submission for HotCRP readiness, covering the abstract-registration and full-paper deadlines, the 12-page technical-content limit with references excluded, the 7x9-inch two-column format, double-blind rules with paper-ID substitution, conflict declaration under PC-chair audit, and desk-reject triage.
---

# SOSP Submission

Run this audit before anything is uploaded to the SOSP HotCRP instance. Every number
below is a 2026-cycle anchor verified on 2026-07-08 against the official CFP and author
guidelines at `sigops.org/s/conferences/sosp/2026/` and the `sosp26.hotcrp.com`
deadlines page. SOSP re-issues these rules each year; treat the current cycle's pages
as controlling and this file as the map of what to check.

## Two deadlines, one hard gate

SOSP registers abstracts ahead of papers, and the registration is a real gate, not a
courtesy: the paper ID assigned at registration replaces the author names on page one
of the anonymized PDF, and conflict screening starts from the registered author list.

| Gate (2026 anchors) | Date | What must be final |
|---|---|---|
| Abstract registration | March 27, 2026 | Title, abstract, complete author list, topics, conflicts |
| Full paper upload | April 2, 2026, 7:59:59 AM EDT | Anonymized PDF, optional supplementary document |
| Notification | July 3, 2026 | — |
| Camera-ready | August 28, 2026 | Shepherd-approved final PDF |

The six-day window between the two gates is for polishing, not for writing. A paper
that does not build cleanly in the official format a week before registration is
already late.

## Page and format compliance

- At most **12 pages of technical content** — all text, figures, and tables count.
  **Bibliographic references are not included** in the limit, so never compress the
  bibliography to save space; compress prose instead.
- 10-point font on 12-point leading, US letter, everything inside a 178 x 229 mm
  (7 x 9 in) block, two columns separated by 8 mm. Reviewers at this venue have seen
  every margin trick; a format violation reads as an integrity problem, not a typo.
- Supplementary material goes in a **separate document** and may cover only items that
  are not critical to evaluating the paper (formal proofs, extra analyses,
  methodological detail). If a claim's evidence lives only in the supplement, the claim
  is unsupported for review purposes — move it into the 12 pages.

## Anonymization the SOSP way

SOSP asks for a good-faith anonymization effort, judged pragmatically:

- Page one carries the **registered paper ID** where the author block would sit.
- No author names, affiliations, acknowledgments, or grant numbers anywhere, including
  in the supplement and PDF metadata.
- Self-references in third person; do not cite an identifying technical report as "our
  earlier version."
- De-identify giveaway context: a deployment description that only one company could
  have written should be generalized ("a large content provider") without falsifying
  the evidence.

```bash
# Leak sweep over the built PDF and the LaTeX tree before upload
pdfinfo main.pdf | grep -iE '^(author|creator|producer)'
pdftotext main.pdf - | grep -inE 'acknowledg|grant no|@[a-z]+\.(edu|com)|github\.com/' | head
grep -rn --include='*.tex' -iE '\\author|university|laboratory|institute' . | grep -v paperid
```

## Conflict declaration is audited

Unlike venues where conflict lists are taken on trust, SOSP's PC chairs review the
declared conflicts, may add missing ones, and may **remove** declared conflicts that
have no basis — naming a PC member as a conflict to dodge a tough reviewer is
explicitly called out as improper. Papers conflicted with both PC chairs are routed to
a designated conflict chair. Practical consequences:

- Build the conflict list from real categories (co-authors, advisors, same institution,
  recent collaboration), and be able to justify every entry if asked.
- An undeclared genuine conflict discovered late can poison an otherwise-positive
  review discussion; over-declaration can be reversed by the chairs and damages trust.

## Desk-reject triage

| Finding | Outcome | Can it be fixed after the deadline? |
|---|---|---|
| More than 12 pages of technical content | Rejected without review | No |
| Font, block, or column-geometry tampering | Rejected without review | No |
| Author names or affiliation leak in PDF or supplement | Rejected or chair-flagged | No |
| Missing abstract registration | Paper cannot be submitted | No |
| Unjustified conflict entries | Removed by chairs; credibility cost | Chairs act unilaterally |
| Core evidence only in the supplement | Survives triage, dies in review | Only before the deadline |

## Final-ten-days sequence

1. Freeze the evaluation and rebuild all figures from logged data with one command.
2. Compile in the official format and resolve overflow by cutting prose, not leading.
3. Register the abstract with the final author list and a conflict list you can defend.
4. Run the leak sweep above on the paper and the supplementary document.
5. Replace the author block with the assigned paper ID; verify page one.
6. Upload to HotCRP early; re-download the PDF from HotCRP and check it renders
   page-complete — the submission of record is what HotCRP holds, not your local file.

## Output format

```text
[SOSP readiness] Ready / Needs fixes / Not ready
[Gate status] abstract registered? / paper uploaded? / hours to deadline
[Format audit] pages of technical content / geometry / references handling
[Anonymity audit] pass / leaks found: <where>
[Conflict list] defensible? <yes/no + weakest entry>
[Fix order] <ordered actions before upload>
```
