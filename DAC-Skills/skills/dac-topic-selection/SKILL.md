---
name: dac-topic-selection
description: Use when deciding whether an EDA or chip-design project belongs at the ACM/IEEE Design Automation Conference (DAC) and, if so, in the double-blind archival Research Manuscript track versus the industry-facing Engineering Track — or whether it should route to a sibling EDA venue (ICCAD, DATE, ASP-DAC) or a computer-architecture venue (ISCA/MICRO/HPCA), decided by contribution shape, QoR evidence maturity, and the November calendar.
---

# DAC Topic Selection

Decide the venue *and the track* before drafting. DAC — the ACM/IEEE **Design Automation
Conference**, "The Chips to Systems Conference" — is the premier forum for **electronic design
automation (EDA)** and chip/system design. Its distinguishing structural fact, absent from the
academic architecture venues, is that DAC hosts **two peer-reviewed paper tracks with different
review models**: the double-blind, archival **Research Manuscript** track and the industry-facing
**Engineering Track**. Picking the wrong track wastes a full cycle just as surely as picking the
wrong conference.

## The two questions, in order

1. **Is this a DAC contribution at all?** DAC rewards work that advances how chips and systems are
   *designed, automated, verified, or secured* — a new placement/routing algorithm, a synthesis or
   verification technique, an ML-for-EDA method, a hardware-security defense, a design methodology
   with measured QoR impact. A pure computer-architecture result (a new microarchitecture, a cache
   policy) whose EDA/automation angle is incidental is respected and then routed to ISCA/MICRO/HPCA.
2. **Research Manuscript or Engineering Track?** This is the DAC-specific fork. Route by whether the
   core deliverable is a *novel, archival research contribution evaluated against baselines*
   (Research) or a *deployed industrial design/flow/methodology lesson from practice* (Engineering).

## Research Manuscript vs Engineering Track

| Signal in your project | Track | Why |
|---|---|---|
| Novel algorithm/technique with QoR gains vs prior art, generalizable | **Research Manuscript** | Double-blind, archival on ACM DL; judged on novelty + evidence |
| An empirical or ML-for-EDA study that changes what the field believes | **Research Manuscript** | Archival research contribution |
| A real tapeout/flow experience, tool-deployment lesson, or methodology from industry | **Engineering Track** | Practitioner audience; separate committee; presentation-first |
| Front-end design, back-end design, IP, or embedded SW/HW practice you want peers to learn from | **Engineering Track** | Its named scope; not required to out-QoR a baseline |
| Result too early/small for archival novelty but timely | **Late Breaking Results** | Short poster-style track, later deadline |

The trap for academics: submitting a solid-but-incremental flow improvement to the Research track
where it dies on novelty, when the Engineering Track would have welcomed it as a practice lesson.
The trap for practitioners: hiding a genuinely novel algorithm in the Engineering Track and losing
the archival citation record.

## Sibling-venue routing (EDA and architecture)

| Signal in your project | Better home | Why |
|---|---|---|
| Broad EDA/chip-design contribution, ready now, DAC deadline nearer | **DAC Research** | The flagship EDA venue; largest audience and industry reach |
| Deeper CAD-algorithm focus, or DAC deadline already passed | **ICCAD** | The other top EDA venue; complementary fall calendar |
| European community, design-and-test emphasis | **DATE** | Design, Automation and Test in Europe (distinct venue) |
| Asia-Pacific community, ASP-DAC's January cycle fits | **ASP-DAC** | Asia and South Pacific DAC (distinct venue) |
| Core is a microarchitecture / accelerator idea, EDA is incidental | **ISCA / MICRO / HPCA** | Computer-architecture flagships, different reviewer pool |
| Test/reliability depth | **ITC / VTS** | Test-community venues |
| Analog/RF circuit design as the contribution | **ISSCC / CICC / VLSI** | Circuits venues, not the EDA-algorithm venue |

> Name-collision guard: **ASP-DAC** and **DATE** are *not* DAC; they have their own calls and
> deadlines. And "DAC" in a circuits paper often means *digital-to-analog converter* — a valid DAC
> research topic, not the conference.

## Contribution shapes DAC Research rewards

- **A new EDA algorithm + tool + QoR evaluation** — synthesis, placement, routing, timing, power,
  verification, or test, showing measured **PPA (power/performance/area)**, wirelength, timing
  slack, or runtime gains over the strongest prior technique on standard benchmarks.
- **ML for EDA** — learning-based placement, routing, synthesis, timing/IR-drop prediction, or an
  agentic/foundation-model approach to a design task, with a fair non-ML or prior-ML baseline.
- **Hardware security** — a concrete attack or defense (side-channel, Trojan, IP protection,
  post-quantum primitive, supply-chain integrity) with a threat model and measured overhead.
- **Design methodology / system-level** — chiplet integration, 3D-IC, near-memory, or a cross-layer
  methodology whose payoff is demonstrated on a realistic design.
- **Emerging technology** — quantum EDA, in-memory/neuromorphic, or approximate computing, with an
  automation or design-quality contribution rather than a device-physics one.

## The QoR-impact and model-swap tests

- **QoR-impact test:** state your gain in the field's own currency — "X% wirelength / Y% total
  negative slack / Z× runtime at equal quality." If you cannot phrase the contribution as a
  measured QoR delta or a new capability, the Research track will read it as incremental.
- **Model-swap test (for ML-for-EDA):** if you swap the learner for another, does the *EDA* lesson
  survive? If the paper is really about a model architecture with a toy EDA wrapper, it is an ML
  paper and routes to an ML venue; DAC wants the design-automation lesson.

## Cheap reconnaissance before committing

```text
[Scope]    scan the last two DAC programs (dblp, ACM DL) for your subarea
           -> 3+ recent papers = a reviewer pool exists; 0 = mismatch or ICCAD/DATE fit
[Benchmarks] does a standard suite exist for your problem (ISPD, EPFL, ISCAS/ITC, TAU, CircuitNet)?
           -> reviewers expect it; a private-benchmark-only evaluation is a scored weakness
[Calendar] DAC manuscript deadline is ~November; ICCAD is later, ASP-DAC is January, DATE differs
           -> route to the nearest honest fit rather than idling a cycle
```

## Decision procedure

```text
[Is it EDA/chip-design?] automation/verification/security/methodology contribution? -> DAC candidate
[Track fork] novel + archival + baselined -> Research Manuscript
             industrial practice/deployment lesson -> Engineering Track
             timely but early -> Late Breaking Results
[Sibling check] CAD-algorithm depth & fall timing -> ICCAD; architecture core -> ISCA/MICRO/HPCA;
                circuits core -> ISSCC/CICC
[Verdict] DAC Research / DAC Engineering / sibling venue, with a one-line QoR-framed reason
```

Run this before the writing skills; a wrong track or venue decision wastes every later step. When
the verdict is DAC Research, continue with `dac-workflow` for the November-anchored calendar and
`dac-writing-style` for the 6+1-page paper shape.
