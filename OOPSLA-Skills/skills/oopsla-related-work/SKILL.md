---
name: oopsla-related-work
description: Use when building an OOPSLA related-work section — positioning against the PACMPL family (POPL, PLDI, ICFP, OOPSLA itself) plus ECOOP, Onward!, and SE venues, citing journal-era OOPSLA papers in PACMPL volume/issue form, verifying every venue attribution on dblp, and stating per-line technical deltas.
---

# OOPSLA Related Work

OOPSLA sits inside a family that shares authors and reviewers: POPL, PLDI,
ICFP publish in the same PACMPL journal, ECOOP is the adjacent European OO
venue, Onward! shares the SPLASH building, and ICSE/FSE/ISSTA overlap on
empirical software questions — ISSTA was literally co-located with SPLASH
2026. The related-work section is therefore written for people who may have
*authored* the cited lines, and who will meet your paper again if a revision
round occurs. Two failure modes dominate: venue misattribution and
delta-free citation lists.

## Citation form in the journal era

Since OOPSLA became a PACMPL track, its papers are journal articles and must
be cited as such:

```bibtex
@article{belyakova2020worldage,
  author  = {Belyakova, Julia and Chung, Benjamin and Gelinas, Jack
             and Nash, Jameson and Tate, Ross and Vitek, Jan},
  title   = {World Age in Julia: Optimizing Method Dispatch
             in the Presence of Eval},
  journal = {Proc. ACM Program. Lang.},
  volume  = {4},
  number  = {OOPSLA},
  articleno = {207},
  year    = {2020},
  doi     = {10.1145/3428275}
}
```

Recent volumes split into OOPSLA1 and OOPSLA2 issues — preserve the issue
name (`number = {OOPSLA1}`) exactly as the ACM DL records it. Citing a PACMPL
article as "In OOPSLA '24" is the kind of sloppiness family reviewers notice
in their own papers' entries.

## Verification discipline

Every venue claim gets checked, not remembered:

| Check | Tool | What it catches |
| --- | --- | --- |
| dblp key (`conf/oopsla/` or `journals/pacmpl/`) | dblp search | PLDI/POPL/ECOOP results misfiled as OOPSLA (see the cut list in `resources/exemplars/library.md`) |
| DOI resolves to claimed venue | ACM DL | Preprint-vs-published divergence; wrong-year citations |
| Issue OOPSLA1 vs OOPSLA2 | ACM DL table of contents | Half-year attribution errors in recent work |
| Sibling series coverage | Per-venue dblp streams | The "we searched OOPSLA only" blind spot |

## Deltas, not inventories

The family's standard is one *technical difference* per cited line of work,
in the sentence where the citation appears:

- Weak: "Ownership types have been widely studied [3,7,12,19]."
- Strong: "[3] and [7] assume whole-program annotation; [12] recovers partial
  soundness but reports blame at the failure site rather than the boundary;
  we prove boundary blame is the weakest sound choice (§3)."

For concurrent work surfacing in the *other round of the same volume* — a
genuinely OOPSLA-specific situation — cite it, mark it concurrent, and state
the relationship without claiming priority; reviewer continuity means the
committee likely knows both papers.

## Coverage strategy

- Sweep the last three volumes of PACMPL Issues OOPSLA1/OOPSLA2, plus the
  matching POPL/PLDI/ICFP issues, before declaring novelty.
- Add ECOOP and the relevant SE venue (ICSE/FSE/ISSTA) whenever the claim is
  empirical or tooling-facing; add TOPLAS/JFP for journal-depth lines.
- Onward! papers are citable idea-stage precedents: acknowledging one
  costs nothing and omitting one your reviewer wrote costs a lot.
- Keep a claims-to-prior-work matrix in the repo; regenerate it at each
  round, because seven months pass between rounds and the family publishes
  continuously.

## Output format

```text
[Attribution audit] entries checked on dblp/DL: n/n, errors: <list>
[Citation form] PACMPL journal form used for post-2017 OOPSLA: yes/no
[Delta coverage] cited lines with explicit deltas: n/m + worst offenders
[Family sweep] OOPSLA/POPL/PLDI/ICFP/ECOOP/SE volumes covered
[Concurrent work] same-volume-round items flagged and handled
```
