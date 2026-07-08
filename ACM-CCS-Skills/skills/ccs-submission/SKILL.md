---
name: ccs-submission
description: Use when auditing an ACM CCS submission for HotCRP readiness, dual-cycle abstract registration and full-paper deadlines, the 12-page ACM sigconf body, anonymization, the ethics considerations appendix, artifact-availability posture, dual-submission policy, per-cycle submission caps, desk-reject triggers, and final-week sequencing.
---

# CCS Submission

Use this for a CCS paper submission audit. Reopen the current Call for Papers, the cycle's
HotCRP site, the ACM sigconf template, and the ethics policy before giving deadline-ready
advice, because CCS rules and dates are set per cycle.

## Submission audit

- Confirm the target is the main CCS research track, not a workshop, poster, or the SIGSAC
  co-located events.
- Register the abstract in HotCRP before the registration deadline. CCS requires a mandatory
  title, author list, abstract, and topics one week before the full-paper deadline; no
  abstract, no paper. In 2026 registration led the paper deadline by seven days each cycle.
- Apply the unaltered ACM `sigconf` two-column template. CCS 2026 set a 12-page main-text
  limit excluding the bibliography, well-marked appendices, and supplementary material.
  Whitespace and margin tampering is forbidden and is a desk-reject trigger.
- Enforce anonymization: cite your own prior work in the third person, blind references only
  where third-person phrasing is infeasible, and strip identity from text, PDF metadata,
  system names, and repository links.
- Place the ethics considerations content in a dedicated section (in 2026, an appendix after
  the 12-page body and bibliography) whenever the work touches human subjects, user data, or
  real-world vulnerabilities.
- Respect the per-cycle submission cap (2026: at most 7 papers per author per cycle) and the
  one-cycle rule — a first-cycle reject cannot return the same year.
- Confirm the work is not concurrently under review at another archival venue.

## Blocking risks

- Missing abstract registration, or a late abstract or paper upload.
- Overlength main text or an altered `sigconf` template.
- Identity leak in the PDF, metadata, artifact link, or a non-blinded system name.
- Missing ethics considerations section for work that plainly needs one.
- Dual submission to another archival security venue.
- A threat model too vague for reviewers to score the attacker.

## Desk-reject and triage table

| Trigger | Severity at CCS | Repair window |
|---|---|---|
| No registered abstract by the deadline | Cannot submit | None |
| Overlength 12-page body or template tampering | Desk reject | None after the deadline |
| Identity leak in PDF or artifact link | Desk reject | None |
| Ethics section missing for human-subjects/vuln work | Desk reject or major flag | Only before the deadline |
| Vague threat model | Review-stage damage | Fixable in the writing pass |

## Final-week sequence for an attack-plus-defense paper

1. Freeze the threat model and attacker-capability statement; reviewers score against it.
2. Re-run the adaptive-attack evaluation from logged configs so the PDF and artifact agree.
3. Draft the ethics and responsible-disclosure section against what you actually did.
4. Strip PDF metadata, tool authorship strings, and repository owner names from every link.
5. Register the abstract early, then confirm the HotCRP PDF matches the registered abstract.

## Format anchors

- CCS uses a dense two-column `sigconf` layout; wide system diagrams, protocol figures, and
  multi-column result tables that fit a one-column draft overflow, so compress early.
- The page and cap numbers above describe the 2026 cycle; treat every number as provisional
  and recheck the current CFP before relying on it.

## Output format

```text
[CCS readiness] Ready / Needs fixes / Not ready
[Blocking checks] <abstract-reg / page / anonymity / ethics / dual-submission / cap>
[Threat-model risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
