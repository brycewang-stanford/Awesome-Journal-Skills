# Language (LSA) — Resources

Capability layer for the **Language** skill pack. Runnable code is vendored for self-containment; the
cross-cutting empirical-method guidance lives once in the shared hub and is linked below. Everything
here is venue-neutral craft — defer to the pack's skills and `official-source-map.md` for what *Language*
specifically requires.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`external_tools.md`](external_tools.md) | The linguistics stack by subfield: Praat, ELAN/FLEx, Montreal Forced Aligner, R (`lme4`/`brms`), corpora (CHILDES, BNC, COCA, Buckeye, treebanks), IPA and Leipzig-glossing tools, archives and OSF. |
| [`official-source-map.md`](official-source-map.md) | Official LSA / Cambridge University Press / Style Sheet URLs behind every fact, with live-check notes for volatile items (word limits, abstract, open-access terms, masthead, data policy). |
| [`exemplars/library.md`](exemplars/library.md) | Well-known works associated with *Language* by subfield, with a sibling-journal omission guard. Design positioning only — read the originals before citing specifics. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a *Language*-style article introduction (generalization + analysis + prediction + evidence + cross-subfield stakes). Illustrative fictional paper. |
| [`code/`](code/) | Optional quantitative-lane skeleton (clean → descriptive → modeling → robustness → tables). Vendored from the Economic-Research-Journal-Skills library (Stata/Python causal-inference tooling); useful for the sociolinguistic/experimental lane, but **most *Language* work is analytic/glossed** — adapt only where a quantitative design applies, and prefer mixed-effects modeling in R (see `external_tools.md`). |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | Objections referees raise by identification strategy — stress-test any quantitative design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Inference and reporting table stakes for quantitative work: clustering, multiple testing, reproducibility. |

## How to use

1. **Before drafting** — pressure-test fit and the theoretical claim (`lang-topic-selection`,
   `lang-theory-building`); a glossed pattern is not yet a contribution.
2. **When building results** — for quantitative work, fit the model the design justifies (mixed-effects
   in R); keep glosses sourced and examples numbered.
3. **Before submission** — walk the pack's `official-source-map.md` for volatile *Language* rules and
   run the `lang-submission` checklist.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *Language* specifically requires.
