---
name: asplos-topic-selection
description: Use when deciding whether a project belongs at ASPLOS or at a single-community venue — applying the cross-layer deletion test, matching against ASPLOS's architecture/PL/OS intersection identity, routing to ISCA/MICRO/HPCA, PLDI/POPL, SOSP/OSDI/EuroSys, SC, or MLSys instead, and choosing between the April and September deadlines.
---

# ASPLOS Topic Selection

ASPLOS's self-description is unusually operational: it seeks work that improves the
core disciplines — operating systems, programming languages, computer architecture —
**and their intersection**, and its 2027 rapid-review round explicitly prioritizes
submissions at that intersection (CFP, checked 2026-07-08). Venue fit is therefore
not a prestige question here; it is a screening variable. A technically strong paper
that lives cleanly inside one community can be filtered in the first round not
because it is bad but because a single-community venue owns its reviewers.

## The deletion test

Ask, for each layer the paper touches: *if this layer's content were deleted, would
a publishable paper remain?*

- Delete the software half and a full paper remains → the work is an ISCA/MICRO/HPCA
  candidate wearing an ASPLOS template.
- Delete the hardware half and a full paper remains → it is a SOSP/OSDI/EuroSys or
  PLDI paper.
- Delete either half and *nothing defensible remains* → the coupling is real; ASPLOS
  is a first-choice target.

The exemplars library shows what passing looks like in award-validated form: an
accelerator argued from data movement, a scheduler premised on hardware
heterogeneity, an interrupt-delivery boundary redrawn between hypervisor and silicon
(see `../../resources/exemplars/library.md`).

## Routing table

| If the core claim is... | Stronger first target | ASPLOS becomes right when... |
|---|---|---|
| A microarchitectural structure (predictor, cache policy, pipeline) | ISCA / MICRO / HPCA | The structure exists to serve a named software behavior, and software changes with it |
| A language design, type system, or compiler optimization | PLDI / POPL / CGO / OOPSLA | The compiler co-evolves with an ISA, accelerator, or OS interface |
| An OS/distributed-systems design on commodity hardware | SOSP / OSDI / EuroSys / ATC | Hardware assumptions are load-bearing: new memory technology, custom hints, near-data compute |
| HPC-scale performance engineering | SC / PPoPP | The result generalizes into an architectural or systems principle beyond one machine |
| ML training/serving systems on stock stacks | MLSys | The ML workload drives a hardware/software interface change, not just better scheduling |
| Security via hardware mechanisms | IEEE S&P / USENIX Security / CCS | The defense requires co-designed architecture + systems support and its evaluation is performance-shaped |

Scope confirmation: the 2027 topics list spans heterogeneous architectures and
accelerators; cloud and datacenters; memory, storage, networking, and I/O; power,
energy, and thermal management; profiling, debugging, and testing; security,
reliability, and availability; parallelism and big-data systems; virtualization; and
experimental methodologies — with non-traditional topics welcome when centered in the
core disciplines.

## Fit interrogation script

Run this before any writing begins:

```text
Q1  Name the interface/boundary the work changes (ISA extension, OS/hardware
    contract, runtime/accelerator ABI, ...). No boundary named -> weak fit.
Q2  Deletion test per layer (above). Both halves survive alone -> route away.
Q3  Who must adopt this? If one community can adopt it without the other
    noticing, the intersection claim is decorative.
Q4  What evidence class does the claim need — real silicon, FPGA, simulator?
    If the answer is "none of these", the paper may be a PL/theory paper.
Q5  Can the contribution be stated in one sentence that a rapid reviewer
    reading only two pages will believe? Draft that sentence now.
```

## Choosing between the two 2027 deadlines

ASPLOS 2027 offers two submission gates — April 15, 2026 (passed as of 2026-07-08)
and **September 9, 2026** — framed by the CFP as "submit when ready." Treat the choice
as an evidence-maturity decision, not a calendar accident:

- Submit September only if the evaluation matrix is complete; the two-deadline model
  removed the mid-year round, so a miss costs roughly half a year.
- A Major Revision outcome effectively adds a private third gate (revision due at the
  camera-ready deadline, six weeks after notification) — but only for papers whose
  core was sound. Do not submit a hollow evaluation hoping for the revision path;
  the revision counts as a submission on your record with that PC.

## Distinctive-fit signals worth writing down

- The paper's insight is *information that crosses a layer* (what hardware knows that
  software needs, or vice versa) — the most reliably ASPLOS-shaped idea.
- The evaluation needs both a hardware-accuracy instrument (simulator/FPGA/silicon)
  and a software-realism instrument (kernel patch, runtime, full applications).
- Related work must be argued against two or three communities at once; if one
  community's literature suffices, so would its venue.

## Intersection anti-patterns

Recurring shapes that look ASPLOS-flavored but fail the screen:

- **The garnish paper** — a complete single-community design plus one paragraph
  of "hardware support could accelerate this." The intersection must be
  load-bearing on page 1, not speculative in section 8.
- **The stapler paper** — an architecture result and an OS result about the same
  workload, bound in one PDF with no shared mechanism. Two rejectable halves do
  not sum to one acceptable whole.
- **The tuning paper** — heroic performance engineering on existing interfaces.
  Without a changed boundary or a transferable principle, it routes to ATC-style
  venues or an industrial track.
- **The premature-generality paper** — a mechanism evaluated only where it was
  conceived, claiming the whole intersection. Scope the claim to the evidence and
  let the routing table above pick the venue for the scoped claim.

## Repairing a near-miss instead of rerouting

If the deletion test fails narrowly, a reframing pass is often cheaper than a
venue change: identify the strongest cross-layer *consequence* of the existing
result (a new OS policy the hardware data enables; a compiler contract the
mechanism makes checkable), promote it from implication to evaluated
contribution, and rebuild pages 1-2 around the promoted claim. Budget this as
real research work — it usually needs one new experiment — and re-run the
interrogation script afterward rather than assuming the patch took.

## Output format

```text
[Fit verdict] first-choice ASPLOS / viable but single-community-stronger / route away
[Boundary changed] <the named interface>
[Deletion test] hardware-only remainder: Y/N · software-only remainder: Y/N
[Route-away target] <venue + one-line reason, or n/a>
[Deadline call] September 9, 2026 readiness: evidence gaps listed
[Two-page sentence] <the one-sentence contribution a rapid reviewer must believe>
```
