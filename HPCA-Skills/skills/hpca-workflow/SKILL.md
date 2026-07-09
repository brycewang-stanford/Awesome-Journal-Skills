---
name: hpca-workflow
description: Use when planning an HPCA project timeline from venue fit through the two-step July registration and paper gate, the autumn review wait, the single rebuttal/revision window, notification, IEEE camera-ready, artifact evaluation, and the February/March talk, with backward-planning offsets for a hardware-evaluated paper.
---

# HPCA Workflow

Use this as the project-management skill for an HPCA submission. Replace every date
with the current official timetable and plan backward from the late-July gate.

HPCA is a conference, not a journal: it has no standing editor-in-chief and no
article-processing charge. It is run by the IEEE-CS Technical Committee on Computer
Architecture (TCCA); the rotating leadership is the per-edition General and Program
Chairs (HPCA 2027 program chairs were reported as Aamer Jaleel and Mattan Erez —
待核实), and the cost model is registration fees. Chairs rotate yearly, so re-check
the current organization page rather than carrying a name forward.

## The shape of the HPCA year

HPCA sits in the **winter seat**: a **late-July deadline** feeds an **autumn review**
and a **February/March conference**. It is the last major architecture deadline of
the summer, so a project that misses it waits for MICRO's spring gate or ISCA's
November gate — plan the fallback before you need it.

## Milestones

- **Venue fit:** confirm a measured microarchitectural cost meets a buildable
  mechanism whose behavior is the contribution.
- **Evidence lock:** freeze the mechanism, the simulator/silicon configuration,
  workloads, sampled regions, baselines, and the artifact mirror.
- **Registration step:** submit real title, abstract, authors, topics, and complete
  conflicts about a week before the paper.
- **Paper step:** upload the anonymous IEEE-template PDF and all HotCRP fields.
- **Review wait:** triage reviews for correctness, methodology, novelty, and
  reproducibility concerns as they land.
- **Rebuttal/revision window:** respond and revise in one combined window (recent
  cycles run a single window, not two rounds).
- **Notification → acceptance:** archive reviews, the response, and the submitted
  versions; then IEEE camera-ready, artifact evaluation on the AE HotCRP, and the
  winter talk.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Hardware-evaluated milestone |
|---|---|
| 8+ | Mechanism implemented; fidelity contract (tool, config, workloads) fixed |
| 6 | Baseline sweeps complete; per-workload results, not just means |
| 4 | Real-silicon or validated-simulator numbers logged with machine state |
| 3 | Full draft in the IEEE two-column template |
| 2 | Internal mock review by an architecture-minded reader |
| 1 | Reference author-list check, anonymity sweep, artifact mirror assembled |
| 0 | Registration then paper on HotCRP |

These offsets are planning heuristics — anchor every one to the current official
timetable, never to a previous cycle.

## Failure modes by stage

- Infrastructure still churning at week 4 forces last-minute configuration changes
  no one has validated — the classic HPCA methodology reject in the making.
- Leaving template conversion to the final week surfaces overflow late; two-column
  architecture figures are tighter than a working draft's.
- Skipping the mock review forfeits the only chance to hear "your baseline is
  under-tuned" from a friend rather than a reviewer.
- Building the artifact mirror after the deadline under pressure is how anonymity
  leaks and un-pinned simulators ship.

## Coordination notes

- Assign one named owner for the fidelity contract and another for the anonymity
  sweep; shared ownership is how both slip.
- Archive the exact submitted PDF, the artifact mirror, and the configuration files,
  since rebuttal replies must quote them precisely.

## Output format

```text
[Current stage] idea / evaluation / writing / registration / paper / window / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page/anonymity/instrument/reproducibility/artifact/presentation>
[Fallback venue] <MICRO / ISCA / ASPLOS branch if rejected>
[Owner map] <task -> person or role>
```
