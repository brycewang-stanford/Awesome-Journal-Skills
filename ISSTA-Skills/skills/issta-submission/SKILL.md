---
name: issta-submission
description: Use when auditing an ISSTA submission for HotCRP readiness, the 18-page (excluding references) limit, ACM sigconf plus review and anonymous formatting, double-anonymous integrity, the January deadline, artifact intent, track choice among research/experience/replicability, and desk-reject triggers before the phase-one upload.
---

# ISSTA Submission

Use this for an ISSTA research-paper submission audit. Reopen the current Research Papers call,
the important-dates page, the ACM `sigconf` template, and the HotCRP site before giving
deadline-ready advice — ISSTA's submission model changes between editions and is the first thing
to re-verify.

## Submission audit

- Confirm the target is the ISSTA **research** track, not a co-located workshop, the Doctoral
  Symposium, or a sibling venue. ISSTA 2026 also invited Experience Papers and Replicability
  Studies — pick the track that matches the contribution's evidence, not its topic alone.
- Build the HotCRP record early: title, abstract, authors, conflicts, and topic tags. Register the
  paper before the deadline even if the PDF is still moving; a late HotCRP creation cannot be
  undone.
- Apply the ACM `sigconf` template with the `review` (line numbers) and `anonymous` options. Do not
  shrink margins, fonts, or spacing to fit — format tampering is a named desk-reject trigger.
- Fit the 18-page limit that excludes references only. In 2026 every section, figure, table, and
  appendix counted against the 18; there is no separate unlimited appendix, so decision-critical
  content lives in the body or in the artifact, not in overflow pages.
- Enforce double-anonymous review: no author names or affiliations, third-person self-citations,
  anonymized or withheld repository links, and no identifying PDF metadata.
- Decide the artifact plan now. The artifact-evaluation track is separate and later, but the paper
  should already promise what it will archive, and the review-time copy must be anonymous.

## Blocking risks

- Late HotCRP registration or PDF upload against the phase-one deadline.
- Over the 18-page limit, or `sigconf` format modified.
- Identity leak in text, self-citation phrasing, repository link, or PDF metadata.
- Wrong track (a replicability study filed as a research paper, or vice versa).
- Evaluation too thin to survive the soundness and evaluation criteria — a review-stage loss even
  when nothing is technically desk-rejectable.

## Desk-reject and triage table

| Trigger | Severity at ISSTA | Repair window |
|---|---|---|
| Over 18 pages (excluding references) | Desk reject | None after the deadline |
| `sigconf` format tampering | Desk reject | None |
| Author identity leak in PDF or metadata | Desk reject | None |
| Missing `review`/`anonymous` options | Chair flag | Only before the deadline |
| Evaluation without real subjects or a baseline | Review-stage loss | Fixable only before submission |

## Final-week sequence for a testing/analysis paper

1. Freeze the technique's scope and threat model; reviewers grade claims against the scope you set.
2. Regenerate every results table from logged runs so the PDF and the artifact cannot diverge.
3. Pin subjects and benchmark versions (Defects4J revision, subject SHAs) in the paper and artifact.
4. Run the anonymity sweep: PDF metadata, `\author` block, acknowledgements, repository owner strings.
5. Confirm the HotCRP abstract matches the PDF abstract and the topic tags match the reviewer pool.

## Format anchors

- ISSTA uses ACM `sigconf`, a two-column layout; wide code listings, algorithm blocks, and
  multi-column result tables overflow easily, so compress or use full-width spans early rather than
  on deadline night.
- The 18-page figure describes the 2026 cycle; older editions used 10 pages plus 2 for references.
  Treat every number as provisional and reopen the current call before relying on it.

## Output format

```text
[ISSTA readiness] Ready / Needs fixes / Not ready
[Track] research / experience / replicability
[Blocking checks] <HotCRP/page/format/anonymity/artifact-intent>
[Evaluation risk] <one soundness or evaluation gap>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before the phase-one deadline>
```
