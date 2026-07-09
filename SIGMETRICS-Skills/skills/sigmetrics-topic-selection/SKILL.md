---
name: sigmetrics-topic-selection
description: Use when deciding whether a computer-systems performance project belongs at ACM SIGMETRICS or should be routed to IMC, SIGCOMM/NSDI/OSDI, INFOCOM, a learning venue (NeurIPS/ICML), or a performance journal (Performance Evaluation/TON/QUESTA), and when picking the right SIGMETRICS track (Theory / Measurement & Applied Modeling / Learning / Operational Systems).
---

# SIGMETRICS Topic Selection

Decide the venue and track before drafting. SIGMETRICS — the ACM flagship for **performance
measurement, modeling, and evaluation of computer systems** — rewards a **rigorous
performance-evaluation contribution**: a stochastic/queueing model with a **proven bound**, a
**principled measurement study**, or a **learning-for-systems** algorithm with guarantees. A
technically strong paper whose real lesson is a *built system* (route to NSDI/OSDI), a *pure network
measurement* (route to IMC), or a *learning-theory result with no systems payoff* (route to
NeurIPS/COLT) is respected and then rejected as out of scope.

## The routing question that matters most

The decisive question is rarely "is this about systems performance?" but **"is the contribution an
analyzed/measured performance result, or is it something else with performance numbers attached?"**
SIGMETRICS wants the *why* — a model, a proof, a validated methodology — not only a faster system or
a bigger dataset.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| A model/policy with a **proven performance bound**, or a principled measurement/modeling study | **ACM SIGMETRICS** | Its center: rigorous performance evaluation published in POMACS |
| The contribution is a **built system**; the design/implementation is the point | **NSDI / OSDI / SIGCOMM** | Systems-building venues; SIGMETRICS wants analysis, not a system artifact |
| The whole paper is **network measurement** (Internet, CDN, topology, traffic) | **IMC** | The dedicated network-measurement venue; single annual deadline |
| Networking with a systems/protocol contribution | **SIGCOMM / NSDI / INFOCOM** | Networking-systems scope |
| A **learning-theory** result with no systems performance payoff | **NeurIPS / ICML / COLT** | Learning venues; SIGMETRICS Learning track wants a systems angle or systems-relevant guarantees |
| A study too long/deep for 20 pages, or wanting multiple revision rounds | **Performance Evaluation / TON / QUESTA** | Journals with no conference page ceiling and open-ended revision |

## Contribution shapes SIGMETRICS rewards

- **Stochastic / queueing / scheduling theory** — a model of a system's performance with a proven
  bound, stability condition, or optimality result, validated numerically (the SOAP lineage).
- **Measurement & applied modeling** — a principled measurement or simulation methodology and the
  characterization it yields about a real system (the Google-Play-study lineage).
- **Learning for systems** — an online-learning/bandit/RL/control algorithm for a systems problem,
  with **regret/convergence/sample-complexity guarantees** (the learning-to-rank lineage).
- **Operational systems** — a deployed system in significant real-world use, analyzed with
  principled measurement and metrics (the Operational Systems Track; may name the system/org).

## The rigor and validation tests

Two quick tests sharpen a borderline verdict:

- **Rigor test:** does the contribution carry a *checkable* claim — a theorem, a stated-assumption
  bound, a measurement methodology a skeptic would accept — or only "it is faster on our setup"? If
  the latter, it is a systems-building paper (NSDI/OSDI), not SIGMETRICS.
- **Model-swap / methodology test:** if your paper leans on a learner or a specific system, ask
  whether the *performance-evaluation* lesson survives — a guarantee, a validated model, a general
  methodology. If the only result is a benchmark score, it is an ML or systems paper wearing a
  SIGMETRICS title.

## Picking the track (do this at abstract registration)

- **Theory:** the core is a proof (queueing, scheduling, caching, algorithms, control).
- **Measurement & Applied Modeling:** the core is data from a real system + a methodology/model.
- **Learning:** the core is a learning algorithm with analysis, applied to or for systems.
- **Operational Systems:** the core is a deployed, in-use system; you may reveal its name/org.

Pick **one**; a second only for genuinely interdisciplinary work (e.g. a learning-theoretic result
validated by measurement). The wrong track routes you to the wrong reviewers.

## Cheap reconnaissance before committing

```text
[Scope]    scan the last few POMACS issues (dblp, ACM DL) for your subarea and track
           -> several recent papers = a reviewer pool exists; none = opening or mismatch
[Rigor]    does your headline claim reduce to a theorem, a validated model, or a principled
           measurement? -> if not, reconsider SIGMETRICS vs. a systems venue
[Calendar] the next rolling deadline (summer/fall/winter) is ~a quarter away -> route to the
           nearest honest fit rather than forcing a rushed proof/measurement
```

## Decision procedure

```text
[Audience]  who acts differently if the claim holds? -> systems designers/operators/theorists?
[Claim type] queueing/theory / measurement / learning-with-guarantees / operational
[Rigor gate] is there a checkable performance claim (proof / validated model / methodology)?
[Sibling check] built system -> NSDI/OSDI; pure net-measurement -> IMC; learning-theory-only -> NeurIPS
[Verdict]   SIGMETRICS <track> / sibling venue / performance journal, with a one-line reason
```

Run this before the writing skills; a wrong venue or track decision wastes every later step. When
the verdict is SIGMETRICS, continue with `sigmetrics-workflow` for the deadline choice and
`sigmetrics-writing-style` for the paper shape.
