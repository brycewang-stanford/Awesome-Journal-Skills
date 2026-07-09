---
name: eacl-related-work
description: Use when positioning an EACL paper against fast-moving NLP literature, covering ACL-Anthology-first citation, correct Findings attribution, handling concurrent preprints fairly, freshness sweeps across recent *ACL rounds and European venues like LREC-COLING, and framing related work as a contrastive argument rather than a list.
---

# EACL Related Work

Use this to build an EACL related-work section that positions the contribution rather than
cataloguing the field. NLP literature moves fast and much of it is on arXiv before it is
archival, so the section must be **current, correctly attributed, and contrastive**. Reopen the
ACL Anthology and recent *ACL proceedings before finalizing.

## Cite from the Anthology first

- The **ACL Anthology** is the canonical record for *ACL papers; cite the Anthology version
  (with its venue and year) rather than an arXiv preprint when both exist. This fixes venue,
  year, and page numbers correctly.
- For a paper that appeared in **Findings**, attribute it as Findings (e.g. "Findings of ACL:
  EACL 2026"), not as the main conference — misattributing Findings as main is a common,
  noticeable error.

## Positioning, not listing

| Weak related work | Strong related work |
|---|---|
| "X did A. Y did B. Z did C." | "Unlike X, which assumes A, we ..." |
| A neutral literature dump | A contrast that sets up the gap |
| Only the famous references | The nearest competitors, named precisely |
| Silent on concurrent work | Concurrent preprints acknowledged fairly |

## Handle concurrent preprints fairly

- If a closely related preprint appeared **shortly before or during** your cycle, acknowledge it
  and state what is independent or different about your work — since ARR has no anonymity period,
  reviewers may well know both.
- Do not claim novelty a reviewer can disprove with a two-week-old arXiv paper; scope the claim
  instead.

## Freshness sweep

```text
Before submitting, sweep for missed neighbours:
  - recent ACL / EMNLP / NAACL / AACL / EACL proceedings in the Anthology
  - Findings volumes (often missed)
  - LREC-COLING for resources / multilingual / lower-resource work
  - TACL and Computational Linguistics for journal-track results
  - arXiv for the last ~3 months of concurrent preprints
```

## Mind the European and multilingual neighbourhood

- EACL's community overlaps heavily with **LREC-COLING** (resources, multilingual, lower-resource
  languages) and **EAMT** (machine translation). A related-work section on a multilingual or
  resource paper that ignores these venues will read as under-read to EACL reviewers.
- Cite work on the specific languages you study, including regional and non-English-language
  publications where relevant.

## Avoid sibling-venue misattribution

- The Anthology hosts every *ACL venue; confirm each citation's venue line before labeling it
  "EACL." See the sibling-confusion guard in `../../resources/exemplars/library.md`.

## Output format

```text
[Positioning] Contrastive / Listy
[Nearest competitors] <named, with the contrast to each>
[Attribution errors] <Findings-as-main, wrong venue, preprint-over-Anthology>
[Freshness gaps] <recent *ACL / LREC-COLING / preprints missed>
[Multilingual neighbourhood] <European/resource venues to add>
[Fix order] <what to revise>
```
