---
name: mobisys-submission
description: Use when auditing a MobiSys submission for HotCRP readiness — the paper-registration prerequisite, the single December UTC deadline, the 12-page double-column body including figures and tables, double-blind anonymity including device and trace giveaways, desk-reject triggers, and final-week submission sequencing.
---

# MobiSys Submission

Use this for a MobiSys paper submission audit. Reopen the current Call for Papers, the
`mobisys<yy>.hotcrp.com/deadlines` page, and the ACM template before giving deadline-ready
advice.

## Submission audit

- Confirm the target is the MobiSys main conference, not a workshop, poster, or demo track.
- Complete **paper registration** (title, abstract, authors, conflicts) before the
  registration cutoff that *precedes* the paper deadline — missing it forfeits the upload.
- Apply the current ACM double-column template without margin, font, or spacing hacks. MobiSys
  2026 capped the body at **12 single-spaced numbered pages including figures and tables**;
  references and appendices sit outside the cap.
- Enforce double-blind anonymity in the paper, appendix, supplement, demo media, code, file
  names, and metadata — including device serial numbers, account handles in screenshots,
  internal codenames, and repository owners in trace paths.
- Confirm concurrent-submission and prior-publication status; do not have the same work under
  review at another archival venue when the CFP forbids it.
- Verify the submission is on the correct per-edition HotCRP site and that the upload matches
  the registered abstract.

## Blocking risks

- Missing paper registration, or a late upload against the single December UTC cutoff.
- Overlength body, or figures/tables that push past 12 pages (they count).
- Identity leak in the PDF, supplement, demo media, screenshots, or trace paths.
- Simulation-only evidence where on-device measurement is expected (`mobisys-experiments`).
- Dual submission to another archival venue.

## Desk-reject and triage table

| Trigger | Severity at MobiSys | Repair window |
|---|---|---|
| Overlength body (figures counted) | Desk reject | None after the deadline |
| Template tampering | Desk reject or chair flag | None |
| Identity leak in PDF, media, or trace paths | Desk reject | None |
| Missing paper registration | Cannot submit | Only before the registration cutoff |
| Undefined energy boundary / single-device result | Review-stage damage | Fixable only before the deadline |

## Final-week sequence for an on-device systems paper

1. Freeze the system and regenerate every figure from logged device runs so the PDF and
   artifact cannot diverge.
2. Run the anonymity sweep including screenshots, demo media, and trace-path device strings.
3. Confirm the 12-page body still holds after figure placement; move overflow to the appendix.
4. Strip PDF metadata, notebook authorship fields, and repository owner strings.
5. Confirm the HotCRP abstract matches the PDF abstract, then upload before the UTC cutoff —
   there is no second deadline this cycle.

## Format anchors

- MobiSys uses a two-column ACM layout; wide device tables and multi-panel latency/energy
  plots that fit a one-column draft routinely overflow, so compress early rather than on
  deadline night.
- The page count and rules above describe the 2026 cycle; treat every number as provisional and
  recheck the current CFP before relying on it.

## Output format

```text
[MobiSys readiness] Ready / Needs fixes / Not ready
[Blocking checks] <registration/deadline/page/anonymity/evidence/dual-submission>
[On-device-evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
