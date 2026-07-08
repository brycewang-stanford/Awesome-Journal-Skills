---
name: rss-submission
description: Use when auditing an RSS (Robotics: Science and Systems) submission for OpenReview readiness — the abstract/paper/supplement deadline cascade, the 8-page-excluding-references ceiling, double-blind compliance, PDF self-containment, the no-links-until-camera-ready rule, and dual-submission exposure.
---

# RSS Submission

Final-gate audit for an RSS submission. Every rule below was verified for the 2026
cycle (CFP + review-process page, checked 2026-07-08); reopen the live CFP before
enforcing any of it on a later cycle.

## The three-deadline cascade

RSS 2026 staged submission across three AoE cutoffs one week apart:

| Gate | 2026 date | What locks |
|---|---|---|
| Abstract | January 23 | Title, abstract, authors, OpenReview record exists |
| Full paper | January 30 | The reviewed PDF — main file, PDF only |
| Supplementary | February 6 | Media/code/appendix archive (`rss-supplementary`) |

Treat the abstract gate as real: no record by January 23 meant no paper submission.
The supplement gate is *later* than the paper — a sequencing gift ML-venue habits
squander by trying to finish everything for the paper date.

## Format audit

- **Page ceiling, not target:** at most 8 pages excluding references, and the CFP
  states reviewers look favorably on papers that are *not* unnecessarily long. Padding
  to the limit is a negative signal at this venue, unlike most.
- **Self-containment rule:** the main PDF must contain everything needed for an expert
  to verify the central claims. Appendices, proofs, and data listings go to the
  supplement — but if a reviewer must open the supplement to believe the claim, the
  paper fails the rule.
- **No external links:** project pages, hosted videos, and repos are welcome only in
  the camera-ready. In the submission they are at best ignored and at worst an
  anonymity breach.

## Double-blind sweep

RSS 2026 review was double-blind. Sweep in this order, because robotics leaks
differently from ML:

1. **Footage and figures** — lab walls, robot decals, institutional colors, staff in
   frame. Robotics papers de-anonymize through pixels more often than through prose.
2. **Platform genealogy** — "our previously published gripper [12]" narrows authorship
   to one lab; rewrite as third-person hardware description.
3. **Metadata** — PDF author fields, video container tags, archive paths containing
   usernames.
4. **Prose** — acknowledgements, grant numbers, dataset names unique to one group.

## Eligibility and overlap

- Declare and resolve dual-submission exposure: the same work under review at ICRA,
  IROS, CoRL, or a journal is a standard robotics failure pattern given the packed
  calendar (`rss-workflow`).
- arXiv preprints: handle per the current cycle's wording — do not assume either
  permission or prohibition (待核实 each year).
- There is no separate demo-paper category in 2026; do not submit a demo write-up
  expecting a lighter track.

## OpenReview record audit

The 2026 venue group lived at `roboticsfoundation.org/RSS/2026/Conference`. Field
errors are self-inflicted desk risks; check each against the PDF:

- Title and abstract match the PDF character-for-character (search indexing and AC
  assignment both read the form, not the file).
- Author list complete *in the form* even though the PDF is anonymous — conflicts
  and reviewer assignment run off form metadata.
- Every author's OpenReview profile has current affiliation and conflict domains;
  a stale profile silently corrupts conflict detection.
- Subject areas chosen for the AC you want: they route the paper to its jury.
- The supplement upload slot is a separate object with its own February deadline —
  verify it attached to the right paper ID.

## Severity ladder

| Finding | Severity | Window to repair |
|---|---|---|
| Missed abstract gate | Fatal for the cycle | None |
| Main text over 8 pages excl. references | Desk risk | Until the paper gate |
| External link in submitted PDF | Anonymity/desk risk | Until the paper gate |
| Lab-identifiable footage in supplement | Anonymity breach | Until the supplement gate |
| Claim provable only via supplement | Review-stage damage | Restructure before paper gate |
| Undeclared sibling-venue overlap | Integrity finding | Withdraw one before review |

## Last-72-hours sequence

1. Freeze the claims sentence and re-derive the title/abstract from it.
2. Rebuild the PDF from clean sources; check author metadata is empty.
3. Run the anonymity sweep above on paper *and* supplement together.
4. Verify every figure is legible at print scale — trial-count tables especially.
5. Enter OpenReview fields; confirm the abstract text matches the PDF verbatim.
6. Submit the paper with hours of margin; AoE is generous but robot demos are not the
   thing to be finishing at 11pm on deadline day.

## Notes that save a cycle

- The abstract-gate week is a real strategic asset: title, abstract, and subject
  areas can be refined against the actual claim during the paper week, but the
  *scope* they promise should not swing wildly — ACs see both versions.
- Reference pages are excluded from the 8-page count in 2026; do not compress
  citations to save body space, and do not smuggle content into reference-page
  footnotes either.
- Templates and any style-file requirements were not verifiable through the
  gateway at check time (待核实): download whatever the live CFP links and diff
  your preamble against it rather than reusing last year's class file.
- If the robot produced new decisive results after January 30: they cannot enter
  the reviewed record. Bank them for the rebuttal *only* as clarification, or for
  the journal extension — not as smuggled supplement additions.

## Output format

```text
[Submission verdict] ready / needs fixes / not ready
[Gate status] abstract <done/pending> | paper <done/pending> | supplement <done/pending>
[Format risks] <pages / self-containment / links / template>
[Anonymity findings] <footage / genealogy / metadata / prose>
[Overlap exposure] <none / declared / unresolved>
[Fix order] <ranked list before the next gate>
```
