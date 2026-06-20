# Journal of Economic Literature — Resources

Capability layer for the **Journal of Economic Literature (JEL)** skill pack. JEL is a
**survey/review journal**: a JEL article synthesizes a body of economic research rather
than reporting original results. There is therefore **no code kit** in this pack — a
survey runs no estimations of its own. Instead, the cross-cutting empirical-methods
guidance is linked below as **background for appraising the primary studies a survey
covers** (you are the field's referee-of-record), and the survey-craft skills live in
`../skills/`.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a **survey** opening in JEL house style (frame the field → why a synthesis is needed now → the organizing question/taxonomy → what the survey concludes and the open questions). Illustrative fictional survey; uses survey-craft skill links, not identification. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JEL survey articles** (confirmed `10.1257/jel…` DOI stem) organized by topic. Design positioning only — no fabricated findings; includes a sibling-confusion guard vs. *JEP* and *AER*. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees raise of an empirical design, by identification strategy (DiD / IV / RDD / DML / matching / mechanism). **Use here to appraise the credibility of the primary studies your survey weighs** — the survey does not run these designs, but it must judge them fairly. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting stakes (SE clustering, weak-IV diagnostics, multiple testing, DiD/RDD reporting, reproducibility). **Use as the yardstick when grading how good each surveyed study actually is.** |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (proposal route, disclosure, JEL codes, AEA data/code policy, volatile fee/editor) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | Literature-discovery databases, reference/synthesis tooling, the JEL classification system, and meta-analysis packages relevant to a survey. |

## How to use

1. **Before drafting the synthesis** — for each major primary study you will weigh, run it
   against the reviewer-objection checklist and the reporting standards to set its
   **credibility tier** (this feeds the who-found-what tables and the even-handed
   treatment of controversies in `../skills/jel-comprehensiveness-and-balance/SKILL.md`).
2. **When building exhibits** — only pool *commensurable* estimates; the reporting
   standards tell you when an apparent consensus is real (`../skills/jel-tables-figures/SKILL.md`).
3. **Before submission** — walk `official-source-map.md` for the proposal route,
   disclosure requirement, and JEL-code rules.

> The empirical-methods hub is venue-neutral and is used here only to **appraise** the
> studies a survey covers — this pack ships **no runnable code**, because a JEL survey
> reports no original estimates. Always defer to this pack's skills and
> `official-source-map.md` for what JEL specifically requires.
