---
name: facct-submission
description: Use when auditing an ACM FAccT submission for OpenReview readiness — the mandatory abstract-registration gate with focus-area selection, the acmart anonymous/review PDF (or ACM Word template), the 14-page (+1 endmatter) budget, mutual anonymity, the required Generative AI Usage Statement and the Ethical Considerations statement, archival vs non-archival choice, the all-authors reviewer sign-up, and desk-reject triage before the deadline.
---

# FAccT Submission

Run this audit before uploading to the FAccT OpenReview site. FAccT papers are **archival ACM
proceedings** in an *interdisciplinary* responsible-AI venue, reviewed **mutually anonymously** by a
mixed CS+law+social-science pool. Every number below was read directly from the FAccT 2027 CFP and
Author Guide on 2026-11-24 (see `resources/official-source-map.md`); treat them as a one-cycle
snapshot and reopen the live call first. FAccT 2027's deadlines (27 October / 3 November 2026) have
passed, so for a new paper this audit is a template for the next call (FAccT 2028, not yet
published).

## The two-step deadline (abstract gate first)

FAccT separates **abstract registration** from **paper submission**, and the gate is hard:

- **Abstract registration** locks the **author list** and the **archival/non-archival choice**, and
  registers title, abstract, and **focus areas** a week early (FAccT 2027: **27 October 2026**,
  11:59 PM AoE). Authors who do not register by this date **cannot submit a paper**, and late
  abstracts are not accepted because reviewer bidding starts immediately. Title, abstract, and focus
  areas may still be refined until the paper deadline; placeholder abstracts ("TBA") can be deleted.
- **Paper submission** uploads the anonymized PDF (FAccT 2027: **3 November 2026**). Unaffiliated
  authors should create their OpenReview profile weeks ahead (FAccT 2027 advised 16 October 2026),
  because verification is slow.
- **Reviewer sign-up:** FAccT 2027 requires **every author** of every paper to fill in the reviewer
  sign-up form; failing to sign up and follow through can lead to (desk) rejection.

Register with the *real* title, abstract, and honestly chosen focus areas, not placeholders — a
mismatch between your registered focus areas and your actual contribution mis-matches you to
reviewers from the wrong discipline, the most damaging thing that can happen at an interdisciplinary
venue.

## Format and page budget

- **ACM TAPS workflow** — LaTeX (strongly recommended; Overleaf) or Microsoft Word, **single-column**.
  In LaTeX, start from `sample-sigconf-authordraft.tex` and build anonymized for review, e.g.
  `\documentclass[manuscript,screen,review,anonymous]{acmart}`. The copyright/bottom-page block may be
  removed at initial submission. Formatting errors (especially in Word) lead to desk rejection.
- **Page budget (FAccT 2027):** up to **14 pages including all figures and tables, excluding
  references** (most papers 12-14), **plus one extra page usable only for endmatter statements**;
  **references unlimited**; **appendices allowed at any length** at the end of the same PDF, not
  counted, and reviewers need not read them — keep the main paper self-contained. Papers at the
  Revision stage and accepted papers may use **15** content pages.
- **References:** ACM Reference Format for archival submissions; non-archival submissions may use
  any style (e.g., Bluebook).
- Do not modify margins, font, or spacing to gain space — editorial compression, not template
  tampering, is how you recover room.

## Mutual-anonymity sweep

