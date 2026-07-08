---
name: oopsla-supplementary
description: Use when deciding what rides along with an OOPSLA submission beyond the 23-page body — appendices, full proofs or mechanizations, extended tables, anonymized code — keeping the package double-anonymous, self-consistent with the PDF, and honest about what reviewers are obliged to read versus what a revision can absorb.
---

# OOPSLA Supplementary Material

The 23-page cap on an OOPSLA initial submission excludes references, required
statements, and appendices — so "supplementary" at OOPSLA is less a separate
upload category than a *layering decision*: what must live in the reviewed
body, what sits in appendices the body can survive without, and what waits
for the artifact stage after acceptance. The controlling rule set is the
current call (待核实 per cycle for upload mechanics on HotCRP); the
controlling *strategy* is the two-round review model.

## The layering rule

A reviewer deciding among Accept, Minor Revision, Major Revision, and Reject
must be able to reach a verdict **from the body alone**. Appendices exist to
let a skeptical reviewer verify, not to let the body skip its argument.

| Layer | Belongs there | Test |
| --- | --- | --- |
| Body (≤23 pp) | Claim statements, mechanism, proof sketches, headline evaluation, threats | Could a reviewer bucket the paper reading only this? |
| Appendix / supplement | Full proofs, extra benchmarks, case-study transcripts, calculus metatheory details | Does the body *state* what the appendix *establishes*? |
| Artifact (post-acceptance) | Runnable code, raw data, mechanization sources | Referenced by the Data-Availability Statement, not needed for the verdict |

## Anonymity applies to every byte

The supplement is reviewed under the same double-anonymous rules as the PDF:

- Strip repository remotes, commit author lines, CI configs, and `~/`-rooted
  paths from any code archive; check binary blobs (notebooks, PDFs) for
  embedded author metadata.
- Anonymized-archive services or a scrubbed zip both work; a "private repo we
  can add reviewers to" does not — access events identify reviewers, which
  breaks the process from the other direction.
- Rename internal project codenames that are Googleable to your group.

## Consistency: the silent killer across rounds

Because a Major Revision returns to the *same reviewers* next round, any
mismatch between body and supplement is remembered. Before each round's
upload:

```text
Cross-check pass:
  numbers   every value quoted in body == value in appendix tables (script it)
  theorems  numbering and side conditions identical body vs full proof
  configs   flags/versions in appendix match the reproducibility ledger
  claims    nothing in the supplement contradicts a scoped claim in the body
  pointers  every "see Appendix X" resolves; no orphan appendices
```

## What NOT to put in the supplement

- **Rescue material** — text that exists because the body overran 23 pages.
  Compress the body instead (`oopsla-writing-style`); reviewers are not
  obliged to read overflow prose, and relying on it undermines the bucket
  decision.
- **Unfinished experiments** flagged "preliminary." In a revision-capable
  venue, half-results invite a Major Revision demanding the full version;
  either finish them or cut them and scope the claims down.
- **De-anonymizing generosity** — screenshots of dashboards, grant-numbered
  cluster names, or user-study consent forms bearing the institution.

## Revision-round dynamics

An invited revision gets 25 pages: the extra room is for absorbing what
reviewers demanded, which often means *promoting* appendix material into the
body. Structure appendices from day one as promotable units (self-contained,
labeled, with their own claim sentences) so a Minor Revision is an editing
job rather than a rewrite (`oopsla-review-process`).

## Output format

```text
[Layering] body-sufficient verdict possible: yes/no + misplaced items
[Anonymity] supplement scrub: clean / findings
[Consistency] cross-check pass results (numbers/theorems/configs/claims/pointers)
[Promotable units] appendices ready to absorb into a revision: <list>
[Cut list] material that should not ship at all
```
