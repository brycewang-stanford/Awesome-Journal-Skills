> **Illustrative teaching example.** The paper, system, chemicals, and every number below are
> **fictional** and exist only to demonstrate Environmental Science & Technology (ES&T) house style.
> No real-paper facts are stated, and **no real policy or regulation is invented or attributed.**
> Corresponding skills: [`est-writing-style`](../../skills/est-writing-style/SKILL.md),
> [`est-topic-selection`](../../skills/est-topic-selection/SKILL.md),
> [`est-study-design`](../../skills/est-study-design/SKILL.md),
> [`est-data-analysis`](../../skills/est-data-analysis/SKILL.md), and
> [`est-figures-and-tables`](../../skills/est-figures-and-tables/SKILL.md).

# Worked Example: An ES&T-Style Abstract + Introduction (before → after)

This demonstrates the **ES&T house style** drawn from this pack's skill files: lead with
**environmental significance** (system, process, magnitude) — not method; write for a
**multidisciplinary** audience; build a single **TOC/abstract graphic** that *illustrates* the core
idea; and signal **methods rigor** (environmental relevance, controls, QA/QC, mass balance, honest
uncertainty) inside the prose. It targets a **Research Article** (`est-topic-selection`).

**Illustrative paper (fictional):** *"Photolytic Half-Life of a Quaternary-Ammonium Disinfectant in
Sunlit Surface Water Controls Its Downstream Persistence."* Fictional setting: a hypothetical
benzalkonium-type biocide ("Compound F") measured in a model river-water matrix under simulated
sunlight.

---

## Before (methods-first, no significance — typical first-draft abstract)

> We spiked Compound F into water and irradiated the samples in a solar simulator. Concentrations were
> measured by LC-MS/MS at several time points and the data were fitted to a first-order decay model. A
> rate constant was obtained. Degradation products were screened by high-resolution mass spectrometry.
> The results are discussed in the context of the literature. This work improves our understanding of
> the behavior of quaternary ammonium compounds and may be useful for future studies.

**What's wrong (against `est-writing-style` / `est-topic-selection`):**

- **Leads with method** ("We spiked... irradiated... measured by LC-MS/MS") — the named anti-pattern:
  *"an abstract full of methods but no significance or headline result."*
- **No environmental significance.** It never answers *"why does this matter for the environment?"* —
  no system, no process magnitude, no exposure or persistence consequence (`est-topic-selection`
  significance test).
- **No headline result with units** ("a rate constant was obtained" — which? how fast?).
- **Generic significance** ("improves our understanding... may be useful") — exactly the
  *"important for the environment" with no mechanism, system, or magnitude* anti-pattern.
- **Reads as routine data** — a measurement with no environmental question driving it
  (`est-topic-selection`: novel insight, not a catalog of measurements).
- **No rigor signals** — no mention of controls, QA/QC, replication, or mass balance, the things an
  ES&T reviewer scrutinizes (`est-study-design`, `est-data-analysis`).

---

## After (ES&T arc — environmental significance first, headline magnitude, rigor signaled)

> **Quaternary-ammonium disinfectants reach surface waters in growing quantities, yet how long they
> persist once there is poorly constrained.** We show that sunlight, not biodegradation, sets the fate
> of one such biocide ("Compound F"): under environmentally relevant summer irradiance and river-water
> chemistry, it phototransforms with a half-life of **4.2 ± 0.6 h** (n = 3; 95% CI), an order of
> magnitude faster than its reported dark/biotic loss. *(environmental significance + headline
> magnitude + units, in the first breath.)*
>
> Constraining this is hard because apparent "degradation" in a beaker can be sorption, volatilization,
> or hydrolysis masquerading as transformation. We isolate the photolytic pathway with dark, abiotic,
> and quencher controls, and we **close a 94 ± 5% mass balance** across parent loss and identified
> products — so the reported rate reflects photochemistry, not unaccounted losses. *(why it is hard +
> controls + mass balance — the rigor an ES&T reviewer checks; see `est-study-design`,
> `est-data-analysis`.)*
>
> Experiments used a solar simulator calibrated to a defined latitude/season, a natural-organic-matter
> river matrix at environmentally realistic pH and ionic strength, and triplicate reactors; analytes
> were quantified by LC-MS/MS with method blanks, matrix-spike recoveries of 88–104%, and a reported
> LOQ, with non-detects handled explicitly. *(environmental relevance + QA/QC + honest uncertainty,
> stated compactly.)*
>
> The environmental implication is concrete: because photolysis dominates, Compound F should persist far
> longer in **turbid, shaded, or under-ice waters** than in clear sunlit rivers — so exposure is
> governed by **light availability**, not by the compound's intrinsic stability. *(environmental
> implications framing — interprets the result for a real system, per `est-writing-style`.)* This
> reframes persistence for this biocide class from a single fixed property to a **light-dependent
> variable**, with measurable consequences for where downstream organisms are exposed.

**TOC / abstract graphic (the visual abstract, per `est-figures-and-tables`):** a single panel
contrasting two river reaches — a clear sunlit reach where Compound F decays to near-zero within hours,
and a shaded/turbid reach where it persists downstream — with a small inset decay curve (C/C0 vs.
hours) annotated with the 4.2 h half-life. It *illustrates the core idea* (light controls fate) rather
than cloning an in-text figure.

---

## Why the "after" meets the ES&T bar

Mapped to the skill checklists:

- **Significance stated early** — the abstract and the implication paragraph both answer *"why for the
  environment?"* concretely (system: surface waters; process: photolysis; magnitude: 4.2 h half-life)
  (`est-writing-style`: significance up front; `est-topic-selection`: environmental-significance test).
- **Headline result with units, with honest uncertainty** — `4.2 ± 0.6 h (n = 3; 95% CI)` appears
  immediately, not a vague "a rate constant was obtained" (`est-data-analysis`: magnitude + uncertainty
  + n + units).
- **Methods rigor signaled in prose** — abiotic/dark/quencher **controls** isolate the mechanism, a
  **94 ± 5% mass balance** closes the budget, and **QA/QC** (blanks, 88–104% recoveries, LOQ,
  non-detect handling) is named — the design and analysis failure modes ES&T reviewers probe
  (`est-study-design`, `est-data-analysis`).
- **Environmental relevance** — realistic irradiance, NOM matrix, pH/ionic strength, and replication,
  not an idealized lab spike presented as field-relevant (`est-study-design` relevance principle;
  `est-topic-selection` anti-pattern).
- **Environmental Implications framing** — the discussion interprets the result for turbid/shaded/
  under-ice waters instead of restating the number (`est-writing-style`: implications, not a
  results-restatement).
- **TOC graphic is a true visual abstract** — required for Research Articles and designed to *illustrate
  the idea*, not duplicate Figure 1 (`est-figures-and-tables`: the TOC-graphic rule).
- **Multidisciplinary, jargon-controlled** — a chemist, engineer, toxicologist, and policy reader can
  all follow the claim; specialist terms are introduced in plain language (`est-writing-style`:
  write for the broad audience).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ES&T papers**
> whose abstracts execute this significance-first arc across methods, and the pack's
> [`../official-source-map.md`](../official-source-map.md) for ES&T article types, the TOC-art mandate,
> and ACS submission policy.
