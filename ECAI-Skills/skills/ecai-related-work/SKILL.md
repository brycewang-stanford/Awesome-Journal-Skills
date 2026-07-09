---
name: ecai-related-work
description: Use when writing the ECAI related-work section — covering the relevant general-AI lanes (symbolic, learning, multi-agent, application) for a broad reviewer pool, writing delta-first positioning, keeping self-citations double-blind, and doing it within a tight reference budget (1 page standalone / 2 pages in IJCAI-ECAI 2026).
---

# ECAI Related Work

ECAI's related work has a peculiar difficulty: the reviewer pool is **broad** (a planning paper may
draw a KR reviewer and an ML reviewer), yet the **space is tiny** — the body is 7 pages and
references overflow into only 1 page (standalone ECAI) or 2 pages (IJCAI-ECAI 2026). You must
position against the right lanes for a general audience *and* stay compact.

## Cover the lanes a general-AI reviewer will expect

Identify which AI lanes your contribution touches and place it in each — a broad reviewer will fault
a section that only cites its author's home subfield:

- **Symbolic / foundational lane** — the KR, planning, search, reasoning, or argumentation line
  your problem sits in.
- **Learning lane** — the ML/statistical methods your work uses or competes with.
- **Multi-agent / decision lane** — if agents, game-theoretic, or sequential-decision aspects
  apply.
- **Application lane** — the real-world domain, especially for a **PAIS**-flavored contribution.
- **Cross-venue neighbors** — the closest work at IJCAI, AAAI, AAMAS, KR, or a specialist venue, so
  a reviewer from that community sees you know the field's flagship results.

You will not cover all lanes deeply at 7+1(2) pages — cover the ones your claim actually engages,
and cite the canonical entry point for the rest.

## Delta-first positioning

Do not write an annotated bibliography. For each closest competitor, state the **delta** in one
sentence: what they do, and precisely what you do differently or additionally.

> "Prior learned-heuristic planners plug the model in directly and lose completeness [refs]; we
> preserve completeness and a (1+ε) bound via per-state switching."

Delta-first writing does three jobs at once in minimal space: it credits prior work, states your
novelty, and pre-empts the "how is this different from [X]?" reviewer question.

## Keep it double-blind

ECAI is **double-blind**. Self-citations are the classic leak:

- Cite your own prior work **in the third person** ("Smith et al. [7] showed...") — never "in our
  previous work [7]."
- Do not let the density or phrasing of self-citations reveal the author group.
- Anonymize a system name that identifies you if it appears in the comparison.

```bash
# Catch first-person self-citation and identity leaks in related work
grep -nEi 'our (previous|prior|earlier) (work|paper|system|approach)|we previously' paper.tex | head
```

## Budget discipline

- The reference pages are **1 page** (standalone) or **2 pages** (IJCAI-ECAI 2026) — finite. Prune
  to the works that *position the contribution*, not every paper you read.
- Prefer the **canonical** citation for a well-known result over three secondary ones.
- Move an extended survey-style discussion to the **supplement** if it is not decision-critical
  (`ecai-supplementary`); keep the delta-establishing citations in the body.
- Do not pad the reference list to signal thoroughness — a broad reviewer notices citations that do
  no positioning work.

## Common failure modes

- **Home-subfield tunnel vision** — a planning paper that ignores the learning lane it competes
  with, or an ML paper blind to the symbolic literature it reinvents.
- **Bibliography, not positioning** — listing works without stating the delta.
- **First-person self-citation** breaking double-blind.
- **Missing the obvious neighbor** at IJCAI/AAAI/AAMAS/KR that a specialist reviewer will know by
  heart.
- **Reference-budget overflow** forcing body cuts (`ecai-submission`).

## Output format

```text
[Lanes covered] symbolic / learning / multi-agent / application / cross-venue — which apply, all present?
[Delta statements] each closest competitor -> one-sentence delta? gaps: <list>
[Double-blind] self-citations third-person; no identifying system names? yes/no
[Budget] reference pages within 1 (standalone) / 2 (2026); extended survey moved to supplement?
[Neighbor check] closest IJCAI/AAAI/AAMAS/KR result cited? yes/no
```
