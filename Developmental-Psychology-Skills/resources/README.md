# Developmental Psychology — Resources

Capability layer for the **Developmental Psychology** (APA) skill pack. The `skills/` give advice; this
directory lets an agent **act** — model a Developmental Psychology-style Introduction, benchmark against
verified exemplars, and check venue facts. Pair each resource with the relevant `skills/devpsych-*/SKILL.md`.

Developmental Psychology is an **empirical lifespan-development** journal whose contribution must be about
**change** (age effects, within-person trajectories, mechanisms), reported under **APA 7th edition + JARS**
and the **Transparency and Openness Promotion (TOP)** guidelines. That shapes what is — and is not —
vendored here.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a Developmental Psychology Introduction in developmental-question → gap (change/age/mechanism) → contribution → design (power, invariance, preregistration) → public significance style. **Fictional** teaching paper; no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *Developmental Psychology* papers by method × developmental domain, with a sibling-journal omission guard (≠ Child Development / Developmental Science / JPSP). Design positioning only — read the originals before citing numbers. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (scope, length tiers, abstract + Public Significance Statement, masked review, JARS, TOP, editor/portal) with sourcing discipline and honest 待核实 markers. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Developmental tooling: preregistration, repositories (OSF / ICPSR / Databrary), developmental data archives, power simulation, growth/SEM/invariance/missing-data packages, `papaja`. |

## Why there is no `code/` kit here

The econometrics / causal-inference code kit vendored into some empirical packs (DiD / IV / RDD / DML
pipelines) is **deliberately not vendored** into this pack. Developmental Psychology's persuasive work is
**developmental design and change-modeling** — growth curves, measurement invariance, attrition handling,
mediation/moderation — not a quasi-experimental panel pipeline. The analogous tooling for this venue is
the **growth/SEM/invariance** stack documented in [`external_tools.md`](external_tools.md). For background
on cross-cutting inference and reviewer objections, two shared references are useful as **general
context** (venue-neutral; always defer to this pack's skills and `official-source-map.md` for what
*Developmental Psychology* specifically requires):

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — common identification/inference objections and their preemptions (read as background, not as this
  journal's checklist).
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — modern
  inference and reporting table stakes (SE clustering, multiple testing, reproducibility) — background to
  complement, not replace, **JARS**.

## How to use

1. **Framing the contribution** — model the Introduction on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md); confirm fit and length tier
   with [`../skills/devpsych-topic-selection`](../skills/devpsych-topic-selection/SKILL.md).
2. **Hardening the design** — use [`../skills/devpsych-study-design`](../skills/devpsych-study-design/SKILL.md)
   for age-vs-cohort, invariance, attrition, and sample-size justification; tooling in
   [`external_tools.md`](external_tools.md).
3. **Before submission** — benchmark against [`exemplars/library.md`](exemplars/library.md) and walk the
   venue facts and limits in [`official-source-map.md`](official-source-map.md).

> Method guidance in the shared references is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *Developmental Psychology* specifically requires.
