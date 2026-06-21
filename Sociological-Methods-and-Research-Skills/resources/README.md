# Sociological Methods & Research — Resources

Capability layer for the **Sociological Methods & Research (SMR)** skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an SMR-style methods introduction, benchmark
against web-verified exemplars, and check venue facts before submission. Pair each resource with the
relevant `skills/smr-*/SKILL.md`.

This is a **methods journal** pack, so it does **not** vendor the venue-neutral applied
causal-inference code kit. SMR papers ship their *own* released software (see
[`../skills/smr-software-and-reproducibility/SKILL.md`](../skills/smr-software-and-reproducibility/SKILL.md));
the shared empirical-methods materials below are linked only as **background** for stress-testing a
design, never as the pack's deliverable.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **methods-paper** introduction in SMR house style (problem → why existing methods fail → contribution → properties → simulation + illustration → released software). Illustrative **fictional** paper, derived only from this pack's own skills. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified SMR papers** organized by method family (causal inference, SEM/fit, latent-variable/mixture, measurement invariance, missing data, multilevel/longitudinal, networks, computational text). Positioning only — no fabricated results; includes a sibling-journal guard (SMR ≠ Sociological Methodology / Psychological Methods / Political Analysis). |
| [`official-source-map.md`](official-source-map.md) | **SMR-specific policy & facts:** ScholarOne submission, double-anonymized review, ASA + DataCite citation style, ≤150-word non-parenthetical abstract, data-and-code availability statement, generative-AI disclosure, accepted file formats, plus a "do-not-misattribute" list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Discipline data sources, software ecosystems, and official SAGE/ASA workflow links referenced by the pack. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | **Background only.** General objections referees raise by identification strategy — useful when an SMR paper's empirical illustration leans on a causal design, but not a substitute for this pack's `smr-derivation-and-properties` / `smr-simulation-studies` skills. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | **Background only.** Cross-cutting inference/reporting table stakes (SE clustering, weak-IV diagnostics, multiple testing, reproducibility) for the empirical illustration. Defer to SMR's own data-and-code policy in `official-source-map.md`. |

## How to use

1. **When deciding fit** — apply [`../skills/smr-topic-selection/SKILL.md`](../skills/smr-topic-selection/SKILL.md): a method contribution, not an application. Then sharpen with [`../skills/smr-method-contribution/SKILL.md`](../skills/smr-method-contribution/SKILL.md).
2. **When framing the paper** — model the introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) and benchmark the method family against the verified [`exemplars/library.md`](exemplars/library.md).
3. **When building the evidence** — derive properties with [`../skills/smr-derivation-and-properties/SKILL.md`](../skills/smr-derivation-and-properties/SKILL.md), design the Monte Carlo with [`../skills/smr-simulation-studies/SKILL.md`](../skills/smr-simulation-studies/SKILL.md), and the real-data demonstration with [`../skills/smr-empirical-illustration/SKILL.md`](../skills/smr-empirical-illustration/SKILL.md). Use the shared checklists above only as background stress tests.
4. **Before submission** — release software with [`../skills/smr-software-and-reproducibility/SKILL.md`](../skills/smr-software-and-reproducibility/SKILL.md) and verify venue limits in [`official-source-map.md`](official-source-map.md) and the workflow links in [`external_tools.md`](external_tools.md).

> Venue facts change. Always reopen `official-source-map.md` and the live SAGE author page before any
> deadline-ready submission advice.
