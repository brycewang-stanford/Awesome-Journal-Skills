# ECAI Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against the
> **official ECAI/PAIS Outstanding-Paper award pages** and **AIhub award posts**, and where
> possible **dblp**, to confirm it appeared at the **European Conference on Artificial
> Intelligence (ECAI)** or its co-located **PAIS** track — matching title, authors, and edition.
> Papers that could not be cleanly confirmed as ECAI (as opposed to IJCAI, AAAI, AAMAS, KR, or
> NeurIPS) were **omitted and documented below**. It is deliberately a short, verified list
> (a few verified > many guessed).
>
> **Sibling-confusion guard:** ECAI is **not** IJCAI, **not** AAAI, **not** AAMAS, **not** KR, and
> **not** a pure-ML venue (NeurIPS/ICML). A famous method or author does **not** prove an ECAI
> placement — general-AI work is often split across these venues. Each row was checked to be an
> ECAI or PAIS edition specifically (see omissions). Note the 2026 twist: **ECAI 2026 is the joint
> IJCAI-ECAI 2026**, so its accepted papers will index under **IJCAI**, not a standalone ECAI
> proceedings.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original in the IOS Press
> FAIA volume before citing anything. For ECAI-specific policy and the publisher/template regime,
> see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
poses a **well-defined AI problem**, backs it with **evidence proportional to the claim** (a
theorem and a construction, or a fair empirical comparison), and fits the argument inside ECAI's
**7-page body** — the ECAI bar (see
[`../../skills/ecai-writing-style/SKILL.md`](../../skills/ecai-writing-style/SKILL.md),
[`../../skills/ecai-topic-selection/SKILL.md`](../../skills/ecai-topic-selection/SKILL.md), and
[`../../skills/ecai-experiments/SKILL.md`](../../skills/ecai-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "ECAI-shaped."

The rows are recent **ECAI/PAIS Outstanding Paper** honorees, so they also model what the European
general-AI community rewards across its breadth — from classical planning and calibration theory
to fairness and deployed applications.

---

## By contribution shape

### Symbolic AI + search — classical planning

- **Wissow & Asai, "Scale-Adaptive Balancing of Exploration and Exploitation in Classical
  Planning," ECAI 2024.** Verified: ECAI 2024 Outstanding Paper Award (ecai2024.eu awards page;
  AIhub 2024-10-30). A heuristic-search planning contribution — adapting the exploration/
  exploitation trade-off in classical planning.
  - **Why it is an exemplar:** it advances a **core symbolic-AI problem** (classical planning)
    with a general, analysable mechanism rather than a one-domain tweak — squarely the kind of
    broad, foundational AI ECAI prizes and that distinguishes it from a pure-ML venue.
  - **Self-check:** is your contribution a general improvement to a foundational AI problem
    (planning, search, KR, reasoning) that a European AI audience would recognize as such?

### Learning theory — calibration

- **Komisarenko & Kull, "Improving Calibration by Relating Focal Loss, Temperature Scaling, and
  Properness," ECAI 2024.** Verified: ECAI 2024 Outstanding Paper Award (ecai2024.eu; AIhub).
  Relates focal loss, temperature scaling, and properness to improve probability calibration.
  - **Why it is an exemplar:** it is **ML with a theoretical spine** — a principled relationship
    among known objects, not a leaderboard number. ECAI rewards the *why*, delivered inside a
    tight page budget.
  - **Self-check:** does your ML paper contribute understanding (a relationship, a guarantee) that
    survives beyond one dataset, rather than only a benchmark delta?

### Trustworthy AI — fairness

- **Bendoukha, Kaaniche, Boudguiga & Sirdey, "FairCognizer: A Model for Accurate Predictions with
  Inherent Fairness Evaluation," ECAI 2024.** Verified: ECAI 2024 Outstanding Paper Award
  (ecai2024.eu; AIhub). A model that couples predictive accuracy with built-in fairness
  evaluation.
  - **Why it is an exemplar:** it tackles a **socially consequential AI property** (fairness) as a
    first-class design goal — a strong fit for ECAI's trustworthy/responsible-AI emphasis.
  - **Self-check:** is a trust property (fairness, robustness, transparency) engineered into the
    method and *evaluated*, not just discussed?

### Multi-agent learning — sample efficiency

- **Chen, Liu, Ba, Zhang, Ding & Li, "Selective Learning for Sample-Efficient Training in
  Multi-Agent Sparse Reward Tasks," ECAI 2023.** Verified: ECAI 2023 Outstanding Paper Award
  (ecai2023.eu; AIhub 2023-10-06). Improves sample efficiency in cooperative multi-agent RL under
  sparse rewards.
  - **Why it is an exemplar:** multi-agent systems are a European AI strength; the paper attacks a
    named, hard sub-problem (sparse-reward credit assignment) with a general mechanism.
  - **Self-check:** does your multi-agent contribution generalize across tasks, or is it tuned to
    one environment? (Note: dedicated MAS venues like AAMAS exist — see
    [`../../skills/ecai-topic-selection/SKILL.md`](../../skills/ecai-topic-selection/SKILL.md).)

### Applied / deployed AI (PAIS) — real-world impact

- **Molina, Ferreira, Veloso, Ribeiro & Gama, "More (Enough) Is Better: Towards Few-Shot Illegal
  Landfill Waste Segmentation," PAIS 2024.** Verified: PAIS 2024 Outstanding Paper Award
  (ecai2024.eu; AIhub). A few-shot segmentation approach for an environmental-monitoring
  application.
  - **Why it is an exemplar:** PAIS rewards a **credible deployment story on a real problem**, not
    a benchmark abstraction — the axis to lead with when routing to PAIS rather than the main
    track.
  - **Self-check:** does the paper demonstrate value on a real application with real constraints,
    such that a practitioner (not only a researcher) is the beneficiary?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified ECAI/PAIS exemplar | Edition | Method |
| --- | --- | --- | --- |
| Symbolic AI + search | Wissow & Asai, "Scale-Adaptive Balancing..." | ECAI 2024 | Classical planning |
| Learning theory | Komisarenko & Kull, "Improving Calibration..." | ECAI 2024 | Calibration theory |
| Trustworthy AI | Bendoukha et al., "FairCognizer" | ECAI 2024 | Fairness-aware modelling |
| Multi-agent learning | Chen et al., "Selective Learning..." | ECAI 2023 | Multi-agent RL |
| Applied / deployed AI | Molina et al., "...Illegal Landfill Waste Segmentation" | PAIS 2024 | Few-shot segmentation |

> Five verified papers across five contribution shapes span ECAI's actual breadth — planning and
> search on the symbolic side, calibration and fairness on the trustworthy-ML side, multi-agent
> learning, and a deployed PAIS application — the range that makes ECAI a *general* AI flagship
> rather than a single-subfield venue.

---

## Omitted for lack of clean ECAI verification (do not attribute to ECAI without re-checking)

To keep the list zero-hallucination, the following classes were **excluded**:

- **Canonical KR/planning/argumentation papers whose flagship placement was IJCAI, AAAI, or KR**
  rather than ECAI. Many foundational European-authored AI results appeared at IJCAI or AAAI; a
  European author is not proof of an ECAI placement. Confirm the venue string on dblp first.
- **Pure-ML landmark papers (NeurIPS/ICML).** Method fame does not imply an ECAI edition; omitted.
- **AAMAS multi-agent classics.** The dedicated MAS venue is AAMAS; do not relabel an AAMAS paper
  as ECAI merely because ECAI also publishes multi-agent work.
- **Any ECAI 2026 paper.** Because ECAI 2026 is the **joint IJCAI-ECAI 2026**, its papers will
  index under IJCAI's proceedings; treat attributions accordingly and re-verify per paper.

Before adding any paper, confirm it on **dblp** and the **IOS Press FAIA volume** (or the IJCAI
proceedings for 2026) by matching the venue string to an ECAI/PAIS edition (not IJCAI, AAAI,
AAMAS, KR, or a pure-ML venue), then record authors, edition, and pages, and update the
access-date header. When in doubt, omit. If web search is unavailable, add the row as
**待核实 / TO VERIFY** with **no attribution**.
