---
name: wacv-related-work
description: Use when writing or auditing a WACV related-work section, covering how to position an applications or algorithms contribution against fast-moving vision literature, sibling-venue (CVPR/ICCV/ECCV) and arXiv concurrency, application-domain literature, double-blind self-citation, and verifying that cited "WACV papers" are actually WACV papers.
---

# WACV Related Work

Use this to position a WACV paper so reviewers see the gap it fills, not a wall of
citations. WACV's applications identity adds a shelf most vision venues underweight — the
**domain literature** — and its two-round model means a thin related-work section is a
predictable revision request. Facts are the WACV 2026/2027 cycles as read on 2026-07-09.

## The shelves to cover

| Shelf | What it establishes | Failure if missing |
|---|---|---|
| Vision method lineage | Where your method sits among CV approaches | Reviewer thinks you reinvented a known method |
| Sibling-venue recent work | Awareness of CVPR/ICCV/ECCV state of the art | Looks unaware of the field's frontier |
| arXiv / concurrent work | Honest handling of near-simultaneous results | Accused of ignoring obvious concurrency |
| **Application-domain literature** | That you understand the real problem (agriculture, medical, robotics) | Applications reviewer sees a naive domain model |
| Your own prior work (anonymized) | Continuity without breaking double-blind | Identity leak or apparent self-plagiarism |

The domain shelf is what separates a strong WACV applications paper from a generic method
with a domain sticker: cite the deployment literature that defines the real constraint, not
only the vision papers that share your architecture.

## Positioning, not enumeration

Each cited cluster should end in a **specific** reason it does not already solve your
problem — "these run in daylight and lose low-contrast boundaries below 20 lux," not "prior
work has limitations." For an Applications-track paper, the gap is usually a constraint no
prior system met; for an Algorithms-track paper, it is a mechanism no prior method used.

## Concurrency at arXiv speed

```text
For each closely related recent preprint/paper:
  - Same problem, different method?      → contrast approaches; note it is concurrent.
  - Same method, different problem?       → clarify what your setting adds.
  - Genuinely concurrent (within months)? → cite and distinguish; do not claim it as prior
                                            or ignore it. Reviewers know the arXiv timeline.
```

## Double-blind self-citation

Cite your own prior work in the **third person** ("Prior work [12] showed…"), never "our
previous paper." Keep repository and project-page links out of the submission. A revised
Round 2 paper must stay just as anonymous as the Round 1 version — do not let a revision
reintroduce an identifying citation.

## Verify the venue of every "WACV" citation

A `thecvf.com` open-access URL is only a WACV citation if its path reads `WACV20XX`; many
famous vision papers are CVPR/ICCV/ECCV. Before attributing a paper to WACV, confirm the
open-access path segment or the dblp record — misattributing a sibling-venue paper to WACV
is a credibility cost a careful reviewer will notice.

## Reverify each cycle

- Any related-work or citation-format expectations in the current guidelines.
- The double-blind and external-link rules for the submission version.
- That cited WACV papers match the WACV proceedings, not a sibling venue.

## Output format

```text
[Shelves covered] vision / sibling-venue / concurrent / domain / self — missing: <list>
[Gap statements] each cluster ends in a specific gap: yes/no
[Domain literature] real-problem sources cited: yes/no
[Concurrency] recent preprints cited and distinguished: yes/no
[Anonymity] self-cites third-person, no links: yes/no
[Venue check] all "WACV" cites verified as WACV: yes/no
```
