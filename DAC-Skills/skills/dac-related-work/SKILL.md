---
name: dac-related-work
description: Use when writing or auditing the related-work and positioning of an ACM/IEEE Design Automation Conference (DAC) Research Manuscript, covering the EDA literature lanes (DAC/ICCAD/DATE/ASP-DAC/TCAD/TODAES), delta-first positioning against the strongest prior tool, honest benchmark-suite lineage, and third-person self-citation under double-blind review within the six-page budget.
---

# DAC Related Work

Position the paper against the EDA literature a DAC reviewer already knows. At six double-column
pages, related work is not a survey — it is a **delta statement**: here is the best prior technique
for this design task, here is precisely what it cannot do, here is what we add, measured in QoR.
DAC reviewers are drawn from exactly the subcommittee whose prior work you are extending, so an
incomplete or unfair positioning is caught immediately.

## The EDA literature lanes

Cover the lanes your contribution touches; do not pad with distant ones:

- **The top EDA venues** — DAC, **ICCAD**, **DATE**, **ASP-DAC** — the conference record of your
  problem. A physical-design paper that cites no recent DAC/ICCAD placement work reads as
  disconnected.
- **The EDA journals** — **IEEE TCAD** (Transactions on CAD) and **ACM TODAES** — where the extended
  and most authoritative versions of techniques live; cite the journal version when it is the
  canonical reference.
- **Adjacent communities when relevant** — ISCA/MICRO/HPCA for architecture-facing work, ITC/VTS for
  test, ISSCC/CICC for circuits, and the ML venues (NeurIPS/ICML/ICLR) *only* when your ML-for-EDA
  method genuinely builds on a learning advance.
- **The benchmark and tool lineage** — the paper introducing the suite you evaluate on (ISPD
  contests, EPFL benchmarks, ISCAS/ITC circuits, TAU contest, CircuitNet) and the open flow you use
  (OpenROAD). Miscrediting a benchmark's origin is an easy, avoidable reviewer irritant.

## Delta-first positioning

For each closely related technique, write the comparison in one move: **what it does → its specific
limitation → your advance**.

- Weak: "Prior work has studied placement extensively [3-15]." (A citation dump; it positions
  nothing.)
- Strong: "The analytic placer [8] minimizes wirelength but degrades on macro-heavy designs because
  it treats macros as movable cells; we handle macros with [mechanism], cutting congestion by X% on
  the macro-dominated ISPD circuits."

The reviewer's implicit question is always "why is this not just [the obvious prior tool] plus
tuning?" Answer it explicitly, early, and in QoR terms.

## Name the strongest baseline as the thing to beat

DAC papers are won and lost on the baseline. In related work, identify the **current state of the
art** for your exact task and commit to comparing against it in the evaluation. Comparing only to an
old or weak method — while a stronger, well-known tool exists and goes uncited — is the fastest way
to a reject, because the assigned reviewer very likely authored or uses that stronger tool.

## Honest benchmark and reproducibility lineage

- Credit the **benchmark suite** correctly and use its **standard metrics**; reporting a nonstandard
  metric on a standard suite invites "why not the usual QoR numbers?"
- If you use an **open-source flow** (OpenROAD, ABC, Yosys) or a public dataset (CircuitNet), cite it
  and state the version — this both positions you honestly and helps reproducibility.
- Distinguish **contest results** (ISPD/TAU/CAD-contest rankings) from peer-reviewed papers when you
  invoke them as prior art.

## Third-person self-citation under double-blind

Cite your own prior papers as if written by others: "Prior work [7] proposed..." not "in our
previous paper [7] we proposed...". A first-person self-citation de-anonymizes the submission. If
your new paper is an extension of your own DAC/ICCAD paper, position the delta in the third person
and let the camera-ready restore ownership.

## Fitting related work into six pages

- No standalone two-column "Section 2: Related Work" wall if space is tight — **weave** positioning
  into the introduction and method, citing at the point of contrast.
- Group distant references (a whole subfield you merely acknowledge) into a single sentence with a
  bundled citation; spend individual sentences only on the techniques you actually beat or build on.

## Output format

```text
[Lanes covered]   DAC/ICCAD/DATE/ASP-DAC + TCAD/TODAES + benchmark/tool lineage present?
[Strongest baseline] named and committed to in the evaluation? yes/no
[Delta statements] each close technique -> its limitation -> your QoR advance? yes/no
[Benchmark credit] suite + version + standard metrics correctly attributed? yes/no
[Anonymity]        self-citations third-person? yes/no
[Space]            positioning woven to fit the six-page budget? yes/no
```
