# New Media & Society — Resources

Capability layer for the **New Media & Society** skill pack. The `skills/` give advice; this directory
lets an agent **act** — model an NM&S-style introduction, benchmark against verified exemplars, and
locate the right tools for an interdisciplinary, methodologically pluralist journal.

NM&S spans qualitative interviews and digital ethnography, critical/theoretical work, content and
discourse analysis, computational methods, and mixed methods. This shapes what is — and is not —
vendored here.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a digital-media paper introduction in NM&S house style: question + a portable concept (the mechanism) + the method that adjudicates the rival reading + broad interdisciplinary stakes. Illustrative fictional paper; no real-paper or policy claims. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified NM&S papers** organized by method × theme — with a sibling-confusion guard (NM&S ≠ Journal of Communication / Communication Research / Information, Communication & Society / Social Media + Society). Conceptual positioning only — no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **NM&S-specific policy & facts:** SAGE ownership, 8,000-word target, 150-word abstract, ≥4 keywords, anonymized workflow, SAGE Harvard referencing, Sage Track portal, editor/transition watch, preprints, data-availability statement, and live-check guardrails. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Tools by method: digital-media data sources, CAQDAS and content-analysis software, computational/network/text-as-data libraries, reference management, and reproducibility tooling. |

## Why there is no `code/` kit here

The econometrics / causal-inference code kit vendored into quantitative empirical packs (e.g., the
Quantitative-Economics pack's Stata + Python DiD/IV/RDD pipeline) is **deliberately NOT vendored** into
this pack. NM&S is **methodologically pluralist** and its center of gravity is qualitative, critical,
content/discourse, and computational work — not a single estimation pipeline. The analogous "tooling"
for NM&S is method-spread: CAQDAS for interviews, reliability tools for content analysis, and
text-as-data / network libraries for computational work — all in
[`external_tools.md`](external_tools.md).

For background only, cross-cutting method guidance lives once in the shared empirical-methods hub and is
linked here for the **computational/quantitative** strand of NM&S work; defer to this pack's skills and
`official-source-map.md` for what *this* journal requires:

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — objections referees raise on quantitative/computational designs, each with its preemption (background for the computational strand only).
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — modern inference + reporting table stakes (SE clustering, multiple-testing, reproducibility) — background for quantitative/computational analyses only.

## Suggested workflow

1. Frame fit and the portable concept with
   [`../skills/newms-topic-selection`](../skills/newms-topic-selection/SKILL.md) and
   [`../skills/newms-theory-building`](../skills/newms-theory-building/SKILL.md); model the intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Defend the design for your method with
   [`../skills/newms-research-design`](../skills/newms-research-design/SKILL.md), then make inference
   transparent with [`../skills/newms-data-analysis`](../skills/newms-data-analysis/SKILL.md).
3. Handle online/platform-data ethics with
   [`../skills/newms-transparency-and-data`](../skills/newms-transparency-and-data/SKILL.md).
4. Benchmark against verified NM&S papers in [`exemplars/library.md`](exemplars/library.md); confirm
   scope, length, masking, referencing, and submission facts in
   [`official-source-map.md`](official-source-map.md) and tooling in
   [`external_tools.md`](external_tools.md).

> Method guidance in the shared hub is venue-neutral and applies only to the computational/quantitative
> strand; always defer to this pack's skills and `official-source-map.md` for what *this* journal
> specifically requires.
