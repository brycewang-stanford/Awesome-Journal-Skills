# The Yale Law Journal — Resources

Capability layer for the **The Yale Law Journal (YLJ)** skill pack. Legal scholarship is carried in its
sources and footnotes rather than in a runnable data pipeline, so this pack ships **no code kit**; the
resources below are reference material for legal research, citation form, and venue facts.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`external_tools.md`](external_tools.md) | Legal-research databases (Westlaw, Lexis, HeinOnline, SSRN, Google Scholar, court/government primary sources) and citation/Bluebook tooling, mapped to the preemption-check and cite-check skills. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (student-edited model, own submission portal, anonymized review, Bluebook style, track/length caps, expedite policy, Forum) with sourcing discipline and 待核实 markers. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a YLJ-style article introduction (claim → stakes → roadmap, generalist-legible, footnotes as support). Illustrative **fictional** piece, clearly labeled. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified YLJ pieces** grouped by contribution type. Positioning only — no fabricated holdings; includes a sibling-law-review do-not-misattribute list. |

## Cross-cutting background (shared hub, not law-specific)

These shared notes are **empirical-methods** material written for quantitative social science. A YLJ
piece is usually doctrinal/theoretical, but if your Article relies on **empirical legal studies** (an
original dataset, a regression, an event study), skim them as background for reporting and review
expectations — they are not a substitute for this pack's law-specific skills:

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — common objections to empirical identification strategies (DiD / IV / RDD / matching), each with a preemption. Relevant only to empirical-legal-studies pieces.
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — inference and reporting table stakes (clustering, weak-IV diagnostics, multiple testing) for any quantitative component.

## How to use

1. **Choosing a topic / claim** — calibrate ambition against `exemplars/library.md`; confirm the venue
   facts in `official-source-map.md`.
2. **Proving novelty** — run the preemption sweep with the databases in `external_tools.md`.
3. **Before submission** — verify track/length, portal, and anonymization against `official-source-map.md`;
   for any empirical component, skim the shared reporting standards above.

> Venue facts change. Always defer to this pack's skills and `official-source-map.md`, and verify
> volatile items on the official YLJ submissions page.
