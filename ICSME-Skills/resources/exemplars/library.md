# IEEE ICSME Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and **IEEE Xplore** to confirm it appeared at the **IEEE International Conference on
> Software Maintenance (ICSM)** or its successor **Software Maintenance and Evolution (ICSME)** —
> matching title, author list, year, and venue string. Several are **ICSME Most Influential Paper
> (10-Year Retrospective)** honorees, cross-checked against the awarding institutions' announcements.
> Papers that could not be cleanly confirmed as ICSM/ICSME (as opposed to ICSE, FSE, MSR, SANER,
> SCAM, or a journal such as TSE/EMSE) were **omitted and documented below**. It is deliberately a
> short, verified list (5 verified > 15 guessed).
>
> **Naming note:** the venue was **ICSM** through 2013 and **ICSME** from 2014 (when "and Evolution"
> was added). A 10-year MIP awarded *at ICSME 20XX* honors a paper published *at ICSM 20(XX-10)*.
>
> **Sibling-confusion guard:** ICSME is **not** ICSE, **not** FSE, **not** MSR, **not** SANER, and
> **not** a PL/journal venue. Several canonical maintenance tools and metrics were introduced at
> those venues instead; a famous author or a familiar topic does **not** prove an ICSM/ICSME
> placement. Each row was checked to be an ICSM/ICSME edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original on IEEE Xplore
> before citing anything. For ICSME-specific policy and the single-round model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **maintenance/evolution problem practitioners recognize**, backs it with **evidence
proportional to the claim** on **real evolving systems**, and names its **threats to validity** —
the ICSME bar (see [`../../skills/icsme-writing-style/SKILL.md`](../../skills/icsme-writing-style/SKILL.md),
[`../../skills/icsme-topic-selection/SKILL.md`](../../skills/icsme-topic-selection/SKILL.md), and
[`../../skills/icsme-experiments/SKILL.md`](../../skills/icsme-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "ICSME-shaped."

---

## By contribution shape

### Technique + tool — refactoring reconstruction from evolution

- **Kim, Prete, Rachatasumrit & Sudan, "Template-Based Reconstruction of Complex Refactorings,"
  ICSM 2010.** Verified: dblp / IEEE Xplore; **ICSME 2020 10-Year Retrospective Most Influential
  Paper**. Reconstructs complex, composite refactorings from two program versions using change
  templates.
  - **Why it is an exemplar:** it takes a core evolution activity — understanding how code was
    refactored across versions — and turns it into a **general, tool-supported technique** evaluated
    on real systems' histories. The problem is legible to any maintainer and the method travels
    beyond one codebase.
  - **Self-check:** does your technique operate on software *as it changes over versions*, and is it
    embodied in a tool a third party could point at their own history?

### Empirical study — API stability and evolution

- **McDonnell, Ray & Kim, "An Empirical Study of API Stability and Adoption in the Android
  Ecosystem," ICSM 2013.** Verified: dblp / IEEE Xplore; **ICSME 2023 Most Influential Paper**.
  Mines how fast Android APIs change and how quickly client code adopts the changes.
  - **Why it is an exemplar:** it measures an **evolution phenomenon practitioners feel** — churning
    platform APIs forcing client maintenance — at ecosystem scale from real repositories, and draws
    conclusions about adoption lag. Pure empirical evolution insight.
  - **Self-check:** does your study change what the community believes about how real software
    *evolves*, with a mined dataset and criteria a reviewer could scrutinize?

### Empirical / human-factors study — mining Q&A for maintenance knowledge

- **Nasehi, Sillito, Maurer & Burns, "What Makes a Good Code Example? A Study of Programming Q&A in
  StackOverflow," ICSM 2012.** Verified: dblp / IEEE Xplore; **ICSME 2022 Most Influential Paper**.
  Qualitatively studies what makes code examples useful to developers.
  - **Why it is an exemplar:** it studies the **knowledge maintainers actually consult**, with a
    disciplined qualitative method, and yields guidance that outlived the specific platform snapshot.
  - **Self-check:** does your study use a sound coding methodology with agreement, and does the
    finding help someone maintaining or comprehending real software?

### Empirical methodology — questioning a received assumption

- **Bettenburg, Premraj, Zimmermann & Kim, "Duplicate Bug Reports Considered Harmful ... Really?"
  ICSM 2008.** Verified: dblp / IEEE Xplore; **ICSME 2018 Most Influential Paper**. Tests the common
  belief that duplicate bug reports are purely wasteful.
  - **Why it is an exemplar:** it **interrogates an assumption the maintenance community relied on**
    and reports a counter-intuitive, evidence-backed answer — the ICSME mode of honest re-examination
    that the modern **RENE** track institutionalizes.
  - **Self-check:** does your paper strengthen or overturn a widely held maintenance belief, with an
    analysis whose data and confounds are laid out explicitly?

### Empirical measurement — code smells vs. maintainability

- **Yamashita & Moonen, "Do Code Smells Reflect Important Maintainability Aspects?", ICSM 2012**
  (DOI 10.1109/ICSM.2012.6405287). Verified: IEEE Xplore / dblp. Relates detected code smells to the
  maintainability factors developers deem important.
  - **Why it is an exemplar:** it validates a **measurement the field leans on** (smells as a proxy
    for maintainability) against what practitioners actually care about — improving how everyone
    evaluates maintainability, not one tool's score.
  - **Self-check:** does your paper question or validate a widely used maintenance metric, with the
    construct-validity argument made explicit?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified ICSM/ICSME exemplar | Edition | Method |
| --- | --- | --- | --- |
| Technique + tool | Kim et al., "Template-Based Reconstruction of Complex Refactorings" | ICSM 2010 | Change-template analysis |
| Empirical evolution study | McDonnell, Ray & Kim, "API Stability and Adoption ... Android" | ICSM 2013 | Repository mining |
| Empirical / human factors | Nasehi et al., "What Makes a Good Code Example?" | ICSM 2012 | Qualitative study |
| Empirical methodology | Bettenburg et al., "Duplicate Bug Reports ... Really?" | ICSM 2008 | Controlled empirical study |
| Empirical measurement | Yamashita & Moonen, "Do Code Smells Reflect ... Maintainability?" | ICSM 2012 | Correlational study |

> Five verified papers across five contribution shapes. Four carry ICSME Most Influential Paper
> recognition, and the Bettenburg row also models the venue's prized "question the assumption" mode
> that the RENE track now rewards directly.

---

## Omitted for lack of clean ICSM/ICSME verification (do not attribute without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Chidamber & Kemerer object-oriented metrics** — the founding metrics paper is **IEEE TSE
  (1994)**, a journal, not ICSM. A classic maintenance-metrics trap; cite the TSE article, not ICSM.
- **DECOR / Moha et al. code-smell detection** — the definitive treatment appeared in **IEEE TSE
  (2010)**, not ICSM; omitted to avoid venue misattribution.
- **Fowler's *Refactoring*** — a **book**, not a conference paper; not an ICSM/ICSME placement.
- **Zimmermann et al. "Mining Version Histories to Guide Software Changes"** — a foundational mining
  paper published at **ICSE (2004)** and later TSE, *not* ICSM; a direct sibling-venue trap.
- **Palomba et al. code-smell / change-history detection line** — spread across **ICSME, ASE, and
  TSE**; confirm the exact edition per paper before attributing any single result to ICSME.

Before adding any paper, confirm it on **dblp** (`db/conf/icsm`) and **IEEE Xplore** by matching the
venue string to an ICSM/ICSME edition (not ICSE, FSE, MSR, SANER, SCAM, or a journal), then record
authors, year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search
is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
