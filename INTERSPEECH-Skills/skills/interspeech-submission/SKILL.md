---
name: interspeech-submission
description: Use when auditing an INTERSPEECH submission before the paper deadline — the strict 4-page-plus-2 format (8 + 2 for Long Papers), double-anonymous rules and current preprint policy, the two-first-author-papers cap, scientific-area and metadata choices, the post-deadline paper-update window, dual-submission policy, and the desk-reject triggers (format, AI-written papers, non-existing references) specific to ISCA's flagship.
---

# INTERSPEECH Submission

Run this audit against the live author pages (Interspeech 2027: interspeech2027.org →
Calls → Main Call; the paper kit and submission page were "available soon" on
2026-11-24), not against memory. Interspeech
re-issues its paper kit every cycle, and the format police here are unusually strict
because the whole review pipeline assumes a uniform 4-page object.

## The format contract

The regular Interspeech 2027 paper is **4 pages of content in two columns, plus 2
additional pages restricted to references and acknowledgments** (2026 also put the
generative-AI disclosure there; 2025 allowed only one extra page). Nothing else goes
on pages 5–6. Consequences worth internalizing:

- There is no appendix escape hatch. Whatever reviewers must see lives in the 4 pages.
- Figures compete directly with argument; every plot must earn its column-inches.
- The Long Paper track (introduced in 2026, continued in 2027: 8 pages + 2, targeted
  acceptance below 30%) has its own rules — and the same work may not be submitted
  as both a long and a regular paper (rejected without review).
- Each author may submit **at most two papers as first author** (2027).
- Use the official paper kit (LaTeX template on the conference site/Overleaf) with
  fonts, margins, and the PDF checker untouched. Interspeech validates PDFs
  mechanically at upload.

## Anonymity: what changed

Interspeech runs double-anonymous review. In 2025 the policy included an **anonymity
period** (no non-anonymized posting from one month before the deadline until
decisions); **Interspeech 2026 dropped it** — preprints were allowed, ideally with a
note that the paper is under review at Interspeech, as long as the submission itself
revealed nothing. The 2027 preprint rule was not yet published on 2026-11-24; check
the submission policy before posting. Audit for:

- Author names, affiliations, grant numbers, and lab-identifying acknowledgments
  (acknowledgments generally wait for camera-ready).
- Demo and repository links that resolve to identifiable accounts — speech papers
  leak identity through audio-sample pages more than through text.
- Self-citation phrasing ("our previous system [3]") and dataset names that only one
  lab could hold.
- PDF metadata and embedded fonts carrying usernames.

## The paper-update window (Interspeech's oddest mechanic)

Interspeech allows the PDF to be **revised for a short window after the submission
deadline** — in 2027, submissions close 9 February and paper updates are accepted
until 16 February (2026: 25 February → 4 March). In 2026 only the PDF, media files,
title and abstract could be updated; topics and authors were frozen. Plan for it deliberately:

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

- Pages 5–6 containing anything beyond references/acknowledgments (and, in 2026, the
  AI-use disclosure).
- A paper "entirely developed or written by AI" or citing a non-existing reference —
  explicit 2027 desk-reject triggers; resolve every reference against a real record.
- The same work submitted as both a long and a regular paper.
- Template tampering (margin, font, or line-spacing tricks) caught by the PDF check.
- Identity leakage anywhere in the PDF or linked material.
- Posting a de-anonymized preprint where the current cycle forbids it (2025 did; 2026
  did not; 2027 not yet stated).
- Missing mandatory metadata fields or an invalid PDF at the CMT cutoff.

## Final 72 hours, in order

1. Rebuild the PDF from a clean clone; confirm the kit's checker passes.
2. Anonymity sweep: text, links, metadata, audio-demo pages, repo history.
3. Freeze metadata early on CMT — the portal slows near the cutoff.
4. Upload, download what CMT stored, and read *that* file end to end.
5. Diary the paper-update close date for the sanctioned typo pass.

## Portal field audit (CMT in 2025–2026; confirm the 2027 portal), one by one

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

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue interspeech-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Output format

```text
[Submission verdict] ready / fixable / not ready
[Format] 4 + 2 (or 8 + 2 long) compliance, template integrity, PDF checker result, first-author cap
[Anonymity] text / links / metadata / demo-page findings
[Metadata] area, abstract match, author list, dual-submission answers
[Update-window plan] <what will be checked before the update close>
[Blockers] <ordered list>
```

## Currency note

The Interspeech 2027 anchor dates — portal opens 19 January, deadline 9 February,
update close 16 February 2027, all for the São Paulo edition — were read directly on
the official call on 2026-11-24 (see `resources/official-source-map.md`); the 2026
Sydney dates were 17 January / 25 February / 4 March. Every one of them is
cycle-specific, and the 2027 paper kit is still to be published.
