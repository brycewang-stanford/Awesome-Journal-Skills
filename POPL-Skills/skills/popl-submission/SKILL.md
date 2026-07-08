---
name: popl-submission
description: Use when preparing a POPL submission for the single July HotCRP deadline — auditing the 25-pages-of-text acmsmall cap, summary-rejection format rules, full double-blind hygiene for theory papers with public proof repositories, dual-submission exposure, and the final-days upload order before the AoE cutoff.
---

# POPL Submission

Audit against the cycle you are actually entering. The mechanics below come from the
POPL 2027 research-papers call, read 2026-07-08 through search renderings of
`popl27.sigplan.org` (direct fetches were blocked — see
`resources/official-source-map.md`). POPL 2027's cutoff was July 9, 2026, 11:59 PM
AoE, one day after that check: confirm the live dates page before assuming any window
is open.

## The 2027-cycle mechanics

- **One July deadline, no abstract deadline.** POPL 2027 papers were due July 9,
  2026 AoE, uploaded to `popl27.hotcrp.com`. Nothing pre-registers the submission,
  so a paper can materialize on deadline day — and so can your forgotten conflicts
  list. A missed July means the next POPL is a year out (though PACMPL siblings
  offer intermediate deadlines; see `popl-workflow`).
- **25 pages of text, bibliography excluded**, in the PACMPL layout: acmart with the
  `acmsmall` option, single column, 10 pt font on 12 pt line spacing, a 5.478 in by
  7.884 in text block. The call names **summary rejection** as the consequence of a
  shrunken font or widened block, and PACMPL takes no Word files.
- **Full double-blind.** Since POPL 2023 this replaced the older lightweight regime:
  reviewers never see author names, and identities are revealed only after
  conditional-acceptance decisions, only for the papers that made it.

## Where theory papers deanonymize themselves

A semantics or verification paper leaks identity through different channels than an
ML paper: a Rocq/Coq development already public under your group's namespace, a
paper-named logic that only one lab builds on, "in our previous work [7]" phrasing,
and appendix PDFs generated with author metadata intact.

```bash
pdfinfo main.pdf | grep -iE 'author|producer'
pdftotext main.pdf - | grep -niE 'our (previous|earlier) (work|paper)|github|gitlab|zenodo|orcid' | head
tar tzf supplement.tar.gz | grep -E '\.git/|home/[a-z]+/|_CoqProject.*~' | head
```

Cite your own prior papers in the third person, scrub `\author` blocks and grant
lines, and route any proof development through an anonymized mirror rather than the
lab repository.

## Severity table

| Failure | Likely outcome under the 2027 call | Can it be repaired after the deadline? |
|---|---|---|
| Text beyond 25 pages or altered format | Summary rejection | No |
| Word manuscript | Not accepted by PACMPL tooling | No |
| Author-identifying PDF or supplement | Chair action against double-blind policy | No |
| Same result under review elsewhere | Dual-submission violation | No |
| Main theorem stated without its assumptions | Survives triage, dies in review | Only before upload |
| Missing HotCRP conflicts/topics | Assignment errors, wasted expert reviews | Sometimes, at chair discretion |

## Last-72-hours order of operations

1. Freeze definitions and theorem numbering; late renumbering desyncs body, appendix,
   and proof scripts.
2. Rebuild the PDF from a clean clone so no stale lemma statement survives.
3. Run the leak scan above on the paper and every supplementary archive.
4. Fill HotCRP metadata — title, abstract, topics, conflicts — a day early; the form
   is fast, but conflict lists take thought.
5. Upload well before 11:59 PM AoE and re-download your own submission to verify the
   PDF the committee will see.

## Output format

```text
[POPL submission audit] pass / blockers found
[Format] <25-page text count, acmsmall compliance, PDF build>
[Anonymity] <leak-scan findings across paper, appendix, proof archive>
[Policy] <dual submission, prior publication, conflicts>
[Remaining actions] <ordered, with owner and cutoff time in AoE>
```
