> **Illustrative teaching example.** The paper, molecules, axis, cell lines, models, and every number
> below are **fictional** and exist only to demonstrate Cancer Cell (Cell Press) house style. No real
> paper, gene, or clinical fact is asserted, and no policy is invented. Corresponding skills:
> [`cc-structured-abstract`](../../skills/cc-structured-abstract/SKILL.md),
> [`cc-writing-style`](../../skills/cc-writing-style/SKILL.md), and
> [`cc-scope-fit`](../../skills/cc-scope-fit/SKILL.md).

# Worked Example: A Cancer Cell Summary + Opening (before → after)

This demonstrates the **Cancer Cell front-matter arc** from `cc-structured-abstract` and the
**claim-calibration discipline** from `cc-writing-style`. The Cell Press Summary is a single-paragraph
**mechanistic arc**: *context/gap → approach (orthogonal systems) → core finding (mechanism, with
direction) → validation in vivo and/or in human data → calibrated translational significance.* It
**leads with the discovery, not the background**, and never lets a verb outrun its evidence
(`cc-writing-style` claim-calibration table).

The two-pillar scope bar from `cc-scope-fit` applies throughout: a Cancer Cell story needs
**mechanistic depth** *and* **translational relevance** anchored in patient data — a phenotype or
correlation alone is off-fit.

**Illustrative paper (fictional):** *"The KRAS-driven kinase MARK7 sustains a fibroblast-to-tumor lactate
relay that licenses immunotherapy resistance in pancreatic cancer."* Fictional axis: MARK7 → CAF lactate
export → CD8⁺ T cell exclusion, studied in cell lines, autochthonous mouse tumors, PDX, and a fictional
patient cohort.

---

## Before (background-heavy Summary that buries the finding)

> Pancreatic cancer is one of the most lethal malignancies, with a five-year survival rate that remains
> dismal despite decades of research. The tumor microenvironment is known to be highly complex and
> immunosuppressive, and immunotherapy has largely failed in this disease. Cancer-associated fibroblasts
> (CAFs) are abundant and have been implicated in many processes. Here we used RNA sequencing, cell
> culture, mouse models, and patient samples to study novel mechanisms of resistance. We identify the
> kinase MARK7 and show it plays an important role. Our findings suggest MARK7 may be a promising new
> therapeutic target and could have important clinical implications for patients.

**What's wrong (against `cc-structured-abstract` / `cc-writing-style` / `cc-scope-fit`):**

- **Leads with three sentences of textbook background** ("one of the most lethal…," "is known to be
  highly complex") and buries the discovery — the named anti-pattern in `cc-structured-abstract`
  ("Background-heavy Summary that buries the finding").
- **No mechanism with direction.** "Plays an important role" is exactly the vague phrasing
  `cc-structured-abstract` forbids; the reader never learns *what regulates what*.
- **Approach is an assay catalog** ("RNA sequencing, cell culture, mouse models") rather than the
  orthogonal-validation logic Cancer Cell wants (cells + in vivo + human).
- **Hype and overclaim:** "novel," "promising new therapeutic target," "important clinical implications"
  — `cc-writing-style` bans hype words and calling a target "therapeutic" without in vivo efficacy or
  human evidence; here the verb outruns the evidence.
- **No calibrated significance line** tied to the actual data (vulnerability vs. biomarker vs. therapy).

---

## After (Cancer Cell mechanistic arc — discovery first, calibrated translation)

> Immunotherapy fails in most pancreatic ductal adenocarcinoma (PDAC), yet why the stroma excludes CD8⁺
> T cells mechanistically is unresolved. *(context + gap, one sentence.)* Using paired tumor and
> stromal profiling across PDAC cell lines, autochthonous *Kras*-driven mouse tumors, patient-derived
> xenografts, and a 214-patient cohort, *(approach — orthogonal systems, not an assay list)* we find
> that tumor-cell **MARK7 is required for a fibroblast-to-tumor lactate relay**: MARK7 signaling induces
> CAFs to export lactate, which acidifies the niche and excludes cytotoxic T cells. *(core finding — the
> axis, with direction.)* **In vivo, MARK7 loss restored intratumoral CD8⁺ T cell infiltration and
> sensitized autochthonous tumors to checkpoint blockade**, and in the patient cohort high MARK7–lactate
> signatures were **associated with** T cell exclusion and shorter survival. *(validation: in vivo
> causal perturbation + human association, verbs matched to each.)* MARK7 thus **represents a candidate
> vulnerability for combination with immune checkpoint blockade** in stroma-rich PDAC, a hypothesis the
> in vivo efficacy and human association support but that requires clinical testing. *(calibrated
> significance — "candidate vulnerability," not "proven therapy.")*

### Opening paragraph of the Introduction (concise; gap → hypothesis, not a review)

> The PDAC stroma is densely fibrotic and immunosuppressive, and CAFs shape T cell access to tumor
> cells. How tumor-intrinsic signaling instructs CAFs to enforce that exclusion — and whether that link
> is druggable — remains unclear. *(the gap, stated as a mechanistic unknown, per `cc-scope-fit`.)* We
> hypothesized that a tumor-cell kinase coordinates a metabolic crosstalk that licenses immune evasion,
> and that interrupting it would re-open the tumor to cytotoxic T cells. *(ends on a clear, testable
> hypothesis — the Introduction's job in `cc-writing-style`.)*

---

## Why the "after" meets the Cancer Cell bar

Mapped to the skill checklists:

- **Summary leads with the discovery and names the mechanism with direction** — MARK7 → CAF lactate
  export → T cell exclusion, in the opening breath, not after a background ramp
  (`cc-structured-abstract`: "Lead with the discovery, not the background").
- **Orthogonal validation is the approach** — cells + autochthonous mouse + PDX + human cohort, the
  two-pillar pattern in `cc-scope-fit` ("validated in ≥2 orthogonal systems, ideally including
  human/patient data").
- **Verbs are calibrated to evidence** (`cc-writing-style` table): "**required for**" for the in-system
  perturbation, "**restored / sensitized**" for the in vivo causal result, "**associated with**" for the
  human correlation, and "**candidate vulnerability**" — *not* "therapeutic target" — for the
  translational line, because efficacy is preclinical.
- **Significance is proportionate** — it states a vulnerability and explicitly flags that clinical
  testing is still required (`cc-writing-style`: state limitations; no clinical promise beyond the data).
- **Hype removed** — no "novel," "promising," "first," "important implications"; the data carry the
  weight (`cc-structured-abstract` and `cc-writing-style` anti-hype rules).
- **Nomenclature discipline** — gene italicized (*Kras* for mouse), protein roman (MARK7), species
  capitalization correct (`cc-writing-style` nomenclature rules).
- **Front matter would stay consistent** — a Highlights list and eTOC blurb built from this Summary
  would each be a *result* ordered mechanism → validation → translation, matching the paper's actual
  claims and `n` (`cc-structured-abstract` checklist).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified Cancer Cell
> papers** whose Summaries execute this discovery-first, calibrated arc, and
> [`../README.md`](../README.md) for how this fits the rest of the pack.
