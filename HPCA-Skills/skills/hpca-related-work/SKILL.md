---
name: hpca-related-work
description: Use when building an HPCA related-work section: sweeping the HPCA/ISCA/MICRO/ASPLOS record on dblp and IEEE Xplore, writing lineage paragraphs with structural deltas, blinding self-citations without touching the bibliography, and honoring the rule that every reference lists all its authors.
---

# HPCA Related Work

Use this to position an HPCA paper against decades of computer-architecture
literature. The bar is a related-work section that reads as a **lineage with
structural deltas**, not a citation pile — and one that respects HPCA's two
bibliography rules: references are never blinded, and every reference lists all of
its authors.

## Sweep the whole architecture record

Architecture ideas recur across four venues and forty years. Search the
**publisher-neutral spine (dblp)** plus **IEEE Xplore**, not a single library:

- dblp HPCA series (`dblp.org/db/conf/hpca/`) for the venue's own line, and the
  ISCA/MICRO/ASPLOS series for cross-venue lineage.
- IEEE Xplore for HPCA's published volumes; ACM DL for the ACM-published siblings.
- The HPCA Test of Time Award list for the load-bearing ancestors of your subfield.

A mechanism you think is new often has a named ancestor at HPCA 2003 or ISCA 2006;
find it before a reviewer does.

## Write lineage, not a pile

Each related-work paragraph should name a prior line, then state the **structural
delta** your paper adds — what changes in the machine or the mechanism, not just that
you are "different." Group by mechanism family, not chronologically.

| Weak related-work move | Stronger HPCA move |
|---|---|
| "Many prefetchers exist [3,7,9,12]." | "History prefetchers [X] cover irregular patterns but issue regardless of bandwidth; we gate on measured utilization." |
| Listing venues and years | Naming the mechanism each prior work uses and where it breaks |
| Omitting a famous ancestor | Citing it and stating the concrete delta |
| Blinding your own prior work out | Citing it in the third person, un-blinded |

## Blind the voice, never the bibliography

Double-blind means the *prose* must not reveal you, but the *references* must stay
intact:

- Cite your own prior work in the **third person** ("Prior work [12] proposed …"),
  never remove it.
- Do not anonymize, omit, or "et al."-abbreviate any reference — HPCA requires each
  reference to list **all** its authors, and a missing citation reads as either a
  gap or a blinding hack.
- Keep acknowledgments and funding out of the submitted version; they return at
  camera-ready.

## The concurrency and preprint question

Recent HPCA guidance asks PC members not to hold arXiv or CAL preprints against a
submission. Position honestly against concurrent work you know of, but do not use a
preprint to claim priority in a way that de-anonymizes you. When a truly concurrent
result exists, name the difference in scope rather than ignoring it.

## Build sequence

```text
1. dblp + IEEE Xplore sweep across HPCA/ISCA/MICRO/ASPLOS for the mechanism family
2. Pull the Test-of-Time ancestors of the subfield
3. Draft one paragraph per mechanism line, each ending in a structural delta
4. Blind self-citations to third person; confirm none were dropped
5. Verify every reference lists all authors (HPCA reject trigger otherwise)
```

## Output format

```text
[Coverage] mechanism families cited / families that exist
[Lineage quality] deltas stated / paragraphs
[Missing ancestor risk] <named prior work not yet cited, or none>
[Blinding] self-cites third-person? bibliography intact? (Y/N)
[Author-list check] every reference lists all authors? (Y/N)
[Top gaps] <ordered>
```

Reopen the current CFP for the preprint policy and the all-authors rule before
finalizing — both are per-edition.
