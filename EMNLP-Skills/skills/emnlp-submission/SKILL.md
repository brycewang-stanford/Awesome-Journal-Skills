---
name: emnlp-submission
description: Use when auditing an EMNLP submission before the ACL Rolling Review deadline, covering ACL-template compliance, the 8-page long / 4-page short caps, the mandatory Limitations section, the Responsible NLP checklist and its desk-reject enforcement, anonymization without an anonymity period, venue preference, and reciprocal-reviewing duties.
---

# EMNLP Submission

Run this audit before uploading to the ARR OpenReview site. EMNLP does not operate its own
submission portal: the paper enters ACL Rolling Review, and the conference only sees it later
at commitment. Everything below reflects the EMNLP 2026 / ARR May 2026 configuration read on
2026-07-08 — reopen the live CFP and `aclrollingreview.org` before acting on any number.

## The two-owner rule

Half of the submission rules belong to ARR, half to the conference, and confusing the owners
causes real mistakes:

| Question | Who owns the answer | 2026 answer |
|---|---|---|
| Deadline for the reviewed PDF | ARR cycle calendar | May 25, 2026 (May cycle) |
| Page caps and template | ARR CFP | ACL templates; long ≤ 8 content pages, short ≤ 4 |
| Limitations section | ARR CFP | Mandatory, after the conclusion, uncounted |
| Checklist | ARR Responsible NLP checklist | Filed at submission; desk-reject enforced |
| Which venue the paper reaches | Conference commitment | EMNLP commitment due August 2, 2026 |
| Acceptance decision | Conference SACs and PCs | Notification August 20, 2026 |

The May 2026 cycle fed both EMNLP 2026 and AACL-IJCNLP 2026, and the form asked authors to
declare the intended venue at submission time. Declare deliberately — the declaration shapes
which conference's area chairs eventually argue over your paper.

## Format gate

- Compile with the current official ACL style files, untouched. ARR's stated policy is
  rejection without review for modified templates or styles borrowed from other venues.
- Count only content pages against the cap: references are unlimited, and the Limitations
  and Ethical Considerations sections are exempt. Do not "save space" by shrinking the
  Limitations section — it is free and reviewers read it.
- Short papers are a different genre, not a truncated long paper: one claim, one clean
  experiment, four pages. A compressed eight-page study reads as exactly that.
- Appendices and supplementary files are permitted for reproducibility, but reviewers are
  not promised to read them; the content-page body must carry the argument.

## Anonymization under the no-embargo policy

ACL abolished the anonymity period: you may post and publicize a preprint at any time. The
submission itself must still be double-blind. In practice this means the PDF cannot close
the loop between itself and your public identity:

- Self-citations in the third person ("Kim et al. showed", never "we previously showed").
- No acknowledgements, grant numbers, or lab names in the reviewed version.
- Repository and demo links must be anonymized (anonymous.4open.science or equivalent) —
  a github.com/yourlab URL is a leak even though your arXiv preprint is legal.
- Scrub PDF metadata and any dataset README inside supplementary archives.

```bash
# Mechanical leak sweep on the submission PDF and supplementary archive
pdftotext main.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|huggingface\.co/[a-z]|acknowledg|grant'
pdfinfo main.pdf | grep -Ei 'author|creator|producer'
unzip -l supp.zip | grep -Ei '\.git|username|/home/'
```

## Checklist as a desk-reject surface

Since December 2024, ARR desk-rejects submissions whose Responsible NLP checklist answers
are incorrect, incomplete, or misleading. Treat the checklist as testimony, not paperwork:
answer it against what the PDF actually contains, and fix the PDF where the honest answer
would look bad. Typical mismatches that get caught: claiming license documentation the
paper lacks, "yes" on reported hyperparameters that appear nowhere, and human-annotation
questions skipped because the ratings came from crowdworkers "informally."

## Obligations that ride along

- The author registration form was due May 27, 2026 EoD AoE — two days after submission;
  a missed form jeopardizes the submission, not just goodwill.
- ARR runs reciprocal reviewing: qualified authors on the submission absorb reviewing or
  AC duties in the same cycle (17,087 submissions in May 2026 stretched the pool). Budget
  that time into the group's summer before the deadline, not after the assignment email.
- The 2026 call singles out thinly sliced submissions, hallucinated citations, and fully
  AI-generated papers as sanctionable; AI writing assistance is allowed. Verify every
  reference resolves to a real paper before upload — citation hallucination is now a
  named offense, and it is mechanically detectable.

## Long or short: decide before the audit

The format choice is strategic, not cosmetic, and it interacts with the audit:

- A long paper with one experiment and six pages of framing reviews worse than the same
  content as a short paper — reviewers calibrate expectations to the format, and a thin
  long paper invites the "thinly sliced" reading the 2026 call warns about.
- A short paper cannot absorb reviewer requests: there is no room to add the control
  experiment R2 wants, so short-paper responses lean harder on scope discipline being
  right the first time.
- Resubmission across formats is possible between cycles, but reviewers who saw the
  long version will notice a short version that simply deleted the weaknesses.

## Dual submission and the preprint boundary

ARR's dual-submission rules prohibit the same work being under review at another
archival venue simultaneously; the venue-preference declaration does not create an
exception. What is *not* dual submission: a public arXiv preprint (explicitly allowed,
no embargo), a non-archival workshop presentation, or a rejected earlier ARR cycle of
the same paper. What is: a concurrent NeurIPS/journal submission of substantially the
same content, and quietly hoping the calendars never collide. When any prior version of
the paper exists — arXiv, workshop, previous ARR cycle — the OpenReview form has fields
for saying so; fill them as disclosures, not confessions, because chairs check overlap
mechanically and forgiveness for a declared overlap is routine while discovery of an
undeclared one is not.

## Fix order for the final 72 hours

1. Freeze the content pages; push overflow into appendices, never into the margins.
2. Rerun the anonymization sweep on the final PDF, not the draft you swept last week.
3. Re-answer the checklist against the frozen PDF; repair contradictions in whichever
   direction is honest.
4. Verify every citation resolves (DOI, Anthology ID, or arXiv ID) — no exceptions.
5. Complete the OpenReview form, venue-preference declaration included, and confirm the
   author registration form is calendared.

## Output format

```text
[EMNLP submission status] ready / blocked / at risk
[Format] template, content pages vs cap, Limitations present
[Anonymity] clean / leaks: <where>
[Checklist] consistent / contradictions: <items>
[Obligations] registration form, reciprocal reviewing, venue declaration
[Fix queue] <ordered actions before the ARR deadline>
```
