---
name: ccs-workflow
description: Use when planning an ACM CCS project timeline across the two HotCRP review cycles, from venue fit through abstract registration, full-paper upload, rebuttal, notification, revision, artifact evaluation, ACM camera-ready, and in-person presentation, with backward-planning offsets and the security big-four deadline-hopping calendar.
---

# CCS Workflow

Use this as the project-management skill for a CCS submission. CCS is a conference, not a
journal: it has no editor-in-chief. Since 2026 ACM publishes the proceedings open access, so
authors outside ACM Open institutions pay an APC (2026: USD 250 ACM/SIG members, 350
non-members). The rotating leadership is the per-edition General Chairs and Program Chairs
(CCS 2026: General Chairs Georgios Smaragdakis and Kaitai Liang; Program Chairs Véronique
Cortier and Zhiqiang Lin, confirmed 2026-11-24 on the organizing-committee page).
Replace every date below with the current cycle's HotCRP deadlines and work backward.

## The dual-deadline cycle

CCS runs two review cycles per year into one conference. A paper enters one cycle only; work
rejected in the first cycle may not be resubmitted (even revised) to the second cycle of the
same year. Pick the cycle from readiness, not hope — a thin first-cycle submission burns the
year at this venue.

- CCS 2026 (The Hague, Netherlands, Nov 15-19, 2026) Cycle A: abstract registration Jan 7,
  full paper Jan 14, early reject Feb 20, rebuttal Mar 17-20, notification Apr 9,
  minor-revision approval Jun 5, camera-ready Aug 9, 2026.
- CCS 2026 Cycle B: abstract registration Apr 22, full paper Apr 29, online artifacts May 2,
  early reject Jun 12, rebuttal Jun 29-Jul 1, notification Jul 17, minor-revision approval
  Sep 4, camera-ready Sep 13, 2026.
- CCS 2026 has met. CCS 2027 is announced for Atlanta, USA, October 11-15, 2027, but its CFP
  was not out on 2026-11-24; treat the 2026 dates as a template and read the 2027 CFP when
  posted.

## Milestones

- Venue fit: confirm the contribution is a broad security result for the SIGSAC PC.
- Evidence lock: freeze threat model, attack/defense implementation, adaptive evaluation,
  measurement validation, and the ethics/disclosure posture.
- Abstract registration: mandatory definitive title, abstract, track, and track justification
  in HotCRP before the registration deadline; no paper without a registered abstract.
- Full-paper deadline: upload the anonymized 12-page ACM sigconf PDF plus appendices
  (including the mandatory Open Science appendix), with every author's ORCID on HotCRP and
  anonymous artifact URLs live within 3 days.
- Rebuttal window: respond to reviews in the short author-response period.
- Notification: accept, minor revision (revise within the cycle), or reject.
- Artifact evaluation: submit artifacts after acceptance for ACM badges if you opt in.
- Camera-ready and registration: ACM proceedings version, then in-person presentation.

## Backward plan from the full-paper deadline

| Weeks out (heuristic) | Attack-plus-defense milestone |
|---|---|
| 10+ | Threat model frozen, attack primitive working end to end |
| 8 | Defense implemented; adaptive attacker designed against it |
| 6 | Measurement or evaluation runs complete, environment logged |
| 4 | Ethics and responsible-disclosure section drafted, disclosure initiated |
| 3 | Full draft in ACM sigconf two-column format |
| 2 | Internal red-team read by an adversarial-minded colleague |
| 1 | Anonymity sweep, artifact-availability statement, appendix assembly |
| 0 | Abstract registered, then full paper in HotCRP |

Anchor every offset to the current cycle, never to a past calendar.

## Big-four deadline-hopping

CCS, IEEE S&P, USENIX Security, and NDSS run rolling multi-cycle deadlines, so a paper
rejected in one can often be reworked into the next open venue within weeks. Keep a live map:
a CCS Cycle A reject in April can target USENIX Security or the next NDSS cycle rather than
waiting a year. Never resubmit unchanged — reviewers rotate across all four venues.

## Coordination notes

- Assign one owner for the ethics/disclosure section and another for the anonymity sweep;
  shared ownership is how both slip.
- Archive the exact submitted PDF and appendices, since rebuttal replies must quote them.

## Output format

```text
[Current stage] idea / building / writing / abstract / submission / rebuttal / accepted / artifact
[Cycle] A / B and next official deadline (date + source, or unknown)
[Critical path] <three tasks that determine readiness>
[Risk register] <threat-model / anonymity / ethics / evidence / artifact / presentation>
[Owner map] <task -> person or role>
```
