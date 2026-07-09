---
name: ipsn-topic-selection
description: Use when deciding whether a sensing/embedded project is an IPSN Information-Processing (IP) contribution or a Sensor Platforms, Tools and Design Methods (SPOTS) contribution, and whether it should go to the IPSN lineage (now the merged SenSys at CPS-IoT Week), a CPS-IoT Week neighbor (RTAS/ICCPS/HSCC), MobiSys/MobiCom, INFOCOM, or a signal-processing journal.
---

# IPSN Topic Selection

Decide two things before drafting: **which track** and **which venue**. IPSN — the ACM/IEEE
International Conference on Information Processing in Sensor Networks — split its research papers into
the **Information Processing (IP) track** and the **Sensor Platforms, Tools and Design Methods
(SPOTS) track**, and it lived inside **CPS-IoT Week**. As of 2026-07-09 IPSN no longer runs
standalone — it merged into **SenSys (Embedded AI and Sensing Systems)** — but the IP-vs-SPOTS
instinct still decides how your paper is read and where its evidence bar sits, so keep it.

## First decision: IP track or SPOTS track

This is the choice with no sibling analogue. Get it wrong and your platform paper is judged by
theory reviewers, or your estimator is judged by hardware reviewers.

| Signal in your project | Track | Why |
|---|---|---|
| The core is an algorithm, estimator, inference, or learning method for sensed data | **IP** | Information processing is the contribution; energy/error/bits are the currency |
| Localization, tracking, sensor fusion, compressive sensing, on-device/TinyML inference | **IP** | These are IP-track staples; the platform is a vehicle, not the point |
| The core is a new device, mote, radio front-end, or embedded-software/tool advance | **SPOTS** | Sensor Platforms, Tools and Design Methods is its named home |
| A real deployment whose lesson is about building/operating the system | **SPOTS** (often) | Yield, synchronization, robustness, and design methods dominate |
| A dataset/measurement study of a sensing modality | Either — decide by whether the *method* or the *platform/measurement* is new | The track is chosen by where the novelty lives |

Rule of thumb from IPSN's own wording: **analysis and processing of collected data → IP;
hardware/software platforms and tools used to collect it → SPOTS.** A paper with both a new
estimator and a new board picks the track matching its *primary* claim and treats the other as
support.

## Second decision: is this the IPSN lineage at all?

IPSN rewards work where **information processing meets physical sensing**. A pure ML result with a
sensing dataset, or a pure networking result, is respected and then rerouted.

| Your project's center of gravity | Better home | Why |
|---|---|---|
| Sensing algorithm/inference/localization with a real-hardware or energy consequence | **IPSN lineage → SenSys** (IP track) | The information-processing-meets-sensing core |
| A sensor platform, tool, or deployment with measured design trade-offs | **IPSN lineage → SenSys** (SPOTS track) | The platform/tools core |
| Hard real-time scheduling or timing guarantees | **RTAS** | CPS-IoT Week neighbor; real-time systems is its center |
| Hybrid/control-theoretic CPS, verification, or autonomy | **HSCC / ICCPS** | CPS-IoT Week neighbors; control and hybrid systems |
| Mobile/wearable/smartphone sensing systems, human-in-the-loop | **MobiSys / MobiCom / UbiComp** | Mobile-computing communities, different reviewer pool |
| Wireless protocol/throughput/network-measurement result | **INFOCOM / NSDI / MobiCom** | Networking venues |
| A deep estimation/signal-processing result with no systems payoff | **IEEE TSP / SPAWC / a SP journal** | Signal-processing home; IPSN wants the sensing consequence |

## The merger reality (do not skip)

IPSN's last standalone edition was **IPSN 2024** (23rd, Hong Kong). From 2025 it merged with SenSys
and IoTDI; the live venue is **SenSys — Embedded AI and Sensing Systems**, still at CPS-IoT Week.
Practical consequences:

- "Submit to IPSN" now means **submit to SenSys** with an IP-track or SPOTS-track *style* of
  contribution. Confirm on the current SenSys call whether it keeps an explicit track split or folds
  it into one technical track with categories (待核实).
- Do not send authors to an archived `ipsn.acm.org/2026` — no such standalone conference exists.

## The model-swap and platform-swap tests

- **Model-swap test (IP track):** if your paper leans on a specific learner/model, ask whether the
  sensing lesson survives swapping it. If not, the model is the contribution and an ML venue fits
  better; if yes, it is an IP-track sensing result.
- **Platform-swap test (SPOTS track):** would your platform/tool contribution still matter on a
  different application? If it only helps your one demo, it is an application paper, not a SPOTS
  contribution.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient. An estimator with a bound but no real-sensor evaluation is a
theory note; a board with a datasheet but no measured power/robustness story is an engineering
report; a deployment with no ground truth is an anecdote. IPSN wants the information-processing claim
*and* the physical measurement that makes it real.

## Cheap reconnaissance before committing

```text
[Scope]   scan recent IPSN (dblp, ACM DL/IEEE Xplore) and the latest SenSys program for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = mismatch or reroute
[Track]   is your novelty in the method (IP) or the platform/tools/deployment (SPOTS)?
[Citations] is your bibliography majority sensing venues (IPSN/SenSys/MobiCom/INFOCOM + SP)?
          -> majority pure-ML or pure-networking => reviewers read you as a visitor; reframe first
[Calendar] the live target is the next SenSys edition at CPS-IoT Week -> confirm its deadline
```

## Decision procedure

```text
[Who acts] who changes behavior if the claim holds? sensor-system builders / deployers / SP researchers?
[Claim type] estimator/inference (IP) / platform/tool/deployment (SPOTS)
[Track] IP vs SPOTS, chosen by where the primary novelty lives
[Venue] IPSN-lineage (SenSys) / RTAS / HSCC-ICCPS / MobiSys-MobiCom / INFOCOM / SP journal
[Verdict] track + venue, with a one-line reason and the live successor deadline to confirm
```

Run this before the writing skills; a wrong track or venue wastes every later step. When the verdict
is the IPSN lineage, continue with `ipsn-workflow` for the CPS-IoT Week calendar and
`ipsn-writing-style` for the paper shape.
