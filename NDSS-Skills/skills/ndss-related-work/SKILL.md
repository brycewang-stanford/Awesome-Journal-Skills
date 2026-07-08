---
name: ndss-related-work
description: Use when positioning an NDSS submission against prior literature — sweeping the security big four plus the specialist venues, writing precise deltas, verifying every citation against NDSS's open proceedings and dblp, and keeping self-reference double-blind.
---

# NDSS Related Work

At NDSS the related-work section is a security argument: it establishes that the adversary,
the precondition, or the defense you present is genuinely new *at the layer you claim*. The
worked example in this pack turns on exactly that move — separating delegation-layer
staleness from well-known record-layer takeover. Aim your section at the same standard:
distinguish by mechanism, not by adjective.

## Where NDSS reviewers expect you to have looked

| Tier | Venues / sources | What you owe them |
| --- | --- | --- |
| Flagships | NDSS, IEEE S&P, USENIX Security, CCS (last ~3-4 years) | The nearest neighbors and your delta against each |
| Specialists | PETS, IMC, ACSAC, RAID, EuroS&P, WOOT | Depth in your sub-area; measurement lineage |
| Co-located ecosystem | NDSS workshops (e.g., BAR, USEC, MADWeb — 2026 list verified) | Early-stage versions of your idea often surface here first |
| Non-academic record | CVEs, vendor advisories, IETF drafts/RFCs, incident writeups | Whether practitioners already know your "novel" issue |
| Preprints | arXiv (cs.CR), IACR ePrint | Concurrent work; cite, date, and differentiate |

The non-academic tier is the one academic drafts skip and security reviewers do not: an
attack already described in a vendor advisory or an RFC's security considerations is not
novel because no PDF said it.

## Writing the delta

A delta sentence names the prior work's mechanism, states yours, and locates the difference
in adversary, layer, precondition, or guarantee:

- Weak: "Unlike prior work, our approach is more practical."
- Strong: "[X] detects dangling A/CNAME records from the registrant's side; our scanner
  operates provider-side at delegation-release time, which covers the zone-takeover case
  record-level hygiene cannot see."

One such sentence per genuine neighbor beats a paragraph of citation carpet. Group the rest
by theme with one honest line each.

## Verification discipline

NDSS's own proceedings are free — there is no paywall excuse for citing from memory.

```text
For each citation:
  1. Resolve it: ndss-symposium.org proceedings page, dblp (conf/ndss,
     conf/uss, conf/sp, conf/ccs...), or DOI (NDSS uses 10.14722/NDSS.*).
  2. Confirm venue + year + author list against the resolved record —
     security classics are chronically misattributed across the big four
     (see the checked list in ../../resources/exemplars/library.md).
  3. Confirm the claim you attribute actually appears in the paper, not
     in its folklore.
  4. Cite the archival version over the preprint when both exist.
```

If a fetch is blocked (this pack's own source map documents 403s from `ndss-symposium.org`
and `dblp.org` in some environments), verify through search renderings of the exact URL and
note what could not be confirmed instead of guessing.

## Double-blind self-citation

The 2027 CFP mandates anonymized submissions. For your own prior work:

- Cite it in third person, exactly like a stranger's paper. Never "we extend our system".
- If the overlap is so tight that third person is implausible, address the relationship in
  the text ("this work differs from [X] in ...") — reviewers may guess authorship, but the
  text must not confirm it.
- Anonymize infrastructure fingerprints too: internal tool names, testbed hostnames, and
  dataset labels that only one lab could produce.

## Handling concurrent work

The dual-cycle structure means near-identical ideas surface months apart. If a concurrent
paper appears (arXiv, another venue's acceptance list) before your deadline: cite it, date
both efforts, and write the technical difference plainly. Reviewers at this venue routinely
review for the sibling conferences in the same season — assume they have seen the
concurrent paper even if you had not.

## Placement and length

Related work at NDSS commonly closes the paper (before conclusion) when the introduction
already carries the sharp deltas, or follows the introduction when the field is crowded and
positioning is the contribution's fulcrum. Either way it draws from the same 13-page
budget: roughly one page, spent on differentiation rather than survey. A tutorial of the
area belongs in background, and only if the design needs it.

## Output format

```text
[Neighbor map] nearest 3-6 works, each with a mechanism-level delta sentence
[Coverage gaps] tiers with no citations (flagship / specialist / advisory / preprint)
[Attribution audit] citations verified N/M; failures listed with resolution
[Anonymity leaks] first-person self-references or fingerprinting labels found
[Concurrent-work plan] known concurrent efforts + how the text handles them
```
