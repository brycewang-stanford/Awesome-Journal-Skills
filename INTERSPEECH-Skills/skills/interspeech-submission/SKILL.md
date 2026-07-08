---
name: interspeech-submission
description: Use when auditing an INTERSPEECH submission before the CMT deadline — the strict 4-page-plus-references format, double-anonymous rules and the pre-deadline anonymity period, scientific-area and metadata choices, the post-deadline paper-update window, dual-submission policy, and the desk-reject triggers specific to ISCA's flagship.
---

# INTERSPEECH Submission

Run this audit against the live author pages (Interspeech 2026 kept them under
interspeech2026.org → Calls / Author Resources), not against memory. Interspeech
re-issues its paper kit every cycle, and the format police here are unusually strict
because the whole review pipeline assumes a uniform 4-page object.

## The format contract

The regular Interspeech paper is **4 pages of content in two columns, plus one
additional page restricted to references and acknowledgments** (2025 wording;
confirm the 2026 kit). Nothing else goes on page 5. Consequences worth internalizing:

- There is no appendix escape hatch. Whatever reviewers must see lives in the 4 pages.
- Figures compete directly with argument; every plot must earn its column-inches.
- The Long Paper track (introduced for 2026; reported 8 pages + 2 reference pages)
  has its own rules — do not mix the two templates.
- Use the official paper kit (LaTeX template on the conference site/Overleaf) with
  fonts, margins, and the PDF checker untouched. Interspeech validates PDFs
  mechanically at upload.

## Anonymity: stricter than you remember

Interspeech runs double-anonymous review, and since 2025 the policy has included an
**anonymity period that starts one month before the submission deadline** and lasts
until decisions: no non-anonymized version of the work may be posted online (arXiv
included) in that window. Audit for:

- Author names, affiliations, grant numbers, and lab-identifying acknowledgments
  (acknowledgments generally wait for camera-ready).
- Demo and repository links that resolve to identifiable accounts — speech papers
  leak identity through audio-sample pages more than through text.
- Self-citation phrasing ("our previous system [3]") and dataset names that only one
  lab could hold.
- PDF metadata and embedded fonts carrying usernames.

## The paper-update window (Interspeech's oddest mechanic)

Interspeech allows the PDF to be **revised for a short window after the submission
deadline** — in 2026, submissions closed 25 February and paper updates were accepted
until 4 March. Title, authors, abstract, and area typically freeze at the deadline;
only the PDF may change. Plan for it deliberately:

| Days after deadline | Sanctioned use of the update window |
|---|---|
| 0–2 | Full-team proofread of the actually-submitted PDF |
| 2–5 | Fix typos, broken references, figure glitches, overfull boxes |
| 5–close | One final upload; verify the portal shows the new checksum/version |

Do not treat the window as a deadline extension for experiments — reviewers may be
bidding on the metadata you froze, and wholesale content swaps invite chair scrutiny.

## Metadata and area selection

- The scientific area you pick routes the paper to its reviewer pool; choose for the
  claim, not the method (see `interspeech-topic-selection`).
- Abstract in CMT must match the PDF abstract; it is what reviewers bid on.
- Declare all authors at submission — post-deadline author changes are restricted.
- Answer dual-submission questions honestly: the same work may not sit under review
  at another conference or journal simultaneously.

## Desk-reject triggers observed at this venue

- Fifth page containing anything beyond references/acknowledgments.
- Template tampering (margin, font, or line-spacing tricks) caught by the PDF check.
- Identity leakage anywhere in the PDF or linked material.
- Posting a de-anonymized preprint inside the anonymity period.
- Missing mandatory metadata fields or an invalid PDF at the CMT cutoff.

## Final 72 hours, in order

1. Rebuild the PDF from a clean clone; confirm the kit's checker passes.
2. Anonymity sweep: text, links, metadata, audio-demo pages, repo history.
3. Freeze metadata early on CMT — the portal slows near the cutoff.
4. Upload, download what CMT stored, and read *that* file end to end.
5. Diary the paper-update close date for the sanctioned typo pass.

## CMT field audit, one by one

Portal fields outlive the PDF — the Archive entry, review assignment, and
program are generated from them:

- **Title**: identical to the PDF, punctuation included; it freezes at the
  deadline in most cycles.
- **Abstract**: paste from the PDF source, not from an old draft; reviewers bid
  on this text.
- **Authors + order**: complete and final; adding an author later needs chair
  intervention. Verify each co-author's CMT account email — collisions create
  duplicate identities that break conflict detection.
- **Scientific area (+ any secondary)**: the routing decision from
  `interspeech-topic-selection`; do not delegate it to whoever uploads.
- **Conflicts/domains**: list every co-author's institutional domains; missed
  conflicts surface as review-integrity problems months later.
- **Policy checkboxes** (dual submission, ethics, anonymity attestations): read
  the year's wording — the sentences change, and a false attestation is a
  desk-reject with memory.

## If something goes wrong at the wire

- Portal outage or personal emergency at the cutoff: email the Technical Program
  Chairs immediately with evidence; discretion exists but shrinks by the hour.
- Wrong file uploaded and the deadline passed: the paper-update window is your
  sanctioned repair channel for the PDF — but metadata errors need a chair email.
- Discovered identity leak after the deadline: update the PDF within the window
  and document the fix; do not silently hope.

## Output format

```text
[Submission verdict] ready / fixable / not ready
[Format] 4+1 compliance, template integrity, PDF checker result
[Anonymity] text / links / metadata / demo-page findings
[Metadata] area, abstract match, author list, dual-submission answers
[Update-window plan] <what will be checked before the update close>
[Blockers] <ordered list>
```

## Currency note

The 2026 anchor dates — portal open 17 January, deadline 25 February, update close
4 March, all for the Sydney edition — were checked 2026-07-08 via official-page
renderings (see `resources/official-source-map.md`). Every one of them is
cycle-specific; the 2027 São Paulo cycle will publish its own kit and calendar.
