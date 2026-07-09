---
name: eacl-camera-ready
description: Use when preparing an EACL or Findings-of-ACL-EACL camera-ready after commitment acceptance, covering the extra content page, de-anonymization, AI-assistance disclosure, satisfying the meta-review's required changes, ACL Anthology metadata and CC BY licensing, registration and presentation obligations, and the public artifact release.
---

# EACL Camera-Ready

Use this once a paper is accepted at commitment to EACL (main conference or Findings of ACL:
EACL). The camera-ready is a short, high-stakes window: for EACL 2027 the ARR notification was
November 12, 2026 and camera-ready was due November 26, 2026. Reopen the edition's camera-ready
instructions and the ACL Anthology policy pages before finalizing.

## Spend the extra page well

- Long and short papers each get **one additional content page** at camera-ready (up to 9 / 5).
  Use it to pay down the debts reviewers named: a promised ablation, a clearer error analysis,
  a fuller multilingual result — not filler.
- The **Limitations** section stays outside the page budget; expand it if review surfaced new
  caveats, and keep it honest.

## De-anonymize cleanly

| Item | Camera-ready action |
|---|---|
| Author names / affiliations | Add on the title block; confirm order (author list is frozen from commitment) |
| Acknowledgements | Add funding, grants, compute credits |
| "Anonymous prior work" citations | Restore the real citations |
| Repo / dataset links | Point to the public, de-anonymized release |
| PDF metadata | Regenerate so it matches the deanonymized authors |

Remember the commitment rule: **author membership cannot change after commitment** (order may).
Do not add a "forgotten" co-author at camera-ready.

## Satisfy the meta-review

- The action editor's meta-review often lists **required or expected changes**. Treat these as a
  checklist and make each change visibly; camera-ready is where the acceptance conditions are
  honored.
- Disclose **AI assistance** consistent with the Responsible NLP checklist answer you filed —
  the camera-ready and the checklist must agree.

## ACL Anthology metadata

```text
Metadata to get right for the Anthology record:
  - Title: correct casing; math/diacritics render (European-language names, é/ø/ł/ş, etc.)
  - Authors: full names, correct order, ORCID if requested, affiliations
  - Abstract: matches the PDF abstract
  - License: CC BY 4.0 (standard for post-2016 *ACL material)
  - Venue line: names the correct EACL edition or "Findings ... EACL"
```

Diacritics and non-ASCII author names are common in the European community — verify they render
in the final Anthology entry rather than assuming the PDF is enough.

## Registration and presentation

- At least one author must **register and present** (in person or in the hybrid format the
  edition offers). Camera-ready acceptance does not substitute for registration.
- Prepare the required presentation format (oral/poster) as assigned; confirm the slot and any
  video/upload requirement on the edition's program pages.

## Public artifact release

- Flip the anonymized ARR supplement into a **public release**: real repo URL, license, a
  version tag matching the camera-ready, and a README that reproduces the headline table.
- See `eacl-artifact-evaluation` for packaging and `eacl-reproducibility` for the claims audit
  the release should pass.

## Final checklist

```text
[ ] Extra page used for substance, not filler
[ ] De-anonymized: authors, acknowledgements, citations, links, metadata
[ ] Author list unchanged from commitment (order-only edits ok)
[ ] Meta-review required changes all made
[ ] AI-assistance disclosure matches the checklist
[ ] Anthology metadata correct incl. diacritics and license
[ ] Registration done; presentation format prepared
[ ] Public artifact released and versioned
```

## Output format

```text
[Camera-ready readiness] Ready / Needs fixes / Not ready
[Extra-page plan] <what the added page carries>
[De-anonymization] <status of names/acks/citations/links/metadata>
[Meta-review compliance] <each required change addressed>
[Anthology + license] <metadata and CC BY status>
[Logistics] <registration + presentation + artifact release>
```
