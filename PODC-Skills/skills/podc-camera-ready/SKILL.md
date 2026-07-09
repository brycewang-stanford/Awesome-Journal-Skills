---
name: podc-camera-ready
description: Use when preparing an accepted ACM PODC paper for the proceedings — de-anonymizing after lightweight double-blind, compressing to the 10-page two-column ACM proceedings format without losing the proof map, completing ACM rights/eRights metadata and CCS concepts, and posting the synchronized full version with all proofs to arXiv.
---

# PODC Camera-Ready

Use this after acceptance, toward the camera-ready deadline (PODC 2026: **20 May 2026**). Two shifts
define the work: the paper moves from **anonymous to attributed**, and from the **unbounded
submission** to the **≤10-page two-column ACM proceedings** version — while the *proofs* migrate to
the arXiv full version. Do both without breaking the proof map a reader follows.

## De-anonymize systematically

Reverse every lightweight-double-blind measure from `podc-submission`:

```text
[Authors]        add real author names, affiliations, and emails to the ACM template header
[Self-citations] restore first-person where natural ("we extend [12]" is fine now)
[Acknowledgements] add funding, grants, and thanks removed for review
[Links]          point to the (now public) arXiv full version, code, or author pages
[Metadata]       set the PDF author/title metadata to the real values
```

Do not accidentally leave a submission-era "[anonymized]" placeholder in the text or bibliography.

## Compress to the proceedings format without losing the proofs

The published regular paper is **≤10 pages** in two-column `acmart` proceedings format — far shorter
than the full-version submission. The compression strategy is *placement*, not deletion:

- Keep in the proceedings: the model box, all theorem statements, the delta over prior bounds, and
  the **proof ideas / key lemmas** — the reader must still see *why* each result holds.
- Move to the **arXiv full version**: complete proofs, routine cases, auxiliary constructions,
  extended related work, optional simulation detail.
- Add an explicit pointer: "Full proofs appear in the full version [arXiv:...]." A proceedings paper
  that just says "proof omitted" with no reachable full version fails the reproducibility contract
  (`podc-reproducibility`).
- Verify every cross-reference ("by Lemma 4.2") resolves in whichever document it points to.

## Post and synchronize the arXiv full version

- Post the **full version with all proofs** to arXiv (the de-anonymized version now that review is
  over).
- The arXiv full version and the proceedings paper must state **identical theorems and constants**;
  only proof detail differs. A theorem tightened in one and not the other is a correctness-record
  bug.
- If a reviewer's comment led you to fix a proof, ensure the fix is in *both* the camera-ready and
  the arXiv version.
- The community reads arXiv for the proofs the 10 pages cannot hold, so treat it as the archival
  scientific record, not an afterthought.

## Complete ACM production metadata

- **ACM rights / eRights:** complete the copyright/licensing form ACM sends after acceptance; paste
  the returned rights block (copyright line, conference string, DOI) into the template exactly.
- **CCS concepts and keywords:** add the ACM Computing Classification System concepts and author
  keywords the template requires.
- **Title/author consistency:** the names and title in the PDF, the rights form, and HotCRP must
  match.
- **Reference hygiene:** for canonical results, cite the correct venue — a JACM article vs. a PODC
  edition vs. a DISC paper (see the exemplars library's omissions list); camera-ready is when
  reviewers stop catching these for you.

## Pre-upload checklist

```text
[ ] Real authors/affiliations/emails in; no leftover "[anonymized]" strings
[ ] <=10 two-column proceedings pages; model box + theorems + deltas + proof ideas all retained
[ ] Full proofs in the arXiv full version, reachable by an explicit pointer and exact cross-refs
[ ] arXiv full version and proceedings paper state identical theorems/constants
[ ] ACM rights block, DOI, conference string, CCS concepts, keywords all in place
[ ] Any post-review proof fix propagated to both documents
[ ] Registration for the conference arranged (one author must present in person)
```

## Common failures

- **Proofs deleted, not relocated** — the proceedings paper loses the proof map and no full version
  holds the deleted proofs.
- **Body and arXiv disagree** on a theorem after a post-review fix.
- **Leftover anonymization** — placeholder strings or third-person self-citations left in.
- **Missing rights block / CCS concepts** — an ACM production reject at the last moment.
- **Wrong-venue citations** — a canonical result attributed to PODC when it is a journal or DISC
  result.

## Output format

```text
[De-anonymization] authors/acks/self-cites/links/metadata all restored; no placeholders left?
[Compression] <=10 proceedings pages; proof ideas retained; full proofs relocated not deleted?
[arXiv sync] full version posted; identical theorems/constants; explicit pointer + exact cross-refs?
[ACM metadata] rights block / DOI / conference string / CCS / keywords complete?
[Presentation] in-person registration arranged?
[Fix queue] <remaining production and sync items before the camera-ready deadline>
```
