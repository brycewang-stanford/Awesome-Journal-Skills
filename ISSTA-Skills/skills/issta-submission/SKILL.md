---
name: issta-submission
description: Use when auditing an ISSTA submission for HotCRP readiness, the 18-page (excluding references and Data Availability) limit, ACM acmsmall plus screen, review and anonymous formatting, the required Data Availability section, double-anonymous integrity, the January abstract and paper deadlines, artifact intent, track choice among research/experience/replicability, and desk-reject triggers before the phase-one upload.
---

# ISSTA Submission

Use this for an ISSTA research-paper submission audit. Reopen the current Research Papers call,
the important-dates page, the ACM `acmart` (`acmsmall`) template, and the HotCRP site before giving
deadline-ready advice — ISSTA's submission model changes between editions and is the first thing
to re-verify.

## Submission audit

- Confirm the target is the ISSTA **research** track, not a co-located workshop, the Doctoral
  Symposium, or a sibling venue. ISSTA 2027 also invites Experience Papers and Replicability
  Studies — pick the kind that matches the contribution's evidence, not its topic alone, and
  mark it in the title ("(Experience Paper)", "(Replicability Study)"). Choose one primary
  research area (optionally a secondary).
- Build the HotCRP record early: title, abstract, authors, conflicts, and topic tags. ISSTA 2027
  has a **mandatory abstract** deadline (January 8, 2027) three days before the paper (January 11,
  2027, AoE); the author list and title cannot change after submission. Each author may be on at
  most 7 submissions.
- Use `\documentclass[acmsmall,screen,review,anonymous]{acmart}` (single-column; numeric or
  author-year citations). Do not shrink margins, fonts, or spacing to fit — non-compliant
  formatting may be desk-rejected without review.
- Fit the 18-page limit that excludes only references and the Data Availability section. Every
  section, figure, table, and appendix counts against the 18; there is no separate unlimited
  appendix, so decision-critical content lives in the body or in the artifact, not in overflow
  pages.
- Add the required **Data Availability** section before the references (not counted): where the
  code, data and evidence-generating tools are, or why they cannot be shared. Link an anonymous
  artifact (anonymized repository or HotCRP supplemental upload); one reviewer checks it.
- If AI tools were used in the research itself, describe that use in the methods section (ACM
  Policy on Authorship); verify every reference — fabricated citations are desk-rejected.
- Enforce double-anonymous review: no author names or affiliations, third-person self-citations,
  anonymized or withheld repository links, and no identifying PDF metadata.
- Decide the artifact plan now. The artifact-evaluation track is separate and later, but the paper
  should already promise what it will archive, and the review-time copy must be anonymous.

## Blocking risks

- Late HotCRP registration or PDF upload against the phase-one deadline.
- Over the 18-page limit, wrong template, or missing Data Availability section.
- Identity leak in text, self-citation phrasing, repository link, or PDF metadata.
- Wrong track (a replicability study filed as a research paper, or vice versa).
- Evaluation too thin to survive the soundness and evaluation criteria — a review-stage loss even
  when nothing is technically desk-rejectable.

## Desk-reject and triage table

| Trigger | Severity at ISSTA | Repair window |
|---|---|---|
| Over 18 pages (excluding references) | Desk reject | None after the deadline |
| Template/format non-compliance | Desk reject possible | None |
| Fabricated or unverifiable reference | Desk reject | None |
| Author identity leak in PDF or metadata | Desk reject | None |
| Missing `review`/`anonymous` options | Chair flag | Only before the deadline |
| Evaluation without real subjects or a baseline | Review-stage loss | Fixable only before submission |

## Final-week sequence for a testing/analysis paper

1. Freeze the technique's scope and threat model; reviewers grade claims against the scope you set.
2. Regenerate every results table from logged runs so the PDF and the artifact cannot diverge.
3. Pin subjects and benchmark versions (Defects4J revision, subject SHAs) in the paper and artifact.
4. Run the anonymity sweep: PDF metadata, `\author` block, acknowledgements, repository owner strings.
5. Confirm the HotCRP abstract matches the PDF abstract and the topic tags match the reviewer pool.

## Format anchors

- ISSTA uses ACM `acmsmall`, a single-column layout (the same format as PACMSE/FSE); code
  listings fit more easily than in two-column `sigconf`, but wide result tables still need
  planning, and 18 single-column pages hold less text than they sound.
- The 18-page figure describes the 2026 and 2027 cycles; older editions used two-column `sigconf`
  with 10 pages plus 2 for references. Treat every number as provisional and reopen the current
  call before relying on it.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue issta-skills   # from a clone of the AJS repository
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
[ISSTA readiness] Ready / Needs fixes / Not ready
[Track] research / experience / replicability
[Blocking checks] <HotCRP/page/format/anonymity/artifact-intent>
[Evaluation risk] <one soundness or evaluation gap>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before the phase-one deadline>
```
