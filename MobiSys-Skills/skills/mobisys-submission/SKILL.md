---
name: mobisys-submission
description: Use when auditing a MobiSys submission for HotCRP readiness — the 100-word abstract-registration prerequisite, the single December AoE deadline (December 4, 2026 for MobiSys 2027), the 12-page double-column body including figures and tables, the complete single-blind author block and conflict declarations, LLM-text and ethics-review declarations, the Emerging Ideas track, desk-reject triggers, and final-week submission sequencing.
---

# MobiSys Submission

Use this for a MobiSys paper submission audit. Reopen the current Call for Papers, the
`mobisys<yy>.hotcrp.com/deadlines` page, and the ACM template before giving deadline-ready
advice. Numbers below are the MobiSys 2027 CFP, re-verified 2026-11-24 by direct fetch.

## MobiSys 2027 clock

| Item | Date |
|---|---|
| Abstract registration | November 27, 2026, 23:59 AoE (HotCRP: Sat Nov 28, 6:59:59 AM EST) |
| Paper submission | December 4, 2026, 23:59 AoE (HotCRP: Sat Dec 5, 6:59:59 AM EST) |
| Early rejection | January 26, 2027 |
| Rebuttal | February 8–12, 2027 |
| Final decision | March 6, 2027 |
| Camera-ready | April 14, 2027 |

No extensions. Portal: `mobisys27.hotcrp.com`.

## Submission audit

- Confirm the target is the MobiSys main conference, not a workshop, poster, or demo track.
- Complete **abstract registration** (meaningful title, an abstract of **at least 100 words**,
  authors, conflicts) before the registration cutoff that *precedes* the paper deadline —
  missing it forfeits the upload, and "TBD"-style placeholders are desk-rejected. All authors
  must be declared by the paper deadline; the list cannot change afterwards.
- Apply the ACM double-column template (`\documentclass[sigconf,10pt]{acmart}`) without margin,
  font, or spacing hacks: **12 single-spaced numbered pages of main content including figures
  and tables**, font ≥10 pt, columns 9.25 x 3.33 in, at most 55 lines per column, US letter;
  references and appendices sit outside the cap, but reviewers need not read the appendix and
  over-length main content is not reviewed.
- **Single-blind review (since 2026):** the manuscript must carry the authors' **names,
  affiliations and contact information**. Do not anonymize — check that the author block is
  complete, correctly spelled, and matches HotCRP. (MobiSys was double-blind from 2017 to
  2025; an anonymized PDF is a leftover from that era.)
- Declare **every** conflict by the CFP's categories (24-month affiliation/co-authorship/
  collaboration windows, advisors, same-group graduates within 48 months, prior exposure to
  the work, family and close personal ties) — reviewers now see your names, so an undeclared
  conflict is visible and a falsified one gets the paper returned unreviewed.
- **LLM text:** any LLM-generated text must be clearly identified in the paper (editing and
  proofreading exempt); never embed hidden text aimed at LLM reviewers.
- **Ethics:** human-subject work, or analysis of non-public human-derived data, must be
  certified as ethics-reviewed (e.g. IRB) during submission; non-compliant papers are rejected.
- **Emerging Ideas track:** prefix the title with "[Emerging Ideas]" and tick the HotCRP
  checkbox if the paper is a bold, early-stage idea rather than a complete system.
- Confirm concurrent-submission and prior-publication status: no overlap with work under
  review elsewhere; a workshop paper counts only if *published* before the submission date and
  substantially extended; arXiv is not prior publication, but a different system name and no
  publicity during review are encouraged. For a previously rejected paper, an optional summary
  of how prior reviews were addressed can be uploaded (reviewers see it after reviewing).
- Verify the submission is on the correct per-edition HotCRP site and that the upload matches
  the registered abstract.

## Blocking risks

- Missing abstract registration, a placeholder abstract, or a late upload against the single
  December AoE cutoff.
- Overlength body, or figures/tables that push past 12 pages (they count).
- Incomplete author block or undeclared conflicts; unidentified LLM-generated text; missing
  ethics certification for human-subject work.
- Simulation-only evidence where on-device measurement is expected (`mobisys-experiments`).
- Dual submission to another archival venue.

## Desk-reject and triage table

| Trigger | Severity at MobiSys | Repair window |
|---|---|---|
| Overlength body (figures counted) | Desk reject | None after the deadline |
| Template tampering | Desk reject or chair flag | None |
| Placeholder registration abstract ("TBD") | Desk reject | Only before the registration cutoff |
| Falsified or hidden conflicts | Returned without reviews | None |
| Missing paper registration | Cannot submit | Only before the registration cutoff |
| Undefined energy boundary / single-device result | Review-stage damage | Fixable only before the deadline |

## Final-week sequence for an on-device systems paper

1. Freeze the system and regenerate every figure from logged device runs so the PDF and
   artifact cannot diverge.
2. Check the author block (names, affiliations, contact emails) and conflicts against HotCRP;
   mark any LLM-generated text; confirm the ethics certification if human subjects are involved.
3. Confirm the 12-page body still holds after figure placement; move overflow to the appendix.
4. Make sure no hidden text or reviewer-directed prompts remain anywhere in the PDF.
5. Confirm the HotCRP abstract matches the PDF abstract, then upload before the AoE cutoff —
   there is no second deadline this cycle.

## Format anchors

- MobiSys uses a two-column ACM layout; wide device tables and multi-panel latency/energy
  plots that fit a one-column draft routinely overflow, so compress early rather than on
  deadline night.
- The page count and rules above describe the MobiSys 2027 cycle; treat every number as
  provisional and recheck the current CFP before relying on it.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue mobisys-skills   # from a clone of the AJS repository
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
[MobiSys readiness] Ready / Needs fixes / Not ready
[Blocking checks] <registration/deadline/page/author block+conflicts/LLM+ethics/evidence/dual-submission>
[On-device-evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
