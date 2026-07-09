# ACM FAccT Exemplars Library (contribution shape × discipline)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`db/conf/fat`), the **ACM Digital Library**, and — for the 2018 inaugural edition —
> **PMLR vol 81**, to confirm it appeared at the **ACM Conference on Fairness, Accountability, and
> Transparency (FAccT, formerly FAT\*)** — matching title, author list, year, and venue string.
> Papers that could not be cleanly confirmed as FAccT/FAT\* (as opposed to a workshop, a journal, or
> a pure-ML/HCI venue) were **omitted and documented below**. It is deliberately a short, verified
> list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** FAccT is **not** NeurIPS/ICML, **not** CHI, **not** a law review, and
> **not** the pre-conference **FAT/ML workshop** (`fatml.org`) or the AIES conference. A famous
> responsible-AI paper is not automatically a FAccT paper — several foundational ones appeared in a
> journal or a workshop instead (see omissions). Note also the venue **lineage**: FAT\* 2018 (New
> York) published in **PMLR**, FAT\* 2019 (Atlanta) was the first **ACM DL** proceedings, and the
> name changed to **FAccT** after 2020.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original on ACM DL / PMLR
> before citing anything. For FAccT-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × discipline** is closest to yours, then study how that
paper makes a **fairness, accountability, or transparency question the first-class contribution**,
backs it with **evidence proportional to the claim** (held to its own discipline's rigor), and is
honest about **limitations and adverse impacts** — the FAccT bar (see
[`../../skills/facct-writing-style/SKILL.md`](../../skills/facct-writing-style/SKILL.md),
[`../../skills/facct-topic-selection/SKILL.md`](../../skills/facct-topic-selection/SKILL.md), and
[`../../skills/facct-experiments/SKILL.md`](../../skills/facct-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "FAccT-shaped."

---

## By contribution shape

### Empirical audit — disaggregated performance disparity

- **Buolamwini & Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender
  Classification," FAT\* 2018.** Verified: PMLR vol 81, pp. 77-91 (the inaugural FAT\* proceedings
  were published in PMLR; conference held New York, Feb 2018). Audited commercial gender-classifiers
  and showed the largest error rates fell on darker-skinned women.
  - **Why it is an exemplar:** it turns a fairness concern into a **measured, disaggregated,
    intersectional** finding on real commercial systems — the archetypal FAccT audit, where the
    contribution is *who is harmed and by how much*, not a new model.
  - **Self-check:** are your results disaggregated by protected/affected subgroup (and intersections),
    with the worst-affected group visible rather than hidden in an aggregate?

### Documentation / accountability infrastructure — model reporting

- **Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji & Gebru, "Model Cards for
  Model Reporting," FAT\* 2019** (DOI 10.1145/3287560.3287596). Verified: ACM DL / dblp. Proposed a
  standardized short document reporting a model's intended use and **disaggregated** evaluation.
  - **Why it is an exemplar:** it contributes **accountability infrastructure** the field adopted —
    a genre, not a result — that changed how models are documented and released.
  - **Self-check:** does your contribution give the community a reusable way to be more transparent
    or accountable, documented well enough that others can actually adopt it?

### Critical / conceptual — reframing a taken-for-granted practice

- **Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots: Can Language
  Models Be Too Big?", FAccT 2021, pp. 610-623.** Verified: ACM DL / dblp.
  - **Why it is an exemplar:** a **critical, argument-driven** paper that reframed the risks of ever-
    larger language models (environmental cost, data harms, illusory understanding) — showing that a
    rigorous *conceptual* contribution is fully first-class at FAccT, not a second-class option.
  - **Self-check:** does your argument engage the technical artifact seriously (not just gesture at
    it) and change what the community takes for granted — with the reasoning laid out to withstand a
    mixed panel?

### Sociotechnical case study — algorithm-assisted decisions in an institution

- **Chouldechova, Benavides-Prado, Fialko & Vaithianathan, "A case study of algorithm-assisted
  decision making in child maltreatment hotline screening decisions," FAT\* 2018** (Best Paper).
  Verified: PMLR vol 81. Studied a predictive-risk tool in real child-welfare screening.
  - **Why it is an exemplar:** it grounds fairness and accountability in a **real institutional
    decision** with real stakes, combining quantitative analysis with the deployment context — the
    sociotechnical mode FAccT prizes and the inaugural edition's Best Paper.
  - **Self-check:** do you understand the actual decision context and the people affected, rather
    than treating the system as an abstract classifier?

### Documentation / tooling — transparent dataset documentation

- **Pushkarna, Zaldivar & Kjartansson, "Data Cards: Purposeful and Transparent Dataset Documentation
  for Responsible AI," FAccT 2022** (DOI 10.1145/3531146.3533231). Verified: ACM DL / dblp.
  - **Why it is an exemplar:** it extends the datasheet/model-card lineage into a **structured,
    studied** dataset-documentation framework — accountability infrastructure evaluated for real use,
    not just proposed.
  - **Self-check:** if your contribution is a documentation or transparency artifact, did you study
    whether it actually helps a real audience, rather than assuming it does?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified FAccT/FAT* exemplar | Edition | Discipline / method |
| --- | --- | --- | --- |
| Empirical audit | Buolamwini & Gebru, "Gender Shades" | FAT* 2018 (PMLR) | Disaggregated commercial-system audit |
| Documentation infrastructure | Mitchell et al., "Model Cards for Model Reporting" | FAT* 2019 | Reporting framework |
| Critical / conceptual | Bender et al., "Stochastic Parrots" | FAccT 2021 | Argument / position |
| Sociotechnical case study | Chouldechova et al., "Child maltreatment hotline screening" | FAT* 2018 (Best Paper) | Institutional case study |
| Documentation / tooling | Pushkarna et al., "Data Cards" | FAccT 2022 | Studied documentation framework |

> Five verified papers across five contribution shapes and disciplines. Together they model FAccT's
> pluralism: an audit, two documentation contributions, a critical argument, and an institutional
> case study are **all** first-class here — as long as fairness, accountability, or transparency is
> the contribution and the work meets its own discipline's rigor.

---

## Omitted for lack of clean FAccT verification (do not attribute to FAccT without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the venue confusions the header warns about:

- **"Datasheets for Datasets" (Gebru, Morgenstern, Vecchione, Wortman Vaughan, Wallach, Daumé,
  Crawford)** — widely associated with FAccT's documentation culture, but it was circulated as an
  **arXiv (2018)** working paper / FAT/ML workshop piece and later published in **Communications of
  the ACM (2021)** — **not** a FAccT/FAT\* proceedings paper. Cite it to CACM, not FAccT.
- **The ProPublica "Machine Bias" COMPAS analysis** — journalism (ProPublica, 2016), not a FAccT
  paper; the surrounding fairness-metric debate produced separate papers, some at FAT\*/FAccT and
  some elsewhere — verify each individually.
- **Foundational fairness-in-ML papers (e.g. equalized-odds / calibration formulations)** — several
  first appeared at **NeurIPS/ICML or on arXiv**, not FAccT; a fairness topic does not make a paper a
  FAccT placement.
- **AIES papers** — the AAAI/ACM Conference on AI, Ethics, and Society is a distinct sibling venue;
  do not merge its proceedings with FAccT's.

Before adding any paper, confirm it on **dblp** (`db/conf/fat`) and **ACM DL** (or **PMLR vol 81**
for FAT\* 2018) by matching the venue string to a FAccT/FAT\* edition — not a workshop, a journal, or
a pure-ML/HCI venue — then record authors, year, and DOI/pages, and update the access-date header.
When in doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
