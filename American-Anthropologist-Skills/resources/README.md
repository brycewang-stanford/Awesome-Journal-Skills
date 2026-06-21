# American Anthropologist — Resources

Action-oriented resources for the *American Anthropologist* (AA) skill pack. The `skills/` give advice;
this directory lets an agent **act** — model an AA-style section and benchmark against web-verified
exemplars. Pair these with the relevant `skills/amanthro-*/SKILL.md`.

AA is the **four-field AAA flagship** (sociocultural, archaeology, biological/physical, linguistic, plus
reflexive/public anthropology). Its craft is **ethnographic and qualitative research, archival and
material analysis, reflexivity, and ethically accountable engagement with communities** — with
appropriate **quantitative/lab** methods in the biological and archaeological subfields. Accordingly,
**this pack ships no code kit**: there is no `resources/code/` directory and nothing to run. The
resources here are reading and modeling aids for prose, argument, evidence, and ethics.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an anthropology-article **introduction** in AA house style — question → four-field significance → reflexive argument → grounded finding, with the contribution stated early. Clearly-marked **fictional** article; no real community, site, or finding. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AA articles** organized by subfield × method (sociocultural ethnography, archaeology, biological, linguistic, reflexive). Positioning and craft cues only — no fabricated findings — with a sibling-journal confusion guard (AA ≠ AE / CA / *Current Anthropology*). |
| [`official-source-map.md`](official-source-map.md) | **AA-specific policy & facts:** owner (AAA) / publisher (Wiley), Research Exchange submission, the 8,000-word / 200-word caps, Chicago author-date with free-format, sections, anonymous review, ethics-of-care and AAA ethics principles, ORCID/APC metadata, alt-text/permissions, and live-check guardrails. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Find archives, primary-source databases, CAQDAS, transcription/paleography tools, GIS/mapping, lab/quant packages, and reference managers (Chicago author-date) matched to your subfield. |

## No empirical/code kit (predominantly qualitative venue)

Unlike the quantitative social-science packs in this repo, the AA pack does **not** vendor a
causal-inference code pipeline. AA is judged on the **quality and reflexivity of ethnographic and
qualitative evidence, the strength of the four-field argument, and ethical accountability** — not on
estimators or reproducibility scripts. For the **biological and archaeological** subfields, where
quantitative analysis does appear, two shared method references are linked **as background only** (they
are venue-neutral; always defer to this pack's skills and `official-source-map.md` for what AA
specifically requires):

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — common objections to quantitative designs, each with a preemption (relevant to biological/archaeological quant work only).
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — modern inference + reporting hygiene (effect sizes, uncertainty, multiple testing) for the quantitative subfields, **subject to** AA's ethics constraints in [`../skills/amanthro-transparency-and-data`](../skills/amanthro-transparency-and-data/SKILL.md).

If you came looking for a `code/` kit, there isn't one — and that is by design for a predominantly
ethnographic flagship.

## Suggested workflow

1. **Scope and frame** the project with
   [`../skills/amanthro-topic-selection`](../skills/amanthro-topic-selection/SKILL.md) (four-field
   significance) and stake the contribution with
   [`../skills/amanthro-literature-positioning`](../skills/amanthro-literature-positioning/SKILL.md).
2. **Build the argument and evidence** with
   [`../skills/amanthro-theory-building`](../skills/amanthro-theory-building/SKILL.md) and
   [`../skills/amanthro-research-design`](../skills/amanthro-research-design/SKILL.md), using
   [`external_tools.md`](external_tools.md) to locate and handle sources.
3. **Design ethics in early** with
   [`../skills/amanthro-transparency-and-data`](../skills/amanthro-transparency-and-data/SKILL.md) —
   consent, anonymization, heritage/repatriation, accountability.
4. **Draft the introduction and structure** by modeling
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), guided by
   [`../skills/amanthro-writing-style`](../skills/amanthro-writing-style/SKILL.md).
5. **Benchmark** against verified AA articles in [`exemplars/library.md`](exemplars/library.md), and
   confirm submission, length, citation, ethics, and review policy in
   [`official-source-map.md`](official-source-map.md).
