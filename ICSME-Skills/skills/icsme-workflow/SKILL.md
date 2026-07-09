---
name: icsme-workflow
description: Use when planning an IEEE ICSME project timeline from venue and track choice through abstract registration, paper submission, the early-decision cut and author-response rebuttal, notification, IEEE Xplore camera-ready, the ROSE-Festival artifact evaluation, and presentation, with backward-planning offsets for a maintenance/evolution paper and honest handling of the single-annual-round calendar.
---

# ICSME Workflow

Use this as the project-management skill for an ICSME submission. Replace every date with the
current official timetable and work backwards from the EasyChair **abstract** cutoff — which
precedes the paper deadline. ICSME runs a **single annual research round** with **no journal-style
Major Revision**: a paper is accepted or rejected in one cycle, so front-load the evidence and plan
the author-response rebuttal, not a revise-and-resubmit.

ICSME is an IEEE conference with **no standing editor-in-chief** and no APC: proceedings go to IEEE
Xplore and the cost model is registration. Rotating leadership is the per-edition General and
Program Co-Chairs (ICSME 2026 committee roster **待核实** on the access date); re-check the
organizing-committee page rather than carrying names forward. ICSME 2026 is the **42nd** edition in
**Benevento, Italy** (University of Sannio), **14-18 September 2026**, co-located with SCAM and
VISSOFT.

## Milestones

- **Venue and track fit:** confirm ICSME over ICSE/FSE/SANER/MSR and pick the track — research,
  Journal-First, Registered Reports, RENE, NIER, tool-demo, or industry (`icsme-topic-selection`).
- **Evidence lock:** freeze research questions, subject systems and their change history, baselines,
  statistics, threats, and the artifact contents.
- **Abstract registration:** submit real title, abstract, authors, and topics by the earlier
  abstract deadline (ICSME 2026: 27 Feb 2026).
- **Paper submission:** upload the anonymized PDF and data-availability statement (ICSME 2026:
  6 Mar 2026).
- **Early-decision cut:** at the response period's start, some papers are already Accept or Reject;
  the rest are "Response Recommended" (ICSME 2026 early decisions: 3 May 2026).
- **Author response:** if invited, answer the PC's specific questions with existing evidence.
- **Notification:** final accept/reject (ICSME 2026: 29 May 2026); archive reviews and the response.
- **Acceptance:** prepare the IEEE Xplore camera-ready, submit to the ROSE-Festival artifact track
  for IEEE badges, register, and present.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Maintenance/evolution milestone |
|---|---|
| 10+ | Research questions fixed; subject systems and their change-history window chosen |
| 8 | Mining / data collection complete; repository SHAs and extraction dates logged |
| 6 | Analysis done; effect sizes and tests computed; threats drafted alongside results |
| 4 | Full draft in IEEEtran conference format; artifact assembled and anonymized |
| 3 | Internal mock review by a maintenance-empiricist reader |
| 2 | Threats hardened, related-work delta sharpened, 10-page budget met |
| 1 | Anonymity sweep on PDF and artifact; data-availability statement final |
| 0 | Abstract registered by its earlier cutoff, then paper + artifact link on EasyChair |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle's calendar.

## The single-round calendar reality

ICSME runs one annual research round; the author-response rebuttal is the *only* mid-cycle lever,
and there is no Major Revision to fall back on. Planning consequences:

- **A rejected paper waits a full year** at ICSME. Before idling, check whether a sibling
  (SANER, ICSE, FSE) has a nearer deadline, or whether the work is better routed to TSE/EMSE and
  returned later via the **Journal-First** track.
- **A not-yet-finished study** may fit **Registered Reports** (protocol reviewed first) rather than
  being rushed into the research track and rejected on thin evidence.
- **A replication or negative result** has a dedicated home in **RENE** — do not force it into the
  research track where novelty framing will hurt it.

## Failure modes by stage

- **Mining still running at week 4** forces last-minute analysis nobody has audited — the classic
  soundness reject for an evolution study.
- **Naming your own subject system or public corpus** breaks double-anonymity when the artifact is
  left to the final week.
- **Skipping the mock review** forfeits the one chance to hear "your baseline maintainer study is
  confounded" from a friend instead of a reviewer.
- **Treating the author response as a debate** wastes the single rebuttal ICSME gives you; answer
  the PC's specific questions with evidence, not argument.

## Coordination notes

- Assign one owner for the data-availability / artifact and another for the anonymity sweep;
  shared ownership is how both slip under double-anonymity.
- Archive the exact submitted PDF and artifact; the response period must quote the paper precisely
  and stay anonymous.
- The ROSE-Festival artifact submission is a separate, post-acceptance deadline shared with SCAM
  and VISSOFT — calendar it apart from the camera-ready.

## Output format

```text
[Current stage] idea / evidence / abstract / submitted / response period / accepted
[Track] research / journal-first / registered report / RENE / NIER / tool-demo / industry
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / anonymity / evidence / threats / artifact / presentation>
[Owner map] <task -> person or role>
```
