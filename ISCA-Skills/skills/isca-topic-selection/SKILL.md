---
name: isca-topic-selection
description: Use when deciding whether a project belongs at ISCA, the ACM/IEEE flagship architecture symposium — testing whether the machine itself is the contribution, choosing between ISCA's November gate and the MICRO, HPCA, and ASPLOS seats in the architecture year, and weighing the main track against the industry track.
---

# ISCA Topic Selection

ISCA reviews reward papers whose central object is a hardware organization: a
pipeline, a cache hierarchy, a memory controller, an accelerator datapath, an
interconnect, a coherence or consistency mechanism. Software may motivate the work
and co-design may strengthen it, but at ISCA the question a program committee member
carries into every discussion is *what does this paper teach us about how to build
machines?* Projects that cannot answer that in one sentence tend to be respected and
rejected in the same review.

## The center-of-gravity question

Write down the single artifact your evaluation section studies hardest. Then ask
where its novelty lives:

- **In the hardware organization** — a new structure, policy, or datapath whose
  behavior you measure across workloads. Natural ISCA material.
- **In the hardware/software contract** — an ISA extension or OS-visible mechanism
  where the software side changes too. ISCA takes these, but ASPLOS's reviewer pool
  is built for them; decide by which half carries the insight.
- **In the software layer alone** — a compiler pass, runtime, or scheduler running
  on unmodified silicon. Reviewers will ask what the architecture lesson is; if the
  answer is "none, but it's fast," route away before writing.
- **In circuits or devices** — below the microarchitecture line, DAC/ISSCC-adjacent
  venues own the expertise ISCA reviewers will say they lack.

A useful stress test: describe the contribution without naming any benchmark. If
what remains is a statement about machine organization ("decoupling X from Y removes
the Z stall class"), the paper is ISCA-shaped. If what remains is only a speedup, it
is a results report, and every top venue struggles to accept those.

## ISCA's seat in the architecture year

ISCA's November deadline and June conference define one corner of a four-venue
rotation. Retargeting between them is normal practice; plan it as a calendar
decision, not an act of desperation. Dates below reflect the most recent verified
cycle (ISCA 2026) — reopen each venue's current CFP before committing.

| Venue | Typical deadline seat | Conference seat | Takes best what |
|---|---|---|---|
| **ISCA** | mid-November (Nov 10/17, 2025 for the 2026 edition) | late June | Broad architecture ideas: cores, memory, accelerators, interconnect, evaluation methodology |
| **MICRO** | spring (roughly April) | October | Microarchitecture depth: front-end, prediction, scheduling, implementation-level mechanisms |
| **HPCA** | mid-summer (roughly July/August) | February | Architecture with a performance-systems flavor; a fast second gate after a June ISCA reject |
| **ASPLOS** | multiple gates per edition | spring | Work whose hardware and software halves are inseparable |

The practical rhythm from ISCA's seat: a paper rejected from ISCA's November gate
can be revised for MICRO in spring; a paper that misses November because evidence
was immature has HPCA's summer gate before the next ISCA November. Retarget on
reviewer-pool fit, never on deadline convenience alone — each venue's committee
notices work dressed for a different room.

## Main track or industry track

ISCA 2026 ran a separate industry track with its own later deadlines (abstracts
December 5, papers December 12, 2025). Choose it when the contribution's value is
*evidence from real products at scale* — measurements, deployment lessons, or
design retrospectives that academia cannot produce — rather than a novel mechanism.
A novel mechanism from an industrial lab still belongs in the main track.

## Fit worksheet

Run this before any drafting; keep the answers in the repo.

```text
CLAIM     One sentence, no benchmark names: what about machine organization
          does this paper establish?
LEVEL     Which layer changes: core / memory hierarchy / accelerator /
          interconnect / ISA contract / methodology?
AUDIENCE  Name three recent ISCA papers whose authors are the natural
          reviewers. (Cannot name three -> wrong room.)
DELTA     Against the nearest of those three: what does this design do that
          theirs cannot, stated as behavior not adjectives?
EVIDENCE  Is the evaluation instrument (simulator / RTL / FPGA / silicon
          measurement) credible for THIS claim? (See isca-experiments.)
TIMING    Can the evidence be complete 6 weeks before mid-November?
          If not, which venue's gate matches the real finish date?
ROUTE     ISCA main / ISCA industry / MICRO / HPCA / ASPLOS / defer.
```

## Shapes with a strong ISCA record

The Influential ISCA Paper Award record (see
`../../resources/exemplars/library.md`) shows the venue's long-run taste. Winning
shapes include a security-motivated cache redesign, a polymorphous core
architecture, 3D-stacked memory organization, a datacenter power-provisioning
measurement study, and a thermal-management design-space classification. Two
lessons: measurement and methodology papers can be first-class ISCA contributions,
and ideas that name a *reusable organizing principle* outlast ideas that optimize
one metric.

## Anti-fits that waste a cycle

- A speedup on an unmodified commercial chip with no architectural mechanism —
  systems venues will treat it better.
- A new benchmark suite with no analysis of what it reveals about designs —
  IISWC-shaped until the analysis exists.
- An accelerator for workload W whose entire delta is "we specialized for W" —
  reviewers ask for the generalizable design insight.
- RTL-quality engineering of a known idea — valuable, but "known idea" is the
  review's first line.
- A simulation study whose conclusion depends on a fidelity level the simulator
  cannot support (see `isca-experiments` before deciding fit, not after).

## Decide and record

```text
[ISCA fit] strong / plausible / weak
[Center of gravity] <layer + one-sentence organizing claim>
[Nearest reviewers] <3 recent ISCA papers>
[Track] main / industry
[Fallback seat] MICRO <year> / HPCA <year> / ASPLOS <cycle> + trigger condition
[Evidence deadline] <date evidence must freeze for a mid-November submission>
```

Facts here are the 2026-cycle snapshot verified 2026-07-08
(`../../resources/official-source-map.md`); the ISCA 2027 CFP was not yet posted at
check time, so treat the November seat as expected, not promised — 待核实. Scope,
track structure, and topics lists are re-decided per edition: reread the live CFP's
topics enumeration before declaring anything out of scope.
