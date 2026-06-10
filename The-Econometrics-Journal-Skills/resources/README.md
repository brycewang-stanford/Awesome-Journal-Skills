# The Econometrics Journal — Resources

Action-oriented resources for The Econometrics Journal (EctJ) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an EctJ-style methodological section and
benchmark against verified exemplars. Pair these with the relevant `skills/ectj-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **methodological** paper introduction in EctJ house style (a new estimator/test/identification result, with theory + simulation + empirical illustration). Illustrative fictional paper, derived only from this pack's own skills. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified EctJ papers** organized by theme × contribution type (inference methods, panel estimators, weak-IV, diagnostic tests). Positioning only — no fabricated results. |
| [`official-source-map.md`](official-source-map.md) | **EctJ-specific policy & facts:** Editorial Express submission, flat £75+VAT fee, ≤150-word summary, ≤20-page printed-paper rule, simulations-within-one-page, proofs in main text/printed appendix, conditional-on-acceptance replication policy, plus a "do-not-misattribute" list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Official OUP/RES workflow links and author-side checks referenced by the pack. |
| [`code/README.md`](code/README.md) | Use the shared econometrics methods kit for Monte Carlo, estimator, empirical-illustration, and replication-package smoke checks. This is not the generic applied causal-inference code kit. |

## Scope note: discipline-appropriate methods code, not the generic applied-code kit

The Econometrics Journal publishes **econometric theory plus applied / computational econometrics** —
new estimators, tests, identification results, and inference methods, each carrying direct applied
value. It is **not** an outlet for running a generic causal-inference data pipeline. Accordingly,
the venue-neutral applied causal-inference code kit is intentionally **not** vendored into this pack.
The local `code/` directory instead points to a methods-focused simulation and replication adapter.
EctJ-specific facts live in `official-source-map.md`. For the actual estimator, test, simulation,
seed, and replication-package mechanics, follow the skills:

- [`../skills/ectj-data-analysis`](../skills/ectj-data-analysis/SKILL.md) — Monte Carlo design,
  estimator comparisons, seeds, software versions, and applied-value evidence.
- [`../skills/ectj-replication-and-data-policy`](../skills/ectj-replication-and-data-policy/SKILL.md) —
  the acceptance-stage replication package (README, software versions, data documentation, code,
  seeds, OUP Supporting Information).

## Suggested workflow

1. Scope and frame with [`../skills/ectj-topic-selection`](../skills/ectj-topic-selection/SKILL.md) and
   [`../skills/ectj-contribution-framing`](../skills/ectj-contribution-framing/SKILL.md); model the
   intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Stress-test theory and asymptotics with
   [`../skills/ectj-identification-strategy`](../skills/ectj-identification-strategy/SKILL.md); design
   the simulation + empirical application with
   [`../skills/ectj-data-analysis`](../skills/ectj-data-analysis/SKILL.md).
   Use [`code/README.md`](code/README.md) to smoke-check the simulation or replication package layout.
3. Tighten prose to the compact RES/OUP format with
   [`../skills/ectj-writing-style`](../skills/ectj-writing-style/SKILL.md).
4. Benchmark against verified EctJ papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission, fee, page, and replication policy in
   [`official-source-map.md`](official-source-map.md) and the workflow links in
   [`external_tools.md`](external_tools.md).
