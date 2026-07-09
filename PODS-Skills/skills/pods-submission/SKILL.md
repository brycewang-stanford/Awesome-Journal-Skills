---
name: pods-submission
description: Use when auditing an ACM PODS research submission for EasyChair readiness, covering the chosen cycle's abstract-then-paper deadlines, the acmsmall[review,anonymous] format and 15-page budget, the at-submission proof appendix, lightweight double-anonymity, the declared conflicts of interest, PACMMOD-track publication, and desk-risk triage before the AoE cutoff.
---

# PODS Submission

Run this audit before uploading to the PODS EasyChair site. PODS research papers are published in the
**PACMMOD PODS track** and presented at the symposium, and the review is **lightweight
double-anonymous** with a proof appendix that ships with the submission. Every number below was read
from the PODS 2026/2027 calls on 2026-07-09 via search renderings of the `sigmod.org` PODS pages (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## Pick the cycle, then the two-step deadline

PODS runs **multiple cycles per year**; choose the cycle whose paper deadline your proofs will
actually be complete for. Within a cycle there are two steps, both AoE:

- **Abstract (and COI) registration** locks title, abstract, authors, and the declared conflicts of
  interest about a week early (PODS 2026 Cycle 1: 3 Jun 2025; Cycle 2: 3 Dec 2025). Miss it and the
  system will not accept the PDF.
- **Full paper submission** uploads the anonymized PDF (PODS 2026 Cycle 1: 10 Jun 2025; Cycle 2: 10
  Dec 2025). As of 2026-07-09 the live next deadline is **PODS 2027 Cycle 2: abstract+COI 10 Oct
  2026, paper 17 Oct 2026**.

Register with the *real* title and abstract; the abstract drives reviewer bidding, and a placeholder
that diverges from the paper worsens your PC match.

## Format and page budget

- **`\documentclass[acmsmall,review,anonymous]{acmart}`**, unmodified, single-column review format —
  this is the current PODS format, not the older two-column `sigconf` style and not an IEEE template.
- **Budget (verify per cycle):** up to **15 pages excluding references**, plus **unlimited
  references**, plus a **clearly marked appendix of unlimited length incorporated in the same PDF**.
  **No online/external appendices** — every proof ships with the submission.
- Margins, font, and spacing are fixed by `acmart`; recover space by editorial compression and by
  moving long proofs to the appendix, not by tampering with the template.

## Lightweight double-anonymous sweep

PODS review is **double-anonymous**: omit author names and affiliations, phrase self-citations in the
third person, and remove identity-revealing material from the body *and* the appendix.

```bash
# Mechanical pass on the submission PDF (single file: body + refs + appendix)
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'acknowledg|grant|funded|thanks|university of|@[a-z0-9.]+\.edu' | head
pdftotext paper.pdf - | grep -nEi 'arxiv\.org/abs|github\.com|https?://[a-z0-9.-]*~' | head
```

The theory-specific leaks: an acknowledgement or funding line, a named system or prototype that
identifies the group, a self-citation phrased in the first person ("in our earlier work [12] we..."),
and a link to an author's arXiv preprint or homepage. Withhold or anonymize the arXiv full version
until acceptance.

## Conflicts of interest

- Declare the full COI list at submission (PODS 2027 Cycle 2 pairs the COI declaration with the
  abstract deadline of 10 Oct 2026). Include advisors, recent coauthors, and same-institution PC
  members per the call's definition.
- An incomplete COI list is a real integrity problem, not a formality; assemble it a day early.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| A stated theorem with no complete proof (body or appendix) | Reject-grade | Complete the proof or scope the claim before submitting |
| Body over 15 pages (excl. refs) | Format violation | Move long proofs to the appendix; references do not count |
| Template altered, or old `sigconf`/two-column used | Format ground for return | Recompile in `acmsmall[review,anonymous]` |
| Identity leak in body or appendix (acks, named system, arXiv link) | Anonymity violation | Scrub and re-anonymize; withhold the arXiv link |
| Abstract/COI not registered by the earlier date | No submission slot | Nothing fixes this post-AoE — calendar it now |
| A proof deferred to an external/online appendix | Not allowed at PODS | Fold all proofs into the single submitted PDF |
| Same result under review elsewhere | Dual-submission exposure | Withdraw one; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the theorem statements and complete every proof; the appendix is not a place to hide a gap.
2. Register abstract, authors, and the COI list well before the abstract cutoff.
3. Assemble the appendix into the single PDF with forward references from the body.
4. Run the mechanical anonymity checks on the *final* PDF (body + appendix), not a draft.
5. Fill every EasyChair field — topics matching your result, coauthors, conflicts — a day early.
6. Re-download the uploaded PDF and read the hardest proof cold to confirm it is the file you meant.

## Reverify each cycle

- Which cycle you are targeting and its exact abstract/paper AoE dates.
- The page budget and the exact `acmart` variant the current call names.
- The revision/shepherd mechanics, the resubmission rule, and any AI-disclosure policy — all
  cycle-volatile; none should be assumed stable.

## Output format

```text
[PODS submission status] ready / blocked / needs work
[Cycle] cycle 1 / cycle 2, abstract+COI and paper dates for it
[Proofs] every stated theorem fully proved (body/appendix)? yes/no
[Format] pages used (body/refs/appendix), acmsmall[review,anonymous] compliance
[Anonymity] clean / leaks: <where, incl. appendix and arXiv link>
[COI] declared list complete? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
