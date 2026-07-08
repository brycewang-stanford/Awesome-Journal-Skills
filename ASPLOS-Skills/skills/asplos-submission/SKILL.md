---
name: asplos-submission
description: Use when running the final pre-upload audit of an ASPLOS submission — the 11-page limit covering figures/tables/footnotes with references excluded, the mandatory template, the no-"et al." full-name citation rule, hyperlinked DOIs, double-blind hygiene, GenAI disclosure, appendix self-containment, and HotCRP completion before the AoE deadline.
---

# ASPLOS Submission

This is the audit to run in the final week, against the exact PDF that will be
uploaded. Every rule below is the ASPLOS 2027 cycle as verified 2026-07-08 through
the CFP and the April-cycle HotCRP pages; the numbers are one edition's snapshot.

## Hard-format gates

| Gate | 2027 rule | Failure mode |
|---|---|---|
| Length | ≤ 11 pages, single-spaced, two-column — the count includes **all text, figures, tables, and footnotes** | Rejection without review is the stated risk for violations |
| References | Excluded from the 11 pages, unlimited | — |
| Template | The provided LaTeX template is **mandatory** | Geometry hacks are detectable and named as reject-risk |
| Appendices | Allowed in the same file, unlimited — but the 11 pages must be **self-contained**; reviewers are neither required nor encouraged to read appendices | Decision-critical content parked past page 11 simply does not exist |
| Deadline | 11:59 PM AoE on the cycle date (next: **September 9, 2026**) | HotCRP *saved-but-incomplete* is not submitted |

## The citation rules almost everyone gets wrong on the first try

ASPLOS imposes bibliography requirements that authors arriving from ISCA, SOSP, or
PLDI habitually violate:

- Every reference entry must list the **full, non-abbreviated first and last names of
  every co-author** — "J. Smith et al." fails on both counts.
- In-text citation numbers should be **hyperlinked** to their reference entries.
- Each entry should carry a **clickable link, preferably a DOI**.

Mechanical sweep before upload:

```bash
# et-al and initials-only detection in the bibliography
grep -nE 'et al\.|\b[A-Z]\.\s*[A-Z][a-z]+' references.bib | head -40
# DOI coverage: entries without a doi/url field
grep -c '@' references.bib; grep -ciE 'doi *=|url *=' references.bib
# PDF-side: confirm links are live (count of URI annotations)
pdftk paper.pdf dump_data 2>/dev/null | grep -c URI || true
```

## Double-blind sweep, ASPLOS flavor

- Cite your own prior work **in the third person**; if that is impossible, upload it
  as anonymized supplemental material instead.
- Do **not** write "removed for blind review" — the 2027 CFP disallows the
  placeholder itself.
- arXiv postings, tech reports, and talks are not prior publications, and the
  submission may *ignore* them to preserve anonymity — you are not obligated to cite
  or differentiate your own preprint.
- Sweep PDF metadata, embedded file paths, repository URLs, acknowledgments, and
  grant numbers. Workload traces or testbeds identifiable to one lab need neutral
  description.

## Disclosure and policy items

- **Generative AI:** ACM authorship policy applies — any GenAI use must be fully
  disclosed; when using the Acknowledgments section for the disclosure, it goes
  immediately before the References.
- **Concurrent submission:** related manuscripts of your own that are under review
  elsewhere are handled through the anonymized-supplemental mechanism, not silence.
- **Revision lineage:** if this submission follows a prior ASPLOS Major Revision,
  the change note must describe deltas **relative to the revision**, since the
  revision itself counted as a submission.

## Why the first two pages are a submission item, not a writing item

The 2027 process screens every paper with a rapid review that considers **only the
first two pages**. Before upload, verify as a mechanical check — not a stylistic
one — that pages 1-2 alone contain: the cross-layer problem, the one-sentence
insight, the mechanism sketch, and the headline result with its platform named.
If any of the four lives on page 3, the submission is structurally incomplete for
the process it enters. (Deeper treatment: `asplos-writing-style`.)

## Upload-day sequence

1. Recompile from a clean tree with the untouched template; diff page count.
2. Run the citation and anonymity sweeps above on the final PDF.
3. Complete every HotCRP field — title, abstract, authors, conflicts, topics — and
   upload.
4. Confirm the paper's HotCRP state reads **complete**, then have a co-author
   independently confirm it.
5. Freeze the exact submitted PDF and tag the repository commit; the response window
   and any revision will be argued against this artifact.

## HotCRP form fields deserve the same audit as the PDF

The form is part of the submission and desynchronizes from the paper easily:

- **Title and abstract** must match the PDF verbatim — reviewers bid on the form
  text, and a stale form abstract mis-routes the paper to the wrong expertise.
- **Author list and conflicts**: every author entered before the deadline, with
  conflicts (advisors, recent co-authors, institutional) declared per the form's
  definitions; missing conflicts create integrity problems after assignment, when
  they are unfixable.
- **Topic selections** steer reviewer matching; choose the intersection topics
  that describe the *contribution*, not every area the paper touches.
- Record who submitted, from which account — response-window access flows
  through that account, and a departed intern's orphaned HotCRP login is a
  classic December emergency.

## The last 48 hours, failure-ranked

1. **AoE arithmetic error** — 11:59 PM AoE is midday-plus the next day in much
   of Asia; compute each co-author's local equivalent in writing.
2. **Recompile drift** — a "trivial" final edit reflows a figure past page 11;
   any post-audit edit re-triggers the geometry check.
3. **Wrong-file upload** — the anonymized and camera-style builds coexist in the
   repo; name the submission artifact unambiguously (`paper-BLIND-final.pdf`).
4. **Bibliography regression** — a hastily added late citation with "et al."
   undoes the format pass; re-run the sweep after every reference edit.

## Output format

```text
[Verdict] ready / blocked (list blockers)
[Geometry] pages used incl. figures/footnotes: N/11 · template untouched: Y/N
[Citations] et-al hits: N · entries missing DOI: N · links live: Y/N
[Anonymity] third-person self-cites: Y/N · metadata clean: Y/N
[Disclosures] GenAI statement present/absent-and-unneeded · revision note lineage OK
[Two-page check] problem/insight/mechanism/result all within pages 1-2: Y/N
[HotCRP] status complete confirmed by second author: Y/N
```
