---
name: sigcomm-topic-selection
description: Use when deciding whether a project is a strong ACM SIGCOMM fit, choosing the research versus experience track, identifying the networking-stack mechanism at the core of the contribution, and routing misfits to NSDI, MobiCom, CoNEXT, IMC, SIGMETRICS, or a systems venue before writing begins.
---

# SIGCOMM Topic Selection

Use this before writing, and before committing the single yearly deadline. SIGCOMM is the
broad networking flagship: it rewards a contribution to the design, measurement, or analysis
of networks and communication systems that is stated as a **mechanism or architecture** and
proven under **realistic conditions**. Reopen the current CFP's topic list before final
routing — emphasis drifts between editions.

## Fit test

- Prefer SIGCOMM when the contribution is a networking-stack idea — a protocol, transport or
  congestion mechanism, routing or forwarding architecture, data-center or wide-area fabric,
  programmable-data-plane technique, network measurement result, or systems-for-networking
  design — with evaluation on a testbed, trace, or deployment.
- The bar is a **principle that travels**, not a tuned deployment. A single-site tuning win
  with no generalizable mechanism reads as under-contribution here even if the numbers are
  good.
- Both tracks live under this bar: **research** wants design novelty and depth; **experience**
  wants lessons only real operation at scale can teach.

## Where else the work might belong

| Signal in the project | Better-fit venue | Why |
|---|---|---|
| Networked-systems build with heavy implementation, USENIX-style | NSDI | Design-and-implementation focus; two deadlines a year |
| Mobile, wireless, or physical-layer / RF mechanism | MobiCom (or SIGMOBILE venues) | Over-the-air and device evidence is that community's core |
| Solid networking result, but incremental for the flagship | CoNEXT | SIGCOMM's sister venue for strong but narrower contributions |
| Pure Internet/traffic **measurement** with no new mechanism | IMC | Measurement-methodology venue; SIGCOMM wants measurement to motivate a mechanism |
| Performance modeling / analysis as the contribution | SIGMETRICS | Analytical and evaluation-method emphasis |
| OS/storage/distributed-systems core, networking secondary | OSDI / SOSP | Systems-first framing |

## The routing that trips people up

SIGCOMM and NSDI overlap heavily, and authors agonize over the split. A workable heuristic:
if the paper's spine is a **networking abstraction, protocol, or measurement-driven design
argument**, it leans SIGCOMM; if the spine is a **built-and-deployed system whose value is in
the engineering and implementation**, it leans NSDI. Neither is a rule — strong papers cross
the line both ways — but the single SIGCOMM deadline means a misroute costs a year, so decide
deliberately. IMC is the other frequent confusion: a measurement paper needs a **mechanism or
a design implication** to be SIGCOMM rather than IMC.

## Vignette: where a congestion-control result goes

A project proposes a new congestion signal and shows it cuts tail flow-completion time on a
data-center testbed. SIGCOMM reading: strong fit — a transport **mechanism** with tail
evidence under realistic traffic is the house genre (compare DCTCP and pFabric in the
exemplars). Strip the mechanism and keep only a measurement of how badly today's schemes
behave, and it drifts toward IMC; rebuild it as a fully implemented, deployed RPC stack whose
contribution is the system, and NSDI becomes competitive. Same core, three homes.

## Sharpening moves before committing

- Name the **mechanism** in one sentence: the protocol change, the architectural shift, or
  the measured invariant. If no mechanism exists, the SIGCOMM framing does not exist either.
- Decide the **track** honestly and early; the experience track is a strength for real
  deployments, not a demotion.
- Confirm the evaluation can reach **testbed, trace, or deployment** evidence, not
  simulation only; simulation-only fabric claims are a quiet fit failure at this venue.
- Weigh the **one-deadline cost**: if the result is a year from convincing, plan the year
  rather than gambling the single February slot.

## Output format

```text
[Fit] strong SIGCOMM / possible SIGCOMM / better elsewhere
[Track] research / experience / n-a
[Best venue] SIGCOMM / NSDI / MobiCom / CoNEXT / IMC / SIGMETRICS / other
[Mechanism sentence] <one sentence naming the networking contribution>
[Top rejection risk] <novelty / evidence realism / measurement-only / scope>
[Next action] <mechanism, evaluation, framing, or venue switch>
```
