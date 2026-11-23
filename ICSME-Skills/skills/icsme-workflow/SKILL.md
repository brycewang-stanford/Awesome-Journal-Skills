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
Program Co-Chairs (ICSME 2027: General Co-Chairs Gias Uddin and Song Wang, Program Co-Chairs Shiva
Nejati and Lei Ma, checked 2026-11-23); re-check the organizing-committee page rather than carrying
names forward. ICSME 2027 is the **43rd** edition in **Toronto, Canada** (York University),
**7-11 September 2027**; SCAM and VISSOFT papers share its artifact track.

## Milestones

- **Venue and track fit:** confirm ICSME over ICSE/FSE/SANER/MSR and pick the track — research,
  Journal-First, Registered Reports, Benchmark & Dataset, NIER, tool-demo, or industry (`icsme-topic-selection`).
- **Evidence lock:** freeze research questions, subject systems and their change history, baselines,
  statistics, threats, and the artifact contents.
- **Abstract registration:** submit real title, abstract, authors, and topics by the earlier
  abstract deadline (ICSME 2027: 19 Feb 2027).
- **Paper submission:** upload the anonymized PDF and data-availability statement (ICSME 2027:
  26 Feb 2027).
- **Early-decision cut:** at the response period's start, some papers are already Accept or Reject;
  the rest are "Response Recommended" (ICSME 2027 early decisions: 26 Apr 2027;
  response period 27-30 Apr 2027).
- **Author response:** if invited, answer the PC's specific questions with existing evidence.
- **Notification:** final accept/reject (ICSME 2027: 25 May 2027); archive reviews and the response.
  Camera-ready is due 25 Jun 2027.
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
- **A replication or negative result** had a dedicated home in **RENE** through 2026, but RENE is
  not in the ICSME 2027 track list. In 2027 submit it to the research track, which evaluates
  replicability explicitly, framed as a replication rather than a novelty claim — or pre-register it
  via Registered Reports; a data or benchmark contribution fits the new Benchmark & Dataset Track.

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
[Track] research / journal-first / registered report / benchmark-dataset / NIER / tool-demo / industry
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / anonymity / evidence / threats / artifact / presentation>
[Owner map] <task -> person or role>
```
