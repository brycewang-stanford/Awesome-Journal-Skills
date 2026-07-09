---
name: percom-topic-selection
description: Use when deciding whether a pervasive-computing project belongs at IEEE PerCom or should be routed to ACM UbiComp/IMWUT, MobiCom, MobiSys, SenSys, or IPSN, and when distinguishing PerCom's human-centric ubicomp focus from networked-sensor-systems venues by contribution shape, the human-centricity test, and the IEEE-conference vs. IMWUT-journal model.
---

# PerCom Topic Selection

Decide the venue before drafting. PerCom — the IEEE International Conference on Pervasive Computing
and Communications — is IEEE's flagship for **human-centric ubiquitous computing**: activity
recognition, context-awareness, wearable and mobile sensing, and smart environments. Its papers are
IEEE Xplore proceedings read for a **pervasive-computing contribution grounded in real human use**.
A technically strong paper whose real lesson is about network protocols, low-power hardware, or a
pure ML model is respected and then rejected as out of scope.

## The routing question that matters most

PerCom overlaps most with **ACM UbiComp/IMWUT** in *topic* — both cover HAR, wearables, and smart
spaces — so the decisive question is rarely "is this ubicomp?" but **"which model and calendar fits
this paper now?"** UbiComp presents papers published in the **IMWUT journal** on **rolling
quarterly deadlines** with a revise cycle; PerCom is an **IEEE conference** with a **single annual
deadline**, a **bounded rebuttal**, and an in-person-presentation requirement. A strong ubicomp
paper is publishable at either — choose by the publication model you want and the nearer honest
deadline.

## Neighbor-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Human-centric ubicomp (HAR, context, wearables, smart space), ready now, PerCom deadline nearer | **IEEE PerCom** | IEEE conference flagship; annual deadline + rebuttal |
| Same topic, but you want a journal publication and a rolling deadline | **ACM UbiComp / IMWUT** | Journal model, quarterly submissions, revise cycle |
| Core is wireless/cellular networking or the mobile *network* itself | **MobiCom / MobiSys** | Mobile-networking and mobile-systems centers |
| Core is a low-power networked-sensor *system* or sensor-platform design | **SenSys** | Networked sensor systems, not human-centric ubicomp |
| Core is information processing in sensor networks / signal-level sensing | **IPSN** | Sensor-network information processing |
| Study is a deep dataset/measurement better as an archival journal article | **IMWUT / IEEE journals** | Journal length and revise cycle |

## Contribution shapes PerCom rewards

- **Human activity / context recognition** — a recognizer or model for human activity, context, or
  behavior from mobile/wearable/ambient sensors, evaluated **cross-subject** on real people (the
  EMGSense lineage).
- **Pervasive system / infrastructure** — a deployable system for sensing, localization, or smart
  environments whose insight outlives the specific hardware (the LANDMARC lineage).
- **Sensing tooling / datasets** — a generator, framework, or dataset that unblocks how the
  community evaluates (the SmartSPEC lineage).
- **Sensing consequence / privacy** — surfacing what ubiquitous sensing makes possible on real
  devices, for good or ill (the DeepMag side-channel lineage).
- **Context modeling / device-to-device** — treating context as a first-class systems concern with
  real deployment tradeoffs (the CHITCHAT lineage).

## The human-centricity and model-swap tests

Two quick tests sharpen a borderline verdict:

- **Human-centricity test:** is a *person* — their activity, context, behavior, or environment —
  the center of the contribution? If the paper is really about the network stack or the sensor
  hardware with no human at the center, route to MobiCom/MobiSys or SenSys/IPSN.
- **Model-swap test:** if the paper leans on a deep model, ask whether the pervasive-computing
  lesson survives swapping the model for another. If not, the model is the contribution and an ML
  venue fits better; PerCom rewards the ubicomp insight, not the architecture.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on evidence
maturity. A recognizer evaluated only **within-subject** or **in-lab** needs cross-subject,
free-living data before the research track; a system shown only on your own testbed needs a
realistic deployment; a study too deep and long for 9 pages may belong in IMWUT first. Submitting a
step early earns a polite "promising, but the evaluation is within-subject" and costs a full cycle,
because PerCom runs on an annual rhythm.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two PerCom programs (dblp, percom.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority ubicomp/mobile/sensing venues (PerCom/UbiComp/IMWUT/
          MobiCom/SenSys)? -> majority non-ubicomp => reviewers read you as a visitor; naturalize first
[Calendar] compare the next PerCom deadline (annual, ~Sep) with IMWUT's rolling quarterly cutoffs
          and MobiCom/SenSys dates -> route to the nearest honest fit, not a year's wait
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> ubicomp researchers/practitioners/users?
[Claim type] recognition / system / tooling-dataset / sensing-consequence / context-modeling
[Human-centricity] is a person at the center? -> yes: PerCom-family; no: MobiCom/SenSys/IPSN
[PerCom vs IMWUT] both fit? -> conference+rebuttal+annual (PerCom) vs journal+rolling (IMWUT)
[Verdict] PerCom research track / neighbor venue / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is PerCom, continue with `percom-workflow` for the calendar and `percom-writing-style` for
the paper shape.
