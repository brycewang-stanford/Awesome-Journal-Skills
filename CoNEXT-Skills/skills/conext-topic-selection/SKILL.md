---
name: conext-topic-selection
description: Use when deciding whether a networking project belongs at ACM CoNEXT or should be routed to SIGCOMM, NSDI, IMC, SIGMETRICS, MobiCom, or HotNets, and when using CoNEXT's two-cycles-per-year calendar and PACMNET journal-style fit to choose the venue and the cycle by contribution shape and evidence maturity.
---

# CoNEXT Topic Selection

Decide the venue *and the cycle* before drafting. CoNEXT — the ACM International Conference on
emerging Networking EXperiments and Technologies, sponsored by ACM SIGCOMM — is a broad
systems-and-measurement networking venue whose research papers are **PACMNET** journal articles.
Reviewers read for a **durable networking contribution evaluated on the real target** (a testbed,
deployment, or trace), not a one-conference result. A technically strong paper whose real lesson is
about pure theory, pure ML, or a non-networking system is respected and then rejected as out of
scope.

## The two routing questions that matter most

Networking has several strong flagships with overlapping scope, so ask two things:

1. **Which networking community and rigor bar fits this contribution?** (CoNEXT vs. SIGCOMM/NSDI/
   IMC/SIGMETRICS/MobiCom.)
2. **Which of CoNEXT's two cycles is the nearest honest deadline my evidence is ready for?**
   (December vs. June — a real lever unique to CoNEXT.)

A strong paper is often publishable at more than one venue; the nearer honest deadline and the best
community fit usually win.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Broad networking contribution — systems, measurement, or architecture — evaluated on a real platform, ready for the nearer CoNEXT cycle | **CoNEXT** | Two-cycle PACMNET track; broad systems-networking scope |
| Top-tier, polished result aimed at the field's most selective single-deadline stage | **SIGCOMM** | The flagship; single annual deadline, its own bar and calendar |
| Systems paper centered on a built-and-deployed networked system with a strong implementation story | **NSDI** | Networked-systems design and implementation focus; USENIX proceedings |
| The whole contribution is a measurement study of the Internet or a large system | **IMC** | Purpose-built internet-measurement venue |
| Core is performance modeling, analysis, or evaluation methodology | **SIGMETRICS** | Measurement-and-modeling home (also a PACMNET-family stream) |
| Wireless/mobile systems are the heart | **MobiCom / MobiSys** | Mobile/wireless-systems scope |
| Early idea or position with an argument but little evaluation | **HotNets** (or CoNEXT Student Workshop) | Venue for provocative early work |

## Contribution shapes CoNEXT rewards

- **Systems + implementation + evaluation on the real target** — a new mechanism in the data plane,
  transport, routing, or the network stack, built and run on real hardware or a faithful testbed
  (the ASIC-switch-insertions lineage).
- **Internet / systems measurement** — a campaign that changes what the community believes about how
  networks or protocols behave in the wild (the QUIC/TLS-performance lineage).
- **Network architecture with deployment or scalability evidence** — a design shown running and
  scaling, not merely proposed (the inter-domain multi-path lineage).
- **Operational / traffic-engineering systems** — measurement plus intervention at real
  carrier/operator scale (the hyper-giants lineage).
- **Wireless and low-power networking** — a model or protocol that respects a real device constraint
  and is validated on a testbed (the ultra-low-power broadcast lineage).

## The platform-realism and re-label tests

Two quick tests sharpen a borderline verdict:

- **Platform-realism test:** is the central claim evaluated on the **real target** the paper is
  about (switch, NIC, kernel, testbed, deployment, or real trace), or does a simulation stand in for
  hardware? CoNEXT rewards evidence on the real platform; a simulation-only systems claim is a
  re-route or a revision risk.
- **Re-label test:** could this paper be submitted to IMC (pure measurement), NSDI (a built system),
  or a theory venue unchanged and read as native there? If its heart is one of those, route
  accordingly; CoNEXT rewards the broad networking framing with real-platform evidence.

## The model-swap test (for ML-for-networking papers)

If your paper leans on a learner or LLM, ask whether the **networking lesson survives swapping the
model** for another. If not, the model is the contribution and an ML venue fits better; if the
lesson is about the network (a measured phenomenon, a deployable mechanism), CoNEXT fits — evaluate
it on the real target and add a contamination-aware ablation (see
[`conext-experiments`](../conext-experiments/SKILL.md)).

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far the
evidence has come. An idea with an argument but little evaluation is a HotNets or Student-Workshop
paper; a mechanism evaluated only in simulation needs a testbed before the research track; a
measurement too preliminary for the bar belongs in a workshop first. Submitting one step early earns
a "promising, but..." — but CoNEXT's two cycles soften this: the next honest deadline is months
away, not a year.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two CoNEXT programs (dblp, conferences.sigcomm.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority networking venues (CoNEXT/SIGCOMM/NSDI/IMC/SIGMETRICS)?
          -> majority non-networking => reviewers read you as a visitor; naturalize the intro first
[Calendar] which CoNEXT cycle (Dec/Jun) is next, vs. SIGCOMM/NSDI/IMC dates -> route to the nearest
          honest fit rather than waiting for a marginal preference
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> operators / protocol designers / systems builders / researchers?
[Claim type] systems mechanism / measurement / architecture / operational / wireless
[Platform] is it evaluated on the real target, or only simulated? -> real => CoNEXT-ready
[CoNEXT vs siblings] pure measurement -> IMC; built system with deep impl -> NSDI; top polish -> SIGCOMM
[Cycle] December vs June -> nearest honest deadline the evidence is ready for
[Verdict] CoNEXT <cycle> / sibling venue / workshop, with a one-line reason
```

Run this before the writing skills; a wrong venue or cycle decision wastes every later step. When
the verdict is CoNEXT, continue with [`conext-workflow`](../conext-workflow/SKILL.md) for the
calendar and [`conext-writing-style`](../conext-writing-style/SKILL.md) for the paper shape.
