# DAC Exemplars Library (contribution shape × EDA subfield)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at the **ACM/IEEE Design
> Automation Conference (DAC)** — matching title, author list, year, and the DAC proceedings
> string. Papers that could not be cleanly confirmed as DAC (as opposed to ICCAD, DATE, ASP-DAC,
> IEEE S&P, or a journal) were **omitted and documented below**. It is deliberately a short,
> verified list (4 verified > 15 guessed).
>
> **Sibling-confusion guard:** DAC is **not** ICCAD, **not** DATE, **not** ASP-DAC, and **not** a
> security/circuits venue (IEEE S&P, ISSCC). Several canonical EDA techniques were introduced at
> those venues instead; a famous author or a familiar tool name does **not** prove a DAC placement.
> Each row was checked to be a DAC edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent QoR numbers, speedups, or table values — read the original on ACM DL before
> citing anything. For DAC-specific policy, tracks, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × EDA subfield** is closest to yours, then study how that
paper states a **design-automation problem practitioners recognize**, backs it with **measured QoR
evidence on real benchmarks against a strong baseline**, and shows **why the mechanism generalizes**
— the DAC bar (see [`../../skills/dac-writing-style/SKILL.md`](../../skills/dac-writing-style/SKILL.md),
[`../../skills/dac-topic-selection/SKILL.md`](../../skills/dac-topic-selection/SKILL.md), and
[`../../skills/dac-experiments/SKILL.md`](../../skills/dac-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "DAC-shaped."

These four span four decades and four EDA subfields; two (Chaff and DREAMPlace) also model what
**decade-scale impact** — the kind honored by the ACM/IEEE **A. Richard Newton Technical Impact
Award** — looks like at this venue.

---

## By contribution shape

### EDA algorithm + tool — Boolean satisfiability / verification

- **Moskewicz, Madigan, Zhao, Zhang & Malik, "Chaff: Engineering an Efficient SAT Solver,"
  DAC 2001, pp. 530-535.** Verified: dblp `conf/dac/MoskewiczMZZM01`. Introduced the Chaff SAT
  solver with its efficient Boolean-constraint-propagation (watched literals) and a low-overhead
  decision heuristic (VSIDS).
  - **Why it is an exemplar:** it takes a core EDA/verification engine and wins through **careful
    engineering measured in solver runtime**, not a new theory — the archetypal DAC "make the tool
    actually fast on real instances" contribution, with impact that reshaped formal verification
    and beyond.
  - **Self-check:** is your contribution a mechanism whose advantage you can *measure* on standard
    instances, and does it generalize past the examples you chose?

### Technique + tool — combinational logic synthesis

- **Mishchenko, Chatterjee & Brayton, "DAG-Aware AIG Rewriting: A Fresh Look at Combinational
  Logic Synthesis," DAC 2006, pp. 532-535** (DOI 10.1145/1146909.1147048). Verified: dblp
  `conf/dac/MishchenkoCB06`, ACM DL (43rd DAC). Introduced And-Inverter-Graph rewriting in the
  public-domain **ABC** tool.
  - **Why it is an exemplar:** a named technique delivered as a **usable, open tool** and evaluated
    on standard circuits for area/delay — the classic DAC "idea you can run," adopted across the
    synthesis community.
  - **Self-check:** is your technique embodied in a tool a third party could point at their own
    netlists, evaluated on recognized benchmarks with real QoR (area/delay) numbers?

### Security analysis — logic locking / IP protection

- **Rajendran, Pino, Sinanoglu & Karri, "Security Analysis of Logic Obfuscation," DAC 2012,
  pp. 83-89** (DOI 10.1145/2228360.2228377). Verified: ACM DL (49th DAC), NYU Scholars. Showed a
  key-sensitization attack that deciphers obfuscated netlists, reshaping the logic-locking field.
  - **Why it is an exemplar:** a **concrete attack with an explicit threat model** that changed what
    the hardware-security community believed a defense was worth — DAC's security lane rewards
    demonstrated attacks/defenses, not asserted ones.
  - **Self-check:** does your security paper state a threat model precisely and *demonstrate* the
    attack or defense with measured effect, rather than arguing safety in the abstract?

### ML for EDA — GPU-accelerated placement

- **Lin, Dhar, Li, Ren, Khailany & Pan, "DREAMPlace: Deep Learning Toolkit-Enabled GPU Acceleration
  for Modern VLSI Placement," DAC 2019** (DOI 10.1145/3316781.3317803). Verified: ACM DL (56th
  DAC); **DAC 2019 Best Paper Award**. Cast analytical placement as neural-network training on
  PyTorch for large GPU speedups at preserved quality.
  - **Why it is an exemplar:** it uses a learning *toolkit* to accelerate a classical EDA task and
    reports **speedup at equal QoR versus a strong prior placer** — an ML-for-EDA contribution whose
    lesson is about design automation, not about a model (the `dac-topic-selection` model-swap test
    passes).
  - **Self-check:** if the ML machinery were swapped, would the **design-automation** advantage
    survive — and is the gain reported as QoR/runtime versus the strongest prior tool, not accuracy
    on a proxy?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified DAC exemplar | Edition | EDA subfield |
| --- | --- | --- | --- |
| Algorithm + tool (runtime) | Moskewicz et al., "Chaff" | DAC 2001 (38th) | SAT / verification |
| Technique + open tool | Mishchenko et al., "DAG-Aware AIG Rewriting" (ABC) | DAC 2006 (43rd) | Logic synthesis |
| Security attack analysis | Rajendran et al., "Security Analysis of Logic Obfuscation" | DAC 2012 (49th) | Hardware security |
| ML for EDA | Lin et al., "DREAMPlace" (Best Paper) | DAC 2019 (56th) | Physical design / ML |

> Four verified papers across four EDA subfields and four decades. Chaff and DREAMPlace also show
> DAC's throughline: **win in the field's own currency** — solver runtime, area/delay, attack
> effectiveness, placement speed at equal quality — on recognized benchmarks.

---

## Omitted for lack of clean DAC verification (do not attribute to DAC without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Trojan Detection using IC Fingerprinting" (Agrawal, Baktir, Karakoyunlu, Rohatgi, Sunar)** —
  verified to be **IEEE Symposium on Security and Privacy (S&P) 2007**, *not* DAC. A direct
  security-venue trap; listed only as a guardrail.
- **"EPIC: Ending Piracy of Integrated Circuits" (Roy, Koushanfar, Markov)** — the logic-locking
  paper the DAC 2012 analysis above attacks was published at **DATE 2008**, *not* DAC; cite each to
  its own venue.
- **"ABC: An Academic Industrial-Strength Verification Tool" (Brayton & Mishchenko)** — the ABC
  tool *paper* appeared at **CAV 2010** (a verification venue), a journal/tool track — not DAC;
  attribute the DAC 2006 rewriting paper to DAC and the tool paper to CAV separately.
- **RePlAce / ePlace placement line** — the canonical journal treatments appeared in **IEEE TCAD**,
  not DAC; do not label a TCAD placement paper as a DAC paper.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to a DAC
edition (not ICCAD, DATE, ASP-DAC, S&P, or a journal), then record authors, year, and DOI/pages, and
update the access-date header. When in doubt, omit. If web search is unavailable, add the row as
**待核实 / TO VERIFY** with **no attribution**.
