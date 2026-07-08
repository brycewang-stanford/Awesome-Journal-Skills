---
name: ccs-related-work
description: Use when positioning an ACM CCS submission against the security big-four and specialist literature, including arXiv preprints, prior CCS/S&P/USENIX/NDSS papers, concurrent disclosures, CVE and advisory records, and the attack-and-defense lineage that a SIGSAC program committee expects to see credited.
---

# CCS Related Work

Use this to audit novelty and eligibility. Reopen the current CFP for dual-submission,
anonymity, and prior-publication rules before advising authors.

## Positioning checks

- Separate a genuine security advance from an engineering increment: a new attack class, a
  broken assumption, a defense with a new guarantee, or a measurement that overturns received
  wisdom.
- Compare against all four top venues, not just CCS. A SIGSAC PC expects the nearest attack
  or defense from S&P, USENIX Security, and NDSS to be cited and distinguished.
- Credit the practitioner and disclosure record: relevant CVEs, vendor advisories, and public
  exploit write-ups count as prior art at CCS even when they are not peer-reviewed papers.
- Cite arXiv and preprint versions without breaking double-blind review; do not point
  reviewers to identity-revealing pages or your own advisory.
- Explain overlap with any concurrent disclosure and do not submit duplicate archival work.
- Use related work to sharpen the delta: a stronger attacker, a weaker assumption, a lower
  overhead, a wider measurement, or a defense where prior work had only detection.

## Literature-lane table

| Literature lane | Typical sources | What CCS reviewers check |
|---|---|---|
| Security big four | CCS, IEEE S&P, USENIX Security, NDSS proceedings | Whether the nearest attack/defense is compared or explicitly distinguished |
| Specialist venues | PETS/PoPETs, ESORICS, ACSAC, CRYPTO/EUROCRYPT | Whether the sub-community's known results are acknowledged |
| Practitioner record | CVEs, vendor advisories, CTF and exploit write-ups | Whether a known real-world case predates the claimed novelty |

A bibliography citing only academic papers while ignoring a well-known CVE that already
demonstrated the attack is a recognizable CCS reject pattern that no amount of measurement
polish repairs.

## Positioning vignette

Imagine the paper reports a new cache side-channel that recovers keys from a TLS library. Its
nearest neighbors: an S&P paper with a slower channel, a USENIX defense that assumed the
channel was impractical, and a public CVE for a related timing bug. The novelty sentence
should name all three contrasts — a faster channel than the S&P line, a break of the USENIX
paper's practicality assumption, and a distinct root cause from the CVE.

## Concurrent-work judgment calls

- Independently concurrent arXiv or disclosure work: cite neutrally, state the technical
  difference, and avoid priority claims reviewers cannot verify.
- Your own prior workshop or poster version: usually citable and non-archival, but verify
  against the current CFP wording and phrase the citation to preserve double-blind review.
- When unsure whether a co-located CCS workshop counts as archival overlap, declare it in the
  submission form rather than gambling on a chair's reading.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest literatures] <big-four / specialist / practitioner record>
[Nearest 3 works] <work -> distinction>
[Archival-overlap risk] <none / issues>
[Novelty sentence] <CCS-ready contribution contrast>
```
