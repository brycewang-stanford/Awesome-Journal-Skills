# Communication Research — Resources

Capability layer for the **Communication Research** (CR) skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared empirical-methods hub and
is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python analysis skeleton (clean → descriptive → models → mechanism → robustness → tables). Vendored from the verified shared empirical-methods library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. For CR, lean on the measurement, mediation, and reporting blocks more than the causal-identification chain. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by strategy, each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: effect sizes, SE clustering, multiple-testing, reproducibility — the APA-reporting bar CR enforces. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (page limit, blinding, two-review rule, APA reporting, data policy) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | Data sources, measurement/reliability/SEM tooling, and the SAGE Track portal for this venue. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional, clearly-labelled CR-style introduction + abstract in house style. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *Communication Research* papers by method × topic, with a sibling-journal guard. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every
   objection you cannot answer in one paragraph + one exhibit is a hole. For CR, pay special attention
   to **measurement validity, common-method variance, and mediation identification**.
2. **When building results** — adapt `code/` to your data; for CR, keep the **effect-size + CI**
   reporting and the **mediation/moderation** blocks; run the modern-estimator chain only where your
   design is causal.
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue limits (45-page cap, APA reporting, double-anonymized, two reviews).

> Method guidance here is venue-neutral; always defer to this pack's skills and `official-source-map.md`
> for what *Communication Research* specifically requires.
