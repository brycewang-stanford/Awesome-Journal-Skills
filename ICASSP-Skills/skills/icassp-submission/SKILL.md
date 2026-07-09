---
name: icassp-submission
description: Use when auditing an ICASSP submission before the CMS portal deadline — the IEEE 4+1 page format, the single-blind rule that the author list must appear, EDICS subject selection, the Compliance-with-Ethical-Standards statement, PDF eXpress validation, the 9-papers-per-author cap, dual-submission policy, and desk-reject triggers.
---

# ICASSP Submission

Run this audit against the live ICASSP paper kit on the current-year CMS portal
(`cmsworkshops.com/ICASSP<year>/papers.php`), not against memory. ICASSP reissues its kit each
cycle, and because the whole review pipeline assumes a uniform IEEE two-column object, the
format is checked mechanically at upload. The next major gate as of 2026-07-09 is the **ICASSP
2027 full-paper deadline, reported ~16 September 2026** — verify on the live 2027 call.

## The format contract: 4 + 1

An ICASSP regular paper is **4 pages** of technical content — text, figures, and references all
count — with an **optional 5th page** that may hold **only** references, funding acknowledgements,
and the Compliance-with-Ethical-Standards statement. Consequences to internalize:

- There is **no reviewed appendix or supplement** that decides acceptance. Whatever a reviewer
  must see to accept the paper lives on the four content pages.
- References compete with content on pages 1-4 unless they spill to page 5; plan the reference
  budget early.
- Use the official IEEE two-column template from the paper kit with fonts, margins, and column
  measure untouched, and confirm the PDF passes **IEEE PDF eXpress** before the portal will
  accept it.

## Single-blind: the inverted anonymity rule

ICASSP review is **single-blind**. Unlike OpenReview or ISCA venues, you **must include the
author list and affiliations** in the submitted PDF; reviewers see who you are, you do not see
them. The failure mode here is the opposite of an identity leak:

- A **missing or wrong author block** is the defect to catch, not a self-citation.
- Write self-citations in normal first person ("in our earlier work [4]"); no anonymization
  gymnastics are needed.
- Acknowledgements and funding are allowed and belong on page 5, not hidden.

## Portal and metadata (CMS, not CMT)

- Submission is through **Conference Management Services (CMS)** at `cmsworkshops.com`, not
  Microsoft CMT and not OpenReview — a genuine ICASSP fingerprint.
- Choose the **EDICS** subject category that routes the paper to the correct technical committee;
  the routing decision comes from `icassp-topic-selection`, not from whoever uploads.
- The CMS abstract must match the PDF abstract; it is what area organizers read.
- **No single author may appear on more than 9 papers** in a cycle — check co-author load early.
- Answer the dual-submission attestation honestly: the same work may not be under review at
  another conference or journal simultaneously.

## Desk-reject and triage table

| Trigger | Severity at ICASSP | Repair window |
|---|---|---|
| Fifth page carrying content beyond references/acks/ethics | Desk reject | None after deadline |
| Template tampering caught by PDF eXpress | Desk reject | None |
| Missing author list (single-blind requires it) | Non-compliant submission | Only before deadline |
| Missing Compliance-with-Ethical-Standards statement | Compliance flag | Only before deadline |
| Author on more than 9 papers | Enforced cap | Withdraw one before deadline |
| Dual submission to another venue | Integrity violation | None |

## Final 72 hours, in order

1. Rebuild the PDF from a clean clone; confirm the paper-kit template version is current and
   PDF eXpress passes.
2. Confirm the author block, affiliations, and page-5 acknowledgements/ethics statement are
   present and correct — the single-blind checklist.
3. Verify every figure is legible at print resolution and no float pushes past four pages.
4. Set EDICS and the CMS abstract to match the PDF; declare all co-authors and their conflicts.
5. Upload, download what CMS stored, and read *that* file end to end.

## Track choice before you submit

- **Standard track** — 4+1 pages, TPC review, proceedings in IEEE Xplore.
- **OJSP-ICASSP** — 8+1 pages, reviewed by the Open Journal of Signal Processing board, open-access
  publication, presented but not in the proceedings (earlier pre-registration deadline).
- **SPS-journal presentation** — present a recently accepted SPS-journal paper, not re-reviewed,
  not in proceedings.

Confirm each track's separate deadline in the current call; see `icassp-workflow`.

## Output format

```text
[Submission verdict] ready / fixable / not ready
[Format] 4+1 compliance, template integrity, PDF eXpress result
[Single-blind] author list present, affiliations, page-5 acks/ethics
[Metadata] EDICS, abstract match, author list, dual-submission answer, 9-paper cap
[Track] standard / OJSP-ICASSP / journal-presentation / grand-challenge
[Blockers] <ordered list>
```

## Currency note

The 4+1 format, single-blind policy, CMS portal, and 9-paper cap were checked 2026-07-09 against
ICASSP 2026 (Barcelona) renderings (see `../../resources/official-source-map.md`). Every value is
cycle-specific; the ICASSP 2027 Toronto cycle publishes its own kit and calendar — re-open it.
