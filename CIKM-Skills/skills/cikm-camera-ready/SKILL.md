---
name: cikm-camera-ready
description: Use when turning an accepted CIKM paper into its ACM proceedings version inside the short notification-to-camera-ready window, covering de-anonymization, the e-rights and TAPS pipeline into the ACM Digital Library, CCS concepts and metadata, GenAI-disclosure retention, artifact link publication, and Rome presentation logistics.
---

# CIKM Camera Ready

CIKM 2026 notifies on August 7 and collects camera-ready on August 20 — a thirteen-day
window (source map, 2026-07-08). Because CIKM publishes through ACM's Digital Library
(the CIKM '25 volume is DOI 10.1145/3746252), that window contains not just editing
but ACM's production machinery: e-rights completion, then source upload through TAPS,
whose validation rejects malformed LaTeX. Start the clock at notification, not when
the camera-ready email arrives.

## Thirteen-day sequence

| Day | Action |
|---|---|
| 0-1 | Reopen the camera-ready instructions; confirm final page allowance (待核实 whether acceptance adds pages) |
| 1-3 | De-anonymization pass; apply the concern → edit ledger from `cikm-author-response` |
| 3-5 | e-rights form completed by the designated author; copyright block generated |
| 5-9 | TAPS-clean source: standard `acmart`, no forbidden packages, rights commands in place |
| 9-11 | Metadata layer: CCS concepts, keywords, author ORCIDs, affiliations as they should appear forever |
| 11-13 | Final validated PDF; artifact links live and public; buffer for TAPS rejects |

## De-anonymization is more than adding names

- Restore authors, affiliations, acknowledgments, and funding — then re-check the
  page budget, since these lines cost space in a two-column layout.
- Rewrite third-person self-citations into honest first-person where clarity gains
  ("we extend our earlier system [12]"), and un-blind any datasets or systems that
  were pseudonymized for review — Applied Research papers especially, where the
  deployment context can finally be named if the operator permits.
- Replace anonymized artifact placeholders with the real repository, license chosen,
  README current, and test every URL logged out.
- **Keep the GenAI Usage Disclosure section.** It was a submission requirement under
  the ACM AI policy, and quietly deleting it at camera-ready contradicts the record;
  update it only if tool usage changed during revision.

## The metadata outlives the talk

ACM DL entries are what the paper *is* for the next decade of citation, indexing,
and search. Spend real attention on: CCS concepts that match where readers browse
(Information systems → retrieval, data mining, or knowledge representation lanes);
author-name forms consistent with each author's dblp record — CIKM's tri-community
audience finds papers through dblp and the DL, and a name variant forks a
publication record; and an abstract whose first sentence stands alone in a DL
search-result snippet.

## Revision scope discipline

Camera-ready edits answer reviewer concerns and fix errors; they do not grow the
contribution. A safe test per edit: would the reviewers who accepted the paper
recognize it as the paper they accepted? Clarifications, added citations, scoped
limitation sentences — yes. New experiments upgrading a claim — no; put those in
the artifact README or the next paper.

## TAPS survival notes

TAPS (The ACM Publishing System) compiles the submitted source itself, and its
failures cluster predictably:

| TAPS complaint | Usual cause | Fast fix |
|---|---|---|
| Build failure | Non-whitelisted LaTeX packages | Replace with ACM-approved equivalents early, not at day 12 |
| Missing rights block | e-rights not completed before source upload | Sequence: e-rights first, then paste the generated commands |
| Figure errors | Exotic image formats, missing fonts in PDFs | Flatten to standard PDF/PNG with embedded fonts |
| Metadata mismatch | Title/authors differ between form and source | Make the e-rights form the single source of truth |
| Reference warnings | Hand-formatted bibliography | Use the ACM reference format via BibTeX, resist manual edits |

Upload a test build to TAPS as soon as credentials arrive rather than polishing
locally until the deadline; the validator's opinion is the only one that counts,
and its error messages take a day of turnaround to act on when accounts, uploads,
and co-author availability are factored in.

## Proceedings-record hygiene

Small camera-ready decisions with decade-long consequences: order authors exactly
as agreed at submission (the abstract-gate freeze means the *set* cannot change;
the displayed order and name spellings still deserve a final confirmation round);
use each author's canonical name form and ORCID so the DL entry merges into the
right dblp profile; make the artifact link in the PDF a stable one (archival DOI
or a release-tagged repository URL), because the proceedings PDF cannot be edited
after publication while repositories move.

## The camera-ready diff audit

Before final upload, produce an explicit diff against the reviewed PDF and audit
it three ways:

1. **Every reviewer concern** from the ledger maps to a visible change or a
   recorded no-change reason — the accountability pass.
2. **Every change** maps back to a reviewer concern, an error fix, or
   de-anonymization — the scope-discipline pass; unprompted "improvements" are
   where accepted papers acquire new errors nobody reviews.
3. **Numbers unchanged**: any table value that moved needs a cause you can state
   in one sentence (bug fix, seed policy correction) and, if the movement affects
   a claim, a flag to the chairs rather than a silent swap.

Archive the reviewed PDF, the camera-ready PDF, and the diff notes together; this
bundle answers every future "what changed after review?" question, including your
own two years later.

## After publication

The DL record is effectively immutable, so post-publication problems route
through process, not re-upload: errata via the chairs/ACM where warranted, code
fixes via new repository releases clearly marked as post-publication (never
rewrite the proceedings-tagged release), and claim corrections — worst case — via
a note in the repository README that honestly states what the paper got wrong.
Teams that handle this transparently keep the baseline-citation afterlife
(`cikm-reproducibility`); teams that quietly retag releases lose it.

## Rome logistics strand (parallel, not sequential)

Registration, visa lead time for Italy/Schengen, and presentation format
(presenter-attendance and registration obligations for CIKM 2026 were not verifiable
— 待核实, check the acceptance email) run in parallel with production. Assign the
logistics strand to a different author than the TAPS strand; the thirteen days do
not fit both jobs for one person.

## Output format

```text
[Days remaining] <n of the notification→camera-ready window>
[Production state] e-rights / TAPS source / validated PDF
[De-anon checklist] names / self-citations / artifacts / GenAI section retained
[Metadata state] CCS concepts / ORCID-dblp consistency / abstract snippet
[Open risks] <page overflow, TAPS reject, dead links, visa/registration>
```
