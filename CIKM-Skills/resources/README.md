# CIKM Resources

Working materials behind the CIKM skill pack. The `skills/` directory holds the
advice; this directory holds what the advice points at — verified sources, verified
exemplar papers, a worked rewrite, tool links, and the shared reproducibility kit —
so an agent can ground CIKM guidance without inventing venue facts.

## Contents

| Resource | What it is for |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | The verified CIKM 2026 fact base: five-track lineup, page budgets with appendices counted inside, EasyChair mechanics, GenAI-disclosure rule, dates — each with URL and access date, plus everything explicitly left 待核实. Read before any deadline- or policy-sensitive answer. |
| [`exemplars/library.md`](exemplars/library.md) | Six dblp-verified CIKM papers spanning the IR × mining × KM lane combinations (TAGME → BERT4Rec), each with a positioning lesson and self-check — plus the named misattribution traps (KDD/SIGIR/WSDM/ICDM/NeurIPS classics that are *not* CIKM). |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before → after rewrite of a fictional abstract + introduction into CIKM's tri-lane register. Entirely fictional content; no policy stated. |
| [`external_tools.md`](external_tools.md) | The live official surfaces (host site, per-track calls, policies page, EasyChair, ACM DL, dblp) and what to re-check on each. |
| [`code/README.md`](code/README.md) | Pointer to the repo-shared ML-conference reproducibility kit (experiment matrix, artifact checklist, package smoke checker) as used for CIKM chained-pipeline artifacts. |

## Scope note

This pack serves an ACM data/information conference, not an economics journal: do not
pull the Stata/econometrics kit from the journal packs into CIKM work. The relevant
shared machinery is the ML-conference kit referenced under `code/`, applied with the
CIKM-specific pipeline-pinning discipline described in
[`../skills/cikm-reproducibility/SKILL.md`](../skills/cikm-reproducibility/SKILL.md).

## How the pieces chain

1. **Route first**: [`../skills/cikm-topic-selection`](../skills/cikm-topic-selection/SKILL.md)
   decides venue and track; the exemplars library supplies the comparison points.
2. **Build under the real rules**: source map + external tools give the current
   budgets and form mechanics that
   [`../skills/cikm-submission`](../skills/cikm-submission/SKILL.md) enforces.
3. **Write for three lanes**: the worked example demonstrates the register that
   [`../skills/cikm-writing-style`](../skills/cikm-writing-style/SKILL.md) teaches.
4. **Package the evidence**: `code/README.md` plus
   [`../skills/cikm-artifact-evaluation`](../skills/cikm-artifact-evaluation/SKILL.md)
   and [`../skills/cikm-supplementary`](../skills/cikm-supplementary/SKILL.md)
   turn results into review-grade artifacts within appendix-inclusive budgets.

Everything dated in this directory carries its access date (2026-07-08 unless noted);
treat any newer official page as overriding.
