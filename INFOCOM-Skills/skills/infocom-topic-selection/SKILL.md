---
name: infocom-topic-selection
description: Use when deciding whether a networking project belongs at IEEE INFOCOM or should be routed to SIGCOMM, NSDI, MobiCom, ICNP, or an IEEE/ACM networking journal (ToN, JSAC), distinguishing INFOCOM by its breadth, its analytical/optimization tradition alongside systems, and the modeling-vs-building axis.
---

# INFOCOM Topic Selection

Decide the venue before drafting. INFOCOM — the IEEE International Conference on Computer
Communications, the IEEE ComSoc networking flagship — is the **broad, large-scale** networking
venue. Its defining feature relative to its siblings is **breadth plus a living analytical
tradition**: a well-posed model with a theorem and a convincing evaluation is a first-class INFOCOM
paper, not a second-class one. A pure systems-building paper is welcome, but so is a
scheduling/optimization/queueing/game-theory result that SIGCOMM or NSDI would push to a journal.

## The routing question that matters most

The decisive question is rarely "is this networking?" but **"is the contribution a model/analysis, a
built system, or a measurement — and which community rewards that shape now?"** INFOCOM is the safe
home for the analytical and the broad; SIGCOMM/NSDI pull toward built-and-measured systems with a
deployment story. Use the finer signals below and the live calendar to choose.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Modeling/optimization/algorithmic core (scheduling, resource allocation, queueing, game theory, network economics) with analysis + simulation | **IEEE INFOCOM** | Its analytical tradition treats theorems-with-evaluation as first-class |
| Broad networking contribution, ready now, with the next INFOCOM deadline nearer | **IEEE INFOCOM** | Large flagship; broad scope and reviewer pool |
| A built, deployed system with a measured Internet/datacenter deployment story | **ACM SIGCOMM** | Rewards architecture + real deployment; smaller, systems-first |
| A systems artifact whose case is a real implementation and hard performance numbers | **USENIX NSDI** | Networked-systems building, artifact-heavy |
| Wireless/mobile system with real devices, PHY/MAC + measurement | **ACM MobiCom / MobiSys** | Mobile-computing center of gravity |
| A focused protocol-design/analysis contribution | **IEEE ICNP** | Protocols venue; narrower than INFOCOM |
| Study too long or too incremental for a nine-page conference limit | **IEEE/ACM ToN, IEEE JSAC** | Journals with no page ceiling and a revise-and-resubmit cycle |

## Contribution shapes INFOCOM rewards

- **Analytical / optimization** — a scheduling, resource-allocation, routing, caching, or
  network-economics problem formulated cleanly, with structural results or an algorithm with
  provable guarantees, validated in simulation. The queueing/optimization lineage is native here.
- **Protocol / mechanism design** — a new protocol or control mechanism (congestion control,
  access, coordination) with analysis and evaluation on a simulator or modest testbed.
- **Wireless and PHY/MAC** — modeling and technique for wireless, cellular, 5G/6G, IoT, or
  backscatter, often blending analysis with measurement.
- **Measurement / empirical networking** — a study of real network behavior with a dataset and
  methodology a reviewer can scrutinize.
- **Learning-for-networking** — ML applied to a networking problem, where the **networking** lesson
  (not the model) is the contribution (see the modeling-swap test).

## The modeling-vs-building and model-swap tests

Two quick tests sharpen a borderline verdict:

- **Modeling-vs-building axis:** if the heart is a *formulation and analysis* (with simulation to
  confirm), INFOCOM fits and SIGCOMM/NSDI may not. If the heart is a *built system with a
  deployment/measurement story*, the systems venues fit better and an analysis-only INFOCOM framing
  undersells it.
- **Model-swap test:** if the paper leans on a learner, ask whether the networking lesson survives
  swapping the model. If not, the model is the contribution and an ML venue fits better; if yes, the
  networking framing is real and INFOCOM welcomes it.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient. A formulation with a theorem but no evaluation reads as
incomplete for the main track; a system evaluated only on a toy topology needs realistic scale
before it convinces; a measurement without a methodology a reviewer can audit will not survive the
crowded pool. INFOCOM's scale means a marginal paper competes against ~1,400 others for ~19% of
slots — submit when the analysis *and* the evaluation are both ready.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two INFOCOM programs (dblp conf/infocom) for your subarea
          -> several recent papers = a reviewer pool exists; near-zero = mismatch or opening
[Shape]   is your core a model/algorithm, a built system, or a measurement?
          -> model/algorithm leans INFOCOM; built-and-deployed leans SIGCOMM/NSDI
[Calendar] compare the next INFOCOM deadline (late July) with SIGCOMM/NSDI/MobiCom/journal dates
          -> route to the nearest honest fit rather than idling a year
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> network designers/operators/theorists?
[Claim type] analytical / protocol / wireless / measurement / learning-for-networking
[Axis] model-and-analyze -> INFOCOM; build-and-deploy -> SIGCOMM/NSDI; wireless system -> MobiCom
[Sibling check] protocol-focused -> ICNP; too long/incremental -> ToN/JSAC
[Verdict] INFOCOM main track / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is INFOCOM, continue with `infocom-workflow` for the calendar and `infocom-writing-style` for the
paper shape.
