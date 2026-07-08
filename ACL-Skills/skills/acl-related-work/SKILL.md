---
name: acl-related-work
description: Use when positioning an ACL submission against the NLP literature, covering ACL Anthology citation practice, arXiv-versus-published version citation, concurrent LLM-era preprints, prior-cycle ARR resubmission overlap, anonymity-preserving self-citation, and the fast-moving baseline problem in computational linguistics.
---

# ACL Related Work

Use this to audit positioning and citation hygiene. NLP moves fast enough that
related-work sections age between ARR cycles; the section must prove the
authors know the field *as of this cycle*, not as of the project's start.

## The Anthology-first rule

- When a paper exists in the ACL Anthology (or another archival venue), cite
  that version, not its arXiv preprint — Anthology entries are the community's
  citation of record and carry stable BibTeX.
- The Anthology is fully open access (post-2016 materials under CC BY 4.0),
  so "couldn't access the published version" is never a defense here.
- For findings-tier work, cite it as Findings of ACL/EMNLP — it is archival
  and reviewers treat miscrediting it as sloppiness.

## Freshness pressure unique to this field

- Expect at least one reviewer to name a baseline or dataset from the last
  two conference rounds. Sweep ACL, EMNLP, NAACL, EACL, TACL, and CL for the
  nearest neighbors published since your project began.
- LLM-era concurrency is the norm: assume 2-4 similar preprints exist. Cite
  the ones findable at submission, contrast on technique rather than date,
  and avoid priority wars that reviewers cannot adjudicate.
- If a newer model release makes your comparison set look dated mid-cycle,
  address it in the author response and plan the upgrade for camera-ready or
  resubmission — silence reads as unawareness.

## Positioning moves that work at ACL

| Contribution type | The contrast reviewers want spelled out |
|---|---|
| Method | Nearest prior method + the mechanism-level difference, not just scores |
| Resource | Existing datasets' coverage gaps: languages, domains, phenomena, license |
| Analysis / evaluation | What prior evaluations measured incorrectly or could not see |
| Metric | Failure cases of the incumbent metric, with correlation evidence |
| Theme-track paper | How the work answers the year's theme question (ACL 2026: explainability) |

One paragraph of typed contrast per lane beats an undifferentiated citation
inventory; ACL's compressed format cannot afford taxonomy for its own sake.

## Self-citation and resubmission overlap

- Cite your own prior work in third person ("Building on Smith (2024)...")
  so anonymity survives; heavy reliance on one group's unpublished thread is
  itself an anonymity leak.
- If this is an ARR resubmission, the revision note — not the related-work
  section — is where you discuss the previous version; the paper itself
  should read cleanly to a fresh reviewer.
- Workshop and non-archival versions (most \*ACL workshops are archival —
  check!) must be declared under the dual-submission policy rather than
  quietly extended.

## Preprint-era eligibility judgment calls

- Your own arXiv preprint of this submission is allowed (no anonymity period
  since January 2024), but the declared preprint status must match reality.
- A competing preprint that appeared after your ARR submission date is
  concurrent work: cite it in camera-ready, note the timing, contrast honestly.
- Do not cite an inaccessible or anonymized document as supporting evidence —
  ARR forbids leaning on materials reviewers cannot read.

## Two-pass audit procedure

```text
Pass 1 (coverage): for each claim of novelty, list the 3 nearest works
  from Anthology search + recent cycles; verify each is cited and
  contrasted, not just listed.
Pass 2 (hygiene): for each bib entry, check venue-of-record vs arXiv,
  Findings attribution, third-person self-citation, and that no cited
  item is reviewer-inaccessible.
```

## Where to actually search, in order

1. ACL Anthology full-text/venue search — the canonical record for every
   \*ACL main conference, Findings volume, TACL, CL, and most workshops.
2. The most recent two conference rounds' accepted-paper lists (each
   edition's site publishes them) — the freshness sweep reviewers run.
3. Semantic Scholar / Google Scholar citation graphs walked *forward* from
   your three nearest neighbors — who already built on them?
4. arXiv cs.CL for the concurrent-preprint scan, dated against your cycle's
   submission deadline so "concurrent" is defensible.
5. Leaderboards and dataset pages for your benchmarks — the SOTA row often
   names an uncited system.

## Related-work paragraph shape that survives compression

For each literature lane, three sentences: (1) what the lane established,
with its two or three best citations; (2) the specific gap or assumption it
left; (3) how this paper differs mechanically. Delete any sentence that
neither cites nor contrasts. In a short paper, the whole section may be one
such paragraph plus contrasts woven into the introduction — that is normal
and reviewers at ACL expect it.

## Red flags reviewers name explicitly

- "The authors seem unaware of X" — the fatal version of staleness; one
  missed obvious neighbor outweighs fifty dutiful citations.
- Citing a paper for a claim it does not make (checked more often than
  authors expect, since reviewers know their own subfield's papers).
- A wall of "recently, LLMs have..." citations with no load-bearing role.
- Comparing against numbers from a cited paper's arXiv v1 that changed in
  the published version.

## Output format

```text
[Positioning verdict] sharp / inventory-like / stale / overlapping
[Nearest neighbors] <3 works -> stated distinction each>
[Freshness risks] <recent baselines or datasets unaddressed>
[Citation hygiene] <arXiv-vs-Anthology, Findings credit, self-citation voice>
[Overlap declarations] <resubmission / workshop / preprint items to declare>
```
