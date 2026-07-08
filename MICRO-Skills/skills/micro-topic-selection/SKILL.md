---
name: micro-topic-selection
description: Use when deciding whether a project belongs at MICRO (IEEE/ACM International Symposium on Microarchitecture) or should route to ISCA, HPCA, ASPLOS, DAC/ICCAD, SC, or MLSys — testing whether the mechanism truly lives inside the machine, gauging the MICRO evidence bar, and weighing the main track against the new Industry Track.
---

# MICRO Topic Selection

Decide venue before writing a single evaluation section. MICRO is the flagship
symposium *of the microarchitecture community specifically* — the 2026 edition is the
59th, which places its lineage back to the 1968 microprogramming workshops. Reviewers
here are calibrated to mechanisms measured in cycles, bytes of state, and milliwatts.

## The mechanism-residency test

Ask where the proposed mechanism physically lives and what evidence proves it works:

1. **State the mechanism in one sentence without naming any software component.** If
   you cannot — if the sentence needs "the compiler", "the OS", or "the runtime" as a
   load-bearing actor — the work is cross-stack and ASPLOS deserves a look first.
2. **Name the structure it modifies:** fetch/decode/rename stages, branch predictor
   tables, cache arrays and replacement metadata, prefetch engines, TLBs, memory
   controller queues, on-chip network routers, accelerator datapaths, or the
   power-management unit. A nameable structure is a strong MICRO signal.
3. **Name the cost line.** MICRO reviewers expect area (mm² or KB of storage), power,
   and latency overheads next to the speedup. If the contribution has no hardware
   cost to account for, ask why it needs to be hardware at all.

## Routing table (deadlines verified 2026-07-08; recheck live pages)

| Symptom of the project | Better home | Why |
|---|---|---|
| Mechanism spans ISA design, coherence protocols, or whole-system organization | ISCA (2027: abstracts Nov 10, papers Nov 17, 2026; Atlanta, June 2027) | Broadest architecture scope |
| Same community, but your evidence matures mid-summer | HPCA (2027: papers July 24, 2026; Salt Lake City, March 2027) | Nearest-cycle sibling |
| Compiler/OS/runtime co-designed with hardware | ASPLOS (2027: April 15 or Sept 9, 2026 deadlines) | Cross-layer is its charter |
| Circuit, EDA-flow, or physical-design contribution | DAC / ICCAD | Below the microarchitecture abstraction |
| Application-scale HPC performance study | SC | Workload, not mechanism |
| ML training/serving systems without new hardware structures | MLSys | Systems-for-ML community |
| Production silicon retrospective, deployment lessons, negative results at scale | MICRO 2026 **Industry Track** (inaugural) | Tailored review for industry constraints |

## What MICRO itself rewards

The Test of Time record is a usable fit oracle. Recent awardees (SIGMICRO ToT pages,
verified 2026-07-08): utility-based cache partitioning (MICRO 2006), 3D die-stacking
microarchitecture, and the CACTI 6.0 NUCA modeling work (both honored in 2025). The
pattern: a **general mechanism or model that other groups can adopt**, not a
point-solution tuned to one workload. Accelerator papers have the same shape —
DaDianNao (MICRO 2014) won by making the *memory locality argument* for ML
accelerators, a structural insight, not a benchmark victory.

Strong MICRO shapes:

- A predictor/replacement/prefetch policy with a storage budget under a few dozen KB
  and a mechanism explanation for *why* it captures the pattern.
- A security mechanism at the speculation/cache boundary with a stated threat model.
- A modeling tool or simulation methodology the community will reuse.
- An accelerator whose novelty is a dataflow or memory-hierarchy decision, defended
  with ablations.

Weak MICRO shapes: pure software optimizations, ISA proposals with no
implementation sketch, "we ran X on Y and report numbers" characterization with no
mechanism, and circuits work with no architectural consequence.

## Quick self-interrogation

```text
Q1  Mechanism sentence written without software actors?          yes / no
Q2  Modified hardware structure named?                            <structure>
Q3  Cost line estimable (KB, mm2, mW)?                             yes / no
Q4  Evidence plan reaches at least cycle-level simulation?         yes / no
Q5  Would the idea survive a 2x-better software baseline?          yes / no
Q6  Is the primary audience microarchitects, not systems builders? yes / no
```

Four or more "yes" answers → draft for MICRO. Q1 or Q6 failing → run the ASPLOS/ISCA
comparison seriously before investing in the MICRO evaluation stack. Record the
answers in the project README — when reviews later dispute the framing, the
original fit reasoning is the fastest input to the resubmission routing decision.

## Borderline cases, adjudicated

Recurring gray zones and how MICRO's own record resolves them:

- **Microarchitectural security** (speculation leaks, cache side channels,
  fault-injection defenses): squarely in scope *when the defense or attack is a
  hardware mechanism with a threat model and a cost line*. If the contribution is
  the vulnerability disclosure or the software mitigation, the security venues
  (IEEE S&P, USENIX Security, CCS) are the primary audience and MICRO the
  secondary.
- **Processing-in-memory / near-data computing:** MICRO-shaped when the paper
  commits to a concrete device organization and evaluates against a tuned
  conventional hierarchy; SC/HPDC-shaped when the story is application scaling.
- **Simulation methodology and modeling tools:** yes — the venue's own Test of
  Time record honors CACTI 6.0, and McPAT is a MICRO paper. The bar is adoption
  potential: the tool must change what *other* groups can evaluate.
- **Compiler-assisted hardware** (hints, ISA extensions consumed by new
  structures): MICRO if the hardware structure does the heavy lifting and the
  software change is a thin enabler; ASPLOS if the interesting decisions are
  split across the boundary.
- **GPU/accelerator scheduling in software:** not MICRO, however
  hardware-adjacent the vocabulary — no new structure, no MICRO.

## Cycle awareness

MICRO's submission deadline sits in early April (2026 cycle: abstracts March 31,
papers April 7, both 11:59 PM **EDT** — not AoE), with the conference in the
October/November slot (MICRO 2026: Athens, Greece, Oct 31 – Nov 4). If you are
reading this after the April deadline, `micro-workflow` maps the fallback lattice:
HPCA in July, ASPLOS in September, ISCA in November, MICRO again next April. Dates
above are one cycle's snapshot — reopen `microarch.org` before committing a plan.

## Output format

```text
[Venue fit] MICRO main / MICRO industry track / re-route to <venue>
[Mechanism sentence] <one sentence, hardware actors only>
[Structure modified] <named pipeline/cache/predictor/accelerator structure>
[Cost line] <area, storage, power estimate or "cannot estimate — warning">
[Evidence plan] analytical / trace-driven / cycle-level sim / RTL / FPGA / silicon
[Nearest competing venue] <venue + one-line reason it loses>
[Next deadline to target] <venue, date, source URL to re-verify>
```
