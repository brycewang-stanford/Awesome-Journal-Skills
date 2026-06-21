# Current Anthropology — Resources

Action-oriented resources for the *Current Anthropology* (CA) skill pack. The `skills/` give advice; this
directory lets an agent **act** — model a CA-style section and benchmark against web-verified exemplars.
Pair these with the relevant `skills/curranthro-*/SKILL.md`.

CA is the transnational, **all-subfields** journal (sociocultural, archaeology, biological/physical,
linguistic, plus ethnohistory, prehistory, applied), published by the **University of Chicago Press for
the Wenner-Gren Foundation**. Its craft is **ethnographic and qualitative research, archival and material
analysis, reflexivity, and ethically accountable engagement with communities**, with appropriate
**quantitative/lab** methods in the biological and archaeological subfields — and its signature is the
**CA✩ Treatment**, in which an accepted Major Article is published with signed Comments and the author's
Reply. Accordingly, **this pack ships no code kit**: there is no `resources/code/` directory and nothing
to run. The resources here are reading and modeling aids for prose, argument, evidence, and ethics.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an anthropology-article **introduction** in CA house style — question → all-fields significance → reflexive argument → grounded finding → portable, **commentary-worthy** concept. Clearly-marked **fictional** article; no real community, site, or finding. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified CA articles** organized by subfield × method. Positioning and craft cues only — no fabricated findings — with a sibling-journal confusion guard (CA ≠ AA / AE / *Cultural Anthropology*). |
| [`official-source-map.md`](official-source-map.md) | **CA-specific policy & facts:** sponsor (Wenner-Gren) / publisher (UChicago Press), Editorial Manager submission, the **CA✩ Treatment**, the 6,000–10,000-word Major Article / 3,000–5,000-word Report / ≤ 200-word abstract / ≤ 800-word Discussion caps, `.doc`/`.rtf` + TIFF/EPS file rules, Chicago author-date, Wenner-Gren copyright, editors, and live-check guardrails. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Find archives, primary-source databases, CAQDAS, transcription/paleography tools, GIS/mapping, lab/quant packages, and reference managers (Chicago author-date) matched to your subfield. |

## No empirical/code kit (predominantly qualitative venue)

Unlike the quantitative social-science packs in this repo, the CA pack does **not** vendor a
causal-inference code pipeline. CA is judged on the **quality and reflexivity of ethnographic and
qualitative evidence, the strength of the agenda-setting all-fields argument, ethical accountability, and
whether the argument rewards and survives the CA✩ commentary** — not on estimators or reproducibility
scripts. For the **biological and archaeological** subfields, where quantitative analysis does appear, two
shared method references are linked **as background only** (they are venue-neutral; always defer to this
pack's skills and `official-source-map.md` for what CA specifically requires):

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — common objections to quantitative designs, each with a preemption (relevant to biological/archaeological quant work only).
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — modern inference + reporting hygiene (effect sizes, uncertainty, multiple testing) for the quantitative subfields, **subject to** CA's ethics constraints in [`../skills/curranthro-transparency-and-data`](../skills/curranthro-transparency-and-data/SKILL.md).

If you came looking for a `code/` kit, there isn't one — and that is by design for a predominantly
ethnographic, comment-and-reply flagship.

## Suggested workflow

1. **Scope and frame** the project with
   [`../skills/curranthro-topic-selection`](../skills/curranthro-topic-selection/SKILL.md) (all-fields,
   commentary-worthy fit) and stake the contribution with
   [`../skills/curranthro-literature-positioning`](../skills/curranthro-literature-positioning/SKILL.md).
2. **Build the argument and evidence** with
   [`../skills/curranthro-theory-building`](../skills/curranthro-theory-building/SKILL.md) and
   [`../skills/curranthro-research-design`](../skills/curranthro-research-design/SKILL.md), using
   [`external_tools.md`](external_tools.md) to locate and handle sources.
3. **Design ethics in early** with
   [`../skills/curranthro-transparency-and-data`](../skills/curranthro-transparency-and-data/SKILL.md) —
   consent, anonymization, heritage/repatriation, accountability, Wenner-Gren copyright.
4. **Draft the introduction and structure** by modeling
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), guided by
   [`../skills/curranthro-writing-style`](../skills/curranthro-writing-style/SKILL.md).
5. **Benchmark** against verified CA articles in [`exemplars/library.md`](exemplars/library.md), and
   confirm submission, length, file formats, ethics, copyright, and the CA✩ review model in
   [`official-source-map.md`](official-source-map.md).
