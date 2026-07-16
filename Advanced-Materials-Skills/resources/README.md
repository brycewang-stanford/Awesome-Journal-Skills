# Advanced Materials Resources

Action-oriented resources for the Advanced Materials (Adv. Mater.) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an Adv. Mater. opening, plan a characterization
matrix, and benchmark framing against landmark materials papers. Pair these with the relevant
`skills/advmat-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **Communication opening paragraph** (which doubles as the abstract) in Adv. Mater. house style — advance-first, de-hyped, structure→property→function, benchmarked, broad-impact named. Illustrative **fictional** material — no real-paper facts, no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark your framing against **real, web-verified *Adv. Mater.* landmarks** (MXenes, superhydrophobic surfaces, e-skin, ultra-flyweight carbon aerogels, AIE, hollow nanostructures — DOIs `10.1002/adma...`), organized by material class × advance type, plus a **venue-trap list** (graphene, MOF-5, perovskite PV, ... are *not* Adv. Mater. papers). Design positioning only — no fabricated numbers. |
| [`external_tools.md`](external_tools.md) | The materials-characterization analysis stack, the **DFT / simulation** toolchain (VASP, Materials Project, ...), figure tools, and data repositories — plus where to confirm the **live** Adv. Mater. article-type limits and submission requirements. |
| [`official-source-map.md`](official-source-map.md) | The real official Wiley URLs behind the pack's hard facts, with a "Checked" date, so every claim is grounded and re-verifiable. |

## Authoritative source

Adv. Mater.-specific policy (article-type page limits, abstract/keyword rules, figure DPI/format, the
TOC-graphic spec, the submission portal, the APC, and required declarations) is **volatile** and lives
on the **official Wiley Advanced Materials author pages** — `advanced.onlinelibrary.wiley.com` — not
duplicated here. Always verify the current limits and requirements there before submitting; the in-pack
skills ([`advmat-length-management`](../skills/advmat-length-management/SKILL.md),
[`advmat-submission`](../skills/advmat-submission/SKILL.md),
[`advmat-figures`](../skills/advmat-figures/SKILL.md)) each repeat this "verify on the Wiley author page"
caveat. See [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
for entry points.

## Why a characterization/simulation toolchain (and not an econometrics kit)

Unlike the economics packs in this repo, Adv. Mater. ships a **materials-science action layer**: the
[`external_tools.md`](external_tools.md) toolchain covers structure/phase analysis (XRD/Rietveld, TEM/
electron diffraction, XPS), first-principles simulation (VASP, Quantum ESPRESSO), and materials
databases (Materials Project, ICSD). A causal-inference / regression pipeline is **not** discipline-
appropriate here and is deliberately not vendored. The action for Adv. Mater. is proving the
structure→property→function chain, benchmarking the device, and fitting the article-type format — which
the `skills/` plus these resources cover.

## Suggested workflow

1. **Gate the result first** with [`../skills/advmat-scope-fit`](../skills/advmat-scope-fit/SKILL.md):
   does it clear *both* the genuine-advance and broad-impact tests? If not, retarget to a sibling journal.
2. **Frame the one advance** with
   [`../skills/advmat-results-framing`](../skills/advmat-results-framing/SKILL.md) and de-hype prose with
   [`../skills/advmat-writing-style`](../skills/advmat-writing-style/SKILL.md); model the opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. **Make the characterization airtight** with
   [`../skills/advmat-methods`](../skills/advmat-methods/SKILL.md) (triangulate + benchmark), using the
   analysis and simulation tools in [`external_tools.md`](external_tools.md); partition to the SI with
   [`../skills/advmat-supplementary`](../skills/advmat-supplementary/SKILL.md).
4. **Benchmark your framing** against the landmark papers in
   [`exemplars/library.md`](exemplars/library.md); make the editorial case with
   [`../skills/advmat-cover-letter`](../skills/advmat-cover-letter/SKILL.md) and run the final check with
   [`../skills/advmat-submission`](../skills/advmat-submission/SKILL.md).
5. **Confirm live policy** (article-type limits, figure specs, portal) on the official Wiley author page —
   see [`official-source-map.md`](official-source-map.md).
