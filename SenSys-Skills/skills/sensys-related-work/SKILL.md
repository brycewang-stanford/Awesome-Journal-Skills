---
name: sensys-related-work
description: Use when positioning a SenSys paper against the sensing, embedded, IoT, and on-device-AI literature — sweeping the right venue lanes after the SenSys/IPSN/IoTDI merger, proving each citation's venue via dblp/ACM DL against the MobiCom/NSDI/IPSN traps, distinguishing your mechanism from the nearest prior system, and self-citing blind-safely.
---

# SenSys Related Work

A SenSys related-work section has one job: show that you know the **closest prior systems** and
can name, precisely, what your mechanism does that theirs does not. Vague "prior work is limited"
draws blood at a systems venue where reviewers built that prior work. The 2026 merger widened the
lanes you must sweep — IPSN and IoTDI literature is now sibling canon, not a separate world.

## Sweep the right lanes

After the merger, a thorough sweep covers more ground than a pre-2026 SenSys paper did:

| Lane | Where it lives | What to look for |
|---|---|---|
| Low-power networked sensing | SenSys, **IPSN** (pre-2026) | The primitive/service your mechanism competes with |
| IoT design & deployment | SenSys, **IoTDI** (pre-2026) | Deployment methodology and system architecture priors |
| On-device / embedded AI | SenSys, TinyML venues, embedded-ML tracks | Footprint/latency baselines on real MCUs |
| Mobile & wireless systems | MobiCom, MobiSys | Adjacent mechanisms you must distinguish from, not claim |
| Sensing algorithms / DSP | Signal-processing venues | The math you build on but do not re-derive |

## Prove the venue before you cite it

The sensing canon is the most-misfiled literature in systems. Directed diffusion is **MobiCom**,
not SenSys; Glossy is **IPSN**; TinyDB's core is **OSDI/SIGMOD**. Getting a venue wrong in related
work signals you do not know the field. Verify every load-bearing citation:

```text
For each key citation:
  1. Look it up on dblp (dblp.org) — read the venue key: conf/sensys? conf/ipsn? conf/mobicom?
  2. Cross-check the ACM DL / proceedings for year and edition.
  3. Record venue + year; if a rendering is unavailable, mark 待核实 — do NOT guess.
```

Post-merger nuance: a paper's *community* may now be part of SenSys, but its **historical venue is
unchanged**. A 2011 IPSN paper is still cited as IPSN 2011, even though IPSN merged into SenSys in
2026. Do not retroactively relabel.

## Distinguish from the closest system, concretely

The paragraph that matters most contrasts you with the **single nearest prior system**. Make it
mechanism-level and, where possible, measurable:

```text
Weak:   "Unlike prior work, our system is more efficient."
Strong: "CTP-style collection assumes a persistent radio; our node duty-cycles the radio to a
         1% budget and recovers routing state from non-volatile memory after each sleep, trading
         a stated latency increase for a measured order-of-magnitude energy reduction (§4.2)."
```

The strong version names the prior mechanism, the specific difference, and the trade-off with a
pointer — exactly what a systems reviewer checks (`sensys-writing-style`).

## Self-cite without breaking blind

Double-blind still applies to related work:

- Cite your own prior papers in the **third person** ("Prior work [12] showed...", never "our
  earlier work [12]").
- Do not drop a relevant citation to preserve anonymity — omission is itself a signal and hurts
  the positioning.
- Keep any comparison to your own unpublished/concurrent work blind and factual.

## Position, do not inflate

A SenSys reviewer distrusts a related-work section that makes every prior system sound broken.
Credit what prior systems got right, then carve the specific gap you fill. A paper that respects
its lineage and names one crisp delta is more credible than one that claims to obsolete the field.

## Output format

```text
[Lanes]    which venue lanes swept (SenSys/IPSN/IoTDI/MobiCom/DSP) — gaps
[Venues]   citations with unverified venues — listed for dblp/ACM DL check
[Nearest]  the closest prior system + the concrete, measurable delta stated
[Blind]    self-citations in third person? pass/gap
[Open]     the one prior system a reviewer will expect and whether it is addressed
```
