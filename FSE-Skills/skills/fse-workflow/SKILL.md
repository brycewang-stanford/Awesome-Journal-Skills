---
name: fse-workflow
description: Use when planning an ESEC/FSE project timeline from venue fit through paper registration, submission, the journal-style Major Revision round, artifact evaluation, PACMSE camera-ready, and presentation, with backward-planning offsets for an empirical-SE paper and honest handling of the single-annual-deadline cycle and cycle-hopping.
---

# FSE Workflow

Use this as the project-management skill for an FSE submission. Replace every date with the
current official timetable and work backwards from the HotCRP registration cutoff — which precedes
the paper deadline. FSE publishes in **PACMSE**, so plan for a possible **Major Revision** round
inside the review year, not just an accept/reject.

FSE is a conference whose papers are journal articles: it has **no standing editor-in-chief** and
**no article-processing charge**. Rotating leadership is the per-edition General and Program/Review
Co-Chairs (FSE 2026 General Chairs: Shin Hwei Tan and Foutse Khomh, verified 2026-07-09), and the
cost model is registration, not APCs — PACMSE is open access. Chairs rotate yearly; re-check the
organizing-committee page rather than carrying a name forward.

## Milestones

- **Venue fit:** confirm FSE over ICSE/ASE/ISSTA and confirm the paper is ready this cycle
  (`fse-topic-selection`).
- **Evidence lock:** freeze research questions, subject systems, baselines, statistics, threats,
  and the artifact contents.
- **Registration:** submit real title, abstract, authors, topics, and conflicts by the earlier
  registration deadline (FSE 2026: 4 Sep 2025).
- **Submission:** upload the anonymized PDF and Data Availability statement (FSE 2026: 11 Sep 2025;
  FSE 2027: 2 Oct 2026).
- **Reviews:** triage each comment by criterion (significance, soundness, evidence, threats,
  clarity, open-science).
- **Major Revision (if issued):** execute a tracked-change revision plus an anonymous, point-by-
  point response, re-read by the original reviewers.
- **Decision:** archive reviews, response, and every submitted version.
- **Acceptance:** prepare the PACMSE camera-ready, pursue ACM artifact badges on the artifact
  track's own deadline, register, and present.

## Backward plan from the submission deadline

| Weeks out (heuristic) | Empirical-SE milestone |
|---|---|
| 10+ | Research questions fixed; subject systems and baselines chosen |
| 8 | Data collection / experiments complete; provenance and seeds logged |
| 6 | Analysis done; effect sizes and tests computed; threats drafted alongside results |
| 4 | Full draft in the ACM template; artifact assembled and anonymized |
| 3 | Internal mock review by an SE-empiricist reader |
| 2 | Threats hardened, related-work delta sharpened, page budget met |
| 1 | Anonymity sweep on PDF and artifact; Data Availability statement final |
| 0 | Registration by its earlier cutoff, then paper + artifact link on HotCRP |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle's calendar.

## Cycle-hopping: the honest calendar reality

FSE runs (currently) a single annual research deadline. As of 2026-07-09, FSE 2026 is in progress
in Montreal, so the live next target is **FSE 2027** (Shenzhen; deadline 2 Oct 2026). Two planning
consequences:

- **A Major Revision that cannot be finished in the window** may, depending on the year's rules,
  be resubmittable to the next FSE cycle rather than lost — but this is exactly the kind of policy
  that changes per edition, so verify it before relying on it.
- **Missing the annual deadline costs roughly a year** at FSE; a sibling flagship (ICSE/ASE/ISSTA)
  or an SE journal may have a nearer date — factor that into routing rather than idling.

## Failure modes by stage

- **Evidence still moving at week 4** forces last-minute analysis nobody has audited — the classic
  soundness reject in the making.
- **Leaving the anonymized artifact to the final week** is how a data-availability link or a
  lab-named tool leaks identity under heavy anonymity.
- **Skipping the mock review** forfeits the one chance to hear "your baseline is unfair" from a
  friend instead of a reviewer.
- **Treating a Major Revision as a formality** and under-budgeting the revision window turns a
  winnable R&R into a reject.

## Coordination notes

- Assign one owner for the Data Availability / artifact and another for the anonymity sweep; shared
  ownership is how both slip.
- Archive the exact submitted PDF, artifact, and (later) response letter — the revision round must
  quote them precisely and stay anonymous.

## Output format

```text
[Current stage] idea / evidence / writing / registration / submitted / major revision / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / anonymity / evidence / threats / artifact / presentation>
[Owner map] <task -> person or role>
```
