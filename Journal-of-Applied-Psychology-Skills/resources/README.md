# Journal of Applied Psychology — Resources

Capability layer for the **Journal of Applied Psychology (JAP)** skill pack. The `skills/` give advice;
this directory lets an agent **model a JAP section**, **benchmark against verified exemplars**, and
**confirm venue facts** before drafting. Pair these with the relevant `skills/joap-*/SKILL.md`.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Before→after rewrite of a JAP introduction in phenomenon → theoretical contribution (mechanism + level + boundary) → rigorous design → applied relevance style. Fictional teaching paper. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *Journal of Applied Psychology* papers by topic × method, with a sibling-journal omission guard. Design positioning only — read the originals before citing numbers. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (publisher, portal, masked review, article types, length, APA style, TOP open-science policy, sibling boundaries) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue (SEM/HLM/meta-analysis software, CMV and invariance tools, preregistration, repositories, APA tooling). |

## Background method references (shared hub — not a vendored code kit)

This is an **I-O / applied-psychology** venue whose methods center on **construct validity, multilevel
(HLM) models, SEM, mediation/moderation, and meta-analysis** — not an econometrics pipeline. **No
`resources/code/` kit is vendored here**; a Stata/Python causal-inference pipeline would be
off-discipline for JAP. Use the domain-appropriate tools in [`external_tools.md`](external_tools.md)
instead. For cross-cutting inference discipline, two shared references are useful **as background**:

- [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — generic objections by identification strategy; read it for the *habit* of pre-empting objections,
  then translate to JAP's actual objections (CMV, level of analysis, measurement invariance, alternative
  models) via [`../skills/joap-study-design/SKILL.md`](../skills/joap-study-design/SKILL.md) and
  [`../skills/joap-data-analysis/SKILL.md`](../skills/joap-data-analysis/SKILL.md).
- [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) — general
  reporting/reproducibility table stakes; for JAP, defer to the effect-size/CI, SEM-fit, indirect-effect-CI,
  and TOP requirements in this pack's skills.

## How to use

1. **Scope and frame** with [`../skills/joap-topic-selection`](../skills/joap-topic-selection/SKILL.md)
   and [`../skills/joap-theory-and-hypotheses`](../skills/joap-theory-and-hypotheses/SKILL.md); model the
   introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. **Harden design and analysis** with
   [`../skills/joap-study-design`](../skills/joap-study-design/SKILL.md) and
   [`../skills/joap-data-analysis`](../skills/joap-data-analysis/SKILL.md) (CMV, nesting, SEM/HLM, indirect-effect CIs).
3. **Benchmark** your framing against verified papers in [`exemplars/library.md`](exemplars/library.md).
4. **Before submission**, confirm article type, length, masking, and TOP open-science policy in
   [`official-source-map.md`](official-source-map.md).

> Method guidance in the shared hub is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
