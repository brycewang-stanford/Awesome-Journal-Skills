# Governance — Resources

Capability layer for the **Governance: An International Journal of Policy, Administration, and
Institutions** skill pack. The runnable code is vendored for self-containment; the cross-cutting method
guidance lives once in the shared empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a comparative-governance paper introduction in Governance house style (question → comparative/institutional significance → identification problem → setting & design → finding + mechanism → portable contribution across cases → brief roadmap). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified Governance papers** organized by theme × method (regulatory governance, bureaucratic reform, policy process, comparative institutions, transparency/norm diffusion). Design positioning only — no fabricated findings; includes a sibling-journal do-not-misattribute list (PAR / JPART / JPAM / Regulation & Governance / Public Administration). |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (word/abstract caps, blinding, Data Availability Statement, submission portal, reference style) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue — comparative-governance data sources, software by method, QCA/fsQCA, CAQDAS, transparency repositories. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD), or, for configurational claims, the QCA/fsQCA tooling in `external_tools.md`.
3. **Before submission** — walk the reporting-standards inference audit, draft an honest **Data Availability Statement**, and check this pack's `official-source-map.md` for venue limits (≤ 9,000 words excluding citations/bibliography; ~150-word abstract; double-blind with a separate title page).

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *Governance* specifically requires.
