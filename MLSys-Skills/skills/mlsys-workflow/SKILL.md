---
name: mlsys-workflow
description: Use when planning an MLSys submission cycle end to end, from venue-fit and track choice through evaluation freeze, the October deadline, the four-day January response, notification, camera-ready, the March artifact-evaluation submission, and the May conference, with backward planning built around scarce GPU time and team ownership.
---

# MLSys Workflow

Use this as the project-management skill for a Conference on Machine Learning and Systems
submission. MLSys runs one cycle per year, so a missed gate costs twelve months or a
reroute to another venue. All dates below are the verified 2026-cycle timetable
(access 2026-07-08) — treat them as *shape*, and replace every one with the current
mlsys.org dates page before committing a plan.

MLSys is a conference with rotating per-edition leadership (2026: General Chair Luis
Ceze; Program Chairs Zhihao Jia and Aakanksha Chowdhery) and no APC — proceedings publish
open on proceedings.mlsys.org, and the money side is registration, where accepted-paper
authors get a two-week reserved-ticket window.

## The 2026-cycle shape

| Gate | 2026 anchor | What it demands |
|---|---|---|
| CFP and track choice | Summer 2025 (CFP publicized ~August) | Research vs industrial routing decided |
| Paper + appendix deadline | October 30, 2025 | Frozen evaluation, blinded PDF, separate appendix upload |
| Reviews released | January 12, 2026 | All authors on deck immediately |
| Author response due | January 16, 2026 | Four days — pre-planned, not improvised |
| Notification | January 25-26, 2026 | Branch: camera-ready+AE, or postmortem+reroute |
| Artifact evaluation submission | March 8, 2026 | Badge-ready package + Artifact Appendix |
| AE window | March 8 - April 8, 2026 | One author on call for evaluator questions |
| Conference | May 18-22, 2026 (Bellevue) | Registration inside reserved window, talk, travel |

## Backward plan from the paper deadline

| Weeks out | Systems-paper milestone |
|---|---|
| 12+ | Bottleneck measurement done; mechanism designed; venue/track locked |
| 10 | Baselines installed, version-pinned, tuning protocol agreed |
| 8 | End-to-end prototype produces its first honest comparison |
| 6 | Full experiment matrix launched — GPU allocation is the critical path from here |
| 4 | Ablations and sensitivity sweeps done; figures generated from logs |
| 3 | Complete draft in the official two-column style; internal review by one systems and one ML reader |
| 2 | Evaluation freeze; only reviewer-anticipation runs remain |
| 1 | Anonymity sweep, appendix assembly as separate file, bibliography full-author check |
| 0 | Upload paper + appendix; verify both files from a logged-out view |

The distinctive constraint versus ML-venue planning: the evaluation competes for
**shared hardware**. Reserve cluster time for weeks 6-4 when the matrix runs, and again
for the January response window, where two rebuttal experiments may need machines on
two days' notice.

## Standing team rituals

```text
Weekly (weeks 12->2):
  - experiment-matrix review: rows launched / landed / failed, GPU budget burned
  - claims board: abstract claim -> supporting figure -> status (red/yellow/green)
  - baseline watch: new releases of compared systems since last week?
Once (week 3): mock review — one systems-culture and one ML-culture reader,
  scored on workload realism, baseline fairness, attribution, and tails.
Response-week protocol (pre-agreed in December):
  - who reads reviews hour 0, who owns machines, who drafts, who signs off
```

## Failure modes by stage

- **Week 6 matrix slip**: the sweep launches late, so ablations get cut — and ablation
  absence is precisely what MLSys reviews punish. Cut breadth (hardware variants)
  before cutting attribution (ablations).
- **Baseline rot**: a compared system ships a major release in September; deciding
  whether to re-run everything at week 4 needs a pre-agreed rule ("re-run headline
  comparisons if the release notes claim >10% on our metric").
- **Response-window surprise**: the four-day window found nobody available in January.
  It is on the calendar from the day of submission.
- **Post-acceptance pile-up**: camera-ready, AE package, and conference logistics all
  land in February-March; assign three different owners at notification time.
- **Reroute paralysis** after rejection: the systems-venue calendar (OSDI/SOSP/NSDI/
  ASPLOS/ATC deadlines) should be listed in the postmortem doc *before* the decision
  arrives.

## The reroute decision, prepared in advance

Because the cycle is annual, "revise and resubmit to next MLSys" costs a year. Write
the decision rule before the notification arrives:

| Rejection pattern | Indicated move |
|---|---|
| Workload/baseline objections, mechanism praised | Strengthen evaluation, resubmit to next MLSys — the reviews are a work list |
| "Insufficient novelty, solid engineering" | Industrial track next cycle, or a systems venue that weighs deployment insight |
| "Wrong audience" signals from both cultures | Re-read `mlsys-topic-selection`; the project may be OSDI/ASPLOS/NSDI-shaped |
| Split reviews, one culture convinced | Rewrite for the unconvinced culture; the paper, not the project, missed |

Maintain the alternative-deadline list (OSDI, SOSP, NSDI, ASPLOS, ATC, EuroSys, SC)
with dates in the project doc from week 12, so a January rejection flows into a
concrete February plan instead of a stall.

## Ownership map (minimum viable)

- Evaluation owner: matrix, logs, figure regeneration.
- Baseline owner: versions, tuning parity, release watch.
- Writing owner: 10-page budget, style-kit compliance, claims board.
- Compliance owner: anonymity, appendix upload, OpenReview fields, deadlines.
- (Post-acceptance) AE owner: package, badges, evaluator on-call.

One person may hold two hats; no hat may be unassigned. Industrial-track submissions
add a sixth hat that academic teams forget: the internal-approval owner, who clears
company names, trace releases, and benchmark numbers with legal/PR — a process whose
latency routinely exceeds the writing itself, so it starts at week 10, not week 1.

## Cycle-volatility warning

Every date above, the track structure, the response-window length, and the AE mechanics
are 2026 facts. The 2027 CFP was not yet visible at access time (待核实, all of it) —
rebuild this table from mlsys.org before planning a real cycle.

## Output format

```text
[Current stage] fit / building / evaluating / writing / submitted / response / decided / AE
[Next official gate] <date + source URL>
[Critical path] <three tasks, with GPU-time dependencies flagged>
[Claims board] <claim -> figure -> status>
[Ownership] <evaluation/baseline/writing/compliance/AE -> person>
[Risk register] <matrix slip / baseline rot / response availability / logistics pile-up>
```
