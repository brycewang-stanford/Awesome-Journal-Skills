# Annals of Mathematics Resources

Action-oriented resources for the Annals of Mathematics skill pack. The `skills/` give advice;
this directory lets an agent **act** — model an Annals-style introduction, benchmark against
verified exemplars, and reach for the right typesetting and reference tooling. Pair these with
the relevant `skills/anmath-*/SKILL.md`.

> **Mathematics venue — no code kit.** Annals of Mathematics is a **pure-mathematics** journal:
> theorem-and-proof, not data or statistics. Unlike the empirical-economics packs, this pack
> deliberately ships **no `code/` pipeline** (there is no dataset to clean and no regression to
> run). The actionable craft here is exposition, rigor, positioning, and TeX/AMS tooling.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a pure-mathematics paper **introduction** in Annals house style — precise Main Theorem stated early, advance quantified against named prior work, one-paragraph proof overview, no hidden gaps. Illustrative **fictional** theorem. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified Annals of Mathematics papers** organized by area (number theory, arithmetic geometry, geometry, geometric analysis, dynamics). Positioning and significance only — no fabricated theorem statements. Includes a sibling-journal "do-not-misattribute" guardrail (Inventiones / Acta / JAMS / IHÉS / Duke). |
| [`external_tools.md`](external_tools.md) | Reach for the right **TeX / AMS typesetting**, reference databases (MathSciNet, zbMATH, arXiv), proof assistants, and revision tooling when preparing a theorem-and-proof manuscript. |

## Suggested workflow

1. **Screen fit** with [`../skills/anmath-scope-fit`](../skills/anmath-scope-fit/SKILL.md):
   is the result deep and important enough for Annals?
2. **State the headline** with
   [`../skills/anmath-results-framing`](../skills/anmath-results-framing/SKILL.md) and **expose
   the proof architecture** with [`../skills/anmath-methods`](../skills/anmath-methods/SKILL.md);
   model the introduction on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. **Benchmark** the framing against verified Annals landmarks in
   [`exemplars/library.md`](exemplars/library.md) — and confirm you are not confusing Annals
   with a sibling journal.
4. **Polish rigor** with
   [`../skills/anmath-writing-style`](../skills/anmath-writing-style/SKILL.md) (eliminate every
   "clearly"/"easy to see"), then prepare the manuscript with the TeX/AMS and reference tooling
   in [`external_tools.md`](external_tools.md).

> **Note on `official-source-map.md`.** Some packs in this repo include an
> `official-source-map.md` of venue-specific policy facts; this pack does **not** have one yet,
> so it is intentionally **not linked** above. Verify volatile submission details (portal,
> formats, length) directly on the journal's official page, `annals.math.princeton.edu`. If an
> `official-source-map.md` is added later, link it from this index.
