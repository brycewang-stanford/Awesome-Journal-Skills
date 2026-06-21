# Psychological Review Resources

Action-oriented resources for the Psychological Review skill pack. The `skills/` give advice; this
directory lets an agent **act** — model a Psychological Review-style *theory* paper and benchmark
against verified exemplars. Pair these with the relevant `skills/psychrev-*/SKILL.md`.

Psychological Review is the American Psychological Association's flagship for **theoretical
contributions**: new theory, formal/mathematical/computational models, and major theoretical
syntheses. It does **not** publish primary empirical reports — data appear only to *motivate* or
*constrain* the theory (those empirical papers belong at the JEP family or Psychological Science).
This shapes what is — and is not — vendored here.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **theory/model** paper introduction in Psychological Review house style: phenomenon/tension → standing theories' gap → the model/mechanism move → derived predictions → contribution-early. Illustrative fictional model; no empirical claims. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified Psychological Review theory/model papers** organized by theoretical form. Theoretical positioning only — no fabricated parameters or numbers — with a sibling-confusion guard (Psychological Review ≠ Psychological Bulletin / BBS / TiCS / JEP / American Psychologist). |
| [`official-source-map.md`](official-source-map.md) | **Psychological Review-specific policy & facts:** theory-only scope, article types (Theoretical articles / Theoretical Notes), Editorial Manager masked review, APA style, editor, the 15,000-word soft threshold, and a "still unverified" list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools for theory/modeling work: modeling environments, identifiability/recovery/model-comparison analysis, locating the theoretical conversation, model diagrams and simulation figures, and argument-logic aids — **no experiment-running or dataset vendors**, by design. |

## Why there is no `code/` kit here

The econometrics / causal-inference code kit vendored into empirical packs (DID / IV / RDD / DML
pipelines) is **deliberately NOT vendored** into Psychological Review. Review is a **theory venue**:
there is no experimental dataset and no empirical-analysis step, so a causal-inference pipeline has
nothing to act on. The analogous "tooling" for Psychological Review is **modeling**, not empirical
estimation — modeling environments, identifiability/recovery analysis, and conceptual-figure aids live
in [`external_tools.md`](external_tools.md). Note the distinction: a *computational* Review paper still
shares its **own model code** (simulation/fitting scripts), but that is the author's model, not a
shared empirical kit.

For background only, the repository's shared reviewer-objection checklist and reporting-standards
references live under
[`../../shared-resources/empirical-methods/`](../../shared-resources/empirical-methods/) — they target
*empirical* manuscripts and are **not** part of the Psychological Review workflow; consult them only if a
project turns out to be empirical (in which case it belongs at a different journal).

## Suggested workflow

1. Frame the problem and confirm theory-fit with
   [`../skills/psychrev-topic-selection`](../skills/psychrev-topic-selection/SKILL.md); position
   against rivals with
   [`../skills/psychrev-literature-positioning`](../skills/psychrev-literature-positioning/SKILL.md);
   model the intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Build the theory with
   [`../skills/psychrev-theory-construction`](../skills/psychrev-theory-construction/SKILL.md) —
   assumptions → mechanism → formalization → derived behavior — then derive and confront predictions
   with [`../skills/psychrev-argument-development`](../skills/psychrev-argument-development/SKILL.md)
   and bound the theory with
   [`../skills/psychrev-boundary-conditions`](../skills/psychrev-boundary-conditions/SKILL.md).
3. Build model diagrams and simulation figures with
   [`../skills/psychrev-conceptual-exhibits`](../skills/psychrev-conceptual-exhibits/SKILL.md);
   polish to APA house style with
   [`../skills/psychrev-writing-style`](../skills/psychrev-writing-style/SKILL.md) (model vocabulary,
   no empirical register).
4. Benchmark against verified Psychological Review papers in
   [`exemplars/library.md`](exemplars/library.md); confirm scope, article types, and submission/format
   facts in [`official-source-map.md`](official-source-map.md) and tooling in
   [`external_tools.md`](external_tools.md).
