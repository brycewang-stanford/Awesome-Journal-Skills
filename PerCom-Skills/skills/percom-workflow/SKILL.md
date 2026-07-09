---
name: percom-workflow
description: Use when planning an IEEE PerCom project timeline from venue fit through paper registration, the September submission, the early-rejection gate, the bounded rebuttal, the IEEE Xplore camera-ready, and in-person presentation, with backward-planning offsets for a human-subjects sensing paper and honest handling of the single-annual-deadline cycle.
---

# PerCom Workflow

Use this as the project-management skill for a PerCom submission. Replace every date with the
current official timetable and work backwards from the HotCRP **registration** cutoff — which
precedes the paper deadline by about a week. PerCom runs a **single annual deadline** feeding one
review round with a **bounded rebuttal** and an **early-rejection gate**; there is no journal-style
revision, so plan for the paper to be complete at submission.

PerCom is an IEEE Computer Society conference: it has **no standing editor-in-chief** and **no APC**
in the open-access sense. Rotating leadership is the per-edition General and TPC (Program) Co-Chairs
(PerCom 2027 full roster **待核实** as of 2026-07-09), and the cost model is IEEE registration with
at least one author presenting **in person**.

## Milestones

- **Venue fit:** confirm PerCom over ACM UbiComp/IMWUT, MobiCom, SenSys, or IPSN, and confirm the
  paper is ready this cycle (`percom-topic-selection`).
- **Data collection lock:** IRB/consent secured, subjects recruited, sensing protocol frozen — the
  long pole for a human-subjects paper.
- **Evidence lock:** freeze claims, cross-subject splits, baselines, metrics, limitations, and the
  dataset contents. Nothing can be added in the rebuttal.
- **Registration:** submit real title, abstract, authors, topics by the earlier registration
  deadline (PerCom 2027: 4 Sep 2026).
- **Submission:** upload the anonymized PDF and the open-data plan (PerCom 2027: 11 Sep 2026 AoE).
- **Early-rejection gate:** notification (~20 Nov 2026) either early-rejects or invites a rebuttal.
- **Rebuttal (if invited):** answer explicit reviewer questions from existing evidence, anonymously
  (~26 Nov 2026).
- **Decision:** accept/reject (~18 Dec 2026); archive reviews, rebuttal, and every submitted
  version.
- **Acceptance:** prepare the IEEE Xplore camera-ready (PDF eXpress, eCopyright, ORCID), deposit the
  de-identified dataset, register, and present in person.

## Backward plan from the submission deadline

| Weeks out (heuristic) | Human-subjects sensing milestone |
|---|---|
| 16+ | IRB/consent approved; recruitment and data collection begun (the long pole) |
| 12 | Data collection complete; labeling protocol run with annotator agreement |
| 10 | Claims fixed; cross-subject (LOSO) splits and baselines chosen |
| 8 | Experiments complete; F1/event-level results with per-subject spread computed |
| 6 | Analysis done; limitations drafted alongside results; dataset de-identified |
| 4 | Full draft in the IEEEtran 9+1 template; artifact assembled and anonymized |
| 3 | Internal mock review by a ubicomp reader ("is this within-subject only?") |
| 2 | Limitations hardened, related-work delta sharpened, 9-page budget met |
| 1 | Double-blind sweep on PDF and dataset link; open-data plan final |
| 0 | Registration by its earlier cutoff, then paper + dataset link on HotCRP |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle's calendar. Note the **16-week IRB/collection pole**: human-subjects data
cannot be rushed in the final month.

## Cycle reality: one shot per year, gated early

PerCom runs one annual research deadline. As of 2026-07-09, PerCom 2026 (Pisa) has concluded, so the
live next target is **PerCom 2027** (Goa; deadline 11 Sep 2026). Two planning consequences:

- **There is no revision cycle.** A paper that is not complete — especially one lacking cross-subject
  evidence — cannot be rescued in the rebuttal; it will likely be early-rejected. Finish the
  evaluation before submitting.
- **Missing the annual deadline costs roughly a year** at PerCom; ACM **IMWUT** has rolling
  quarterly deadlines and a revise cycle, so a paper that needs another round of experiments may be
  better routed there than held for a year — factor that into routing rather than idling.

## Failure modes by stage

- **IRB or recruitment slipping** pushes data collection into the final month and forces a
  within-subject-only evaluation — the classic PerCom early-reject in the making.
- **Discovering at week 3 that the split was within-subject** is fatal with no time to recollect;
  design the LOSO split at week 10.
- **Leaving the anonymized dataset to the final week** is how a testbed name, a re-identifying photo,
  or an owner string leaks identity under double-blind review.
- **Skipping the mock review** forfeits the one chance to hear "your evaluation is within-subject"
  from a friend instead of a reviewer — and there is no revision to fix it.
- **Treating the rebuttal as a revision** and planning to "add the experiment then" — the process
  neither expects nor permits it.

## Coordination notes

- Assign one owner for IRB/consent and the dataset, and another for the double-blind anonymity
  sweep; shared ownership is how both slip.
- Archive the exact submitted PDF, dataset, and (later) rebuttal — the discussion must quote them
  precisely and stay anonymous.

## Output format

```text
[Current stage] idea / IRB+collection / evidence / writing / registration / submitted / rebuttal / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness -- IRB/collection is usually one>
[Risk register] <IRB / cross-subject evaluation / 9-page budget / anonymity / dataset / presentation>
[Owner map] <task -> person or role>
```