FAccT review is **mutually anonymous**: authors and reviewers are hidden from each other. Because
FAccT papers often name systems, communities, and field sites, the leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|osf\.io|acknowledg|funded|grant|IRB #' | head
grep -rniE 'our (lab|group|team|university)|@[a-z0-9.]+\.edu' artifact/ --include='*.md' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
```

The FAccT-specific leaks: a **positionality statement left in the anonymous PDF** (it is
identity-revealing by design — remove it), acknowledgements or funding, an IRB protocol number, a
named field site or partner organization that identifies the team, and a data-availability link to a
personal repository.

## Required and optional endmatter (do not skip)

- **Generative AI Usage Statement — REQUIRED, even if you used no AI.** State whether and how
  generative AI was used (tool, model version, tasks — including routine grammar or translation
  help). FAccT 2027 follows ACM's authorship policy: AI may generate content only if disclosed, and
  substantive use (ideas, drafting, analysis, findings) also belongs in a Methods section when it is
  core to the work. AI cannot be an author. **Failure to disclose is grounds for desk rejection.**
  (FAccT 2026 instead prohibited LLM-generated manuscript text.)
- **Ethical Considerations statement — include at submission:** the ethical concerns and adverse
  impacts you considered and mitigated, anonymized; expected for human-subjects work, deployed
  systems, or sensitive data, and read seriously. Limitations do **not** go in endmatter — keep them
  in the body.
- **Withhold until acceptance:** Positionality, Author Contributions, Acknowledgements, Competing
  Interests — all identity-revealing; they must not appear in the anonymous submission.

## Archival vs non-archival

Choose deliberately: **archival** (the default) publishes in the ACM DL proceedings; **non-archival**
appears only as an abstract in the proceedings (useful for law, policy, humanities, and social-science
work headed to a journal; a conference-length version of a paper under journal review is allowed
**only** as non-archival, but a paper already accepted or published in a journal is not). The choice
is made at abstract registration and cannot be switched; reviewers are not told which you chose.
**All accepted papers are presented regardless** (in person expected, virtual option available).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Abstract/focus areas not registered by the earlier date | No submission slot exists | Nothing fixes this post-deadline — calendar it now |
| Main text over the 14-page budget | Desk-reject-grade | Cut or move to appendix; endmatter page does not absorb body text |
| Template altered (margins, shrunk font) | Desk-reject risk | Recompile clean, recover space editorially |
| Missing Generative AI Usage Statement (or undisclosed AI use) | Desk-reject grounds | Add it before upload, even if no AI was used |
| A coauthor never filled in the reviewer sign-up form | (Desk) rejection risk | Every author signs up before the deadline |
| Positionality/acks left in the anonymous PDF | Anonymity violation | Remove; restore only at camera-ready |
| Focus areas mismatched to the actual contribution | Wrong-discipline reviewers | Fix at registration; realign before the abstract gate |
| Identity leak (field site, IRB #, repo, funder) | Anonymity violation | Re-anonymize and re-host |

## Final-week order of operations

1. Freeze the body early; endmatter statements can be drafted in parallel.
2. Register title/abstract/authors/**focus areas** well before the abstract gate.
3. Write the Generative AI Usage Statement; draft Ethical Considerations and Adverse Impacts.
4. Run the mutual-anonymity checks on the *final* PDF and archive — and confirm positionality/acks
   are **out**.
5. Fill every OpenReview field — focus areas, conflicts for every coauthor's institution and recent
   collaborators, archival/non-archival choice — a day early; late conflicts are the classic
   midnight failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The abstract-gate and paper deadlines and their time zone.
- The page budget (14 + 1 endmatter page; 15 at Revision) and the exact acmart options.
- Whether the Revise decision, OpenReview platform, Generative AI Usage requirement (all introduced
  in 2026), the merged revision-plus-rebuttal, and the all-authors reviewer duty (2027) persist,
  plus the ACM Open APC level for the year (2026 subsidy $250/$350; 2027 not yet announced).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue facct-skills   # from a clone of the AJS repository
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
[FAccT submission status] ready / blocked / needs work
[Registration] title/abstract/authors/focus-areas locked by the earlier gate? yes/no
[Format] pages used (body/endmatter/refs), acmart anonymous-review compliance
[Anonymity] clean / leaks: <where> / positionality+acks withheld? yes/no
[Endmatter] Generative AI Usage present? Ethical Considerations (adverse impacts) included?
[Reviewer duty] every author signed up to review? yes/no
[Archival choice] archival / non-archival, deliberate?
[Fix queue] <ordered, with owners and dates before the deadline>
```
