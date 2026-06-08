# JET Resources

Action-oriented resources for the Journal of Economic Theory (JET) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a JET-style theorem-first section and benchmark
against verified exemplars. Pair these with the relevant `skills/jet-*/SKILL.md`.

JET is a **theory journal**: the deciding criterion is a rigorous, original theoretical contribution
(a theorem, model, or characterization), with empirical/computational work admitted only when grounded
in theory (see [`../skills/jet-topic-selection/SKILL.md`](../skills/jet-topic-selection/SKILL.md)).

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a theory-paper introduction in JET house style — the theorem-first arc (question theoretically posed → result as a theorem → delta from prior theory → scope guardrail → subfield signal). Illustrative fictional paper; no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JET papers** (Elsevier; DOI/PII family `10.1016/0022-0531...` / `10.1016/j.jet...`) organized by theory area × theme. Design positioning only — no fabricated theorems or parameters. Includes a sibling-journal "do-not-confuse" omissions list. |
| [`official-source-map.md`](official-source-map.md) | **JET-specific policy & facts:** single-anonymized (single-blind) review with a minimum of two reviewers, scope across mechanism design / information / decision theory / game theory / matching / market design / political economy / finance-macro theory, the elsarticle `.tex` requirement, ISSN, and a do-not-misattribute list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack. |

## Why no econometrics code kit here

JET is a **theory venue**, so this resource layer deliberately does **not** vendor the shared
econometric/causal-inference code kit (TWFE/DID, IV, RDD, DML pipelines) that empirical-journal packs
carry: there is no data-identification design to run for a theorem-proof paper. The JET analogue of an
"identification strategy" is **explicit load-bearing assumptions, precise results, and a referee-checkable
proof architecture** — see
[`../skills/jet-identification-strategy/SKILL.md`](../skills/jet-identification-strategy/SKILL.md). For
typesetting and tooling references (e.g. the Elsevier `elsarticle` class), see
[`external_tools.md`](external_tools.md).

## Suggested workflow

1. Scope the project against the JET gate with
   [`../skills/jet-topic-selection/SKILL.md`](../skills/jet-topic-selection/SKILL.md) — state the result
   you would put in the abstract as a proposition/theorem.
2. Frame the contribution theorem-first with
   [`../skills/jet-contribution-framing/SKILL.md`](../skills/jet-contribution-framing/SKILL.md), and
   model the introduction on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Make assumptions and proof architecture referee-proof with
   [`../skills/jet-identification-strategy/SKILL.md`](../skills/jet-identification-strategy/SKILL.md);
   polish notation and statements with
   [`../skills/jet-writing-style/SKILL.md`](../skills/jet-writing-style/SKILL.md).
4. Benchmark against verified JET papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission, review model, and house-style policy in
   [`official-source-map.md`](official-source-map.md).
