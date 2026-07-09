---
name: facct-submission
description: Use when auditing an ACM FAccT submission for OpenReview readiness — the mandatory abstract-registration gate with focus-area selection, the acmart anonymous/review PDF, the 14-page (+1 endmatter) budget, mutual anonymity, the required Generative AI Usage Statement and optional ethics/adverse-impacts statements, archival vs non-archival choice, and desk-reject triage before the deadline.
---

# FAccT Submission

Run this audit before uploading to the FAccT OpenReview site. FAccT papers are **archival ACM
proceedings** in an *interdisciplinary* responsible-AI venue, reviewed **mutually anonymously** by a
mixed CS+law+social-science pool. Every number below was read from the FAccT 2026 CFP and Author
Guide on 2026-07-09 via search renderings (see `resources/official-source-map.md`); treat them as a
one-cycle snapshot and reopen the live call first.

## The two-step deadline (abstract gate first)

FAccT separates **abstract registration** from **paper submission**, and the gate is hard:

- **Abstract registration** locks title, abstract, authors, and **focus areas** roughly a week early
  (FAccT 2026: **8 January 2026**). Authors who do not register by this date **cannot submit a
  paper** — the focus areas drive reviewer/AC matching in the mixed pool.
- **Paper submission** uploads the anonymized acmart PDF (FAccT 2026: **13 January 2026**).

Register with the *real* title, abstract, and honestly chosen focus areas, not placeholders — a
mismatch between your registered focus areas and your actual contribution mis-matches you to
reviewers from the wrong discipline, the most damaging thing that can happen at an interdisciplinary
venue.

## Format and page budget

- **ACM `acmart` template**, built anonymized for review, e.g.
  `\documentclass[manuscript,screen,review,anonymous]{acmart}` (single-column review format). The
  camera-ready later uses the `sigconf` proceedings format.
- **Page budget (verify per cycle):** up to **14 pages excluding references** (most papers 12-14),
  **plus one additional content page** for endmatter statements; **references unlimited**. Revised
  and accepted papers may use **15** content pages.
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

- **Generative AI Usage Statement — REQUIRED.** State whether and how generative AI was used to
  prepare the manuscript. FAccT **prohibits** using generative AI to wholesale-generate text. A
  missing statement is a compliance defect independent of the paper's merit.
- **Optional but expected where relevant:** Ethical Considerations and Adverse Impacts statements —
  include them anonymized; they are read seriously.
- **Withhold until acceptance:** Positionality, Author Contributions, Acknowledgements, Competing
  Interests — all identity-revealing; they must not appear in the anonymous submission.

## Archival vs non-archival

Choose deliberately: **archival** (the default) publishes in the ACM DL proceedings; **non-archival**
presents at the conference without proceedings publication (useful for work headed to a journal or
already-published elsewhere). **All accepted papers present in person regardless.** Confirm the
current non-archival mechanics on the Author Guide (**待核实** per cycle).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Abstract/focus areas not registered by the earlier date | No submission slot exists | Nothing fixes this post-deadline — calendar it now |
| Main text over the 14-page budget | Desk-reject-grade | Cut or move to appendix; endmatter page does not absorb body text |
| Template altered (margins, shrunk font) | Desk-reject risk | Recompile clean, recover space editorially |
| Missing Generative AI Usage Statement | Compliance defect | Add it before upload |
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
- The page budget (14 vs 15, endmatter-page counting) and the exact acmart options.
- Whether the Revise decision, OpenReview platform, and Generative AI Usage requirement persist
  (all introduced in 2026), plus non-archival mechanics and any APC/fee-waiver policy (**待核实**).

## Output format

```text
[FAccT submission status] ready / blocked / needs work
[Registration] title/abstract/authors/focus-areas locked by the earlier gate? yes/no
[Format] pages used (body/endmatter/refs), acmart anonymous-review compliance
[Anonymity] clean / leaks: <where> / positionality+acks withheld? yes/no
[Endmatter] Generative AI Usage present? ethics/adverse-impacts included?
[Archival choice] archival / non-archival, deliberate?
[Fix queue] <ordered, with owners and dates before the deadline>
```
