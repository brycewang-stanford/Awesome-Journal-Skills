---
name: ipsn-workflow
description: Use when planning an IPSN-lineage project timeline from track/venue selection through the CPS-IoT Week deadline, double-blind submission, deployment and hardware logistics, rebuttal, the Best Research Artifact Award, and the dual ACM/IEEE camera-ready — with honest handling of the fact that IPSN merged into SenSys.
---

# IPSN Workflow

Use this as the project-management skill for an IPSN-lineage submission. Replace every date with the
current official timetable and work backwards from the successor (SenSys) deadline at **CPS-IoT
Week**. The single biggest planning fact: **IPSN no longer runs standalone** — it merged into
**SenSys (Embedded AI and Sensing Systems)**, so plan against the current SenSys call, keeping the
IP-vs-SPOTS instinct.

IPSN had **no standing editor-in-chief** and **no APC**; rotating leadership was the per-edition
General Chair(s) and per-track (IP / SPOTS) Program Chairs under CPS-IoT Week, ACM SIGBED, and IEEE.
The cost model is registration; at least one author presents. Re-check the successor's
organizing-committee page rather than carrying a name forward.

## Milestones

- **Venue + track fit:** confirm the IPSN lineage over MobiSys/MobiCom/INFOCOM/RTAS, and pick IP vs
  SPOTS (`ipsn-topic-selection`).
- **Evidence lock:** freeze the testbed, ground-truth reference, baselines, energy/latency
  measurement setup, and the dataset/firmware artifact contents.
- **Deployment window (if applicable):** schedule field time early — a bridge, building, or wildlife
  deployment cannot be redone in the final week and is weather/permit-bound.
- **Registration/abstract:** submit real title, abstract, authors, track, and conflicts by the
  earlier cutoff.
- **Submission:** upload the anonymized PDF and dataset/firmware link on HotCRP.
- **Rebuttal (if offered):** correct misreadings and supply any measured number a reviewer flagged.
- **Decision:** archive reviews, rebuttal, and every submitted version.
- **Acceptance:** prepare the **dual ACM/IEEE** camera-ready, pursue the **Best Research Artifact
  Award** and ACM badges, register, and present.

## Backward plan from the submission deadline

| Weeks out (heuristic) | Sensor-systems milestone |
|---|---|
| 12+ | Track chosen; testbed and ground-truth reference decided; deployment permits/weather scheduled |
| 10 | Hardware/firmware frozen; power-measurement harness built and validated |
| 8 | Data collection / deployment complete; raw traces, energy logs, and calibration archived |
| 6 | Analysis done; accuracy/energy/latency budgets computed; baselines run under equal conditions |
| 4 | Full draft on the ACM template (two-column, ≤12 pp); artifact assembled and anonymized |
| 3 | Internal mock review by a sensor-systems reader; check the IP/SPOTS framing holds |
| 2 | Limits hardened, related-work delta sharpened, page budget met |
| 1 | Double-blind sweep on PDF, board photos, scope screenshots, testbed names, dataset links |
| 0 | Register/track-select by the earlier cutoff, then paper + artifact link on HotCRP |

These offsets are planning heuristics only — anchor every one to the current CPS-IoT Week /
successor Important Dates page.

## The merger and calendar reality

- IPSN's last standalone edition was **IPSN 2024** (Hong Kong). The live target is the next **SenSys**
  edition at CPS-IoT Week; SenSys 2026 (Saint Malo) had a **13 Nov 2025** paper deadline, so the next
  edition's deadline is **待核实** — confirm before planning.
- **Deployment lead time is the hidden critical path.** Unlike a software paper, a sensing paper's
  schedule is bounded by physical access (a bridge closure window, a field season, a hardware
  fabrication run). Missing the deadline often costs a full year *and* a deployment window.

## Failure modes by stage

- **Testbed still moving at week 4** forces last-minute measurement nobody has audited — the classic
  evidence-realism reject.
- **Leaving anonymization to the final week** is how a lab-logo board photo or a named testbed leaks
  identity under double-blind review.
- **Skipping the mock review** forfeits the one chance to hear "your baseline is simulated" or "you
  never report energy" from a friend instead of a reviewer.
- **Treating the rebuttal as decisive** — it is narrow; the measured evidence in the paper carries
  the argument.
- **Assuming IPSN still runs** — check the successor venue before anything else.

## Coordination notes

- Assign one owner for the **artifact/dataset/firmware release** and another for the **double-blind
  sweep** (including hardware imagery); shared ownership is how both slip.
- Archive the exact submitted PDF, artifact, raw traces, and calibration — the rebuttal and
  camera-ready must quote them precisely, and the artifact award needs them.

## Output format

```text
[Current stage] idea / evidence / deployment / writing / submitted / rebuttal / accepted
[Venue + track] successor (SenSys) edition + IP/SPOTS, with the next deadline (or 待核实)
[Critical path] <three tasks that determine readiness — often deployment-bound>
[Risk register] <page budget / anonymity / evidence-realism / energy accounting / artifact / deployment window>
[Owner map] <task -> person or role>
```
