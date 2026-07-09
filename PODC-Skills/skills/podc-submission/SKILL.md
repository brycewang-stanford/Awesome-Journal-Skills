---
name: podc-submission
description: Use when auditing an ACM PODC submission for HotCRP readiness, covering the two-step abstract-registration then full-paper deadline, the ACM Master template with the 10-page-merits budget and unbounded full version, lightweight double-blind anonymization, the regular-paper-vs-Brief-Announcement choice, and desk-risk triage before the AoE cutoff.
---

# PODC Submission

Run this audit before uploading to the PODC HotCRP site (`podc26.hotcrp.com` for the 2026 cycle).
PODC — the ACM Symposium on Principles of Distributed Computing — judges a **model, a theorem, and a
proof**, so the submission is read as a mathematical argument, not as a system or a study. Every
number below was read from the PODC 2026 call for papers on 2026-07-09 via search renderings (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## The two-step deadline

PODC 2026 separates **abstract registration** from **full-paper submission**, and both are AoE:

- **Abstract registration** locks in title, abstract, authors, and conflicts a few days early
  (PODC 2026: **11 February 2026**). Miss it and the system will not accept the PDF later.
- **Full-paper submission** uploads the anonymized PDF (PODC 2026: **16 February 2026**, 23:59 AoE).

Register with the *real* title and abstract, not a placeholder — the abstract drives reviewer
bidding among a specialized PC, and a registered abstract that diverges from the final paper quietly
worsens your match.

## Regular paper or Brief Announcement — decide before formatting

PODC has two tracks, and choosing wrong wastes the slot:

| Situation | Track | Limit |
|---|---|---|
| Complete result with full proofs, ready for archival publication | **Regular paper** | Submission unbounded; **first 10 pages after the title page** carry the merits; published ≤10 pages |
| Work in progress, a result whose full version is (or will be) published elsewhere, or a small self-contained contribution | **Brief Announcement** | Submission **≤5 pages** incl. title/abstract/references; published ≤3 pages |

A Brief Announcement is a real strategic option — it timestamps a result, reaches the community, and
does **not** bar a later full paper elsewhere — not a demotion. But a regular result padded into a
BA, or an incomplete result stretched into a regular paper, both read as misjudged. See
`podc-supplementary` for the content split.

## Format and page budget

- **ACM Master template (`acmart`)**, two-column proceedings format, unmodified. This is the ACM
  path — do not carry an LNCS/LIPIcs habit over from a DISC or OPODIS submission.
- **The 10-page-merits rule:** a regular *submission* has **no page limit**, but only the abstract
  and the **first 10 pages following the title page** are guaranteed to be read. Everything after is
  read at the committee's discretion. So the first 10 pages must contain: the model, the result
  statement, the positioning against prior work, and the key technical/conceptual ideas — enough to
  decide acceptance. Authors are encouraged to submit the **full version** (all proofs) as the
  submission; the extra pages hold the proofs a convinced reviewer will check.
- **Published length:** accepted regular papers appear in **≤10 pages** two-column; Brief
  Announcements in **≤3 pages**. Plan the compression now, not in May.

## Lightweight double-blind sweep

PODC 2026 runs **lightweight double-blind** review: the submission must not reveal author names,
affiliations, or email addresses anywhere. This is a change from PODC's historically single-blind
practice — do not carry a prior single-blind habit forward, but also do not over-anonymize past what
the call asks.

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'          # scrub identifying metadata
pdftotext paper.pdf - | grep -nEi 'university|@[a-z0-9.]+\.edu|acknowledg|grant|thanks' | head
pdftotext paper.pdf - | grep -nEi 'our (previous|prior|earlier) (work|paper)|we showed in \[' | head
```

The theory-specific leaks: a self-citation phrased as "in our earlier paper [12] we proved..." (make
it third-person "[12] proves..."), a named funding grant, an acknowledgements block, a
non-anonymized arXiv link, or a repository/author page for an optional simulation. Neutralize
self-references and remove the acknowledgements until camera-ready.

## The proof is the deliverable

Because PODC has **no artifact track**, the reviewers' object of scrutiny is the **proof**. Before
upload, confirm:

- Every theorem invoked on the first 10 pages has its proof present in the submission/full version.
- The **model box** (network, timing, fault model, adversary, cost measure) is fixed *before* the
  first theorem and no proof silently changes it.
- Lemmas are stated where used and proved, not gestured at; a "proof sketch" in the body has its full
  version in the appendix.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Merits case not made within the first 10 pages | Effectively unreviewable | Restructure so model+result+delta+key ideas fit in 10 pages |
| Template altered / not `acmart` two-column | Format-reject grade | Recompile clean in the ACM Master template |
| Identity leak in PDF, self-citation, or linked repo | Anonymity violation | Third-person self-cites, strip metadata/acknowledgements, anonymize links |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Proof gap or missing lemma in a first-10-pages theorem | Soundness risk | Close the proof or weaken the claim before submitting |
| Regular result forced into a ≤5-page Brief Announcement (or vice versa) | Misrouted | Re-choose the track before formatting |
| Same result under review at DISC/SPAA/a journal | Dual-submission exposure | Withdraw one venue; a *preprint* on arXiv is allowed, a concurrent *submission* is not |

## Final-week order of operations

1. Freeze the model box and theorem statements early; the proof text can be polished, the claims
   cannot churn.
2. Register title/abstract/authors/conflicts before the 11 Feb cutoff.
3. Decide regular vs. Brief Announcement and format to the right budget.
4. Run the anonymization checks on the *final* PDF; make every self-citation third-person.
5. Confirm the first 10 pages make the full merits case and that all invoked proofs are present in
   the full version.
6. Fill every HotCRP field — topics that match your model/subarea, conflicts for every coauthor's
   institution and recent collaborators — a day early.
7. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The exact dates and whether abstract registration precedes the full-paper deadline.
- The double-blind wording and how strictly it is enforced (recently changed).
- Whether the cycle runs an author-response/rebuttal phase (待核实 for 2026).
- The Brief Announcement limits and the 10-page-merits wording.
- Any generative-AI-use disclosure policy (待核实).

## Output format

```text
[PODC submission status] ready / blocked / needs work
[Track] regular paper / brief announcement
[Registration] title/abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] first-10-pages merits case complete? acmart two-column? published-length plan?
[Anonymity] clean / leaks: <where>  (self-cites third-person? metadata scrubbed?)
[Proofs] every first-10-pages theorem has a present proof? model box fixed? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
