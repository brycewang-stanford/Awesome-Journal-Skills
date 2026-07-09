---
name: issta-related-work
description: Use when positioning an ISSTA submission against the testing and analysis literature, covering the sibling venues (ICSE, FSE, ASE, ICST, PLDI, CAV), delta-first framing against the nearest technique, double-anonymous self-citation, distinguishing the closest tool baseline, and avoiding the venue-confusion of citing a paper to the wrong conference.
---

# ISSTA Related Work

Use this to audit novelty and positioning. ISSTA reviewers know the testing/analysis literature
well, so the job is to name the nearest technique and state the delta, not to survey the field.
Reopen the current call for any dual-submission and prior-publication rules before advising authors.

## Positioning checks

- Separate a genuine technique or measurement contribution from an engineering improvement: a new
  bug class found, a new property analyzed, a new evaluation of a technique class, or a
  sharper-but-cheaper analysis.
- Name the single nearest technique and state the delta in one sentence: what it could not do, what
  yours does, and at what cost. Reviewers look for the closest competitor first.
- Sweep the right venues. Testing and analysis work is spread across ISSTA and its siblings; missing
  a paper because it was at FSE or CAV rather than ISSTA reads as not knowing the field.
- Keep self-citations double-anonymous: cite your own prior tool in the third person and do not link
  to an identity-revealing repository.
- Declare any overlap with a prior workshop or preprint version, and do not put duplicate archival
  work under review.

## Literature lanes for testing and analysis

| Lane | Typical venues | What ISSTA reviewers check |
|---|---|---|
| Software-engineering flagships | ICSE, ESEC/FSE, ASE | Whether the closest SE technique is compared or distinguished |
| Testing-specific venues | ISSTA, ICST, ISSRE | Whether the direct predecessor and its benchmark are used |
| Programming languages / verification | PLDI, POPL, OOPSLA, CAV, TACAS | Whether the analysis's formal neighbours are acknowledged |
| Security testing | S&P, CCS, USENIX Security, NDSS | Whether fuzzing/analysis-for-security work is credited where relevant |

A bibliography that cites only ISSTA papers signals to a reviewer that nearer work at FSE, ASE, or
CAV was missed — a recognizable weakness that benchmark strength does not repair.

## Delta-first positioning vignette

Suppose the paper proposes a directed fuzzer for a specific bug class. Its nearest neighbours: a
coverage-guided fuzzer at a security venue with no directedness, a directed symbolic-execution tool
at a PL venue that does not scale, and a prior ISSTA fuzzer for a different bug class. The novelty
sentence names all three deltas — directedness the coverage fuzzer lacked, scale the symbolic tool
lacked, and a different, harder target than the prior ISSTA fuzzer — rather than a generic "we
improve on prior fuzzers."

## Venue-attribution discipline

- Before citing a paper as ISSTA, confirm the venue on dblp or the ACM DL; many canonical
  testing/analysis papers (KLEE at OSDI, EvoSuite at ESEC/FSE, Randoop at ICSE) are *not* ISSTA, and
  mis-attributing them signals carelessness.
- For a tool everyone knows by name, cite the paper that introduced it, at its actual venue, not the
  venue where you first encountered it.
- When unsure whether a venue is archival for dual-submission purposes, declare the overlap in the
  submission form rather than guessing.

## Output format

```text
[Novelty] clear / incremental / at-risk
[Closest lanes] <SE / testing / PL-verification / security>
[Nearest 3 works] <work -> venue -> delta>
[Venue-attribution check] <any paper cited to the wrong conference?>
[Archival-overlap risk] none / issues
[Novelty sentence] <ISSTA-ready delta statement>
```
