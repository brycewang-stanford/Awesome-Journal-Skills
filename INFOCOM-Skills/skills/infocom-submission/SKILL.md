---
name: infocom-submission
description: Use when auditing an IEEE INFOCOM main-conference submission for EDAS readiness, covering the two-step abstract-then-paper registration, the IEEEtran two-column 10-page/9-page-of-text budget, double-blind anonymization of the PDF and metadata, the five-papers-per-author cap, and desk-reject triage before the AoE cutoff.
---

# INFOCOM Submission

Run this audit before the EDAS deadline. INFOCOM is a **large IEEE ComSoc flagship** — on the
order of ~1,400-1,500 submissions per year — so mechanical non-compliance is caught at scale and
papers over the length limit are simply **not reviewed**. Every number below was read from the
INFOCOM 2026/2027 Call for Papers and Submission Guidelines on 2026-07-09 via search renderings of
the `ieee-infocom.org` URLs (see `resources/official-source-map.md`); treat them as a one-cycle
snapshot and reopen the live call first.

## The two-step deadline (abstract, then paper)

INFOCOM separates the **abstract/metadata registration** from the **full-paper upload**, both on
EDAS and both AoE:

- **Abstract/metadata** (INFOCOM 2026: 24 July 2025) locks title, all co-authors, and a **≤200-word
  abstract** into EDAS. This metadata drives the automated review assignment, so it must reflect the
  real paper.
- **Full paper** (INFOCOM 2026: 31 July 2025; INFOCOM 2027: 31 July 2026) uploads the anonymized
  PDF. Miss the abstract step and EDAS will not accept the PDF later.

Register with the *real* title and abstract, not a placeholder — the assignment system matches your
manuscript and abstract to TPC members' publications, and a vague abstract worsens your reviewer
fit before a human ever reads the paper.

## Format and page budget (hard)

- **IEEEtran.cls version 1.8, unmodified**, two-column: `\documentclass[10pt, conference,
  letterpaper]{IEEEtran}`, 10-point Times, default margins and line spacing. This is the IEEE path,
  not ACM/USENIX — do not carry an `acmart` single-column habit over from a sibling venue.
- **Page budget:** **10 pages maximum**. The **main text — including figures, tables, appendices,
  and everything other than references — must be no more than 9 pages**; only references may use the
  10th page. There is **no separate supplementary or appendix channel** at review time.
- Papers that violate the length limit **are not reviewed** — this is a mechanical, non-negotiable
  screen, not a soft preference. Recover space by editing, never by shrinking the font or margins.

## Double-blind sweep

INFOCOM runs **double-blind** review: author identities are removed from the PDF **title page,
body, and PDF metadata**. Because networking papers lean on testbeds, traces, and released tools,
the leak surface is wide:

```bash
# Mechanical pass on the submission PDF before EDAS upload
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'   # scrub metadata identity
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|our (prior|previous) (work|system)|acknowledg|this work was supported' | head
grep -nEi '\\thanks|\\author\{[^}]*[A-Za-z]' paper.tex | head   # stray author/thanks blocks
```

The networking-specific leaks: a self-citation phrased as "our previous system," a testbed or
university cluster name, a released-tool GitHub URL, a funding/acknowledgement line left in, and
identifying dataset names. Cite your own prior work in the **third person** and defer
acknowledgements and grant numbers to the camera-ready.

## The five-paper cap

An individual may be listed as author or co-author on **at most five** papers submitted to a given
INFOCOM; if exceeded, only the first five received before the deadline are reviewed. On a large
group's submission sprint, confirm nobody crosses the cap **before** the abstract deadline — EDAS
enforces it on receipt order, and a late sixth paper is silently dropped.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Text (incl. appendices) over 9 pages, or total over 10 | Not-reviewed-grade | Cut or compress into the budget; references do not absorb body text |
| Template altered (margins, shrunk font, wrong `IEEEtran` options) | Named non-compliance | Recompile clean with the required preamble; recover space editorially |
| Author identity in PDF, metadata, or a "our system" self-citation | Double-blind violation | Re-anonymize; scrub PDF metadata; third-person self-citations |
| Abstract/metadata not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| A coauthor already on five submissions | Sixth paper dropped | Rebalance authorship before the abstract deadline |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; the system model and results cannot churn in the last days.
2. Enter title/abstract/co-authors into EDAS before the abstract cutoff; confirm the ≤200-word
   abstract matches the paper.
3. Compile with the exact IEEEtran preamble; measure the 9-page text boundary with references
   excluded, not the 10-page total.
4. Run the mechanical double-blind checks on the *final* PDF, including `pdfinfo` metadata.
5. Fill every EDAS field — topics that match your evidence so the automated assignment routes you
   to the right TPC members, and every coauthor's affiliation — a day early.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The exact abstract and full-paper dates and their AoE/ET cutoffs.
- The page-budget wording (the 9-of-10 text/references split) and which IEEEtran revision is
  required.
- The per-author paper cap (5 for 2026), dual-submission wording, and any AI-disclosure rule — all
  cycle-volatile.

## Output format

```text
[INFOCOM submission status] ready / blocked / needs work
[Registration] title/abstract/co-authors in EDAS by the abstract deadline? yes/no
[Format] IEEEtran preamble correct? text pages (excl. refs) / total pages
[Anonymity] clean / leaks: <where, incl. PDF metadata and self-citations>
[Author cap] any coauthor at 5 submissions already? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
