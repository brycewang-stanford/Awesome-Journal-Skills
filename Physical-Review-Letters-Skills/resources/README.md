# PRL Resources

Action-oriented resources for the Physical Review Letters (PRL) skill pack. The `skills/` give advice;
this directory lets an agent **act** — model a PRL-style abstract + opening and benchmark against
verified Letters. Pair these with the relevant `skills/prl-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a Letter **abstract + opening** in PRL house style (one central claim, finding-first, the importance + broad-interest gate, out-of-subfield readability, within the ~3750-word / ~4-page limit). Illustrative **fictional** Letter — no real-paper facts, no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified PRL Letters** organized by subfield × method, each carrying its `10.1103/PhysRevLett...` DOI. Design positioning only — no fabricated numbers; siblings (PRX, PRD/C/B/A/E, RMP, Phys. Lett. B, Nature Physics) explicitly excluded. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack — including where to confirm the **live** PRL length/abstract limits and submission categories on the official APS / PRL author page. |

## Authoritative source

PRL-specific policy (the length deductible, abstract limit, Letter article type, REVTeX/format
expectations, Supplemental Material, and subject classification) is **volatile** and lives on the
**official APS / PRL author pages** — `journals.aps.org/prl` — not duplicated here. Always verify the
current limit and categories there before submitting; the in-pack skills
([`prl-length-management`](../skills/prl-length-management/SKILL.md),
[`prl-submission`](../skills/prl-submission/SKILL.md),
[`prl-results-framing`](../skills/prl-results-framing/SKILL.md)) each repeat this "verify on the APS
author page" caveat. See [`external_tools.md`](external_tools.md) for the entry points.

## No econometric / causal-inference code kit (by design)

Unlike the economics packs in this repo, **PRL ships no vendored empirical-methods code directory**.
Physical Review Letters is a **physics-letters venue** spanning condensed matter, AMO,
particle/nuclear, gravitation/astro, statistical/soft matter, and quantum information; a Stata/Python
causal-inference pipeline (TWFE/DID/IV/RDD/DML) is **not discipline-appropriate** here and is
deliberately **not vendored**. The action layer for PRL is editorial and structural — framing the one
central claim, fitting the strict length budget, and partitioning Letter vs. Supplemental Material —
which the `skills/` plus the two resources above already cover.

## Suggested workflow

1. **Gate the result first** with [`../skills/prl-scope-fit`](../skills/prl-scope-fit/SKILL.md): does it
   pass *both* importance and broad interest? If not, retarget to a specialized Physical Review journal.
2. **Frame the one central claim** with
   [`../skills/prl-results-framing`](../skills/prl-results-framing/SKILL.md) and polish prose with
   [`../skills/prl-writing-style`](../skills/prl-writing-style/SKILL.md); model the abstract + opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. **Fit the length budget** with
   [`../skills/prl-length-management`](../skills/prl-length-management/SKILL.md) and partition methods
   vs. Supplemental Material with [`../skills/prl-methods`](../skills/prl-methods/SKILL.md) and
   [`../skills/prl-supplementary`](../skills/prl-supplementary/SKILL.md).
4. **Benchmark** your subfield × method against the verified Letters in
   [`exemplars/library.md`](exemplars/library.md); make the editorial case with
   [`../skills/prl-cover-letter`](../skills/prl-cover-letter/SKILL.md) and run the final check with
   [`../skills/prl-submission`](../skills/prl-submission/SKILL.md).
5. **Confirm live policy** (length formula, abstract limit, categories) on the official APS / PRL author
   page — see [`external_tools.md`](external_tools.md).
