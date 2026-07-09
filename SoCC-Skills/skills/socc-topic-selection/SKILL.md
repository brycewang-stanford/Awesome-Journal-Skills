---
name: socc-topic-selection
description: Use when deciding whether a cloud-computing project belongs at ACM SoCC or should be routed to OSDI, NSDI, EuroSys, USENIX ATC, SOSP, or a data venue (SIGMOD/VLDB), leaning on SoCC's unique joint SIGMOD+SIGOPS identity, its welcome of measurement and experience papers alongside systems-building, and the model-swap and re-label tests.
---

# SoCC Topic Selection

Decide the venue before drafting. SoCC — the ACM Symposium on Cloud Computing — is the **only
conference co-sponsored by SIGMOD and SIGOPS**, and that joint sponsorship *is* its identity: it
sits at the **systems-and-data intersection** of cloud research. Reviewers read for a **cloud
contribution that matters at scale**, and the venue explicitly welcomes not just clean-slate
systems but **measurement studies, experience papers, and cloud-economics work** that a pure
OS/networking flagship might treat as second-class. A technically strong paper whose real home is
kernel scheduling, network fabric, or query-optimizer internals is respected and then routed
elsewhere.

## The routing question that matters most

The decisive question is rarely "is this cloud?" but **"does this contribution live at the
systems-and-data intersection that SoCC owns, or is it a pure-systems or pure-data result better
served by a specialized flagship?"** SoCC's sweet spot is the paper that a *datacenter operator or
cloud platform team* would act on: storage and data services, resource management and scheduling,
serverless, multi-tenancy, big-data and ML-systems infrastructure, edge/fog, and the cost and
economics of running all of it.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Cloud infrastructure at the systems+data intersection: storage/data services, resource mgmt, serverless, ML-systems infra, multi-tenancy, cloud economics | **ACM SoCC** | The joint SIGMOD+SIGOPS venue; welcomes systems *and* measurement/experience |
| Core is a novel OS/kernel or a clean-slate distributed-systems mechanism, depth over cloud framing | **OSDI / SOSP** | OS and systems flagships; deeper systems-novelty bar |
| Core is the network — datacenter fabric, congestion control, RDMA, SDN | **NSDI** | Networked-systems flagship |
| General systems contribution, European rotation, OS/runtime flavor | **EuroSys** | Broad systems venue; ACM, different community and calendar |
| Solid systems/experience result that fits a broad practitioner venue | **USENIX ATC** | General systems + experience; USENIX template and process |
| Core is a database engine, query processing, transactions, or data mgmt theory | **SIGMOD / VLDB** | Data-management flagships; SoCC shares SIGMOD sponsorship but is systems-facing |
| Pure ML modeling result whose cloud consequence is incidental | **an ML venue** | The model, not the cloud system, is the contribution |

## Contribution shapes SoCC rewards

- **Cloud system + evaluation on a real/realistic deployment** — a new storage, scheduling,
  serverless, or data-serving mechanism, built and measured on a cluster or testbed against
  credible baselines (the Cake / YARN lineage).
- **Measurement / trace study** — turning production traces or large-scale measurement into
  durable findings about how real cloud infrastructure behaves (the Google-trace lineage) — a
  distinctly prized SoCC mode, reflecting the SIGMOD half of its identity.
- **Benchmark / measurement instrument** — a reusable tool the community adopts to compare cloud
  systems (the YCSB lineage).
- **Experience paper** — design decisions and operational lessons from a deployed system at scale,
  reported honestly including what failed (the YARN lineage) — SoCC's welcome mat for industry and
  operations.
- **Cloud economics / data markets** — pricing, cost models, SLAs, and the data economy, a scope
  the joint sponsorship makes native rather than exotic.

## The model-swap and re-label tests

Two quick tests sharpen a borderline verdict:

- **Model-swap / mechanism-swap test:** if your paper leans on an ML predictor or one specific
  engine, ask whether the **cloud lesson** survives swapping it. If not, the model is the
  contribution and an ML venue fits better; if yes, the cloud-systems framing is real.
- **Re-label test:** could this paper be submitted to OSDI/NSDI/SIGMOD unchanged and read as native
  there? If its heart is kernel novelty (OSDI), network fabric (NSDI), or query internals (SIGMOD),
  route accordingly. SoCC rewards the paper whose contribution genuinely spans **operating a cloud
  service on real data at scale**.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far the
evidence has come. A mechanism evaluated only in simulation needs a testbed or deployment before
the research track; a measurement study needs a trace or corpus a reviewer can scrutinize; an
experience paper needs a system that was actually operated. Submitting a simulation-only systems
claim invites the "does this hold on a real deployment?" reject that both sponsoring communities
apply.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two SoCC programs (dblp conf/cloud, acmsocc.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography a mix of systems (OSDI/NSDI/EuroSys/ATC/SoCC) and data
          (SIGMOD/VLDB) venues? -> a SoCC paper usually cites both lanes
[Calendar] SoCC has two rounds/year; compare the nearer round with OSDI/NSDI/EuroSys/ATC and
          SIGMOD/VLDB dates -> route to the nearest honest fit, but never reuse a Round-1 reject
          in Round 2
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> cloud operators / platform teams / data-infra builders?
[Claim type] cloud system / measurement / benchmark / experience / cloud-economics
[Intersection check] does it span systems AND data/scale, or is it pure-OS / pure-network / pure-DB?
[Sibling check] kernel depth -> OSDI/SOSP; network fabric -> NSDI; DB engine -> SIGMOD/VLDB
[Verdict] SoCC research track / sibling venue, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is SoCC, continue with `socc-workflow` for the two-round calendar and `socc-writing-style`
for the paper shape.
